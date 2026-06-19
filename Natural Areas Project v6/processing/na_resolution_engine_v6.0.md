# RESOLUTION ENGINE v6.0
Authoritative Execution Framework for Entity Resolution
Natural Areas Project — v6.x Pipeline

This module supersedes Resolution Engine v5.5.

------------------------------------------------------------
# CHANGES FROM v5.5 → v6.0

- **Entity type consolidation**: Trail, Trail Segment, and Trail Network are
  unified into the single Trailthing entity type. All references to Trail,
  Trail Segment, and Trail Network updated throughout. §2 Scope, §8.2 Grouping
  Keys, §9.3 Identity Anchors, §9.5 Field Model, §11.3 Field Strategy Assignment,
  §12.6 Resolved Entity Structure updated.

- **§9.5 Field Model updated**: Trail/Segment/Network entity-specific fields
  replaced with Trailthing fields. New fields added for all four entity types
  (habitat_type_raw, access_notes_raw, last_verified_date, field_verified for
  Sites; source_term_raw, source_hierarchy_context_raw, parent_id_raw,
  site_parent_raw, parent_site_network_raw,
  member_trailthing_names_raw for Trailthings; parent_trailthings_raw for
  Access Points replacing parent_trails_raw + parent_trail_segments_raw).

- **§11.3 Field Strategy Assignment updated**: Trail/Segment/Network field
  strategies replaced with Trailthing field strategies. source_term_raw
  added as choose_or_conflict (REQUIRED). Trailthing parent fields updated.

- **§11.8 Cross-Tier Trail Canonicalization renamed and scope extended**:
  Now §11.8 Cross-Tier Trailthing Canonicalization. Detection criteria updated
  to entity_type = Trailthing. Scope limitation (was "Trail entities only")
  updated to "all Trailthing entities." §11.8.6 updated accordingly.

- **§12.6 Resolved Entity Structure updated**: entity_type is now one of four
  types (Site, Trailthing, Site Network, Access Point); Trailthing-specific
  parent relationships documented in parent_block.

- **All v5.5 rules carried forward**: design principles (§4), five-phase
  pipeline (§6), grouping rules (§8), identity matching (§9), merge decisions
  (§10), field-level merging (§11), parent resolution and record construction
  (§12).

------------------------------------------------------------
# 1. PURPOSE

The Resolution Engine v6.0 provides the authoritative, deterministic workflow for
transforming **Raw Discovery Records v6.x** into **Resolved Entities v6.x**. It
performs the mechanical execution of identity detection, similarity scoring, merge
decisions, field-level merging, parent resolution, and metadata propagation.

This module does **not** define identity anchors, identity signatures, entity-type
rules, category rules, parent/child rules, or multi-county rules. Those are defined
exclusively in the **Resolution Rules Module v6.x**, which this engine consumes.

Resolution Engine v6.0 is responsible for:

- grouping raw discovery records into comparison sets
- applying identity anchors and signatures defined in the Rules Module
- computing similarity scores
- forming deterministic merge clusters
- merging raw values using field-level strategies
- preserving all conflicts without resolving them
- resolving parent names to IDs while preserving lineage metadata
- assembling complete Resolved Records v6.x for downstream normalization
- assigning canonical tier status to cross-tier Trailthing records (§11.8)

Resolution Engine v6.0 is **purely mechanical**. It does not interpret, infer,
normalize, or decide between conflicting values — except for the canonical tier
assignment described in §11.8, which is a deterministic rule-driven operation.

------------------------------------------------------------
# 2. SCOPE

Resolution Engine v6.0 governs:

- all four entity types (Site, Trailthing, Site Network, Access Point)
- all raw discovery records produced by v6.x discovery modules
- all metadata blocks defined in discovery metadata specifications
- all parent_*_raw lists and lineage metadata
- all merge provenance and conflict structures
- all similarity scoring and merge decisions
- canonical tier assignment for cross-tier Trailthing records

Resolution Engine v6.0 does **not**:

- normalize vocabulary
- choose canonical values
- apply tier authority (except for the cross-tier Trailthing rule in §11.8)
- infer missing values
- modify raw values
- modify raw metadata
- apply category rules
- apply entity-type rules
- apply identity logic beyond what is defined in the Rules Module

Normalization Engine v6.0 performs all vocabulary decisions, canonicalization,
and conflict resolution.

------------------------------------------------------------
# 3. ARCHITECTURAL ROLE

Resolution Engine v6.0 sits between:

- **Discovery v6.x** (raw values + metadata)
- **Normalization v6.0** (canonicalization + vocabulary decisions)

Its role is to:

1. **Preserve** all raw values exactly as discovered
2. **Detect** identity relationships
3. **Merge** records mechanically
4. **Record** conflicts without resolving them
5. **Propagate** metadata blocks without alteration
6. **Resolve** parent names to IDs without modifying lineage metadata
7. **Assign** canonical tier status to cross-tier Trailthing records (§11.8)
8. **Produce** deterministic Resolved Records v6.x

The engine is intentionally **stateless**, **deterministic**, and **reversible**.

------------------------------------------------------------
# 4. DESIGN PRINCIPLES

### 4.1 Determinism
Given identical inputs, the engine must always produce identical outputs.
No randomness, order-dependence, or heuristic shortcuts are permitted.

### 4.2 Purity
Resolution Engine v6.0 must not modify, infer, or normalize raw values or metadata.
All transformations must be mechanical and reversible.

### 4.3 Rule Externalization
All identity anchors, signatures, entity-type rules, category rules, and parent/child
rules live in the Resolution Rules Module v6.x. The engine must call those rules,
not re-implement them.

### 4.4 Metadata Integrity
All metadata blocks (identity, organizational, provenance, lineage, conflict,
uncertainty, boundary, baseline) must be preserved exactly as discovered and merged
without alteration.

### 4.5 No Inference
The engine must not infer:
- missing parents
- missing counties
- missing URLs
- missing organizational fields
- missing GPS values
- missing lineage metadata

### 4.6 No Normalization
The engine must not normalize names, categories, URLs, organizational fields, or GPS
values. Matching-only normalization is permitted **only** inside the identity functions
defined in the Rules Module.

### 4.7 No Ontological Decisions
The engine must not decide entity type, category, parent/child classification, network
membership, or multi-county identity. Those decisions are defined in the Rules Module.

### 4.8 No Classification of Trailthings
The engine must not classify Trailthings as trail vs. trail network vs. trail segment.
That classification is deferred per IMP-009 and will be made systematically after
sufficient county runs. Resolution treats all Trailthings uniformly.

------------------------------------------------------------
# 5. INPUTS AND OUTPUTS

### 5.1 Inputs
Resolution Engine v6.0 consumes:

- Raw Discovery Records v6.x
- All embedded metadata blocks
- Identity anchors and signatures from the Rules Module
- Entity-type and category rules from the Rules Module
- Parent/child rules from the Rules Module
- Multi-county rules from the Rules Module
- Merge thresholds (configuration)

### 5.2 Outputs
Resolution Engine v6.0 produces:

- Resolved Records v6.x (in-memory objects)
- Conflict metadata blocks
- Review sets (for similarity scores below merge threshold)
- Merge provenance metadata
- Parent resolution metadata
- Lineage preservation metadata
- Canonical tier assignments for cross-tier Trailthing records

These outputs are consumed directly by the Normalization Engine v6.0.

------------------------------------------------------------
# 6. PIPELINE OVERVIEW

Resolution Engine v6.0 executes the following phases:

1. **Phase 1 — Grouping**
   Partition raw discovery records into deterministic comparison sets.

2. **Phase 2 — Identity Matching**
   Apply identity anchors and signatures from the Rules Module to compute similarity
   scores.

3. **Phase 3 — Merge Decisions**
   Convert similarity scores into merge clusters and review sets.

4. **Phase 4 — Field-Level Merging**
   Merge raw values using deterministic strategies while preserving conflicts.
   Includes cross-tier Trailthing canonicalization (§11.8).

5. **Phase 5 — Parent Resolution and Metadata Assembly**
   Resolve parent names to IDs, preserve lineage metadata, and assemble
   Resolved Records v6.x.

Each phase is deterministic, reversible, and rule-driven.

------------------------------------------------------------
# 7. MODULE DEPENDENCIES

Resolution Engine v6.0 depends on:

- **Resolution Rules Module v6.x** *(or v5.x until v6.x is written)*
  (identity anchors, identity signatures, entity-type rules, category rules,
  parent/child rules, multi-county rules)

- **Discovery Metadata Specification v6.0**
  (raw field model — Trailthing fields, new Site/AP fields)

- **Discovery Orchestration Module v6.0**
  (cross-tier Trailthing flagging semantics)

- **Normalization Engine v6.0**
  (downstream consumer)

- **Entity Graph Schema v6.x**
  (ID structure and parent relationships)

Resolution Engine v6.0 must not duplicate logic from these modules.

------------------------------------------------------------
# RESOLUTION ENGINE v6.0
Phase 1 — Grouping
Natural Areas Project — v6.x Pipeline

------------------------------------------------------------
# 8. PHASE 1: GROUPING

Phase 1 partitions Raw Discovery Records v6.x into deterministic comparison sets.
Grouping defines which records are allowed to be compared, which similarity scores
will ever be computed, and which entities can ever be merged.

Grouping must never infer, normalize, or reinterpret raw values. It must use raw
discovery fields exactly as provided.

------------------------------------------------------------
# 8.1 PURPOSE OF GROUPING

Grouping serves three critical functions:

- **Reduce comparison space** by preventing unnecessary cross-entity comparisons.
- **Enforce ontological boundaries** by ensuring that only plausible candidates are
  compared.
- **Guarantee determinism** by producing stable, reproducible comparison sets.

Grouping is not a heuristic. It is a strict partitioning step that defines the
universe of possible identity matches.

------------------------------------------------------------
# 8.2 GROUPING KEYS

Each Raw Discovery Record v6.x must be assigned to one or more groups based on:

- **entity_type**
- **county_primary**

This produces grouping keys of the form: `(entity_type, county_primary)`

These keys reflect the two most stable, non-inferred identity dimensions available
at discovery time. Grouping by these keys ensures that:

- Sites are only compared to Sites.
- Trailthings are only compared to Trailthings.
- Site Networks are only compared to Site Networks.
- Access Points are only compared to Access Points.

This prevents cross-type comparisons and enforces the ontological boundaries defined
in the Resolution Rules Module v6.x.

**Note on Trailthings**: Trailthings of all scales and apparent hierarchy levels
(trail systems, individual trails, connectors) are grouped and compared together
within the same entity type. The engine does not create sub-groups by apparent
scale or hierarchy. Records from any discovery tier that name the same Trailthing
will land in the same comparison group.

------------------------------------------------------------
# 8.3 MULTI-COUNTY ENTITIES

If a record's `counties_raw` list contains more than one county, the record must
be added to **every** corresponding county group.

For example, a Trailthing with `counties_raw = ["Wood", "Lucas"]` must be placed into:
- (Trailthing, Wood)
- (Trailthing, Lucas)

This ensures that multi-county entities can match with records discovered in any
of their legitimate counties, without splitting the entity or creating county-specific
duplicates.

Multi-county grouping rules:
- Multi-county inclusion is **additive**, not substitutive.
- A record must appear in **all** groups corresponding to its raw counties.
- No inference or GIS-based county expansion is permitted.
- No normalization of county names is permitted.

------------------------------------------------------------
# 8.4 GROUPING MUST USE RAW VALUES ONLY

Grouping must use: `entity_type`, `county_primary`, `counties_raw`

Grouping must **not** use: normalized values, inferred values, GIS-derived values,
geometry, map URLs, organizational fields, identity signatures, parent_*_raw,
or lineage metadata.

------------------------------------------------------------
# 8.5 DETERMINISM REQUIREMENTS

Grouping must be stable, order-independent, pure, and reversible. The grouping phase
must not reorder raw values, modify metadata, infer missing counties, collapse
multi-county entities, or apply any identity logic.

------------------------------------------------------------
# 8.6 OUTPUT OF PHASE 1

The output of Phase 1 is a deterministic mapping:
`(group_key) → [list of raw discovery records]`

No similarity scoring, merging, or conflict detection occurs in Phase 1.

------------------------------------------------------------
# RESOLUTION ENGINE v6.0
Phase 2 — Identity Matching
Natural Areas Project — v6.x Pipeline

------------------------------------------------------------
# 9. PHASE 2: IDENTITY MATCHING

Phase 2 determines whether two or more Raw Discovery Records v6.x represent the
same real-world entity. Identity Matching is a pure execution layer: all identity
logic is defined in the **Resolution Rules Module v6.x**, and the engine applies
those rules deterministically.

------------------------------------------------------------
# 9.1 PURPOSE OF IDENTITY MATCHING

Identity Matching:
- **Applies identity anchors** to determine whether two records are eligible for comparison.
- **Computes similarity scores** using identity signatures defined in the Rules Module.
- **Produces a similarity matrix** for each grouping from Phase 1.

------------------------------------------------------------
# 9.2 RELATIONSHIP TO THE RESOLUTION RULES MODULE v6.x

The engine must call the following rule sets from the Resolution Rules Module v6.x:

- **Identity Anchors** (strict prerequisites)
- **Identity Signatures** (weighted similarity scoring)
- **Entity-Type Definitions** (to ensure correct rule selection)
- **Parent/Child Rules** (for Access Points and Trailthings with site parents)
- **Multi-County Rules** (for anchor evaluation)

The engine must not reinterpret, modify, or override these rules.

------------------------------------------------------------
# 9.3 IDENTITY ANCHORS (STRICT PREREQUISITES)

Identity anchors determine whether two records may be compared at all. Anchors must:
- use raw discovery fields only
- be applied exactly as defined in the Rules Module
- be evaluated before any similarity scoring
- be deterministic and order-independent

Anchor failure is final; no fallback or inference is permitted.

Examples of anchor requirements (defined in the Rules Module):
- Sites: fuzzy-normalized name + county overlap
- Trailthings: fuzzy-normalized name + county overlap
- Access Points: identity parent + GPS proximity bucket
- Site Networks: fuzzy-normalized network name + network type

The engine simply calls these rules.

------------------------------------------------------------
# 9.4 IDENTITY SIGNATURES (FUZZY SIMILARITY)

If anchors pass, the engine computes a similarity score using the identity signature
defined for the entity type in the Rules Module.

Identity signatures:
- produce a score from **0 to 100**
- use weighted components (name similarity, organizational similarity, GPS proximity, etc.)
- use raw values only
- may apply matching-only normalization internally
- must not modify or normalize raw values for output

------------------------------------------------------------
# 9.5 FIELD MODEL FOR MATCHING (v6.0)

Identity Matching must use the v6.x discovery fields. The following replaces the
v5.5 §9.5 field model.

**Fields shared by all entity types:**
- `name_raw`
- `counties_raw`
- `urls_raw`
- `governance_raw`, `ownership_raw`, `partner_agencies_raw`, `coordination_raw`
- `identity_notes_raw`
- `discovery_tier`
- `last_verified_date`, `field_verified`

**Site-specific fields:**
- `category_raw`, `subtype_raw`, `designation_raw`, `status_raw`
- `location_raw`, `gps_lat_raw`, `gps_lon_raw`
- `acres_raw`
- `description_raw`, `features_raw`
- `habitat_type_raw` *(new in v6.0)*
- `access_notes_raw` *(new in v6.0)*
- `parent_site_raw`

**Trailthing-specific fields:**
- `source_term_raw` *(REQUIRED — primary identity signal alongside name)*
- `source_hierarchy_context_raw`
- `use_type_raw`, `surface_raw`, `origin_type_raw`, `org_type_raw`
- `status_raw`, `difficulty_raw`, `accessibility_raw`
- `total_length_raw`
- `parent_id_raw` *(self-referential Trailthing parent)*
- `site_parent_raw` *(parent Site)*
- `parent_site_network_raw` *(parent Site Network)*
- `member_trailthing_names_raw`

**Site Network-specific fields:**
- `network_type_raw`, `org_type_raw`, `status_raw`
- `member_sites_raw`

**Access Point-specific fields:**
- `access_point_type_raw`, `status_raw`
- `gps_lat_raw`, `gps_lon_raw`
- `address_raw`
- `parent_sites_raw`
- `parent_trailthings_raw` *(replaces parent_trails_raw + parent_trail_segments_raw)*

Identity Matching must **not** use inferred or GIS-derived values, normalized values,
or any field not listed above.

**Special note on source_term_raw**: When two Trailthing records have the same name
and overlapping counties, `source_term_raw` is an important secondary matching signal.
Records with conflicting source terms (e.g., one calls the entity a "trail system,"
another calls a same-named entity a "connector") should receive a review flag in the
review set even if they otherwise score above the merge threshold. The Rules Module
defines the exact weight of this signal.

------------------------------------------------------------
# 9.6 SIMILARITY MATRIX CONSTRUCTION

For each group from Phase 1, the engine must construct a **similarity matrix**:
- rows = records in the group
- columns = records in the group
- cell (i, j) = similarity score or null if anchors fail

The matrix must be symmetric, contain no inferred values, and contain no scores for
anchor failures.

------------------------------------------------------------
# 9.7 DETERMINISM REQUIREMENTS

Identity Matching must be deterministic, order-independent, pure, and stable. The
engine must not adjust scores, apply thresholds, or form clusters in this phase.

------------------------------------------------------------
# 9.8 OUTPUT OF PHASE 2

Phase 2 produces:
- a similarity matrix for each group
- anchor pass/fail indicators
- raw similarity scores (0–100)
- no merges, no conflicts, no parent resolution

------------------------------------------------------------
# RESOLUTION ENGINE v6.0
Phase 3 — Merge Decisions
Natural Areas Project — v6.x Pipeline

------------------------------------------------------------
# 10. PHASE 3: MERGE DECISIONS

Phase 3 converts similarity scores into **deterministic merge clusters** and
**review sets**. It determines *which* records will be merged, *which* require
human review, and *which* must remain separate.

Phase 3 does **not** merge fields, resolve conflicts, or modify raw values.

------------------------------------------------------------
# 10.1 PURPOSE OF MERGE DECISIONS

Merge Decisions:
- **Interpret similarity scores** from Phase 2.
- **Apply merge thresholds** defined in configuration.
- **Form deterministic merge clusters** using similarity ≥ MERGE_THRESHOLD.
- **Emit review sets** for ambiguous cases.

------------------------------------------------------------
# 10.2 INPUTS TO PHASE 3

Phase 3 receives:
- similarity matrices from Phase 2
- anchor pass/fail indicators
- entity_type for each record
- configured thresholds: MERGE_THRESHOLD, REVIEW_THRESHOLD

------------------------------------------------------------
# 10.3 THRESHOLD APPLICATION

Each entity type has two thresholds:
- **MERGE_THRESHOLD**: Similarity ≥ MERGE_THRESHOLD → records must be merged.
- **REVIEW_THRESHOLD**: REVIEW_THRESHOLD ≤ similarity < MERGE_THRESHOLD → records
  must be flagged for review.
- Similarity < REVIEW_THRESHOLD → records must remain separate.

Thresholds are configuration, not logic; entity-type specific; external to the engine.

------------------------------------------------------------
# 10.4 MERGE CLUSTER FORMATION

Records that meet or exceed MERGE_THRESHOLD must be merged into a single cluster.
Cluster formation must be deterministic, order-independent, and based on undirected
connectivity (transitive closure: if A merges with B, and B merges with C, then
A/B/C are in the same cluster). No cluster may contain records with anchor failures.

------------------------------------------------------------
# 10.5 HARD SEPARATION CONDITIONS

Some conditions require records to remain separate even if similarity ≥
MERGE_THRESHOLD. These are defined in the Resolution Rules Module and include:
- incompatible parent relationships
- incompatible entity-type rules
- identity anchor contradictions discovered post-scoring

If a hard separation condition is triggered: records must not be merged; the pair
must be emitted as a review set; the reason must be recorded in merge provenance.

------------------------------------------------------------
# 10.6 REVIEW SET GENERATION

A review set must be created when:
- REVIEW_THRESHOLD ≤ similarity < MERGE_THRESHOLD
- a hard separation condition is triggered
- identity anchors pass but similarity is inconclusive
- parent relationships conflict
- organizational fields strongly disagree despite high name similarity
- source_term_raw values are incompatible (Trailthings only)

Each review set must include: record IDs, similarity score, entity_type, anchor
status, contributing fields, disagreement fields, and any hard separation conditions.

------------------------------------------------------------
# 10.7 NO MERGING IN PHASE 3

Phase 3 must not merge fields, modify raw values or metadata, resolve conflicts,
choose canonical values, apply normalization, or infer missing values.

------------------------------------------------------------
# 10.8 OUTPUT OF PHASE 3

Phase 3 produces:
1. **Merge Clusters** — lists of raw discovery records to be merged in Phase 4.
2. **Review Sets** — structured objects with record IDs, scores, and disagreement data.

------------------------------------------------------------
# RESOLUTION ENGINE v6.0
Phase 4 — Field-Level Merging
Natural Areas Project — v6.x Pipeline

------------------------------------------------------------
# 11. PHASE 4: FIELD-LEVEL MERGING

Phase 4 transforms each merge cluster from Phase 3 into a single **Resolved
Entity v6.x**. This phase merges raw values, preserves conflicts, assigns canonical
tier status to cross-tier Trailthing records (§11.8), and assembles metadata blocks.

Field-level merging is mechanical and rule-driven. The engine applies merge strategies
to each field using the v6.x discovery field model.

------------------------------------------------------------
# 11.1 PURPOSE OF FIELD-LEVEL MERGING

Field-level merging:
- Combines raw values from all records in a merge cluster.
- Preserves all conflicts without resolving them.
- Applies deterministic merge strategies to each field.
- Propagates metadata blocks without alteration.
- Produces a complete merged identity_block, organizational_block, parent_block,
  and metadata_block for the Resolved Entity.

------------------------------------------------------------
# 11.2 MERGE STRATEGY TYPES

### 1. choose
Select a single value deterministically, based on tier precedence.

### 2. union
Combine all distinct raw values into a list.

### 3. choose_or_conflict
If all values agree (after matching-only normalization), choose. If values differ,
record a conflict in the conflict metadata block.

### 4. conflict
Always record a conflict if more than one distinct value exists. Used for quantitative
fields where disagreement is semantically important.

### 5. metadata_union
Merge metadata blocks by combining all entries without modification.

### 6. parent_resolution
Special strategy for merging parent_*_raw lists and preparing for Phase 5.
Preserves raw parent names and defers ID resolution to the next phase.

------------------------------------------------------------
# 11.3 FIELD STRATEGY ASSIGNMENT (v6.0)

The following assignments apply to all entity types unless explicitly overridden.

### Identity Fields
- `name_raw` — choose_or_conflict
- `counties_raw` — union
- `urls_raw` — union
- `location_raw` — choose_or_conflict (Sites, Access Points)

### Organizational Fields
- `ownership_raw` — choose_or_conflict
- `governance_raw` — choose_or_conflict
- `partner_agencies_raw` — union
- `coordination_raw` — union

### Site-Specific Fields
- `category_raw` — choose_or_conflict
- `subtype_raw` — choose_or_conflict
- `designation_raw` — union
- `status_raw` — choose_or_conflict
- `gps_lat_raw` — conflict
- `gps_lon_raw` — conflict
- `acres_raw` — conflict
- `description_raw` — choose_or_conflict
- `features_raw` — union
- `habitat_type_raw` — choose_or_conflict *(new in v6.0)*
- `access_notes_raw` — choose_or_conflict *(new in v6.0)*

### Trailthing-Specific Fields
- `source_term_raw` — choose_or_conflict *(REQUIRED; conflict if values differ significantly)*
- `source_hierarchy_context_raw` — choose_or_conflict
- `use_type_raw` — choose_or_conflict
- `surface_raw` — choose_or_conflict
- `origin_type_raw` — choose_or_conflict
- `org_type_raw` — choose_or_conflict
- `status_raw` — choose_or_conflict
- `difficulty_raw` — choose_or_conflict
- `accessibility_raw` — choose_or_conflict
- `total_length_raw` — conflict
- `parent_id_raw` — parent_resolution *(self-referential Trailthing parent)*
- `site_parent_raw` — parent_resolution
- `parent_site_network_raw` — parent_resolution
- `member_trailthing_names_raw` — union

### Site Network-Specific Fields
- `network_type_raw` — choose_or_conflict
- `org_type_raw` — choose_or_conflict
- `status_raw` — choose_or_conflict
- `member_sites_raw` — union (raw names; ID resolution in Phase 5)

### Access Point-Specific Fields
- `access_point_type_raw` — choose_or_conflict
- `status_raw` — choose_or_conflict
- `gps_lat_raw` — conflict
- `gps_lon_raw` — conflict
- `address_raw` — choose_or_conflict
- `parent_sites_raw` — parent_resolution
- `parent_trailthings_raw` — parent_resolution

### Verification Fields (all entity types)
- `last_verified_date` — choose (most recent date wins)
- `field_verified` — choose (true if any record has true)

### Metadata Blocks (all entity types)
- provenance — metadata_union
- lineage — metadata_union
- conflict metadata — metadata_union
- uncertainty metadata — metadata_union
- boundary metadata — metadata_union
- baseline metadata — metadata_union

------------------------------------------------------------
# 11.4 CONFLICT RECORDING

When a field uses **choose_or_conflict** or **conflict** and multiple distinct raw
values exist, the engine must record a conflict entry in the conflict metadata block
including: field name, all distinct raw values, source record IDs, source tiers,
and any relevant URLs or provenance.

The engine must not choose a winner, normalize values, or infer a canonical value.
Conflicts are preserved for the Normalization Engine v6.0 to resolve.

------------------------------------------------------------
# 11.5 METADATA PROPAGATION

All metadata blocks must be merged using **metadata_union**, which preserves all raw
metadata entries without normalization, reinterpretation, collapsing, or deduplication.
No metadata may be discarded. Metadata propagation must be deterministic,
order-independent, and reversible.

------------------------------------------------------------
# 11.6 MERGE PROVENANCE

Each merged field must record: which merge strategy was applied, which source records
contributed values, whether a conflict was detected, whether the field was left
unresolved, the merge cluster ID, and the thresholds used in Phase 3.

Merge provenance is stored in the **resolution_provenance** block of the Resolved Entity.

------------------------------------------------------------
# 11.7 OUTPUT OF PHASE 4

Phase 4 produces a **partially resolved entity**, containing:
- merged identity_block
- merged organizational_block
- merged raw parent_*_raw lists
- merged metadata_block
- merge provenance
- canonical tier assignment (for Trailthing clusters with cross-tier records — §11.8)

Parent IDs are not yet resolved; that occurs in Phase 5.

------------------------------------------------------------
# 11.8 CROSS-TIER TRAILTHING CANONICALIZATION

When the same named Trailthing is staged at multiple discovery tiers — for example,
by a metro park district at Tier 3 and a municipality at Tier 6 — the ordinary merge
process will produce a cluster containing records from different tiers. This section
defines how the engine assigns canonical tier status within that cluster.

### 11.8.1 Detection Criteria

A merge cluster is a **cross-tier Trailthing cluster** when all of the following are true:

- `entity_type` = Trailthing for all records in the cluster
- the cluster contains records from two or more distinct discovery tiers
- at least one record carries an `identity_notes_raw` entry containing the substring
  `"Cross-tier trail"` (as flagged by the tier sub-procedures)

### 11.8.2 Canonical Record Selection

Within a cross-tier Trailthing cluster, the engine assigns canonical status to the
record from the **primary managing entity's tier**. Determined as follows, in order:

1. **Governance field evidence** — If exactly one record in the cluster has
   `governance_raw` that unambiguously identifies it as the primary manager (e.g.,
   "Metro Parks manages and maintains [trail name]"), that record's tier is canonical.

2. **Absence of cross-tier flag** — If exactly one record in the cluster does NOT
   carry the `"Cross-tier trail"` flag in `identity_notes_raw`, that record's tier
   is canonical.

3. **Tier precedence fallback** — If the above criteria are inconclusive, the record
   with the lowest discovery tier number becomes canonical. A review set is also
   emitted (§11.8.5).

The engine must apply these criteria in order and stop at the first conclusive result.

### 11.8.3 Canonical Tier Assignment Output

The engine must record the following in `resolution_provenance`:

- `cross_tier_trailthing`: true
- `canonical_tier`: the discovery tier of the canonical record
- `canonical_record_id`: the raw discovery record ID of the canonical record
- `non_canonical_record_ids`: list of all other record IDs in the cluster
- `selection_basis`: "governance_evidence", "flag_absence", or "tier_precedence_fallback"
- `governance_raw_values`: all distinct `governance_raw` values, for audit
- `source_term_raw_values`: all distinct `source_term_raw` values, for audit

### 11.8.4 Non-Canonical Record Handling

Non-canonical records are **not discarded**. Their data must be:
- fully merged using the standard field strategies in §11.3
- preserved in `resolution_provenance` with `role: non_canonical`
- flagged so that the Normalization Engine suppresses them from TSV output and
  DB upsert

The Normalization Engine v6.0 is responsible for applying the suppression flag.
The Resolution Engine only sets it.

### 11.8.5 Review Set Emission

The engine must emit a review set for the cross-tier Trailthing cluster when:
- the tier_precedence_fallback criterion was used
- `governance_raw` values across records are contradictory
- `source_term_raw` values are contradictory (indicating possible identity ambiguity)
- the canonical selection is ambiguous for any reason

The review set must include all standard fields (§10.6) plus:
- `cross_tier_trailthing`: true
- `canonical_tier_assigned`: the tier assigned (if any)
- `reason_for_review`: a brief description of the ambiguity

### 11.8.6 Scope

This section applies to **all Trailthing entities**. Sites, Site Networks, and Access
Points are not subject to canonical tier assignment in this version. Cross-tier
duplication for non-Trailthing entity types is handled by the standard review set
mechanism (§10.6).

------------------------------------------------------------
# RESOLUTION ENGINE v6.0
Phase 5 — Parent Resolution & Resolved Record Construction
Natural Areas Project — v6.x Pipeline

------------------------------------------------------------
# 12. PHASE 5: PARENT RESOLUTION AND RESOLVED RECORD CONSTRUCTION

Phase 5 completes the resolution workflow by resolving parent relationships,
preserving lineage metadata, and assembling the final **Resolved Entity v6.x**
object. This phase does not modify raw values, does not infer missing parents, and
does not normalize or reinterpret lineage.

------------------------------------------------------------
# 12.1 PURPOSE OF PHASE 5

Phase 5 performs four essential tasks:
- **Resolve parent_*_raw names to internal IDs**, when possible.
- **Preserve lineage metadata exactly as discovered**, without correction.
- **Record parent conflicts and uncertainties** when resolution is ambiguous.
- **Assemble the final Resolved Entity v6.x**, including all merged blocks and provenance.

------------------------------------------------------------
# 12.2 INPUTS TO PHASE 5

Phase 5 receives:
- the merged entity from Phase 4
- merged `parent_*_raw` lists
- merged metadata blocks (including lineage)
- the full set of resolved entities produced so far (for ID lookup)
- entity-type rules and parent/child rules from the Resolution Rules Module v6.x

------------------------------------------------------------
# 12.3 NAME-TO-ID PARENT RESOLUTION

Parent resolution converts raw parent names into internal IDs **without altering the
raw names**.

Parent resolution rules:
- Use entity-type rules from the Rules Module to determine which parent types are valid.
- Match raw parent names using the same identity logic as primary entities (lookup mode).
- Use raw county context to disambiguate matches.
- If exactly one match is found, assign the parent ID.
- If multiple matches exist, record a parent conflict.
- If no match exists, record an unresolved parent.
- Never invent a parent ID.
- Never infer missing parents.
- Never modify lineage metadata to "fix" inconsistencies.

**Trailthing parent resolution** follows the same rules with three parent types:
- `parent_id_raw` → resolves to a Trailthing ID (self-referential)
- `site_parent_raw` → resolves to a Site ID
- `parent_site_network_raw` → resolves to a Site Network ID

**Access Point parent resolution** follows the same rules with two parent types:
- `parent_sites_raw` → resolves to Site IDs
- `parent_trailthings_raw` → resolves to Trailthing IDs

------------------------------------------------------------
# 12.4 LINEAGE PRESERVATION

Lineage metadata must be preserved exactly as discovered, never overwritten or
normalized, never reconciled with resolved parent IDs. If lineage metadata contradicts
resolved parent IDs: record a lineage conflict; do not modify either value.

------------------------------------------------------------
# 12.5 PARENT CONFLICT AND UNCERTAINTY HANDLING

Parent conflicts arise when:
- multiple possible parent matches exist
- no valid parent match exists
- lineage metadata contradicts resolved parent IDs
- parent_*_raw lists disagree across merged records

When a conflict occurs: record a conflict entry in the conflict metadata block
including raw parent names, candidate parent IDs, source record IDs, source tiers,
and lineage metadata. Do not choose a winner or infer a canonical parent.

------------------------------------------------------------
# 12.6 FINAL RESOLVED ENTITY STRUCTURE (v6.0)

Each Resolved Entity v6.x must contain the following blocks:

### 1. resolved_entity_id
A stable internal ID assigned by the engine.

### 2. entity_type
One of the four entity types: Site, Trailthing, Site Network, Access Point.

### 3. source_records
List of all raw discovery record IDs that contributed to the merged entity.

### 4. identity_block
Merged identity fields:
- name_raw
- counties_raw
- urls_raw
- location_raw (Sites, Access Points)
- source_term_raw (Trailthings — REQUIRED)
- source_hierarchy_context_raw (Trailthings)
- any entity-specific identity fields

### 5. organizational_block
Merged organizational fields:
- ownership_raw
- governance_raw
- partner_agencies_raw
- coordination_raw

### 6. parent_block
Contains:
- raw parent_*_raw lists
- resolved parent_*_id lists
- parent conflicts and uncertainties
- lineage metadata (preserved exactly)

For Trailthings specifically:
- parent_id_raw → resolved_parent_trailthing_id
- site_parent_raw → resolved_site_parent_id
- parent_site_network_raw → resolved_parent_site_network_id

For Access Points specifically:
- parent_sites_raw → resolved_parent_site_ids
- parent_trailthings_raw → resolved_parent_trailthing_ids

### 7. metadata_block
Merged metadata: provenance, lineage, conflict metadata, uncertainty metadata,
boundary metadata, baseline metadata.

### 8. resolution_provenance
A complete record of:
- merge strategies applied
- similarity thresholds used
- merge cluster membership
- conflicts detected
- parent resolution outcomes
- any hard separation conditions encountered
- canonical tier assignment (for cross-tier Trailthing clusters — §11.8.3)

### 9. entity-specific payload
Raw fields specific to the entity type.

For **Sites**: category_raw, subtype_raw, designation_raw, status_raw, gps_lat_raw,
gps_lon_raw, acres_raw, description_raw, features_raw, habitat_type_raw,
access_notes_raw, last_verified_date, field_verified.

For **Trailthings**: use_type_raw, surface_raw, origin_type_raw, org_type_raw,
status_raw, difficulty_raw, accessibility_raw, total_length_raw,
member_trailthing_names_raw, last_verified_date, field_verified.

For **Site Networks**: network_type_raw, org_type_raw, status_raw, member_sites_raw.

For **Access Points**: access_point_type_raw, status_raw, gps_lat_raw, gps_lon_raw,
address_raw, last_verified_date, field_verified.

------------------------------------------------------------
# 12.7 OUTPUT OF PHASE 5

Phase 5 produces a fully assembled **Resolved Entity v6.x**, ready for:
- Normalization Engine v6.0
- Graph upsert
- Review workflows
- Audit and provenance analysis

The resolved entity is deterministic, reversible, fully traceable, ontology-aligned,
and metadata-complete. No further resolution steps occur after Phase 5.

------------------------------------------------------------
# END OF RESOLUTION ENGINE v6.0
