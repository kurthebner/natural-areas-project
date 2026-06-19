# NATURAL AREAS PROJECT — README v6.0

A statewide, document-driven, tier-ordered system for discovering, classifying,
normalizing, relating, and exporting natural areas, parks, trails, and access
infrastructure across all 88 Ohio counties, with a designed path to national expansion.

The Natural Areas System v6.x is fully modular, deterministic, and audit-ready.
Every rule lives in exactly one authoritative module.
Every module is versioned.
Every run is reproducible.

------------------------------------------------------------
# CORE PRINCIPLE

**Discovery = Collection. Normalization = Decisions.**

Raw data is collected during discovery exactly as found. No normalization,
vocabulary enforcement, or GPS parsing occurs during discovery. All decisions
— field selection, vocabulary mapping, GPS derivation, township and municipality
assignment — happen during normalization.

------------------------------------------------------------
# KEY v6.0 CHANGES FROM v5.x

**Trailthing unified entity type** — Trail, Trail Segment, and Trail Network are
replaced by a single interim entity type called "Trailthing." The name carries no
hierarchical connotation. Trailthings capture how authoritative sources describe
trail-related entities verbatim (`source_term_raw`) without pre-classifying them.
Classification into sub-types is deferred until sufficient county data has been
collected (IMP-007). Entity type count: 6 → 4.

**No-classification mandate** — Discoverers and the pipeline must never classify
a Trailthing as trail, trail segment, or trail network. `source_term_raw` is the
primary discovery obligation for all Trailthing records.

**New Site fields** — `habitat_type` (ecological/natural character, open vocabulary),
`access_notes` (seasonal restrictions and access caveats), `last_verified_date`,
`field_verified`. These enable ecological queries and field verification tracking.

**Single Resolution pass** — Resolution Pass 2 (Access Points only) is eliminated.
AP identity in v6 uses name + governance + county + parent entity ID, not GPS proximity.

**Single GPS Gate** — The two-gate v5 design (one for Sites, one for APs) collapses
into a single gate after GPS acquisition. Trailthings and Site Networks are not gated.

**Browser as primary GPS method** — Claude in Chrome is a named, first-class GPS
acquisition method. It can navigate ArcGIS viewers, Google Maps detail cards, and
county GIS portals that static downloads cannot reach.

**Document Collection System** — A formal county-level document log
(`{county}_document_log.yaml`) tracks all downloaded maps, PDFs, GIS exports, and
field documents. `boundary_document_raw` on Site records links to boundary files.

**`parent_site_network_id` field** — Replaces the abstract `external_parent_id` /
`external_parent_type` pattern. A Trailthing's Site Network parent is now named
explicitly.

**Discovery Output Specification retired** — The raw record templates moved into
each entity's discovery sub-procedure, where they are maintained alongside the
field-level guidance that governs them.

------------------------------------------------------------
# PROJECT OVERVIEW

The Natural Areas Project builds a complete, statewide dataset of:

- Natural areas, parks, preserves, and open spaces (Sites)
- Trail systems, greenways, water trails, and trail corridors (Trailthings)
- Organizational collections and designated networks of sites (Site Networks)
- Visitor access points — trailheads, parking, boat launches (Access Points)
- Parent/child site relationships (Child Sites)

The system emphasizes:

- Identity-first ontology
- Tier-ordered discovery (Federal → State → District → County → Township →
  Municipal → Conservancy → Private → Baseline)
- Trailthing no-classification — source vocabulary preserved verbatim
- Ecological character capture (habitat_type, description priority)
- GPS accuracy without inference
- Deterministic, repeatable processing
- Zero invented data
- Full auditability
- Cross-entity relationships
- Perfect TSV delimiter integrity

------------------------------------------------------------
# SYSTEM ARCHITECTURE v6.x

The system is composed of authoritative modules in eight domains.

## 1. Schema Modules (4 active)
`schemas/na_site_schema_v6.0.md`
`schemas/na_trailthing_schema_v6.0.md`
`schemas/na_site_network_schema_v6.0.md`
`schemas/na_access_point_schema_v6.0.md`

## 2. Vocabulary Modules (4 active)
`vocabularies/na_site_vocabulary_v6.0.md`
`vocabularies/na_trailthing_vocabulary_v6.0.md`
`vocabularies/na_site_network_vocabulary_v6.0.md`
`vocabularies/na_access_point_vocabulary_v6.0.md`

## 3. Normalization Modules (6)
`normalization/na_site_normalization_v6.0.md`
`normalization/na_trailthing_normalization_v6.0.md`
`normalization/na_site_network_normalization_v6.0.md`
`normalization/na_access_point_normalization_v6.0.md`
`normalization/na_normalization_engine_v6.0.md`
`normalization/na_entity_upsert_engine_v6.0.md`

## 4. Discovery Modules (16)

### Core Discovery Modules (4)
`discovery/na_discovery_protocol_v6.0.md`
`discovery/na_discovery_orchestration_v6.0.md`
`discovery/na_discovery_metadata_spec_v6.0.md`
`discovery/na_gps_acquisition_v6.0.md`

### Tier Discovery Sub-Procedures (8)
Federal/Tribal, State, District, County, Township, Municipal,
Conservancy, Private

### Entity Discovery Sub-Procedures (4)
Site, Trailthing, Site Network, Access Point

*Note: Discovery Output Specification is retired in v6.x — raw record
templates live in each entity's discovery sub-procedure.*

## 5. Output Modules (5)
`output/na_tsv_output_site_v6.0.md`         (30 fields)
`output/na_tsv_output_trailthing_v6.0.md`   (31 fields)
`output/na_tsv_output_site_network_v6.0.md` (18 fields)
`output/na_tsv_output_access_point_v6.0.md` (20 fields)
`output/na_tsv_integrity_check_v6.0.md`

## 6. Processing Modules (6)
`processing/na_processing_orchestration_v6.0.md`  ← End-to-end pipeline
`processing/na_resolution_engine_v6.0.md`         ← Identity resolution (single pass)
`processing/na_resolution_rules_v6.0.md`          ← Resolution decision rules
`processing/na_child_site_rules_v6.0.md`          ← Parent/child site rules
`processing/na_county_baseline_v6.0.md`           ← Tier-0 baseline management
`processing/na_cross_county_resolution_v6.0.md`   ← MC entity protocol

## 7. Audit Module (1)
`audit/na_audit_and_logging_v6.0.md`

## 8. Root Documents
`README_v6.0.md`, `CONTRIBUTING_v6.0.md`, `na_module_manifest_v6.0.md`,
`na_improvement_tracker_v6.md`, `na_db_migration_log.md`

------------------------------------------------------------
# END-TO-END WORKFLOW (v6.x PIPELINE)

Each county is processed through a deterministic pipeline:

```
Stage 0    Module availability check
Stage 1    Discovery (Tiers 1–8)
Stage 2    Load County Baseline (Tier-0)
Stage 3    Resolution Engine (single pass)
Stage 4a   GPS Fill-Forward (IMP-031)
Stage 4b   GPS Acquisition (browser, GIS, geocoding, human assist)
Stage 4c   GPS Gate (Sites and APs; Trailthings and Site Networks not gated)
Stage 5    Normalization Engine
Stage 6    TSV Output (four files)
Stage 6.5  Vocabulary Validation Gate ← halts on violation
Stage 7    TSV Integrity Check
Stage 7.5  Human Review Gate ← pipeline halts
Stage 8    Database Upsert
Stage 9    Relationship Validation
Stage 10   Final Output Bundle
```

See `processing/na_processing_orchestration_v6.0.md` for the full specification.

------------------------------------------------------------
# RUNNING A COUNTY

1. Start with `CLAUDE.md` (project root) for session orientation
2. Use the `na-bootstrap` skill to initialize session files
3. Use the `na-discovery` skill for 8-tier discovery
4. Use the `na-pipeline` skill for post-discovery processing
5. Use the `na-quality` skill for audit and integrity checks

------------------------------------------------------------
# REPOSITORY STRUCTURE

```
Natural Areas Project v6/
├── CLAUDE.md                          ← session startup guide
├── README_v6.0.md                     ← this file
├── CONTRIBUTING_v6.0.md
├── na_module_manifest_v6.0.md         ← authoritative module inventory
├── na_improvement_tracker_v6.md       ← open and decided improvements
├── na_db_migration_log.md             ← historical DB migration records
├── na_session_log_template_v6.md      ← county session log template
├── na_pipeline_config_template_v6.json← county pipeline config skeleton
├── schemas/           (4 modules)
├── vocabularies/      (4 modules)
├── normalization/     (6 modules)
├── discovery/         (16 modules)
├── output/            (5 modules)
├── processing/        (6 modules)
├── audit/             (1 module)
└── utilities/         (4 v6 scripts; shared scripts in v5/utilities/)
```

------------------------------------------------------------
# DESIGN PRINCIPLES

- **Determinism** — same inputs → same outputs
- **Transparency** — every decision logged
- **Non-invention** — no fabricated data
- **Strict formatting** — TSVs with perfect delimiter integrity
- **Modularity** — each rule lives in exactly one place
- **Auditability** — every step traceable
- **Ontology-driven design** — identity first, classification second
- **No-classification for Trailthings** — source vocabulary preserved verbatim
- **Tier-ordered discovery** — authoritative sources always win
- **Collection-decision separation** — discovery collects, normalization decides
- **Ecological priority** — description and habitat_type capture land character
  before amenity inventory

------------------------------------------------------------
# END OF README v6.0
