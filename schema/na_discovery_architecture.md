# NATURAL AREAS PROJECT — DISCOVERY ARCHITECTURE v4.0
Unified architecture describing how all Discovery modules interact across the  
six‑entity ontology within the **Raw → Resolution → Normalization → Entity Graph** pipeline.

This document is descriptive, not normative.  
Authority resides in the four Discovery modules:

1. Discovery Protocol Module v4.0  
2. Discovery Orchestration Module v4.0  
3. Discovery Metadata Specification v4.0  
4. Discovery Output Specification v4.0  

------------------------------------------------------------
# 1. PURPOSE

The Discovery Architecture v4.0 defines:

- The conceptual boundaries between Discovery modules  
- How discovery rules differ from execution logic  
- How Raw Discovery Records and Discovery Metadata are produced  
- How child Sites are represented within the v4.0 ontology  
- How Discovery integrates with Baseline, Resolution, Normalization, TSV Output, and the Entity Graph  
- How enumerative and recursive discovery operate together  
- How provenance is preserved across all tiers and sources  

This architecture ensures:

- Clean separation of concerns  
- Zero redundancy  
- Zero conflicting authority  
- Deterministic, auditable discovery  
- Full alignment with the v4.0 ontology and processing pipeline  

------------------------------------------------------------
# 2. ENTITY TYPES (ONTOLOGY v4.0)

Discovery surfaces candidates for exactly six identity‑bearing entity types:

1. **Site**  
   - Includes child Sites (internal identity‑bearing units)  
   - Parent Site relationships governed by **Child Site Rules Module v4.0**  

2. **Trail**  
3. **Trail Segment**  
4. **Trail Network**  
5. **Site Network**  
6. **Access Point**  

Sub‑Sites are not an entity type in v4.0.  
Child Sites are represented as Sites with a Parent Site value.

------------------------------------------------------------
# 3. MODULE ROLES AND AUTHORITY

## 3.1 Discovery Protocol Module v4.0 — “WHAT”
Defines:

- Discovery rules  
- Entity‑type definitions  
- Tier rules  
- Required sources  
- Entity‑specific discovery logic  
- Cross‑entity relationship rules  
- Requirements for Raw Discovery Records  
- Requirements for Discovery Metadata  
- Enumerative + recursive discovery rules  

Does **not** define execution order or state management.

## 3.2 Discovery Orchestration Module v4.0 — “HOW”
Defines:

- Per‑county execution  
- Tier order (Federal → Private → Tier‑0 Baseline)  
- Entity track order (Site → Trail → Segment → Networks → Access Points)  
- Sub‑procedure invocation  
- Enumerative discovery  
- Recursive discovery  
- State management  
- Baseline integration  
- Error handling  

Implements the Protocol; does **not** redefine rules.

## 3.3 Discovery Metadata Specification v4.0 — “METADATA STRUCTURE”
Defines:

- The Discovery Metadata Object  
- Identity metadata  
- Tier metadata  
- Source metadata  
- Conflict metadata  
- Uncertainty metadata  
- Parent/relationship metadata  
- Boundary metadata  
- Baseline metadata  
- Notes  

Metadata is stored **separately** from raw values but embedded within each Raw Discovery Record.

## 3.4 Discovery Output Specification v4.0 — “RECORD STRUCTURE”
Defines:

- The Raw Discovery Record structure  
- Field applicability by entity type  
- Raw value rules  
- Embedding of Discovery Metadata  
- Multi‑table raw output format  

Does **not** define metadata semantics.

------------------------------------------------------------
# 4. CROSS‑MODULE DATA FLOW (PER COUNTY)

1. **Orchestration initializes county state**  
2. **Orchestration executes tiers 1–8 + Tier‑0 Baseline**  
3. **Within each tier, Orchestration invokes entity‑specific sub‑procedures**  
4. **Sub‑procedures apply Protocol rules to surface candidates**  
5. **Enumerative discovery extracts first‑level entity URLs**  
6. **Recursive discovery follows allowed internal links**  
7. **Sub‑procedures produce Raw Discovery Records + Discovery Metadata**  
8. **Orchestration assembles the Raw Discovery Layer (multi‑table)**  
9. **Resolution Engine merges, aligns, and resolves identity conflicts**  
10. **Normalization Engine formats and validates resolved entities**  
11. **Entity Upsert Engine writes to the multi‑table Entity Graph**  
12. **TSV Output serializes normalized entities**  
13. **TSV Integrity Check validates delimiter and field integrity**  
14. **Audit & Logging records all actions**  

------------------------------------------------------------
# 5. CHILD SITE LOGIC (v4.0)

Internal identity‑bearing units are:

- Discovered exclusively by the Site Discovery Sub‑Procedure v4.0  
- Evaluated using the **Child Site Rules Module v4.0**  
- Represented as **Sites with Parent Site populated**  
- Normalized using the Site Normalization Contract v4.0  
- Resolved using the Resolution Module v4.0  

Discovery does not produce Sub‑Site entities.

------------------------------------------------------------
# 6. MULTI‑COUNTY LOGIC (v4.0)

Discovery must:

- Record all counties exactly as discovered  
- Preserve raw county lists in metadata  
- Never infer boundaries  
- Never segment multi‑county entities  
- Never expand entities into multiple rows  

Resolution v4.0 determines the authoritative county list.  
Normalization v4.0 alphabetizes and semicolon‑delimits the final list.

------------------------------------------------------------
# 7. ACCESS POINT LOGIC (v4.0)

Access Points:

- May be discovered in any tier  
- May have multiple parent Sites, Trails, or Trail Segments  
- Must preserve raw parent relationships  
- Must not be normalized during discovery  
- Must follow Access Point Schema Module v4.0 and Access Point Vocabulary v4.0  
- Are resolved using the Resolution Module v4.0  

------------------------------------------------------------
# 8. CONSOLIDATION LOGIC (v4.0)

Discovery v4.0 performs **no consolidation**.

Logical consolidation rules (Resolution Module v4.0):

- Merge identical entities across tiers  
- Apply tier precedence  
- Preserve conflicts  
- Preserve all source references  
- Align parent/child relationships  
- Align network membership  
- Align Access Point parent sets  

Execution rules (Orchestration + Resolution):

- State merging  
- Conflict preservation  
- Boundary handling  
- Provenance‑driven identity resolution  

------------------------------------------------------------
# 9. INTEGRATION WITH OTHER MODULES

Discovery integrates with:

- Schema Modules v4.0  
- Vocabulary Modules v4.0  
- Child Site Rules Module v4.0  
- Resolution Module v4.0  
- Normalization Contracts v4.0  
- TSV Output Specifications v4.0  
- TSV Integrity Check Module v4.0  
- Audit & Logging Module v4.0  
- County Baseline Module v4.0  
- Processing Orchestration Module v4.0  

------------------------------------------------------------
# 10. VERSIONING

This document describes the architecture of the Discovery layer in **v4.0**.  
Future ontology changes require updates to all four Discovery modules.

------------------------------------------------------------
# END OF DISCOVERY ARCHITECTURE v4.0