# NATURAL AREAS PROJECT
# MODULE MANIFEST v5.24
(Authoritative Inventory, Structure, and Cross-Module Dependencies
for the v5.x Architecture)

This manifest defines the authoritative module inventory, directory
structure, and dependency graph for the Natural Areas Project v5.x
architecture.

The manifest is authoritative for:
- Module presence
- Module purpose
- Module location
- Current version of every module
- Cross-module dependencies
- Domain counts
- Repository structure

The manifest lists the **current canonical filename** (including specific version
number) for each module. Update the manifest whenever a module is versioned up.

## Versioning and Reference Convention (IMP-109)

- **Filenames** include the version number: `na_module_name_v5.N.md`
- **Document internal headers** include the version number
- **Inter-module and intra-module references** use the bare document title
  only — no version suffix. Example: `na_resolution_engine.md §5`, never
  `na_resolution_engine_v5.5.md §5`. Section citations follow the same rule.
- **This manifest** is the single authoritative source for current version
  numbers. When a module is versioned up, update this manifest. No other
  documents require changes to their cross-references.

------------------------------------------------------------
# CHANGELOG FROM PREVIOUS MANIFEST

v5.24 (2026-05-23):
- na_state_discovery_subproc_v5.5.md — internal version v5.6 → v5.7
  - IMP-132: §3.3 Division of Wildlife — ODNR Ohio Lake Map Resource ArcGIS Experience
    (`experience.arcgis.com/experience/2a39044c75b04e68872564b4c6ec0638`) added as mandatory
    GIS source for fishing lake and wildlife area centroids; cross-references §5.9 in
    na_gps_acquisition for GPS provenance protocol
  - IMP-133: §3.7 State-Owned Real Property (SORP) added — cross-agency Ohio state parcel
    enumeration and GPS fallback source; documents SORP program URL (das.ohio.gov),
    ArcGIS Export Tool URL, project CSV asset (SORP_Parcels_2023.csv), when to use, and
    data limitations
- na_gps_acquisition_v5.3.md — internal version v5.3 → v5.4
  - IMP-132: §5.9 ODNR Ohio Lake Map Resource added; §5.2 step 3 updated with pointer to
    §5.9; `"odnr_lake_map"` added to §6 Provenance Model acquisition_method values
  - IMP-133: §5.9 SORP GPS source added; §5.2 step 3 updated with pointer to §5.9;
    `"sorp_gis"` added to §6 Provenance Model acquisition_method values
- na_conservancy_discovery_subproc_v5.5.md — internal version v5.5 → v5.6
  - IMP-134: §4.5 Southwest Ohio added — Cardinal Land Conservancy entry (Hamilton, Clinton,
    Brown, Clermont counties; 18 preserves; 4 with public access as of 2026-05-23; access
    verification guidance; county run history table seeded)

v5.23 (2026-05-22):
- na_conservancy_discovery_subproc_v5.3.md → na_conservancy_discovery_subproc_v5.5.md (IMP-130)
  - §4 "Known Organizations — Running Inventory" added (modeled on State sub-procedure §4);
    subsections: §4.1 Statewide (TNC Ohio, BTA), §4.2 Northwestern Ohio/Black Swamp (BSC,
    WCOLC), §4.3 Indiana-border mandatory (ACRES Land Trust — mandatory for Williams, Defiance,
    Paulding, Van Wert, Mercer), §4.4 Trail Management (NORTA, MVHC, PARC Inc.); each entry
    includes explicit URLs, service territory, and cumulative county run history tables
  - §3.2 updated: LTA directory URL added
  - §3.5 updated: forward reference to new §4 for known Ohio organizations
  - Existing §4–§11 renumbered to §5–§12; internal cross-references updated (§4.7→§5.7, §6.1→§7.1)

v5.22 (2026-05-20):
- na_normalization_engine_v5.8.md (content update, filename unchanged)
  - IMP-113: Canonical HELD_* hold_reason vocabulary table added to §1
    Pre- and Intra-Normalization Hold Conditions — 6 canonical hold_reason values
    defined with triggering stage and resolution stage for each
  - IMP-113: Held entity TSV exclusion rule added (held entities in held_entities only)
- na_access_point_normalization_v5.2.md → na_access_point_normalization_v5.3.md
  - IMP-114: §10a AP-to-Site Reclassification added between §10 and §11 — qualifying
    criteria, disqualifying conditions, required steps, prohibition
- na_site_normalization_v5.10.md → na_site_normalization_v5.11.md
  - IMP-116: §5.18 Features — Step 5 Unmapped Token Logging added after Step 4;
    dropped tokens logged to normalization_provenance as vocabulary expansion candidates
- na-pipeline_SKILL.md updated (Stage 4, Stage 5.5, Stage 6)
  - IMP-113: Stage 4 — held entity exclusion note and vocabulary expansion candidates
    surfacing added
  - IMP-114: Stage 5.5 — AP-to-Site reclassification review item added
  - IMP-115: Stage 6 — Pre-Upsert MC Entity County Format Scan section added
- na-bootstrap_SKILL.md updated (cross-county section)
  - IMP-117: Entity Sequence Numbering Gaps note added — gaps are expected, causes
    documented, operators must not infer missing entities from gaps

v5.21 (2026-05-18):
- na-discovery_SKILL.md updated to v5.6
  - IMP-112: Project Orientation Protocol added as mandatory first step in every session
    - Step 1: `ls` on project root required before any module reads or data work
    - Step 2: Identify authoritative directories (/discovery, /schemas, /vocabularies,
      /normalization, /output, /processing, /audit)
    - Step 3: Read module manifest to confirm current canonical filenames
    - Step 4: Files in `deprecated/` and `Natural Areas supplelmental files/` are
      explicitly prohibited as procedure or schema references
    - Step 5: Broad Glob patterns (`**/*.md`) prohibited; manifest → filename → direct
      read is the required pattern
  - IMP-074 (Resumed Session Protocol): Step 0 added — execute IMP-112 before all
    other resumed-session steps
  - Root cause codified: failure to run `ls` at session start caused use of v4/deprecated
    files when authoritative v5.x files existed in /discovery and /schemas

v5.20 (2026-05-16):
- na_fed_tribal_discovery_subproc_v5.3.md — internal version v5.4 → v5.5
  - IMP-111: §2 Scope — VA National Cemetery Administration added
  - IMP-111: §3.7 added — VA NCA mandatory source (cem.va.gov national cemeteries + Soldiers' Lots)
- na_private_discovery_subproc_v5.3.md — internal version v5.6 → v5.7
  - IMP-111: §2 Scope — Private Cemetery added as explicit T8 type
  - IMP-111: §5.1 — mandatory cemetery enumeration step added before search queries;
    three sources: OhioGenealogyExpress.com (primary), PeopleLegacy (GPS), USGS GNIS (authoritative fallback)

v5.19 (2026-05-16):
- na_private_discovery_subproc_v5.3.md — internal version v5.5 → v5.6
  - IMP-110: §2 Scope extended to all golf courses regardless of access (replaces private-only from IMP-099)
  - IMP-110: §4 Conditions — golf course exception to no-public-access exclusion rule added
  - IMP-110: §5.1 Method 1 — mandatory Golf Course Enumeration step added (PGA.com + county CVB)
  - IMP-110: §8 Tier-Specific Expectations updated

v5.18 (2026-05-12):
- na_cross_county_resolution_v5.1.md → na_cross_county_resolution_v5.2.md (IMP-107)
  - §3.1: Universal entity ID format updated to OH-{COUNTY}-{TYPE}-{SEQ}
    (state prefix OH- mandatory; MC county code for multi-county entities)
  - §3.2: Entity type code table updated with OH-MC-* and OH-{ABBREV}-* examples
  - §3.3: Sequence management SQL updated — LIKE 'OH-MC-T-%' patterns
  - §5.1: Bootstrap queries updated to OH-MC-* patterns
  - §7.2: MC ID assignment algorithm updated — produces OH-MC-{TYPE}-{####}
  - §8: Migration records updated with current canonical IDs (OH-MC-T-0001,
    OH-MC-T-0002); Category 1 renumber table added; Non-Migration Entities
    table updated with current OH-* IDs
  - §8.5: Category 2 deletion rule added — confirmed true duplicates with
    no unique data may be deleted rather than deprecated
  - §10: Anti-patterns table updated; new row: bare {COUNTY}-{TYPE}-{SEQ}
    without OH- prefix is obsolete
- Global DB key migration (IMP-107):
  - 2,245 entity IDs renamed: {COUNTY}-{TYPE}-{SEQ} → OH-{COUNTY}-{TYPE}-{SEQ}
  - All multi-county entities (counties field >1 value) → OH-MC-{TYPE}-{SEQ}
  - 7 Category 2 duplicate trails deleted; APs reparented to canonical records
  - 4 Category 1 sequence collisions resolved by renumbering
  - 34 TSV files updated across 12 county directories
  - 15 held_entities records renamed to OH- format
  - 8 orphan trail_parents rows deleted
  - "Lucas, Ohio" → "Lucas" in 7 sites.counties values

v5.17 (2026-05-07):
- na_trail_network_vocabulary_v5.3.md → na_trail_network_vocabulary_v5.3.md (IMP-105)
  - §2.1: "Equestrian Trail Network" added to allowed values
  - §2.2: Equestrian Trail Network definition block added
  - §6.1: Four equestrian raw-value mappings added
  - Live DB: SC-TN-0001 network_type "Other" → "Equestrian Trail Network"
- na_site_network_normalization_v5.3.md → na_site_network_normalization_v5.3.md (IMP-105)
  - §5.2a schema gap note removed — org_type column now exists in DB
  - §10 auditability schema gap log instruction removed
- site_networks DB table: ALTER TABLE ADD COLUMN org_type TEXT (IMP-105)
  - 18 existing records have org_type = NULL; values populated on next pipeline run

v5.16 (2026-05-07):
- na_cross_county_resolution_v5.1.md added to /processing (IMP-104)
  - New module establishing the MC (multi-county) ID scheme for entities
    that span multiple counties; defines three cross-county scenarios (Held,
    Collision, Known), bootstrap pre-discovery DB check, discovery-time
    CROSS_COUNTY_CANDIDATE flagging, and Resolution Engine Phase 0 extension
  - MC ID format: MC-{TYPE}-{####} (e.g., MC-T-0001, MC-TN-0001)
  - Migration records: MC-T-0001 (Maumee River Water Trail, 4→1 record),
    MC-T-0002 (Wabash Cannonball Trail, 3→1 record); 7 deprecated county
    IDs; 6 access_point_parents rows updated; held_entities de-duplicated
- Processing module count: 5 → 6; Total module count: 57 → 58

v5.15 (2026-05-07):
- na_water_trail_discovery_subproc_v5.1.md added to /discovery (IMP-103)
  - New module consolidating all water trail entity typing, qualification,
    GPS, and Access Point rules previously scattered across IMP-008, IMP-009,
    IMP-019, and IMP-044
  - Covers: Water Site vs. Trail entity typing, Trail Segment segmentation
    triggers, qualification threshold (published name + 2 APs; WATER_TRAIL_REVIEW
    for near-misses), economy-of-scale GPS capture workflow, Access Point rules
    (Watercraft Access, Hazard Portage, two-record rule), multi-county handling
- Discovery module count: 19 → 20; Total module count: 56 → 57

v5.14 (2026-05-07):
- na_trail_network_vocabulary_v5.1.md → na_trail_network_vocabulary_v5.3.md
  - IMP-102: §6 replaced with enforcement-grade §6.1–§6.4 mapping tables
    (Network Type, Status, Multi-Value/Empty String Enforcement, Ambiguous Cases)
- na_trail_network_normalization_v5.1.md → na_trail_network_normalization_v5.2.md
  - IMP-102: Workflow Step 3 added — mandatory Trail Network Vocabulary §6.x read gate
  - IMP-102: §5.2 network_type — mandatory §6.1 read gate; null-and-log/REVIEW enforcement
  - IMP-102: §5.3 status — mandatory §6.2 read gate; "open"/"operational"→"Active" explicit
  - IMP-102: §5.20 Empty String Enforcement added (network_type, status)
- na_site_network_vocabulary_v5.2.md → na_site_network_vocabulary_v5.3.md
  - IMP-102: §7 replaced with enforcement-grade §7.1–§7.5 mapping tables
    (Network Type, Org Type, Status, Multi-Value/Empty String Enforcement, Ambiguous Cases)
- na_site_network_normalization_v5.1.md → na_site_network_normalization_v5.3.md
  - IMP-102: Workflow Step 3 added — mandatory Site Network Vocabulary §7.x read gate
  - IMP-102: §5.2 network_type — mandatory §7.1 read gate; null-and-log/REVIEW enforcement
  - IMP-102: §5.2a Org Type — new section; mandatory §7.2 read gate; schema gap noted
    (org_type column not yet in DB schema — normalization computes but does not upsert)
  - IMP-102: §5.3 status — mandatory §7.3 read gate; "open"/"operational"→"Active" explicit;
    "dormant"/"inactive"→"Inactive" (not "Dissolved"); REVIEW on "closed"
  - IMP-102: §5.20 Empty String Enforcement added (network_type, org_type, status)
- Live DB remediation applied (IMP-102):
  - FR-TN-0001: network_type "Greenway Network"→"Regional Greenway System"; status "Open"→"Active"
  - FR-TN-0002: status "Open"→"Active"
  - FR-TN-0003: status "Open"→"Active"
  - PAU-TN-001: network_type "National Scenic Trail"→"National Scenic Trail System"
  - SC-TN-0001: network_type "Equestrian Trail Network"→"Other" (OOV — flag for vocab expansion)
  - WA-TN-0001: network_type "Rail-trail Network"→"County Trail Network"; status "Open"→"Active"

v5.12 (2026-05-05):
- na_township_discovery_subproc_v5.4.md — internal version v5.5 → v5.6
  - IMP-099: §5.6 Township Cemeteries — Mandatory Enumeration added
- na_county_discovery_subproc_v5.3.md — internal version v5.4 → v5.5
  - IMP-099: §4.9 County Cemeteries and County Golf Courses added
- na_municipal_discovery_subproc_v5.9.md — internal version v5.11 → v5.12
  - IMP-099: §4.2 Step 2 cemetery and golf course search queries added
- na_private_discovery_subproc_v5.3.md — internal version v5.4 → v5.5
  - IMP-099: §2 Scope extended (church/family cemeteries, private golf courses)
  - IMP-099: §5.1 Method 1 cemetery and private golf course search queries added

v5.13 (2026-05-07):
- na_run_county.py v1.0 → v1.1
  - IMP-101: `check_db_integrity()` added — runs PRAGMA integrity_check and
    PRAGMA foreign_key_check before every non-dry-run pipeline execution
  - IMP-101: `load_config()` now rejects configs where `state` is a two-character
    uppercase abbreviation (e.g., "OH") — must be full name ("Ohio")
- na-pipeline skill v5.4: Pipeline Startup section updated with PRAGMA integrity
  check requirement and state field rule (IMP-101)
- Live DB: 4 run_metadata rows corrected (state "OH" → "Ohio": Defiance, Fulton,
  Lucas, Wood)

v5.12 (2026-05-07):
- na_trail_vocabulary_v5.2.md → na_trail_vocabulary_v5.2.md
  - IMP-100: §3.2 Natural Surface definition expanded (primitive, rustic, singletrack mappings)
  - IMP-100: §3.2 Paved definition expanded (chip-and-seal mapping)
  - IMP-100: §5.2 Active normalization mappings added ("open" → "Active")
  - IMP-100: §9 replaced with enforcement-grade §9.1–§9.6 mapping tables (Use Type, Surface Type,
    Origin Type, Status, Difficulty, Multi-Value and Empty String Enforcement)
- na_trail_normalization_v5.3.md → na_trail_normalization_v5.3.md
  - IMP-100: §5.3–§5.5, §5.10–§5.11 updated with mandatory §9.x read gates and enforcement
    language (null-and-log, REVIEW, compound-value rules)
  - IMP-100: §5.21 Empty String Enforcement added (all five vocabulary-controlled Trail fields)
  - Workflow step 3 added: mandatory Trail Vocabulary §9.x read before normalizing any
    vocabulary-controlled field
- na_access_point_normalization_v5.2.md → na_access_point_normalization_v5.2.md
  - IMP-100: §5.2 ap_type — mandatory AP Vocabulary §5.1 read gate added; compound type rule
    (IMP-084) codified with explicit Trailhead/Parking → "Trailhead" + features update logic;
    enforcement language (null-and-log, REVIEW) added
  - IMP-100: §5.5 status — mandatory AP Vocabulary §5.1 read gate added; "open"/"operational"
    → "Active" made explicit; null-and-log enforcement added
  - IMP-100: §5.18 Empty String Enforcement added (ap_type, status)
  - Workflow step 3 added: mandatory AP Vocabulary §5.1 read before normalizing ap_type or status
- Live DB remediation applied (IMP-100):
  - 13 Wayne County AP records: ap_type "Trailhead/Parking" → "Trailhead"; "Parking Area"
    prepended to features where not already present
  - 17 Wayne County AP records: status "Open" → "Active"
  - 6 Henry County AP records: status "" → NULL

v5.11 (2026-05-05):
- na_site_vocabulary_v5.5.md → na_site_vocabulary_v5.6.md
  - IMP-099: §7.4 Cemetery subtype inference rules added (7-step ordered rule set)
  - IMP-099: §3.1 inference exception extended to include Cemetery (was 4 categories, now 5)
  - IMP-099: Status guidance for cemeteries added to §7.4

v5.10 (2026-04-07):
- na_site_vocabulary_v5.4.md → na_site_vocabulary_v5.5.md
  - IMP-063: §7.1 Category Normalization Mapping table added (FATAL REJECT for unmappable values)
  - IMP-064: §7.3 Subtype Normalization Mapping tables by category added
  - IMP-065: §7.4 Subtype Inference Rules added; §3.1 exception clause for name-keyword inference
  - IMP-068: §7.2 Cultural Institution Name-Pattern Recognition table added
- na_site_normalization_v5.8.md → na_site_normalization_v5.9.md
  - IMP-063: §5.2 Category — full vocabulary enforcement with FATAL REJECT/REVIEW logic
  - IMP-064: §5.3 Subtype — per-category enforcement, ecological descriptor routing, Features-term detection
  - IMP-065: §5.3a Deterministic Subtype Inference added
  - IMP-066: §5.14 Municipality — explicit `get_both()` call spec and result routing added
  - IMP-068: §5.2 — CATEGORY MISMATCH flag for cultural institution name patterns
  - IMP-069: §5.17a GPS Gate added (held_entities route for GPS-null sites)
- na_gps_acquisition_v5.2.md → na_gps_acquisition_v5.3.md
  - IMP-069: §7 GPS Unresolvable Flag — definition, qualifying criteria, documentation requirements, pipeline behavior
- na_site_discovery_subproc_v5.8.md → na_site_discovery_subproc_v5.9.md
  - IMP-068: §5b Cultural Institution Category Assignment rule added
- na-pipeline_SKILL.md updated to v5.6
  - IMP-069: Stage 3c GPS Gate added; Stage 3 diagram updated

v5.9 (2026-04-05):
- na_site_normalization_v5.8.md (content update, filename unchanged):
  - IMP-053 refined: clarified that only narrow, meaningless pipeline scaffolding
    markers are stripped from Notes; substantive content is always preserved.
  - IMP-061 added (new): Notes field preservation principle — Notes is a content
    field; GPS approximation notes with location detail, MORPC/ODNR identifiers,
    source citations, verification flags, funding notes, and operational information
    must not be stripped. Strip list is narrow and explicit (see §5.19).

v5.5 (2026-03-31):
- na_site_vocabulary_v5.3.md → na_site_vocabulary_v5.4.md (four new
  Features terms: Hiking Trail, Hunting Area, Mini Golf, Wilderness Area).
- na_trail_parent_site_schema_v5.1.md added to /schemas (new module
  defining the trail_parents relationship table for contained trails).
- Schema count updated: 6 → 7.
- Domain count for /schemas updated: 6 → 7.
- Total module count updated: 55 → 56.
- na-quality_SKILL.md updated to v5.3 (post-pipeline content audit added).
- Manifest filename unchanged (authoritative file reference updated in
  §10 root docs self-reference and END marker).

v5.4 (2026-03-22):
- All module references updated to current specific versions.
- Manifest changed from version-agnostic (v5.x) to version-authoritative
  (specific filenames with version numbers).
- §4 Features note corrected: Features vocabulary is not retired; it is
  defined in na_site_vocabulary_v5.x.md §6.
- §11 Skills list corrected to match current skill filenames.
- END marker updated.

v5.3:
- Site Network and Trail Network split: Previously listed as single
  na_network_* modules; now correctly listed as separate
  na_site_network_* and na_trail_network_* modules in all domains
- GPS Acquisition Module added: Stage 3 of the pipeline, between
  Resolution Pass 1 and Normalization; in /discovery
- Entity sub-procedures listed explicitly: Six entity-specific
  discovery sub-procedures
- Tier sub-procedures listed explicitly: Eight tier sub-procedures
- Resolution Engine and Resolution Rules moved to /processing
- Entity Upsert Engine in /normalization (not /processing)
- Derived Label removed from all entities
- identity_notes added to all entities
- maps field simplified: Plain semicolon-delimited URL list
- Skills directory noted (not counted as project modules)
- Field counts updated in schema notes
- Total module count: 55

------------------------------------------------------------
# 1. DOMAIN COUNTS (TOTAL MODULES = 58)

Schemas:                            7
Vocabularies:                       6
Normalization:                      8
Output:                             7
Discovery:                         20
Processing:                         6
Audit:                              1
Root docs:                          3

**By directory:**
- /schemas:       7
- /vocabularies:  6
- /normalization: 8
- /output:        7
- /discovery:    20
- /processing:    6
- /audit:         1
- root:           3 (README, CONTRIBUTING, manifest)

Total: **58 modules**

------------------------------------------------------------
# 2. REPOSITORY STRUCTURE (CANONICAL v5.x)

- /schemas
  - na_site_schema_v5.4.md
  - na_trail_schema_v5.4.md
  - na_trail_segment_schema_v5.3.md
  - na_access_point_schema_v5.2.md
  - na_site_network_schema_v5.4.md
  - na_trail_network_schema_v5.3.md
  - na_trail_parent_site_schema_v5.1.md

- /vocabularies
  - na_site_vocabulary_v5.6.md
  - na_trail_vocabulary_v5.2.md
  - na_trail_segment_vocabulary_v5.1.md
  - na_access_point_vocabulary_v5.3.md
  - na_site_network_vocabulary_v5.3.md
  - na_trail_network_vocabulary_v5.3.md

- /normalization
  - na_site_normalization_v5.11.md
  - na_trail_normalization_v5.3.md
  - na_trail_segment_normalization_v5.1.md
  - na_access_point_normalization_v5.3.md
  - na_site_network_normalization_v5.3.md
  - na_trail_network_normalization_v5.2.md
  - na_normalization_engine_v5.8.md
  - na_entity_upsert_engine_v5.2.md

- /output
  - na_tsv_output_site_v5.2.md
  - na_tsv_output_trail_v5.1.md
  - na_tsv_output_trail_segment_v5.1.md
  - na_tsv_output_access_point_v5.1.md
  - na_tsv_output_site_network_v5.1.md
  - na_tsv_output_trail_network_v5.1.md
  - na_tsv_integrity_check_v5.3.md

- /discovery
  - na_discovery_protocol_v5.9.md
  - na_discovery_orchestration_v5.3.md
  - na_discovery_output_spec_v5.3.md
  - na_discovery_metadata_spec_v5.3.md
  - na_gps_acquisition_v5.3.md
  - na_site_discovery_subproc_v5.10.md
  - na_trail_discovery_subproc_v5.3.md
  - na_trail_segment_discovery_subproc_v5.1.md
  - na_access_point_discovery_subproc_v5.2.md
  - na_site_network_discovery_subproc_v5.1.md
  - na_trail_network_discovery_subproc_v5.2.md
  - na_fed_tribal_discovery_subproc_v5.3.md
  - na_state_discovery_subproc_v5.5.md
  - na_district_discovery_subproc_v5.7.md
  - na_county_discovery_subproc_v5.3.md
  - na_township_discovery_subproc_v5.4.md
  - na_municipal_discovery_subproc_v5.9.md
  - na_conservancy_discovery_subproc_v5.5.md
  - na_private_discovery_subproc_v5.3.md
  - na_water_trail_discovery_subproc_v5.1.md

- /processing
  - na_processing_orchestration_v5.5.md
  - na_resolution_engine_v5.5.md
  - na_resolution_rules_v5.3.md
  - na_child_site_rules_v5.4.md
  - na_county_baseline_v5.1.md
  - na_cross_county_resolution_v5.2.md

- /audit
  - na_audit_and_logging_v5.1.md

- /utilities *(pipeline runtime code — not counted as project modules)*
  - na_pipeline_core.py               — shared PipelineRunner engine (Stages 3–6)
  - na_run_county.py                  — county pipeline driver; reads JSON config, calls PipelineRunner
  - na_pipeline_config_template.json  — empty county config skeleton for new runs
  - na_feature_mapper_reference.md    — canonical FEATURE_MAP regex table
  - na_plus_code.py                   — Plus Code encoder
  - na_township_lookup.py             — Ohio MCD (township/municipality) GIS lookup
  - na_vocab_constants.py             — shared vocabulary constant sets

- /skills *(operational tools — not counted as project modules)*
  *(Working copies maintained in project root as na-*-SKILL-updated.md; install to Claude Customize area)*
  - na-bootstrap-SKILL-updated.md
  - na-discovery-SKILL-updated.md
  - na-entities-SKILL-updated.md
  - na-pipeline-SKILL-updated.md
  - na-quality-SKILL-updated.md
  - na_skills_changelog.md            — version history for all five skills

- README_v5.2.md
- CONTRIBUTING_v5.2.md
- na_module_manifest_v5.10.md

------------------------------------------------------------
# 3. SCHEMA MODULES (7)

- na_site_schema_v5.4.md
- na_trail_schema_v5.4.md
- na_trail_segment_schema_v5.3.md
- na_access_point_schema_v5.2.md
- na_site_network_schema_v5.4.md
- na_trail_network_schema_v5.3.md
- na_trail_parent_site_schema_v5.1.md

**Notes:**
- All schemas define authoritative field lists, identity rules,
  and relationship rules.
- Derived Label is not a stored field in any schema.
- identity_notes is a normalized field in all six entity schemas.
- GPS fields (gps_lat, gps_lon) apply to Site, Trail, and Access
  Point. Trail Segment uses LineString geometry. Trail Network and
  Site Network have no GPS or geometry fields.
- na_trail_parent_site_schema_v5.1.md defines the trail_parents
  relationship table (schema extension). Applies to contained
  trails only — trails wholly within one site whose access and
  legal existence depend on that site. Extra-limital trails do not
  receive a trail_parents row.

**Field counts (TSV output — entity ID is DB-only and not included):**
- Site:          25 fields, 24 tab delimiters
- Trail:         19 fields, 18 tab delimiters
- Trail Segment: 17 fields, 16 tab delimiters
- Access Point:  17 fields, 16 tab delimiters
- Site Network:  15 fields, 14 tab delimiters
- Trail Network: 17 fields, 16 tab delimiters

------------------------------------------------------------
# 4. VOCABULARY MODULES (6)

- na_site_vocabulary_v5.6.md
- na_trail_vocabulary_v5.2.md
- na_trail_segment_vocabulary_v5.1.md
- na_access_point_vocabulary_v5.3.md
- na_site_network_vocabulary_v5.3.md
- na_trail_network_vocabulary_v5.3.md

**Notes:**
- Each vocabulary module is authoritative for its entity's
  controlled fields.
- Free-text fields (accessibility, identity_notes, notes,
  ownership, description) have no controlled vocabulary.
- The Site Features controlled vocabulary is defined in
  na_site_vocabulary §6.

------------------------------------------------------------
# 5. NORMALIZATION MODULES (8)

- na_site_normalization_v5.10.md
- na_trail_normalization_v5.3.md
- na_trail_segment_normalization_v5.1.md
- na_access_point_normalization_v5.2.md
- na_site_network_normalization_v5.3.md
- na_trail_network_normalization_v5.2.md
- na_normalization_engine_v5.8.md
- na_entity_upsert_engine_v5.2.md

**Notes:**
- All six entity normalization contracts define field-by-field
  transformation rules from Resolved Entity to Normalized Entity.
- GPS normalization (gps_lat/gps_lon from gps_lat_raw/gps_lon_raw)
  applies to Site, Trail, and Access Point.
- Trail Segment uses geometry (LineString) — no GPS normalization.
- Trail Network and Site Network: no GPS or geometry fields.
- identity_notes is normalized from identity_notes_raw for all
  entities.
- maps normalizes to a plain semicolon-delimited URL list for all
  entities.

------------------------------------------------------------
# 6. OUTPUT MODULES (7)

- na_tsv_output_site_v5.2.md
- na_tsv_output_trail_v5.1.md
- na_tsv_output_trail_segment_v5.1.md
- na_tsv_output_access_point_v5.1.md
- na_tsv_output_site_network_v5.1.md
- na_tsv_output_trail_network_v5.1.md
- na_tsv_integrity_check_v5.3.md

**Notes:**
- Derived Label is not an output field for any entity.
- Parent Trail Network is not an output field for Trail or Trail
  Segment — network membership lives in the trail_network_members
  relationship table.
- maps serializes as a semicolon-delimited URL list in all TSV
  outputs.
- States Included is blank for Ohio-only networks (both Site
  Network and Trail Network).
- Member Trail IDs and Member Site IDs serialize as semicolon-
  delimited integer lists.

------------------------------------------------------------
# 7. DISCOVERY MODULES (19)

## 7a. Core Discovery Modules (5)

- na_discovery_protocol_v5.9.md
  Authoritative discovery rules, philosophy, field naming
  conventions, and core extraction guidance.

- na_discovery_orchestration_v5.3.md
  Multi-tier orchestration, tier sequencing, and county-level
  workflow coordination.

- na_discovery_output_spec_v5.3.md
  Raw Discovery Record format, required fields, and field naming
  conventions (identity_notes_raw, urls_raw, url_primary_raw,
  maps_raw as URL list).

- na_discovery_metadata_spec_v5.3.md
  Discovery Metadata Record format and source_map requirements.

- na_gps_acquisition_v5.3.md
  GPS Acquisition Module. Stage 3 of the pipeline, between
  Resolution Pass 1 and Normalization. 11-step, 5-stage workflow
  for acquiring gps_lat and gps_lon for entities missing GPS
  coordinates. Applies to Site, Trail, and Access Point only.

## 7b. Entity Discovery Sub-Procedures (6)

- na_site_discovery_subproc_v5.10.md
- na_trail_discovery_subproc_v5.3.md
- na_trail_segment_discovery_subproc_v5.1.md
- na_access_point_discovery_subproc_v5.2.md
- na_site_network_discovery_subproc_v5.1.md
- na_trail_network_discovery_subproc_v5.2.md

**Notes:**
- Each entity sub-procedure defines identity rules, field-by-field
  extraction guidance, special cases, and quality checklist.
- All use identity_notes_raw, urls_raw, url_primary_raw.
- maps_raw is a plain URL list (no type/description metadata).

## 7c. Tier Discovery Sub-Procedures (8)

- na_fed_tribal_discovery_subproc_v5.3.md    (Tier 1)
- na_state_discovery_subproc_v5.5.md         (Tier 2)
- na_district_discovery_subproc_v5.7.md      (Tier 3)
- na_county_discovery_subproc_v5.3.md        (Tier 4)
- na_township_discovery_subproc_v5.4.md      (Tier 5)
- na_municipal_discovery_subproc_v5.9.md     (Tier 6)
- na_conservancy_discovery_subproc_v5.5.md   (Tier 7)
- na_private_discovery_subproc_v5.3.md       (Tier 8)

**Notes:**
- Each tier sub-procedure defines tier-specific source requirements,
  expected entity types, and verification methodology.
- Municipal sub-procedure includes mandatory map-viewing verification
  methodology.

------------------------------------------------------------
# 8. PROCESSING MODULES (6)

- na_processing_orchestration_v5.5.md
  End-to-end pipeline orchestration: Discovery → Resolution →
  GPS Acquisition → Resolution Pass 2 → GPS Gate → Normalization
  → TSV Output → Human Review Gate → Upsert. (v5.5: GPS Gate
  moved to after Resolution Pass 2; Human Review Gate added;
  stage-label cross-reference to na-pipeline skill added.)

- na_resolution_engine_v5.5.md
  Identity resolution logic, conflict detection, and record
  merging across discovery sources.

- na_resolution_rules_v5.3.md
  Authoritative resolution decision rules and conflict-handling
  procedures.

- na_child_site_rules_v5.4.md
  Child Site identity rules, creation criteria, and relationship
  management with parent Sites.

- na_county_baseline_v5.1.md
  County baseline data structure, bootstrap procedure, and county
  completion tracking.

- na_cross_county_resolution_v5.2.md
  Multi-county entity protocol: OH-MC-* ID scheme (OH-MC-{TYPE}-{SEQ}),
  three cross-county scenarios (Held/Collision/Known), bootstrap
  pre-discovery DB check, discovery-time CROSS_COUNTY_CANDIDATE
  flagging, Resolution Engine Phase 0 extension for MC ID assignment,
  field authority rules, and migration procedure. (v5.1: inaugural
  version, IMP-104; includes migration records for MC-T-0001 and
  MC-T-0002.)

------------------------------------------------------------
# 9. AUDIT MODULES (1)

- na_audit_and_logging_v5.1.md
  Authoritative logging requirements across all pipeline stages.
  Defines provenance record structure, normalization log format,
  and audit trail requirements.

------------------------------------------------------------
# 10. ROOT DOCUMENTATION (3)

- README_v5.2.md
  Project overview, architecture summary, entity type definitions,
  pipeline overview, and quick-start guide.

- CONTRIBUTING_v5.2.md
  Contributor guide: module authoring standards, versioning
  conventions, field naming rules, and contribution process.

- na_module_manifest_v5.17.md *(this file)*

------------------------------------------------------------
# 11. SKILLS (NOT COUNTED AS MODULES)

Skills are **orchestration layers**, not self-contained procedure documents.
Each skill sequences the stages of a workflow, enforces mandatory module reads
at each stage, and defines key enforcement rules (GPS Gate, held-entity logic,
human review gates). The authoritative detail — field-level procedures, identity
rules, vocabulary definitions, acquisition protocols — lives in the modules, not
in the skills.

When a skill instructs Claude to read a module before proceeding, that read is
mandatory, not optional. The skill cannot substitute for the module: it directs
Claude to the module because the module contains content the skill does not
reproduce.

**Verification:** Each skill file ends with an explicit `# END OF NA_*_SKILL`
marker. If that marker is absent after loading, the file was truncated and must
be re-installed before the run proceeds.

**Source of truth:** The working copies of all skill files are maintained in the
project root as `na-*-SKILL-updated.md`. Install by copying to the Claude
Customize area. Version history is in `na_skills_changelog.md`.

Skills:
- na-bootstrap_SKILL.md — county run initialization; seeds staging YAML and session log
- na-discovery_SKILL.md — tier-based entity discovery (8 tiers); hands off to na-pipeline
- na-entities_SKILL.md — compact entity type reference; schemas, anchors, parent rules
- na-pipeline_SKILL.md — post-discovery pipeline orchestration (Stages 1a–6)
- na-quality_SKILL.md — QA, integrity checks, audit logging, manual review

------------------------------------------------------------
# 12. PIPELINE STAGE SUMMARY

**Stage 1 — Discovery**
Raw Discovery Records emitted per entity per tier.
Governed by: discovery_protocol, tier sub-procedures, entity
sub-procedures, discovery_output_spec, discovery_metadata_spec.

**Stage 2 — Resolution Pass 1**
Identity resolution and conflict detection on raw records.
Governed by: resolution_engine, resolution_rules.

**Stage 3 — GPS Acquisition**
GPS coordinates acquired for entities missing gps_lat/gps_lon.
Governed by: gps_acquisition.
Applies to: Site, Trail, Access Point.
Does not apply to: Trail Segment (LineString geometry), Trail
Network, Site Network (no GPS fields).

**Stage 4 — Normalization**
Raw fields transformed to normalized values per entity contract.
Governed by: entity normalization contracts, normalization_engine,
child_site_rules.

**Stage 5 — Resolution Pass 2**
Post-normalization deduplication and final conflict resolution.
Governed by: resolution_engine, resolution_rules.

**Stage 6 — Entity Upsert**
Normalized entities written to the Entity Graph.
Governed by: entity_upsert_engine.

**Stage 7 — TSV Output**
Normalized entities serialized to TSV for import.
Governed by: entity TSV output specs, tsv_integrity_check.

------------------------------------------------------------
# 13. CROSS-MODULE DEPENDENCY SUMMARY

**All entity modules depend on:**
- Their vocabulary module (controlled field values)
- resolution_engine (identity resolution)
- normalization_engine (normalization orchestration)
- entity_upsert_engine (Entity Graph integration)
- audit_and_logging (provenance)

**Additional dependencies by entity:**
- Trail Segment → Trail Schema (parent Trail validation)
- Trail Network → Trail Schema (member Trail validation)
- Site Network → Site Schema (member Site validation)
- Access Point → Site Schema and Trail Schema (identity parent
  validation)
- Child Site → Site Schema and child_site_rules

**GPS Acquisition dependencies:**
- gps_acquisition → resolution_engine (resolved entities as input)
- gps_acquisition → site, trail, access_point norm