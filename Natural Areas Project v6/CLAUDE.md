# Natural Areas Project v6 — CLAUDE.md
# Persistent session context for Claude Code (and Claude Cowork parallel use)
# Last updated: 2026-05-31 | Manifest: na_module_manifest_v6.0.md

---

## 1. PROJECT ORIENTATION PROTOCOL
**Run this at the start of every session — new or resumed — before touching any data.**

```bash
ls "D:\users\user1\Documents\CP Projects\Natural Areas Project v6"
```

1. Confirm these authoritative directories exist: `/discovery`, `/schemas`, `/vocabularies`,
   `/normalization`, `/output`, `/processing`, `/audit`
2. Read `na_module_manifest_v6.0.md` at the project root.
   The manifest is the single authoritative source for current module filenames.
3. Derive exact filenames from the manifest — never from memory or session summaries.
4. **Prohibited sources**: The v5 project folder (`Natural Areas Project v5/`) contains
   superseded modules. Never use v5 modules as procedure or schema references for v6 work.
5. **No broad globs**: `**/*.md` may surface wrong versions. Always:
   read manifest → get exact filename → read that file directly.

---

## 2. PROJECT OVERVIEW

The Natural Areas Project (NAP) catalogs natural areas, parks, trails, and open spaces
across Ohio counties into a unified SQLite database (`natural_areas_v5.db`).

**Four entity types** (always process in this order within any tier):
1. Sites
2. Trailthings
3. Site Networks
4. Access Points

**What is a Trailthing?** A working name for the unified interim entity type that
replaces Trail, Trail Segment, and Trail Network. It carries no semantic implication
about whether the entity is a trail, a system, a segment, or a network — that
classification is deferred pending data collection across v6 county runs (IMP-007).

**Entity ID format**: `OH-{COUNTY}-{TYPE}-{SEQ}` (e.g., `OH-OTT-S-0001`)
**Multi-county ID format**: `OH-MC-{TYPE}-{SEQ}` (e.g., `OH-MC-TT-0001`)
**Type codes**: S=Site, TT=Trailthing (v6 new), SN=Site Network, AP=Access Point
**Legacy codes** (existing DB): T=Trail, TR=Trail variant, TS=Trail Segment,
TN=Trail Network, SI=Site variant — retained as-is; new discoveries use TT.

**Database**: `/NASqlite/natural_areas_v6.db` at v6 project root — SQLite, do not
modify directly.
**Improvement tracker**: `na_improvement_tracker_v6.md` at v6 project root.
**Migration log**: `na_db_migration_log.md` at v6 project root — historical DB migrations.

---

## 3. DIRECTORY STRUCTURE

```
Natural Areas Project v6/
├── CLAUDE.md                          ← this file
├── na_module_manifest_v6.0.md         ← READ THIS FIRST every session
├── na_improvement_tracker_v6.md       ← protocol gaps and decisions log
├── na_db_migration_log.md             ← historical DB migration records
│
├── Statewide Data Assets (project root — used across all county runs)
│   ├── SORP_Parcels_2023.csv               ← State-Owned Real Property; T2 GPS source (IMP-133)
│   ├── Parks_and_Open_Space_*.csv          ← MORPC 15-county GIS layer; T4/T6 completeness + GPS
│   ├── Townships_Officials2022-2023.xlsx   ← OTA official roster; authoritative T5 enumeration
│   ├── ODOT rest stops baseline.xlsx       ← ODOT rest areas statewide; T2 baseline by county
│   ├── OH_Features_GNIS_20210825.txt       ← GNIS Ohio 2021 archive; 69K features; query via
│   │                                          utilities/na_gnis_query.py; use for GPS acquisition
│   │                                          and discovery completeness check (all tiers)
│   ├── PADUS4_0_State_OH_GDB.zip           ← PAD-US 4.0 Ohio (USGS GAP); protected areas database
│   ├── PADUS4_0_StateOH.gdb/               ← PAD-US 4.0 extracted GDB (use with QGIS/ogr2ogr)
│   ├── PADUS4_0_State_OH.csv               ← PAD-US Fee layer as CSV; 7,607 fee-owned areas;
│   │                                          fields: Unit_Nm, d_Own_Name, d_Mang_Name, d_GAP_Sts,
│   │                                          GIS_Acres, d_Pub_Access, d_Des_Tp; use for T1-T7
│   │                                          pre-discovery cross-check and completeness audit
│   ├── PADUS4_0_State_OH_Easements.csv     ← PAD-US Easement layer as CSV; 2,390 conservation
│   │                                          easements; includes EsmtHldr (holder org); replaces
│   │                                          NCED (defunct Jan 2025); use for T7 org enumeration
│   ├── NWI_OH_GDB.zip                      ← National Wetlands Inventory Ohio (USFWS); polygon
│   └── OH_geodatabase_wetlands.gdb/        ← NWI extracted GDB; use with QGIS/ogr2ogr; layer:
│                                              OH_Wetlands; Cowardin classification; use for T2/T7
│                                              wetland natural area identification
│
├── /discovery/                        ← tier sub-procedures, entity sub-procedures,
│                                         GPS acquisition, discovery orchestration,
│                                         discovery metadata spec
├── /schemas/                          ← entity schema modules
├── /vocabularies/                     ← controlled vocabulary modules
├── /normalization/                    ← normalization contracts, normalization engine,
│                                         entity upsert engine
├── /output/                           ← TSV output specs and integrity check
├── /processing/                       ← orchestration, resolution engine, resolution rules,
│                                         cross-county resolution, child site rules,
│                                         county baseline
├── /audit/                            ← audit and logging module
│
├── /County_Spreadsheets/{County}/     ← per-county working files
│   ├── {county}_ohio_raw_discovery.yaml     ← staging YAML (discovery record)
│   ├── {county}_ohio_handoff.md             ← inter-session progress tracker
│   ├── {county}_ohio_session_log.md         ← session log
│   ├── {county}_config.json                 ← pipeline run config
│   ├── {county}_document_log.yaml           ← document collection log
│   ├── source_documents/                    ← downloaded maps, PDFs, GIS exports
│   ├── {county}_sites.tsv                   ← normalized output
│   ├── {county}_trailthings.tsv
│   ├── {county}_access_points.tsv
│   ├── {county}_site_networks.tsv
│   └── upsert_{county}.py                   ← generated upsert script
│
└── /utilities/                        ← Python pipeline code (in v5 folder; shared)
```

**v5 project folder** (`Natural Areas Project v5/`) is archived.
Do not use v5 modules as v6 references. All active resources are now in v6.

---

## 4. SOURCE AUTHORITY HIERARCHY

1. **Protocol modules and sub-procedures** — authoritative for all rules
2. **Handoff document** — progress tracker only; records where you are, not the rules
3. **Session memory / CLAUDE.md summaries** — no protocol authority

When any two conflict, the higher-authority source wins without exception.

For modules not yet rewritten for v6: use the v5 equivalent, but confirm with
the v6 manifest that no v6 version exists before falling back to v5.

---

## 5. SESSION AUTONOMY

When bootstrapping a new county, proceed directly through all setup steps (session
files, handoff, staging YAML, document log) without asking for confirmation, unless
there is a discrepancy or perceived problem.
Begin Tier 1 discovery immediately after setup. Only pause at the Human Review Gate
(Stage 7.5) or when genuine ambiguity requires a decision.

---

## 6. DISCOVERY WORKFLOW — 8-TIER SEQUENCE

Before starting a county: run the orientation protocol (§1), then read
`discovery/na_discovery_orchestration_v6.0.md` for the canonical tier order.

| Tier | Governance | Sub-procedure | Key notes |
|------|-----------|---------------|-----------|
| 1 | Federal & Tribal | `na_fed_tribal_discovery_subproc_v6.0.md` | VA NCA §3.7 mandatory |
| 2 | State | `na_state_discovery_subproc_v6.0.md` | Public universities = Tier 2; cross-reference `ODOT rest stops baseline.xlsx` for rest area baseline |
| 3 | District (Metroparks, conservancy) | `na_district_discovery_subproc_v6.0.md` | Ohio Auditor pre-enumeration §3.0 is MANDATORY FIRST STEP |
| 4 | County | `na_county_discovery_subproc_v6.0.md` | Cross-reference MORPC CSV for covered counties |
| 5 | Township | `na_township_discovery_subproc_v6.0.md` | Enumerate from `Townships_Officials2022-2023.xlsx` first |
| 6 | Municipal | `na_municipal_discovery_subproc_v6.0.md` | Never skip villages; cross-reference MORPC CSV |
| 7 | Conservancy & Land Trust | `na_conservancy_discovery_subproc_v6.0.md` | Check §4 Known Org inventory before any county T7 run |
| 8 | Private | `na_private_discovery_subproc_v6.0.md` | All golf courses; GNIS cemetery enumeration §5.1 |

**Before each tier**: Read (or re-read) the authoritative sub-procedure. Not optional.
**Entity type sequence within each tier**: Sites → Trailthings → Site Networks → Access Points.
**Every entity type requires a documented result** before closing a tier — either entities
or a confirmed null with evidence and sources checked. Silence is not a null.

### Discovery Raw Record — Core Fields

**Sites:**
```yaml
entity_type: Site
name_raw:
counties_raw: []
county_primary:
ownership_raw:
governance_raw:
partner_agencies_raw:
coordination_raw:
description_raw:       # narrative prose, verbatim — ecological/physical character priority
habitat_type_raw:      # ecological/natural character; open vocabulary
features_raw:          # amenity LIST, verbatim (not sentences)
access_notes_raw:      # seasonal restrictions, permit requirements, access caveats
location_raw:
acres_raw:
gps_lat_raw:           # only if explicitly stated by authoritative source
gps_lon_raw:
boundary_document_raw: # filename in source_documents/ if boundary file downloaded
urls_raw: []
ebird_hotspot_id:      # eBird L-code if site has a hotspot (e.g. L123456); blank if none
identity_notes_raw:
township_raw:          # BLANK — GIS-derived only
municipality_raw:      # BLANK — GIS-derived only
last_verified_date:    # today's date
field_verified:        # false at discovery
discovery_tier:        # 1-8
seeded_from_baseline:  # true | false
baseline_id:
```

**Trailthings:**
```yaml
entity_type: Trailthing
name_raw:
source_term_raw:              # REQUIRED — verbatim term from source ("trail system", "greenway", etc.)
source_hierarchy_context_raw: # how source frames this entity relative to others
counties_raw: []
county_primary:
parent_id_raw:                # name of parent Trailthing — only if explicitly stated
site_parent_raw:              # name of parent Site — only if explicitly stated
parent_site_network_raw:      # name of parent Site Network — only if explicitly stated
member_trailthing_names_raw:  # names of member Trailthings if this is a container
ownership_raw:
governance_raw:
partner_agencies_raw:
coordination_raw:
description_raw:
use_type_raw:
surface_type_raw:
origin_type_raw:
status_raw:
difficulty_raw:               # only if explicitly stated
accessibility_raw:
total_length_raw:
urls_raw: []
maps_raw: []
identity_notes_raw:
last_verified_date:
field_verified:
discovery_tier:
seeded_from_baseline:
baseline_id:
```

**Site Networks:**
```yaml
entity_type: Site Network
network_name_raw:               # Required; official name verbatim
network_type_raw:               # Optional; verbatim from source; used in threshold evaluation
org_type_raw:                   # Optional; organization category; essential for Rules 2–4
status_raw:                     # Optional; verbatim; only if explicitly stated
ownership_raw:                  # Optional; often blank for designating bodies
governance_raw:                 # Optional; primary managing organization
partner_agencies_raw:           # Optional; semicolon-delimited; only if explicitly documented
coordination_raw:               # Optional; friends groups, volunteers, advisory boards
counties_raw:                   # Optional; semicolon-delimited; all counties encompassed
states_raw:                     # Optional; multi-state networks only; blank for Ohio-only
member_count_raw:               # Optional; published count only; do not self-count
member_site_names_raw:          # Optional; semicolon-delimited; exactly as listed in source
description_raw:                # Optional; character and mission priority; 1–3 sentences
identity_notes_raw:             # Optional; SITE_NETWORK_PROVISIONAL or SITE_NETWORK_UNCERTAIN
notes_raw:                      # Optional; operational context; no provenance artifacts
urls_raw: []                    # All URLs; includes primary org website
discovery_tier:                 # 1–8
seeded_from_baseline:           # true | false
baseline_id:
```

**Access Points:**
```yaml
entity_type: Access Point
name_raw:
counties_raw: []
county_primary:
parent_sites_raw: []          # Site names that are identity parents
parent_trailthings_raw: []    # Trailthing names that are identity parents
governance_raw:
description_raw:              # operational access detail
features_raw:
location_raw:
gps_lat_raw:
gps_lon_raw:
urls_raw: []
identity_notes_raw:
last_verified_date:
field_verified:
discovery_tier:
seeded_from_baseline:
baseline_id:
```

### Tier Close Verification (IMP-080)
Before marking any tier complete: physically read or grep the staging YAML to confirm
every result block (entity records or null-evidence blocks) is actually on disk.
"I staged it above" is not sufficient — the file is the record.

### Cross-County Candidate Flagging (IMP-104)
When closing any tier, check: if any entity's `counties_raw` lists more than one county,
`identity_notes_raw` must contain either `CROSS_COUNTY_CANDIDATE` or `KNOWN_MC:{id}`.

### Document Collection (v6 new)
When any map, PDF, brochure, GPX/KML, or GIS export is downloaded during discovery:
1. Save to `source_documents/` with filename: `{date}_{tier}_{short-descriptor}.{ext}`
2. Log in `{county}_document_log.yaml` — see `discovery/na_discovery_orchestration_v6.0.md` §4
3. If the document is a boundary file for a specific Site, populate `boundary_document_raw`
   on that entity's raw record with the filename.

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

## 7. PIPELINE WORKFLOW

Read `processing/na_processing_orchestration_v6.0.md` before any pipeline work.
Pipeline config is a JSON file per county (template in v5 `utilities/` folder).

```
Stage 0    Module availability check
Stage 1    Discovery (Tiers 1–8)
Stage 2    Load county baseline (Tier-0)
Stage 3    Resolution Engine              → na_resolution_engine_v6.0.md (single pass)
Stage 4a   GPS Fill-Forward              → preserve previously acquired GPS (IMP-031)
Stage 4b   GPS Acquisition               → na_gps_acquisition_v6.0.md; single pass all entity types
Stage 4c   GPS Gate                      → Sites and APs only; gps_missing → held_entities
Stage 5    Normalization Engine          → na_normalization_engine_v6.0.md; MANDATORY BLOCKING GATE
Stage 6    TSV Output                   → four files; held entities excluded
Stage 6.5  Vocabulary Validation Gate   → halts on any violation
Stage 7    TSV Integrity Check          → surface vocabulary expansion candidates
Stage 7.5  Human Review Gate            → PIPELINE HALTS; explicit human confirmation required
Stage 8    Database Upsert             → ON CONFLICT DO UPDATE; DDL for all 4 table groups required
Stage 9    Relationship Validation
Stage 10   Final Output Bundle
```

### Stage 6 — TSV Column Order (canonical, must match exactly)
- **Sites** (31 cols): read `output/na_tsv_output_site_v6.0.md`
- **Trailthings** (31 cols): read `output/na_tsv_output_trailthing_v6.0.md`
- **Access Points** (20 cols): read `output/na_tsv_output_access_point_v6.0.md`
- **Site Networks** (18 cols): read `output/na_tsv_output_site_network_v6.0.md`
- Entity IDs are DB-only — do NOT appear in TSV.
- **Held entities are excluded from all TSV files**. They appear only in `held_entities` table.

### Stage 7 — Surface Vocabulary Expansion Candidates
Any token logged as `unmapped_token_dropped` in `normalization_provenance` (IMP-116)
should appear here as a vocabulary expansion candidates list. Informational, non-blocking.

### Stage 7.5 — Human Review Checklist
- Entity counts reasonable (no unexpected zeros or inflated counts)
- Category/subtype assignments substantively correct
- GPS coordinates plausible (spot-check a few)
- Held entities expected — no surprises in what was held or why
- **AP-to-Site reclassification check (IMP-114)**: Any AP with `acres_raw` populated,
  `description_raw` present, and governance distinct from parent Trailthing → candidate
  for reclassification. See `normalization/na_access_point_normalization_v6.0.md` §10a.
- Vocabulary expansion candidates reviewed — flag any for addition to vocabulary modules.

Do not proceed to Stage 8 without explicit human confirmation.

### Stage 8 — Pre-Upsert MC County Format Scan (IMP-115)
Before running the upsert script, query for malformed county fields:
```sql
SELECT entity_id, counties FROM trailthings  WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
SELECT entity_id, counties FROM sites        WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
SELECT entity_id, counties FROM site_networks WHERE entity_id LIKE 'OH-MC-%' AND counties LIKE '%; %';
```
Canonical format: `"Ottawa;Wood"` — semicolon-delimited, no spaces, alphabetical order.

### Stage 8 — Required DDL Table Groups (IMP-087)
Every upsert script must include `CREATE TABLE IF NOT EXISTS` for:
- **Primary entity tables**: `sites`, `trailthings`, `site_networks`, `access_points`
  (plus legacy: `trails`, `trail_segments`, `trail_networks`)
- **Relationship tables**: `site_parent`, `trailthing_hierarchy`, `site_network_members`,
  `access_point_parents` (plus legacy: `trail_to_segment`, `trail_network_members`, `trail_parents`)
- **Operational tables**: `held_entities`, `manual_review_queue`, `entity_conflicts`,
  `entity_uncertainty`, `entity_geometry`
- **Provenance tables**: `run_metadata`, `discovery_provenance`, `resolution_provenance`,
  `normalization_provenance`

### Live DB Schema — Verified Column Names (use exactly)
`resolution_provenance` columns: `(prov_id, entity_id, entity_type, county, resolution_run, notes, run_id, created_at)`
— use `resolution_run`, NOT `resolution_action`.

`run_metadata` INSERT: `(run_id, county, state, run_date, records_input, normalized, held, notes, created_at)`
— `state` must be full name ("Ohio"), NOT abbreviation ("OH").
— do NOT use `pipeline_version`, `entity_id`, or `entity_name`.

---

## 8. HELD ENTITIES — CANONICAL hold_reason VALUES

| `hold_reason` | Triggering stage | Resolved by |
|---|---|---|
| `gps_missing` | Stage 4c GPS Gate | GPS re-run or `gps_unresolvable=true` |
| `parent_held` | Normalization Engine | Parent entity released |
| `unresolved_parent` | Upsert Engine | Parent entity upserted in partner county run |
| `unresolved_member_ids` | Upsert Engine | Member Sites upserted |
| `cross_county_candidate` | Resolution Engine Phase 0 | Cross-county resolution pass |
| `cross_county_held` | Cross-county resolution Scenario A | Partner county pipeline run |
| `unconfirmed_baseline_seed` | Discovery close-out / baseline reconciliation | Authoritative source confirms active entity; or entity confirmed non-existent |
| `identity_uncertain` | Discovery — individual identity unresolvable from available sources | Field verification or authoritative source inventory |

---

## 9. CROSS-COUNTY ENTITIES (IMP-104)

Three scenarios during resolution:
- **Scenario A** — Partner county not yet run: assign provisional `OH-{COUNTY}-{TYPE}-{SEQ}` ID,
  hold with `hold_reason = cross_county_held` pending partner run
- **Scenario B** — Collision detected: merge to `OH-MC-{TYPE}-{SEQ}` immediately
- **Scenario C** — Known MC ID already in DB: use `KNOWN_MC:{id}` flag in `identity_notes_raw`

Bootstrap pre-discovery check: always query DB for existing MC entities referencing the
target county before discovery begins. See `processing/na_cross_county_resolution_v6.0.md` §5.

**Sequence number gaps are expected** (IMP-117) — do not infer missing entities from gaps.

---

## 10. CRITICAL PROTOCOL RULES

### Cross-Cutting Change Protocol
When any change affects a field, count, name, or rule that appears in multiple
modules — adding a field, renaming a field, changing a field count, retiring an
entity type, or any similar structural change — **the manifest is the checklist**.

Before writing any edit:
1. Read `na_module_manifest_v6.0.md` and identify every module in every domain
   the change touches.
2. For a field on entity type X, the minimum checklist is:
   - Schema module
   - Vocabulary module (if the field is controlled)
   - Normalization contract
   - Discovery sub-procedure (entity-type sub-procedure)
   - Discovery Metadata Specification
   - TSV output specification
   - TSV integrity check
   - Every skill (na-bootstrap, na-discovery, na-entities, na-pipeline, na-quality)
     that carries a field list, template, or count for that entity type
   - Processing orchestration (if it carries a count or field reference)
   - Audit module (if it carries a count reference)
   - CLAUDE.md itself (raw record template and any count references)
3. Grep for the old field name / old count across the entire project to catch
   any module the checklist missed.
4. Do not report a change complete until every module on the checklist has been
   explicitly confirmed updated or confirmed not applicable — with a reason for each.

**Reasoning about which modules "seem relevant" is not a substitute for this
process.** The manifest is the authoritative inventory. Use it.

### Trailthing No-Classification Mandate
**Never classify a Trailthing** as trail, trail segment, trail network, or any other
sub-type during discovery, resolution, or normalization. Capture `source_term_raw`
verbatim — that is the discoverer's entire classification obligation. The Resolution
Engine passes `source_term` through unchanged. Classification is deferred to after
sufficient county runs under v6.x (IMP-007).

### File Writing (IMP-106)
**Never use bash heredocs for files longer than ~30 lines.** Heredocs have a silent size
limit — content beyond the limit is truncated without error. Always use the Write/Edit
tools directly or Python `open().write()`.

### Module Version References (IMP-109)
- **Filenames** include version numbers: `na_site_normalization_v6.0.md`
- **Cross-references in module bodies** use bare titles only: `na_site_normalization.md §5`
- **The manifest** is the only authoritative source for current version numbers

### Features Field Rules
- `features_raw`: raw amenity LIST (bullets/icons from source), verbatim — NOT sentences
- `description_raw`: narrative prose — NOT an amenity list; ecological/physical character priority
- `habitat_type_raw`: ecological/natural character — NOT amenities or governance
- `features` (normalized): controlled vocabulary terms only, semicolon-delimited, alphabetized
- Activities (hiking, fishing) are prohibited in `features` — map to physical infrastructure or drop
- Named Trailthing/AP entities are prohibited in `features`

### GPS Rules
- Never estimate or infer GPS coordinates
- `gps_lat_raw` / `gps_lon_raw` as separate fields
- Sites and APs without GPS → `held_entities` unless `gps_unresolvable=true`
- Trailthings and Site Networks: GPS optional; most are `gps_unresolvable` by nature
- Previously acquired GPS is filled forward on re-runs (IMP-031) — not overwritten

### Governance Field Contamination
- `governance_raw` must contain only the managing organization's name
- GIS park type labels ("Community Park", "Neighborhood Park") are NOT governance
- Record GIS type labels in `category_raw` or `identity_notes_raw`

### Alternate Names (IMP-029)
When any source uses a name for an entity that differs from the canonical name being
recorded, always capture the alternate in `identity_notes_raw` during discovery:
`ALT NAME: '[alternate name]' — [source context]`
This applies to all four entity types. During normalization, alternate name notes pass
through to the `notes` field and must never be discarded. Never silently drop a known
alternate name in favor of the canonical name alone.

### parent_site_network_raw (not external_parent)
- The field that records a Trailthing's Site Network parent is `parent_site_network_raw`
- `external_parent_id` and `external_parent_type` are retired v5 names — do not use

### DEFECT Status (IMP-076)
If a tier was worked under wrong protocol or with missing mandatory steps, mark it
**DEFECT** in the staging file and **PENDING** in the handoff — never carry it forward as complete.

---

## 11. QUALITY AND IMPROVEMENT

**Quality module**: Read `na-quality.md` before any audit work.

**Improvement tracker**: `na_improvement_tracker_v6.md`
- Section 1 — Open items
- Section 2 — Decided, pending implementation
- Section 3 — Decided and implemented (fully closed)
- Item ID format: `IMP-###` (sequential, v6-scoped; separate from v5 IMP numbers)

When a new protocol gap is identified during county work, add it to Section 1 immediately.

---

## 12. UTILITY SCRIPTS

**v6-specific scripts** live in `/utilities/` in this v6 project folder:

| Script | Purpose |
|---|---|
| `utilities/na_run_county.py` | v6 county pipeline driver — reads JSON config, calls PipelineRunner v6 |
| `utilities/na_pipeline_core_v6.py` | v6 PipelineRunner engine — four entity types, Trailthing table |

**Shared scripts** now live in `/utilities/` in this v6 project folder:

| Script | Purpose |
|---|---|
| `na_pipeline_config_template_v6.json` | v6 county config skeleton — four entity types, all v6 fields |
| `na_feature_mapper_reference.md` | Canonical FEATURE_MAP — copy into county script, extend as needed |
| `na_plus_code.py` | Plus Code encoder — `from na_plus_code import encode_plus_code` (never subprocess) |
| `na_township_lookup.py` | Ohio MCD point-in-polygon lookup against TIGER/Line 2024 |
| `na_yaml_preprocess.py` | Pre-processes discovery YAML before `yaml.safe_load_all()` — handles `#` in values |
| `na_generate_config.py` | Reads raw discovery YAML, assigns IDs, outputs blank normalized JSON config — needs v6 update |
| `na_vocab_constants.py` | Shared vocabulary constant sets — Trailthing vocab mapped from trail vocab until v6 update |
| `na_gnis_query.py` | GNIS Ohio 2021 archive query — `gnis_by_county(county, classes)`, `gnis_cemetery_gps(county)`, `gnis_county_summary(county)`; CLI: `python na_gnis_query.py Ottawa Park Trail` |

---

## 13. STARTING A NEW COUNTY

1. Run orientation protocol (§1 above)
2. Read `na_module_manifest_v6.0.md` to confirm current filenames
3. Create county folder: `County_Spreadsheets/{County}/`
4. Create session files: raw_discovery YAML, handoff.md, session_log.md, config JSON,
   document_log.yaml, source_documents/ folder
5. Query DB for existing MC entities referencing this county:
   `processing/na_cross_county_resolution_v6.0.md` §5
6. Begin Tier 1 discovery

## RESUMING A COUNTY

1. Run orientation protocol (§1 above)
2. Read `na_module_manifest_v6.0.md`
3. Read the county handoff.md — note current tier status
4. Read `discovery/na_discovery_orchestration_v6.0.md` — verify handoff tier labels
   match canonical tier order
5. If they disagree, the module wins — correct the handoff before proceeding
6. Read the sub-procedure for the current tier before any work begins

---

*This file is a session startup guide. For authoritative procedure detail, always read
the module files in the canonical directories listed in §3. When this file and a module
conflict, the module wins.*
