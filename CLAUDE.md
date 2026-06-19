# Natural Areas Project v5 — CLAUDE.md
# Persistent session context for Claude Code (and Claude Cowork parallel use)
# Last updated: 2026-05-23 | Manifest: na_module_manifest_v5.22.md

---

## 1. PROJECT ORIENTATION PROTOCOL (IMP-112)
**Run this at the start of every session — new or resumed — before touching any data.**

```bash
ls "D:\users\user1\Documents\CP Projects\Natural Areas Project v5"
```

1. Confirm these authoritative directories exist: `/discovery`, `/schemas`, `/vocabularies`,
   `/normalization`, `/output`, `/processing`, `/audit`
2. Read the highest-versioned `na_module_manifest_v5.*.md` at the project root.
   The manifest is the single authoritative source for current module filenames.
3. Derive exact filenames from the manifest — never from memory or session summaries.
4. **Prohibited sources**: `deprecated/` and `Natural Areas supplelmental files/` are
   legacy/v4 material. Never use them as procedure or schema references.
5. **No broad globs**: `**/*.md` surfaces deprecated copies before authoritative ones.
   Always: read manifest → get exact filename → read that file directly.

---

## 2. PROJECT OVERVIEW

The Natural Areas Project (NAP) catalogs natural areas, parks, trails, and open spaces
across Ohio counties into a unified SQLite database (`natural_areas_v5.db`).

**Six entity types** (always process in this order within any tier):
1. Sites
2. Trails
3. Trail Segments
4. Trail Networks
5. Site Networks
6. Access Points

**Entity ID format**: `OH-{COUNTY}-{TYPE}-{SEQ}` (e.g., `OH-OTT-S-001`)
**Multi-county ID format**: `OH-MC-{TYPE}-{SEQ}` (e.g., `OH-MC-T-0109`)
**Type codes**: S=Site, T=Trail, TS=Trail Segment, TN=Trail Network, SN=Site Network, AP=Access Point, TR=Trail (water), SI=Site (water)

**Database**: `/NASqlite/natural_areas_v5.db` at project root — SQLite, do not modify directly.
**Improvement tracker**: `na_improvement_tracker.md` at project root.

---

## 3. DIRECTORY STRUCTURE

```
Natural Areas Project v5/
├── CLAUDE.md                          ← this file
├── na_module_manifest_v5.22.md        ← READ THIS FIRST every session
├── na_improvement_tracker.md          ← protocol gaps and decisions log
├── Parks_and_Open_Space_*.csv         ← MORPC GIS layer (15-county coverage)
├── Townships_Officials2022-2023.xlsx  ← OTA authoritative township roster (T5)
├── SORP_Parcels_2023.csv              ← supplemental parcel reference
│
├── /NASqlite/natural_areas_v5.db      ← live SQLite database
├── /discovery/                        ← tier sub-procedures and entity discovery sub-procedures
├── /schemas/                          ← entity schema modules
├── /vocabularies/                     ← controlled vocabulary modules
├── /normalization/                    ← normalization contracts + normalization engine
├── /output/                           ← TSV output specs and integrity check
├── /processing/                       ← resolution engine, cross-county resolution, baseline
├── /audit/                            ← audit and logging module
├── /utilities/                        ← Python pipeline code (na_run_county.py, na_pipeline_core.py, etc.)
├── /GIS_Assets/                       ← Ohio township/MCD shapefiles for GIS lookups
│
├── /County_Spreadsheets/{County}/     ← per-county working files
│   ├── {county}_ohio_raw_discovery.yaml   ← staging YAML (discovery record)
│   ├── {county}_ohio_handoff.md           ← inter-session progress tracker
│   ├── {county}_ohio_session_log.md       ← session log
│   ├── {county}_config.json               ← pipeline run config
│   ├── {county}_sites.tsv                 ← normalized output
│   ├── {county}_trails.tsv
│   ├── {county}_access_points.tsv
│   ├── {county}_site_networks.tsv
│   └── upsert_{county}.py                 ← generated upsert script
│
└── /deprecated/       ← superseded modules — never use as references
```

---

## 4. SOURCE AUTHORITY HIERARCHY (IMP-078)

1. **Protocol modules and sub-procedures** — authoritative for all rules
2. **Handoff document** — progress tracker only; records where you are, not the rules
3. **Session memory / CLAUDE.md summaries** — no protocol authority

When any two conflict, the higher-authority source wins without exception.

---

## 5. SESSION AUTONOMY

    When bootstrapping a new county, proceed directly through all setup steps (session files, handoff, staging YAML) without asking for confirmation, unless there is a discrepancy or perceived problem.
    Begin Tier 1 discovery immediately after setup. Only pause at mandatory human gates (Stage 5.5 Human Review Gate) or when genuine ambiguity requires a decision.

---

## 6. DISCOVERY WORKFLOW — 8-TIER SEQUENCE

Before starting a county: run IMP-112 orientation, then read
`discovery/na_discovery_orchestration_v5.3.md` §6 for the canonical tier order.

| Tier | Governance | Sub-procedure | Key notes |
|------|-----------|---------------|-----------|
| 1 | Federal & Tribal | `na_fed_tribal_discovery_subproc_v5.3.md` | VA NCA §3.7 mandatory |
| 2 | State | `na_state_discovery_subproc_v5.5.md` | Public universities = Tier 2 |
| 3 | District (Metroparks, conservancy) | `na_district_discovery_subproc_v5.7.md` | Ohio Auditor pre-enumeration §3.0 is MANDATORY FIRST STEP |
| 4 | County | `na_county_discovery_subproc_v5.3.md` | Cross-reference MORPC CSV for covered counties |
| 5 | Township | `na_township_discovery_subproc_v5.4.md` | Enumerate from `Townships_Officials2022-2023.xlsx` first |
| 6 | Municipal | `na_municipal_discovery_subproc_v5.9.md` | Never skip villages; cross-reference MORPC CSV |
| 7 | Conservancy & Land Trust | `na_conservancy_discovery_subproc_v5.5.md` | Check §4 Known Org inventory before any county T7 run |
| 8 | Private | `na_private_discovery_subproc_v5.3.md` | All golf courses; GNIS cemetery enumeration §5.1 |

**Before each tier**: Read (or re-read) the authoritative sub-procedure. Not optional.
**Entity type sequence within each tier**: Sites → Trails → Trail Segments → Trail Networks → Site Networks → Access Points.
**Every entity type requires a documented result** before closing a tier — either entities or a confirmed null with evidence and sources checked. Silence is not a null.

### Discovery Raw Record — Required Fields
```yaml
entity_type:          # Site | Trail | Trail Segment | Trail Network | Site Network | Access Point
name_raw:             # exactly as found
counties_raw: []
county_primary:
ownership_raw:
governance_raw:
partner_agencies_raw:
coordination_raw:
gps_lat_raw:          # only if explicitly stated by authoritative source
gps_lon_raw:
location_raw:         # Sites and Access Points only
description_raw:      # Sites/APs — narrative prose, verbatim
features_raw:         # Sites/APs — amenity LIST, verbatim (not sentences)
difficulty_raw:       # Trails/Trail Segments only
accessibility_raw:    # Trails/Trail Segments only
urls_raw: []
identity_notes_raw:
township_raw:         # BLANK — GIS-derived only
municipality_raw:     # BLANK — GIS-derived only
discovery_tier:       # 1-8
seeded_from_baseline: # true | false
baseline_id:
```

**Retired fields** (do not use): `gps_raw`, `notes_raw`, `maps_raw`

### Tier Close Verification (IMP-080)
Before marking any tier complete: physically read or grep the staging YAML to confirm
every result block (entity records or null-evidence blocks) is actually on disk.
"I staged it above" is not sufficient — the file is the record.

### Cross-County Candidate Flagging (IMP-104)
When closing any tier, check: if any entity's `counties_raw` lists more than one county,
`identity_notes_raw` must contain either `CROSS_COUNTY_CANDIDATE` or `KNOWN_MC:{id}`.

### YAML Staging Append Safety (IMP-079)
After Tier 6, always append records by key name in Python — never by text position:
```python
import yaml, pathlib
f = pathlib.Path("county_oh_raw_discovery.yaml")
data = yaml.safe_load(f.read_text())
data.setdefault("records", [])
data["records"].append({ ... })
f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False))
```

---

## 7. PIPELINE WORKFLOW — STAGES 1–6

Read `processing/na_processing_orchestration_v5.5.md` before any pipeline work.
Pipeline config is a JSON file per county (template: `utilities/na_pipeline_config_template.json`).

```
Stage 1a  Resolution Engine Pass 1       → na_resolution_engine_v5.5.md
Stage 1b  Resolution Engine Pass 2 (APs)
Stage 2a  GPS Fill-Forward               → preserve previously acquired GPS (IMP-031)
Stage 2b  GPS Acquisition                → na_gps_acquisition_v5.3.md; MORPC layer primary for 15 counties
Stage 2c  GPS Gate — Sites               → no GPS + no gps_unresolvable=true → held_entities
Stage 2d  GPS Gate — APs
Stage 3   Normalization Engine           → na_normalization_engine_v5.8.md; MANDATORY BLOCKING GATE
Stage 4   TSV Output                     → read output spec for each entity type present
Stage 4.5 Vocabulary Validation Gate     → halts on any violation; features check required
Stage 5   TSV Integrity Check            → non-halting; surface vocabulary expansion candidates
Stage 5.5 Human Review Gate             → PIPELINE HALTS; explicit human confirmation required
Stage 6   Database Upsert               → ON CONFLICT DO UPDATE; DDL for all 3 table groups required
```

### Stage 4 — TSV Column Order (canonical, must match exactly)
- **Sites** (25 cols): `name, category, subtype, designation, status, ownership, governance, partner_agencies, coordination, description, location, acres, counties, municipality, township, gps_lat, gps_lon, plus_code, features, notes, url_primary, urls, parent_site_id, created_at, updated_at`
- **Trails** (19 cols): read `output/na_tsv_output_trail_v5.1.md`
- **Access Points** (17 cols): read `output/na_tsv_output_access_point_v5.1.md`
- **Site Networks** (15 cols): read `output/na_tsv_output_site_network_v5.1.md`
- `site_id` and `features_raw` are DB-only — do NOT appear in TSV.
- **Held entities are excluded from all TSV files** (IMP-113). They appear only in `held_entities` table.

### Stage 5 — Surface Vocabulary Expansion Candidates
Any token logged as `unmapped_token_dropped` in `normalization_provenance` (IMP-116)
should appear here as a vocabulary expansion candidates list. Informational, non-blocking.

### Stage 5.5 — Human Review Checklist
- Entity counts reasonable (no unexpected zeros or inflated counts)
- Category/subtype assignments substantively correct
- GPS coordinates plausible (spot-check a few)
- Held entities expected — no surprises in what was held or why
- **AP-to-Site reclassification check (IMP-114)**: Any AP with `acres_raw` populated,
  `description_raw` present, and governance distinct from parent trail → candidate for
  reclassification. See `normalization/na_access_point_normalization_v5.3.md` §10a.

Do not proceed to Stage 6 without explicit human confirmation.

### Stage 6 — Pre-Upsert MC County Format Scan (IMP-115)
Before running the upsert script, query for malformed county fields:
```sql
SELECT entity_id, counties FROM trails        WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
SELECT entity_id, counties FROM sites         WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
SELECT entity_id, counties FROM site_networks WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
```
Canonical format: `"Ottawa;Wood"` — semicolon-delimited, no spaces, alphabetical order.

### Stage 6 — Required DDL Table Groups (IMP-087)
Every upsert script must include `CREATE TABLE IF NOT EXISTS` for:
- **Primary entity tables**: `sites`, `trails`, `trail_segments`, `trail_networks`, `site_networks`, `access_points`
- **Relationship tables**: `site_parent`, `trail_parents`, `trail_to_segment`, `trail_network_members`, `site_network_members`, `access_point_parents`
- **Operational tables**: `held_entities`, `manual_review_queue`, `entity_conflicts`, `entity_uncertainty`, `entity_geometry`
- **Provenance tables**: `run_metadata`, `discovery_provenance`, `resolution_provenance`, `normalization_provenance`

### Live DB Schema — Verified Column Names (use exactly)
| Field in normalized JSON | DB column name |
|---|---|
| `url_secondary` | `urls` |
| `surface` | `surface_type` |
| `origin` | `origin_type` |
| `site_network_id` | `network_id` |

`resolution_provenance` columns: `(prov_id, entity_id, entity_type, county, resolution_run, notes, run_id, created_at)`
— use `resolution_run`, NOT `resolution_action`.

`run_metadata` INSERT: `(run_id, county, state, run_date, records_input, normalized, held, notes, created_at)`
— do NOT use `pipeline_version`, `entity_id`, or `entity_name`.

---

## 8. HELD ENTITIES — CANONICAL hold_reason VALUES (IMP-113)

| `hold_reason` | Triggering stage | Resolved by |
|---|---|---|
| `gps_missing` | Stage 2c/2d GPS Gate | GPS re-run or `gps_unresolvable=true` |
| `parent_held` | Normalization Engine §1 | Parent entity released |
| `unresolved_parent` | Upsert Engine | Partner county pipeline run |
| `unresolved_member_ids` | Upsert Engine | Member trails upserted in partner county |
| `cross_county_candidate` | Resolution Engine Phase 0 | Cross-county resolution pass |
| `cross_county_held` | Cross-county resolution Scenario A | Partner county pipeline run |
| `unconfirmed_baseline_seed` | Discovery close-out / baseline reconciliation — GNIS name or baseline seed entry could not be confirmed as an active managed natural area through Tier 1–8 discovery | Authoritative source confirms active managed public access (→ proceed to full pipeline); or entity confirmed non-existent/inaccessible (→ remove from `held_entities` with disposition note in `hold_detail`) |
| `identity_uncertain` | Discovery — source implies entity existence but individual identity (name, count, or extent) is unresolvable from available sources | Field verification or authoritative source inventory confirming individual entity names and count |

---

## 9. CROSS-COUNTY ENTITIES (IMP-104)

Three scenarios during resolution:
- **Scenario A** — Partner county not yet run: assign provisional `OH-{COUNTY}-{TYPE}-{SEQ}` ID, hold pending partner run
- **Scenario B** — Collision detected: merge to `OH-MC-{TYPE}-{SEQ}` immediately
- **Scenario C** — Known MC ID already in DB: use `KNOWN_MC:{id}` flag in `identity_notes_raw`

Bootstrap pre-discovery check: always query DB for existing MC entities referencing the
target county before discovery begins. See `processing/na_cross_county_resolution_v5.2.md` §5.

**Sequence number gaps are expected** (IMP-117) — do not infer missing entities from gaps.
Gaps arise from provisional IDs superseded during resolution, entities merged into existing
records, or sequence numbers withdrawn during QA.

---

## 10. CRITICAL PROTOCOL RULES

### File Writing (IMP-106)
**Never use bash heredocs for files longer than ~30 lines.** Heredocs have a silent size
limit — content beyond the limit is truncated without error. Always use Python `open().write()`
or the Write/Edit tools directly.

### Module Version References (IMP-109)
- **Filenames** include version numbers: `na_site_normalization_v5.11.md`
- **Cross-references in module bodies** use bare titles only: `na_site_normalization.md §5`
- **This manifest** is the only authoritative source for current version numbers

### Features Field Rules
- `features_raw`: raw amenity LIST (bullets/icons from source), verbatim — NOT narrative sentences
- `description_raw`: narrative prose — NOT an amenity list
- `features` (normalized): controlled vocabulary terms only, semicolon-delimited, alphabetized
- Activities (hiking, fishing) are prohibited in `features` — they map to physical infrastructure or are dropped
- Named Trail/AP entities are prohibited in `features`
- Vocabulary mapping: load from `utilities/na_feature_mapper_reference.md` — never transcribe from memory

### GPS Rules
- Never estimate or infer GPS coordinates
- `gps_lat_raw` / `gps_lon_raw` as separate fields (not combined `gps_raw`)
- Sites and APs without GPS → `held_entities` unless `gps_unresolvable=true`
- Previously acquired GPS is filled forward on re-runs (IMP-031) — not overwritten

### Governance Field Contamination
- `governance_raw` must contain only the managing organization's name
- GIS park type labels ("Community Park", "Neighborhood Park") are NOT governance
- Record GIS type labels in `category_raw` or `identity_notes_raw`

### DEFECT Status (IMP-076)
If a tier was worked under wrong protocol or with missing mandatory steps, mark it
**DEFECT** in the staging file and **PENDING** in the handoff — never carry it forward as complete.

---

## 11. QUALITY AND IMPROVEMENT

**Quality module**: Read `na-quality.md` (or the na-quality SKILL.md) before any audit work.
Covers: PAD-US completeness gate, vocabulary compliance audit, county mismatch review.

**Improvement tracker**: `na_improvement_tracker.md`
- Section 1 — Open items
- Section 2 — Decided, pending implementation
- Section 3 — Decided and implemented (fully closed)
- Item ID format: `IMP-###` (sequential, project-wide)

When a new protocol gap is identified during county work, add it to Section 1 immediately.

---

## 12. UTILITY SCRIPTS

| Script | Purpose |
|---|---|
| `utilities/na_run_county.py` | County pipeline driver — reads JSON config, calls PipelineRunner |
| `utilities/na_pipeline_core.py` | Shared PipelineRunner engine (Stages 3–6) |
| `utilities/na_pipeline_config_template.json` | Empty county config skeleton |
| `utilities/na_feature_mapper_reference.md` | Canonical FEATURE_MAP — copy into county script, extend as needed |
| `utilities/na_plus_code.py` | Plus Code encoder — import as `from utilities.na_plus_code import encode_plus_code` (never subprocess) |
| `utilities/na_township_lookup.py` | Ohio MCD point-in-polygon lookup against TIGER/Line 2024 |
| `utilities/na_yaml_preprocess.py` | Pre-processes discovery YAML before `yaml.safe_load_all()` — handles `#` in values |
| `utilities/na_generate_config.py` | Reads raw discovery YAML, assigns IDs, outputs blank normalized JSON config |

---

## 13. STARTING A NEW COUNTY

1. Run IMP-112 orientation (§1 above)
2. Read `na_module_manifest_v5.22.md` to confirm current filenames
3. Run bootstrap: read `na-bootstrap.md` (or na-bootstrap SKILL in Cowork)
4. Create county folder: `County_Spreadsheets/{County}/`
5. Create session files: raw_discovery YAML, handoff.md, session_log.md, config JSON
6. Query DB for existing MC entities referencing this county (`processing/na_cross_county_resolution_v5.2.md` §5)
7. Begin Tier 1 discovery

## RESUMING A COUNTY

1. Run IMP-112 orientation (§1 above)
2. Read `na_module_manifest_v5.22.md`
3. Read the county handoff.md — note current tier status
4. Read `discovery/na_discovery_orchestration_v5.3.md` §6 — verify handoff tier labels match canonical tier order
5. If they disagree, the module wins — correct the handoff before proceeding
6. Read the sub-procedure for the current tier before any work begins

---

*This file is a session startup guide. For authoritative procedure detail, always read
the module files in the canonical directories listed in §3. When this file and a module
conflict, the module wins.*
