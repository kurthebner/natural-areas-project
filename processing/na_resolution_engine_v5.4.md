# RESOLUTION ENGINE v5.4  
Authoritative Execution Framework for Entity Resolution  
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# 1. PURPOSE

The Resolution Engine v5.4 provides the authoritative, deterministic workflow for transforming **Raw Discovery Records v5.x** into **Resolved Entities v5.x**. It performs the mechanical execution of identity detection, similarity scoring, merge decisions, field‑level merging, parent resolution, and metadata propagation.  

This module does **not** define identity anchors, identity signatures, entity‑type rules, category rules, parent/child rules, or multi‑county rules. Those are defined exclusively in the **Resolution Rules Module v5.x**, which this engine consumes.

Resolution Engine v5.4 is responsible for:

- grouping raw discovery records into comparison sets  
- applying identity anchors and signatures defined in the Rules Module  
- computing similarity scores  
- forming deterministic merge clusters  
- merging raw values using field‑level strategies  
- preserving all conflicts without resolving them  
- resolving parent names to IDs while preserving lineage metadata  
- assembling complete Resolved Records v5.x for downstream normalization  

Resolution Engine v5.4 is **purely mechanical**. It does not interpret, infer, normalize, or decide between conflicting values.

------------------------------------------------------------
# 2. SCOPE

Resolution Engine v5.4 governs:

- all six entity types (Site, Trail, Trail Segment, Trail Network, Site Network, Access Point)  
- all raw discovery records produced by Discovery Output Specification v5.x  
- all metadata blocks defined in Discovery Metadata Specification v5.x  
- all parent_*_raw lists and lineage metadata  
- all merge provenance and conflict structures  
- all similarity scoring and merge decisions  

Resolution Engine v5.4 does **not**:

- normalize vocabulary  
- choose canonical values  
- apply tier authority  
- infer missing values  
- modify raw values  
- modify raw metadata  
- apply category rules  
- apply entity‑type rules  
- apply identity logic beyond what is defined in the Rules Module  

Normalization Engine v5.x performs all vocabulary decisions, canonicalization, and conflict resolution.

------------------------------------------------------------
# 3. ARCHITECTURAL ROLE

Resolution Engine v5.4 sits between:

- **Discovery v5.x** (raw values + metadata)  
- **Normalization v5.x** (canonicalization + vocabulary decisions)  

Its role is to:

1. **Preserve** all raw values exactly as discovered  
2. **Detect** identity relationships  
3. **Merge** records mechanically  
4. **Record** conflicts without resolving them  
5. **Propagate** metadata blocks without alteration  
6. **Resolve** parent names to IDs without modifying lineage metadata  
7. **Produce** deterministic Resolved Records v5.x  

The engine is intentionally **stateless**, **deterministic**, and **reversible**.

------------------------------------------------------------
# 4. DESIGN PRINCIPLES

### 4.1 Determinism  
Given identical inputs, the engine must always produce identical outputs.  
No randomness, order‑dependence, or heuristic shortcuts are permitted.

### 4.2 Purity  
Resolution Engine v5.4 must not modify, infer, or normalize raw values or metadata.  
All transformations must be mechanical and reversible.

### 4.3 Rule Externalization  
All identity anchors, signatures, entity‑type rules, category rules, and parent/child rules live in the Resolution Rules Module v5.x.  
The engine must call those rules, not re‑implement them.

### 4.4 Metadata Integrity  
All metadata blocks (identity, organizational, provenance, lineage, conflict, uncertainty, boundary, baseline) must be preserved exactly as discovered and merged without alteration.

### 4.5 No Inference  
The engine must not infer:

- missing parents  
- missing counties  
- missing URLs  
- missing organizational fields  
- missing GPS values  
- missing lineage metadata  

### 4.6 No Normalization  
The engine must not:

- normalize names  
- normalize categories  
- normalize URLs  
- normalize organizational fields  
- normalize GPS values  

Matching‑only normalization is permitted **only** inside the identity functions defined in the Rules Module.

### 4.7 No Ontological Decisions  
The engine must not decide:

- entity type  
- category  
- parent/child classification  
- network membership  
- multi‑county identity  

Those decisions are defined in the Rules Module and consumed by the engine.

------------------------------------------------------------
# 5. INPUTS AND OUTPUTS

### 5.1 Inputs  
Resolution Engine v5.4 consumes:

- Raw Discovery Records v5.x  
- All embedded metadata blocks  
- Identity anchors and signatures from the Rules Module  
- Entity‑type and category rules from the Rules Module  
- Parent/child rules from the Rules Module  
- Multi‑county rules from the Rules Module  
- Merge thresholds (configuration)  

### 5.2 Outputs  
Resolution Engine v5.4 produces:

- Resolved Records v5.x (in‑memory objects)  
- Conflict metadata blocks  
- Review sets (for similarity scores below merge threshold)  
- Merge provenance metadata  
- Parent resolution metadata  
- Lineage preservation metadata  

These outputs are consumed directly by the Normalization Engine v5.x.

------------------------------------------------------------
# 6. PIPELINE OVERVIEW

Resolution Engine v5.4 executes the following phases:

1. **Phase 1 — Grouping**  
   Partition raw discovery records into deterministic comparison sets.

2. **Phase 2 — Identity Matching**  
   Apply identity anchors and signatures from the Rules Module to compute similarity scores.

3. **Phase 3 — Merge Decisions**  
   Convert similarity scores into merge clusters and review sets.

4. **Phase 4 — Field‑Level Merging**  
   Merge raw values using deterministic strategies while preserving conflicts.

5. **Phase 5 — Parent Resolution and Metadata Assembly**  
   Resolve parent names to IDs, preserve lineage metadata, and assemble Resolved Records v5.x.

Each phase is deterministic, reversible, and rule‑driven.

------------------------------------------------------------
# 7. MODULE DEPENDENCIES

Resolution Engine v5.4 depends on:

- **Resolution Rules Module v5.x**  
  (identity anchors, identity signatures, entity‑type rules, category rules, parent/child rules, multi‑county rules)

- **Discovery Output Specification v5.x**  
  (raw field model)

- **Discovery Metadata Specification v5.x**  
  (metadata blocks)

- **Normalization Engine v5.x**  
  (downstream consumer)

- **Entity Graph Schema v5.x**  
  (ID structure and parent relationships)

Resolution Engine v5.4 must not duplicate logic from these modules.

------------------------------------------------------------
# RESOLUTION ENGINE v5.4  
Phase 1 — Grouping  
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# 8. PHASE 1: GROUPING

Phase 1 partitions Raw Discovery Records v5.x into deterministic comparison sets. Grouping is the foundation of the entire resolution pipeline: it defines which records are allowed to be compared, which similarity scores will ever be computed, and which entities can ever be merged. The grouping rules in v5.4 are intentionally simple, stable, and fully aligned with the v5.3 discovery field model.

Grouping must never infer, normalize, or reinterpret raw values. It must use the raw discovery fields exactly as provided.

------------------------------------------------------------
# 8.1 PURPOSE OF GROUPING

Grouping serves three critical functions:

- **Reduce comparison space** by preventing unnecessary cross‑entity comparisons.  
- **Enforce ontological boundaries** by ensuring that only plausible candidates are compared.  
- **Guarantee determinism** by producing stable, reproducible comparison sets for identical inputs.

Grouping is not a heuristic. It is a strict partitioning step that defines the universe of possible identity matches.

------------------------------------------------------------
# 8.2 GROUPING KEYS

Each Raw Discovery Record v5.x must be assigned to one or more groups based on:

- **entity_type**  
- **county_primary**  

This produces grouping keys of the form:
(entity_type, county_primary)


These keys reflect the two most stable, non‑inferred identity dimensions available at discovery time:

- **entity_type** is authoritative and never inferred.  
- **county_primary** is a raw discovery field representing the primary county of the entity.  

Grouping by these keys ensures that:

- Sites are only compared to Sites.  
- Trails are only compared to Trails.  
- Access Points are only compared to Access Points.  
- And so on for all six entity types.  

This prevents cross‑type comparisons and enforces the ontological boundaries defined in the Resolution Rules Module v5.x.

------------------------------------------------------------
# 8.3 MULTI‑COUNTY ENTITIES

If a record’s `counties_raw` list contains more than one county, the record must be added to **every** corresponding county group.

For example, a Trail with:
counties_raw = ["Wood", "Lucas"]


must be placed into:

- (Trail, Wood)  
- (Trail, Lucas)  

This ensures that multi‑county entities can match with records discovered in any of their legitimate counties, without splitting the entity or creating county‑specific duplicates.

### Multi‑county grouping rules:

- Multi‑county inclusion is **additive**, not substitutive.  
- A record must appear in **all** groups corresponding to its raw counties.  
- No inference or GIS‑based county expansion is permitted.  
- No normalization of county names is permitted.  
- The engine must not attempt to “correct” county lists.  

This rule preserves the identity of multi‑county entities without fragmenting them.

------------------------------------------------------------
# 8.4 GROUPING MUST USE RAW VALUES ONLY

Grouping must use:

- `entity_type`  
- `county_primary`  
- `counties_raw`  

Grouping must **not** use:

- normalized values  
- inferred values  
- GIS‑derived values  
- geometry  
- map URLs  
- organizational fields  
- identity signatures  
- parent_*_raw  
- lineage metadata  

Grouping is a raw‑value operation only.

------------------------------------------------------------
# 8.5 DETERMINISM REQUIREMENTS

Grouping must be:

- **Stable** — identical inputs produce identical groups.  
- **Order‑independent** — discovery order must not affect grouping.  
- **Pure** — grouping must not depend on runtime conditions or external state.  
- **Reversible** — grouping must not alter or discard raw values.  

The grouping phase must not:

- reorder raw values  
- modify metadata  
- infer missing counties  
- collapse multi‑county entities  
- apply any identity logic  

Grouping is a pure partitioning step.

------------------------------------------------------------
# 8.6 OUTPUT OF PHASE 1

The output of Phase 1 is a deterministic mapping:
(group_key) → [list of raw discovery records]


Each group is then passed to Phase 2 (Identity Matching), where identity anchors and signatures from the Resolution Rules Module v5.x are applied.

No similarity scoring occurs in Phase 1.  
No merging occurs in Phase 1.  
No conflicts are detected in Phase 1.  

Phase 1 defines the comparison universe.  
Phase 2 performs the comparisons.

------------------------------------------------------------
# RESOLUTION ENGINE v5.4  
Phase 2 — Identity Matching  
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# 9. PHASE 2: IDENTITY MATCHING

Phase 2 determines whether two or more Raw Discovery Records v5.x represent the **same real‑world entity**. In v5.4, Identity Matching is a *pure execution layer*: it does not define identity rules, anchors, or signatures. All identity logic is defined in the **Resolution Rules Module v5.x**, and the engine simply applies those rules deterministically.

Identity Matching is the first phase where records are compared. It is also the phase that produces the similarity scores used in Phase 3 to form merge clusters and review sets.

------------------------------------------------------------
# 9.1 PURPOSE OF IDENTITY MATCHING

Identity Matching performs three essential functions:

- **Apply identity anchors** to determine whether two records are even eligible for comparison.  
- **Compute similarity scores** using identity signatures defined in the Rules Module.  
- **Produce a similarity matrix** for each grouping from Phase 1.  

Identity Matching does not:

- infer missing values  
- normalize values for output  
- modify raw values  
- apply entity‑type or category decisions  
- resolve conflicts  
- merge fields  

Identity Matching is strictly a comparison phase.

------------------------------------------------------------
# 9.2 RELATIONSHIP TO THE RESOLUTION RULES MODULE v5.x

Resolution Engine v5.4 does not contain any identity logic. Instead, it must call the following rule sets from the Resolution Rules Module v5.x:

- **Identity Anchors** (strict prerequisites)  
- **Identity Signatures** (weighted similarity scoring)  
- **Entity‑Type Definitions** (to ensure correct rule selection)  
- **Parent/Child Rules** (for Trail Segments and Access Points)  
- **Multi‑County Rules** (for anchor evaluation)  

The engine must not reinterpret, modify, or override these rules.

------------------------------------------------------------
# 9.3 IDENTITY ANCHORS (STRICT PREREQUISITES)

Identity anchors determine whether two records may be compared at all. Anchors must:

- use raw discovery fields only  
- be applied exactly as defined in the Rules Module  
- be evaluated before any similarity scoring  
- be deterministic and order‑independent  

If anchors fail, similarity scoring must not be computed.

### Anchor behavior in v5.4:

- Anchors are **entity‑type specific**.  
- Anchors must be evaluated using the raw values from the discovery record.  
- Matching‑only normalization (case folding, punctuation stripping) is permitted *only* inside the anchor functions defined in the Rules Module.  
- The engine must not apply any additional normalization.  
- Anchor failure is final; no fallback or inference is permitted.  

Examples of anchor requirements (defined in the Rules Module):

- Sites: fuzzy‑normalized name + county overlap  
- Trails: fuzzy‑normalized name + county overlap  
- Trail Segments: parent trail must match; segment name if present  
- Access Points: identity parent + GPS proximity bucket  
- Networks: fuzzy‑normalized network name + network type  

The engine simply calls these rules.

------------------------------------------------------------
# 9.4 IDENTITY SIGNATURES (FUZZY SIMILARITY)

If anchors pass, the engine must compute a similarity score using the identity signature defined for the entity type in the Rules Module.

Identity signatures:

- produce a score from **0 to 100**  
- use weighted components (e.g., name similarity, organizational similarity, GPS proximity)  
- use raw values only  
- may apply matching‑only normalization internally  
- must not modify or normalize raw values for output  

The engine must:

- call the signature function for the entity type  
- record the resulting similarity score  
- store the score in the similarity matrix for the group  

The engine must not:

- adjust weights  
- reinterpret scoring rules  
- add or remove scoring components  
- apply entity‑type logic not defined in the Rules Module  

------------------------------------------------------------
# 9.5 UPDATED FIELD MODEL FOR MATCHING (v5.x COMPLIANCE)

Identity Matching must use the updated v5.x discovery fields:

- `name_raw`  
- `counties_raw`  
- `urls_raw`  
- `gps_lat_raw`, `gps_lon_raw` (Access Points)  
- organizational cluster fields  
- `location_raw` (Sites, Access Points)  
- `trail_use_type_raw`, `trail_surface_type_raw`, `total_length_miles_raw`  
- `segment_name_raw`, `segment_length_miles_raw`, `surface_type_raw`, `segment_type_raw`  
- `network_name_raw`, `network_type_raw`  
- `parent_*_raw` lists  
- lineage metadata  

Identity Matching must **not** use:

- `gps_raw`  
- `maps_raw`  
- `map_url`  
- `geometry_raw`  
- inferred or GIS‑derived values  
- normalized values  

All comparisons must be based on raw discovery values.

------------------------------------------------------------
# 9.6 SIMILARITY MATRIX CONSTRUCTION

For each group from Phase 1, the engine must construct a **similarity matrix**:

- rows = records in the group  
- columns = records in the group  
- cell (i, j) = similarity score or null if anchors fail  

The matrix must:

- be symmetric  
- contain no inferred values  
- contain no normalized values  
- contain no scores for anchor failures  

The matrix is the input to Phase 3 (Merge Decisions).

------------------------------------------------------------
# 9.7 DETERMINISM REQUIREMENTS

Identity Matching must be:

- **deterministic** — identical inputs produce identical scores  
- **order‑independent** — discovery order must not affect scoring  
- **pure** — no inference, no normalization, no silent correction  
- **stable** — scoring must not depend on runtime conditions  

The engine must not:

- adjust similarity scores  
- apply thresholds  
- form clusters  

Those actions occur in Phase 3.

------------------------------------------------------------
# 9.8 OUTPUT OF PHASE 2

Phase 2 produces:

- a similarity matrix for each group  
- anchor pass/fail indicators  
- raw similarity scores (0–100)  
- no merges  
- no conflicts  
- no parent resolution  

These outputs are passed directly to Phase 3.

------------------------------------------------------------
# RESOLUTION ENGINE v5.4  
Phase 3 — Merge Decisions  
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# 10. PHASE 3: MERGE DECISIONS

Phase 3 converts the similarity scores from Identity Matching into **deterministic merge clusters** and **review sets**. This phase is where the engine decides *which* records will be merged, *which* require human review, and *which* must remain separate.  

Phase 3 does **not** merge fields, resolve conflicts, or modify raw values. It only determines the grouping of records for Phase 4.

------------------------------------------------------------
# 10.1 PURPOSE OF MERGE DECISIONS

Merge Decisions serve four core purposes:

- **Interpret similarity scores** produced in Phase 2.  
- **Apply merge thresholds** defined in configuration (not hard‑coded).  
- **Form deterministic merge clusters** using similarity ≥ MERGE_THRESHOLD.  
- **Emit review sets** for ambiguous cases.  

This phase ensures that merging is:

- rule‑driven  
- deterministic  
- reproducible  
- auditable  

No field‑level merging occurs here.

------------------------------------------------------------
# 10.2 INPUTS TO PHASE 3

Phase 3 receives:

- similarity matrices from Phase 2  
- anchor pass/fail indicators  
- entity_type for each record  
- configured thresholds:
  - MERGE_THRESHOLD  
  - REVIEW_THRESHOLD  

Phase 3 must not reinterpret similarity scores or modify them.

------------------------------------------------------------
# 10.3 THRESHOLD APPLICATION

Each entity type has two thresholds:

- **MERGE_THRESHOLD**  
  Similarity ≥ MERGE_THRESHOLD → records must be merged.

- **REVIEW_THRESHOLD**  
  REVIEW_THRESHOLD ≤ similarity < MERGE_THRESHOLD → records must be flagged for review.

Similarity < REVIEW_THRESHOLD → records must remain separate.

Thresholds are:

- **configuration**, not logic  
- **entity‑type specific**  
- **external to the engine**  
- **deterministic**  

The engine must apply thresholds exactly as provided.

------------------------------------------------------------
# 10.4 MERGE CLUSTER FORMATION

Records that meet or exceed MERGE_THRESHOLD must be merged into a single cluster.  
Cluster formation must be:

- deterministic  
- order‑independent  
- based solely on similarity ≥ MERGE_THRESHOLD  
- based on undirected connectivity  

### Cluster rules:

- If A merges with B, and B merges with C, then A, B, and C must be in the same cluster—even if A and C were never directly compared.  
- Clusters must represent **connected components** in the similarity graph.  
- No cluster may contain records with anchor failures.  
- No cluster may contain records with similarity < MERGE_THRESHOLD.  

Clusters are the units passed to Phase 4 for field‑level merging.

------------------------------------------------------------
# 10.5 HARD SEPARATION CONDITIONS

Some conditions require records to remain separate even if similarity ≥ MERGE_THRESHOLD. These conditions are defined in the Resolution Rules Module v5.x and include:

- incompatible parent relationships  
- incompatible entity‑type rules  
- violations of parent/child identity constraints  
- violations of multi‑county identity rules  
- identity anchor contradictions discovered post‑scoring  

The engine must:

- apply these separation rules exactly as defined  
- never override them  
- never infer exceptions  

If a hard separation condition is triggered:

- the records must not be merged  
- the pair must be emitted as a **review set**  
- the reason must be recorded in merge provenance  

------------------------------------------------------------
# 10.6 REVIEW SET GENERATION

Review sets capture ambiguous cases where similarity is high enough to warrant human attention but not high enough to justify automatic merging.

A review set must be created when:

- REVIEW_THRESHOLD ≤ similarity < MERGE_THRESHOLD  
- a hard separation condition is triggered  
- identity anchors pass but similarity is inconclusive  
- parent relationships conflict  
- lineage metadata conflicts with parent resolution  
- organizational fields strongly disagree despite high name similarity  

Each review set must include:

- the record IDs involved  
- the similarity score  
- the entity_type  
- the anchor status  
- the fields contributing most to similarity  
- the fields contributing most to disagreement  
- any hard separation conditions triggered  

Review sets must be deterministic and reproducible.

------------------------------------------------------------
# 10.7 NO MERGING IN PHASE 3

Phase 3 must not:

- merge fields  
- modify raw values  
- modify metadata  
- resolve conflicts  
- choose canonical values  
- apply normalization  
- infer missing values  

Phase 3 only determines **which records will be merged**, not **how** they will be merged.

------------------------------------------------------------
# 10.8 OUTPUT OF PHASE 3

Phase 3 produces two outputs:

### 1. **Merge Clusters**
Each cluster is a list of raw discovery records that must be merged in Phase 4.

### 2. **Review Sets**
Each review set is a structured object containing:

- record IDs  
- similarity score  
- entity_type  
- anchor status  
- contributing fields  
- disagreement fields  
- hard separation conditions (if any)  

These outputs are passed directly to Phase 4.

------------------------------------------------------------
# RESOLUTION ENGINE v5.4  
Phase 4 — Field‑Level Merging  
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# 11. PHASE 4: FIELD‑LEVEL MERGING

Phase 4 transforms each merge cluster from Phase 3 into a single **Resolved Entity v5.x**. This phase merges raw values, preserves conflicts, and assembles metadata blocks. It does not normalize, infer, or choose canonical values. All raw values and all metadata must be preserved exactly as discovered.

Field‑level merging is mechanical and rule‑driven. The engine applies merge strategies to each field, using the updated v5.x discovery field model and the merge semantics defined for v5.4.

------------------------------------------------------------
# 11.1 PURPOSE OF FIELD‑LEVEL MERGING

Field‑level merging serves five core purposes:

- **Combine raw values** from all records in a merge cluster.  
- **Preserve all conflicts** without resolving them.  
- **Apply deterministic merge strategies** to each field.  
- **Propagate metadata blocks** without alteration.  
- **Produce a complete, merged identity_block, organizational_block, parent_block, and metadata_block** for the Resolved Entity.

Field‑level merging must not:

- normalize values  
- infer missing values  
- choose between conflicting values  
- modify raw metadata  
- apply category or entity‑type rules  
- apply identity logic  

All decisions about identity and classification were already made in the Rules Module and Phases 1–3.

------------------------------------------------------------
# 11.2 MERGE STRATEGY TYPES

Each field in the discovery model is assigned one of the following merge strategies. These strategies define how raw values are combined and how conflicts are recorded.

### **1. choose**  
Select a single value deterministically, based on tier precedence.  
Used when disagreement is not meaningful or when a single authoritative value is required downstream.

### **2. union**  
Combine all distinct raw values into a list.  
Used for fields where multiple values are meaningful (e.g., URLs, counties, partner agencies).

### **3. choose_or_conflict**  
If all values agree (after matching‑only normalization), choose.  
If values differ, record a conflict in the conflict metadata block.

### **4. conflict**  
Always record a conflict if more than one distinct value exists.  
Used for quantitative fields where disagreement is semantically important (e.g., length, acres).

### **5. metadata_union**  
Merge metadata blocks by combining all entries without modification.  
Used for provenance, lineage, uncertainty, boundary, and baseline metadata.

### **6. parent_resolution**  
Special strategy for merging parent_*_raw lists and preparing them for Phase 5.  
This strategy preserves raw parent names and defers ID resolution to the next phase.

These strategies must be applied exactly as defined. The engine must not reinterpret or override them.

------------------------------------------------------------
# 11.3 FIELD STRATEGY ASSIGNMENT (v5.4)

The following high‑level assignments apply to all entity types. Entity‑specific payloads inherit these rules unless explicitly overridden.

### **Identity Fields**
- name_raw — choose_or_conflict  
- counties_raw — union  
- urls_raw — union  
- location_raw — choose_or_conflict (Sites, Access Points)

### **Organizational Fields**
- ownership_raw — choose_or_conflict  
- governance_raw — choose_or_conflict  
- partner_agencies_raw — union  
- coordination_raw — union  

### **Quantitative Fields**
- total_length_miles_raw — conflict  
- segment_length_miles_raw — conflict  
- difficulty_raw — choose_or_conflict  
- accessibility_raw — choose_or_conflict  

### **Trail/Segment Fields**
- trail_use_type_raw — choose_or_conflict  
- trail_surface_type_raw — choose_or_conflict  
- trail_origin_type_raw — choose_or_conflict  
- surface_type_raw — choose_or_conflict  
- segment_type_raw — choose_or_conflict  

### **Access Point Fields**
- gps_lat_raw — conflict  
- gps_lon_raw — conflict  
- access_point_type_raw — choose_or_conflict  

### **Network Fields**
- network_name_raw — choose_or_conflict  
- network_type_raw — choose_or_conflict  
- member_*_raw — union (raw names only; ID resolution occurs in Phase 5)

### **Metadata Blocks**
- provenance — metadata_union  
- lineage — metadata_union  
- conflict metadata — metadata_union  
- uncertainty metadata — metadata_union  
- boundary metadata — metadata_union  
- baseline metadata — metadata_union  

### **Parent Fields**
- parent_*_raw — parent_resolution  

These assignments ensure that all raw values are preserved and all disagreements are surfaced for normalization.

------------------------------------------------------------
# 11.4 CONFLICT RECORDING

When a field uses **choose_or_conflict** or **conflict**, and multiple distinct raw values exist, the engine must:

- record a conflict entry in the conflict metadata block  
- include:
  - field name  
  - all distinct raw values  
  - source record IDs  
  - source tiers  
  - any relevant URLs or provenance  
- not choose a winner  
- not normalize values  
- not infer a canonical value  

Conflicts are preserved for the Normalization Engine v5.x to resolve.

------------------------------------------------------------
# 11.5 METADATA PROPAGATION

All metadata blocks must be merged using **metadata_union**, which:

- preserves all raw metadata entries  
- does not normalize or reinterpret metadata  
- does not collapse or deduplicate entries unless explicitly required  
- preserves lineage metadata exactly as discovered  
- preserves uncertainty and conflict metadata exactly as discovered  
- preserves boundary and baseline metadata exactly as discovered  

Metadata propagation must be:

- deterministic  
- order‑independent  
- reversible  

No metadata may be discarded.

------------------------------------------------------------
# 11.6 MERGE PROVENANCE

Each merged field must record:

- which merge strategy was applied  
- which source records contributed values  
- whether a conflict was detected  
- whether the field was left unresolved  
- the merge cluster ID  
- the thresholds used in Phase 3  

Merge provenance is stored in the **resolution_provenance** block of the Resolved Entity.

------------------------------------------------------------
# 11.7 OUTPUT OF PHASE 4

Phase 4 produces a **partially resolved entity**, containing:

- merged identity_block  
- merged organizational_block  
- merged raw parent_*_raw lists  
- merged metadata_block  
- merge provenance  

Parent IDs are not yet resolved.  
That occurs in Phase 5.

------------------------------------------------------------
# RESOLUTION ENGINE v5.4  
Phase 5 — Parent Resolution & Resolved Record Construction  
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# 12. PHASE 5: PARENT RESOLUTION AND RESOLVED RECORD CONSTRUCTION

Phase 5 completes the resolution workflow by resolving parent relationships, preserving lineage metadata, and assembling the final **Resolved Entity v5.x** object. This phase does not modify raw values, does not infer missing parents, and does not normalize or reinterpret lineage. It is a mechanical, deterministic transformation from the merged cluster (Phase 4) into a fully structured resolved entity.

------------------------------------------------------------
# 12.1 PURPOSE OF PHASE 5

Phase 5 performs four essential tasks:

- **Resolve parent_*_raw names to internal IDs**, when possible.  
- **Preserve lineage metadata exactly as discovered**, without correction.  
- **Record parent conflicts and uncertainties** when resolution is ambiguous.  
- **Assemble the final Resolved Entity v5.x**, including all merged blocks and provenance.

This phase finalizes the entity for downstream normalization and graph upsert.

------------------------------------------------------------
# 12.2 INPUTS TO PHASE 5

Phase 5 receives:

- the merged entity from Phase 4  
- merged `parent_*_raw` lists  
- merged metadata blocks (including lineage)  
- the full set of resolved entities produced so far (for ID lookup)  
- entity‑type rules and parent/child rules from the Resolution Rules Module v5.x  

Phase 5 must not modify any raw values or metadata.

------------------------------------------------------------
# 12.3 NAME‑TO‑ID PARENT RESOLUTION

Parent resolution converts raw parent names into internal IDs **without altering the raw names**.

### Parent resolution rules:

- Use the entity‑type rules from the Rules Module to determine which parent types are valid.  
- Match raw parent names using the same identity logic as primary entities, but in lookup mode.  
- Use raw county context to disambiguate matches.  
- If exactly one match is found, assign the parent ID.  
- If multiple matches exist, record a parent conflict.  
- If no match exists, record an unresolved parent.  
- Never invent a parent ID.  
- Never infer missing parents.  
- Never modify lineage metadata to “fix” inconsistencies.

Parent resolution is deterministic and reversible.

------------------------------------------------------------
# 12.4 LINEAGE PRESERVATION

Lineage metadata (e.g., `lineage.parent_entity_id`, `lineage.parent_entity_type`) must be:

- preserved exactly as discovered  
- never overwritten  
- never normalized  
- never reconciled with resolved parent IDs  

If lineage metadata contradicts resolved parent IDs:

- record a lineage conflict  
- do not modify either value  
- do not infer a correction  

Lineage is a historical record, not a truth source.

------------------------------------------------------------
# 12.5 PARENT CONFLICT AND UNCERTAINTY HANDLING

Parent conflicts arise when:

- multiple possible parent matches exist  
- no valid parent match exists  
- lineage metadata contradicts resolved parent IDs  
- parent_*_raw lists disagree across merged records  

When a conflict occurs:

- record a conflict entry in the conflict metadata block  
- include:
  - raw parent names  
  - candidate parent IDs (if any)  
  - source record IDs  
  - source tiers  
  - lineage metadata involved  
- do not choose a winner  
- do not infer a canonical parent  

Normalization Engine v5.x will resolve these conflicts later.

------------------------------------------------------------
# 12.6 FINAL RESOLVED ENTITY STRUCTURE (v5.4)

Each Resolved Entity v5.x must contain the following blocks:

### **1. resolved_entity_id**
A stable internal ID assigned by the engine.

### **2. entity_type**
One of the six entity types, inherited from the merge cluster.

### **3. source_records**
List of all raw discovery record IDs that contributed to the merged entity.

### **4. identity_block**
Merged identity fields:
- name_raw  
- counties_raw  
- urls_raw  
- location_raw (if applicable)  
- any entity‑specific identity fields  

### **5. organizational_block**
Merged organizational fields:
- ownership_raw  
- governance_raw  
- partner_agencies_raw  
- coordination_raw  

### **6. parent_block**
Contains:
- raw parent_*_raw lists  
- resolved parent_*_id lists  
- parent conflicts and uncertainties  
- lineage metadata (preserved exactly)  

### **7. metadata_block**
Merged metadata:
- provenance  
- lineage  
- conflict metadata  
- uncertainty metadata  
- boundary metadata  
- baseline metadata  

### **8. resolution_provenance**
A complete record of:
- merge strategies applied  
- similarity thresholds used  
- merge cluster membership  
- conflicts detected  
- parent resolution outcomes  
- any hard separation conditions encountered  

### **9. entity‑specific payload**
Raw fields specific to the entity type (e.g., trail length, segment type, GPS coordinates).

------------------------------------------------------------
# 12.7 OUTPUT OF PHASE 5

Phase 5 produces a fully assembled **Resolved Entity v5.x**, ready for:

- Normalization Engine v5.x  
- Graph upsert  
- Review workflows  
- Audit and provenance analysis  

The resolved entity is:

- deterministic  
- reversible  
- fully traceable  
- ontology‑aligned  
- metadata‑complete  

No further resolution steps occur after Phase 5.

------------------------------------------------------------ 
# END OF RESOLUTION ENGINE v5.4 