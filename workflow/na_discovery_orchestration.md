# NATURAL AREAS PROJECT
# DISCOVERY ORCHESTRATION MODULE v4.0
(Execution Engine for Tiered, Multi‑Entity, Enumerative + Recursive Discovery)

This module defines the **runtime execution workflow** for the Discovery Protocol
Module v4.0. It coordinates all eight discovery tiers, Tier‑0 baseline seeds,
all six entity types, all sub‑procedures, and all metadata and raw‑layer output
specifications.

This module does **not** define discovery rules.  
It **executes** them within the v4.0 Raw → Resolution → Normalization → Entity Graph pipeline.

------------------------------------------------------------
# 1. PURPOSE

The Discovery Orchestration Module v4.0 provides the authoritative execution engine for:

- Running all eight discovery tiers (plus Tier‑0) in the correct order  
- Executing all six entity‑specific discovery tracks  
- Performing **enumerative discovery** (sibling enumeration)  
- Performing **recursive discovery** (child URL propagation)  
- Managing state across tiers and counties  
- Enforcing the Discovery Protocol v4.0  
- Producing **Raw Discovery Records v4.0**  
- Producing **Discovery Metadata v4.0**  
- Passing raw outputs to the Resolution Engine v4.0  
- Supporting deterministic, reproducible discovery runs  

This module ensures that discovery is **deterministic, auditable, reproducible, and complete**.

------------------------------------------------------------
# 2. SCOPE

This module governs:

- Execution order of all discovery tiers  
- Execution of all entity‑specific sub‑procedures  
- Enumerative discovery (listing‑page enumeration)  
- Recursive discovery (URL propagation)  
- State management across tiers  
- Metadata enforcement  
- Raw output assembly  
- Tier‑0 baseline integration  
- Error handling and fallback logic  

This module applies to:

- All counties  
- All six entity types  
- All eight discovery tiers  
- Tier‑0 baseline seeds  
- All authoritative sources  
- All discovery sub‑procedures v4.0  

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
- County lists  

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
Given the same inputs, discovery must always produce the same raw outputs.

## 3.5 Tier Authority
Lower‑numbered tiers override higher‑numbered tiers in:

- Primary tier assignment  
- Conflict precedence (applied downstream in Resolution)  

## 3.6 Enumerative + Recursive Discovery
Discovery must:

- Enumerate **all first‑level entity URLs** from authoritative listing pages  
- Recursively follow allowed internal links for deeper metadata  

------------------------------------------------------------
# 4. HIGH‑LEVEL WORKFLOW

For each county:

1. Initialize county discovery state  
2. Run Tiers 1–8 in order (skipping tiers already fully discovered)  
3. Run Tier‑0 Baseline (if provided)  
4. For each tier, perform **enumerative discovery**  
5. For each enumerated entity URL, run entity detection + extraction  
6. Perform **recursive discovery** on allowed internal links  
7. Collect Raw Discovery Records  
8. Collect Discovery Metadata  
9. Pass all raw outputs to the Resolution Engine v4.0  
10. Log all actions in Audit & Logging Module v4.0  

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
9. **Tier‑0 Baseline (optional; runs last)**

Each tier must complete before the next begins.

Tiers may be **skipped** if previously discovered and unchanged.

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

Each entity track must call its authoritative **v4.0** sub‑procedure:

- Site Discovery Sub‑Procedure v4.0  
- Trail Discovery Sub‑Procedure v4.0  
- Trail Segment Discovery Sub‑Procedure v4.0  
- Trail Network Discovery Sub‑Procedure v4.0  
- Site Network Discovery Sub‑Procedure v4.0  
- Access Point Discovery Sub‑Procedure v4.0  

Each sub‑procedure returns:

- Raw Discovery Records v4.0  
- Discovery Metadata v4.0  

Child Sites are surfaced via the Site Discovery Sub‑Procedure v4.0 and represented
as Sites with Parent Site relationships, governed by the Child Site Rules Module v4.0.

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

- Raw Discovery Records  
- Metadata objects  
- Parent relationships (as discovered)  
- Boundary flags  
- parent_url (for propagated pages)  

State must never be shared across counties.

------------------------------------------------------------
# 9. MULTI‑COUNTY RULE ENFORCEMENT

The orchestration engine must enforce the authoritative multi‑county rule:

- **No segmentation** of multi‑county entities  
- **Record all counties exactly as discovered**  
- **Preserve raw county lists in metadata**  
- **Normalization (downstream) alphabetizes and semicolon‑delimits**  

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
# 10. ENUMERATIVE DISCOVERY (NEW IN v4.0)

For each tier, the orchestration engine must:

1. Identify authoritative listing/index pages (e.g., `/parks/`, `/trails/`, `/locations/`)  
2. Extract **all first‑level entity URLs**  
3. Queue each URL for entity detection and extraction  

Enumerative discovery ensures discovery of siblings such as:

- `/parks/englewood`  
- `/parks/foreman`  
- `/parks/argyll`  

This is required for complete tier coverage.

------------------------------------------------------------
# 11. RECURSIVE DISCOVERY (NEW IN v4.0)

For each discovered entity page, the orchestration engine must:

1. Extract internal links  
2. Filter by allowed patterns (e.g., `trails`, `maps`, `facilities`, `access`)  
3. Enforce recursion depth limits  
4. Enforce per‑domain and per‑entity page limits  
5. Queue child URLs for processing  
6. Record `parent_url` for provenance  

Recursive discovery ensures discovery of deeper metadata such as:

- `/parks/englewood/trails`  
- `/parks/englewood/maps`  

------------------------------------------------------------
# 12. RAW OUTPUT ASSEMBLY (REVISED)

The orchestration engine must produce:

- One **Raw Discovery Record v4.0** per entity occurrence  
- One **Discovery Metadata Object v4.0** per raw record  

Outputs must conform to:

- **Discovery Output Specification v4.0**  
- All Schema Modules v4.0  
- All Vocabulary Modules v4.0  

Discovery must not:

- Normalize  
- Correct  
- Dedupe  
- Infer  
- Invent  
- Silently modify  

------------------------------------------------------------
# 13. BASELINE INTEGRATION (TIER‑0)

If a county baseline exists:

- Load baseline rows as Tier‑0 raw records  
- Mark `seeded_from_baseline = true`  
- Preserve baseline IDs  
- Allow discovery to override baseline values  
- Preserve conflicts in metadata  

Tier‑0 runs **after** all authoritative tiers.

------------------------------------------------------------
# 14. ERROR HANDLING & FALLBACKS

The orchestration engine must:

- Log all errors  
- Never discard partial results  
- Never invent missing values  
- Never silently correct malformed values  
- Mark uncertainties in metadata  
- Continue execution unless a tier is completely inaccessible  

------------------------------------------------------------
# 15. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v4.0  
- All Discovery Sub‑Procedures v4.0  
- Discovery Metadata Specification v4.0  
- Discovery Output Specification v4.0  
- Normalization Engine v4.0  
- Resolution Engine v4.0  
- Entity Upsert Engine v4.0  
- Audit & Logging Module v4.0  
- County Baseline Module v4.0  

Retired modules:

- Access Point Association Module  
- Child Site Discovery Sub‑Procedure  

------------------------------------------------------------
# 16. VERSIONING

This module is **Discovery Orchestration Module v4.0**.  
Sub‑procedures may advance to v4.0+ without requiring a version bump.  
Future updates may produce v4.1, v4.2, etc.

------------------------------------------------------------
# END OF DISCOVERY ORCHESTRATION MODULE v4.0