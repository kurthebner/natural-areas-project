# NATURAL AREAS PROJECT
# MODULE MANIFEST v5.3
(Authoritative Inventory, Structure, and Cross-Module Dependencies
for the v5.x Architecture)

This manifest defines the authoritative module inventory, directory
structure, and dependency graph for the Natural Areas Project v5.x
architecture.

The manifest is **version-agnostic within the v5 family**:
- All modules listed here are part of the v5.x architecture.
- Minor updates (v5.1, v5.2, v5.3…) do not require manifest changes.
- Only architectural changes (v6.0) require a new manifest.

The manifest is authoritative for:
- Module presence
- Module purpose
- Module location
- Cross-module dependencies
- Domain counts
- Repository structure

It is **not** a version ledger. Individual modules declare their own
v5.x version number.

------------------------------------------------------------
# CHANGELOG FROM PREVIOUS MANIFEST

- **Site Network and Trail Network split**: Previously listed as single
  na_network_* modules; now correctly listed as separate
  na_site_network_* and na_trail_network_* modules in all domains
- **GPS Acquisition Module added**: Stage 3 of the pipeline, between
  Resolution Pass 1 and Normalization; in /discovery
- **Entity sub-procedures listed explicitly**: Six entity-specific
  discovery sub-procedures
- **Tier sub-procedures listed explicitly**: Eight tier sub-procedures
- **Resolution Engine and Resolution Rules moved to /processing**
- **Entity Upsert Engine in /normalization** (not /processing)
- **Derived Label removed from all entities**: No longer computed or
  stored at any stage
- **identity_notes added to all entities**: Separate field for identity
  clarifications; sourced from identity_notes_raw
- **maps field simplified**: Plain semicolon-delimited URL list at all
  stages for all entities; rich object format retired
- **Skills directory noted** (not counted as project modules)
- **Field counts updated** in schema notes
- **Total module count: 55**

------------------------------------------------------------
# 1. DOMAIN COUNTS (TOTAL MODULES = 55)

Schemas:                            6
Vocabularies:                       6
Normalization:                      8
Output:                             7
Discovery:                         19
Processing:                         5
Audit:                              1
Root docs:                          3

**By directory:**
- /schemas:       6
- /vocabularies:  6
- /normalization: 8
- /output:        7
- /discovery:    19
- /processing:    5
- /audit:         1
- root:           3 (README, CONTRIBUTING, manifest)

Total: **55 modules**

------------------------------------------------------------
# 2. REPOSITORY STRUCTURE (CANONICAL v5.x)

- /schemas
  - na_site_schema_v5.x.md
  - na_trail_schema_v5.x.md
  - na_trail_segment_schema_v5.x.md
  - na_access_point_schema_v5.x.md
  - na_site_network_schema_v5.x.md
  - na_trail_network_schema_v5.x.md

- /vocabularies
  - na_site_vocabulary_v5.x.md
  - na_trail_vocabulary_v5.x.md
  - na_trail_segment_vocabulary_v5.x.md
  - na_access_point_vocabulary_v5.x.md
  - na_site_network_vocabulary_v5.x.md
  - na_trail_network_vocabulary_v5.x.md

- /normalization
  - na_site_normalization_v5.x.md
  - na_trail_normalization_v5.x.md
  - na_trail_segment_normalization_v5.x.md
  - na_access_point_normalization_v5.x.md
  - na_site_network_normalization_v5.x.md
  - na_trail_network_normalization_v5.x.md
  - na_normalization_engine_v5.x.md
  - na_entity_upsert_engine_v5.x.md

- /output
  - na_tsv_output_site_v5.x.md
  - na_tsv_output_trail_v5.x.md
  - na_tsv_output_trail_segment_v5.x.md
  - na_tsv_output_access_point_v5.x.md
  - na_tsv_output_site_network_v5.x.md
  - na_tsv_output_trail_network_v5.x.md
  - na_tsv_integrity_check_v5.x.md

- /discovery
  - na_discovery_protocol_v5.x.md
  - na_discovery_orchestration_v5.x.md
  - na_discovery_output_spec_v5.x.md
  - na_discovery_metadata_spec_v5.x.md
  - na_gps_acquisition_v5.x.md
  - na_site_discovery_subproc_v5.x.md
  - na_trail_discovery_subproc_v5.x.md
  - na_trail_segment_discovery_subproc_v5.x.md
  - na_access_point_discovery_subproc_v5.x.md
  - na_site_network_discovery_subproc_v5.x.md
  - na_trail_network_discovery_subproc_v5.x.md
  - na_fed_tribal_discovery_subproc_v5.x.md
  - na_state_discovery_subproc_v5.x.md
  - na_district_discovery_subproc_v5.x.md
  - na_county_discovery_subproc_v5.x.md
  - na_township_discovery_subproc_v5.x.md
  - na_municipal_discovery_subproc_v5.x.md
  - na_conservancy_discovery_subproc_v5.x.md
  - na_private_discovery_subproc_v5.x.md

- /processing
  - na_processing_orchestration_v5.x.md
  - na_resolution_engine_v5.x.md
  - na_resolution_rules_v5.x.md
  - na_child_site_rules_v5.x.md
  - na_county_baseline_v5.x.md

- /audit
  - na_audit_and_logging_v5.x.md

- /skills *(operational tools — not counted as project modules)*
  - na-bootstrap_SKILL.md
  - na-discovery_SKILL.md
  - na-entities_SKILL.md
  - na-pipeline_SKILL.md
  - na-quality_SKILL.md

- README_v5.2.md
- CONTRIBUTING_v5.2.md
- na_module_manifest_v5.3.md

------------------------------------------------------------
# 3. SCHEMA MODULES (6)

- na_site_schema_v5.x.md
- na_trail_schema_v5.x.md
- na_trail_segment_schema_v5.x.md
- na_access_point_schema_v5.x.md
- na_site_network_schema_v5.x.md
- na_trail_network_schema_v5.x.md

**Notes:**
- All schemas define authoritative field lists, identity rules,
  and relationship rules.
- Derived Label is not a stored field in any schema.
- identity_notes is a normalized field in all six entity schemas.
- GPS fields (gps_lat, gps_lon) apply to Site, Trail, and Access
  Point. Trail Segment uses LineString geometry. Trail Network and
  Site Network have no GPS or geometry fields.

**Field counts (TSV output, including entity ID):**
- Site:          26 fields, 25 tab delimiters
- Trail:         19 fields, 18 tab delimiters
- Trail Segment: 17 fields, 16 tab delimiters
- Access Point:  17 fields, 16 tab delimiters
- Site Network:  15 fields, 14 tab delimiters
- Trail Network: 17 fields, 16 tab delimiters

------------------------------------------------------------
# 4. VOCABULARY MODULES (6)

- na_site_vocabulary_v5.x.md
- na_trail_vocabulary_v5.x.md
- na_trail_segment_vocabulary_v5.x.md
- na_access_point_vocabulary_v5.x.md
- na_site_network_vocabulary_v5.x.md
- na_trail_network_vocabulary_v5.x.md

**Notes:**
- Each vocabulary module is authoritative for its entity's
  controlled fields.
- Free-text fields (accessibility, identity_notes, notes,
  ownership, description) have no controlled vocabulary.
- The Features Vocabulary (formerly listed) has been retired —
  feature details are captured in site-level free-text fields.

------------------------------------------------------------
# 5. NORMALIZATION MODULES (8)

- na_site_normalization_v5.x.md
- na_trail_normalization_v5.x.md
- na_trail_segment_normalization_v5.x.md
- na_access_point_normalization_v5.x.md
- na_site_network_normalization_v5.x.md
- na_trail_network_normalization_v5.x.md
- na_normalization_engine_v5.x.md
- na_entity_upsert_engine_v5.x.md

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

- na_tsv_output_site_v5.x.md
- na_tsv_output_trail_v5.x.md
- na_tsv_output_trail_segment_v5.x.md
- na_tsv_output_access_point_v5.x.md
- na_tsv_output_site_network_v5.x.md
- na_tsv_output_trail_network_v5.x.md
- na_tsv_integrity_check_v5.x.md

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

- na_discovery_protocol_v5.x.md
  Authoritative discovery rules, philosophy, field naming
  conventions, and core extraction guidance.

- na_discovery_orchestration_v5.x.md
  Multi-tier orchestration, tier sequencing, and county-level
  workflow coordination.

- na_discovery_output_spec_v5.x.md
  Raw Discovery Record format, required fields, and field naming
  conventions (identity_notes_raw, urls_raw, url_primary_raw,
  maps_raw as URL list).

- na_discovery_metadata_spec_v5.x.md
  Discovery Metadata Record format and source_map requirements.

- na_gps_acquisition_v5.x.md
  GPS Acquisition Module. Stage 3 of the pipeline, between
  Resolution Pass 1 and Normalization. 11-step, 5-stage workflow
  for acquiring gps_lat and gps_lon for entities missing GPS
  coordinates. Applies to Site, Trail, and Access Point only.

## 7b. Entity Discovery Sub-Procedures (6)

- na_site_discovery_subproc_v5.x.md
- na_trail_discovery_subproc_v5.x.md
- na_trail_segment_discovery_subproc_v5.x.md
- na_access_point_discovery_subproc_v5.x.md
- na_site_network_discovery_subproc_v5.x.md
- na_trail_network_discovery_subproc_v5.x.md

**Notes:**
- Each entity sub-procedure defines identity rules, field-by-field
  extraction guidance, special cases, and quality checklist.
- All use identity_notes_raw, urls_raw, url_primary_raw.
- maps_raw is a plain URL list (no type/description metadata).

## 7c. Tier Discovery Sub-Procedures (8)

- na_fed_tribal_discovery_subproc_v5.x.md    (Tier 1)
- na_state_discovery_subproc_v5.x.md         (Tier 2)
- na_district_discovery_subproc_v5.x.md      (Tier 3)
- na_county_discovery_subproc_v5.x.md        (Tier 4)
- na_township_discovery_subproc_v5.x.md      (Tier 5)
- na_municipal_discovery_subproc_v5.x.md     (Tier 6)
- na_conservancy_discovery_subproc_v5.x.md   (Tier 7)
- na_private_discovery_subproc_v5.x.md       (Tier 8)

**Notes:**
- Each tier sub-procedure defines tier-specific source requirements,
  expected entity types, and verification methodology.
- Municipal sub-procedure includes mandatory map-viewing verification
  methodology.

------------------------------------------------------------
# 8. PROCESSING MODULES (5)

- na_processing_orchestration_v5.x.md
  End-to-end pipeline orchestration: Discovery → Resolution →
  GPS Acquisition → Normalization → Resolution Pass 2 → Upsert
  → TSV Output.

- na_resolution_engine_v5.x.md
  Identity resolution logic, conflict detection, and record
  merging across discovery sources.

- na_resolution_rules_v5.x.md
  Authoritative resolution decision rules and conflict-handling
  procedures.

- na_child_site_rules_v5.x.md
  Child Site identity rules, creation criteria, and relationship
  management with parent Sites.

- na_county_baseline_v5.x.md
  County baseline data structure, bootstrap procedure, and county
  completion tracking.

------------------------------------------------------------
# 9. AUDIT MODULES (1)

- na_audit_and_logging_v5.x.md
  Authoritative logging requirements across all pipeline stages.
  Defines provenance record structure, normalization log format,
  and audit trail requirements.

------------------------------------------------------------
# 10. ROOT DOCUMENTATION (3)

- README_v5.x.md
  Project overview, architecture summary, entity type definitions,
  pipeline overview, and quick-start guide.

- CONTRIBUTING_v5.x.md
  Contributor guide: module authoring standards, versioning
  conventions, field naming rules, and contribution process.

- na_module_manifest_v5.x.md *(this file)*

------------------------------------------------------------
# 11. SKILLS (NOT COUNTED AS MODULES)

The /skills directory contains operational Claude skill files used
to optimize discovery and normalization workflows. These are not
project architecture modules.

- na-complete-system_SKILL.md
- na-discovery-workflow_SKILL.md
- na-normalization-output_SKILL.md
- na-processing-quality_SKILL.md
- na-schema-vocabulary_SKILL.md

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
- gps_acquisition → site, trail, access_point normalization
  contracts (GPS-populated records feed normalization)

------------------------------------------------------------
# END OF MODULE MANIFEST v5.3
