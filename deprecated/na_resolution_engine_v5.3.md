# NATURAL AREAS PROJECT
# RESOLUTION ENGINE v5.3
Authoritative Specification for Entity Resolution and Deduplication

The Resolution Engine v5.3 defines the complete workflow for identifying and merging
duplicate entities discovered across all tiers and sources in the v5.x pipeline.
This version updates the Resolution Engine to align with:

- Discovery Output Specification v5.3
- Discovery Metadata Specification v5.3
- Updated identity field model (`gps_lat_raw`, `gps_lon_raw`, `urls_raw`)
- Updated organizational cluster (`ownership_raw`, `governance_raw`, `partner_agencies_raw`, `coordination_raw`)
- Updated parent and lineage model
- Updated metadata propagation requirements
- Removal of `geometry_raw`, `maps_raw`, `map_url`, and `gps_raw`
- Preservation of raw values and conflicts exactly as discovered

This module supersedes Resolution Engine v5.0.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.3

- Updated all identity fields to match Discovery Output Specification v5.3.
- Replaced `gps_raw` with `gps_lat_raw` and `gps_lon_raw`.
- Removed `geometry_raw`, `maps_raw`, and `map_url` from all logic.
- Updated URL handling to use `urls_raw` exclusively.
- Updated organizational field handling to match Metadata v5.3 semantics.
- Updated parent relationship model to use:
  - `parent_*_raw` lists (raw logical parents)
  - lineage metadata (recursive provenance parent)
- Updated merge rules to remove deprecated fields and add new fields.
- Updated metadata propagation rules to include:
  - boundary metadata
  - baseline metadata
  - conflict metadata
  - uncertainty metadata
  - lineage metadata
- Updated Access Point identity logic to use lat/lon pairs.
- Updated Trail Segment and Network logic to remove map dependencies.
- Updated output format to reflect v5.3 resolved record structure.
- Updated resolution provenance model to include metadata merge provenance.

------------------------------------------------------------
# 1. PURPOSE

The Resolution Engine v5.3 provides the authoritative workflow for:

- Identifying duplicate entities across tiers, sources, and recursive paths.
- Merging raw discovery records into unified resolved entities.
- Detecting and preserving conflicts without resolving them.
- Resolving parent relationships (names → IDs) while preserving lineage metadata.
- Propagating all metadata blocks (identity, organizational, provenance, lineage, conflict, uncertainty, boundary, baseline).
- Producing resolved records for downstream normalization and upsert.

Resolution performs **identity detection, merging, and conflict detection**.  
Normalization performs **vocabulary decisions, canonicalization, and tier authority selection**.

------------------------------------------------------------
# 2. RESOLUTION PHILOSOPHY

## 2.1 Core Principle: Detect Conflicts, Do Not Resolve Them

Resolution must:

- Detect duplicate entities.
- Merge complementary raw values.
- Preserve all conflicting values.
- Preserve all raw values exactly as discovered.
- Preserve all metadata exactly as discovered.
- Resolve parent names to IDs without altering lineage metadata.

Resolution must not:

- Normalize vocabulary.
- Infer missing values.
- Invent values.
- Choose between conflicting values.
- Modify raw discovery metadata.

## 2.2 Why This Separation Exists

Normalization rules may change over time.  
Resolution must remain stable, deterministic, and reversible.

By separating detection from decision:

- Resolution can be re-run without changing outcomes.
- Normalization can be re-run with different rules.
- Audit trails remain clean and interpretable.
- Metadata integrity is preserved.

------------------------------------------------------------
# 3. RESOLUTION PIPELINE ARCHITECTURE (UPDATED FOR v5.3)

The Resolution Engine v5.3 operates as the bridge between **Raw Discovery Records v5.3**
and the **Normalization Engine v5.x**, consuming the discovery output structure
(including the embedded metadata object) and producing in‑memory **Resolved Records**.

High‑level flow:

1. **Input:** Raw Discovery Records v5.3 (one per discovered entity occurrence)  
2. **Phase 1 – Grouping:** Partition records by `entity_type` and `county_primary`,
   with special handling for multi‑county entities.  
3. **Phase 2 – Identity Matching:** Within each group, apply entity‑specific
   identity anchors and similarity signatures using v5.3 fields
   (`name_raw`, `counties_raw`, `urls_raw`, organizational fields, GPS where applicable).  
4. **Phase 3 – Merge Decisions:** Use similarity thresholds to decide:
   - auto‑merge  
   - flag for review  
   - keep separate  
5. **Phase 4 – Field Merging:** For each merge set, apply field‑level merge
   strategies (choose, union, conflict, choose_or_conflict) updated to:
   - remove `maps` / `map_url` / `geometry_raw` / `gps_raw`  
   - use `gps_lat_raw` / `gps_lon_raw`  
   - use `url_primary_raw` / `urls_raw`  
   - respect the updated organizational cluster  
   - merge and propagate metadata blocks (identity, organizational, provenance,
     lineage, conflict, uncertainty, boundary, baseline).  
6. **Phase 5 – Parent Resolution:** Resolve `parent_*_raw` name lists to IDs,
   while preserving lineage metadata (`lineage.parent_entity_id`,
   `lineage.parent_entity_type`) exactly as discovered.  
7. **Output:** Resolved Records v5.3 (in‑memory objects) passed directly to the
   Normalization Engine v5.x, with merge provenance and conflict structures
   preserved for audit and downstream decision‑making.

The pipeline is **purely functional** with respect to inputs:

- Given the same Raw Discovery Records v5.3, Resolution must always produce the
  same Resolved Records v5.3 and the same conflict structures.
- No normalization, inference, or silent correction is permitted at any stage.

------------------------------------------------------------
# 4. PHASE 1: GROUPING

## 4.1 Purpose

Grouping reduces comparison space by clustering raw discovery records into
manageable sets before identity matching. This ensures deterministic behavior
and prevents unnecessary cross‑entity comparisons.

## 4.2 Grouping Key

Records must be grouped by:

- `entity_type`
- `county_primary`

This matches the v5.3 discovery output structure and ensures that entities are
only compared against plausible matches.

```python
key = (
    record.entity_type,
    record.county_primary
)

## 4.3 Cross‑County Entities

If an entity spans multiple counties (as indicated by `counties_raw`), it must
be added to each relevant county group:

```python
for county in record.counties_raw:
    key = (record.entity_type, county)
    groups[key].append(record)
	
This ensures that multi‑county entities can participate in matching within every
county where they legitimately appear, without segmenting the entity itself.

## 4.4 Determinism Requirements

- Grouping must be stable and reproducible for a given input set.
- Grouping must not depend on discovery order or runtime conditions.
- Grouping must not use normalized, inferred, or corrected values.
- Grouping must use raw values (`entity_type`, `county_primary`, `counties_raw`)
  exactly as discovered in the Raw Discovery Records v5.3.
- State must never be shared across counties beyond the explicit multi‑county
  inclusion described above.

------------------------------------------------------------
# 5. PHASE 2: IDENTITY MATCHING

## 5.1 Purpose

Identity Matching determines whether two or more Raw Discovery Records v5.3
represent the **same real‑world entity**. This phase uses:

- entity‑specific **identity anchors** (strict prerequisites)
- entity‑specific **identity signatures** (fuzzy similarity scoring)
- updated v5.3 field model (`urls_raw`, `gps_lat_raw`, `gps_lon_raw`, organizational fields)
- raw values only (no normalization for output, matching‑only normalization permitted)

Identity Matching produces **similarity scores (0–100)** used in Phase 3 to
decide whether records should be merged, reviewed, or kept separate.

## 5.2 Identity Anchors (Strict)

Identity anchors define the minimum conditions under which two records may be
compared. If anchors do not match, similarity is **not computed** and the
records cannot be merged.

Anchors must use **raw discovery fields** and must not rely on inferred or
normalized values.

Each entity type defines its own anchor:

- Sites: fuzzy‑normalized name + county overlap  
- Trails: fuzzy‑normalized name + county overlap  
- Trail Segments: parent trail must match (ID), plus segment name if present  
- Trail Networks: fuzzy‑normalized network name + network type  
- Site Networks: fuzzy‑normalized network name + network type  
- Access Points: identity parent + GPS proximity bucket (lat/lon)

Anchors are updated in v5.3 to remove dependencies on deprecated fields such as
`gps_raw`, `map_url`, or `maps_raw`.

## 5.3 Identity Signatures (Fuzzy Similarity)

If anchors match, a similarity score (0–100) is computed using:

- name similarity  
- organizational field similarity (ownership_raw, governance_raw, partner_agencies_raw, coordination_raw)  
- county overlap  
- location_raw similarity (Sites, Access Points)  
- GPS proximity (Access Points)  
- length similarity (Trails, Trail Segments, Networks)  
- surface/use/origin type similarity (Trails, Segments)  
- URL overlap using `urls_raw`  
- network membership similarity (Networks)

All similarity functions must:

- use raw values only  
- avoid normalization that alters values  
- avoid inference  
- avoid silent correction  

Similarity functions may use **matching‑only normalization** (e.g., case folding,
punctuation stripping) as long as raw values remain untouched.

## 5.4 Updated Field Model for Matching (v5.3)

Identity Matching must use the updated discovery fields:

- `name_raw` (no normalization)
- `counties_raw`
- `urls_raw` (includes map URLs)
- `gps_lat_raw`, `gps_lon_raw` (Access Points)
- `ownership_raw`, `governance_raw`, `partner_agencies_raw`, `coordination_raw`
- `location_raw` (Sites, Access Points)
- `difficulty_raw`, `accessibility_raw` (Trails, Segments)
- `parent_*_raw` lists (Segments, Access Points)
- lineage metadata (identity parent)

Identity Matching must **not** use:

- `gps_raw` (removed)
- `maps_raw` (removed)
- `map_url` (removed)
- `geometry_raw` (removed)
- any inferred or GIS‑derived values

## 5.5 Determinism Requirements

Identity Matching must be:

- deterministic for identical inputs  
- independent of discovery order  
- independent of runtime conditions  
- based solely on raw discovery values and metadata  

Similarity scoring must produce identical results for identical inputs.

## 5.6 Entity‑Specific Identity Rules

Each entity type defines its own identity anchor (strict prerequisite) and
identity signature (fuzzy similarity scoring). All rules in this section are
updated to align with the v5.3 discovery field model:

- `urls_raw` replaces all prior URL fields  
- `gps_lat_raw` / `gps_lon_raw` replace `gps_raw`  
- organizational fields use the v5.3 cluster  
- no geometry or map fields are referenced  
- raw values are preserved exactly as discovered  

The following subsections define the updated identity rules for:

- Sites  
- Trails  
- Trail Segments  
- Access Points  
- Trail Networks  
- Site Networks  

Each subsection specifies:

1. **Identity Anchor** — strict conditions required before similarity scoring  
2. **Identity Signature** — weighted fuzzy scoring (0–100)  
3. **Updated field usage** — ensuring compliance with v5.3 discovery output  

------------------------------------------------------------
## 6. SITE IDENTITY RULES (UPDATED FOR v5.3)

Site identity matching uses the updated v5.3 discovery field model and removes all
dependencies on deprecated fields (`gps_raw`, `maps_raw`, `map_url`, `geometry_raw`).
All matching is performed on raw values, with matching‑only normalization permitted
for comparison but never for output.

### 6.1 Site Identity Anchor (Strict)

Two Site records may only be compared if **both** of the following are true:

1. **Name Anchor:**  
   `name_raw` must match under fuzzy name normalization  
   (case‑folding, punctuation stripping, whitespace normalization allowed for matching only).

2. **County Anchor:**  
   The sets `counties_raw` must overlap.  
   (A Site must appear in at least one of the same counties.)

If either anchor fails, similarity scoring is **not computed** and the records
cannot represent the same Site.

### 6.2 Site Identity Signature (Fuzzy Similarity, 0–100)

If anchors match, compute a weighted similarity score:

- **Name similarity — 40 points**  
  Fuzzy string similarity on `name_raw`.

- **Organizational similarity — 35 points total**  
  - ownership_raw match — 10  
  - governance_raw match — 10  
  - partner_agencies_raw overlap — 10  
  - coordination_raw overlap — 5  

- **County overlap — 10 points**  
  Any shared county in `counties_raw`.

- **Location similarity — 10 points**  
  `location_raw` string similarity (if present).

- **URL overlap — 5 points**  
  Overlap in `urls_raw` (includes map URLs).

Total possible: **100 points**.

### 6.3 Updated Field Usage (v5.3 Compliance)

Site identity matching must use:

- `name_raw`  
- `counties_raw`  
- `location_raw`  
- `urls_raw`  
- organizational cluster fields  
- identity metadata (notes_raw may inform manual review but not scoring)

Site identity matching must **not** use:

- `gps_raw`  
- `maps_raw`  
- `map_url`  
- `geometry_raw`  
- any inferred or GIS‑derived values

### 6.4 Determinism Requirements

- Identical inputs must always produce identical similarity scores.
- No inference, normalization for output, or silent correction is permitted.
- Matching‑only normalization must not alter stored raw values.

------------------------------------------------------------
## 7. TRAIL IDENTITY RULES (UPDATED FOR v5.3)

Trail identity matching uses the same updated field model and removes all
dependencies on deprecated geometry or map fields.

### 7.1 Trail Identity Anchor (Strict)

Two Trail records may only be compared if:

1. **Name Anchor:**  
   `name_raw` matches under fuzzy name normalization.

2. **County Anchor:**  
   `counties_raw` overlap.

If either fails, similarity scoring is not computed.

### 7.2 Trail Identity Signature (Fuzzy Similarity, 0–100)

- **Name similarity — 40 points**
- **Trail use type match — 15 points** (`trail_use_type_raw`)
- **Length similarity — 15 points** (`total_length_miles_raw`)
- **Governance match — 10 points**
- **County overlap — 10 points**
- **Surface type match — 5 points** (`trail_surface_type_raw`)
- **URL overlap — 5 points** (`urls_raw`)

### 7.3 Updated Field Usage (v5.3 Compliance)

Trail identity matching must use:

- `name_raw`
- `counties_raw`
- `trail_use_type_raw`
- `trail_surface_type_raw`
- `total_length_miles_raw`
- `urls_raw`
- organizational cluster fields

Trail identity matching must **not** use:

- `maps_raw`
- `map_url`
- `gps_raw`
- `geometry_raw`

------------------------------------------------------------
## 8. TRAIL SEGMENT IDENTITY RULES (UPDATED FOR v5.3)

Trail Segments have the strictest anchors because they are subordinate to Trails.

### 8.1 Trail Segment Identity Anchor (Strict)

Two Trail Segment records may only be compared if:

1. **Parent Trail Anchor:**  
   `parent_trail_id` must match exactly.  
   (If unresolved, matching uses the raw parent name and county set.)

2. **Segment Name Anchor:**  
   If both have `segment_name_raw`, they must match under fuzzy normalization.  
   If both are unnamed, anchor passes.

If parent trails differ, similarity = **0**.

### 8.2 Trail Segment Identity Signature (Fuzzy Similarity, 0–100)

- **Segment name similarity — 50 points**  
  (or 25 points if both unnamed)

- **Length similarity — 20 points** (`segment_length_miles_raw`)

- **Surface type match — 15 points** (`surface_type_raw`)

- **County overlap — 10 points**

- **Segment type match — 5 points** (`segment_type_raw`)

### 8.3 Updated Field Usage (v5.3 Compliance)

Trail Segment identity matching must use:

- `segment_name_raw`
- `segment_length_miles_raw`
- `surface_type_raw`
- `segment_type_raw`
- `counties_raw`
- `parent_trail_id` (or raw parent name if unresolved)

Trail Segment identity matching must **not** use:

- `maps_raw`
- `map_url`
- `gps_raw`
- `geometry_raw`

------------------------------------------------------------
## 9. ACCESS POINT IDENTITY RULES (UPDATED FOR v5.3)

Access Points use the updated GPS model (`gps_lat_raw`, `gps_lon_raw`) and the
updated parent model.

### 9.1 Access Point Identity Anchor (Strict)

Two Access Point records may only be compared if:

1. **Identity Parent Anchor:**  
   `identity_parent_entity_id` matches.  
   (Derived from parent_*_raw + lineage metadata.)

2. **GPS Proximity Anchor:**  
   Both records fall into the same 100‑meter proximity bucket:
	lat_bucket = round(gps_lat_raw, 3) lon_bucket = round(gps_lon_raw, 3)


If either anchor fails, similarity scoring is not computed.

### 9.2 Access Point Identity Signature (Fuzzy Similarity, 0–100)

- **Parent match — 40 points**
- **GPS distance — 30 points**  
<50m = 30 points  
<100m = 20 points

- **Access point type match — 20 points** (`access_point_type_raw`)
- **Name similarity — 10 points** (if both named)

### 9.3 Updated Field Usage (v5.3 Compliance)

Access Point identity matching must use:

- `gps_lat_raw`, `gps_lon_raw`
- `access_point_type_raw`
- `name_raw`
- `parent_*_raw`
- lineage metadata

Access Point identity matching must **not** use:

- `gps_raw`
- `maps_raw`
- `map_url`
- `geometry_raw`

------------------------------------------------------------
## 10. TRAIL NETWORK IDENTITY RULES (UPDATED FOR v5.3)

### 10.1 Trail Network Identity Anchor (Strict)

Two Trail Network records may only be compared if:

- `network_name_raw` matches under fuzzy normalization  
- `network_type_raw` matches exactly (case‑folded for matching only)

### 10.2 Trail Network Identity Signature (Fuzzy Similarity, 0–100)

- **Name similarity — 50 points**
- **Network type match — 20 points**
- **Governance match — 15 points**
- **County overlap — 10 points**
- **URL overlap — 5 points** (`urls_raw`)

------------------------------------------------------------
## 11. SITE NETWORK IDENTITY RULES (UPDATED FOR v5.3)

### 11.1 Site Network Identity Anchor (Strict)

Two Site Network records may only be compared if:

- `network_name_raw` matches under fuzzy normalization  
- `network_type_raw` matches exactly

### 11.2 Site Network Identity Signature (Fuzzy Similarity, 0–100)

- **Name similarity — 50 points**
- **Network type match — 20 points**
- **Governance match — 15 points**
- **County overlap — 10 points**
- **URL overlap — 5 points**

------------------------------------------------------------
# 12. PHASE 3: MERGE DECISIONS

## 12.1 Purpose

Phase 3 converts similarity scores from Identity Matching into **merge decisions**:

- auto‑merge into a single Resolved Entity
- flag for manual review
- keep separate (no merge)

This phase is **entity‑type specific** but follows a common decision pattern.

## 12.2 Decision Inputs

For each candidate pair or cluster:

- similarity score (0–100) from Phase 2
- entity_type
- anchor status (must have passed)
- any hard conflicts that should force separation (e.g., incompatible parents)

## 12.3 Decision Thresholds

Each entity type defines:

- **MERGE_THRESHOLD** — similarity ≥ this value → auto‑merge
- **REVIEW_THRESHOLD** — similarity between REVIEW_THRESHOLD and MERGE_THRESHOLD → flag for review
- similarity < REVIEW_THRESHOLD → keep separate

Thresholds are **configuration**, not hard‑coded into the engine, but the engine must:

- apply thresholds deterministically
- never override thresholds based on runtime conditions
- never auto‑merge below MERGE_THRESHOLD

Example (illustrative only, not prescriptive):

- Sites: MERGE_THRESHOLD = 80, REVIEW_THRESHOLD = 60
- Trails: MERGE_THRESHOLD = 85, REVIEW_THRESHOLD = 65
- Access Points: MERGE_THRESHOLD = 90, REVIEW_THRESHOLD = 70

## 12.4 Cluster Formation

When multiple records are mutually similar above MERGE_THRESHOLD, they form a **merge cluster**:

- clusters must be built using a deterministic algorithm (e.g., union‑find or connected components)
- similarity is treated as an undirected edge between records
- any records connected by a path of edges ≥ MERGE_THRESHOLD belong to the same cluster

Clusters are then passed to Phase 4 for field‑level merging.

## 12.5 Review Sets

Pairs or small clusters with similarity between REVIEW_THRESHOLD and MERGE_THRESHOLD:

- must not be auto‑merged
- must be emitted as **review candidates** with:
  - involved record IDs
  - similarity scores
  - key contributing fields (e.g., name, counties, URLs, parents)
- may be merged later via manual decision or normalization rules, but not in Resolution

## 12.6 Determinism Requirements

- Given identical similarity scores and thresholds, cluster formation must be identical.
- No random tie‑breaking is permitted.
- Review vs merge decisions must be reproducible.

------------------------------------------------------------
# 13. PHASE 4: FIELD‑LEVEL MERGE STRATEGIES (UPDATED FOR v5.3)

## 13.1 Purpose

Phase 4 merges raw discovery records within each merge cluster into a single **Resolved Record v5.3**, using field‑level strategies that:

- preserve all raw values
- detect and record conflicts
- do not normalize or infer values
- respect the updated v5.3 field model (no geometry/map/gps_raw fields)

## 13.2 Merge Strategy Types

Each field is assigned one of the following strategies:

- **choose:** select a single value deterministically (no conflict structure)
- **union:** combine all distinct values into a list (no conflict structure)
- **choose_or_conflict:** if values agree, choose; if they differ, record a conflict
- **metadata_union:** union of metadata blocks (e.g., provenance, lineage)
- **parent_resolution:** special strategy for parent_*_raw and lineage

These strategies are defined formally in Appendix A.

## 13.3 Field Strategy Assignment (High‑Level)

At a high level:

- **Identity fields** (e.g., name_raw, counties_raw, urls_raw):
  - typically **union** or **choose_or_conflict**
- **Organizational fields** (ownership_raw, governance_raw, partner_agencies_raw, coordination_raw):
  - typically **union** or **choose_or_conflict**
- **Quantitative fields** (length, difficulty, etc.):
  - typically **choose_or_conflict**
- **Metadata blocks** (provenance, lineage, conflict, uncertainty, boundary, baseline):
  - **metadata_union** with additional conflict recording where applicable
- **Parent fields**:
  - **parent_resolution** (see Phase 5)

## 13.4 Updated Field Model Compliance

The merge logic must:

- **Use**:
  - `gps_lat_raw`, `gps_lon_raw` (Access Points only)
  - `urls_raw`
  - organizational cluster fields
  - `parent_*_raw` lists
  - lineage metadata
  - boundary/baseline/conflict/uncertainty metadata
- **Not reference**:
  - `gps_raw`
  - `maps_raw`
  - `map_url`
  - `geometry_raw`

## 13.5 Example Field Strategy Table (Conceptual)

The exact schema is defined in the Resolved Record Structure (Section 16), but conceptually:

- **name_raw:** choose_or_conflict
- **counties_raw:** union
- **urls_raw:** union
- **ownership_raw / governance_raw / partner_agencies_raw / coordination_raw:** union
- **total_length_miles_raw / segment_length_miles_raw:** choose_or_conflict
- **trail_use_type_raw / trail_surface_type_raw / access_point_type_raw:** choose_or_conflict
- **location_raw:** choose_or_conflict
- **network_name_raw / network_type_raw:** choose_or_conflict
- **metadata blocks:** metadata_union
- **parent_*_raw:** parent_resolution

## 13.6 Conflict Recording

When a **choose_or_conflict** strategy encounters multiple distinct values:

- the Resolved Record must:
  - not pick a winner
  - record a **conflict entry** in the conflict metadata block, including:
    - field name
    - all distinct values
    - source record IDs
- the field’s resolved value may be:
  - null, or
  - a deterministic placeholder indicating unresolved conflict (implementation‑specific),
  - but Resolution must not invent or normalize a value.

Normalization later may decide how to handle these conflicts.

## 13.7 Provenance Preservation

For every merged field:

- provenance must record:
  - which source records contributed values
  - which strategy was applied
  - whether a conflict was detected
- provenance must be stored in a dedicated **resolution_provenance** block (see Section 18).

------------------------------------------------------------
# 14. PHASE 5: PARENT RESOLUTION AND LINEAGE HANDLING

## 14.1 Purpose

Phase 5 resolves parent relationships from raw names to internal IDs while preserving:

- raw parent_*_raw lists
- lineage metadata (recursive parent relationships)
- conflict and uncertainty around parent assignments

## 14.2 Inputs

For each Resolved Record:

- merged `parent_*_raw` lists (e.g., parent_trail_raw, parent_site_raw, parent_network_raw)
- lineage metadata from discovery (e.g., lineage.parent_entity_id, lineage.parent_entity_type)
- the current set of resolved entities (for ID lookup)

## 14.3 Parent Resolution Rules

1. **Name‑to‑ID Resolution:**
   - For each entry in `parent_*_raw`, attempt to resolve to a Resolved Entity ID:
     - match by entity_type + name_raw + county context
     - use the same identity rules as for primary entities, but in a **lookup mode**
   - If a unique match is found:
     - record `parent_*_id` in the Resolved Record
     - preserve the original raw name in `parent_*_raw`
   - If multiple matches or no match:
     - do not invent an ID
     - record an uncertainty or conflict in metadata

2. **Lineage Preservation:**
   - Do not overwrite or “correct” lineage metadata from discovery.
   - If lineage.parent_entity_id conflicts with resolved parent_*_id:
     - record a conflict in the conflict metadata block
     - do not silently reconcile

3. **Recursive Parent Chains:**
   - Resolution may compute parent chains (e.g., segment → trail → network) for internal use,
     but must:
     - not alter stored lineage metadata
     - not infer missing parents
     - not collapse or normalize the hierarchy

## 14.4 Determinism Requirements

- Given the same set of Resolved Entities and raw parent_*_raw values, parent resolution must:
  - produce the same parent_*_id assignments
  - produce the same conflicts and uncertainties
- No heuristic that depends on runtime order or external state is permitted.

------------------------------------------------------------
# 15. RESOLVED RECORDS v5.3: GENERAL STRUCTURE

## 15.1 Purpose

Resolved Records v5.3 are in‑memory objects produced by the Resolution Engine and consumed by the Normalization Engine. They:

- represent merged entities
- preserve all raw values and conflicts
- include full metadata blocks
- are strictly aligned with the v5.3 discovery model

## 15.2 Common Envelope

All Resolved Records share a common envelope:

- **resolved_entity_id** — stable internal ID for the resolved entity
- **entity_type** — site, trail, trail_segment, access_point, trail_network, site_network
- **source_records** — list of contributing discovery record IDs
- **identity_block** — merged identity fields (names, counties, URLs, etc.)
- **organizational_block** — merged organizational fields
- **parent_block** — resolved parent IDs + raw parent names
- **metadata_block** — composite of:
  - provenance metadata
  - lineage metadata
  - conflict metadata
  - uncertainty metadata
  - boundary metadata
  - baseline metadata
- **resolution_provenance** — how the merge was performed (strategies, thresholds, etc.)

## 15.3 Entity‑Specific Payloads

Each entity type adds its own payload fields, all in raw form:

- **Sites:**
  - name_raw, location_raw, counties_raw, urls_raw
  - organizational cluster fields
  - site‑specific attributes (e.g., amenities_raw, designations_raw) as defined in discovery

- **Trails:**
  - name_raw, counties_raw, urls_raw
  - trail_use_type_raw, trail_surface_type_raw, total_length_miles_raw
  - organizational cluster fields

- **Trail Segments:**
  - segment_name_raw, segment_length_miles_raw, surface_type_raw, segment_type_raw
  - counties_raw
  - parent_trail_id + parent_trail_raw
  - organizational cluster fields (if present)

- **Access Points:**
  - name_raw (optional)
  - gps_lat_raw, gps_lon_raw
  - access_point_type_raw
  - location_raw (if present)
  - parent_*_id + parent_*_raw
  - organizational cluster fields (if present)

- **Trail Networks / Site Networks:**
  - network_name_raw, network_type_raw
  - counties_raw
  - urls_raw
  - organizational cluster fields
  - membership lists (raw member references, not normalized)

## 15.4 Alignment with Discovery v5.3

- Every field in the Resolved Record must map directly to:
  - a discovery field, or
  - a metadata block derived from discovery (provenance, conflict, lineage, etc.)
- No new semantic fields may be introduced at Resolution time.
- Normalization is responsible for any canonical fields or derived attributes.

------------------------------------------------------------
# 16. METADATA PROPAGATION RULES (UPDATED FOR v5.3)

## 16.1 Purpose

Metadata propagation ensures that all relevant metadata from contributing discovery records is:

- preserved
- merged deterministically
- available for downstream normalization and audit

## 16.2 Metadata Blocks

Resolution must handle the following metadata blocks:

- **Provenance metadata** — where and how each record was discovered
- **Lineage metadata** — parent/ancestor relationships as discovered
- **Conflict metadata** — field‑level conflicts detected during merge
- **Uncertainty metadata** — ambiguous or low‑confidence aspects
- **Boundary metadata** — spatial/boundary descriptors (non‑geometry)
- **Baseline metadata** — baseline or reference flags (e.g., authoritative source)

## 16.3 Propagation Strategy

For each metadata block:

- **Provenance metadata:**
  - **metadata_union** of all contributing records
  - no deduplication beyond exact duplicates
  - must include source system, crawl time, and any discovery‑level notes

- **Lineage metadata:**
  - **metadata_union** of all lineage entries
  - do not reconcile or normalize conflicting parent chains
  - record conflicts where parent_entity_id or parent_entity_type disagree

- **Conflict metadata:**
  - constructed during merge (see Section 17)
  - not present in discovery; Resolution is the first producer

- **Uncertainty metadata:**
  - **metadata_union**
  - includes flags such as “parent ambiguous”, “GPS approximate”, etc.
  - Resolution may add uncertainty flags when parent resolution or identity matching is ambiguous

- **Boundary metadata:**
  - **metadata_union**
  - includes non‑geometry boundary descriptors (e.g., “county‑wide”, “multi‑jurisdictional”)
  - must not include geometry_raw or derived shapes

- **Baseline metadata:**
  - **metadata_union**
  - includes indicators of baseline/authoritative records
  - Resolution must not reinterpret or override baseline flags

## 16.4 No Loss, No Invention

- No metadata from discovery may be dropped.
- No new metadata semantics may be invented.
- Resolution may add:
  - conflict entries
  - uncertainty flags
  - resolution_provenance entries
  but must not alter original discovery metadata.

------------------------------------------------------------
# 17. CONFLICT MODEL v5.3

## 17.1 Purpose

The conflict model captures **field‑level disagreements** between contributing records so that:

- Resolution remains non‑destructive
- Normalization can make explicit decisions later
- Auditors can see exactly what disagreed and where it came from

## 17.2 Conflict Entry Structure

Each conflict entry must include:

- **field_name** — the field with conflicting values
- **values** — list of distinct raw values
- **source_records** — list of discovery record IDs contributing each value
- **entity_type** — for context
- **notes** (optional) — machine‑generated notes about the nature of the conflict

Conflicts are stored in the **conflict metadata block** within the Resolved Record.

## 17.3 Conflict Triggers

Conflicts are created when:

- a **choose_or_conflict** strategy encounters multiple distinct values
- parent resolution finds:
  - multiple possible parent IDs
  - disagreement between lineage.parent_entity_id and resolved parent_*_id
- identity metadata (e.g., notes_raw) contains explicit contradictions that can be structurally detected (optional, implementation‑dependent)

## 17.4 Non‑Resolution of Conflicts

Resolution must:

- never pick a winner among conflicting values
- never discard conflicting values
- never normalize conflicting values into a single canonical form

Normalization may later:

- choose a canonical value
- mark one source as authoritative
- suppress or override certain conflicts

but these actions are outside the Resolution Engine.

## 17.5 Determinism

Given the same input records and merge strategies:

- the same set of conflicts must be produced
- conflict entries must be ordered deterministically (e.g., sorted by field_name, then value)

------------------------------------------------------------
# 18. RESOLUTION PROVENANCE MODEL

## 18.1 Purpose

Resolution provenance explains **how** a Resolved Record was formed:

- which records were merged
- which strategies were applied
- which thresholds and rules were in effect

This enables:

- reproducibility
- auditability
- safe re‑runs under new normalization rules

## 18.2 Resolution Provenance Structure

Each Resolved Record must include a **resolution_provenance** block with:

- **engine_version** — e.g., "Resolution Engine v5.3"
- **run_id** — identifier for the resolution run (batch or job)
- **timestamp** — when resolution was executed
- **merge_cluster**:
  - list of source discovery record IDs
  - pairwise similarity scores (optional but recommended)
  - decision outcome (merged / review / separate)
- **field_strategies**:
  - mapping of field_name → strategy_name (choose, union, choose_or_conflict, metadata_union, parent_resolution)
- **thresholds**:
  - MERGE_THRESHOLD and REVIEW_THRESHOLD used for this entity_type
- **conflict_summary**:
  - count of conflicts by field_name
  - optional severity or impact indicators

## 18.3 Stability and Re‑Run Behavior

If Resolution is re‑run with:

- the same engine_version
- the same thresholds
- the same discovery inputs

then:

- resolution_provenance must be identical
- Resolved Records must be identical
- conflict structures must be identical

If engine_version or thresholds change, provenance must reflect the new configuration, enabling comparison between runs.

------------------------------------------------------------
# 19. DETERMINISM AND RE‑RUN GUARANTEES

## 19.1 Determinism Requirements

The Resolution Engine v5.3 must be:

- **purely functional** with respect to its inputs:
  - same inputs → same outputs
- independent of:
  - discovery order
  - runtime environment
  - non‑deterministic operations

## 19.2 Sources of Non‑Determinism to Avoid

Resolution must not:

- rely on random tie‑breaking
- rely on non‑stable sorting without explicit keys
- use external mutable state (e.g., “first seen” caches)
- depend on wall‑clock time for any decision logic

Timestamps may be recorded in provenance but must not affect merge decisions.

## 19.3 Re‑Run Scenarios

Resolution may be re‑run when:

- new discovery records are added
- discovery specifications are updated (e.g., v5.4)
- normalization rules change and require a fresh resolved baseline

In all cases:

- previously resolved entities must be reproducible from their original inputs
- differences between runs must be attributable to:
  - changes in inputs, or
  - changes in engine_version / configuration (captured in provenance)

------------------------------------------------------------
# APPENDIX A: MERGE STRATEGY DEFINITIONS

## A.1 Strategy: choose

**Purpose:** Select a single value when all contributing values are identical or when a deterministic choice is acceptable and non‑conflicting.

**Behavior:**

- If all non‑null values are identical:
  - resolved_value = that value
  - no conflict entry
- If values differ:
  - implementation may:
    - treat as an implicit conflict and escalate to choose_or_conflict, or
    - require pre‑validation to ensure choose is only used where values are guaranteed identical
  - Resolution v5.3 recommends using choose only where upstream guarantees uniqueness.

## A.2 Strategy: union

**Purpose:** Preserve all distinct values in a list.

**Behavior:**

- Collect all non‑null values from contributing records.
- Deduplicate by exact match.
- resolved_value = list of distinct values.
- No conflict entry is created; union is considered non‑conflicting by design.

**Use Cases:**

- counties_raw
- urls_raw
- partner_agencies_raw
- coordination_raw (if modeled as a list)

## A.3 Strategy: choose_or_conflict

**Purpose:** Either choose a single value when all values agree, or record a conflict when they do not.

**Behavior:**

- Collect all non‑null values.
- If the set of distinct values has size 0:
  - resolved_value = null
  - no conflict
- If size 1:
  - resolved_value = the single value
  - no conflict
- If size > 1:
  - resolved_value = null or unresolved placeholder
  - create a conflict entry:
    - field_name
    - values (all distinct values)
    - source_records

**Use Cases:**

- name_raw (when multiple name variants exist)
- length fields (total_length_miles_raw, segment_length_miles_raw)
- trail_use_type_raw, trail_surface_type_raw
- access_point_type_raw
- network_name_raw, network_type_raw

## A.4 Strategy: metadata_union

**Purpose:** Merge metadata blocks without losing any entries.

**Behavior:**

- For each metadata block (provenance, lineage, uncertainty, boundary, baseline):
  - collect all entries from contributing records
  - deduplicate exact duplicates
  - resolved_metadata_block = union of entries
- No conflicts are created by metadata_union itself; conflicts are recorded separately when semantics disagree (e.g., conflicting parents).

**Use Cases:**

- provenance metadata
- lineage metadata
- uncertainty metadata
- boundary metadata
- baseline metadata

## A.5 Strategy: parent_resolution

**Purpose:** Resolve parent relationships while preserving raw names and lineage.

**Behavior:**

1. Merge `parent_*_raw` lists using union.
2. For each raw parent entry:
   - attempt to resolve to a Resolved Entity ID using lookup rules
   - if unique match:
     - add to `parent_*_id` list
   - if ambiguous or no match:
     - add uncertainty entry
3. Compare resolved parent_*_id with lineage.parent_entity_id:
   - if they disagree:
     - create a conflict entry for the parent field

**Use Cases:**

- parent_trail_raw / parent_trail_id
- parent_site_raw / parent_site_id
- parent_network_raw / parent_network_id

------------------------------------------------------------
# APPENDIX B: SUMMARY OF v5.3 ALIGNMENT CHANGES

For quick reference, Resolution Engine v5.3:

- replaces `gps_raw` with `gps_lat_raw` and `gps_lon_raw` (Access Points)
- removes all references to:
  - `geometry_raw`
  - `maps_raw`
  - `map_url`
- uses `urls_raw` as the sole URL field (including map URLs)
- uses the updated organizational cluster:
  - ownership_raw
  - governance_raw
  - partner_agencies_raw
  - coordination_raw
- uses `parent_*_raw` lists and lineage metadata for parent resolution
- propagates all metadata blocks:
  - provenance
  - lineage
  - conflict
  - uncertainty
  - boundary
  - baseline
- maintains strict separation between:
  - Resolution (detection, merging, conflict recording)
  - Normalization (canonicalization, vocabulary decisions, authority selection)

This completes the **NATURAL AREAS PROJECT — RESOLUTION ENGINE v5.3** specification.
