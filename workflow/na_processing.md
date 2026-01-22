# NATURAL AREAS PROJECT — PROCESSING ORCHESTRATION MODULE v3.2.2
A deterministic, end‑to‑end workflow defining the exact sequence Copilot follows
to transform county baseline data into fully normalized, audit‑ready datasets for
**all six entity types**:

- Site
- Access Point
- Trail
- Trail Segment
- Trail Network
- Site Network

**Sub‑Sites are no longer a standalone entity type.**
They are represented as **Sites with a Parent Site value**, governed by the
**Child Site Rules Module v3.2.2**.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v3.2.2.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The full processing pipeline for all six entity types
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

1. **Schema Modules v3.2.2** (all six)
2. **County Baseline Module v3.2.2**
3. **Discovery Protocol Module v3.2.2**
4. **Resolution Module v3.2.2**
5. **Normalization Contracts v3.2.2** (all six)
6. **TSV Output Specifications v3.2.2** (all six)
7. **TSV Integrity Check Module v3.2.2**
8. **Audit & Logging Module v3.2.2**

Authority rules:

- Schema defines ontology and field definitions.
- Baseline provides identity seeds.
- Discovery expands the identity list.
- Resolution overrides all ambiguity.
- Normalization structures each entity type.
- TSV Output serializes each entity type.
- TSV Integrity Check overrides TSV Output.
- Audit & Logging records all actions.

If modules conflict:

- **Resolution overrides Discovery and Normalization.**
- **Schema overrides all modules except Resolution.**
- **Normalization overrides Baseline formatting but not Baseline identity.**
- **TSV Integrity Check overrides TSV Output.**

------------------------------------------------------------
# 3. END‑TO‑END PROCESSING PIPELINE (SIX‑ENTITY)

The pipeline consists of **nine deterministic stages**, applied to all six entities.

------------------------------------------------------------
# STAGE 0 — MODULE AVAILABILITY CHECK

Before any county processing begins, Copilot must verify that all required
v3.2.2 modules are available for this run. Copilot does not persist documents
across sessions; therefore, module availability must be confirmed at the start
of each processing run.

### 0.1 Confirm required modules are available
Copilot must verify that the user can provide the following modules on demand:

- All six Schema Modules v3.2.2
- All six Vocabulary Modules v3.2.2
- All six Normalization Contracts v3.2.2
- Discovery Protocol Module v3.2.2
- Resolution Module v3.2.2
- County Baseline Module v3.2.2
- TSV Output Specifications v3.2.2
- TSV Integrity Check Module v3.2.2
- Audit & Logging Module v3.2.2
- Processing Orchestration Module v3.2.2
- Overview & Workflow Module v3.2.2
- Child Site Rules Module v3.2.2

### 0.2 Confirm version alignment
All modules must be version‑aligned at **v3.2.2**.
Mixed versions are not permitted.

### 0.3 Confirm module integrity
Copilot must verify that each module provided:

- Contains all required sections
- Matches the authoritative v3.2.2 structure
- Does not contain outdated field counts or vocabulary references
- Does not conflict with other modules

### 0.4 Request missing modules
If any required module is missing, Copilot must:

- Halt processing
- Surface a clear message identifying the missing module(s)
- Request the user to provide the missing module(s)

### 0.5 Proceed only when all modules are available
Processing may begin only when all required modules have been provided and
verified for this run.

**Output:**  
Verified module environment for deterministic processing.

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

### 2.1 Perform the full authority‑ordered sweep by tier
Federal → State → District → County → Township → Municipal → Conservancy → Private

### 2.2 Verify geographic correctness

### 2.3 Extract candidate entities:
- Sites
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
Expanded candidate list (six entities)

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
Fully classified candidate list (six entities)

------------------------------------------------------------
# STAGE 4 — APPLY NORMALIZATION CONTRACTS (ENTITY‑SPECIFIC)

Normalization is performed separately for each entity type.

### 4A — Normalize Sites (26 fields)  
### 4B — Normalize Access Points (12 fields)  
### 4C — Normalize Trails (18 fields)  
### 4D — Normalize Trail Segments (14 fields)  
### 4E — Normalize Trail Networks (12 fields)  
### 4F — Normalize Site Networks (12 fields)  

Each normalization step includes:

- Vocabulary validation
- Formatting validation
- GPS / Plus Code validation
- Semicolon rules
- Derived Label computation
- Integrity‑anchor validation
- Multi‑county expansion
- Parent/child validation (Child Site Rules Module v3.2.2)

**Output:**  
Six fully normalized datasets

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
Six TSV datasets:
- Sites.tsv  
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
- Site → Parent Site
- Trail → Trail Segment
- Trail → Trail Network
- Site → Site Network
- Access Point → Site / Trail

### 7.2 Surface relationship anomalies

**Output:**  
Relationship‑validated datasets

------------------------------------------------------------
# STAGE 8 — FINAL OUTPUT BUNDLE

### 8.1 Package all six TSVs  
### 8.2 Package audit log  
### 8.3 Package metadata (module versions, timestamps)  

**Output:**  
County Output Bundle v3.2.2

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

- All six Schema Modules v3.2.2  
- All six Vocabulary Modules v3.2.2  
- All six Normalization Contracts v3.2.2  
- Discovery Protocol Module v3.2.2  
- Resolution Module v3.2.2  
- County Baseline Module v3.2.2  
- TSV Output Specifications v3.2.2  
- TSV Integrity Check Module v3.2.2  
- Audit & Logging Module v3.2.2  
- Child Site Rules Module v3.2.2  

------------------------------------------------------------
# END OF PROCESSING ORCHESTRATION MODULE v3.2.2