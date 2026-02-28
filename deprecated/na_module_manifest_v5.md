# NATURAL AREAS PROJECT
# MODULE MANIFEST v5.1
Authoritative manifest of all modules in the Natural Areas & Trails System,
aligned to the six‑entity ontology and the v5.x discovery, normalization,
resolution, and orchestration architecture.

This manifest defines:
- All active v5.x modules
- The authoritative domain of each module
- Repository structure
- Versioning expectations

This module contains no controlled vocabularies.

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.x

- v5 architecture finalized at **50 modules** (47 → 50)
- Resolution Rules Module added (extracted from v4 Resolution Module)
- Processing Orchestration Module updated
- Bootstrap retired (skills system replaces it)
- Resolution Module retired (superseded by Resolution Engine + Resolution Rules)
- Discovery Architecture and Entity Graph Schema retired (absorbed into v5 schemas and protocol)
- Repository tree standardized
- v5.1 updates:
  - Corrected domain counts
  - Corrected repository structure
  - Corrected total module count
  - Removed erroneous “55 modules” count from v5.0 manifest

------------------------------------------------------------
# 1. ACTIVE MODULES (AUTHORITATIVE LIST)

------------------------------------------------------------
## 1.1 Schema Modules (6)

`schemas/na_site_schema_v5.md`  
`schemas/na_access_point_schema_v5.md`  
`schemas/na_trail_schema_v5.md`  
`schemas/na_trail_segment_schema_v5.md`  
`schemas/na_trail_network_schema_v5.md`  
`schemas/na_site_network_schema_v5.md`

------------------------------------------------------------
## 1.2 Vocabulary Modules (6)

`vocabularies/na_site_vocabulary_v5.md`  
`vocabularies/na_access_point_vocabulary_v5.md`  
`vocabularies/na_trail_vocabulary_v5.md`  
`vocabularies/na_trail_segment_vocabulary_v5.md`  
`vocabularies/na_trail_network_vocabulary_v5.md`  
`vocabularies/na_site_network_vocabulary_v5.md`

------------------------------------------------------------
## 1.3 Normalization Modules (8)

`normalization/na_site_normalization_v5.md`  
`normalization/na_access_point_normalization_v5.md`  
`normalization/na_trail_normalization_v5.md`  
`normalization/na_trail_segment_normalization_v5.md`  
`normalization/na_trail_network_normalization_v5.md`  
`normalization/na_site_network_normalization_v5.md`  
`normalization/na_normalization_engine_v5.md`  
`normalization/na_entity_upsert_engine_v5.md`

------------------------------------------------------------
## 1.4 Discovery System (19)

### Wrapper Modules (5)
`discovery/na_discovery_protocol_v5.md`  
`discovery/na_discovery_metadata_spec_v5.md`  
`discovery/na_discovery_output_spec_v5.md`  
`discovery/na_discovery_orchestration_v5.md`  
`discovery/na_resolution_engine_v5.md`

### Jurisdictional Discovery Sub‑Procedures (8)
`discovery/na_fed_tribal_discovery_subproc_v5.md`  
`discovery/na_state_discovery_subproc_v5.md`  
`discovery/na_district_discovery_subproc_v5.md`  
`discovery/na_county_discovery_subproc_v5.md`  
`discovery/na_township_discovery_subproc_v5.md`  
`discovery/na_municipal_discovery_subproc_v5.md`  
`discovery/na_conservancy_discovery_subproc_v5.md`  
`discovery/na_private_discovery_subproc_v5.md`

### Entity Discovery Sub‑Procedures (6)
`discovery/na_site_discovery_subproc_v5.md`  
`discovery/na_trail_discovery_subproc_v5.md`  
`discovery/na_trail_segment_discovery_subproc_v5.md`  
`discovery/na_trail_network_discovery_subproc_v5.md`  
`discovery/na_site_network_discovery_subproc_v5.md`  
`discovery/na_access_point_discovery_subproc_v5.md`

------------------------------------------------------------
## 1.5 Output Modules (7)

`output/na_tsv_output_site_v5.md`  
`output/na_tsv_output_access_point_v5.md`  
`output/na_tsv_output_trail_v5.md`  
`output/na_tsv_output_trail_segment_v5.md`  
`output/na_tsv_output_trail_network_v5.md`  
`output/na_tsv_output_site_network_v5.md`  
`output/na_tsv_integrity_check_v5.md`

------------------------------------------------------------
## 1.6 Processing & Logic Modules (4)

`processing/na_processing_v5.md`  
`processing/na_resolution_rules_v5.md`  
`processing/na_county_baseline_v5.md`  
`processing/na_child_site_rules_v5.md`

------------------------------------------------------------
## 1.7 Audit Module (1)

`audit/na_audit_and_logging_v5.md`

------------------------------------------------------------
## 1.8 Best Practices (1)

`best-practices/improved_discovery_methodology.md`

------------------------------------------------------------
## 1.9 Project Documents (2)

`README_v5.md`  
`CONTRIBUTING_v5.md`

------------------------------------------------------------
## 1.10 This Manifest (1)

`na_module_manifest_v5.md`

------------------------------------------------------------
# 2. MODULE COUNT SUMMARY

| Domain | Count |
|--------|-------|
| Schemas | 6 |
| Vocabularies | 6 |
| Normalization | 8 |
| Discovery | 19 |
| Output | 7 |
| Processing & Logic | 4 |
| Audit | 1 |
| Best Practices | 1 |
| Project Documents | 2 |
| Manifest | 1 |
| **Total** | **50** |

------------------------------------------------------------
# 3. MODULE DEPENDENCY GRAPH (HIGH‑LEVEL)

Session Initialization
|
v
Schema Modules (6)
|
v
Vocabulary Modules (6)
|
v
Normalization Modules (8)
|
v
Discovery Protocol
|
v
Discovery Modules (Tiers 1–8)
|
v
Entity Discovery (6 entity types)
|
v
Resolution Engine ← Resolution Rules Module
|
v
Normalization Engine (6 entity types)
|
v
Entity Upsert Engine
|
v
TSV Output (6 files)
|
v
TSV Integrity Check
|
v
Relationship Validation
|
v
Audit & Logging

------------------------------------------------------------
# 4. REPOSITORY STRUCTURE (CANONICAL v5)

natural-areas-project/
│
├── schemas/
├── vocabularies/
├── normalization/
├── discovery/
├── output/
├── processing/
├── audit/
├── best-practices/
│
├── README_v5.md
├── CONTRIBUTING_v5.md
└── na_module_manifest_v5.md

------------------------------------------------------------
# 5. RETIRED v4.0 MODULES

| Retired Module | Superseded By |
|----------------|---------------|
| `na_resolution.md` | Resolution Engine v5.0 + Resolution Rules v5.0 |
| `na_bootstrap.md` | Skills system |
| `schema/na_discovery_architecture.md` | Discovery Protocol v5.0 |
| `schema/na_entity_graph_schema.md` | Schemas + Upsert Engine |
| `workflow/natural-areas-project.md` | README v5.0 |

------------------------------------------------------------
# 6. VERSIONING RULES

- Each module is versioned independently  
- Breaking changes increment major  
- Clarifications increment minor  
- Formatting increments patch  
- Manifest updated whenever modules are added, retired, or renamed  

------------------------------------------------------------
# END OF MODULE MANIFEST v5.1