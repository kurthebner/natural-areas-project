# NATURAL AREAS PROJECT — OVERVIEW & WORKFLOW v1
A unified, document‑driven system for discovering, classifying, normalizing, and exporting **Sites** and **Access Points** across all 88 Ohio counties.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v1 and Access Point Vocabulary Module v1.

---

# 1. PROJECT GOAL
Build a statewide, audit‑ready dataset of natural areas, parks, preserves, trail systems, trail segments, and access infrastructure, with a focus on:

- Ecological identity  
- Governance clarity  
- Public access  
- Repeatable, deterministic processing  
- Zero invention  
- Full auditability  

The system supports conservation planning, ecological scoring, public engagement, and long‑term stewardship.

---

# 2. SYSTEM ARCHITECTURE (DOCUMENT‑DRIVEN)
The Natural Areas Project operates through a modular, document‑driven architecture.  
Each module is authoritative for its domain and overrides lower‑level logic.

### **Active Modules**
- **Site Schema Module v1**  
  Defines the 25‑field Site structure and field‑level rules.

- **Access Point Schema Module v1**  
  Defines the 10‑field Access Point structure and field‑level rules.

- **Site Vocabulary Module v1**  
  Controlled vocabularies for all Site‑level fields.

- **Access Point Vocabulary Module v1**  
  Controlled vocabularies for Access Point Type and Status.

- **County Baseline Module v1**  
  Provides the initial seed list of Sites for each county.

- **Discovery Protocol Module v1**  
  Defines how Copilot discovers additional Sites and Access Points.

- **Resolution Module v1**  
  Resolves ambiguous cases, multi‑site complexes, and classification conflicts.

- **Site Normalization Contract v1**  
  Applies the 25‑field Site schema and enforces formatting rules.

- **Access Point Normalization Contract v1**  
  Applies the 10‑field Access Point schema and enforces formatting rules.

- **Site TSV Output Specification v1**  
  Defines the 25‑field TSV serialization rules.

- **Access Point TSV Output Specification v1**  
  Defines the 10‑field TSV serialization rules.

- **Processing Orchestration Module v1**  
  Defines the end‑to‑end pipeline and module hierarchy.

- **Audit & Logging Module v1**  
  Records all decisions, conflicts, corrections, and delimiter‑integrity checks.

This document provides the **high‑level workflow** that ties these modules together.

---

# 3. END‑TO‑END WORKFLOW (HIGH‑LEVEL OVERVIEW)
The Natural Areas system processes each county through a deterministic, multi‑entity pipeline defined in the Processing Orchestration Module v1.

---

## **Stage 1 — Load County Baseline**
- Load the county’s baseline Site list.  
- Mark all baseline entries as seeded.  
- Surface baseline anomalies.  
- Access Points are never baseline‑seeded.

---

## **Stage 2 — Run Discovery Protocol (Sites + Access Points)**
- Perform the full authority‑ordered sweep (county → municipal → township → state → federal → land trust).  
- Extract all candidate **Sites**.  
- Extract all candidate **Access Points**.  
- Deduplicate by name, location, GPS, and parcel identity.  
- Merge with baseline.

---

## **Stage 3 — Apply Resolution Module**
- Resolve Category/Subtype conflicts (Sites).  
- Resolve Access Point Type and Status conflicts (Access Points).  
- Resolve governance conflicts.  
- Split multi‑site complexes.  
- Exclude non‑qualifying entities.  
- Surface unresolved ambiguities.

---

## **Stage 4 — Normalize (Sites + Access Points)**

### **4A — Normalize Sites (25 fields)**
- Apply Site Schema Module v1.  
- Enforce controlled vocabularies.  
- Apply GPS, address, and Plus Code rules.  
- Apply trail logic.  
- Apply ownership/management rules.  
- Apply URL normalization.  
- Compute Derived Label (not stored).  
- Validate formatting rules.

### **4B — Normalize Access Points (10 fields)**
- Apply Access Point Schema Module v1.  
- Validate Access Point Type and Status.  
- Apply GPS and Plus Code rules.  
- Validate Road Name and Access Notes.  
- Compute Derived Label (not stored).  
- Validate formatting rules.

---

## **Stage 5 — Generate TSV Output**
- Serialize Sites into 25‑field TSV rows (24 delimiters).  
- Serialize Access Points into 10‑field TSV rows (9 delimiters).  
- No placeholders.  
- No invented data.  
- No formatting drift.

---

## **Stage 6 — TSV Integrity Check**
- Validate delimiter count for both entity types.  
- Validate blank‑field representation.  
- Validate Derived Label placement.  
- Validate Parent Site placement (Sites only).  
- Surface any anomalies.

---

## **Stage 7 — Audit & Logging**
- Record all sources, conflicts, corrections, exclusions, and delimiter‑integrity results.  
- Produce a complete audit trail for the county’s run.  
- Store logs with module version numbers.

---

# 4. FIELD‑LEVEL PROCESSING SUMMARY (SITES)
This section summarizes how the system handles key Site fields.  
Full rules live in the Site Schema Module v1 and Site Normalization Contract v1.

### **4.1 Description**
- Identity‑defining ecology  
- Governance history  
- Former names  
- No amenities  
- No temporary conditions  

### **4.2 Features**
- Controlled vocabulary only  
- Physical amenities  
- No ecology  
- No governance  
- No named trails  

### **4.3 Notes**
- Access details  
- Temporary conditions  
- Clarifications  
- Official listings  

### **4.4 GPS Coordinates**
- Must be authoritative  
- Verified using Name + locality  
- No reverse‑geocoded inventions  

### **4.5 Plus Code**
- Derived only from accepted coordinates  
- Blank if GPS is blank  

### **4.6 Trail Logic**
- Trail Role  
- Parent Trail Name  
- Trail Segment Type  
- Trail Access Type  
- Trail Length (Miles)  

### **4.7 Ownership / Management / Coordination**
- Ownership = legal owner  
- Management = operational steward(s)  
- Coordination = formal partners only  

### **4.8 URL Normalization**
- Full `https://` URLs only  
- Semicolon‑delimited if multiple  

---

# 5. FIELD‑LEVEL PROCESSING SUMMARY (ACCESS POINTS)
Full rules live in the Access Point Schema Module v1 and Access Point Normalization Contract v1.

### **5.1 Access Point Name**
- Human‑readable  
- Unique within parent Site  
- Constructed only when unnamed  

### **5.2 Access Point Type**
- Must match controlled vocabulary  
- Never inferred from amenities  

### **5.3 GPS + Plus Code**
- Must be authoritative  
- Plus Code derived only from accepted GPS  

### **5.4 Road Name**
- Must be authoritative  
- No invented street numbers  

### **5.5 Access Notes**
- Short, factual, non‑invented  
- No features or amenities  

### **5.6 URL**
- Optional  
- Must be authoritative  

### **5.7 Status**
- Must match controlled vocabulary  
- Never inferred from imagery  

---

# 6. RELATIONSHIP TO OTHER MODULES
This document is intentionally high‑level.  
It delegates all authoritative rules to the specialized modules:

- **Site Schema Module v1**  
- **Access Point Schema Module v1**  
- **Site Vocabulary Module v1**  
- **Access Point Vocabulary Module v1**  
- **Discovery Protocol v1**  
- **Resolution Module v1**  
- **Site Normalization Contract v1**  
- **Access Point Normalization Contract v1**  
- **Site TSV Output Specification v1**  
- **Access Point TSV Output Specification v1**  
- **Audit & Logging Module v1**  
- **Processing Orchestration Module v1**  

This prevents duplication and ensures a single source of truth for each rule.

---

# 7. AI CAPSULE (UPDATED)
A compressed summary of the system for rapid rehydration during sessions.

### **Schema**
- Sites: 25 fields  
- Access Points: 10 fields  
- Derived Label computed for both  
- Parent Site applies to Sites only  

### **Workflow**
Baseline → Discovery → Resolution → Normalization → TSV Output → Integrity Check → Audit

### **Key Rules**
- No invented data  
- No silent corrections  
- No silent exclusions  
- Blank fields must be true blanks  
- All decisions must be logged  
- All modules override in the hierarchy defined by the Orchestration Module  

### **Outputs**
- 25‑field normalized Site dataset  
- 10‑field normalized Access Point dataset  
- Two TSVs (Sites + Access Points)  
- Full audit trail  

---

# 8. VERSIONING
This document is versioned independently from all other modules.  
All changes must be explicit and documented.

---

# END OF OVERVIEW & WORKFLOW v1