# NATURAL AREAS PROJECT — PROCESSING ORCHESTRATION MODULE v3.1
A deterministic, end‑to‑end workflow defining the exact sequence Copilot follows
to transform county baseline data into fully normalized, audit‑ready datasets for
**all seven entity types**:

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
# 1. PURPOSE

This module defines:

- The full processing pipeline for all seven entity types
- The order in which modules are applied
- How data flows from one stage to the next
- How entity type is determined
- How conflicts are surfaced and resolved
- How final TSV outputs are produced and validated
- How audit logs are generated

This module ensures:

- Deterministic execution
- Zero skipped steps
- Zero improvisation
- Full alignment across all modules
- Full delimiter‑integrity compliance
- Full auditability

------------------------------------------------------------
# 2. MODULE HIERARCHY AND AUTHORITY

The following hierarchy governs all processing:

1. **Schema Modules v3.1** (all seven)
2. **County Baseline Module v3.1**
3. **Discovery Protocol Module v3.1**
4. **Resolution Module v3.1**
5. **Normalization Contracts v3.1** (all seven)
6. **TSV Output Specifications v3.1** (all seven)
7. **TSV Integrity Check Module v3.1**
8. **Audit & Logging Module v3.1**

Authority rules:

- Schema defines ontology and field definitions.
- Baseline provides identity seeds.
- Discovery expands the identity list.
- Resolution overrides all ambiguity.
- Normalization structures each entity type.
- TSV Output serializes each entity type.
- TSV Integrity Check overrides TSV Output if delimiter‑integrity fails.
- Audit & Logging records all actions.

If modules conflict:

- **Resolution overrides Discovery and Normalization.**
- **Schema overrides all modules except Resolution.**
- **Normalization overrides Baseline formatting but not Baseline identity.**
- **TSV Integrity Check overrides TSV Output.**

------------------------------------------------------------
# 3. END‑TO‑END PROCESSING PIPELINE (SEVEN‑ENTITY)

The pipeline consists of **nine deterministic stages**, applied to all seven entities.

------------------------------------------------------------
# STAGE 1 — LOAD COUNTY BASELINE

### 1.1 Identify the county being processed
### 1.2 Load the county’s baseline section
### 1.3 Mark all baseline entries as “seeded”
### 1.4 Accept any entity type (identity‑bearing only)
### 1.5 Surface baseline anomalies for review

**Output:**  
Baseline identity list (entity‑agnostic)

------------------------------------------------------------
# STAGE 2 — RUN DISCOVERY PROTOCOL (ALL ENTITIES)

### 2.1 Perform the full authority‑ordered sweep  
County → Municipal → Township → State → Federal → Tribal → Land Trust → Supplemental

### 2.2 Verify geographic correctness

### 2.3 Extract candidate entities:
- Sites
- Sub‑Sites
- Access Points
- Trails
- Trail Segments
- Trail Networks
- Site Networks

### 2.4 Deduplicate (non‑destructive)
- Name
- Location
- GPS
- Parcel identity
- Trail identity
- Network identity

### 2.5 Merge discovery results with baseline
- Add new entities
- Retain all baseline entries
- Surface redundancies

**Output:**  
Expanded candidate list (all seven entities)

------------------------------------------------------------
# STAGE 3 — APPLY RESOLUTION MODULE (ALL ENTITIES)

### 3.1 Check each candidate for ambiguity:
- Entity type
- Category / Subtype
- Governance
- Trail role
- Segment identity
- Network membership
- Parent/child relationships
- Multi‑site or multi‑trail complexes

### 3.2 Apply Resolution Module rules
- Assign correct entity type
- Assign correct Category/Subtype
- Assign Trail Role / Segment Type
- Assign Network membership
- Split identity‑bearing internal units
- Exclude non‑entities
- Resolve ambiguous governance

### 3.3 Surface unresolved conflicts

**Output:**  
Fully classified candidate list (all seven entities)

------------------------------------------------------------
# STAGE 4 — APPLY NORMALIZATION CONTRACTS (ENTITY‑SPECIFIC)

Normalization is performed separately for each entity type.

### 4A — Normalize Sites (25 fields)
### 4B — Normalize Sub‑Sites (14 fields)
### 4C — Normalize Access Points (11 fields)
### 4D — Normalize Trails (16 fields)
### 4E — Normalize Trail Segments (15 fields)
### 4F — Normalize Trail Networks (12 fields)
### 4G — Normalize Site Networks (12 fields)

Each normalization step includes:

- Vocabulary validation
- Formatting validation
- GPS / Plus Code validation
- Semicolon rules
- Derived Label computation
- Integrity‑anchor validation
- Multi‑county expansion
- Parent/child validation

**Output:**  
Seven fully normalized datasets

------------------------------------------------------------
# STAGE 5 — GENERATE TSV OUTPUT (ALL ENTITIES)

### 5.1 Assemble records in exact field order per TSV spec
### 5.2 Use tab‑separated values
### 5.3 Ensure:
- No missing columns
- No invented data
- No placeholders
- No formatting drift
- No spaces between delimiters
- No trailing spaces

**Output:**  
Seven TSV datasets:
- Sites.tsv  
- SubSites.tsv  
- AccessPoints.tsv  
- Trails.tsv  
- TrailSegments.tsv  
- TrailNetworks.tsv  
- SiteNetworks.tsv  

------------------------------------------------------------
# STAGE 6 — TSV INTEGRITY CHECK (ALL ENTITIES)

### 6.1 Validate delimiter count (entity‑specific)
### 6.2 Validate blank‑field representation
### 6.3 Validate field alignment
### 6.4 Validate Derived Label placement
### 6.5 Validate integrity‑anchor placement
### 6.6 Validate multi‑county expansion
### 6.7 Surface anomalies
### 6.8 Halt finalization if integrity fails

**Output:**  
Delimiter‑validated TSV datasets

------------------------------------------------------------
# STAGE 7 — RELATIONSHIP VALIDATION (CROSS‑ENTITY)

### 7.1 Validate:
- Parent Site relationships
- Trail → Trail Segment relationships
- Trail → Trail Network membership
- Site → Site Network membership
- Access Point → Site / Trail relationships

### 7.2 Surface relationship anomalies

**Output:**  
Relationship‑validated datasets

------------------------------------------------------------
# STAGE 8 — FINAL OUTPUT BUNDLE

### 8.1 Package all seven TSVs
### 8.2 Package audit log
### 8.3 Package metadata (module versions, timestamps)

**Output:**  
County Output Bundle v3.1

------------------------------------------------------------
# STAGE 9 — LOGGING AND AUDIT TRAIL

### 9.1 Record:
- All sources
- All conflicts
- All resolutions
- All normalization corrections
- All unverifiable claims
- All delimiter‑integrity results
- All relationship validations

### 9.2 Store:
- Module versions
- Timestamps
- County baseline version

**Output:**  
Complete audit log for the county’s processing run

------------------------------------------------------------
# 10. PIPELINE SUMMARY (CONDENSED)

1. Load Baseline  
2. Discover all entities  
3. Resolve ambiguity  
4. Normalize all entities  
5. Generate TSVs  
6. Validate TSVs  
7. Validate relationships  
8. Produce output bundle  
9. Log everything  

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- All seven Schema Modules v3.1
- All seven Vocabulary Modules v3.1
- All seven Normalization Contracts v3.1
- Discovery Protocol Module v3.1
- Resolution Module v3.1
- County Baseline Module v3.1
- TSV Output Specifications v3.1
- TSV Integrity Check Module v3.1
- Audit & Logging Module v3.1

------------------------------------------------------------
# END OF PROCESSING ORCHESTRATION MODULE v3.1