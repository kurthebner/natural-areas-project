# NATURAL AREAS PROJECT — SESSION BOOTSTRAP MODULE v4.0
A deterministic startup sequence for activating the full six‑entity Natural
Areas System v4.0. This module defines the upload order, activation command,
and session health checks required to initialize the v4.0 architecture.

This module contains no controlled vocabularies.

------------------------------------------------------------
# 1. PURPOSE

The Session Bootstrap Module ensures:

- All modules load in the correct order  
- No module is missing, duplicated, or overwritten  
- The AI activates the correct v4.0 system state  
- All schemas, vocabularies, workflows, and contracts are bound  
- The session is deterministic and reproducible  
- Tier‑ordered discovery and v4.0 identity rules are active  

This is the authoritative ignition file for the Natural Areas System v4.0.

------------------------------------------------------------
# 2. REQUIRED MODULES AND FILENAMES

All modules must be uploaded exactly as listed below.

## 2.1 Schema Modules
- schema/na_site_schema.md  
- schema/na_access_point_schema.md  
- schema/na_trail_schema.md  
- schema/na_trail_segment_schema.md  
- schema/na_trail_network_schema.md  
- schema/na_site_network_schema.md  
- schema/na_child_site_rules.md  
- schema/na_discovery_architecture.md  
- schema/na_entity_graph_schema.md  

## 2.2 Vocabulary Modules
- vocabularies/na_site_vocabulary.md  
- vocabularies/na_access_point_vocabulary.md  
- vocabularies/na_trail_vocabulary.md  
- vocabularies/na_trail_segment_vocabulary.md  
- vocabularies/na_trail_network_vocabulary.md  
- vocabularies/na_site_network_vocabulary.md  

## 2.3 Normalization Modules
- normalization/na_site_normalization.md  
- normalization/na_access_point_normalization.md  
- normalization/na_trail_normalization.md  
- normalization/na_trail_segment_normalization.md  
- normalization/na_trail_network_normalization.md  
- normalization/na_site_network_normalization.md  
- normalization/na_normalization_engine.md  
- normalization/na_entity_upsert_engine.md  

## 2.4 Discovery System (Stem + Leaf Modules)

### Stem & Specifications
- workflow/na_discovery_protocol.md  
- workflow/na_discovery_metadata_spec.md  
- workflow/na_discovery_output_spec.md  
- workflow/na_discovery_orchestration.md  

### Jurisdictional Discovery Sub‑Procedures
- workflow/na_county_discovery_subproc.md  
- workflow/na_municipal_discovery_subproc.md  
- workflow/na_township_discovery_subproc.md  
- workflow/na_state_discovery_subproc.md  
- workflow/na_fed_tribal_discovery_subproc.md  
- workflow/na_district_discovery_subproc.md  
- workflow/na_private_discovery_subproc.md  
- workflow/na_conservancy_discovery_subproc.md  

### Entity‑Specific Discovery Sub‑Procedures
- workflow/na_site_discovery_subproc.md  
- workflow/na_trail_discovery_subproc.md  
- workflow/na_trail_segment_discovery_subproc.md  
- workflow/na_trail_network_discovery_subproc.md  
- workflow/na_site_network_discovery_subproc.md  
- workflow/na_access_point_discovery_subproc.md  

## 2.5 Workflow & Logic Modules
- workflow/natural-areas-project.md  
- workflow/na_processing.md  
- workflow/na_resolution.md  
- workflow/na_resolution_engine.md  
- workflow/na_bootstrap.md  *(this file)*  

## 2.6 Output Modules
- output/na_site_tsv_specs.md  
- output/na_access_point_tsv_specs.md  
- output/na_trail_tsv_specs.md  
- output/na_trail_segment_tsv_specs.md  
- output/na_trail_network_tsv_specs.md  
- output/na_site_network_tsv_specs.md  
- output/na_tsv_integrity_check.md  

## 2.7 Audit & Baseline Modules
- audit/na_audit_and_logging.md  
- baseline/na_county_baseline.md  

## 2.8 Manifest
- na_module_manifest.md  

------------------------------------------------------------
# 3. UPLOAD ORDER (AUTHORITATIVE)

Modules must be uploaded in this exact sequence:

1. **Schema Modules**  
2. **Vocabulary Modules**  
3. **Normalization Modules**  
4. **Discovery System (Stem + Leaf)**  
5. **Workflow & Logic Modules**  
6. **Output Modules**  
7. **Audit & Baseline Modules**  
8. **Module Manifest**  
9. **This Bootstrap Module (last)**  

This guarantees deterministic module loading and correct v4.0 activation.

------------------------------------------------------------
# 4. ACTIVATION COMMAND

After uploading all modules in the correct order, say:

**“Load these as the active Natural Areas System v4.0.”**

This triggers:

- Module registration  
- Dependency linking  
- Vocabulary binding  
- Schema activation  
- Discovery Protocol initialization  
- Normalization contract registration  
- Resolution Engine activation  
- Processing Orchestration initialization  
- TSV specification registration  
- Integrity check registration  

The system is then ready to process counties.

------------------------------------------------------------
# 5. SESSION HEALTH CHECK

After activation, the AI must verify:

- All schema modules are present  
- All vocabulary modules are present  
- All normalization contracts are present  
- All TSV output specifications are present  
- TSV Integrity Check Module is registered  
- Discovery Protocol is active  
- Discovery Architecture is active  
- Discovery Metadata Spec is active  
- Resolution Module and Resolution Engine are active  
- Processing Orchestration Module is active  
- Audit & Logging Module is active  
- County Baseline Module is present  
- No duplicate or mis‑named modules exist  

If any module is missing or mis‑named, the system must halt and report the issue.

------------------------------------------------------------
# 6. COUNTY PROCESSING ENTRYPOINT

Once the system is active, the user may begin processing by uploading a county
baseline file and saying:

**“Process this county.”**

The system will then:

1. Load the county baseline  
2. Run tier‑ordered discovery (all six entities)  
3. Apply resolution rules  
4. Normalize Sites  
5. Normalize Access Points  
6. Normalize Trails  
7. Normalize Trail Segments  
8. Normalize Trail Networks  
9. Normalize Site Networks  
10. Generate six TSVs  
11. Run the TSV Integrity Check  
12. Validate cross‑entity relationships  
13. Produce a full audit log  

------------------------------------------------------------
# 7. VERSIONING

This module is versioned independently.  
Changes to filenames, folder structure, or module list require incrementing the version.

------------------------------------------------------------
# END OF SESSION BOOTSTRAP MODULE v4.0