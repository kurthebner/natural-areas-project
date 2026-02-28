# NATURAL AREAS PROJECT
# DISCOVERY ORCHESTRATION MODULE v5.1
(Execution Engine for Tiered, Multi-Entity, Enumerative + Recursive Discovery)

This module defines the **runtime execution workflow** for the Discovery Protocol
Module v5.0. It coordinates all eight discovery tiers, Tier-0 baseline seeds,
all six entity types, all sub-procedures, and all metadata and raw-layer output
specifications.

This module does **not** define discovery rules.
It **executes** them within the v5.0 Raw → Resolution → Normalization → Entity Graph pipeline.

------------------------------------------------------------
# CHANGES FROM v5.0

- `role_raw` and `access_level_raw` removed from execution context — deleted from Access Point schema
- `features_raw`, `difficulty_raw`, `accessibility_raw`, `maps_raw` added to raw record assembly
- `township_raw` and `municipality_raw` explicitly prohibited during execution — must remain blank; GIS-derived only
- **Core principle reinforced**: Orchestration enforces Discovery = Collection only; no decisions permitted
- All version references updated to v5.0

**CHANGES FROM v5.0 (Clinton County session):**
- **OBS-001/002/003**: Added §3 Discovery Staging File — mandatory persistent output artifact;
  raw records must be written to file, not held in chat session
- **OBS-002**: Added §4 Chat Window vs. File Output guidance
- **OBS-009**: Added skill revision notes file as standing session artifact (see §3)
- **OBS-017**: Added null-tier record format to §5 Tier Execution Order

------------------------------------------------------------
# 1. PURPOSE

The Discovery Orchestration Module v5.0 provides the authoritative execution engine for:

- Running all eight discovery tiers (plus Tier-0) in the correct order
- Executing all six entity-specific discovery tracks
- Performing **enumerative discovery** (sibling enumeration)
- Performing **recursive discovery** (child URL propagation)
- Managing state across tiers and counties
- Enforcing the Discovery Protocol v5.0
- Producing **Raw Discovery Records v5.0**
- Producing **Discovery Metadata v5.0**
- Passing raw outputs to the Resolution Engine v5.0
- Supporting deterministic, reproducible discovery runs

This module ensures that discovery is **deterministic, auditable, reproducible, and complete**.

------------------------------------------------------------
# 2. SCOPE

This module governs:

- Execution order of all discovery tiers
- Execution of all entity-specific sub-procedures
- Enumerative discovery (listing-page enumeration)
- Recursive discovery (URL propagation)
- State management across tiers
- Metadata enforcement
- Raw output assembly
- Tier-0 baseline integration
- Error handling and fallback logic

This module applies to:

- All counties
- All six entity types
- All eight discovery tiers
- Tier-0 baseline seeds
- All authoritative sources
- All discovery sub-procedures v5.0

------------------------------------------------------------
# 3. DISCOVERY STAGING FILE (MANDATORY SESSION ARTIFACT)

Every discovery session must create and maintain a raw discovery staging file.

## 3.1 File Creation
Create at bootstrap, before Tier 1 begins:
```
Filename: {county}_{state}_raw_discovery.yaml
Location: working directory for the session
```

Also create a skill revision notes file at bootstrap:
```
Filename: {county}_{state}_skill_revision_notes.md
```

## 3.2 Append Discipline
Append each entity to the staging file **immediately upon discovery** — before
moving to the next entity or the next source. Do not batch-write at tier end.

Records that exist only in conversation history are fragile and may be lost if
the session is interrupted or the context window fills. The staging file is the
authoritative record of discovery.

## 3.3 Chat Window vs. File Output
The chat window and the staging file serve different purposes:

| Output | Destination |
|--------|-------------|
| Raw discovery records | Staging file only |
| Brief entity summary (name, tier, type, flags) | Chat window |
| Uncertainties and conflicts | Both chat (flag) and staging file (notes_raw) |
| Tier completion status | Chat window |
| Null-tier documentation | Staging file (see §5) |

Keep chat output lean to preserve context window. The chat window is a progress
monitor, not a data store.

------------------------------------------------------------
# 4. EXECUTION PRINCIPLES (NON-NEGOTIABLE)

The orchestration engine must enforce:

## 4.1 No Normalization
Discovery must not normalize:

- Names
- Access Point Types
- Features
- Difficulty or accessibility ratings
- Ownership
- GPS
- Addresses
- County lists
- URLs

## 4.2 No Invention
Discovery must not invent:

- Names
- Parents
- URLs
- GPS coordinates
- Features
- Difficulty or accessibility ratings
- Ownership

## 4.3 No Inference
Discovery must not infer:

- Township — must remain blank; populated via GIS spatial lookup in normalization
- Municipality — must remain blank; populated via GIS spatial lookup in normalization
- Difficulty — only record if explicitly stated by an authoritative source
- Accessibility — only record if explicitly stated by an authoritative source
- Parent relationships — must be documented in a source

## 4.4 No Silent Correction
Malformed values must be:

- Preserved exactly
- Logged in metadata
- Resolved downstream by Normalization

## 4.5 Deterministic Execution
Given the same inputs, discovery must always produce the same raw outputs.

## 4.6 Tier Authority
Lower-numbered tiers take precedence over higher-numbered tiers in:

- Primary tier assignment
- Conflict precedence (applied downstream in Resolution)

## 4.7 Enumerative + Recursive Discovery
Discovery must:

- Enumerate **all first-level entity URLs** from authoritative listing pages
- Recursively follow allowed internal links for deeper metadata

------------------------------------------------------------
# 5. HIGH-LEVEL WORKFLOW

For each county:

1. Initialize county discovery state
2. Run Tiers 1–8 in order (skipping tiers already fully discovered)
3. Run Tier-0 Baseline (if provided)
4. For each tier, perform **enumerative discovery**
5. For each enumerated entity URL, run entity detection + extraction
6. Perform **recursive discovery** on allowed internal links
7. Collect Raw Discovery Records
8. Collect Discovery Metadata
9. Pass all raw outputs to the Resolution Engine v5.0
10. Log all actions in Audit & Logging Module v5.0

This workflow must be executed **once per county**, independently.
State must never be shared across counties.

------------------------------------------------------------
# 6. TIER EXECUTION ORDER

The orchestration engine must execute tiers in this exact order:

1. Federal
2. State
3. Park District
4. County
5. Township
6. Municipal
7. Land Trust & Conservancy
8. Private & Organization-Based
9. **Tier-0 Baseline (optional; runs last)**

Each tier must complete before the next begins.

Tiers may be **skipped** if previously discovered and sources are unchanged.

No parallelization is permitted across tiers within the same county.

## 6.1 Null-Tier Documentation

When a tier yields zero entities, the result must still be documented in the
staging file using the null-tier record format:

```yaml
tier_result:
  tier: [number]
  category: [name, e.g., "Park District"]
  result: null
  entities_count: 0
  sources_checked:
    - [URL or source description]
    - [URL or source description]
  notes: >
    [What was searched. What was found. Why the tier is null.]
  date: [ISO date]
```

This makes tier coverage machine-auditable. A tier with no record is a discovery
defect — it means the tier was never searched, not that it was searched and empty.
Never leave a tier undocumented.

------------------------------------------------------------
# 7. ENTITY TRACK EXECUTION ORDER

Within each tier, the orchestration engine must execute the six entity tracks
in this order:

1. Site
2. Trail
3. Trail Segment
4. Trail Network
5. Site Network
6. Access Point

This ordering ensures that parent entities are surfaced before children and
networks, enabling complete parent relationship recording during discovery.

------------------------------------------------------------
# 8. SUB-PROCEDURE INVOCATION

Each entity track must call its authoritative **v5.0** sub-procedure:

- Site Discovery Sub-Procedure v5.0
- Trail Discovery Sub-Procedure v5.0
- Trail Segment Discovery Sub-Procedure v5.0
- Trail Network Discovery Sub-Procedure v5.0
- Site Network Discovery Sub-Procedure v5.0
- Access Point Discovery Sub-Procedure v5.0

Each sub-procedure returns:

- Raw Discovery Records v5.0
- Discovery Metadata v5.0

Child Sites are surfaced via the Site Discovery Sub-Procedure v5.0 and represented
as Sites with Parent Site relationships, governed by the Child Site Rules Module v5.0.

------------------------------------------------------------
# 9. STATE MANAGEMENT

The orchestration engine must maintain:

## 8.1 County-Scoped State

- All discovered entities
- All metadata
- All source references
- All conflicts
- All uncertainties

## 8.2 Tier-Scoped State

- Entities discovered in the current tier
- Sources used in the current tier
- Errors and fallbacks

## 8.3 Entity-Scoped State

- Raw Discovery Records
- Metadata objects
- Parent relationships (as discovered, raw)
- Boundary flags
- `parent_url` (for propagated pages)

State must never be shared across counties.
State must never be carried forward from a prior run without explicit reload.

------------------------------------------------------------
# 10. MULTI-COUNTY RULE ENFORCEMENT

The orchestration engine must enforce the authoritative multi-county rule:

- **No segmentation** of multi-county entities
- **Record all counties exactly as discovered**
- **Preserve raw county lists in metadata**
- **Normalization (downstream) alphabetizes and semicolon-delimits**

This rule applies universally to all six entity types:

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
# 11. ENUMERATIVE DISCOVERY

For each tier, the orchestration engine must:

1. Identify authoritative listing/index pages (e.g., `/parks/`, `/trails/`, `/locations/`)
2. Extract **all first-level entity URLs**
3. Queue each URL for entity detection and extraction

Enumerative discovery ensures complete coverage of siblings such as:

- `/parks/englewood`
- `/parks/foreman`
- `/parks/argyll`

This step is required for complete tier coverage. Partial enumeration is a
discovery defect and must be logged.

------------------------------------------------------------
# 12. RECURSIVE DISCOVERY

For each discovered entity page, the orchestration engine must:

1. Extract internal links
2. Filter by allowed patterns (e.g., `trails`, `maps`, `facilities`, `access`)
3. Enforce recursion depth limits
4. Enforce per-domain and per-entity page limits
5. Queue child URLs for processing
6. Record `parent_url` for provenance

Recursive discovery ensures coverage of deeper metadata such as:

- `/parks/englewood/trails`
- `/parks/englewood/maps`

------------------------------------------------------------
# 13. RAW OUTPUT ASSEMBLY

The orchestration engine must produce:

- One **Raw Discovery Record v5.0** per entity occurrence
- One **Discovery Metadata Object v5.0** per raw record

Outputs must conform to:

- **Discovery Output Specification v5.0**
- All Schema Modules v5.0
- All Vocabulary Modules v5.0

The following fields must be left blank during raw output assembly and must not
be populated or estimated by the orchestration engine:

- `township_raw` — GIS-derived; populated in normalization
- `municipality_raw` — GIS-derived; populated in normalization

Discovery must not:

- Normalize
- Correct
- Dedupe
- Infer
- Invent
- Silently modify

------------------------------------------------------------
# 14. BASELINE INTEGRATION (TIER-0)

If a county baseline exists:

- Load baseline rows as Tier-0 raw records
- Mark `seeded_from_baseline = true`
- Preserve baseline IDs
- Allow discovery to override baseline values
- Preserve conflicts in metadata

Tier-0 runs **after** all authoritative tiers.

------------------------------------------------------------
# 15. ERROR HANDLING & FALLBACKS

The orchestration engine must:

- Log all errors in the Audit & Logging Module v5.0
- Never discard partial results
- Never invent missing values
- Never silently correct malformed values
- Mark uncertainties in metadata
- Continue execution unless a tier is completely inaccessible
- Flag inaccessible tiers explicitly in the run log

------------------------------------------------------------
# 16. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v5.0
- All Discovery Sub-Procedures v5.0 (entity-specific)
- All Tier Sub-Procedures v5.0
- Discovery Metadata Specification v5.0
- Discovery Output Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Upsert Engine v5.0
- Audit & Logging Module v5.0
- County Baseline Module v5.0

Retired in v5.0:

- Access Point Association Module (v4.0)
- Child Site Discovery Sub-Procedure (v4.0)

------------------------------------------------------------
# 17. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.0
- Discovery Output Specification v5.0
- Discovery Metadata Specification v5.0
- All six entity Discovery Sub-Procedures v5.0
- All eight Tier Sub-Procedures v5.0
- Child Site Rules Module v5.0
- Resolution Engine v5.0
- Audit & Logging Module v5.0
- County Baseline Module v5.0

------------------------------------------------------------
# END OF DISCOVERY ORCHESTRATION MODULE v5.0
