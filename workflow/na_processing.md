# NATURAL AREAS PROJECT
# PROCESSING ORCHESTRATION MODULE v4.0
(Authoritative End‑to‑End Execution Pipeline for Raw → Resolution → Normalization → Entity Graph)

This module defines the authoritative, deterministic, multi‑stage processing pipeline
for transforming county‑scoped discovery outputs into fully resolved, normalized,
audit‑ready datasets for all six entity types:

- Site
- Trail
- Trail Segment
- Trail Network
- Site Network
- Access Point

Child Sites are represented as **Sites with a Parent Site value**, governed by the
**Child Site Rules Module v4.0**.

This module contains no controlled vocabularies.  
All vocabularies are defined in the respective Vocabulary Modules v4.0.

------------------------------------------------------------
# 1. PURPOSE

The Processing Orchestration Module v4.0 defines:

- The full end‑to‑end processing pipeline
- The order in which modules execute
- How raw discovery outputs flow through Resolution and Normalization
- How conflicts are surfaced, preserved, and resolved
- How final TSV outputs are produced, validated, and packaged
- How audit logs and provenance are generated
- How deterministic, reproducible processing is enforced

This module ensures:

- Deterministic execution
- Zero skipped steps
- Zero improvisation
- Strict alignment across all v4.0 modules
- Full delimiter‑integrity compliance
- Full auditability
- Full preservation of raw discovery values

------------------------------------------------------------
# 2. MODULE HIERARCHY AND AUTHORITY

The following hierarchy governs all processing:

1. **Schema Modules v4.0** (all six)
2. **County Baseline Module v4.0**
3. **Discovery Protocol Module v4.0**
4. **Discovery Orchestration Module v4.0**
5. **Resolution Engine v4.0**
6. **Normalization Engine v4.0** (all six entity types)
7. **Entity Upsert Engine v4.0**
8. **TSV Output Specifications v4.0** (all six)
9. **TSV Integrity Check Module v4.0**
10. **Audit & Logging Module v4.0**

Authority rules:

- Schema defines ontology and field definitions.
- Baseline provides identity seeds.
- Discovery expands the identity list (raw, unnormalized).
- Resolution resolves ambiguity and merges multi‑tier conflicts.
- Normalization structures each entity type.
- Entity Upsert writes entities into the multi‑table SQLite Entity Graph.
- TSV Output serializes each entity type.
- TSV Integrity Check overrides TSV Output.
- Audit & Logging records all actions.

If modules conflict:

- **Resolution overrides Discovery and Normalization.**
- **Schema overrides all modules except Resolution.**
- **Normalization overrides Baseline formatting but not Baseline identity.**
- **TSV Integrity Check overrides TSV Output.**

------------------------------------------------------------
# 3. END‑TO‑END PROCESSING PIPELINE (RAW → RESOLUTION → NORMALIZATION → ENTITY GRAPH)

The pipeline consists of **ten deterministic stages**, applied to all six entity types.

------------------------------------------------------------
# STAGE 0 — MODULE AVAILABILITY & VERSION CHECK

Before any county processing begins, the system must verify that all required
v4.0 modules are available and version‑aligned.

### 0.1 Confirm required modules are available
The system must verify that the following modules are present:

- All six Schema Modules v4.0
- All six Vocabulary Modules v4.0
- All six Normalization Modules v4.0
- Discovery Protocol Module v4.0
- Discovery Orchestration Module v4.0
- Resolution Engine v4.0
- County Baseline Module v4.0
- Entity Upsert Engine v4.0
- TSV Output Specifications v4.0
- TSV Integrity Check Module v4.0
- Audit & Logging Module v4.0
- Child Site Rules Module v4.0

### 0.2 Confirm version alignment
All modules must be version‑aligned at **v4.0**.  
Mixed versions are not permitted.

### 0.3 Confirm module integrity
Each module must:

- Contain all required sections
- Match the authoritative v4.0 structure
- Not contain outdated field counts or vocabulary references
- Not conflict with other modules

### 0.4 Request missing modules
If any required module is missing:

- Halt processing
- Surface a clear message identifying missing module(s)
- Request the missing module(s)

### 0.5 Proceed only when all modules are available

**Output:**  
Verified v4.0 module environment.

------------------------------------------------------------
# STAGE 1 — LOAD COUNTY BASELINE (TIER‑0)

### 1.1 Identify the county being processed  
### 1.2 Load the county’s baseline section  
### 1.3 Mark all baseline entries as `seeded_from_baseline = true`  
### 1.4 Accept any identity‑bearing entity type  
### 1.5 Preserve all raw baseline values  
### 1.6 Surface baseline anomalies for review  

**Output:**  
Baseline identity list (raw, unnormalized).

------------------------------------------------------------
# STAGE 2 — RUN DISCOVERY ORCHESTRATION (ALL TIERS, ALL ENTITIES)

### 2.1 Execute the full authority‑ordered tier sweep  
Federal → State → District → County → Township → Municipal → Conservancy → Private → Tier‑0 Baseline

### 2.2 Perform enumerative discovery  
Extract all first‑level entity URLs from authoritative listing pages.

### 2.3 Perform recursive discovery  
Follow allowed internal links; record parent_url; enforce recursion limits.

### 2.4 Extract raw discovery records  
For all six entity types.

### 2.5 Preserve all raw values  
No normalization, no inference, no correction.

### 2.6 Merge discovery results with baseline  
- Add new entities  
- Retain all baseline entries  
- Preserve conflicts  
- Preserve provenance  

**Output:**  
Raw Discovery Layer (all six entity types + metadata).

------------------------------------------------------------
# STAGE 3 — APPLY RESOLUTION ENGINE (MERGE, ALIGN, DISAMBIGUATE)

### 3.1 Evaluate each raw record for ambiguity
- Entity type
- Ownership
- Management
- Coordination
- Parent/child relationships
- Trail/segment identity
- Network membership
- Multi‑tier conflicts
- Multi‑county conflicts
- Naming conflicts

### 3.2 Apply Resolution Engine v4.0 rules
- Merge identical entities across tiers
- Apply tier precedence
- Preserve conflicts in metadata
- Align parent/child relationships
- Align network membership
- Align Access Point parent sets
- Exclude non‑entities

### 3.3 Surface unresolved conflicts

**Output:**  
Resolved Entity Layer (six entity types, conflict‑aware).

------------------------------------------------------------
# STAGE 4 — NORMALIZATION ENGINE (ENTITY‑SPECIFIC)

Normalization is performed separately for each entity type.

### 4A — Normalize Sites  
### 4B — Normalize Trails  
### 4C — Normalize Trail Segments  
### 4D — Normalize Trail Networks  
### 4E — Normalize Site Networks  
### 4F — Normalize Access Points  

Each normalization step includes:

- Vocabulary validation  
- Formatting validation  
- GPS / geometry validation  
- Semicolon rules  
- Derived Label computation  
- Multi‑county normalization  
- Parent/child validation (Child Site Rules Module v4.0)  
- Access level normalization (Access Point rules)  
- Governance normalization  

**Output:**  
Six fully normalized datasets.

------------------------------------------------------------
# STAGE 5 — ENTITY UPSERT ENGINE (WRITE TO ENTITY GRAPH)

### 5.1 Insert or update entities in the multi‑table SQLite Entity Graph  
### 5.2 Maintain entity IDs across runs  
### 5.3 Maintain relationship tables  
### 5.4 Maintain provenance tables  
### 5.5 Maintain geometry tables  
### 5.6 Maintain conflict and uncertainty tables  

**Output:**  
Updated Entity Graph (SQLite multi‑table structure).

------------------------------------------------------------
# STAGE 6 — GENERATE TSV OUTPUT (SERIALIZATION)

### 6.1 Assemble records in exact field order per TSV spec  
### 6.2 Use tab‑separated values  
### 6.3 Ensure:  
- No missing columns  
- No invented data  
- No placeholders  
- No formatting drift  
- No trailing spaces  
- No delimiter drift  

**Output:**  
Six TSV datasets.

------------------------------------------------------------
# STAGE 7 — TSV INTEGRITY CHECK (STRICT)

### 7.1 Validate delimiter count  
### 7.2 Validate blank‑field representation  
### 7.3 Validate field alignment  
### 7.4 Validate Derived Label placement  
### 7.5 Validate integrity‑anchor placement  
### 7.6 Validate multi‑county formatting  
### 7.7 Surface anomalies  
### 7.8 Halt finalization if integrity fails  

**Output:**  
Delimiter‑validated TSV datasets.

------------------------------------------------------------
# STAGE 8 — RELATIONSHIP VALIDATION (CROSS‑ENTITY)

### 8.1 Validate:  
- Site → Parent Site  
- Trail → Trail Segment  
- Trail → Trail Network  
- Site → Site Network  
- Access Point → Site / Trail / Segment  

### 8.2 Surface relationship anomalies  

**Output:**  
Relationship‑validated datasets.

------------------------------------------------------------
# STAGE 9 — FINAL OUTPUT BUNDLE

### 9.1 Package all six TSVs  
### 9.2 Package audit log  
### 9.3 Package metadata (module versions, timestamps)  
### 9.4 Package Entity Graph snapshot (optional)  

**Output:**  
County Output Bundle v4.0.

------------------------------------------------------------
# STAGE 10 — LOGGING & AUDIT TRAIL

### 10.1 Record:  
- All sources  
- All conflicts  
- All resolutions  
- All normalization corrections  
- All unverifiable claims  
- All delimiter‑integrity results  
- All relationship validations  
- All upsert operations  

### 10.2 Store:  
- Module versions  
- Timestamps  
- County baseline version  
- Discovery run ID  

**Output:**  
Complete audit log for the county’s processing run.

------------------------------------------------------------
# 11. PIPELINE SUMMARY (CONDENSED)

1. Load Baseline  
2. Run Discovery  
3. Apply Resolution  
4. Normalize Entities  
5. Upsert into Entity Graph  
6. Generate TSVs  
7. Validate TSVs  
8. Validate Relationships  
9. Produce Output Bundle  
10. Log Everything  

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- All six Schema Modules v4.0  
- All six Vocabulary Modules v4.0  
- All six Normalization Modules v4.0  
- Discovery Protocol Module v4.0  
- Discovery Orchestration Module v4.0  
- Resolution Engine v4.0  
- County Baseline Module v4.0  
- Entity Upsert Engine v4.0  
- TSV Output Specifications v4.0  
- TSV Integrity Check Module v4.0  
- Audit & Logging Module v4.0  
- Child Site Rules Module v4.0  

------------------------------------------------------------
# END OF PROCESSING ORCHESTRATION MODULE v4.0