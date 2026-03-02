# NATURAL AREAS PROJECT — README v5.1

A statewide, document-driven, tier-ordered system for discovering, classifying,
normalizing, relating, and exporting natural areas, parks, trails, trail
segments, networks, and access infrastructure across all 88 Ohio counties,
with a designed path to national expansion.

The Natural Areas System v5.x is fully modular, deterministic, and audit-ready.
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
# PROJECT OVERVIEW

The Natural Areas Project builds a complete, statewide dataset of:

- Natural areas
- Parks and preserves
- Sites and Child Sites (via Child Site Rules v5.x)
- Trail systems
- Trail segments
- Trail networks
- Site networks
- Visitor access points (trailheads, parking, boat launches, etc.)

The system emphasizes:

- Identity-first ontology
- Tier-ordered discovery (Federal → State → District → County → Township → Municipal → Conservancy → Private → Baseline)
- Governance and ecological clarity
- Public access accuracy
- Deterministic, repeatable processing
- Zero invented data
- Full auditability
- Cross-entity relationships
- Perfect TSV delimiter integrity

------------------------------------------------------------
# SYSTEM ARCHITECTURE v5.x

The system is composed of 52 authoritative modules in seven domains.

## 1. Schema Modules (6)

Define field structure, identity rules, and relationship rules for each entity type.

  schemas/na_site_schema_v5.x.md
  schemas/na_trail_schema_v5.x.md
  schemas/na_trail_segment_schema_v5.x.md
  schemas/na_access_point_schema_v5.x.md
  schemas/na_trail_network_schema_v5.x.md
  schemas/na_site_network_schema_v5.x.md

## 2. Vocabulary Modules (6)

Controlled vocabularies for all vocabulary-governed fields.

  vocabularies/na_site_vocabulary_v5.x.md
  vocabularies/na_trail_vocabulary_v5.x.md
  vocabularies/na_trail_segment_vocabulary_v5.x.md
  vocabularies/na_access_point_vocabulary_v5.x.md
  vocabularies/na_trail_network_vocabulary_v5.x.md
  vocabularies/na_site_network_vocabulary_v5.x.md

## 3. Normalization Modules (8)

Entity-specific normalization contracts and engines.

  normalization/na_normalization_engine_v5.x.md
  normalization/na_entity_upsert_engine_v5.x.md
  normalization/na_site_normalization_v5.x.md
  normalization/na_trail_normalization_v5.x.md
  normalization/na_trail_segment_normalization_v5.x.md
  normalization/na_access_point_normalization_v5.x.md
  normalization/na_trail_network_normalization_v5.x.md
  normalization/na_site_network_normalization_v5.x.md

## 4. Discovery Modules (19)

### Wrapper Modules (4)
  discovery/na_discovery_protocol_v5.x.md
  discovery/na_discovery_orchestration_v5.x.md
  discovery/na_discovery_output_spec_v5.x.md
  discovery/na_discovery_metadata_spec_v5.x.md

### GPS Acquisition Module (1)
  discovery/na_gps_acquisition_v5.x.md

### Jurisdictional Discovery Sub-Procedures (8)
  Tiers 1–8: Federal/Tribal, State, District, County,
  Township, Municipal, Conservancy, Private

### Entity Discovery Sub-Procedures (6)
  Site, Trail, Trail Segment, Access Point,
  Trail Network, Site Network

## 5. Output Modules (7)

TSV specifications for all six entity types plus integrity check.

  output/na_tsv_output_site_v5.x.md
  output/na_tsv_output_trail_v5.x.md
  output/na_tsv_output_trail_segment_v5.x.md
  output/na_tsv_output_access_point_v5.x.md
  output/na_tsv_output_trail_network_v5.x.md
  output/na_tsv_output_site_network_v5.x.md
  output/na_tsv_integrity_check_v5.x.md

## 6. Processing Modules (5)

  processing/na_processing_orchestration_v5.x.md  ← End-to-end pipeline
  processing/na_resolution_engine_v5.x.md         ← Conflict detection and merge
  processing/na_resolution_rules_v5.x.md          ← Entity-type and category rules
  processing/na_child_site_rules_v5.x.md          ← Parent/child site assignment
  processing/na_county_baseline_v5.x.md           ← Tier-0 baseline management

## 7. Audit Module (1)

  audit/na_audit_and_logging_v5.x.md

------------------------------------------------------------
# KEY v5.x CHANGES FROM v4.0

**Discovery = Collection principle formalized** — discovery modules strictly
prohibit normalization, inference, or field decisions during collection.

**Township and Municipality are GIS-derived** — never populated from web sources
during discovery; GIS spatial lookup occurs during normalization.

**GPS field split** — gps_raw replaced by gps_lat_raw and gps_lon_raw at
discovery stage; normalized to gps_lat and gps_lon (WGS84 decimal degrees).

**GPS Acquisition Module added** — new five-stage, 11-step module inserted
between Resolution Pass 1 and Resolution Pass 2 in the pipeline.

**Field renames** — notes_raw renamed to identity_notes_raw; url_all renamed
to urls_raw; url_primary renamed to url_primary_raw at discovery stage.

**maps_raw removed** — map URLs are now captured in urls_raw along with all
other URL types. No separate map URL field exists.

**New raw fields** — features_raw, difficulty_raw, and accessibility_raw added
for Trails, Trail Segments, and Access Points.

**Access Point fields removed** — role_raw, access_level_raw, and their
normalized counterparts removed from Access Point schema.

**Network member tracking** — member_count and member_site_ids added to Site
Networks; member_trail_count and member_trail_ids added to Trail Networks.

**County Baseline runs last** — Baseline is Tier-0 and runs after Tiers 1–8,
not before. It provides candidate seeds, not authoritative data.

**Resolution Engine redesigned** — detects conflicts and merges duplicates but
does not resolve conflicts. Normalization resolves conflicts.

**Resolution Rules Module added** — extracts entity-type and category edge case
catalog into its own authoritative reference.

**Resolution Engine and Rules moved to processing/** — their logical home,
separate from discovery modules.

**Skills system replaces bootstrap** — module loading handled by the custom
skills system; the v4.0 bootstrap upload sequence is retired.

------------------------------------------------------------
# END-TO-END WORKFLOW (v5.x PIPELINE — 11 STEPS, 5 STAGES)

Each county is processed through a deterministic pipeline:

**Stage 1 — Discovery**
  Step 1: Run Tiers 1–8 Discovery (jurisdictional sub-procedures)
  Step 2: Run Entity Discovery Sub-Procedures
  Step 3: Load County Baseline (Tier-0)

**Stage 2 — Resolution Pass 1**
  Step 4: Apply Resolution Engine (conflict detection, deduplication)
  Step 5: Apply Resolution Rules (entity-type and category decisions)

**Stage 3 — GPS Acquisition**
  Step 6: GPS Acquisition Pass (5-stage GPS workflow for all entities)

**Stage 4 — Resolution Pass 2**
  Step 7: Apply Resolution Engine (post-GPS conflict detection)
  Step 8: Apply Resolution Rules (post-GPS decisions)

**Stage 5 — Normalization and Output**
  Step 9:  Normalize all six entity types
  Step 10: Upsert into entity graph
  Step 11: Generate six TSV files and run TSV Integrity Check

See processing/na_processing_orchestration_v5.x.md for the full specification.

------------------------------------------------------------
# RUNNING A COUNTY

The skills system handles module loading automatically. To run a county:

1. Use the na-complete-system skill (or start with na-discovery-workflow)
2. Specify the target county and state
3. Follow the 8-tier discovery sequence
4. Normalize and generate output

------------------------------------------------------------
# REPOSITORY STRUCTURE

  natural-areas-project/
  ├── schemas/           (6 modules)
  ├── vocabularies/      (6 modules)
  ├── normalization/     (8 modules)
  ├── discovery/         (19 modules)
  ├── output/            (7 modules)
  ├── processing/        (5 modules)
  ├── audit/             (1 module)
  ├── skills/            (5 skill files — not modules)
  ├── deprecated/
  ├── README_v5.md
  ├── CONTRIBUTING_v5.md
  └── na_module_manifest_v5.x.md

------------------------------------------------------------
# DESIGN PRINCIPLES

- **Determinism** — same inputs produce same outputs
- **Transparency** — every decision logged
- **Non-invention** — no fabricated data
- **Strict formatting** — TSVs with perfect delimiter integrity
- **Modularity** — each rule lives in exactly one place
- **Auditability** — every step traceable
- **Ontology-driven design** — identity first, amenities second
- **Tier-ordered discovery** — authoritative sources always win
- **Collection-decision separation** — discovery collects, normalization decides
- **Systematic beats smart** — complete every tier exhaustively before moving on

------------------------------------------------------------
# CHANGES FROM v5.0

- Module count corrected to 52 (from 55)
- Pipeline updated to 11-step, 5-stage model (from 10-step)
- GPS Acquisition Module documented as Stage 3
- Resolution Engine and Resolution Rules moved to processing/
- Field names updated throughout: identity_notes_raw, urls_raw, gps_lat_raw, gps_lon_raw
- maps_raw removal documented
- Repository structure updated to reflect deprecated/ directory
- Processing domain count corrected to 5 (from 4)

------------------------------------------------------------
# END OF README v5.1
