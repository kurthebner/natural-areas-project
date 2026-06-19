# NATURAL AREAS PROJECT
# PROCESSING ORCHESTRATION MODULE v6.0
Authoritative End-to-End Execution Pipeline for the v6.x Architecture

This module supersedes Processing Orchestration Module v5.5.

------------------------------------------------------------
# CHANGES FROM v5.5 → v6.0

- **Entity types updated throughout**: Six entity types (Site, Trail, Trail Segment,
  Trail Network, Site Network, Access Point) → four (Site, Trailthing, Site Network,
  Access Point). TSV output updated to four files.

- **Resolution Pass 2 eliminated**: v5.5 ran a second resolution pass for Access
  Points after GPS acquisition, because AP identity used GPS proximity as an anchor.
  In v6.x, AP identity is anchored by name + governance + county + parent entity ID.
  GPS proximity is not an identity anchor. Resolution runs once. GPS acquisition
  follows resolution with no feedback loop.

- **Two GPS gates collapsed into one**: v5.5 had a GPS Gate for Sites before Pass 2
  and a GPS Gate for APs after Pass 2. With Pass 2 eliminated, a single GPS Gate
  runs after GPS acquisition, covering all entity types that require GPS (Sites and
  APs). Trailthings and Site Networks are not gated — they are typically
  gps_unresolvable and proceed without GPS.

- **GPS Acquisition updated**: Single pass covering all four entity types. Browser
  (Claude in Chrome) is a named primary method. Human assist is explicit and
  first-class. See GPS Acquisition Module v6.0.

- **Pipeline coding conventions carried forward** (§12, IMP-106): Write tool
  required for all file writes >30 lines; bash heredocs prohibited.

- **IMP-PENDING — Skill label cross-reference validation**: The pipeline summary
  table (§5) includes na-pipeline skill stage labels carried forward from v5.5.
  These should be validated against the current na-pipeline skill after the v6.x
  skills are finalized to confirm no divergence has accumulated. Tracked as an
  open improvement item pending skill stabilization.

- **All v5.5 core principles carried forward**: Discovery = Collection, Resolution =
  Identity, GPS Acquisition = Coordinate Collection, Normalization = Decisions,
  Upsert = Persistence.

------------------------------------------------------------
# 1. PURPOSE

The Processing Orchestration Module v6.0 defines the authoritative, deterministic,
multi-stage pipeline that transforms raw discovery outputs into fully resolved,
normalized, GIS-enhanced, audit-ready datasets for all four v6.x entity types:

- Site
- Trailthing
- Site Network
- Access Point

This module governs:

- The order of execution for all v6.x modules
- How raw discovery values flow through resolution, GPS acquisition, normalization,
  and upsert
- How conflicts, lineage, and metadata are preserved
- How deterministic, reproducible processing is enforced
- How final TSV outputs are validated and packaged

This module contains **no vocabularies** and **no schema**. It orchestrates modules
that do.

------------------------------------------------------------
# 2. CORE PRINCIPLES

### 2.1 Discovery = Collection
Discovery collects raw values only. No normalization, inference, GPS validation,
or GIS derivation occurs.

### 2.2 Resolution = Identity
Resolution applies identity anchors and signatures, forms merge clusters, preserves
conflicts, and resolves parent names to IDs. It does not normalize or infer. It runs
once — there is no second pass.

### 2.3 GPS Acquisition = Coordinate Collection
GPS Acquisition obtains missing GPS coordinates for Sites and Access Points (and
optionally Trailthings and Site Networks) and records provenance. It does not
validate or normalize GPS. It runs as a single pass after Resolution with no
feedback loop into identity.

### 2.4 Normalization = Decisions
Normalization validates GPS, computes Plus Codes, performs GIS lookup, applies
vocabularies, validates parent/child relationships, and produces normalized entities.

### 2.5 Upsert = Persistence
Upsert writes normalized entities into the database.

------------------------------------------------------------
# 3. MODULE HIERARCHY AND AUTHORITY

The following hierarchy governs all v6.x processing:

1.  Schema Modules v6.x
2.  Vocabulary Modules v6.x
3.  Discovery Protocol Module v6.x
4.  Discovery Orchestration Module v6.x
5.  Discovery Metadata Specification v6.x
6.  Resolution Rules Module v6.x
7.  Resolution Engine v6.x
8.  GPS Acquisition Module v6.x
9.  Normalization Engine v6.x
10. Child Site Rules Module v6.x
11. Entity Upsert Engine v6.x
12. TSV Output Specifications v6.x
13. TSV Integrity Check Module v6.x
14. Audit & Logging Module v6.x

Authority rules:

- Schema defines ontology and normalized field definitions
- Discovery collects raw values
- Resolution determines identity and merges raw values (single pass)
- GPS Acquisition collects missing coordinates (single pass, no identity feedback)
- Normalization applies vocabularies, GIS, formatting, and validation
- Upsert writes entities into the database
- TSV Output serializes normalized entities
- TSV Integrity Check overrides TSV Output on format issues
- Audit & Logging records all actions

------------------------------------------------------------
# 4. END-TO-END PIPELINE (v6.x)

The v6.x pipeline consists of **ten deterministic stages**.

------------------------------------------------------------
# STAGE 0 — MODULE AVAILABILITY CHECK

**Entry condition:** All 8 discovery tiers are complete. The staging YAML
(`{county}_{state}_raw_discovery.yaml`) is finalized and the handoff document
is set to `DISCOVERY COMPLETE — PIPELINE READY`. If discovery is not yet
complete, return to the na-discovery skill.

Verify all required v6.x modules are available.
If any module is missing, halt processing and identify the missing module.

**Output:** Verified v6.x module environment.

------------------------------------------------------------
# STAGE 1 — RUN DISCOVERY (TIERS 1–8)

Discovery collects raw values only.

Rules:

- No normalization
- No inference
- No GPS validation
- No GIS lookup
- No parent assignment
- All values stored as `_raw`
- Township and municipality must remain blank
- Trailthings: capture `source_term_raw` and `source_hierarchy_context_raw`
  verbatim; do not classify as trail vs. trail network vs. trail segment

**Output:** Raw Discovery Layer v6.x.

------------------------------------------------------------
# STAGE 2 — LOAD COUNTY BASELINE (TIER-0)

Baseline loads after discovery.

Rules:

- Load baseline rows exactly as written
- Mark `seeded_from_baseline = true`
- Assign a `baseline_id` per row
- Preserve all raw values
- Do not populate township or municipality
- Trail-type baseline rows seed as Trailthings (County Baseline Module v6.x §7.8)
- Baseline entries that cannot be confirmed during discovery are held with
  `hold_reason = "unconfirmed_baseline_seed"` at resolution time

**Output:** Baseline seed layer.

------------------------------------------------------------
# STAGE 3 — RESOLUTION ENGINE v6.x

Resolution performs:

- Grouping
- Identity anchor evaluation
- Similarity scoring
- Merge cluster formation
- Conflict preservation
- Parent name → ID resolution
- Lineage preservation
- Unconfirmed baseline seed identification → `held_entities`

**GPS is not required for resolution.** AP identity in v6.x is anchored by
name + governance + county + parent entity ID — not GPS proximity. There is
no second resolution pass.

**Output:** Fully resolved entities for all four entity types.

------------------------------------------------------------
# STAGE 4a — GPS FILL-FORWARD (IMP-031)

Before running GPS acquisition, check the database for each entity being
processed. If the DB record already has non-blank `gps_lat` and `gps_lon`
from a prior pipeline run, carry those values forward without re-acquisition.

Precedence: source-stated GPS > DB GPS (fill-forward) > blank → Stage 4b.

Preserved fields: `gps_lat`, `gps_lon`, `plus_code`, `township`, `municipality`.

**Output:** Entities with GPS carried forward from prior runs where applicable.

------------------------------------------------------------
# STAGE 4b — GPS ACQUISITION MODULE v6.x

GPS Acquisition obtains missing coordinates in a **single pass covering all
four entity types**.

Priority targets:
- **Sites** — GPS required for upsert (GPS Gate applies)
- **Access Points** — GPS required for upsert (GPS Gate applies)
- **Trailthings** — GPS optional; most are gps_unresolvable (linear corridors)
- **Site Networks** — GPS optional; most are gps_unresolvable (multi-location)

Acquisition methods (ranked — see GPS Acquisition Module v6.x §5):
1. Authoritative source page
2. Authoritative GIS download (MORPC, ODNR Lake Map, SORP)
3. Browser-assisted lookup (Claude in Chrome — Google Maps, ArcGIS viewers)
4. Address geocoding (Nominatim with rural fallback protocol)
5. OSM / public map lookup
6. Human-assisted acquisition
7. Declare gps_unresolvable

Rules:
- Acquire GPS from authoritative sources
- Verify plausibility (county bounding box, parent context for APs)
- Record GPS provenance for every entity processed
- Do not normalize or validate GPS
- Do not compute Plus Codes
- Do not perform GIS lookup

**Output:** Entities with updated `gps_lat_raw` / `gps_lon_raw` and GPS
provenance records.

------------------------------------------------------------
# STAGE 4c — GPS GATE (ALL ENTITY TYPES)

After GPS acquisition, every Site and Access Point must pass the GPS Gate
before proceeding to normalization.

**An entity passes if:**
- `gps_lat` and `gps_lon` are both non-null, OR
- `gps_unresolvable = true` is set and documented

**An entity fails if:**
- GPS is null AND `gps_unresolvable` is not set

**On failure:**
- Route to `held_entities` with `hold_reason = "gps_missing"`
- Log: `"Entity [id] held: GPS null and gps_unresolvable not set."`
- Entity will be released when GPS is acquired in a subsequent run

**GPS Gate applies to:** Sites and Access Points
**GPS Gate does not apply to:** Trailthings and Site Networks (gps_unresolvable
is the expected state for most; if GPS is present, it flows through normally)

**`gps_unresolvable = true` entities:** Pass this gate and proceed to
normalization without coordinates. `plus_code`, `township`, and `municipality`
will be blank.

**Output:** GPS-null Sites and APs (without `gps_unresolvable`) written to
`held_entities`; all remaining entities proceed to normalization.

------------------------------------------------------------
# STAGE 5 — NORMALIZATION ENGINE v6.x

Normalization performs:

- Schema validation
- Vocabulary normalization
- Formatting normalization
- GPS validation → numeric `gps_lat`, `gps_lon`
- Plus Code computation
- GIS spatial lookup → township, municipality
- Integrity anchor validation and dedup check
- Parent/child validation (Child Site Rules v6.x)
- Trailthing parent hierarchy validation
- `source_term` and `source_hierarchy_context` pass-through (verbatim — not
  normalized or mapped)

Normalization does **not** merge conflicts or infer identity.

**Output:** Four normalized datasets (Sites, Trailthings, Site Networks,
Access Points).

------------------------------------------------------------
# STAGE 6 — GENERATE TSV OUTPUT (v6.x)

Generate four TSV files from normalized entities **before** database upsert:

- Sites.tsv
- Trailthings.tsv
- Site_Networks.tsv
- Access_Points.tsv

Rules:

- Tab-delimited
- UTF-8
- No embedded tabs or newlines
- Arrays → semicolon-delimited
- Held entities are excluded from all TSV files — they appear only in
  `held_entities` table
- Column order must match the authoritative TSV Output Specification for each
  entity type exactly

**Output:** TSV dataset bundle (four files).

------------------------------------------------------------
# STAGE 6.5 — VOCABULARY VALIDATION GATE (v6.x)

Validate all vocabulary-governed fields in each TSV against the authoritative
Vocabulary Modules v6.x. **Halts the pipeline on any violation** — no upsert
may proceed until all TSVs pass.

Validates per entity type:
- **Sites**: category, subtype, designation, status, features
- **Trailthings**: use_type, surface_type, origin_type, status, difficulty
- **Site Networks**: network_type, org_type, status
- **Access Points**: ap_type, status

Also surfaces vocabulary expansion candidates: any token logged as
`unmapped_token_dropped` in normalization provenance should appear as an
informational list at this stage (non-blocking).

**Output:** Vocabulary-validated TSVs, or pipeline halt with violation report.

------------------------------------------------------------
# STAGE 7 — TSV INTEGRITY CHECK (v6.x)

Validate:

- Delimiter count per entity type (Sites: 30 tabs; Trailthings: 30 tabs;
  Site Networks: 17 tabs; Access Points: 19 tabs)
- Field alignment
- Blank-field representation
- County formatting
- Cross-entity reference pairing: every ID field must be paired with the
  referenced entity's human-readable name field

If integrity fails, halt finalization.

**Output:** Integrity-validated TSVs.

------------------------------------------------------------
# STAGE 7.5 — HUMAN REVIEW GATE

**The pipeline halts here. Do not proceed to Stage 8 until a human has
reviewed the TSV files and explicitly confirmed.**

The reviewer opens the four TSV files and verifies:

- Entity counts look reasonable for this county (no unexpected zeros or
  inflated counts)
- Category and subtype assignments are substantively correct — not just
  vocabulary-valid
- Any GPS coordinates that were newly acquired look plausible (spot-check
  against a map)
- Held entities are expected — no surprises in what was held or why
- AP-to-Site reclassification candidates (IMP-114): any AP with `acres_raw`
  populated, `description_raw` present, and governance distinct from parent
  Trailthing → review for reclassification
- Vocabulary expansion candidates surfaced at Stage 6.5 — review for addition
  to the relevant Vocabulary Module

To confirm review and proceed, the user must explicitly confirm (e.g., "TSV
looks good, proceed with upsert"). Silence, a skill re-run, or any automated
signal is not confirmation.

Record the reviewer and confirmation statement in the session log before
Stage 8.

**Output:** Human-confirmed TSV bundle, ready for upsert.

------------------------------------------------------------
# STAGE 8 — ENTITY UPSERT ENGINE v6.x

**Pre-upsert MC county format scan (IMP-115):** Before running the upsert
script, query for malformed county fields on MC entities:

```sql
SELECT entity_id, counties FROM trailthings    WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
SELECT entity_id, counties FROM sites          WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
SELECT entity_id, counties FROM site_networks  WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
```

Canonical format: `"Ottawa;Wood"` — semicolon-delimited, no spaces, alphabetical
order. Correct any violations before proceeding.

Upsert:

- Inserts or updates entities in the database (ON CONFLICT DO UPDATE)
- Maintains stable IDs
- Writes relationship tables
- Writes provenance tables
- Processes held entity release workflow

Required DDL table groups — every upsert script must include
`CREATE TABLE IF NOT EXISTS` for:
- **Primary entity tables**: `sites`, `trailthings`, `site_networks`,
  `access_points`
- **Relationship tables**: `site_parent`, `trailthing_hierarchy`,
  `site_network_members`, `access_point_parents`
- **Operational tables**: `held_entities`, `manual_review_queue`,
  `entity_conflicts`, `entity_uncertainty`, `entity_geometry`
- **Provenance tables**: `run_metadata`, `discovery_provenance`,
  `resolution_provenance`, `normalization_provenance`

**Output:** Updated database.

------------------------------------------------------------
# STAGE 9 — RELATIONSHIP VALIDATION (CROSS-ENTITY)

Validate:

- Site → Parent Site (child site relationships)
- Trailthing → Parent Trailthing (hierarchy relationships)
- Trailthing → Site Parent (site_parent_id references)
- Trailthing → Parent Site Network (site_network membership via parent_site_network_id)
- Site → Site Network (site_network_members)
- Access Point → Site or Trailthing (access_point_parents)

**Output:** Relationship-validated dataset.

------------------------------------------------------------
# STAGE 10 — FINAL OUTPUT BUNDLE

Package:

- Four TSVs
- Audit logs
- Metadata (module versions, timestamps)
- Discovery summary
- Document log (`{county}_document_log.yaml`)

**Output:** County Output Bundle v6.0.

------------------------------------------------------------
# 5. PIPELINE SUMMARY

**Note (IMP-020, resolved 2026-06-01):** The na-pipeline skill stage labels were
validated against this module. Both use the canonical stage numbering (Stage 0,
1, 2, 3, 4a, 4b, 4c, 5, 6, 6.5, 7, 7.5, 8, 9, 10) — no divergence found.

| This Module (v6.0) | na-pipeline Skill Label | Description |
|---|---|---|
| Stage 0 | (prereq check) | Module availability check |
| Stage 1 | (prereq) | Discovery — tiers 1–8 |
| Stage 2 | (prereq) | Load county baseline |
| Stage 3 | Stage 3 | Resolution Engine (single pass) |
| Stage 4a | Stage 4a | GPS fill-forward from DB |
| Stage 4b | Stage 4b | GPS acquisition (single pass, all entity types) |
| Stage 4c | Stage 4c | GPS Gate (Sites and APs) |
| Stage 5 | Stage 5 | Normalization Engine |
| Stage 6 | Stage 6 | TSV Output (four files) |
| Stage 6.5 | Stage 6.5 | Vocabulary Validation Gate |
| Stage 7 | Stage 7 | TSV Integrity Check |
| Stage 7.5 | Stage 7.5 | Human Review Gate ← pipeline halts |
| Stage 8 | Stage 8 | Database Upsert |
| Stage 9 | — | Relationship Validation |
| Stage 10 | — | Final Output Bundle |

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- Schema Modules v6.x
- Vocabulary Modules v6.x
- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.x
- Discovery Metadata Specification v6.x
- Resolution Rules Module v6.x
- Resolution Engine v6.x
- GPS Acquisition Module v6.x
- Normalization Engine v6.x
- Child Site Rules Module v6.x
- County Baseline Module v6.x
- Entity Upsert Engine v6.x
- TSV Output Specifications v6.x
- TSV Integrity Check Module v6.x
- Audit & Logging Module v6.x

------------------------------------------------------------
# 12. PIPELINE CODING CONVENTIONS (IMP-106)

## 12.1 File Writing — Write Tool Required

**Never use bash heredocs to write pipeline scripts or any file longer than
~30 lines.**

Bash heredocs pass the entire file content as part of the command string.
That string has a silent size limit — content beyond the limit is truncated
without any error or warning. The result is a syntactically broken file that
appears to have been written successfully.

### Required approach by operation type

| Operation | Correct tool |
|---|---|
| New file or complete rewrite | `Write` tool — content is a dedicated parameter, no size limit |
| Targeted change to existing file | `Edit` tool — exact string replacement |
| Key-targeted YAML append (IMP-079) | Python `yaml.safe_load` / `yaml.dump` via bash — the one legitimate bash file operation |

### Mandatory syntax verification after every script write

```bash
python -m py_compile path/to/script.py && echo "OK"
```

If this fails, the file was likely truncated. Do not attempt to patch —
rewrite from scratch using the `Write` tool.

### Recognizing a truncated file

- `wc -l` returns fewer lines than expected
- Last line is mid-expression: unclosed parenthesis, incomplete string,
  cut-off identifier
- File appears written (no error was reported)

This is always a heredoc size truncation, not a logic error.

------------------------------------------------------------
# END OF PROCESSING ORCHESTRATION MODULE v6.0
