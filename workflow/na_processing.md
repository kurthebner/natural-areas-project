# NATURAL AREAS PROJECT — PROCESSING ORCHESTRATION MODULE v1
A deterministic, end‑to‑end workflow defining the exact sequence Copilot follows to transform county baseline data into fully normalized, audit‑ready **Site** and **Access Point** datasets.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v1 and Access Point Vocabulary Module v1.

---

# 1. PURPOSE
This module defines:

- The full processing pipeline for **both entity types**  
- The order in which modules are applied  
- How data flows from one stage to the next  
- How conflicts are surfaced and resolved  
- How final TSV outputs are produced and validated  

This module ensures:

- Deterministic execution  
- Zero skipped steps  
- Zero improvisation  
- Full alignment across all modules  
- Full delimiter‑integrity compliance  

---

# 2. MODULE HIERARCHY AND AUTHORITY
The following hierarchy governs all processing:

1. **Site Schema Module v1**  
2. **Access Point Schema Module v1**  
3. **County Baseline Module**  
4. **Discovery Protocol Module v1**  
5. **Resolution Module v1**  
6. **Site Normalization Contract v1**  
7. **Access Point Normalization Contract v1**  
8. **Site TSV Output Specification v1**  
9. **Access Point TSV Output Specification v1**  
10. **TSV Integrity Check Module**  
11. **Audit & Logging Module**

Authority rules:

- Schema Modules define the ontology and field definitions.  
- Baseline provides the initial seed list.  
- Discovery expands the list (Sites + Access Points).  
- Resolution resolves ambiguity for both entities.  
- Normalization structures each entity type.  
- TSV Output serializes each entity type.  
- TSV Integrity Check validates delimiter correctness.  
- Audit & Logging records all actions.

If modules conflict:

- **Resolution overrides Discovery and Normalization.**  
- **Schema overrides all modules except Resolution.**  
- **Normalization overrides Baseline formatting but not Baseline identity.**  
- **TSV Integrity Check overrides TSV Output if delimiter‑integrity fails.**

---

# 3. END‑TO‑END PROCESSING PIPELINE
The pipeline consists of **eight deterministic stages**, applied to **both Sites and Access Points**.

---

# STAGE 1 — LOAD COUNTY BASELINE

### 1.1 Identify the county being processed  
### 1.2 Load the county’s baseline section  
### 1.3 Mark all baseline entries as “seeded”  
### 1.4 Validate baseline formatting against both Schema Modules  
### 1.5 Surface any baseline anomalies for review  

**Output:**  
Baseline candidate list (Sites only; Access Points are never baseline‑seeded)

---

# STAGE 2 — RUN DISCOVERY PROTOCOL (SITES + ACCESS POINTS)

### 2.1 Perform the full authority‑ordered sweep  
County → Municipal → Township → State → Federal → Land Trust → Supplemental Sources

### 2.2 Verify geographic correctness  
Prevent cross‑state contamination.

### 2.3 Extract all candidate **Sites**  
- Named sites  
- Mapped sites  
- Natural areas within parks  
- Linear parks and greenways  
- Water access sites  
- Cemeteries with natural areas  
- Stormwater greens with ecological identity  
- Unnamed natural areas visible in GIS  

### 2.4 Extract all candidate **Access Points**  
- Trailheads  
- Parking areas  
- Boat ramps  
- Watercraft access points  
- Fishing access  
- River access  
- Roadside pull‑offs  
- Pedestrian/vehicle entrances  
- Bicycle/snowmobile/XC ski/equestrian access  
- Administrative access (if documented)

### 2.5 Deduplicate (non‑destructive)  
- Name  
- Location  
- GPS  
- Parcel identity  

### 2.6 Merge discovery results with baseline  
- Add new Sites  
- Add all Access Points  
- Retain all baseline entries  
- Surface redundancies for review  

**Output:**  
Expanded candidate list (Sites + Access Points)

---

# STAGE 3 — APPLY RESOLUTION MODULE (SITES + ACCESS POINTS)

### 3.1 Check each candidate for ambiguity  
- Category  
- Subtype  
- Governance  
- Trail role  
- Ecological identity  
- Multi‑site complex relationships  
- Access Point vs. Feature vs. Site  

### 3.2 Apply Resolution Module rules  
- Assign correct Category/Subtype (Sites)  
- Determine correct Trail Role (Sites)  
- Determine correct Access Point Type (Access Points)  
- Resolve internal vs. standalone features  
- Split multi‑site complexes when required  
- Exclude entities that must be excluded  

### 3.3 Surface unresolved conflicts for user review  

**Output:**  
Fully classified candidate list (Sites + Access Points)

---

# STAGE 4 — APPLY NORMALIZATION CONTRACTS

Normalization is **entity‑specific**.

---

## 4A — Normalize Sites (25 fields)

### 4A.1 Apply Site Normalization Contract v1  
### 4A.2 Validate all vocabulary‑controlled fields  
### 4A.3 Validate formatting rules  
### 4A.4 Validate GPS and Plus Code  
### 4A.5 Validate semicolon rules  
### 4A.6 Compute Derived Label (not stored)  
### 4A.7 Surface normalization failures  

**Output:**  
Fully normalized Site dataset

---

## 4B — Normalize Access Points (10 fields)

### 4B.1 Apply Access Point Normalization Contract v1  
### 4B.2 Validate Access Point Type and Status  
### 4B.3 Validate GPS and Plus Code  
### 4B.4 Validate Road Name and Access Notes  
### 4B.5 Compute Derived Label (not stored)  
### 4B.6 Surface normalization failures  

**Output:**  
Fully normalized Access Point dataset

---

# STAGE 5 — GENERATE TSV OUTPUT (SITES + ACCESS POINTS)

### 5.1 Assemble Site records in exact 25‑field order  
### 5.2 Assemble Access Point records in exact 10‑field order  
### 5.3 Use tab‑separated values  
### 5.4 Ensure:  
- No missing columns  
- No invented data  
- No placeholders  
- No formatting drift  
- No spaces between delimiters  
- No trailing spaces  

**Output:**  
Two TSV datasets:  
- **Sites.tsv**  
- **AccessPoints.tsv**

---

# STAGE 6 — TSV INTEGRITY CHECK (SITES + ACCESS POINTS)

### 6.1 Validate delimiter count  
- Sites: exactly **24 tabs**  
- Access Points: exactly **9 tabs**

### 6.2 Validate blank‑field representation  
- `\t\t` only  
- No spaces inside blanks  

### 6.3 Validate field alignment  
- Sites: Derived Label = field 24; Parent Site = field 25  
- Access Points: Derived Label = field 10  

### 6.4 Surface delimiter anomalies  
### 6.5 Halt finalization if integrity fails  

**Output:**  
Delimiter‑validated TSV datasets

---

# STAGE 7 — LOGGING AND AUDIT TRAIL

### 7.1 Record  
- All sources used  
- All conflicts surfaced  
- All edge‑case resolutions  
- All normalization corrections  
- All unverifiable claims  
- All delimiter‑integrity results  

### 7.2 Store  
- Version numbers of all modules used  
- Timestamp of processing  
- County name and baseline version  

**Output:**  
Complete audit log for the county’s processing run

---

# 8. PIPELINE SUMMARY (CONDENSED)
1. Load Baseline  
2. Discover Sites + Access Points  
3. Resolve ambiguities  
4. Normalize Sites  
5. Normalize Access Points  
6. Output TSVs  
7. Validate TSVs  
8. Log everything  

---

# 9. MODULE DEPENDENCIES
This module depends on:

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
- **TSV Integrity Check Module**  
- **Audit & Logging Module**

---

# END OF PROCESSING ORCHESTRATION MODULE v1