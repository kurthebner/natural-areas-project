# NATURAL AREAS PROJECT — MODULE MANIFEST v3.1
Authoritative manifest of all modules in the statewide Natural Areas & Trails
System, aligned to the seven‑entity ontology and the v3.1 discovery,
normalization, and orchestration architecture.

This manifest defines:
- All active modules
- The authoritative domain of each module
- Module‑to‑module dependencies
- Repository structure
- Versioning expectations

This module contains no controlled vocabularies.

------------------------------------------------------------
# 1. PURPOSE

This manifest provides:

- A complete list of all active modules
- The authoritative domain of each module
- The dependency graph across schemas, vocabularies, normalization, discovery,
  orchestration, and output
- The repository structure
- Versioning rules

This ensures architectural clarity, determinism, and zero duplication of rules.

------------------------------------------------------------
# 2. ACTIVE MODULES (AUTHORITATIVE LIST)

Mapped directly to the actual repository structure.

------------------------------------------------------------
# 2.1 Schema Modules (Entity Definitions)

`schema/na_site_schema.md`  
`schema/na_sub-site_schema.md`  
`schema/na_trail_schema.md`  
`schema/na_trail_segment_schema.md`  
`schema/na_trail_network_schema.md`  
`schema/na_site_network_schema.md`  
`schema/na_access_point_schema.md`  
`schema/na_access_point_association.md`

------------------------------------------------------------
# 2.2 Vocabulary Modules

`vocabularies/na_site_vocabulary.md`  
`vocabularies/na_sub-site_vocabulary.md`  
`vocabularies/na_trail_vocabulary.md`  
`vocabularies/na_trail_segment_vocabulary.md`  
`vocabularies/na_trail_network_vocabulary.md`  
`vocabularies/na_site_network_vocabulary.md`  
`vocabularies/na_access_point_vocabulary.md`

------------------------------------------------------------
# 2.3 Normalization Modules

`normalization/na_site_normalization.md`  
`normalization/na_sub-site_normalization.md`  
`normalization/na_access_point_normalization.md`  
`normalization/na_trail_normalization.md`  
`normalization/na_trail_segment_normalization.md`  
`normalization/na_trail_network_normalization.md`  
`normalization/na_site_network_normalization.md`

------------------------------------------------------------
# 2.4 Discovery System (Stem + Leaf Modules)

## Stem & Specifications
`workflow/na_discovery_protocol.md`  
`workflow/na_discovery_metadata_spec.md`  
`workflow/na_discovery_output_spec.md`  
`workflow/na_discovery_orchestration.md`

## Jurisdictional Discovery Sub‑Procedures
`workflow/na_county_discovery_subproc.md`  
`workflow/na_municipal_discovery_subproc.md`  
`workflow/na_township_discovery_subproc.md`  
`workflow/na_state_discovery_subproc.md`  
`workflow/na_fed_tribal_discovery_subproc.md`  
`workflow/na_park_district_discovery_subproc.md`  
`workflow/na_private_discovery_subproc.md`  
`workflow/na_conservancy_discovery_subproc.md`

## Entity‑Specific Discovery Sub‑Procedures
`workflow/na_site_discovery_subproc.md`  
`workflow/na_sub-site_discovery_subproc.md`  
`workflow/na_trail_discovery_subproc.md`  
`workflow/na_trail_segment_discovery_subproc.md`  
`workflow/na_trail_network_discovery_subproc.md`  
`workflow/na_site_network_discovery_subproc.md`  
`workflow/na_access_point_discovery_subproc.md`

------------------------------------------------------------
# 2.5 Output Modules

`output/na_site_tsv_specs.md`  
`output/na_sub-site_tsv_specs.md`  
`output/na_access_point_tsv_specs.md`  
`output/na_trail_tsv_specs.md`  
`output/na_trail_segment_tsv_specs.md`  
`output/na_trail_network_tsv_specs.md`  
`output/na_site_network_tsv_specs.md`  
`output/na_tsv_integrity_check.md`

------------------------------------------------------------
# 2.6 Workflow & Logic Modules

`workflow/natural-areas-project.md`  
`workflow/na_bootstrap.md`  
`workflow/na_processing.md`  
`workflow/na_resolution.md`

------------------------------------------------------------
# 2.7 Audit & Baseline Modules

`audit/na_audit_and_logging.md`  
`baseline/na_county_baseline.md`

------------------------------------------------------------
# 2.8 Manifest

`na_module_manifest.md`

------------------------------------------------------------
# 3. MODULE DEPENDENCY GRAPH (HIGH‑LEVEL)

                  +----------------------+
                  |  Session Bootstrap   |
                  +----------+-----------+
                             |
                             v
                   +---------------------+
                   |   Schema Modules    |
                   +----------+----------+
                              |
                              v
                   +---------------------+
                   | Vocabulary Modules  |
                   +----------+----------+
                              |
                              v
                   +---------------------+
                   | Normalization Mods  |
                   +----------+----------+
                              |
                              v
                   +---------------------+
                   | Discovery Protocol  |
                   +----------+----------+
                              |
                              v
                   +---------------------+
                   | Discovery Modules   |
                   +----------+----------+
                              |
                              v
                   +---------------------+
                   |  Resolution Module  |
                   +----------+----------+
                              |
                              v
                   +---------------------+
                   | Processing Orches.  |
                   +----------+----------+
                              |
                              v
                   +---------------------+
                   | TSV Output Modules  |
                   +----------+----------+
                              |
                              v
                   +---------------------+
                   | TSV Integrity Check |
                   +----------+----------+
                              |
                              v
                   +---------------------+
                   | Audit & Logging     |
                   +---------------------+

------------------------------------------------------------
# 4. RECOMMENDED REPOSITORY STRUCTURE

natural-areas-project/  
│  
├── schema/  
│   ├── na_site_schema.md  
│   ├── na_sub-site_schema.md  
│   ├── na_trail_schema.md  
│   ├── na_trail_segment_schema.md  
│   ├── na_trail_network_schema.md  
│   ├── na_site_network_schema.md  
│   ├── na_access_point_schema.md  
│   └── na_access_point_association.md  
│  
├── vocabularies/  
│   ├── na_site_vocabulary.md  
│   ├── na_sub-site_vocabulary.md  
│   ├── na_trail_vocabulary.md  
│   ├── na_trail_segment_vocabulary.md  
│   ├── na_trail_network_vocabulary.md  
│   ├── na_site_network_vocabulary.md  
│   └── na_access_point_vocabulary.md  
│  
├── normalization/  
│   ├── na_site_normalization.md  
│   ├── na_sub-site_normalization.md  
│   ├── na_access_point_normalization.md  
│   ├── na_trail_normalization.md  
│   ├── na_trail_segment_normalization.md  
│   ├── na_trail_network_normalization.md  
│   └── na_site_network_normalization.md  
│  
├── workflow/  
│   ├── natural-areas-project.md  
│   ├── na_bootstrap.md  
│   ├── na_processing.md  
│   ├── na_resolution.md  
│   ├── na_discovery_protocol.md  
│   ├── na_discovery_metadata_spec.md  
│   ├── na_discovery_output_spec.md  
│   ├── na_discovery_orchestration.md  
│   ├── na_county_discovery_subproc.md  
│   ├── na_municipal_discovery_subproc.md  
│   ├── na_township_discovery_subproc.md  
│   ├── na_state_discovery_subproc.md  
│   ├── na_fed_tribal_discovery_subproc.md  
│   ├── na_park_district_discovery_subproc.md  
│   ├── na_private_discovery_subproc.md  
│   ├── na_conservancy_discovery_subproc.md  
│   ├── na_site_discovery_subproc.md  
│   ├── na_sub-site_discovery_subproc.md  
│   ├── na_trail_discovery_subproc.md  
│   ├── na_trail_segment_discovery_subproc.md  
│   ├── na_trail_network_discovery_subproc.md  
│   ├── na_site_network_discovery_subproc.md  
│   └── na_access_point_discovery_subproc.md  
│  
├── output/  
│   ├── na_site_tsv_specs.md  
│   ├── na_sub-site_tsv_specs.md  
│   ├── na_access_point_tsv_specs.md  
│   ├── na_trail_tsv_specs.md  
│   ├── na_trail_segment_tsv_specs.md  
│   ├── na_trail_network_tsv_specs.md  
│   ├── na_site_network_tsv_specs.md  
│   └── na_tsv_integrity_check.md  
│  
├── audit/  
│   └── na_audit_and_logging.md  
│  
├── baseline/  
│   └── na_county_baseline.md  
│  
└── na_module_manifest.md  

------------------------------------------------------------
# 5. VERSIONING RULES

- Each module is versioned independently.  
- Breaking changes increment the major version.  
- Clarifications increment the minor version.  
- All changes must be documented in the module itself.  

------------------------------------------------------------
# 6. MODULE STATUS

All modules listed here are active, authoritative, and aligned with the
seven‑entity ontology and the v3.1 discovery and orchestration architecture.

------------------------------------------------------------
# END OF MODULE MANIFEST v3.1