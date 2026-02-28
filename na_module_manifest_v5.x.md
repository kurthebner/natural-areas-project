# NATURAL AREAS PROJECT
# MODULE MANIFEST v5.x
(Authoritative Inventory, Structure, and Cross‑Module Dependencies for the v5.x Architecture)

This manifest defines the authoritative module inventory, directory structure,
and dependency graph for the Natural Areas Project v5.x architecture.

The manifest is **version‑agnostic within the v5 family**:
- All modules listed here are considered part of the v5.x architecture.
- Minor updates (v5.1, v5.2, v5.3…) do not require manifest changes.
- Only architectural changes (v6.0) require a new manifest.

The manifest is authoritative for:
- Module presence
- Module purpose
- Module location
- Cross‑module dependencies
- Domain counts
- Repository structure

It is **not** a version ledger. Individual modules declare their own v5.x version.

------------------------------------------------------------
# 1. DOMAIN COUNTS (TOTAL MODULES = 50)

Schemas: 6  
Vocabularies: 6  
Normalization: 8  
Discovery: 19  
Output: 7  
Processing: 4  
Audit: 1  
Best Practices: 1  
Project Docs: 2  
Manifest: 1  

Total: **50 modules**

------------------------------------------------------------
# 2. REPOSITORY STRUCTURE (CANONICAL v5.x)

The repository contains the following top-level directories and modules.  
This section intentionally avoids nested code blocks to ensure compatibility with all paste targets.

- /schemas  
  - na_site_schema_v5.x.md  
  - na_trail_schema_v5.x.md  
  - na_trail_segment_schema_v5.x.md  
  - na_access_point_schema_v5.x.md  
  - na_network_schema_v5.x.md  
  - na_entity_graph_schema_v5.x.md  

- /vocabularies  
  - na_site_vocabulary_v5.x.md  
  - na_trail_vocabulary_v5.x.md  
  - na_trail_segment_vocabulary_v5.x.md  
  - na_access_point_vocabulary_v5.x.md  
  - na_network_vocabulary_v5.x.md  
  - na_features_vocabulary_v5.x.md  

- /normalization  
  - na_site_normalization_v5.x.md  
  - na_trail_normalization_v5.x.md  
  - na_trail_segment_normalization_v5.x.md  
  - na_access_point_normalization_v5.x.md  
  - na_network_normalization_v5.x.md  
  - na_child_site_rules_v5.x.md  
  - na_county_baseline_v5.x.md  
  - na_normalization_engine_contract_v5.x.md  

- /discovery  
  - na_discovery_overview_v5.x.md  
  - na_discovery_tiers_v5.x.md  
  - na_discovery_output_spec_v5.x.md  
  - na_discovery_metadata_spec_v5.x.md  
  - na_discovery_rules_v5.x.md  
  - na_discovery_sources_v5.x.md  
  - na_discovery_county_workflow_v5.x.md  
  - na_discovery_site_rules_v5.x.md  
  - na_discovery_trail_rules_v5.x.md  
  - na_discovery_trail_segment_rules_v5.x.md  
  - na_discovery_access_point_rules_v5.x.md  
  - na_discovery_network_rules_v5.x.md  
  - na_discovery_gps_rules_v5.x.md  
  - na_discovery_location_rules_v5.x.md  
  - na_discovery_features_rules_v5.x.md  
  - na_discovery_url_rules_v5.x.md  
  - na_discovery_validation_v5.x.md  
  - na_discovery_engine_contract_v5.x.md  

- /output  
  - na_tsv_output_site_v5.x.md  
  - na_tsv_output_trail_v5.x.md  
  - na_tsv_output_trail_segment_v5.x.md  
  - na_tsv_output_access_point_v5.x.md  
  - na_tsv_output_network_v5.x.md  
  - na_tsv_integrity_check_v5.x.md  
  - na_output_engine_contract_v5.x.md  

- /processing  
  - na_resolution_engine_v5.x.md  
  - na_upsert_engine_v5.x.md  
  - na_processing_orchestration_v5.x.md  
  - na_processing_rules_v5.x.md  

- /audit  
  - na_audit_and_logging_v5.x.md  

- /best_practices  
  - na_best_practices_v5.x.md  

- /docs  
  - contributing_v5.x.md  
  - architecture_overview_v5.x.md  

- manifest_v5.x.md

------------------------------------------------------------
# 3. SCHEMA MODULES (6)

- na_site_schema_v5.x.md  
- na_trail_schema_v5.x.md  
- na_trail_segment_schema_v5.x.md  
- na_access_point_schema_v5.x.md  
- na_network_schema_v5.x.md  
- na_entity_graph_schema_v5.x.md  

**Notes:**  
- Site Schema v5.x includes the four‑tier organizational model: ownership, governance, partner_agencies, coordination.  
- All schemas define authoritative field lists and identity anchors.

------------------------------------------------------------
# 4. VOCABULARY MODULES (6)

- na_site_vocabulary_v5.x.md  
- na_trail_vocabulary_v5.x.md  
- na_trail_segment_vocabulary_v5.x.md  
- na_access_point_vocabulary_v5.x.md  
- na_network_vocabulary_v5.x.md  
- na_features_vocabulary_v5.x.md  

------------------------------------------------------------
# 5. NORMALIZATION MODULES (8)

- na_site_normalization_v5.x.md  
- na_trail_normalization_v5.x.md  
- na_trail_segment_normalization_v5.x.md  
- na_access_point_normalization_v5.x.md  
- na_network_normalization_v5.x.md  
- na_child_site_rules_v5.x.md  
- na_county_baseline_v5.x.md  
- na_normalization_engine_contract_v5.x.md  

**Notes:**  
- Site normalization includes partner_agencies handling in v5.x.  
- GIS-derived fields (municipality, township) remain engine-populated.

------------------------------------------------------------
# 6. DISCOVERY MODULES (19)

(Full list preserved exactly as in v5.0; discovery is version‑stable across v5.x.)

- na_discovery_overview_v5.x.md  
- na_discovery_tiers_v5.x.md  
- na_discovery_output_spec_v5.x.md  
- na_discovery_metadata_spec_v5.x.md  
- na_discovery_rules_v5.x.md  
- na_discovery_sources_v5.x.md  
- na_discovery_county_workflow_v5.x.md  
- na_discovery_site_rules_v5.x.md  
- na_discovery_trail_rules_v5.x.md  
- na_discovery_trail_segment_rules_v5.x.md  
- na_discovery_access_point_rules_v5.x.md  
- na_discovery_network_rules_v5.x.md  
- na_discovery_gps_rules_v5.x.md  
- na_discovery_location_rules_v5.x.md  
- na_discovery_features_rules_v5.x.md  
- na_discovery_url_rules_v5.x.md  
- na_discovery_validation_v5.x.md  
- na_discovery_engine_contract_v5.x.md  

------------------------------------------------------------
# 7. OUTPUT MODULES (7)

- na_tsv_output_site_v5.x.md  
- na_tsv_output_trail_v5.x.md  
- na_tsv_output_trail_segment_v5.x.md  
- na_tsv_output_access_point_v5.x.md  
- na_tsv_output_network_v5.x.md  
- na_tsv_integrity_check_v5.x.md  
- na_output_engine_contract_v5.x.md  

**Notes:**  
- Site TSV output uses 25 fields in v5.x.  
- Map URL and Derived Label are removed.  
- url_primary, parent_site_id, and site_id are canonical names.

------------------------------------------------------------
# 8. PROCESSING MODULES (4)

- na_resolution_engine_v5.x.md  
- na_upsert_engine_v5.x.md  
- na_processing_orchestration_v5.x.md  
- na_processing_rules_v5.x.md  

------------------------------------------------------------
# 9. AUDIT MODULES (1)

- na_audit_and_logging_v5.x.md  

------------------------------------------------------------
# 10. BEST PRACTICES (1)

- na_best_practices_v5.x.md  

------------------------------------------------------------
# 11. PROJECT DOCUMENTATION (2)

- contributing_v5.x.md  
- architecture_overview_v5.x.md  

------------------------------------------------------------
# 12. MANIFEST (1)

- manifest_v5.x.md  

------------------------------------------------------------
# END OF MODULE MANIFEST v5.x