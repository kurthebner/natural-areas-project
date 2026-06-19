---
name: na-pipeline
description: Executes the Natural Areas Project v6 pipeline after discovery — resolution, normalization, GPS acquisition, TSV output, and database upsert. Triggers on resolve, normalize, generate TSV, upsert, pipeline, or post-discovery processing.
---

# Natural Areas Project — Pipeline Skill v6.0

Executes all post-discovery pipeline stages: Resolution → GPS Acquisition → Normalization → TSV Output → Vocabulary Validation → TSV Integrity Check → Database Upsert.

**Prerequisite:** All 8 discovery tiers must be complete and the staging YAML must be finalized before this skill is invoked. See `processing/na_processing_orchestration_v6.0.md` for the full pipeline stage reference.

## Pipeline Startup — Mandatory Read

Before writing any pipeline code or beginning any pipeline stage, read:

**`audit/na_audit_and_logging_v6.0.md`** — Defines what must be logged at every stage. Provenance tables (`run_metadata`, `resolution_provenance`, `normalization_provenance`, `discovery_provenance`) must be populated during the run, not deferred.

---

## Pipeline Overview

```
Raw Discovery Records (staging file)
        ↓
Stage 3: Resolution Engine (single pass)
        (grouping, identity matching, merge decisions, parent resolution)
        (no GPS required; no second pass)
        ↓
Stage 4a: GPS Fill-Forward (IMP-031)
        (carry forward GPS from prior runs)
        ↓
Stage 4b: GPS Acquisition (single pass — all four entity types)
        (browser, GIS layers, geocoding, human assist)
        ↓
Stage 4c: GPS Gate — Sites and APs only
        (gps_missing → held_entities; Trailthings and Site Networks not gated)
        ↓
Stage 5: Normalization Engine
        (5a: read vocabulary modules FIRST)
        (5b: normalize all fields)
        (5c: map features_raw → controlled vocab)
        ↓
Stage 6: TSV Output (four files)
        ↓
Stage 6.5: Vocabulary Validation Gate ← halts on any violation
        ↓
Stage 7: TSV Integrity Check
        ↓
Stage 7.5: Human Review Gate ← pipeline halts; explicit confirmation required
        ↓
Stage 8: Database Upsert
```

## Stage 3 — Resolution Engine (Single Pass)

### Mandatory Reads — Before Writing Any Resolution Code

- **`processing/na_resolution_engine_v6.0.md`** — five-phase algorithm, merge strategies, conflict detection, anchor types, similarity thresholds, provenance requirements
- **`processing/na_resolution_rules_v6.0.md`** — entity-type-specific identity rules, scoring overrides, known edge cases

---

Resolution transforms raw discovery records into resolved entities. Single pass — there is no Pass 2 for Access Points. GPS is not required for resolution; AP identity in v6 uses parent entity ID + name + county, not GPS proximity.

Five phases: grouping → identity matching → merge decisions → field-level merging → parent resolution.

**Phase 0 (MC candidate detection)**: Before Phase 1, scan all records for `CROSS_COUNTY_CANDIDATE`, `COLLISION:{id}`, or `KNOWN_MC:{id}` flags. Handle per `processing/na_cross_county_resolution_v6.0.md` §7.1.

**Output:** Fully resolved entities for all four types.

## Stage 4a — GPS Fill-Forward (IMP-031)

Before running GPS acquisition, check the DB for each entity. If the DB record already has non-blank `gps_lat` and `gps_lon` from a prior run, carry those values forward.

YAML GPS > DB GPS (fill-forward) > blank → Stage 4b.
Preserved: `gps_lat`, `gps_lon`, `plus_code`, `township`, `municipality`.

## Stage 4b — GPS Acquisition (Single Pass)

### Mandatory Read — Before Writing Any GPS Acquisition Code

**`discovery/na_gps_acquisition_v6.0.md`** — full acquisition workflow, ranked methods, browser protocol, Nominatim fallback, county bounding box check, `gps_unresolvable` flag criteria, provenance requirements.

---

Single pass covering all four entity types. Priority targets: Sites and APs (GPS Gate applies). Trailthings and Site Networks: GPS optional; most are `gps_unresolvable`.

**Ranked acquisition methods** (stop at first success):
1. Authoritative source page (stated coordinates)
2. Authoritative GIS download (MORPC for covered counties, ODNR Lake Map, SORP)
3. Browser — Claude in Chrome (Google Maps, ArcGIS viewers, county GIS portals)
4. Address geocoding — Nominatim with rural fallback protocol (§5.7) and county bounding box check (§5.8)
5. OSM / public map lookup
6. Human assist
7. Declare `gps_unresolvable`

**Plus Code**: `from na_plus_code import encode_plus_code` — direct import only, never subprocess.

## Stage 4c — GPS Gate

**Applies to: Sites and Access Points only.**
Trailthings and Site Networks are not gated — `gps_unresolvable` is the expected state for most.

A Site or AP passes if:
- `gps_lat` and `gps_lon` are both non-null, OR
- `gps_unresolvable = true` is set and documented

If neither: route to `held_entities` with `hold_reason = "gps_missing"`.

`gps_unresolvable = true` entities:
- Pass this gate without GPS
- `plus_code`, `township`, `municipality` will be blank
- NOT written to `held_entities`
- Upserted to DB with null GPS and `gps_unresolvable = true` in normalization provenance

## Stage 5 — Normalization Engine

### 5a — Mandatory Reads Before Writing Any Normalization Code

**Vocabulary modules (read all four every run):**
- `vocabularies/na_site_vocabulary.md`
- `vocabularies/na_trailthing_vocabulary.md`
- `vocabularies/na_site_network_vocabulary.md`
- `vocabularies/na_access_point_vocabulary.md`

**Normalization contracts (read for each entity type present):**

| Entity type present | Read this contract |
|---|---|
| Sites | `normalization/na_site_normalization.md` |
| Trailthings | `normalization/na_trailthing_normalization.md` |
| Site Networks | `normalization/na_site_network_normalization.md` |
| Access Points | `normalization/na_access_point_normalization.md` |

If any Site has a non-null `parent_site_id`, also read **`processing/na_child_site_rules_v6.0.md`**.

**Code imports**: Controlled vocabulary sets are in `utilities/na_vocab_constants_v6.py` (v6 utilities folder). Reading the markdown vocabulary files is still required — the constants encode allowed values, but normalization mapping tables live only in the markdown.

### 5b — Key Normalizations

- **Plus Code**: direct import only — `from na_plus_code import encode_plus_code`
- **GPS county check (IMP-067)**: GPS cross-checked against county via TIGER COUSUB; mismatch → `manual_review_queue` with `flag='county_mismatch'`
- **IMP-063 FATAL REJECT**: any category value with no valid mapping halts normalization for that entity
- **source_term / source_hierarchy_context**: pass through verbatim — never normalize or map to controlled vocabulary
- **habitat_type**: open vocabulary — pass through verbatim; no mapping applied

### 5c — Features Normalization (Sites and APs)

`features` is controlled vocabulary — map `features_raw` through `FEATURE_MAP` (see `utilities/na_feature_mapper_reference.md`). Emit only matched canonical terms. Never pass free text to the `features` TSV column.

### Held-Entity Child Rule (IMP-086)

After the held entities list is finalized, scan all child entities:

**Access Points:** Any AP whose `parent_entity_id` references a held entity → held with `hold_reason = "parent_held"`.

**Child Sites:** Any child site whose `parent_site_id` references a held site → held with `hold_reason = "parent_held"`.

**Trailthings with parent_id:** Any Trailthing whose `parent_id` references a held Trailthing → held with `hold_reason = "parent_held"`.

**Site Networks:** `member_site_ids` referencing held Sites → network is NOT automatically held. Log as INFO.

## Stage 6 — TSV Output

### Mandatory Reads — Before Writing TSV Output Code

| Entity type present | Read this output spec |
|---|---|
| Sites | `output/na_tsv_output_site_v6.0.md` |
| Trailthings | `output/na_tsv_output_trailthing_v6.0.md` |
| Site Networks | `output/na_tsv_output_site_network_v6.0.md` |
| Access Points | `output/na_tsv_output_access_point_v6.0.md` |

---

Write four TSV files, one per entity type. Files with zero entities still get written (header row only).

**Held entity exclusion (IMP-113):** Held entities must not appear in any entity TSV file.

**Cross-entity name pairing rule**: Every field that references another entity by ID must be immediately followed by a field containing that entity's human-readable name.

**Vocabulary expansion candidates**: Surface any `unmapped_token_dropped` records from normalization provenance as an informational list — non-blocking.

## Stage 6.5 — Vocabulary Validation Gate

**Halts the pipeline on any violation.** Validate ALL of the following:
- Every `category` value is in the Site vocabulary
- Every `subtype` value is in the permitted list for its category
- Every `designation` value is in the designation vocabulary
- Every `status` value is in the status vocabulary
- Every `features` value is in the allowed features list
- Every Trailthing `use_type`, `surface_type`, `origin_type`, `status`, `difficulty` value is in the Trailthing vocabulary
- Every Site Network `network_type`, `org_type`, `status` value is in the Site Network vocabulary
- Every Access Point `ap_type`, `status` value is in the AP vocabulary

## Stage 7 — TSV Integrity Check

Non-halting; log warnings for review. Read `output/na_tsv_integrity_check_v6.0.md` for field position anchors and delimiter requirements.

**Delimiter requirements (exact):**

| Entity Type | Fields | Tabs Required |
|---|---|---|
| Site | 31 | 30 |
| Trailthing | 31 | 30 |
| Site Network | 18 | 17 |
| Access Point | 20 | 19 |

## Stage 7.5 — Human Review Gate

**The pipeline halts here. Do not proceed to Stage 8 until a human has reviewed and confirmed.**

Open the four TSV files and verify:
- Entity counts look reasonable (no unexpected zeros or inflated counts)
- Category and subtype assignments are substantively correct
- Any newly acquired GPS coordinates look plausible (spot-check against a map)
- Held entities are expected — no surprises in what was held or why
- **AP-to-Site reclassification check (IMP-114):** Any AP with `acres_raw`, `description_raw`, and governance distinct from parent Trailthing → candidate for reclassification. See AP Normalization Contract §10a.
- Vocabulary expansion candidates reviewed

To confirm and proceed, the user must explicitly confirm. Silence is not confirmation.

## Stage 8 — Database Upsert

### Pre-Upsert MC County Format Scan (IMP-115)

```sql
SELECT entity_id, counties FROM trailthings  WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
SELECT entity_id, counties FROM sites        WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
SELECT entity_id, counties FROM site_networks WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
```

Canonical format: `"Ottawa;Wood"` — semicolon-delimited, no spaces, alphabetical order.

### Required DDL Table Groups (IMP-087)

Every upsert script must include `CREATE TABLE IF NOT EXISTS` for all four groups:

**Primary entity tables**: `sites`, `trailthings`, `site_networks`, `access_points`
(plus legacy: `trails`, `trail_segments`, `trail_networks`)

**Relationship tables**: `site_parent`, `trailthing_hierarchy`, `site_network_members`, `access_point_parents`
(plus legacy: `trail_to_segment`, `trail_network_members`, `trail_parents`)

**Operational tables**: `held_entities`, `manual_review_queue`, `entity_conflicts`, `entity_uncertainty`, `entity_geometry`

**Provenance tables**: `run_metadata`, `discovery_provenance`, `resolution_provenance`, `normalization_provenance`

### Correct DB Schema Column Names

`run_metadata` INSERT:
```python
INSERT OR IGNORE INTO run_metadata
  (run_id, county, state, run_date, records_input, normalized, held, notes, created_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
```
`state` must be full name ("Ohio") — NOT abbreviation ("OH"). Do NOT use `pipeline_version`, `entity_id`, or `entity_name`.

`resolution_provenance` columns: `(prov_id, entity_id, entity_type, county, resolution_run, notes, run_id, created_at)`
— use `resolution_run`, NOT `resolution_action`.

## Canonical Feature Mapper

Use `utilities/na_feature_mapper_reference.md` (v6 utilities folder) as the starting point for every county pipeline. Copy the `FEATURE_MAP` list into the county script and extend with county-specific patterns as needed. Do not transcribe from memory.

## File Writing Rules (IMP-106)

**Never use bash heredocs to write pipeline scripts or any file longer than ~30 lines.**

| Operation | Correct tool |
|---|---|
| New file or complete rewrite | `Write` tool |
| Targeted change to existing file | `Edit` tool |
| Key-targeted YAML append (IMP-079) | Python `yaml.safe_load` / `yaml.dump` via bash |

Mandatory syntax verification after every script write:
```bash
python -m py_compile path/to/script.py && echo "OK"
```

---
# END OF NA_PIPELINE_SKILL
