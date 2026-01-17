# NATURAL AREAS PROJECT — OVERVIEW & WORKFLOW v3.1
A unified, document‑driven system for discovering, classifying, normalizing,
relating, and exporting **all seven entity types** across all 88 Ohio counties:

- Site
- Sub‑Site
- Access Point
- Trail
- Trail Segment
- Trail Network
- Site Network

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v3.1.

------------------------------------------------------------
# 1. PROJECT GOAL

Build a statewide, audit‑ready dataset of natural areas, parks, preserves,
trail systems, trail segments, networks, and access infrastructure, with a focus on:

- Ecological identity
- Governance clarity
- Public access
- Repeatable, deterministic processing
- Zero invention
- Full auditability
- Cross‑entity relationships
- Multi‑county correctness
- Identity‑first ontology

The system supports conservation planning, ecological scoring, public engagement,
land management, and long‑term stewardship.

------------------------------------------------------------
# 2. SYSTEM ARCHITECTURE (DOCUMENT‑DRIVEN)

The Natural Areas Project operates through a modular, document‑driven
architecture. Each module is authoritative for its domain and overrides
lower‑level logic.

### **Active Modules (v3.1)**

#### **Schema Modules (7)**
Define the authoritative field structure and identity rules for:
- Site (25 fields)
- Sub‑Site (14 fields)
- Access Point (11 fields)
- Trail (16 fields)
- Trail Segment (15 fields)
- Trail Network (12 fields)
- Site Network (12 fields)

#### **Vocabulary Modules (7)**
Define controlled vocabularies for all vocabulary‑governed fields.

#### **County Baseline Module v3.1**
Identity‑bearing seed layer for any entity type.

#### **Discovery Protocol Module v3.1**
Defines how Copilot discovers all seven entity types.

#### **Resolution Module v3.1**
Resolves ambiguous cases, entity‑type conflicts, internal parcels, trail
hierarchies, and network membership.

#### **Normalization Contracts (7)**
Apply schema rules, formatting rules, vocabulary rules, and Derived Label logic.

#### **TSV Output Specifications (7)**
Define the exact serialization rules for each entity type.

#### **TSV Integrity Check Module v3.1**
Validates delimiter counts, blank‑field rules, alignment, and multi‑county output.

#### **Processing Orchestration Module v3.1**
Defines the end‑to‑end pipeline and module hierarchy.

#### **Audit & Logging Module v3.1**
Records all decisions, conflicts, corrections, relationships, and integrity checks.

This document provides the **high‑level workflow** that ties these modules together.

------------------------------------------------------------
# 3. END‑TO‑END WORKFLOW (HIGH‑LEVEL OVERVIEW)

The Natural Areas system processes each county through a deterministic,
multi‑entity pipeline defined in the Processing Orchestration Module v3.1.

------------------------------------------------------------
## **Stage 1 — Load County Baseline**
- Load the county’s baseline identity list.
- Accept any entity type (identity‑bearing only).
- Mark all baseline entries as seeded.
- Surface baseline anomalies.
- Do not trust entity type; resolution determines it.

------------------------------------------------------------
## **Stage 2 — Run Discovery Protocol (All Seven Entities)**
- Perform the full authority‑ordered sweep:
  County → Municipal → Township → State → Federal → Tribal → Land Trust → Supplemental
- Extract candidate:
  - Sites
  - Sub‑Sites
  - Access Points
  - Trails
  - Trail Segments
  - Trail Networks
  - Site Networks
- Deduplicate by name, location, GPS, parcel identity, trail identity, network identity.
- Merge with baseline.

------------------------------------------------------------
## **Stage 3 — Apply Resolution Module**
- Resolve entity‑type conflicts.
- Resolve Category/Subtype conflicts.
- Resolve governance conflicts.
- Resolve trail role and segment identity.
- Resolve network membership.
- Split multi‑site and multi‑trail complexes.
- Exclude non‑qualifying entities.
- Surface unresolved ambiguities.

------------------------------------------------------------
## **Stage 4 — Normalize (All Seven Entities)**

### **4A — Normalize Sites (25 fields)**
### **4B — Normalize Sub‑Sites (14 fields)**
### **4C — Normalize Access Points (11 fields)**
### **4D — Normalize Trails (16 fields)**
### **4E — Normalize Trail Segments (15 fields)**
### **4F — Normalize Trail Networks (12 fields)**
### **4G — Normalize Site Networks (12 fields)**

Each normalization step:
- Applies schema rules
- Applies vocabulary rules
- Validates formatting
- Validates GPS + Plus Code
- Validates semicolon rules
- Computes Derived Label
- Validates integrity anchors
- Validates parent/child relationships
- Applies multi‑county expansion

------------------------------------------------------------
## **Stage 5 — Generate TSV Output**
- Serialize each entity type using its TSV Output Specification.
- Enforce:
  - No placeholders
  - No invented data
  - No formatting drift
  - No spaces between delimiters
  - No trailing spaces

**Output:**  
Seven TSVs:
- Sites.tsv  
- SubSites.tsv  
- AccessPoints.tsv  
- Trails.tsv  
- TrailSegments.tsv  
- TrailNetworks.tsv  
- SiteNetworks.tsv  

------------------------------------------------------------
## **Stage 6 — TSV Integrity Check**
- Validate delimiter count (entity‑specific).
- Validate blank‑field representation.
- Validate Derived Label placement.
- Validate integrity‑anchor placement.
- Validate multi‑county expansion.
- Surface anomalies.

------------------------------------------------------------
## **Stage 7 — Relationship Validation**
- Validate:
  - Site → Sub‑Site
  - Trail → Trail Segment
  - Trail → Trail Network
  - Site → Site Network
  - Access Point → Site / Trail
- Surface relationship anomalies.

------------------------------------------------------------
## **Stage 8 — Audit & Logging**
- Record all sources, conflicts, corrections, exclusions, relationships,
  and delimiter‑integrity results.
- Store module versions and timestamps.
- Produce a complete audit trail.

------------------------------------------------------------
# 4. FIELD‑LEVEL PROCESSING SUMMARY (HIGH‑LEVEL)

Full rules live in the Schema Modules and Normalization Contracts.

### **4.1 Sites**
- Ecology → Description  
- Amenities → Features  
- Governance never inferred  
- Parent Site validated  
- Derived Label computed  
- Multi‑county expansion applied  

### **4.2 Sub‑Sites**
- Must be identity‑bearing  
- Must belong to a parent Site  
- Derived Label computed  

### **4.3 Access Points**
- Must be entrances  
- Type must match vocabulary  
- GPS must be authoritative  
- Derived Label computed  

### **4.4 Trails**
- Named, identity‑bearing routes  
- Trail Role validated  
- Network membership optional  

### **4.5 Trail Segments**
- Identity‑bearing subdivisions  
- Never Features  
- Must belong to a Trail  

### **4.6 Trail Networks**
- Collections of Trails  
- Must be documented  

### **4.7 Site Networks**
- Collections of Sites  
- Must be documented  

------------------------------------------------------------
# 5. RELATIONSHIP TO OTHER MODULES

This document is intentionally high‑level.  
It delegates all authoritative rules to:

- Schema Modules v3.1  
- Vocabulary Modules v3.1  
- County Baseline Module v3.1  
- Discovery Protocol Module v3.1  
- Resolution Module v3.1  
- Normalization Contracts v3.1  
- TSV Output Specifications v3.1  
- TSV Integrity Check Module v3.1  
- Audit & Logging Module v3.1  
- Processing Orchestration Module v3.1  

This prevents duplication and ensures a single source of truth.

------------------------------------------------------------
# 6. AI CAPSULE (UPDATED)

A compressed summary for rapid rehydration.

### **Ontology**
Seven entity types:
Site, Sub‑Site, Access Point, Trail, Trail Segment, Trail Network, Site Network.

### **Workflow**
Baseline → Discovery → Resolution → Normalization → TSV Output → Integrity Check → Relationship Validation → Audit

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

### **Outputs**
Seven normalized TSV datasets + full audit trail.

------------------------------------------------------------
# 7. VERSIONING

This document is versioned independently from all other modules.  
All changes must be explicit and documented.

------------------------------------------------------------
# END OF OVERVIEW & WORKFLOW v3.1