---
name: na-pipeline
description: Executes the Natural Areas Project pipeline after discovery — resolution, normalization, GPS acquisition, TSV output, and database upsert. Triggers on resolve, normalize, generate TSV, upsert, pipeline, or post-discovery processing.
---

# Natural Areas Project — Pipeline Skill v5.6

## CHANGES FROM v5.5 → v5.6

- **IMP-069 — GPS gate before TSV Output**: Added Stage 3c GPS Gate between GPS Acquisition
  (Stage 3b) and TSV Output (Stage 4). No Site entity may proceed to Stage 4 unless GPS is
  confirmed non-null, OR `gps_unresolvable = true` is explicitly set. GPS-null entities without
  the flag are routed to `held_entities` with `hold_reason = "gps_missing"` and excluded from
  the current run's TSV output. Late-addition sites entered outside the normal pipeline flow
  must re-enter at Stage 2 — they cannot be upserted directly.
- Updated Site Normalization Contract reference to v5.9.
- Updated Site Vocabulary Module reference to v5.5.

## CHANGES FROM v5.4 → v5.5

- **IMP-031 — GPS preservation on pipeline re-run**: Stage 3 now includes a GPS fill-forward step. Before running GPS acquisition, the pipeline reads any previously acquired GPS (and derived fields: Plus Code, township, municipality) from the DB for each entity. Entities that already have GPS in the DB are not re-acquired; their existing values are carried forward. Only entities with no GPS in the DB proceed through the full acquisition workflow. Updated Stage 3 description and added GPS Preservation Rule section.
- Updated Normalization Engine reference to v5.7.

Executes all post-discovery pipeline stages: Resolution → Normalization → GPS Acquisition → TSV Output → Database Upsert.

## Pipeline Overview

```
Raw Discovery Records (staging file)
        ↓
Stage 1: Resolution Engine v5.4
        ↓
Stage 2: Normalization Engine v5.8  ← blocking gate
         (Site Normalization Contract v5.9; Site Vocabulary Module v5.5)
        ↓
Stage 3: GPS Acquisition Module v5.3
         3a. GPS fill-forward (read existing GPS from DB)
         3b. GPS acquisition (for entities with no GPS in DB)
         3c. GPS Gate ← IMP-069 (hold GPS-null entities; block if no gps_unresolvable flag)
        ↓
Stage 4: TSV Output (six files, one per entity type)
        ↓
Stage 5: TSV Integrity Check v5.3
        ↓
Stage 6: Database Upsert (SQLite via Entity Upsert Engine v5.1)
```

## Stage 1 — Resolution Engine v5.4

Transforms raw discovery records into resolved entities by detecting identity, merging duplicates, and preserving conflicts.

**Five phases:**
1. **Grouping** — partition records by `(entity_type, county_primary)`
2. **Identity Matching** — apply anchors and similarity scoring
3. **Merge Decisions** — form clusters above MERGE_THRESHOLD; flag review sets
4. **Field-Level Merging** — merge raw values using deterministic strategies
5. **Parent Resolution** — resolve parent names to IDs; preserve lineage metadata

**Key rules:**
- Resolution is purely mechanical — it does not normalize, infer, or choose between conflicting values
- All raw values are preserved exactly
- Conflicts are recorded, not resolved — Normalization resolves them
- Multi-county records are placed in all relevant county groups
- Resolution does not modify raw metadata

**Field merge strategies:**
- `choose_or_conflict` — name, location, organizational fields
- `union` — counties, URLs, partner agencies
- `conflict` — GPS lat/lon, lengths, acreage
- `metadata_union` — all metadata blocks
- `parent_resolution` — parent_*_raw lists

Reference: `na_resolution_engine_v5.x.md`, `na_resolution_rules_v5.x.md`

## Stage 2 — Normalization Engine v5.6

Transforms resolved entities into normalized entities ready for TSV output and database upsert.

**Normalization is a mandatory blocking gate.** No TSV Output (Stage 4) or Database Upsert (Stage 6)
may proceed until every entity has reached a `normalized`, `rejected`, or `held` outcome. All
rejections — including vocabulary failures for required fields — must be surfaced and logged before
any downstream stage begins.

**Key normalizations (all entity types):**
- Schema validation against Schema Modules v5.x
- Vocabulary normalization against Vocabulary Modules v5.x
  - Required vocabulary-governed fields: unmappable values → **Fatal Error (rejection)**
  - Optional vocabulary-governed fields: unmappable values → Warning (field left blank)
- County normalization: semicolon-delimited, alphabetized, "County" suffix stripped
- GPS validation: parse to numeric, validate ranges, round to 6 decimal places
- Plus Code computation from validated GPS
- GIS spatial lookup: derive `township` and `municipality` from GPS coordinates
- Integrity anchor dedup check against current run and existing graph entities
- Parent/child validation

**Site-specific normalizations:**
- Columbus CRP "Parkland" suffix: if `name_raw` ends with "Parkland" (whole-word, case-insensitive),
  the normalized `name` replaces the suffix with "Park". Raw value preserved in `name_raw`.
  Required for correct GPS name-matching against MORPC and county GIS sources at Stage 3.
  See Site Normalization Contract v5.4 §5.1.
- Status inference: if `status_raw` is blank (not captured at discovery) AND the entity has an
  active authoritative URL or GPS from an authoritative source, normalize `status = "Active"`.
  Inference is recorded in normalization provenance with basis. Does not apply when `status_raw`
  is present but unmappable. See Normalization Engine v5.6 §4.2a.

**Per-entity routing:**
- Sites: category, subtype, designation, features, GPS, Plus Code, GIS, Derived Label, status inference
- Trails: use type, surface type, origin type, difficulty, maps URL list, identity notes
- Trail Segments: segment type, surface type, difficulty, geometry, maps URL list, identity notes
- Trail Networks: network type, member trail IDs validation, maps URL list, identity notes
- Site Networks: network type, member site IDs validation, identity notes
- Access Points: type, features, GPS (required), Plus Code, GIS, Derived Label, identity notes

**Note**: Derived Label is computed for Sites and Access Points only. It is not computed for Trails, Trail Segments, Trail Networks, or Site Networks.

**Outcomes:**
- `normalized` — ready for upsert
- `rejected` — fatal validation errors (entity must not proceed downstream)
- `held` — valid but incomplete (see held entity rules below)

Reference: `na_normalization_engine_v5.x.md`

## Stage 3 — GPS Acquisition Module v5.2

Handles GPS for entities with blank GPS coordinates. Two sub-steps run in order:

**Stage 3a — GPS Fill-Forward (IMP-031)**: Before any acquisition, the pipeline reads the DB for each entity being processed. If an entity already has `gps_lat`, `gps_lon`, `plus_code`, `township`, and `municipality` values in the DB from a prior pipeline run, those values are carried forward directly into the current run's normalized output. The entity is not re-submitted to the GPS acquisition workflow. This ensures that a pipeline re-run (e.g., to reprocess new YAML records) does not wipe GPS data acquired in a previous run.

**Stage 3b — GPS Acquisition**: Entities with no GPS in the DB proceed through the full acquisition workflow. Read `na_gps_acquisition_v5.x.md` for the full workflow.

**Primary GPS source for 15 MORPC-covered Ohio counties** (FRA, FAI, DEL, PIC, LIC, MAD, UNI, ROS, KNO, FAY, MAR, MRW, HOC, LOG, PER): use the MORPC Parks & Open Space ArcGIS layer (`d898fa77e91d414f8f296b0511f14fbf_11`) before geocoding or manual lookup. Download the full layer once as a project asset; apply county filter at match time. Achieved 96.4% GPS coverage for Franklin County. See `na_gps_acquisition_v5.x.md` §5.5 for matching protocol and thresholds.

Entities with GPS newly acquired in Stage 3b re-enter normalization for Plus Code computation and GIS derivation.

**Stage 3c — GPS Gate (IMP-069)**: After GPS fill-forward and acquisition, every Site entity is
checked for GPS completeness before proceeding to TSV Output:

- **GPS confirmed** (`gps_lat` and `gps_lon` non-null) → proceed to Stage 4.
- **GPS unresolvable** (`gps_unresolvable = true` set in normalization record) → proceed to Stage 4.
  `notes` must include an explanation of why GPS cannot be obtained.
- **GPS null, no flag** → route to `held_entities` with `hold_reason = "gps_missing"`. Entity is
  excluded from Stage 4 output for this run. It will be re-checked on the next pipeline run.

**Late-addition sites**: Any site added outside the normal discovery-to-pipeline flow (e.g., added
manually to a staging file after the main pipeline run) must re-enter at **Stage 2** — not injected
directly into Stage 6. They must pass Stage 3 GPS Acquisition and Stage 3c GPS Gate before upsert.

GPS Gate applies to **Sites only**. Access Points are already held at `missing_gps` by the existing
Held Entity Rules. Trails, Trail Segments, and Networks are not gated on GPS.

### GPS Preservation Rule

**On any pipeline re-run, previously acquired GPS must not be overwritten by blank.**

Precedence when an entity is processed:
1. **YAML GPS** (`gps_lat_raw` / `gps_lon_raw` directly from the discovery source) — highest priority; use if present.
2. **DB GPS** (previously acquired and stored from any prior run) — use if YAML has no GPS.
3. **No GPS** — proceed to Stage 3b acquisition. If acquisition also fails, GPS fields remain blank (entity held if Access Point; others proceed with blank GPS).

Fields preserved by fill-forward: `gps_lat`, `gps_lon`, `plus_code`, `township`, `municipality`.

Provenance: fill-forward GPS must be recorded in normalization provenance as `acquisition_method: "db_fill_forward"` with the original acquisition provenance source noted.

## Held Entity Rules

Entities are held (not rejected) when valid but incomplete:

| Hold Reason | Trigger | Release Condition |
|-------------|---------|-------------------|
| `missing_gps` | Access Point without GPS after GPS Acquisition | GPS acquired in subsequent run |
| `unresolved_member_ids` | Network with unresolved member IDs | Member entities added to graph |
| `unresolved_parent` | Entity whose parent not yet in graph | Parent entity added to graph |

Held entities are stored in the `held_entities` table and checked on every subsequent run.

**Multi-county Trail Network handling (IMP-046)**: A Trail Network spanning multiple counties is created during the **first county session** that encounters it — not held until all counties are done. At creation, `member_trail_ids` is populated with only the trails documented in the current county. The `identity_notes` field must record that membership is partial and which counties are pending. The network TSV lives in the first county's spreadsheet folder only. When subsequent county sessions are processed, they add member trail entries to `trail_network_members` and update `member_trail_ids` on the existing network record — they do NOT create a new network entity. See Trail Network Discovery Subproc v5.2 §17 for the full protocol.

## Stage 4 — TSV Output

Six TSV files produced, one per entity type. Column order is absolute and must never change.
Each file must contain exactly the canonical fields listed below — no more, no fewer.

| File | Spec | Fields | Tabs |
|------|------|--------|------|
| `{county}_sites.tsv` | `na_tsv_output_site_v5.x.md` | 25 | 24 |
| `{county}_trails.tsv` | `na_tsv_output_trail_v5.x.md` | 19 | 18 |
| `{county}_trail_segments.tsv` | `na_tsv_output_trail_segment_v5.x.md` | 17 | 16 |
| `{county}_trail_networks.tsv` | `na_tsv_output_trail_network_v5.x.md` | 17 | 16 |
| `{county}_site_networks.tsv` | `na_tsv_output_site_network_v5.x.md` | 15 | 14 |
| `{county}_access_points.tsv` | `na_tsv_output_access_point_v5.x.md` | 17 | 16 |

**Canonical field order (all six entity types):**

**Site** (25): name · category · subtype · designation · status · ownership · governance · partner_agencies · coordination · description · location · acres · counties · municipality · township · gps_lat · gps_lon · plus_code · features · notes · url_primary · urls · parent_site_id · created_at · updated_at

**Trail** (19): Trail Name · Alternate Names · Trail Use Type · Trail Surface Type · Trail Origin Type · Total Length (Miles) · Counties · Governance · Partner Agencies · Status · Difficulty · Accessibility · Description · Trail History · Identity Notes · Notes · URL · Maps · Trail ID

**Trail Segment** (17): Parent Trail · Segment Name · Counties · Governance · Segment Length (Miles) · Surface Type · Segment Type · Status · Difficulty · Accessibility · Description · Identity Notes · Notes · URL · Maps · Geometry · Segment ID

**Trail Network** (17): Network Name · Network Type · Status · Ownership · Governance · Partner Agencies · Counties · States Included · Total Length (Miles) · Member Trail Count · Member Trail IDs · Description · Identity Notes · Notes · URL · Maps · Network ID

**Site Network** (15): Network Name · Network Type · Status · Ownership · Governance · Partner Agencies · Counties · States Included · Member Count · Member Site IDs · Description · Identity Notes · Notes · URL · Network ID

**Access Point** (17): Access Point Name · Access Point Type · Status · Identity Parent Entity Type · Identity Parent Entity Name · County · Township · Municipality · Address · GPS Lat · GPS Lon · Plus Code · Features · Identity Notes · Notes · URL · Access Point ID

**Provenance exclusion rule**: Entity TSV files must never contain fields from provenance tables
(`discovery_provenance`, `resolution_provenance`, `normalization_provenance`, `run_metadata`).
The canonical field lists above are exhaustive. No additional columns may be appended.
Column order must exactly match the canonical list for each entity type.

Before emitting any TSV row, validate that the output column set matches the canonical list exactly.
Any extra field — including any provenance field accidentally included — is a Stage 4 failure.

## Stage 5 — TSV Integrity Check v5.3

Run against all six TSV files before upsert. Checks:
- Exact delimiter counts per entity type
- No internal tabs or newlines
- True blank fields (no placeholders)
- No leading/trailing whitespace
- All anchor fields in correct positions
- Identity anchor fields populated
- Counties semicolon-delimited and alphabetized
- No multi-row expansion
- **Provenance field exclusion**: no field from any provenance table appears in the entity TSV
  column set; all columns match the canonical field list for the entity type

If any row fails, pipeline halts. All failures logged before halting.

Reference: `na_tsv_integrity_check_v5.x.md`

## Stage 6 — Database Upsert

Writes normalized entities to SQLite database via Entity Upsert Engine v5.1.

**Intent flags:**
- `insert` — new entity
- `update` — existing entity matched on integrity anchor
- `hold` — valid but incomplete; written to `held_entities` table
- `review` — collision detected; written to `manual_review_queue`

**Core tables:** `sites`, `trails`, `trail_segments`, `trail_networks`, `site_networks`, `access_points`

**Relationship tables:** `site_parent`, `trail_to_segment`, `trail_to_network`, `site_to_network`, `access_point_parents`

**Operational tables:** `held_entities`, `manual_review_queue`, `entity_conflicts`, `entity_uncertainty`, `entity_geometry`

**Provenance tables:** `discovery_provenance`, `resolution_provenance`, `normalization_provenance`, `run_metadata`

All provenance tables are append-only. Prior run records are never overwritten.

Reference: `na_entity_upsert_engine_v5.x.md`
