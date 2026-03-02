# NATURAL AREAS PROJECT
# DISCOVERY ORCHESTRATION MODULE v5.3
Execution Engine for Tiered, Multi-Entity, Enumerative and Recursive Discovery

This module defines the runtime execution workflow for the Discovery Protocol
Module v5.x. It coordinates all eight discovery tiers, Tier‑0 baseline seeds,
all six entity types, all sub-procedures, and all metadata and raw-layer output
specifications.

This module does not define discovery rules.
It executes them within the v5.x Raw → Resolution → Normalization → Entity Graph pipeline.

------------------------------------------------------------
# CHANGES FROM v5.1 TO v5.3

- Updated module version to v5.3
- Updated all cross-module references to v5.x
- Updated organizational field cluster to four-field model:
  ownership_raw, governance_raw, partner_agencies_raw, coordination_raw
- Replaced address_raw with location_raw for Sites and Access Points
- Updated raw output assembly to include partner_agencies_raw and coordination_raw
- Updated integration points and module dependencies to v5.x
- No changes to enumerative or recursive logic
- Updated output field model to v5.3:
  gps_raw replaced by gps_lat_raw and gps_lon_raw
  maps_raw removed; map URLs included in urls_raw
  url_primary renamed to url_primary_raw
  url_all renamed to urls_raw
  notes_raw renamed to identity_notes_raw
  geometry_raw removed
- Discovery Output Specification v5.x retired; all references now v5.x
- No changes to enumerative or recursive logic
- No changes to staging file rules

------------------------------------------------------------
# 1. PURPOSE

Discovery Orchestration Module v5.3 provides the authoritative execution engine for:

- Running all eight discovery tiers (plus Tier‑0) in the correct order
- Executing all six entity-specific discovery tracks
- Performing enumerative discovery (sibling enumeration)
- Performing recursive discovery (child URL propagation)
- Managing state across tiers and counties
- Enforcing the Discovery Protocol v5.x
- Producing Raw Discovery Records v5.x
- Producing Discovery Metadata v5.x
- Passing raw outputs to the Resolution Engine v5.x
- Supporting deterministic, reproducible discovery runs

This module ensures that discovery is deterministic, auditable, reproducible, and complete.

------------------------------------------------------------
# 2. SCOPE

This module governs:

- Execution order of all discovery tiers
- Execution of all entity-specific sub-procedures
- Enumerative discovery
- Recursive discovery
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
- All discovery sub-procedures v5.x

------------------------------------------------------------
# 3. DISCOVERY STAGING FILE
Mandatory Session Artifact

Every discovery session must create and maintain a raw discovery staging file.

File creation:
- Create at bootstrap, before Tier 1 begins.
- Filename pattern: {county}_{state}_raw_discovery.yaml
- Location: working directory for the session

Skill revision notes file:
- Also create at bootstrap
- Filename pattern: {county}_{state}_skill_revision_notes.md

Append discipline:
- Append each entity to the staging file immediately upon discovery
- Do not batch-write at tier end
- Records must not rely on chat history

Chat window vs. file output:
- Raw discovery records → staging file only
- Brief entity summary (name, tier, type, flags) → chat window
- Uncertainties and conflicts → both chat (flag) and staging file (identity_notes_raw)
- Tier completion status → chat window
- Null-tier documentation → staging file

The chat window is a progress monitor, not a data store.

------------------------------------------------------------
# 4. EXECUTION PRINCIPLES

The orchestration engine must enforce:

No normalization:
- Do not normalize names
- Do not normalize access point types
- Do not normalize features
- Do not normalize difficulty or accessibility ratings
- Do not normalize ownership or governance
- Do not normalize partner agencies or coordination
- Do not normalize GPS, locations, county lists, or URLs

No invention:
- Do not invent names
- Do not invent parents
- Do not invent URLs
- Do not invent GPS coordinates
- Do not invent features
- Do not invent difficulty or accessibility ratings
- Do not invent ownership, governance, partner agencies, or coordination

No inference:
- Do not infer township (GIS-derived in normalization)
- Do not infer municipality (GIS-derived in normalization)
- Do not infer difficulty (must be explicitly stated)
- Do not infer accessibility (must be explicitly stated)
- Do not infer parent relationships (must be documented in a source)

No silent correction:
- Malformed values must be preserved exactly as discovered
- Corrections are handled downstream by Normalization

Deterministic execution:
- Given the same inputs, discovery must always produce the same raw outputs

Tier authority:
- Lower-numbered tiers take precedence in primary tier assignment
- Conflict precedence is applied downstream in Resolution

Enumerative + recursive discovery:
- Enumerate all first-level entity URLs from authoritative listing pages
- Recursively follow allowed internal links for deeper metadata

------------------------------------------------------------
# 5. HIGH-LEVEL WORKFLOW

For each county:

1. Initialize county discovery state
2. Run Tiers 1–8 in order (skipping tiers already fully discovered)
3. Run Tier‑0 Baseline (if provided)
4. For each tier, perform enumerative discovery
5. For each enumerated entity URL, run entity detection and extraction
6. Perform recursive discovery on allowed internal links
7. Collect Raw Discovery Records v5.x
8. Collect Discovery Metadata v5.x
9. Pass all raw outputs to the Resolution Engine v5.x
10. Log all actions in the Audit & Logging Module v5.x

This workflow must be executed once per county, independently.
State must never be shared across counties.

------------------------------------------------------------
# 6. TIER EXECUTION ORDER

Discovery must execute tiers in the following strict order:

1. Federal  
2. State  
3. Park District  
4. County  
5. Township  
6. Municipal  
7. Land Trust and Conservancy  
8. Private  
9. Tier‑0 Baseline (runs last)

Each tier must fully complete before the next tier begins.  
Parallelization across tiers within the same county is not permitted.

Null-tier documentation is mandatory.  
If a tier produces zero entities, the staging file must record:

- The tier number  
- The tier category  
- A null result indicator  
- The number of entities discovered (zero)  
- All sources checked  
- Notes explaining what was searched  
- The date of completion  

A missing null-tier record is a discovery defect.

------------------------------------------------------------
# 7. ENTITY TRACK EXECUTION ORDER

Within each tier, entity tracks must execute in the following order:

1. Site  
2. Trail  
3. Trail Segment  
4. Trail Network  
5. Site Network  
6. Access Point  

This ordering ensures that parent entities are surfaced before children and that Access Points can correctly reference all possible parent entities.

------------------------------------------------------------
# 8. SUB-PROCEDURE INVOCATION

Each entity track must invoke its authoritative v5.x discovery sub-procedure:

- Site Discovery Sub-Procedure v5.x  
- Trail Discovery Sub-Procedure v5.x  
- Trail Segment Discovery Sub-Procedure v5.x  
- Trail Network Discovery Sub-Procedure v5.x  
- Site Network Discovery Sub-Procedure v5.x  
- Access Point Discovery Sub-Procedure v5.x  

Each sub-procedure must return:

- Raw Discovery Records v5.x  
- Discovery Metadata v5.x  

Child Sites must follow the Child Site Rules Module v5.x.

------------------------------------------------------------
# 9. STATE MANAGEMENT

The orchestration engine must maintain three scopes of state.

County-scoped state includes:

- All discovered entities  
- All metadata  
- All source references  
- All conflicts  
- All uncertainties  

Tier-scoped state includes:

- Entities discovered within the current tier  
- Sources used  
- Errors and fallbacks  

Entity-scoped state includes:

- Raw Discovery Records  
- Metadata objects  
- Parent relationships (raw)  
- Boundary flags  
- parent_url provenance  

State must never be shared across counties.

------------------------------------------------------------
# 10. MULTI-COUNTY RULE ENFORCEMENT

The orchestration engine must enforce the multi-county rule:

- Multi-county entities must not be segmented  
- All counties must be recorded exactly as discovered  
- Raw county lists must be preserved  
- Normalization alphabetizes and formats county lists downstream  

This rule applies to all six entity types.

------------------------------------------------------------
# 11. ENUMERATIVE DISCOVERY

For each tier, enumerative discovery must:

- Identify authoritative listing or index pages  
- Extract all first-level entity URLs  
- Queue each URL for entity detection and extraction  

Partial enumeration is a discovery defect.

------------------------------------------------------------
# 12. RECURSIVE DISCOVERY

For each discovered entity page, recursive discovery must:

- Extract internal links  
- Filter links using allowed patterns  
- Enforce recursion depth limits  
- Enforce per-domain and per-entity page limits  
- Queue child URLs  
- Record parent_url for provenance  

Recursive discovery must never infer structure or invent relationships.

------------------------------------------------------------
# 13. RAW OUTPUT ASSEMBLY

The orchestration engine must produce one Raw Discovery Record v5.x per entity
occurrence and one Discovery Metadata Object v5.x per raw record. All outputs
must conform to the Discovery Output Specification v5.x, the Schema Modules
v5.x, and the Vocabulary Modules v5.x.

The following fields must remain blank at discovery time:

- township_raw  
- municipality_raw  

Discovery must not normalize, correct, dedupe, infer, invent, or silently
modify any values. All malformed or partial values must be preserved exactly as
found.

------------------------------------------------------------
# 14. BASELINE INTEGRATION (TIER‑0)

If a county baseline exists, the orchestration engine must:

- Load baseline rows as Tier‑0 raw records  
- Mark seeded_from_baseline = true  
- Preserve baseline IDs exactly  
- Allow authoritative discovery to override baseline values  
- Preserve all conflicts in metadata  
- Record all discrepancies without correction  

Tier‑0 runs after all authoritative tiers.  
Tier‑0 must never override authoritative discovery.

------------------------------------------------------------
# 15. ERROR HANDLING AND FALLBACKS

The orchestration engine must:

- Log all errors  
- Never discard partial results  
- Never invent missing values  
- Never silently correct malformed values  
- Mark uncertainties in metadata  
- Continue execution unless a tier is completely inaccessible  
- Explicitly flag inaccessible tiers  

If a tier cannot be accessed due to outage, missing pages, or structural
failure, the staging file must record:

- The nature of the failure  
- All attempted sources  
- The date and time  
- Whether retry is recommended  

------------------------------------------------------------
# 16. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v5.x  
- All Discovery Sub-Procedures v5.x  
- All Tier Sub-Procedures v5.x  
- Discovery Metadata Specification v5.x  
- Discovery Output Specification v5.x  
- Resolution Engine v5.x  
- Normalization Engine v5.x  
- Entity Upsert Engine v5.x  
- Audit and Logging Module v5.x  
- County Baseline Module v5.x  

Integration must be deterministic and must not rely on chat history.

------------------------------------------------------------
# 17. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.x  
- Discovery Output Specification v5.x  
- Discovery Metadata Specification v5.x  
- All six entity Discovery Sub-Procedures v5.x  
- All eight Tier Sub-Procedures v5.x  
- Child Site Rules Module v5.x  
- Resolution Engine v5.x  
- Audit and Logging Module v5.x  
- County Baseline Module v5.x  

------------------------------------------------------------
# END OF DISCOVERY ORCHESTRATION MODULE v5.3