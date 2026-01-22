# NATURAL AREAS PROJECT — SESSION BOOTSTRAP MODULE v3.2.2
A deterministic startup sequence for activating the full seven‑entity Natural
Areas System. This module defines the upload order, activation command, and
session health checks required to initialize the v3.2.2 architecture.

This module contains no controlled vocabularies.

------------------------------------------------------------
# 1. PURPOSE

The Session Bootstrap Module ensures:

- All modules load in the correct order
- No module is missing, duplicated, or overwritten
- The AI activates the correct v3.2.2 system state
- All schemas, vocabularies, workflows, and contracts are bound
- The session is deterministic and reproducible

This is the authoritative ignition file for the Natural Areas System v3.2.2.

------------------------------------------------------------
# 2. REQUIRED MODULES AND FILENAMES

All modules must be uploaded exactly as listed below.

## 2.1 Schema Modules (6)
- schema/na_site_schema.md
- schema/na_access_point_schema.md
- schema/na_trail_schema.md
- schema/na_trail_segment_schema.md
- schema/na_trail_network_schema.md
- schema/na_site_network_schema.md

## 2.2 Vocabulary Modules (6)
- vocabularies/na_site_vocabulary.md
- vocabularies/na_access_point_vocabulary.md
- vocabularies/na_trail_vocabulary.md
- vocabularies/na_trail_segment_vocabulary.md
- vocabularies/na_trail_network_vocabulary.md
- vocabularies/na_site_network_vocabulary.md

## 2.3 Workflow & Logic Modules
- workflow/natural-areas-project.md
- workflow/na_processing.md
- workflow/na_discovery_protocol.md
- workflow/na_discovery_architecture.md
- workflow/na_discovery_metadata_spec.md
- workflow/na_resolution.md
- workflow/na_bootstrap.md  *(this file)*

## 2.4 Normalization Modules (6)
- normalization/na_site_normalization.md
- normalization/na_access_point_normalization.md
- normalization/na_trail_normalization.md
- normalization/na_trail_segment_normalization.md
- normalization/na_trail_network_normalization.md
- normalization/na_site_network_normalization.md

## 2.5 Output Modules (6 + Integrity Check)
- output/na_site_tsv_specs.md
- output/na_access_point_tsv_specs.md
- output/na_trail_tsv_specs.md
- output/na_trail_segment_tsv_specs.md
- output/na_trail_network_tsv_specs.md
- output/na_site_network_tsv_specs.md
- output/na_tsv_integrity_check.md

## 2.6 Audit & Baseline Modules
- audit/na_audit_and_logging.md
- baseline/na_county_baseline.md

## 2.7 Manifest
- na_module_manifest.md

------------------------------------------------------------
# 3. UPLOAD ORDER (AUTHORITATIVE)

Modules must be uploaded in this exact sequence:

1. **Schema Modules (6)**
2. **Vocabulary Modules (6)**
3. **Workflow & Logic Modules**
4. **Normalization Modules (6)**
5. **Output Modules (6 + Integrity Check)**
6. **Audit & Baseline Modules**
7. **Module Manifest**
8. **This Bootstrap Module (last)**

This guarantees deterministic module loading.

------------------------------------------------------------
# 4. ACTIVATION COMMAND

After uploading all modules in the correct order, say:

**“Load these as the active Natural Areas system.”**

This triggers:

- Module registration
- Dependency linking
- Vocabulary binding
- Schema activation
- Workflow initialization
- Normalization contract registration
- TSV specification registration
- Integrity check registration

The system is then ready to process counties.

------------------------------------------------------------
# 5. SESSION HEALTH CHECK

After activation, the AI must verify:

- All six schema modules are present
- All six vocabulary modules are present
- All six normalization contracts are present
- All six TSV output specifications are present
- TSV Integrity Check Module is registered
- Discovery Protocol is active
- Discovery Architecture Module is active
- Discovery Metadata Spec is active
- Resolution Module is active
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
2. Run discovery (all six entities)
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
# END OF SESSION BOOTSTRAP MODULE v3.2.2