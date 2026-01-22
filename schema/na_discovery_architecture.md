# NATURAL AREAS PROJECT — DISCOVERY ARCHITECTURE v3.2.2
Unified architecture describing how all Discovery modules interact across the  
six‑entity ontology.

This document is descriptive, not normative. Authority resides in the four  
Discovery modules:

1. Discovery Protocol Module v3.2.2  
2. Discovery Orchestration Module v3.2.2  
3. Discovery Metadata Specification v3.2.2  
4. Discovery Output Specification v3.2.2  

------------------------------------------------------------
# 1. PURPOSE

The Discovery Architecture v3.2.2 defines:

- The conceptual boundaries between Discovery modules  
- How discovery rules differ from execution logic  
- How Raw Candidate Records and Discovery Metadata are produced  
- How child Sites replace Sub‑Sites in the ontology  
- How Discovery integrates with Baseline, Normalization, Resolution, and TSV output  

This architecture ensures:

- Clean separation of concerns  
- Zero redundancy  
- Zero conflicting authority  
- Deterministic, auditable discovery  
- Full alignment with the v3.2.2 ontology  

------------------------------------------------------------
# 2. ENTITY TYPES (ONTOLOGY v3.2.2)

Discovery surfaces candidates for exactly six entity types:

1. **Site**  
   - Includes child Sites (internal identity‑bearing units)  
   - Parent Site relationships governed by **Child Site Rules Module v3.2.2**  

2. **Trail**  
3. **Trail Segment**  
4. **Trail Network**  
5. **Site Network**  
6. **Access Point**  

Sub‑Sites are no longer an entity type.

------------------------------------------------------------
# 3. MODULE ROLES AND AUTHORITY

## 3.1 Discovery Protocol Module v3.2.2 — “WHAT”
Defines:

- Discovery rules  
- Entity‑type definitions  
- Tier rules  
- Required sources  
- Entity‑specific discovery logic  
- Cross‑entity relationship rules  
- Logical consolidation rules  
- Requirements for Raw Candidate Records  
- Requirements for Discovery Metadata  

Does **not** define execution order or state management.

## 3.2 Discovery Orchestration Module v3.2.2 — “HOW”
Defines:

- Per‑county execution  
- Tier order  
- Entity track order  
- Sub‑procedure invocation  
- State management  
- Cross‑tier consolidation workflow  
- Baseline integration  
- Error handling  

Implements the Protocol; does **not** redefine rules.

## 3.3 Discovery Metadata Specification v3.2.2 — “METADATA STRUCTURE”
Defines:

- The Discovery Metadata Object  
- Identity, tier, source, conflict, uncertainty, parent, boundary, baseline, notes  
- Metadata semantics  
- Completeness requirements  

Embedded inside Raw Candidate Records.

## 3.4 Discovery Output Specification v3.2.2 — “RECORD STRUCTURE”
Defines:

- The Raw Candidate Record structure  
- Field applicability by entity type  
- Raw value rules  
- Embedding of Discovery Metadata  

Does **not** define metadata semantics.

------------------------------------------------------------
# 4. CROSS‑MODULE DATA FLOW (PER COUNTY)

1. **Orchestration initializes county state**  
2. **Orchestration executes tiers 1–8**  
3. **Within each tier, Orchestration invokes entity‑specific sub‑procedures**  
4. **Sub‑procedures apply Protocol rules to surface candidates**  
5. **Sub‑procedures produce Raw Candidate Records + Discovery Metadata**  
6. **Orchestration consolidates cross‑tier results**  
7. **Orchestration outputs final Raw Candidate Records**  
8. **Normalization consumes Raw Candidate Records**  
9. **Resolution resolves conflicts**  
10. **TSV Output serializes normalized entities**  
11. **Audit & Logging records all actions**  

------------------------------------------------------------
# 5. CHILD SITE LOGIC (REPLACES SUB‑SITES)

Internal identity‑bearing units are:

- Discovered by the Site Discovery Sub‑Procedure v3.2.2  
- Evaluated using the **Child Site Rules Module v3.2.2**  
- Represented as **Sites with Parent Site populated**  
- Normalized using the Site Normalization Contract v3.2.2  

Discovery no longer produces Sub‑Site entities.

------------------------------------------------------------
# 6. MULTI‑COUNTY LOGIC

Discovery must:

- Flag multi‑county entities  
- Record all counties in Discovery Metadata  
- Preserve raw county values exactly as found  
- Never infer boundaries  
- Produce multiple Raw Candidate Records **only when required by Orchestration**  

Normalization v3.2.2 determines final multi‑county representation:

- Raw county list preserved  
- Normalized list alphabetized  
- No segmentation of multi‑county entities  
- County field must not include “County”  
- County field must not include municipalities  

------------------------------------------------------------
# 7. ACCESS POINT LOGIC

Access Points:

- May be discovered in any tier  
- May have multiple parent Sites and/or Trails  
- Must preserve raw parent relationships  
- Must not be normalized during discovery  
- Must follow Access Point Schema Module v3.2.2 and Access Point Vocabulary v5  

------------------------------------------------------------
# 8. CONSOLIDATION LOGIC (LOGICAL VS EXECUTION)

Discovery Protocol defines **logical** consolidation rules.  
Discovery Orchestration defines **execution** of consolidation.

Logical rules:

- Merge identical entities across tiers  
- Preserve conflicts  
- Preserve all source references  
- Maintain parent relationships  

Execution rules:

- Tier precedence  
- State merging  
- Conflict preservation  
- Boundary handling  

------------------------------------------------------------
# 9. INTEGRATION WITH OTHER MODULES

Discovery integrates with:

- Schema Modules v3.2.2  
- Vocabulary Modules v3.2  
- Child Site Rules Module v3.2.2  
- Normalization Contracts v3.2.2  
- Resolution Module v3.2  
- TSV Output Specifications v3.2.2  
- Audit & Logging Module v3.2  
- County Baseline Module v3.2  

------------------------------------------------------------
# 10. VERSIONING

This document describes the architecture of the Discovery layer in **v3.2.2**.  
Future ontology changes require updates to all four Discovery modules.

------------------------------------------------------------
# END OF DISCOVERY ARCHITECTURE v3.2.2