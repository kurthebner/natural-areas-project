# NATURAL AREAS PROJECT — SESSION BOOTSTRAP MODULE v1
A deterministic startup sequence for activating the Natural Areas system.  
This module defines the upload order, activation command, and session health checks.

This module contains no controlled vocabularies.

---

# 1. PURPOSE
The Session Bootstrap Module ensures:

- All modules load in the correct order  
- No module is missing or overwritten  
- The AI activates the correct system state  
- The session is deterministic and reproducible  

This is the authoritative ignition file for the Natural Areas system.

---

# 2. REQUIRED MODULES AND FILENAMES
All modules must be uploaded exactly as listed below.

## 2.1 Schema Modules
- schema/na_site_schema.md  
- schema/na_access_point_schema.md  

## 2.2 Vocabulary Modules
- vocabularies/na_site_vocabulary.md  
- vocabularies/na_access_point_vocabulary.md  

## 2.3 Workflow & Logic Modules
- workflow/natural-areas-project.md  
- workflow/na_processing.md  
- workflow/na_discovery_protocol.md  
- workflow/na_resolution.md  
- workflow/na_bootstrap.md  *(this file)*

## 2.4 Normalization Modules
- normalization/na_site_normalization.md  
- normalization/na_access_point_normalization.md  

## 2.5 Output Modules
- output/na_site_tsv_specs.md  
- output/na_access_points_tsv_specs.md  
- output/na_tsv_integrity_check.md  

## 2.6 Audit & Baseline Modules
- audit/na_audit_and_logging.md  
- baseline/na_county_baseline.md  

## 2.7 Manifest
- na_module_manifest.md  

---

# 3. UPLOAD ORDER (AUTHORITATIVE)
Modules must be uploaded in this exact sequence:

1. **Schema Modules**  
2. **Vocabulary Modules**  
3. **Workflow & Logic Modules**  
4. **Normalization Modules**  
5. **Output Modules**  
6. **Audit & Baseline Modules**  
7. **Module Manifest**  
8. **This Bootstrap Module (last)**  

This guarantees deterministic module loading.

---

# 4. ACTIVATION COMMAND
After uploading all modules in the correct order, say:

**“Load these as the active Natural Areas system.”**

This triggers:

- Module registration  
- Dependency linking  
- Vocabulary binding  
- Schema activation  
- Workflow initialization  

The system is then ready to process counties.

---

# 5. SESSION HEALTH CHECK
After activation, the AI must verify:

- All modules are present  
- No duplicate modules were loaded  
- No filenames are missing  
- All schemas and vocabularies are bound  
- All workflow modules are active  
- TSV specifications and integrity rules are registered  
- Audit logging is enabled  

If any module is missing or mis‑named, the system must halt and report the issue.

---

# 6. COUNTY PROCESSING ENTRYPOINT
Once the system is active, the user may begin processing by uploading a county baseline file and saying:

**“Process this county.”**

The system will then:

1. Load the county baseline  
2. Run discovery  
3. Apply resolution rules  
4. Normalize Sites  
5. Normalize Access Points  
6. Generate TSVs  
7. Run the TSV Integrity Check  
8. Produce a full audit log  

---

# 7. VERSIONING
This module is versioned independently.  
Changes to filenames or folder structure require incrementing the version.

---

# END OF SESSION BOOTSTRAP MODULE v1