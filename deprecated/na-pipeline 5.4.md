---
name: na-pipeline
description: Executes the Natural Areas Project pipeline after discovery — resolution, normalization, GPS acquisition, TSV output, and database upsert. Triggers on resolve, normalize, generate TSV, upsert, pipeline, or post-discovery processing.
---

# Natural Areas Project — Pipeline Skill v5.4

Executes all post-discovery pipeline stages: Resolution → GPS Acquisition → Normalization → TSV Output → Vocabulary Validation → TSV Integrity Check → Database Upsert.

**Prerequisite:** All 8 discovery tiers must be complete and the staging YAML must be finalized
before this skill is invoked. If discovery is still in progress, use the `na-discovery` skill.
See `processing/na_processing_orchestration.md` for the full pipeline stage reference and the stage-label cross-reference table.

## Pipeline Startup — Mandatory Read and Pre-Run Checks

Before writing any pipeline code or beginning any pipeline stage, read:

**`audit/na_audit_and_logging.md`** — Defines what must be logged at every stage of the run. Covers 14 "no silent X" rules governing corrections, exclusions, assumptions, conflicts, multi-entity splits, and normalization decisions. Provenance tables (`run_metadata`, `resolution_provenance`, `normalization_provenance`, `discovery_provenance`) must be populated during the run, not deferred. Failure to read this module before beginning means the session log, conflict log, correction log, and provenance tables will be incomplete or missing.

**Pre-run DB integrity check (IMP-101):** Before any pipeline writes, run:
```python
PRAGMA integrity_check   # → must return single row "ok"
PRAGMA foreign_key_check # → must return zero rows (or log any violations)
```
`na_run_county.py` runs this automatically via `check_db_integrity()` before invoking PipelineRunner. If running the pipeline manually, execute both PRAGMAs first. A non-"ok" result from `integrity_check` is a hard stop — do not proceed. FK violations are warnings (log and continue).

**State field rule (IMP-101):** The `run_metadata.state` field must always be the full state name (`"Ohio"`) — never a two-letter abbreviation (`"OH"`). The config loader in `na_run_county.py` rejects configs where `state` is a two-character uppercase string.

---

## Pipeline Overview

```
Raw Discovery Records (staging file)
        ↓
Stage 1a: Resolution Engine — Pass 1
        (grouping, identity matching, merge decisions, parent resolution)
        ↓
Stage 2: GPS Acquisition
        (2a: GPS fill-forward from DB for prior-run entities)
        (2b: Acquire GPS for entities with blank GPS)
        (2c: GPS Gate — Sites only: hold GPS-null sites without gps_unresolvable flag)
        ↓
Stage 1b: Resolution Engine — Pass 2 (Access Points only)
        (re-evaluate AP identity using GPS anchors and proximity buckets)
        ↓
Stage 2d: GPS Gate — APs only: hold GPS-null APs without gps_unresolvable flag
        ↓
Stage 3: Normalization Engine
        (3a: Read vocabulary modules FIRST)
        (3b: Normalize all fields)
        (3c: Map features_raw → controlled vocab features)
        ↓
Stage 4: TSV Output  (six files, one per entity type)
        ↓
Stage 4.5: Vocabulary Validation Gate  ← halts on any violation
        ↓
Stage 5: TSV Integrity Check
        ↓
Stage 5.5: Human Review Gate  ← pipeline halts; explicit confirmation required
        ↓
Stage 6: Database Upsert
```

## Stage 1a — Resolution Engine — Pass 1

### Mandatory Reads — Before Writing Any Resolution Code

- **`processing/na_resolution_engine.md`** — defines the five-phase resolution algorithm, merge strategies, conflict detection, anchor types, similarity thresholds, and provenance requirements.
- **`processing/na_resolution_rules.md`** — defines entity-type-specific identity rules, required anchors per type, scoring overrides, and known edge cases.

These are the authoritative source for all resolution behavior. Skipping them leads to incorrect merge decisions, missed conflicts, or wrong anchor priority — defects that are silent until a duplicate entity or wrong identity appears in the DB.

---

Transforms raw discovery records into resolved entities by detecting identity, merging duplicates, and preserving conflicts.

Five phases: grouping → identity matching → merge decisions → field-level merging → parent resolution. Resolution is purely mechanical — no normalization, no inference, no conflict resolution. All raw values preserved exactly. GPS is not required; APs may lack GPS after Pass 1.

**Output:** Partially resolved entities. Access Points may still lack GPS. Full algorithm, merge strategies, and threshold values are in `na_resolution_engine.md`.

## Stage 1b — Resolution Engine — Pass 2 (Access Points only)

Runs **after Stage 2c GPS Gate (Sites)** and **before Stage 2d GPS Gate (APs)**. Re-evaluates
Access Point identity using GPS data that was unavailable in Pass 1.

Re-evaluates AP identity using GPS anchors, proximity buckets, and parent context. May merge or split APs relative to Pass 1. Applies to Access Points only.

**Output:** Fully resolved entity layer — all entity types resolved, APs have GPS. See `na_resolution_engine.md` §STAGE 5.

## Stage 2 — GPS Acquisition

### Stage 2a — GPS Fill-Forward (IMP-031)

Before running GPS acquisition, check the DB for each entity being processed. If the DB record already has non-blank `gps_lat` and `gps_lon` from a prior pipeline run, carry those values forward without re-acquisition.

YAML GPS takes precedence over DB GPS; DB GPS fills forward when YAML is blank; both blank → Stage 2b. Preserves `gps_lat`, `gps_lon`, `plus_code`, `township`, `municipality`. See GPS Acquisition Module §3a for full fill-forward logic and provenance requirements.

### Stage 2b — GPS Acquisition

**Mandatory Read — Before Writing Any GPS Acquisition Code**

**`discovery/na_gps_acquisition.md`** — defines the full GPS acquisition workflow: confidence levels (`HIGH`/`MED`/`LOW`/`NONE`), Nominatim query formats, rural address fallback protocol, the fill-forward rule (IMP-031), the `gps_unresolvable` flag protocol (§7), county bounding box validation, and provenance field requirements. Column names and confidence semantics used downstream in normalization and the TSV output are defined here.

---

For every entity with blank GPS, attempt acquisition before TSV output. Priority: authoritative agency page → GIS layer (MORPC for covered counties) → geocoding → manual. Confidence levels: `HIGH`/`MED`/`LOW`/`NONE`. Round to 6 decimal places. Full acquisition workflow, MORPC protocol, and provenance requirements are in the GPS Acquisition Module §5.

See `discovery/na_gps_acquisition.md` §5.7–§5.8 for the Nominatim rural address fallback protocol and county bounding box sanity check (IMP-081), and §9.4 for the large-county timeout protocol and SQL repair path (IMP-083). These are required reading before writing Stage 2b code (see mandatory read gate above).

### Stage 2c — GPS Gate — Sites only (IMP-069)

**Runs after Stage 2b GPS Acquisition, before Stage 1b Resolution Pass 2. Applies to Sites only.**

Sites do not participate in Resolution Pass 2, so they can be gated here. Access Points are gated separately in Stage 2d after their identity is finalized by Pass 2.

No Site may proceed past this gate unless one of the following is true:

**A. GPS confirmed** — both `gps_lat` and `gps_lon` are non-null valid numerics.

**B. GPS explicitly flagged unresolvable** — the entity has `gps_unresolvable = true` in its normalization record, accompanied by a `notes` entry explaining why GPS cannot be obtained. See GPS Acquisition Module §7 for qualifying criteria and required documentation.

**If neither condition is met:**
- Route to `held_entities` with `hold_reason = "gps_missing"`
- Log: `"Entity [site_id] held: GPS null and gps_unresolvable not set. Entity must re-enter at Stage 2b before proceeding to normalization."`
- Entity is not rejected — it will be released when GPS is acquired in a subsequent run.

**`gps_unresolvable = true` Sites:**
- Excluded from Stage 2b acquisition workflow
- Pass this gate and proceed to TSV Output without GPS
- `plus_code`, `township`, `municipality` will be blank (no GPS → no GIS derivation)
- NOT written to `held_entities`
- Upserted to DB with null GPS and `gps_unresolvable = true` in normalization provenance

**Late-addition sites** must pass through Stage 2 (GPS Acquisition + GPS Gate) and Stage 3 (Normalization) before Stage 4 output. No direct DB injection is permitted.

Reference: Site Normalization Contract §5.17a; GPS Acquisition Module §7

### Stage 2d — GPS Gate — Access Points only (IMP-069)

**Runs after Stage 1b Resolution Pass 2, before Stage 3 Normalization. Applies to Access Points only.**

Access Points are gated here — after Pass 2 has had the opportunity to finalize their identity using GPS anchors and proximity data. Gating APs before Pass 2 (as was done in the single-gate design) would incorrectly hold APs whose GPS was valid but whose identity had not yet been resolved.

The same pass/hold rules apply as Stage 2c:

**A.** GPS confirmed — both `gps_lat` and `gps_lon` are non-null valid numerics → proceeds to normalization.

**B.** `gps_unresolvable = true` with documented reason → passes gate without GPS.

**If neither:** Route to `held_entities` with `hold_reason = "gps_missing"`. Log: `"Entity [ap_id] held: GPS null and gps_unresolvable not set."` Not rejected — released when GPS is acquired in a subsequent run.

Reference: Site Normalization Contract §5.17a; GPS Acquisition Module §7

## Stage 3 — Normalization Engine

Transforms resolved entities into normalized entities ready for TSV output and database upsert.

### 3a — Mandatory Reads Before Writing Any Normalization Code

Two groups of modules must be read before writing normalization logic. Read both groups every run — do not rely on memory of prior runs.

**Group 1 — Vocabulary modules (one per entity type; read all six every run):**

- `vocabularies/na_site_vocabulary.md` — category (18 values), subtype (category-dependent lists), designation, status, features, and §7.x normalization mapping tables
- `vocabularies/na_trail_vocabulary.md` — use type, surface type, origin type, status, difficulty
- `vocabularies/na_trail_segment_vocabulary.md` — segment type, surface type, difficulty
- `vocabularies/na_trail_network_vocabulary.md` — network type, status
- `vocabularies/na_site_network_vocabulary.md` — network type, status
- `vocabularies/na_access_point_vocabulary.md` — access point type, status

**Group 2 — Normalization contracts (one per entity type present in this run's entity set):**

| Entity type present | Read this contract |
|---|---|
| Sites | `normalization/na_site_normalization.md` |
| Trails | `normalization/na_trail_normalization.md` |
| Trail Segments | `normalization/na_trail_segment_normalization.md` |
| Trail Networks | `normalization/na_trail_network_normalization.md` |
| Site Networks | `normalization/na_site_network_normalization.md` |
| Access Points | `normalization/na_access_point_normalization.md` |

If any Site has a non-null `parent_site_id`, also read **`processing/na_child_site_rules.md`** — it governs inheritance rules, validation constraints, and hold conditions for child sites.

The normalization contracts define the full, authoritative field-by-field procedure for each entity type — including mandatory fields, conflict resolution logic, hold triggers, and provenance requirements. They are not paraphrased in this skill. Field-level decisions (what to do with a blank status, how to handle a conflicting subtype, when to halt normalization) are defined only in the contracts.

**Code imports**: All controlled vocabulary sets (ALLOWED_CATEGORIES, ALLOWED_SUBTYPES, ALLOWED_FEATURES, etc.) are codified in `utilities/na_vocab_constants.py`. Import from there rather than transcribing values manually into pipeline scripts. Reading the vocabulary markdown files is still required — the constants encode what values are allowed, but the §7.x normalization mapping tables (raw term → canonical value) live only in the markdown and are essential for normalization decisions.

This is not optional research — it is the source of truth for every controlled value the normalization code will assign. The failure mode when you skip this step is that you invent plausible-sounding values ("City Park", "Private Reserve", "Riparian", "Conservancy Preserve") that feel reasonable but are not in the vocabulary and will fail the Stage 4.5 gate. Every controlled field assignment must trace directly to a value found in one of these files.

Pay particular attention to:
- **§7.x normalization mappings in the site vocabulary** — the tables that map raw discovery terms to correct values (e.g., "Community Park" → "Neighborhood Park", "natural feature" → "Natural Area", "Wildlife Area" subtype → "State Wildlife Area"). These mappings exist precisely because discovery captures informal terms that need remapping.
- **Category-specific subtype lists (§3.2)** — subtypes are not global; each category has its own permitted list. A subtype valid for Nature Preserve is not valid for Park. If a raw subtype value is not in the list for that category, null it or apply the normalization mapping — never leave an out-of-vocabulary value in place.
- **IMP-065 subtype inference rules (§7.4)** — deterministic inference is permitted for Nature Preserve, Water Site, Recreation Facility, and Campground when subtype is blank after vocabulary validation.
- **IMP-063 FATAL REJECT rule** — any category value with no valid mapping must halt normalization for that entity, not silently pass through.

### 3b — Key Normalizations

Follow the normalization contract for each entity type (mandatory reads above). Key cross-cutting rules:
- **Plus Code**: use `from na_plus_code import encode_plus_code` — direct import only, never subprocess (see GPS Acquisition Module §5.6)
- **GPS county check (IMP-067)**: HIGH/MED confidence GPS cross-checked against county via TIGER COUSUB point-in-polygon; mismatch → `manual_review_queue` with `flag='county_mismatch'`; entity continues with existing counties value
- **IMP-063 FATAL REJECT**: any category value with no valid mapping halts normalization for that entity

### 3c — Features Normalization (Sites)

`features` is controlled vocabulary — map `features_raw` through `FEATURE_MAP` (see `utilities/na_feature_mapper_reference.md`), emit only matched canonical terms, leave unmatched text in `features_raw` only. Never pass free text through to the `features` TSV column. Per-entity field routing is defined in each entity's normalization contract.

### Held-Entity Child Rule (IMP-086)

After the held entities list is finalized during normalization, scan all child entities for parent references pointing to a held entity:

**Access Points:** Any access point whose `parent_entity_id` references a held entity is itself held — move it to `held_entities` with `hold_reason = "parent_held"`. The hold detail must reference the parent's `entity_id`.

```python
held_ids = {e["entity_id"] for e in held_entities}
for ap in access_points:
    if ap.get("parent_entity_id") in held_ids:
        held_entities.append({
            "record_id": ap["ap_id"],
            "entity_type": "Access Point",
            "name": ap["name"],
            "hold_reason": "parent_held",
            "hold_detail": f"Parent entity {ap['parent_entity_id']} is held pending cross-county resolution",
            "county": ap["county_primary"],
            "run_id": RUN_ID,
        })
        access_points.remove(ap)
```

**Child Sites:** Any child site whose `parent_site_id` references a held site is itself held — move it to `held_entities` with `hold_reason = "parent_held"`.

**Trail Networks:** `member_trail_ids` referencing held trails remain in the network record (the network is not held). Log as `INFO` — the dangling member reference will resolve when the cross-county run completes. Do not log as `WARNING`.


## Stage 4 — TSV Output

### Mandatory Reads — Before Writing TSV Output Code

Read the output spec for each entity type present in this run's normalized entity set:

| Entity type present | Read this output spec |
|---|---|
| Sites | `output/na_tsv_output_site.md` |
| Trails | `output/na_tsv_output_trail.md` |
| Trail Segments | `output/na_tsv_output_trail_segment.md` |
| Trail Networks | `output/na_tsv_output_trail_network.md` |
| Site Networks | `output/na_tsv_output_site_network.md` |
| Access Points | `output/na_tsv_output_access_point.md` |

The output specs define the authoritative column order, column names, and encoding rules for each TSV file. Column order is significant — downstream importers rely on fixed column positions. The spec also defines which fields are DB-only (must be excluded from TSV) and which are TSV-only.

---

Write six TSV files, one per entity type. Files with zero entities still get written (header row only).

Sites TSV columns: `name, category, subtype, designation, status, ownership, governance, partner_agencies, coordination, description, location, acres, counties, municipality, township, gps_lat, gps_lon, plus_code, features, notes, url_primary, urls, parent_site_id, created_at, updated_at`

Note: `site_id` and `features_raw` are DB-only — they do not appear in the TSV.

## Stage 4.5 — Vocabulary Validation Gate

**Halts the pipeline on any violation.** Must validate ALL of the following:
- Every `category` value is in the 18-value site vocabulary §2.1 list
- Every `subtype` value is in the permitted list for its category (§3.2)
- Every `designation` value is in the designation vocabulary (§4.x)
- Every `status` value is in the status vocabulary (§5)
- **Every `features` value is in the §6.2 allowed features list** ← gap identified Fulton County 2026-04-13: this check was missing and 18 violations passed undetected. Always include this check.

```python
for site in sites:
    for term in site["features"].split(";"):
        term = term.strip()
        if term and term not in ALLOWED_FEATURES:
            raise ValueError(f"Invalid features term: '{term}' on {site['site_id']}")
```

## Stage 5 — TSV Integrity Check

Non-halting; log warnings for review:
- Sites with GPS: report count and names of any missing GPS
- All `parent_site_id` references resolve to a known `site_id` in this run or the DB
- No duplicate entity IDs within run
- Held entities: confirm each HELD_ID has a corresponding held_entities record

## Stage 5.5 — Human Review Gate

**The pipeline halts here. Do not proceed to Stage 6 until a human has reviewed the TSV files and confirmed.**

Open the six TSV files and verify:
- Entity counts look reasonable for this county (no unexpected zeros or inflated counts)
- Category and subtype assignments are substantively correct — not just vocabulary-valid
- Any GPS coordinates that were newly acquired look plausible (spot-check a few against a map)
- Held entities are expected — no surprises in what was held or why

To confirm review and proceed, the user must explicitly say something like "TSV looks good, proceed with upsert" or equivalent. Do not interpret silence, a re-run of this skill, or any automated signal as confirmation.

Record the reviewer and confirmation in the session log Errors and Fixes table (or a dedicated Review sign-off row) before running Stage 6.

## Stage 6 — Database Upsert

### Required DDL Table Groups (IMP-087)

Every generated upsert script must include `CREATE TABLE IF NOT EXISTS` DDL for all three table groups, not just primary entity tables. A missing table group causes schema conformance failure post-upsert.

**Primary entity tables** (already standard):
`sites`, `trails`, `trail_segments`, `trail_networks`, `site_networks`, `access_points`

**Relationship tables** — required in every script:
`site_parent`, `trail_parents`, `trail_to_segment`, `trail_network_members`, `site_network_members`, `access_point_parents`

**Operational tables** — required in every script:
`held_entities`, `manual_review_queue`, `entity_conflicts`, `entity_uncertainty`, `entity_geometry`

**Provenance tables** — required in every script:
`run_metadata`, `discovery_provenance`, `resolution_provenance`, `normalization_provenance`

Provenance logging must populate these tables during the run — do not defer provenance writes to a post-run step.

---

Upsert all entities into `natural_areas_v5.db` using `ON CONFLICT DO UPDATE`.

**Correct DB schema column names** — verified against live DB 2026-04-13; use these exactly:

`run_metadata`:
```python
INSERT OR IGNORE INTO run_metadata
  (run_id, county, state, run_date, records_input, normalized, held, notes, created_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
```

`held_entities`:
```python
INSERT OR IGNORE INTO held_entities
  (record_id, entity_type, name, hold_reason, hold_detail, county, run_id, created_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
```

> ⚠️ Do not use `pipeline_version`, `entity_id`, or `entity_name` — these columns do not exist in the live schema.

## Canonical Feature Mapper

Use `utilities/na_feature_mapper_reference.md` as the starting point for every county pipeline. Copy the `FEATURE_MAP` list into the county script and extend with county-specific patterns as needed. Do not transcribe the map from memory — load it from the reference file.

Note: `features_raw` terms with no vocabulary equivalent (e.g., Concession Stand, Dump Station, Water Frontage) are documented in the reference file and must remain in `features_raw` only.

## Session Log Updates

Update `{county}_{state}_session_log.md` (see `na_session_log_template_v1.md`) as the pipeline runs:

- **After Stage 2b (GPS Acquisition)**: Fill in `gps_acquired`, `gps_high`, `gps_med`, `gps_low`, `gps_none`. Record any Nominatim failures, bounding box rejections, or timeout events in the Errors and Fixes table.
- **After Stage 3 (Normalization)**: Fill in `records_normalized`, `records_held`, and the held entities table. Record any vocabulary violations or FATAL REJECT events in the Errors and Fixes table.
- **After Stage 4 (TSV Output)**: Note TSV file counts per entity type.
- **After Stage 4.5 (Vocabulary Validation Gate)**: Record any gate halts and the specific violations that triggered them.
- **After Stage 5.5 (Human Review Gate)**: Record reviewer name/initials and confirmation statement in the session log before proceeding to Stage 6.
- **After Stage 6 (Database Upsert)**: Fill in `records_upserted`. Confirm run_metadata row written. Note any schema errors.

---
# END OF NA_PIPELINE_SKILL
