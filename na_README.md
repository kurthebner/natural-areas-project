# NATURAL AREAS PROJECT — README.md (v4.0)
A statewide, document‑driven, tier‑ordered system for discovering, classifying,
normalizing, relating, and exporting natural areas, parks, trails, trail
segments, networks, and access infrastructure across all 88 Ohio counties.

The Natural Areas System v4.0 is fully modular, deterministic, and audit‑ready.
Every rule lives in exactly one authoritative module.  
Every module is versioned.  
Every run is reproducible.

------------------------------------------------------------
##  Project Overview

The Natural Areas Project builds a complete, statewide dataset of:

- Natural areas  
- Parks and preserves  
- Sites and Child Sites (via Child Site Rules v4.0)  
- Trail systems  
- Trail segments  
- Trail networks  
- Site networks  
- Visitor access points (trailheads, parking, boat launches, etc.)

The system emphasizes:

- **Identity‑first ontology**  
- **Tier‑ordered discovery** (Federal → State → District → County → Township → Municipal → Conservancy → Private → Baseline)  
- **Governance and ecological clarity**  
- **Public access accuracy**  
- **Deterministic, repeatable processing**  
- **Zero invented data**  
- **Full auditability**  
- **Cross‑entity relationships**  
- **Perfect TSV delimiter integrity**

------------------------------------------------------------
##  System Architecture (v4.0)

The system is composed of authoritative modules grouped into eight domains.

### **1. Schema Modules**
Define the field structure, identity rules, and parent/relationship rules for each entity type.

- `schema/na_site_schema.md`  
- `schema/na_access_point_schema.md`  
- `schema/na_trail_schema.md`  
- `schema/na_trail_segment_schema.md`  
- `schema/na_trail_network_schema.md`  
- `schema/na_site_network_schema.md`  
- `schema/na_child_site_rules.md`  
- `schema/na_discovery_architecture.md`  
- `schema/na_entity_graph_schema.md`

### **2. Vocabulary Modules**
Controlled vocabularies for all vocabulary‑governed fields.

- `vocabularies/na_site_vocabulary.md`  
- `vocabularies/na_access_point_vocabulary.md`  
- `vocabularies/na_trail_vocabulary.md`  
- `vocabularies/na_trail_segment_vocabulary.md`  
- `vocabularies/na_trail_network_vocabulary.md`  
- `vocabularies/na_site_network_vocabulary.md`

### **3. Normalization Modules**
Entity‑specific normalization contracts and engines.

- `normalization/na_site_normalization.md`  
- `normalization/na_access_point_normalization.md`  
- `normalization/na_trail_normalization.md`  
- `normalization/na_trail_segment_normalization.md`  
- `normalization/na_trail_network_normalization.md`  
- `normalization/na_site_network_normalization.md`  
- `normalization/na_normalization_engine.md`  
- `normalization/na_entity_upsert_engine.md`

### **4. Discovery System (Stem + Leaf Modules)**

#### Stem & Specifications
- `workflow/na_discovery_protocol.md`  
- `workflow/na_discovery_metadata_spec.md`  
- `workflow/na_discovery_output_spec.md`  
- `workflow/na_discovery_orchestration.md`

#### Jurisdictional Discovery Sub‑Procedures
- `workflow/na_county_discovery_subproc.md`  
- `workflow/na_municipal_discovery_subproc.md`  
- `workflow/na_township_discovery_subproc.md`  
- `workflow/na_state_discovery_subproc.md`  
- `workflow/na_fed_tribal_discovery_subproc.md`  
- `workflow/na_district_discovery_subproc.md`  
- `workflow/na_private_discovery_subproc.md`  
- `workflow/na_conservancy_discovery_subproc.md`

#### Entity‑Specific Discovery Sub‑Procedures
- `workflow/na_site_discovery_subproc.md`  
- `workflow/na_trail_discovery_subproc.md`  
- `workflow/na_trail_segment_discovery_subproc.md`  
- `workflow/na_trail_network_discovery_subproc.md`  
- `workflow/na_site_network_discovery_subproc.md`  
- `workflow/na_access_point_discovery_subproc.md`

### **5. Workflow & Logic Modules**
- `workflow/natural-areas-project.md`  
- `workflow/na_bootstrap.md`  
- `workflow/na_processing.md`  
- `workflow/na_resolution.md`  
- `workflow/na_resolution_engine.md`

### **6. Output Modules**
- `output/na_site_tsv_specs.md`  
- `output/na_access_point_tsv_specs.md`  
- `output/na_trail_tsv_specs.md`  
- `output/na_trail_segment_tsv_specs.md`  
- `output/na_trail_network_tsv_specs.md`  
- `output/na_site_network_tsv_specs.md`  
- `output/na_tsv_integrity_check.md`

### **7. Audit & Baseline Modules**
- `audit/na_audit_and_logging.md`  
- `baseline/na_county_baseline.md`

### **8. Manifest**
- `na_module_manifest.md`

------------------------------------------------------------
##  End‑to‑End Workflow (v4.0 Tiered Pipeline)

Each county is processed through a deterministic v4.0 pipeline:

1. **Load County Baseline (Tier‑0)**  
2. **Run Tiered Discovery Protocol (Tiers 1–8)**  
3. **Apply Resolution Engine**  
4. **Normalize Sites**  
5. **Normalize Access Points**  
6. **Normalize Trails**  
7. **Normalize Trail Segments**  
8. **Normalize Trail Networks**  
9. **Normalize Site Networks**  
10. **Generate TSV Output (6 files)**  
11. **Run TSV Integrity Check**  
12. **Validate Cross‑Entity Relationships**  
13. **Audit & Logging**

This workflow guarantees:

- No silent corrections  
- No silent exclusions  
- No invented data  
- Perfect delimiter integrity  
- Full reproducibility  
- Full cross‑entity consistency  

------------------------------------------------------------
##  Recommended Repository Structure (v4.0)

Matches your current directory exactly.
# NATURAL AREAS PROJECT — README.md (v4.0)
A statewide, document‑driven, tier‑ordered system for discovering, classifying,
normalizing, relating, and exporting natural areas, parks, trails, trail
segments, networks, and access infrastructure across all 88 Ohio counties.

The Natural Areas System v4.0 is fully modular, deterministic, and audit‑ready.
Every rule lives in exactly one authoritative module.  
Every module is versioned.  
Every run is reproducible.

------------------------------------------------------------
##  Project Overview

The Natural Areas Project builds a complete, statewide dataset of:

- Natural areas  
- Parks and preserves  
- Sites and Child Sites (via Child Site Rules v4.0)  
- Trail systems  
- Trail segments  
- Trail networks  
- Site networks  
- Visitor access points (trailheads, parking, boat launches, etc.)

The system emphasizes:

- **Identity‑first ontology**  
- **Tier‑ordered discovery** (Federal → State → District → County → Township → Municipal → Conservancy → Private → Baseline)  
- **Governance and ecological clarity**  
- **Public access accuracy**  
- **Deterministic, repeatable processing**  
- **Zero invented data**  
- **Full auditability**  
- **Cross‑entity relationships**  
- **Perfect TSV delimiter integrity**

------------------------------------------------------------
##  System Architecture (v4.0)

The system is composed of authoritative modules grouped into eight domains.

### **1. Schema Modules**
Define the field structure, identity rules, and parent/relationship rules for each entity type.

- `schema/na_site_schema.md`  
- `schema/na_access_point_schema.md`  
- `schema/na_trail_schema.md`  
- `schema/na_trail_segment_schema.md`  
- `schema/na_trail_network_schema.md`  
- `schema/na_site_network_schema.md`  
- `schema/na_child_site_rules.md`  
- `schema/na_discovery_architecture.md`  
- `schema/na_entity_graph_schema.md`

### **2. Vocabulary Modules**
Controlled vocabularies for all vocabulary‑governed fields.

- `vocabularies/na_site_vocabulary.md`  
- `vocabularies/na_access_point_vocabulary.md`  
- `vocabularies/na_trail_vocabulary.md`  
- `vocabularies/na_trail_segment_vocabulary.md`  
- `vocabularies/na_trail_network_vocabulary.md`  
- `vocabularies/na_site_network_vocabulary.md`

### **3. Normalization Modules**
Entity‑specific normalization contracts and engines.

- `normalization/na_site_normalization.md`  
- `normalization/na_access_point_normalization.md`  
- `normalization/na_trail_normalization.md`  
- `normalization/na_trail_segment_normalization.md`  
- `normalization/na_trail_network_normalization.md`  
- `normalization/na_site_network_normalization.md`  
- `normalization/na_normalization_engine.md`  
- `normalization/na_entity_upsert_engine.md`

### **4. Discovery System (Stem + Leaf Modules)**

#### Stem & Specifications
- `workflow/na_discovery_protocol.md`  
- `workflow/na_discovery_metadata_spec.md`  
- `workflow/na_discovery_output_spec.md`  
- `workflow/na_discovery_orchestration.md`

#### Jurisdictional Discovery Sub‑Procedures
- `workflow/na_county_discovery_subproc.md`  
- `workflow/na_municipal_discovery_subproc.md`  
- `workflow/na_township_discovery_subproc.md`  
- `workflow/na_state_discovery_subproc.md`  
- `workflow/na_fed_tribal_discovery_subproc.md`  
- `workflow/na_district_discovery_subproc.md`  
- `workflow/na_private_discovery_subproc.md`  
- `workflow/na_conservancy_discovery_subproc.md`

#### Entity‑Specific Discovery Sub‑Procedures
- `workflow/na_site_discovery_subproc.md`  
- `workflow/na_trail_discovery_subproc.md`  
- `workflow/na_trail_segment_discovery_subproc.md`  
- `workflow/na_trail_network_discovery_subproc.md`  
- `workflow/na_site_network_discovery_subproc.md`  
- `workflow/na_access_point_discovery_subproc.md`

### **5. Workflow & Logic Modules**
- `workflow/natural-areas-project.md`  
- `workflow/na_bootstrap.md`  
- `workflow/na_processing.md`  
- `workflow/na_resolution.md`  
- `workflow/na_resolution_engine.md`

### **6. Output Modules**
- `output/na_site_tsv_specs.md`  
- `output/na_access_point_tsv_specs.md`  
- `output/na_trail_tsv_specs.md`  
- `output/na_trail_segment_tsv_specs.md`  
- `output/na_trail_network_tsv_specs.md`  
- `output/na_site_network_tsv_specs.md`  
- `output/na_tsv_integrity_check.md`

### **7. Audit & Baseline Modules**
- `audit/na_audit_and_logging.md`  
- `baseline/na_county_baseline.md`

### **8. Manifest**
- `na_module_manifest.md`

------------------------------------------------------------
##  End‑to‑End Workflow (v4.0 Tiered Pipeline)

Each county is processed through a deterministic v4.0 pipeline:

1. **Load County Baseline (Tier‑0)**  
2. **Run Tiered Discovery Protocol (Tiers 1–8)**  
3. **Apply Resolution Engine**  
4. **Normalize Sites**  
5. **Normalize Access Points**  
6. **Normalize Trails**  
7. **Normalize Trail Segments**  
8. **Normalize Trail Networks**  
9. **Normalize Site Networks**  
10. **Generate TSV Output (6 files)**  
11. **Run TSV Integrity Check**  
12. **Validate Cross‑Entity Relationships**  
13. **Audit & Logging**

This workflow guarantees:

- No silent corrections  
- No silent exclusions  
- No invented data  
- Perfect delimiter integrity  
- Full reproducibility  
- Full cross‑entity consistency  

------------------------------------------------------------
##  Recommended Repository Structure (v4.0)

Matches your current directory exactly.


natural-areas-project/ ├── schema/ ├── vocabularies/ ├── normalization/ ├── workflow/ ├── output/ ├── audit/ ├── baseline/ └── na_module_manifest.md

------------------------------------------------------------
##  Running a County (Quick Start)

1. Upload all modules in the order defined in **na_bootstrap.md (v4.0)**  
2. Say:  
   **“Load these as the active Natural Areas system.”**  
3. Upload the county baseline file  
4. Say:  
   **“Process this county.”**  
5. Receive:  
   - Six normalized datasets  
   - Six TSV outputs  
   - Relationship validation  
   - Full audit log  

------------------------------------------------------------
##  Design Principles

The system is built on:

- **Determinism** — same inputs → same outputs  
- **Transparency** — every decision logged  
- **Non‑invention** — no fabricated data  
- **Strict formatting** — TSVs with perfect delimiter integrity  
- **Modularity** — each rule lives in exactly one place  
- **Auditability** — every step traceable  
- **Ontology‑driven design** — identity first, amenities second  
- **Tier‑ordered discovery** — authoritative sources always win  

------------------------------------------------------------
## 🛠 Contributing

Contributions should:

- Modify only the relevant module  
- Document all changes  
- Maintain backward compatibility when possible  
- Follow the versioning rules in the Module Manifest  

Pull requests should include:

- Summary of changes  
- Updated module version number  
- Rationale for the change  

------------------------------------------------------------
##  Status

All modules listed here are active, authoritative, and aligned with the
Natural Areas System v4.0.

------------------------------------------------------------
# END OF README.md v4.0