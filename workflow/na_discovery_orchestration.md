# NATURAL AREAS PROJECT
# DISCOVERY ORCHESTRATION MODULE v3.1
(Execution Engine for Tiered, Multi‑Entity Discovery)

This module defines the **runtime execution workflow** for the Discovery Protocol
Module v3.1. It coordinates all eight discovery tiers, all seven entity types, all
sub‑procedures, and all metadata and output specifications.

This module does **not** define discovery rules.  
It **executes** them.

------------------------------------------------------------
# 1. PURPOSE

The Discovery Orchestration Module v3.1 provides the authoritative execution engine
for:

- Running all eight discovery tiers in the correct order
- Executing all seven entity‑specific discovery tracks
- Managing state across tiers and counties
- Enforcing the Discovery Protocol v3.1
- Producing Raw Candidate Records v3.1
- Producing Discovery Metadata v3.1
- Consolidating cross‑tier results
- Passing outputs to normalization and resolution modules

This module ensures that discovery is **deterministic, auditable, reproducible, and
complete**.

------------------------------------------------------------
# 2. SCOPE

This module governs:

- Execution order of all discovery tiers
- Execution of all entity‑specific sub‑procedures
- State management across tiers
- Cross‑tier consolidation
- Metadata enforcement
- Output assembly
- Baseline integration
- Error handling and fallback logic

This module applies to:

- All counties
- All seven entity types
- All eight discovery tiers
- All authoritative sources
- All discovery sub‑procedures v3.1

------------------------------------------------------------
# 3. EXECUTION PRINCIPLES (NON‑NEGOTIABLE)

The orchestration engine must enforce:

## 3.1 No Normalization
Discovery must not normalize:
- Names
- Access Point Types
- Roles
- Ownership
- Access levels
- GPS
- Addresses

## 3.2 No Invention
Discovery must not invent:
- Names
- Parents
- URLs
- GPS
- Access levels
- Ownership

## 3.3 No Silent Correction
Malformed values must be:
- Preserved
- Logged in metadata
- Resolved later by normalization

## 3.4 Deterministic Execution
Given the same inputs, discovery must always produce the same outputs.

## 3.5 Tier Authority
Lower‑numbered tiers override higher‑numbered tiers in:
- Primary tier assignment
- Conflict resolution ordering
- Consolidation precedence

------------------------------------------------------------
# 4. HIGH‑LEVEL WORKFLOW

For each county:

1. Initialize county discovery state  
2. Run Tiers 1–8 in order  
3. For each tier, run all seven entity discovery tracks  
4. Collect Raw Candidate Records  
5. Collect Discovery Metadata  
6. Consolidate cross‑tier results  
7. Produce final Raw Candidate Record set  
8. Pass results to normalization  
9. Log all actions in Audit & Logging Module v1.1  

This workflow must be executed **once per county**, independently.

------------------------------------------------------------
# 5. TIER EXECUTION ORDER

The orchestration engine must execute tiers in this exact order:

1. Federal  
2. State  
3. Park District  
4. County  
5. Township  
6. Municipal  
7. Land Trust & Conservancy  
8. Private & Organization‑Based  

Each tier must complete before the next begins.

No parallelization is permitted across tiers.

------------------------------------------------------------
# 6. ENTITY TRACK EXECUTION ORDER

Within each tier, the orchestration engine must execute the seven entity tracks in
this order:

1. Site  
2. Sub‑Site  
3. Trail  
4. Trail Segment  
5. Trail Network  
6. Site Network  
7. Access Point  

This ensures parent entities exist before children.

------------------------------------------------------------
# 7. SUB‑PROCEDURE INVOCATION

Each entity track must call its authoritative v3.1 sub‑procedure:

- Site Discovery Sub‑Procedure v3.1  
- Sub‑Site Discovery Sub‑Procedure v3.1  
- Trail Discovery Sub‑Procedure v3.1  
- Trail Segment Discovery Sub‑Procedure v3.1  
- Trail Network Discovery Sub‑Procedure v3.1  
- Site Network Discovery Sub‑Procedure v3.1  
- Access Point Discovery Sub‑Procedure v3.1  

Each sub‑procedure returns:
- Raw Candidate Records v3.1  
- Discovery Metadata v3.1  

------------------------------------------------------------
# 8. STATE MANAGEMENT

The orchestration engine must maintain:

## 8.1 County‑Scoped State
- All discovered entities
- All metadata
- All source references
- All conflicts
- All uncertainties

## 8.2 Tier‑Scoped State
- Entities discovered in the current tier
- Sources used in the current tier
- Errors and fallbacks

## 8.3 Entity‑Scoped State
- Raw Candidate Records
- Metadata objects
- Parent relationships
- Boundary flags

State must never be shared across counties.

------------------------------------------------------------
# 9. CROSS‑TIER CONSOLIDATION

After all tiers complete, the orchestration engine must consolidate:

## 9.1 Sites  
Merge identical Sites across tiers.

## 9.2 Sub‑Sites  
Merge identical Sub‑Sites within parent Sites.

## 9.3 Trails  
Merge identical Trails across tiers.

## 9.4 Trail Segments  
Merge identical segments and align with parent Trails.

## 9.5 Trail Networks  
Merge identical networks and align with member Trails.

## 9.6 Site Networks  
Merge identical networks and align with member Sites.

## 9.7 Access Points  
Merge identical APs and assign identity parents.

Rules:
- No normalization  
- No invention  
- All conflicts preserved in metadata  
- Primary tier = lowest tier number  

------------------------------------------------------------
# 10. METADATA ENFORCEMENT

For every entity, the orchestration engine must ensure:

- Identity metadata is complete  
- Tier metadata is complete  
- Source metadata is complete  
- Conflict metadata is preserved  
- Uncertainty metadata is preserved  
- Parent metadata is correct (AP only)  
- Boundary metadata is correct  
- Baseline metadata is correct  
- Notes are preserved  

Metadata must conform to:
- **Discovery Metadata Specification v3.1**

------------------------------------------------------------
# 11. OUTPUT ASSEMBLY

The orchestration engine must produce:

- One Raw Candidate Record v3.1 per entity  
- One Discovery Metadata Object v3.1 per entity  
- One consolidated output set per county  

Outputs must conform to:
- **Discovery Output Specification v3.1**  
- All Schema Modules v3.1  
- All Vocabulary Modules v3.1  

------------------------------------------------------------
# 12. BASELINE INTEGRATION

If a county baseline exists:

- Pre‑seed entities into state  
- Mark `seeded_from_baseline = true`  
- Preserve baseline IDs  
- Allow discovery to override baseline values  
- Preserve conflicts in metadata  

------------------------------------------------------------
# 13. ERROR HANDLING & FALLBACKS

The orchestration engine must:

- Log all errors  
- Never discard partial results  
- Never invent missing values  
- Never silently correct malformed values  
- Mark uncertainties in metadata  
- Continue execution unless a tier is completely inaccessible  

------------------------------------------------------------
# 14. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v3.1  
- All eight Discovery Sub‑Procedures v3.1  
- Discovery Metadata Specification v3.1  
- Discovery Output Specification v3.1  
- Access Point Association Module v3.1  
- Normalization Contracts v3.1  
- TSV Output Specifications v3.1  
- Audit & Logging Module v1.1  
- County Baseline Module v1.1  
- Resolution Module v1  

------------------------------------------------------------
# 15. VERSIONING

This module is **Discovery Orchestration Module v3.1**.  
Future updates may produce v3.2, v3.3, etc.

------------------------------------------------------------
# END OF DISCOVERY ORCHESTRATION MODULE v3.1