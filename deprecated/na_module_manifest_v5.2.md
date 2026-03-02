# NATURAL AREAS PROJECT
# MODULE MANIFEST v5.2
(Authoritative Inventory, Structure, and Cross-Module Dependencies for the v5.x Architecture)

This manifest defines the authoritative module inventory, directory structure,
and dependency graph for the Natural Areas Project v5.x architecture.

The manifest is **version-agnostic within the v5 family**:
- All modules listed here are considered part of the v5.x architecture.
- Minor updates (v5.1, v5.2, v5.3…) do not require manifest changes.
- Only architectural changes (v6.0) require a new manifest.

The manifest is authoritative for:
- Module presence
- Module purpose
- Module location
- Cross-module dependencies
- Domain counts
- Repository structure

It is **not** a version ledger. Individual modules declare their own v5.x version.

Cross-module references within all modules use the **v5.x** suffix, not a specific
version number. This ensures references remain valid as individual modules increment.

------------------------------------------------------------
# 1. DOMAIN COUNTS (TOTAL MODULES = 52)

Schemas: 6
Vocabularies: 6
Normalization: 8
Discovery: 19
Output: 7
Processing: 5
Audit: 1

Total: **52 modules**

Project documents (README, CONTRIBUTING, this manifest) and skills files
are not counted as modules.

------------------------------------------------------------
# 2. REPOSITORY STRUCTURE (CANONICAL v5.x)

- /schemas
  - na_site_schema_v5.x.md
  - na_trail_schema_v5.x.md
  - na_trail_segment_schema_v5.x.md
  - na_access_point_schema_v5.x.md
  - na_trail_network_schema_v5.x.md
  - na_site_network_schema_v5.x.md

- /vocabularies
  - na_site_vocabulary_v5.x.md
  - na_trail_vocabulary_v5.x.md
  - na_trail_segment_vocabulary_v5.x.md
  - na_access_point_vocabulary_v5.x.md
  - na_trail_network_vocabulary_v5.x.md
  - na_site_network_vocabulary_v5.x.md

- /normalization
  - na_normalization_engine_v5.x.md
  - na_entity_upsert_engine_v5.x.md
  - na_site_normalization_v5.x.md
  - na_trail_normalization_v5.x.md
  - na_trail_segment_normalization_v5.x.md
  - na_access_point_normalization_v5.x.md
  - na_trail_network_normalization_v5.x.md
  - na_site_network_normalization_v5.x.md

- /discovery
  - na_discovery_protocol_v5.x.md
  - na_discovery_orchestration_v5.x.md
  - na_discovery_output_spec_v5.x.md
  - na_discovery_metadata_spec_v5.x.md
  - na_gps_acquisition_v5.x.md
  - na_fed_tribal_discovery_subproc_v5.x.md
  - na_state_discovery_subproc_v5.x.md
  - na_district_discovery_subproc_v5.x.md
  - na_county_discovery_subproc_v5.x.md
  - na_township_discovery_subproc_v5.x.md
  - na_municipal_discovery_subproc_v5.x.md
  - na_conservancy_discovery_subproc_v5.x.md
  - na_private_discovery_subproc_v5.x.md
  - na_site_discovery_subproc_v5.x.md
  - na_trail_discovery_subproc_v5.x.md
  - na_trail_segment_discovery_subproc_v5.x.md
  - na_trail_network_discovery_subproc_v5.x.md
  - na_site_network_discovery_subproc_v5.x.md
  - na_access_point_discovery_subproc_v5.x.md

- /output
  - na_tsv_output_site_v5.x.md
  - na_tsv_output_trail_v5.x.md
  - na_tsv_output_trail_segment_v5.x.md
  - na_tsv_output_access_point_v5.x.md
  - na_tsv_output_trail_network_v5.x.md
  - na_tsv_output_site_network_v5.x.md
  - na_tsv_integrity_check_v5.x.md

- /processing
  - na_processing_orchestration_v5.x.md
  - na_resolution_engine_v5.x.md
  - na_resolution_rules_v5.x.md
  - na_child_site_rules_v5.x.md
  - na_county_baseline_v5.x.md

- /audit
  - na_audit_and_logging_v5.x.md

- /skills
  - na-complete-system_SKILL.md
  - na-discovery-workflow_SKILL.md
  - na-schema-vocabulary_SKILL.md
  - na-normalization-output_SKILL.md
  - na-processing-quality_SKILL.md

- README_v5.md
- CONTRIBUTING_v5.md
- na_module_manifest_v5.x.md

------------------------------------------------------------
# 3. SCHEMA MODULES (6)

- na_site_schema_v5.x.md
- na_trail_schema_v5.x.md
- na_trail_segment_schema_v5.x.md
- na_access_point_schema_v5.x.md
- na_trail_network_schema_v5.x.md
- na_site_network_schema_v5.x.md

**Notes:**
- Site Schema v5.x includes the four-tier organizational model:
  ownership, governance, partner_agencies, coordination.
- All schemas define authoritative field lists and identity anchors.
- GPS fields are gps_lat_raw and gps_lon_raw at discovery stage;
  gps_lat and gps_lon (normalized numeric, WGS84 decimal degrees) after normalization.

------------------------------------------------------------
# 4. VOCABULARY MODULES (6)

- na_site_vocabulary_v5.x.md
- na_trail_vocabulary_v5.x.md
- na_trail_segment_vocabulary_v5.x.md
- na_access_point_vocabulary_v5.x.md
- na_trail_network_vocabulary_v5.x.md
- na_site_network_vocabulary_v5.x.md

------------------------------------------------------------
# 5. NORMALIZATION MODULES (8)

- na_normalization_engine_v5.x.md
- na_entity_upsert_engine_v5.x.md
- na_site_normalization_v5.x.md
- na_trail_normalization_v5.x.md
- na_trail_segment_normalization_v5.x.md
- na_access_point_normalization_v5.x.md
- na_trail_network_normalization_v5.x.md
- na_site_network_normalization_v5.x.md

**Notes:**
- Site normalization includes partner_agencies handling.
- GIS-derived fields (municipality, township) are engine-populated during
  normalization; never populated from web sources during discovery.
- Entity Upsert Engine handles merge and deduplication logic.

------------------------------------------------------------
# 6. DISCOVERY MODULES (19)

## 6.1 Wrapper Modules (4)

- na_discovery_protocol_v5.x.md
- na_discovery_orchestration_v5.x.md
- na_discovery_output_spec_v5.x.md
- na_discovery_metadata_spec_v5.x.md

## 6.2 GPS Acquisition Module (1)

- na_gps_acquisition_v5.x.md

Inserted between Resolution Pass 1 and Resolution Pass 2 in the pipeline.
Defines the 11-step, 5-stage GPS acquisition workflow for all entity types.

## 6.3 Jurisdictional Discovery Sub-Procedures (8)

Tier-ordered. Must be executed in this sequence:

- na_fed_tribal_discovery_subproc_v5.x.md     (Tier 1)
- na_state_discovery_subproc_v5.x.md          (Tier 2)
- na_district_discovery_subproc_v5.x.md       (Tier 3)
- na_county_discovery_subproc_v5.x.md         (Tier 4)
- na_township_discovery_subproc_v5.x.md       (Tier 5)
- na_municipal_discovery_subproc_v5.x.md      (Tier 6)
- na_conservancy_discovery_subproc_v5.x.md    (Tier 7)
- na_private_discovery_subproc_v5.x.md        (Tier 8)

County Baseline (Tier 0) runs after Tiers 1–8, not before.
See na_county_baseline_v5.x.md in /processing.

## 6.4 Entity Discovery Sub-Procedures (6)

- na_site_discovery_subproc_v5.x.md
- na_trail_discovery_subproc_v5.x.md
- na_trail_segment_discovery_subproc_v5.x.md
- na_access_point_discovery_subproc_v5.x.md
- na_trail_network_discovery_subproc_v5.x.md
- na_site_network_discovery_subproc_v5.x.md

------------------------------------------------------------
# 7. OUTPUT MODULES (7)

- na_tsv_output_site_v5.x.md
- na_tsv_output_trail_v5.x.md
- na_tsv_output_trail_segment_v5.x.md
- na_tsv_output_access_point_v5.x.md
- na_tsv_output_trail_network_v5.x.md
- na_tsv_output_site_network_v5.x.md
- na_tsv_integrity_check_v5.x.md

**Notes:**
- Site TSV output uses the v5.x field model (25 fields).
- url_primary, parent_site_id, and site_id are canonical names.
- maps_raw is removed; map URLs are captured in urls_raw.

------------------------------------------------------------
# 8. PROCESSING MODULES (5)

- na_processing_orchestration_v5.x.md
- na_resolution_engine_v5.x.md
- na_resolution_rules_v5.x.md
- na_child_site_rules_v5.x.md
- na_county_baseline_v5.x.md

**Notes:**
- Processing Orchestration defines the full 11-step, 5-stage pipeline.
- Resolution Engine detects conflicts and merges duplicates; it does not
  resolve conflicts. Normalization resolves conflicts.
- Resolution Rules is the entity-type and category edge case catalog.
- Child Site Rules defines parent/child site assignment logic.
- County Baseline is Tier 0 — runs after Tiers 1–8, providing candidate
  seeds, not authoritative data.
- Resolution Engine and Resolution Rules files are physically located in
  /processing (their logical home), not in /discovery.

------------------------------------------------------------
# 9. AUDIT MODULES (1)

- na_audit_and_logging_v5.x.md

------------------------------------------------------------
# 10. SKILLS FILES (not modules)

Skills are Claude custom skill files used for module loading. They are
maintained separately from the module system and not counted as modules.

- na-complete-system_SKILL.md       — end-to-end orchestration
- na-discovery-workflow_SKILL.md    — all discovery modules
- na-schema-vocabulary_SKILL.md     — schemas and vocabularies
- na-normalization-output_SKILL.md  — normalization and TSV output
- na-processing-quality_SKILL.md    — processing, audit, resolution

------------------------------------------------------------
# 11. PROJECT DOCUMENTS (not modules)

- README_v5.md
- CONTRIBUTING_v5.md
- na_module_manifest_v5.2.md (this file)

------------------------------------------------------------
# END OF MODULE MANIFEST v5.2
