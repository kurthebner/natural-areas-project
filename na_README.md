# NATURAL AREAS PROJECT — README.md (v3.1)
A statewide, document‑driven system for discovering, classifying, normalizing,
relating, and exporting natural areas, parks, trails, trail segments, networks,
and access infrastructure across all 88 Ohio counties.

The Natural Areas System v3.1 is fully modular, deterministic, and audit‑ready.
Every rule lives in exactly one authoritative module.

------------------------------------------------------------
## 📌 Project Overview

The Natural Areas Project builds a complete, statewide dataset of:

- Natural areas  
- Parks and preserves  
- Sub‑sites and internal identity‑bearing units  
- Trail systems  
- Trail segments  
- Trail networks  
- Site networks  
- Visitor access points (trailheads, parking, boat launches, etc.)

The system emphasizes:

- **Identity‑first ontology**  
- **Ecological and governance clarity**  
- **Public access accuracy**  
- **Deterministic, repeatable processing**  
- **Zero invented data**  
- **Full auditability**  
- **Cross‑entity relationships**  
- **Perfect TSV delimiter integrity**

Every decision is logged.  
Every module is versioned.  
Every run is reproducible.

------------------------------------------------------------
## 🧱 System Architecture (v3.1)

The system is composed of authoritative modules grouped into seven domains.

### **1. Schema Modules (7)**
Define the field structure and identity rules for each entity type.

- `schema/na_site_schema.md`  
- `schema/na_sub-site_schema.md`  
- `schema/na_trail_schema.md`  
- `schema/na_trail_segment_schema.md`  
- `schema/na_trail_network_schema.md`  
- `schema/na_site_network_schema.md`  
- `schema/na_access_point_schema.md`  
- `schema/na_access_point_association.md`

### **2. Vocabulary Modules (7)**
Controlled vocabularies for all vocabulary‑governed fields.

- `vocabularies/na_site_vocabulary.md`  
- `vocabularies/na_sub-site_vocabulary.md`  
- `vocabularies/na_trail_vocabulary.md`  
- `vocabularies/na_trail_segment_vocabulary.md`  
- `vocabularies/na_trail_network_vocabulary.md`  
- `vocabularies/na_site_network_vocabulary.md`  
- `vocabularies/na_access_point_vocabulary.md`

### **3. Normalization Modules (7)**
Entity‑specific normalization contracts.

- `normalization/na_site_normalization.md`  
- `normalization/na_sub-site_normalization.md`  
- `normalization/na_access_point_normalization.md`  
- `normalization/na_trail_normalization.md`  
- `normalization/na_trail_segment_normalization.md`  
- `normalization/na_trail_network_normalization.md`  
- `normalization/na_site_network_normalization.md`

### **4. Discovery System (Stem + Leaf Modules)**

**Stem & Specifications**
- `workflow/na_discovery_protocol.md`  
- `workflow/na_discovery_metadata_spec.md`  
- `workflow/na_discovery_output_spec.md`  
- `workflow/na_discovery_orchestration.md`

**Jurisdictional Discovery**
- `workflow/na_county_discovery_subproc.md`  
- `workflow/na_municipal_discovery_subproc.md`  
- `workflow/na_township_discovery_subproc.md`  
- `workflow/na_state_discovery_subproc.md`  
- `workflow/na_fed_tribal_discovery_subproc.md`  
- `workflow/na_park_district_discovery_subproc.md`  
- `workflow/na_private_discovery_subproc.md`  
- `workflow/na_conservancy_discovery_subproc.md`

**Entity‑Specific Discovery**
- `workflow/na_site_discovery_subproc.md`  
- `workflow/na_sub-site_discovery_subproc.md`  
- `workflow/na_trail_discovery_subproc.md`  
- `workflow/na_trail_segment_discovery_subproc.md`  
- `workflow/na_trail_network_discovery_subproc.md`  
- `workflow/na_site_network_discovery_subproc.md`  
- `workflow/na_access_point_discovery_subproc.md`

### **5. Workflow & Logic Modules**
- `workflow/natural-areas-project.md`  
- `workflow/na_processing.md`  
- `workflow/na_resolution.md`  
- `workflow/na_bootstrap.md`

### **6. Output Modules (7 + Integrity)**
- `output/na_site_tsv_specs.md`  
- `output/na_sub-site_tsv_specs.md`  
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
## 🔁 End‑to‑End Workflow (Seven‑Entity Pipeline)

Each county is processed through a deterministic v3.1 pipeline:

1. **Load County Baseline**  
2. **Run Discovery Protocol** (all seven entities)  
3. **Apply Resolution Module**  
4. **Normalize Sites**  
5. **Normalize Sub‑Sites**  
6. **Normalize Access Points**  
7. **Normalize Trails**  
8. **Normalize Trail Segments**  
9. **Normalize Trail Networks**  
10. **Normalize Site Networks**  
11. **Generate TSV Output (7 files)**  
12. **Run TSV Integrity Check**  
13. **Validate Cross‑Entity Relationships**  
14. **Audit & Logging**  

This workflow guarantees:

- No silent corrections  
- No silent exclusions  
- No invented data  
- Perfect delimiter integrity  
- Full reproducibility  
- Full cross‑entity consistency  

------------------------------------------------------------
## 📂 Recommended Repository Structure (v3.1)
natural-areas-project/ │ ├── schema/ ├── vocabularies/ ├── normalization/ ├── workflow/ ├── output/ ├── audit/ ├── baseline/ └── na_module_manifest.md

Matches your current directory exactly.

------------------------------------------------------------
## 🧪 Running a County (Quick Start)

1. Upload all modules in the order defined in the **Session Bootstrap Module v3.1**  
2. Say:  
   **“Load these as the active Natural Areas system.”**  
3. Upload the county baseline file  
4. Say:  
   **“Process this county.”**  
5. Receive:  
   - Seven normalized datasets  
   - Seven TSV outputs  
   - Relationship validation  
   - Full audit log  

------------------------------------------------------------
## 🧭 Design Principles

The system is built on:

- **Determinism** — same inputs → same outputs  
- **Transparency** — every decision logged  
- **Non‑invention** — no fabricated data  
- **Strict formatting** — TSVs with perfect delimiter integrity  
- **Modularity** — each rule lives in exactly one place  
- **Auditability** — every step traceable  
- **Ontology‑driven design** — identity first, amenities second  

------------------------------------------------------------
## 🛠️ Contributing

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
## 🌟 Status

All modules listed here are active, authoritative, and aligned with the
Natural Areas System v3.1.

------------------------------------------------------------
# END OF README.md v3.1