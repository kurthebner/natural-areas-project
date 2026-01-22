# NATURAL AREAS PROJECT
# DISCOVERY ORCHESTRATION MODULE v3.2
(Execution Engine for Tiered, Multi‑Entity Discovery)

This module defines the **runtime execution workflow** for the Discovery Protocol
Module v3.2. It coordinates all eight discovery tiers, all six entity types, all
sub‑procedures, and all metadata and output specifications.

This module does **not** define discovery rules.  
It **executes** them.

------------------------------------------------------------
# 1. PURPOSE

The Discovery Orchestration Module v3.2 provides the authoritative execution engine for:

- Running all eight discovery tiers in the correct order  
- Executing all six entity‑specific discovery tracks  
- Managing state across tiers and counties  
- Enforcing the Discovery Protocol v3.2  
- Producing Raw Candidate Records v3.2  
- Producing Discovery Metadata v3.2  
- Consolidating cross‑tier results  
- Passing outputs to normalization and resolution modules  

This module ensures that discovery is **deterministic, auditable, reproducible, and complete**.

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
- All six entity types  
- All eight discovery tiers  
- All authoritative sources  
- All discovery sub‑procedures v3.2.1  

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
3. For each tier, run all six entity discovery tracks  
4. Collect Raw Candidate Records  
5. Collect Discovery Metadata  
6. Consolidate cross‑tier results  
7. Produce final Raw Candidate Record set  
8. Pass results to normalization  
9. Log all actions in Audit & Logging Module v3.2  

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

Within each tier, the orchestration engine must execute the six entity tracks in this order:

1. Site  
2. Trail  
3. Trail Segment  
4. Trail Network  
5. Site Network  
6. Access Point  

This ensures parent entities exist before children and networks.

------------------------------------------------------------
# 7. SUB‑PROCEDURE INVOCATION

Each entity track must call its authoritative **v3.2.1** sub‑procedure:

- Site Discovery Sub‑Procedure v3.2.1  
- Trail Discovery Sub‑Procedure v3.2.1  
- Trail Segment Discovery Sub‑Procedure v3.2.1  
- Trail Network Discovery Sub‑Procedure v3.2.1  
- Site Network Discovery Sub‑Procedure v3.2.1  
- Access Point Discovery Sub‑Procedure v3.2.1  

Each sub‑procedure returns:

- Raw Candidate Records v3.2  
- Discovery Metadata v3.2  

Child Sites are surfaced via the Site Discovery Sub‑Procedure v3.2.1 and represented
as Sites with Parent Site relationships, governed by the Child Site Rules Module v3.2.1.

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
- Parent relationships (as discovered)  
- Boundary flags  

State must never be shared across counties.

------------------------------------------------------------
# 9. MULTI‑COUNTY RULE ENFORCEMENT (UNIVERSAL, v3.2.3)

The orchestration engine must enforce the authoritative multi‑county rule:

- **No segmentation** of multi‑county entities  
- **Record all counties exactly as discovered**  
- **Preserve raw county lists in metadata**  
- **Normalization converts raw lists into semicolon‑delimited, alphabetized lists**  

This rule applies universally to:

- Sites  
- Child Sites  
- Trails  
- Trail Segments  
- Trail Networks  
- Site Networks  
- Access Points  

Discovery never expands entities into multiple rows.  
Discovery only records raw county lists.

------------------------------------------------------------
# 10. CROSS‑TIER CONSOLIDATION

After all tiers complete, the orchestration engine must consolidate:

## 10.1 Sites  
Merge identical Sites across tiers, including child Sites.

## 10.2 Trails  
Merge identical Trails across tiers.

## 10.3 Trail Segments  
Merge identical segments and align with parent Trails.

## 10.4 Trail Networks  
Merge identical networks and align with member Trails.

## 10.5 Site Networks  
Merge identical networks and align with member Sites.

## 10.6 Access Points  
Merge identical Access Points and assign identity parents.

Rules:

- No normalization  
- No invention  
- All conflicts preserved in metadata  
- Primary tier = lowest tier number  

------------------------------------------------------------
# 11. METADATA ENFORCEMENT

For every entity, the orchestration engine must ensure:

- Identity metadata is complete  
- Tier metadata is complete  
- Source metadata is complete  
- Conflict metadata is preserved  
- Uncertainty metadata is preserved  
- Parent metadata is correct (Access Points only)  
- Boundary metadata is correct  
- Baseline metadata is correct  
- Notes are preserved  

Metadata must conform to:

- **Discovery Metadata Specification v3.2**

------------------------------------------------------------
# 12. OUTPUT ASSEMBLY

The orchestration engine must produce:

- One Raw Candidate Record v3.2 per entity  
- One Discovery Metadata Object v3.2 per entity  
- One consolidated output set per county  

Outputs must conform to:

- **Discovery Output Specification v3.2**  
- All Schema Modules v3.2.2  
- All Vocabulary Modules v3.2  

------------------------------------------------------------
# 13. BASELINE INTEGRATION

If a county baseline exists:

- Pre‑seed entities into state  
- Mark `seeded_from_baseline = true`  
- Preserve baseline IDs  
- Allow discovery to override baseline values  
- Preserve conflicts in metadata  

------------------------------------------------------------
# 14. DEVELOPER PREVIEW TSVs

Developer‑requested previews:

- Use raw values only  
- Follow TSV Output field order  
- Are not normalized  
- Are not authoritative  
- Are not persisted  

------------------------------------------------------------
# 15. ERROR HANDLING & FALLBACKS

The orchestration engine must:

- Log all errors  
- Never discard partial results  
- Never invent missing values  
- Never silently correct malformed values  
- Mark uncertainties in metadata  
- Continue execution unless a tier is completely inaccessible  

------------------------------------------------------------
# 16. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v3.2  
- All Discovery Sub‑Procedures v3.2.1  
- Discovery Metadata Specification v3.2  
- Discovery Output Specification v3.2  
- Access Point Association Module v3.2  
- Normalization Contracts v3.2  
- TSV Output Specifications v3.2  
- Audit & Logging Module v3.2  
- County Baseline Module v3.2  
- Resolution Module v3.2  

------------------------------------------------------------
# 17. VERSIONING

This module is **Discovery Orchestration Module v3.2**.  
Sub‑procedures may advance to v3.2.1+ without requiring a version bump.  
Future updates may produce v3.3, v3.4, etc.

------------------------------------------------------------
# END OF DISCOVERY ORCHESTRATION MODULE v3.2