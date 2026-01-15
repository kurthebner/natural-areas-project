# NATURAL AREAS PROJECT — MODULE MANIFEST v1
A complete index of all modules in the Natural Areas system, aligned to the actual filenames in this repository.
This manifest defines the modular architecture, authoritative domains, and dependencies.

This module contains no controlled vocabularies.

---

# 1. PURPOSE
This manifest provides:

- A complete list of all active modules
- The authoritative domain of each module
- Module-to-module dependencies
- The repository structure
- Versioning expectations

This ensures architectural clarity, determinism, and zero duplication of rules.

---

# 2. ACTIVE MODULES (AUTHORITATIVE LIST)

Below is the full set of modules that define the Natural Areas system, mapped to your actual filenames.

---

## 2.1 Schema Modules

### Site Schema Module v1
schema/na_site_schema.md

### Access Point Schema Module v1
schema/na_access_point_schema.md

---

## 2.2 Vocabulary Modules

### Site Vocabulary Module v1
vocabularies/na_site_vocabulary.md

### Access Point Vocabulary Module v1
vocabularies/na_access_point_vocabulary.md

---

## 2.3 Workflow & Logic Modules

### Overview & Workflow Module v1
workflow/natural-areas-project.md

### Processing Orchestration Module v1
workflow/na_processing.md

### Discovery Protocol Module v1
workflow/na_discovery_protocol.md

### Resolution Module v1
workflow/na_resolution.md

### Session Bootstrap Module v1
workflow/na_bootstrap.md

---

## 2.4 Normalization Modules

### Site Normalization Contract v1
normalization/na_site_normalization.md

### Access Point Normalization Contract v1
normalization/na_access_point_normalization.md

---

## 2.5 Output Modules

### Site TSV Output Specification v1
output/na_site_tsv_specs.md

### Access Point TSV Output Specification v1
output/na_access_points_tsv_specs.md

### TSV Integrity Check Module v1
output/na_tsv_integrity_check.md

---

## 2.6 Audit & Baseline Modules

### Audit & Logging Module v1
audit/na_audit_and_logging.md

### County Baseline Module v1
baseline/na_county_baseline.md

---

## 2.7 Manifest

### Module Manifest v1
na_module_manifest.md

---

# 3. MODULE DEPENDENCY GRAPH (ASCII)

                          +----------------------+
                          |  Session Bootstrap   |
                          |        v1            |
                          +/---------+-----------+
                          /          |
                         v           v
+----------------------+     +-----------------------+
|  Site Schema v1      |     | Access Point Schema v1|
|  (na_site_schema)    |     | (na_access_point...)  |
+----------+-----------+     +-----------+-----------+
           |                             |
           v                             v
+----------------------+     +-----------------------+
| Site Vocabulary v1   |     | Access Point Vocab v1 |
| (na_site_vocabulary) |     | (na_access_point...)  |
+----------+-----------+     +-----------+-----------+
           |                             |
           v                             v
+----------------------+     +-----------------------+
| Site Normalization   |     | Access Point Normal.  |
| (na_site_normal...)  |     | (na_access_point...)  |
+----------+-----------+     +-----------+-----------+
           |                             |
           v                             v
+----------------------+     +-----------------------+
| Site TSV Spec v1     |     | Access Point TSV Spec |
| (na_site_tsv_specs)  |     | (na_access_points...) |
+----------+-----------+     +-----------+-----------+
           \                             \
            \                             \
             v                             v
           +-------------------------------+
           |   TSV Integrity Check v1      |
           |   (na_tsv_integrity_check)    |
           +-------------------------------+
                         |
                         v
           +-------------------------------+
           |     Audit & Logging v1        |
           |   (na_audit_and_logging)      |
           +-------------------------------+
                         |
                         v
           +-------------------------------+
           | Processing Orchestration v1   |
           |       (na_processing)         |
           +-------------------------------+
                         |
                         v
           +-------------------------------+
           |     Discovery Protocol v1     |
           |   (na_discovery_protocol)     |
           +-------------------------------+
                         |
                         v
           +-------------------------------+
           |      Resolution Module v1     |
           |        (na_resolution)        |
           +-------------------------------+
                         |
                         v
           +-------------------------------+
           |   County Baseline Module v1   |
           |     (na_county_baseline)      |
           +-------------------------------+

---

# 4. RECOMMENDED REPOSITORY STRUCTURE (USING YOUR FILENAMES)

natural-areas-project/
│
├── audit/
│   └── na_audit_and_logging.md
│
├── baseline/
│   ├── na_county_baseline.md
│   └── counties/
│
├── normalization/
│   ├── na_access_point_normalization.md
│   └── na_site_normalization.md
│
├── output/
│   ├── na_access_points_tsv_specs.md
│   ├── na_site_tsv_specs.md
│   └── na_tsv_integrity_check.md
│
├── schema/
│   ├── na_access_point_schema.md
│   └── na_site_schema.md
│
├── vocabularies/
│   ├── na_access_point_vocabulary.md
│   └── na_site_vocabulary.md
│
├── workflow/
│   ├── natural-areas-project.md
│   ├── na_bootstrap.md
│   ├── na_discovery_protocol.md
│   ├── na_processing.md
│   └── na_resolution.md
│
└── na_module_manifest.md

---

# 5. VERSIONING RULES
- Each module is versioned independently.
- Breaking changes increment the major version.
- Clarifications increment the minor version.
- All changes must be documented in the module itself.

---

# 6. MODULE STATUS
All modules listed here are active, authoritative, and aligned with the filenames in this repository.

---

# END OF MODULE MANIFEST v1