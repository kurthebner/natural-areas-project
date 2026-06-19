# NATURAL AREAS PROJECT
# MODULE MANIFEST v5.0
Authoritative manifest of all modules in the Natural Areas & Trails System,
aligned to the six-entity ontology and the v5.0 discovery, normalization,
resolution, and orchestration architecture.

This manifest defines:
- All active v5.0 modules
- The authoritative domain of each module
- Repository structure
- Versioning expectations

This module contains no controlled vocabularies.

------------------------------------------------------------
# CHANGES FROM v4.0

- `na_resolution_rules_v5.md` added (edge case catalog extracted from v4.0 Resolution Module)
- `na_processing_v5.md` added (updated from v4.0 Processing Orchestration Module)
- `na_bootstrap.md` retired — skills system handles module loading
- `na_resolution.md` retired — superseded by Resolution Engine v5.0 + Resolution Rules v5.0
- `na_discovery_architecture.md` retired — architecture now defined in Discovery Protocol v5.0
- `na_entity_graph_schema.md` retired — entity graph defined implicitly by schemas + upsert engine
- `na_natural-areas-project.md` retired — superseded by README v5.0
- All module filenames updated with `_v5` suffix
- Module count: 47 (v4.0) → 50 (v5.0)

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

### Jurisdictional Discovery Sub-Procedures (8)
`discovery/na_fed_tribal_discovery_subproc_v5.md`
`discovery/na_state_discovery_subproc_v5.md`
`discovery/na_district_discovery_subproc_v5.md`
`discovery/na_county_discovery_subproc_v5.md`
`discovery/na_township_discovery_subproc_v5.md`
`discovery/na_municipal_discovery_subproc_v5.md`
`discovery/na_conservancy_discovery_subproc_v5.md`
`discovery/na_private_discovery_subproc_v5.md`

### Entity Discovery Sub-Procedures (6)
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

`processing/na_processing_v5.md`          ← End-to-end pipeline orchestration
`processing/na_resolution_rules_v5.md`    ← Entity-type and category decision rules
`processing/na_county_baseline_v5.md`     ← Tier-0 baseline management
`processing/na_child_site_rules_v5.md`    ← Parent/child site assignment rules

------------------------------------------------------------
## 1.7 Audit Module (1)

`audit/na_audit_and_logging_v5.md`

------------------------------------------------------------
## 1.8 Best Practices (1)

`best-practices/improved_discovery_methodology.md`   ← Wood County lessons learned

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
| Discovery (wrappers + tier + entity) | 19 |
| Output | 7 |
| Processing & Logic | 4 |
| Audit | 1 |
| Best Practices | 1 |
| Project Documents | 2 |
| Manifest | 1 |
| **Total** | **55** |

------------------------------------------------------------
# 3. MODULE DEPENDENCY GRAPH (HIGH-LEVEL)

```
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
```

------------------------------------------------------------
# 4. REPOSITORY STRUCTURE

```
natural-areas-project/
│
├── schemas/
│   ├── na_site_schema_v5.md
│   ├── na_access_point_schema_v5.md
│   ├── na_trail_schema_v5.md
│   ├── na_trail_segment_schema_v5.md
│   ├── na_trail_network_schema_v5.md
│   └── na_site_network_schema_v5.md
│
├── vocabularies/
│   ├── na_site_vocabulary_v5.md
│   ├── na_access_point_vocabulary_v5.md
│   ├── na_trail_vocabulary_v5.md
│   ├── na_trail_segment_vocabulary_v5.md
│   ├── na_trail_network_vocabulary_v5.md
│   └── na_site_network_vocabulary_v5.md
│
├── normalization/
│   ├── na_normalization_engine_v5.md
│   ├── na_entity_upsert_engine_v5.md
│   ├── na_site_normalization_v5.md
│   ├── na_access_point_normalization_v5.md
│   ├── na_trail_normalization_v5.md
│   ├── na_trail_segment_normalization_v5.md
│   ├── na_trail_network_normalization_v5.md
│   └── na_site_network_normalization_v5.md
│
├── discovery/
│   ├── na_discovery_protocol_v5.md
│   ├── na_discovery_metadata_spec_v5.md
│   ├── na_discovery_output_spec_v5.md
│   ├── na_discovery_orchestration_v5.md
│   ├── na_resolution_engine_v5.md
│   ├── na_fed_tribal_discovery_subproc_v5.md
│   ├── na_state_discovery_subproc_v5.md
│   ├── na_district_discovery_subproc_v5.md
│   ├── na_county_discovery_subproc_v5.md
│   ├── na_township_discovery_subproc_v5.md
│   ├── na_municipal_discovery_subproc_v5.md
│   ├── na_conservancy_discovery_subproc_v5.md
│   ├── na_private_discovery_subproc_v5.md
│   ├── na_site_discovery_subproc_v5.md
│   ├── na_trail_discovery_subproc_v5.md
│   ├── na_trail_segment_discovery_subproc_v5.md
│   ├── na_trail_network_discovery_subproc_v5.md
│   ├── na_site_network_discovery_subproc_v5.md
│   └── na_access_point_discovery_subproc_v5.md
│
├── output/
│   ├── na_tsv_output_site_v5.md
│   ├── na_tsv_output_access_point_v5.md
│   ├── na_tsv_output_trail_v5.md
│   ├── na_tsv_output_trail_segment_v5.md
│   ├── na_tsv_output_trail_network_v5.md
│   ├── na_tsv_output_site_network_v5.md
│   └── na_tsv_integrity_check_v5.md
│
├── processing/
│   ├── na_processing_v5.md
│   ├── na_resolution_rules_v5.md
│   ├── na_county_baseline_v5.md
│   └── na_child_site_rules_v5.md
│
├── audit/
│   └── na_audit_and_logging_v5.md
│
├── best-practices/
│   └── improved_discovery_methodology.md
│
├── README_v5.md
├── CONTRIBUTING_v5.md
└── na_module_manifest_v5.md
```

------------------------------------------------------------
# 5. RETIRED V4.0 MODULES

The following v4.0 modules are retired and superseded:

| Retired Module | Superseded By |
|----------------|---------------|
| `na_resolution.md` | Resolution Engine v5.0 + Resolution Rules v5.0 |
| `na_bootstrap.md` | Skills system (na-processing-quality skill) |
| `schema/na_discovery_architecture.md` | Discovery Protocol v5.0 |
| `schema/na_entity_graph_schema.md` | Schemas + Entity Upsert Engine v5.0 |
| `workflow/natural-areas-project.md` | README v5.0 |

------------------------------------------------------------
# 6. VERSIONING RULES

- Each module is versioned independently
- Breaking changes increment the major version
- Clarifications or additions increment the minor version
- Formatting or non-semantic edits increment the patch version
- All changes must be documented in the module itself
- The manifest must be updated whenever modules are added, retired, or renamed

------------------------------------------------------------
# 7. MODULE STATUS

All modules listed in Section 1 are active, authoritative, and aligned with the
six-entity ontology and the v5.0 discovery, normalization, resolution, and
orchestration architecture.

------------------------------------------------------------
# END OF MODULE MANIFEST v5.0
