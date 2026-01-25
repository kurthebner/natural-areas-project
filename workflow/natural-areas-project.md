# NATURAL AREAS PROJECT
# OVERVIEW & WORKFLOW MODULE v4.0
(Authoritative High‑Level Architecture for the Raw → Resolution → Normalization → Entity Graph Pipeline)

A unified, document‑driven system for discovering, resolving, normalizing,
relating, and exporting **all six entity types** across all 88 Ohio counties:

- **Site**
- **Trail**
- **Trail Segment**
- **Trail Network**
- **Site Network**
- **Access Point**

**Child Sites are not a standalone entity type.**  
They are represented as **Sites with a Parent Site value**, governed by the  
**Child Site Rules Module v4.0**.

This module contains no controlled vocabularies.  
All vocabularies are defined in the respective Vocabulary Modules v4.0.

------------------------------------------------------------
# 1. PROJECT GOAL

Build a statewide, audit‑ready, provenance‑rich dataset of natural areas, parks,
preserves, trail systems, trail segments, networks, and access infrastructure,
with a focus on:

- Identity‑first ontology  
- Provenance‑driven discovery  
- Governance clarity  
- Public access  
- Deterministic, reproducible processing  
- Zero invention  
- Full auditability  
- Cross‑entity relationships  
- Multi‑tier conflict resolution  
- Multi‑county integrity  
- Entity Graph persistence  

The system supports conservation planning, ecological scoring, public engagement,
land management, and long‑term stewardship.

------------------------------------------------------------
# 2. SYSTEM ARCHITECTURE (DOCUMENT‑DRIVEN)

The Natural Areas Project operates through a modular, document‑driven architecture.
Each module is authoritative for its domain and overrides lower‑level logic.

### **Active Modules (v4.0)**

#### **Schema Modules (6)**
Define the authoritative field structure and identity rules for:
- Site
- Trail
- Trail Segment
- Trail Network
- Site Network
- Access Point

#### **Vocabulary Modules (6)**
Define controlled vocabularies for all vocabulary‑governed fields.

#### **County Baseline Module v4.0**
Identity‑bearing seed layer for any entity type.

#### **Discovery Protocol Module v4.0**
Defines the unified discovery architecture, enumerative + recursive discovery,
tier rules, and raw output requirements.

#### **Discovery Metadata Specification v4.0**
Defines required metadata fields for all raw discovery records.

#### **Tier Sub‑Procedure Template v4.0**
Defines the required structure and responsibilities for all tier modules.

#### **Discovery Orchestration Module v4.0**
Executes all tiers, manages recursion, enforces provenance, and produces raw records.

#### **Resolution Engine v4.0**
Resolves entity‑type conflicts, governance conflicts, parent/child relationships,
network membership, and multi‑tier identity merging.

#### **Normalization Engine v4.0 (6 modules)**
Applies schema rules, vocabulary rules, formatting rules, and Derived Label logic.

#### **Entity Upsert Engine v4.0**
Writes normalized entities into the multi‑table SQLite Entity Graph.

#### **TSV Output Specifications (6) v4.0**
Define the exact serialization rules for each entity type.

#### **TSV Integrity Check Module v4.0**
Validates delimiter counts, blank‑field rules, alignment, and multi‑county output.

#### **Audit & Logging Module v4.0**
Records all actions, conflicts, resolutions, provenance, and integrity checks.

This document provides the **high‑level workflow** that ties these modules together.

------------------------------------------------------------
# 3. END‑TO‑END WORKFLOW (HIGH‑LEVEL OVERVIEW)

The Natural Areas system processes each county through a deterministic,
multi‑entity pipeline defined in the Processing Orchestration Module v4.0.

------------------------------------------------------------
## **Stage 1 — Load County Baseline (Tier‑0)**
- Load the county’s baseline identity list.
- Accept any identity‑bearing entity type.
- Mark all baseline entries as `seeded_from_baseline = true`.
- Preserve all raw baseline values.
- Surface baseline anomalies.
- Do not trust entity type; Resolution determines it.

------------------------------------------------------------
## **Stage 2 — Run Discovery Protocol v4.0**
- Execute the full authority‑ordered sweep:
  Federal → State → District → County → Township → Municipal → Conservancy → Private → Tier‑0 Baseline
- Perform **enumerative discovery** (listing‑page enumeration).
- Perform **recursive discovery** (URL propagation).
- Extract raw discovery records for:
  - Sites
  - Trails
  - Trail Segments
  - Trail Networks
  - Site Networks
  - Access Points
- Preserve all raw values (no normalization, no correction).
- Merge discovery results with baseline.

------------------------------------------------------------
## **Stage 3 — Apply Resolution Engine v4.0**
- Resolve entity‑type conflicts.
- Resolve Category/Subtype conflicts.
- Resolve governance conflicts.
- Resolve trail role and segment identity.
- Resolve network membership.
- Merge multi‑tier identities.
- Align parent/child relationships.
- Exclude non‑qualifying entities.
- Surface unresolved ambiguities.

------------------------------------------------------------
## **Stage 4 — Normalize (All Six Entities)**
Normalization is entity‑specific:

### **4A — Normalize Sites**  
### **4B — Normalize Trails**  
### **4C — Normalize Trail Segments**  
### **4D — Normalize Trail Networks**  
### **4E — Normalize Site Networks**  
### **4F — Normalize Access Points**

Each normalization step:
- Applies schema rules  
- Applies vocabulary rules  
- Validates formatting  
- Validates GPS / geometry  
- Validates semicolon rules  
- Computes Derived Label  
- Validates integrity anchors  
- Validates parent/child relationships  
- Applies multi‑county normalization  

**Child Sites:**  
Handled entirely within **Site normalization** via the Parent Site field  
(see Child Site Rules Module v4.0).

------------------------------------------------------------
## **Stage 5 — Entity Upsert (Entity Graph)**
- Insert or update entities in the multi‑table SQLite Entity Graph.
- Maintain entity IDs across runs.
- Maintain relationship tables.
- Maintain provenance tables.
- Maintain geometry tables.
- Maintain conflict and uncertainty tables.

------------------------------------------------------------
## **Stage 6 — Generate TSV Output**
- Serialize each entity type using its TSV Output Specification.
- Enforce:
  - No placeholders
  - No invented data
  - No formatting drift
  - No spaces between delimiters
  - No trailing spaces

**Output:**  
Six TSVs:
- Sites.tsv  
- Trails.tsv  
- TrailSegments.tsv  
- TrailNetworks.tsv  
- SiteNetworks.tsv  
- AccessPoints.tsv  

------------------------------------------------------------
## **Stage 7 — TSV Integrity Check**
- Validate delimiter count (entity‑specific).
- Validate blank‑field representation.
- Validate Derived Label placement.
- Validate integrity‑anchor placement.
- Validate multi‑county formatting.
- Surface anomalies.

------------------------------------------------------------
## **Stage 8 — Relationship Validation**
- Validate:
  - Site → Parent Site
  - Trail → Trail Segment
  - Trail → Trail Network
  - Site → Site Network
  - Access Point → Site / Trail / Segment
- Surface relationship anomalies.

------------------------------------------------------------
## **Stage 9 — Audit & Logging**
- Record all sources, conflicts, resolutions, exclusions, relationships,
  and delimiter‑integrity results.
- Store module versions and timestamps.
- Produce a complete audit trail.

------------------------------------------------------------
# 4. FIELD‑LEVEL PROCESSING SUMMARY (HIGH‑LEVEL)

Full rules live in the Schema Modules and Normalization Engine.

### **4.1 Sites**
- Ecology → Description  
- Amenities → Features  
- Governance never inferred  
- Parent Site validated  
- Derived Label computed  
- Multi‑county normalization applied  

### **4.2 Trails**
- Named, identity‑bearing routes  
- Use/Surface/Origin validated  
- Network membership optional  

### **4.3 Trail Segments**
- Identity‑bearing subdivisions  
- Never Features  
- Must belong to a Trail  

### **4.4 Trail Networks**
- Collections of Trails  
- Must be documented  

### **4.5 Site Networks**
- Collections of Sites  
- Must be documented  

### **4.6 Access Points**
- Must be entrances  
- Type must match vocabulary  
- GPS must be authoritative  
- Derived Label computed  

------------------------------------------------------------
# 5. RELATIONSHIP TO OTHER MODULES

This document is intentionally high‑level.  
It delegates all authoritative rules to:

- Schema Modules v4.0  
- Vocabulary Modules v4.0  
- County Baseline Module v4.0  
- Discovery Protocol Module v4.0  
- Discovery Metadata Specification v4.0  
- Tier Sub‑Procedure Template v4.0  
- Discovery Orchestration Module v4.0  
- Resolution Engine v4.0  
- Normalization Engine v4.0  
- Entity Upsert Engine v4.0  
- TSV Output Specifications v4.0  
- TSV Integrity Check Module v4.0  
- Audit & Logging Module v4.0  
- Child Site Rules Module v4.0  
- Processing Orchestration Module v4.0  

This prevents duplication and ensures a single source of truth.

------------------------------------------------------------
# 6. AI CAPSULE (UPDATED)

A compressed summary for rapid rehydration.

### **Ontology**
Six entity types:  
Site, Trail, Trail Segment, Trail Network, Site Network, Access Point.  
Child Sites are represented as Sites with a Parent Site value.

### **Workflow**
Baseline → Discovery → Resolution → Normalization → Entity Upsert → TSV Output → Integrity Check → Relationship Validation → Audit

### **Key Rules**
- Identity first  
- No invented data  
- No silent corrections  
- No silent exclusions  
- Blank fields must be true blanks  
- All decisions must be logged  
- Resolution overrides ambiguity  
- Schema defines identity  
- Normalization enforces structure  
- Entity Graph preserves identity across runs  

### **Outputs**
Six normalized TSV datasets + Entity Graph + full audit trail.

------------------------------------------------------------
# 7. VERSIONING

This document is versioned independently from all other modules.  
All changes must be explicit and documented.

------------------------------------------------------------
# END OF OVERVIEW & WORKFLOW MODULE v4.0