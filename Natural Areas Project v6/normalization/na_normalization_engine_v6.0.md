# NATURAL AREAS PROJECT
# NORMALIZATION ENGINE v6.0
Cross-Entity Normalization Orchestrator for Resolved Entities
Natural Areas Project — v6.x Pipeline

This module supersedes Normalization Engine v5.8.

------------------------------------------------------------
# CHANGES FROM v5.8 → v6.0

- **Entity type consolidation**: Trail, Trail Segment, and Trail Network are unified
  into the single Trailthing entity type. §1.2 Scope updated from six entity types
  to four. §3 workflow Step 1 updated. §5.2–5.4 (Trails, Trail Segments, Trail
  Networks) consolidated into §5.2 (Trailthings). §5.5 Site Networks renumbered
  to §5.3; §5.6 Access Points renumbered to §5.4.

- **§4.7 County Normalization updated**: "Multi-location entities (Trails, Trail
  Segments, Trail Networks, Site Networks)" updated to "Multi-location entities
  (Trailthings, Site Networks)."

- **§4.10 Parent/Child Validation updated**: Access Point allowed parent types
  updated from Site + Trail + Trail Segment to Site + Trailthing.

- **Hold reason `unresolved_member_ids` scope updated**: In v5.x this reason
  applied to Trail Networks with unresolved member trail IDs. In v6.0 it applies
  to Site Networks with unresolved member Site IDs. Trailthing parent relationships
  use `unresolved_parent` (single parent_id reference), not `unresolved_member_ids`.

- **All v5.8 cross-entity rules carried forward unchanged**: Schema validation,
  vocabulary normalization (required vs. optional fields, partial-match specificity
  ordering), status inference (Sites only), formatting rules, GPS validation,
  Plus Code computation, GIS spatial lookup, county normalization, integrity anchor
  validation, parent/child validation, error handling, blocking gate enforcement.

------------------------------------------------------------
# 1. PURPOSE, SCOPE, AND ARCHITECTURAL ROLE

## 1.1 Purpose

The Normalization Engine v6.0 transforms **Resolved Entities v6.x** into
**Normalized Entities v6.0** ready for:

- Entity Graph Schema v6.x
- TSV Output Specifications v6.x

It is the authoritative layer for:

- Schema validation
- Vocabulary normalization
- Formatting normalization
- GPS validation and Plus Code computation
- GIS spatial lookup (township, municipality)
- Integrity anchor validation and last-line dedup checks
- Parent/child validation

The engine does **not**:

- Discover entities
- Perform fuzzy identity matching or merging
- Acquire GPS (that is the GPS Acquisition Module's responsibility)
- Apply ontology or identity rules (those live in the Resolution Engine v6.x)
- Write TSVs or upsert directly to the graph

## 1.2 Scope

Normalization Engine v6.0 governs:

- All four entity types:
  - Site
  - Trailthing
  - Site Network
  - Access Point

- All resolved entities produced by:
  - Resolution Engine v6.x (Pass 1 and Pass 2 for Access Points)
  - GPS Acquisition Module v6.x (for GPS-updated entities)

- All normalized fields required by:
  - Entity Graph Schema v6.x
  - TSV Output Specifications v6.x

## 1.3 Architectural Role

Normalization sits between:

- **Resolution Engine v6.x / GPS Acquisition Module v6.x** (inputs)
- **Entity Upsert Engine v6.x** (outputs)

Its role is to:

1. **Validate** resolved entities against schema and contracts.
2. **Normalize** vocabulary-governed fields.
3. **Normalize** formatting and list structures.
4. **Validate GPS** and compute Plus Codes.
5. **Derive township and municipality via GIS**.
6. **Validate integrity anchors and parent/child relationships**.
7. **Produce normalized entities** with full normalization provenance.

**The Normalization Engine is a mandatory blocking gate.** No TSV Output (Stage 4)
or Database Upsert (Stage 6) may proceed until every entity in the current run has
been assigned a normalization outcome: `normalized`, `rejected`, or `held`. All
rejections — including vocabulary failures for required fields — must be surfaced
and logged before any downstream stage begins. A pipeline run halts at the
normalization gate if any entity is rejected.

Normalization is deterministic and must not infer identity or modify raw resolution
decisions.

### Pre- and Intra-Normalization Hold Conditions

Two hold conditions interact with this stage that are not part of normalization
logic itself:

**Stage 2c GPS Gate — pre-normalization filter:** Before this engine runs, the GPS
Gate has already diverted any Site or Access Point that lacks GPS coordinates and
does not carry `gps_unresolvable=true` to `held_entities` with
`hold_reason = gps_missing`. Those entities are **not present in this engine's
input set**. If a GPS-missing Site or AP arrives here without that flag, treat it
as a pipeline error, not a normalization decision.

**IMP-086 Held-Entity Child Rule — intra-normalization hold:** After the GPS Gate
held list is finalized at the start of this stage, the engine scans all child
entities (Access Points, child Sites) for parent references pointing to a held
entity. Any such child is itself moved to `held_entities` with
`hold_reason = parent_held` before normalization of the remaining entities proceeds.
This is the only hold the Normalization Engine writes directly; all other holds
(`unresolved_parent`, `unresolved_member_ids`) are deferred to the Upsert Engine.

**Canonical HELD_* Vocabulary (IMP-113):** The `held_entities.hold_reason` column
accepts only the following values. Using freeform strings produces unreliable audit
queries across county runs.

| `hold_reason` value | Triggering stage | Resolved by |
|---|---|---|
| `gps_missing` | Stage 2c GPS Gate (Sites); Stage 2d (APs) | GPS Acquisition re-run or `gps_unresolvable=true` flag set |
| `parent_held` | Normalization Engine §1 (this stage) | Parent entity released from held status |
| `unresolved_parent` | Upsert Engine — parent ID not found in DB | Partner county pipeline run; manual resolution |
| `unresolved_member_ids` | Upsert Engine — Site Network member Site IDs not in DB | Member Sites upserted in partner county run |
| `cross_county_candidate` | Resolution Engine Phase 0 | Cross-county resolution pass assigns MC ID |
| `cross_county_held` | Cross-county resolution — Scenario A provisional hold | Partner county pipeline run completes |

Held entities are excluded from TSV output by definition. They appear only in the
`held_entities` table, never in any entity TSV file. The Stage 4 TSV writer must
verify that no held entity ID appears in any entity TSV column.

------------------------------------------------------------
# 2. INPUTS, OUTPUTS, AND DEPENDENCIES

## 2.1 Inputs

Normalization Engine v6.0 consumes:

- **Resolved Entities v6.x** from Resolution Engine v6.x:
  - Including merged identity_block, organizational_block, parent_block,
    metadata_block, and resolution_provenance.

- **GPS-updated entities** from GPS Acquisition Module v6.x:
  - Entities with `gps_lat_raw` / `gps_lon_raw` and GPS provenance.
  - Note: The input set has already been filtered by the Stage 2c GPS Gate.
    Sites and Access Points without GPS and without `gps_unresolvable=true`
    are absent — they were routed to `held_entities` before this module ran.

- **Schema Modules v6.x** (4):
  - One per entity type, defining normalized field sets and types.

- **Vocabulary Modules v6.x** (4):
  - Controlled vocabularies for categories, statuses, Trailthing use types,
    surface types, etc.

- **Normalization Contracts v6.x** (4):
  - Per-entity normalization rules (required fields, integrity anchors).
  - Each contract designates vocabulary-governed fields as **required** or
    **optional**.

- **GIS Spatial Data**:
  - Authoritative township and municipal boundaries.

- **Entity Graph Schema v6.x**:
  - For ID validation and parent/child validation.

## 2.2 Outputs

Normalization Engine v6.0 produces:

- **Normalized Entity Objects v6.0**:
  - One per resolved entity, ready for upsert.

- **Normalization Provenance Records**:
  - Field-level normalization actions, vocabulary mappings, GPS/GIS results,
    errors, warnings, holds.
  - Includes `status_inferred` and `inference_basis` when §4.2a applies.

- **Validation Results**:
  - Warnings, errors, and hold statuses.

These outputs are consumed by:

- Entity Upsert Engine v6.x
- Audit & Logging
- Review and QA workflows

## 2.3 Dependencies and Boundaries

Normalization depends on:

- Resolution Engine v6.x for identity and merging.
- GPS Acquisition Module v6.x for GPS collection and provenance.
- Resolution Engine v6.x indirectly via contracts and schema.

Normalization must not:

- Re-implement identity logic.
- Override resolution decisions.
- Modify resolution metadata (except to append normalization provenance).

------------------------------------------------------------
# 3. CROSS-ENTITY NORMALIZATION WORKFLOW

For each Resolved Entity:

1. **Determine entity_type**
   - Site, Trailthing, Site Network, Access Point.

2. **Route to the appropriate Normalization Contract v6.x**
   - Each contract defines required fields, integrity anchors, and per-field rules.
   - Each contract designates which vocabulary-governed fields are required vs optional.

3. **Apply cross-entity normalization steps**:
   - Schema validation
   - Vocabulary normalization (required fields block; optional fields warn)
   - Status inference (Sites with blank status_raw, per §4.2a)
   - Formatting normalization
   - GPS validation and numeric conversion
   - Plus Code computation
   - GIS spatial lookup (township, municipality)
   - Integrity anchor validation and dedup check
   - Parent/child validation

4. **Construct the normalized entity object**:
   - Populate normalized fields according to schema.
   - Attach normalization provenance.

5. **Classify outcome**:
   - Normalized (ready for upsert)
   - Rejected (fatal errors — entity must not proceed)
   - Held (valid but incomplete; dependencies unresolved)

6. **Emit outputs**:
   - Normalized entity
   - Provenance
   - Validation status

7. **Enforce blocking gate**:
   - After all entities in the run are classified, halt pipeline if any are Rejected.
   - Surface all rejections before halting.

The workflow is deterministic and must produce identical outputs for identical inputs.

------------------------------------------------------------
# 4. CROSS-ENTITY RULES

These rules apply to all four entity types unless explicitly overridden in a
per-entity contract.

## 4.1 Schema Validation

- All required fields defined in Schema Modules v6.x must be present.
- Field types must match schema (e.g., numeric, string, boolean, list).
- Unknown fields must be ignored or logged as warnings.
- Deprecated fields from v5.x (Trail, Trail Segment, Trail Network fields) must
  be dropped if present in resolved entities.

Entities failing required-field checks must be rejected or held according to
per-entity contracts.

## 4.2 Vocabulary Normalization

All vocabulary-governed fields must map to controlled values from the appropriate
Vocabulary Module v6.x. Raw values must be preserved in normalization provenance
when mapping is lossy or non-obvious. Vocabulary normalization must be deterministic
and case-insensitive where appropriate.

Vocabulary-governed fields are classified as **required** or **optional** in each
entity's Normalization Contract v6.x.

**Required vocabulary-governed fields — unmappable values:**

- Must be treated as **Fatal Errors** (see §4.11).
- The entity is **rejected** and must not proceed to TSV Output or Database Upsert.
- Must be logged before the pipeline halts.
- Must not be silently coerced or left blank without rejection.

**Optional vocabulary-governed fields — unmappable values:**

- Must be logged as warnings.
- Must not be silently coerced.
- Resulting normalized field is left blank if no valid mapping exists.

If any entity in a run is rejected for a required-field vocabulary failure, the
pipeline halts after all entities are classified and surfaces all rejections before
any downstream stage proceeds.

## 4.2a Status Inference Rule (Sites Only)

Status inference is an **explicitly permitted exception** to the normalization rule
against inventing data. It applies only when `status_raw` is blank or absent for
Site entities — meaning the discovery source did not state a status value, not that
the value was present but unmappable.

**This rule applies when all of the following are true:**

- `entity_type == "Site"`
- `status_raw` is blank or absent (field not captured at discovery)
- At least one of the following authoritative indicators is present:
  - `url_primary_raw` is a non-blank URL to a current (non-historical) authoritative source
  - `gps_lat_raw` and `gps_lon_raw` are both present from an authoritative GPS acquisition source
  - Discovery metadata records an active listing in a current authoritative source

**When all conditions are met:**

- Normalize `status = "Active"`.
- Record in normalization provenance: `"status_inferred": true, "inference_basis": "<which indicator applied>"`.

**When conditions are not met:**

- Leave `status` blank.
- Log: "status_raw absent; inference conditions not met."

**This rule does not apply when:**

- `status_raw` is present but unmappable — treat as a vocabulary error per §4.2.
- The entity type is not Site.
- The entity carries a flag indicating historical closure, demolition, or transfer.

## 4.2b Vocabulary Partial-Match Specificity Ordering (IMP-026)

When a vocabulary map uses partial string matching to map a raw value to a
controlled term, candidate map keys must be evaluated in **descending length
order** — longest keys first, shortest keys last.

**Required matching algorithm:**

1. Collect all candidate keys from the vocabulary map.
2. Sort candidate keys by character length, **descending** (longest first).
3. Iterate through the sorted keys. Return the controlled value for the **first**
   key that matches (exact match or substring match, per the map's matching mode).
4. If no key matches, follow §4.2 required vs. optional field handling.

**Implementation note**: This sort must be applied at the time of each lookup,
not assumed from vocabulary map insertion order.

## 4.3 Formatting Rules

- **Semicolon-delimited lists** (e.g., counties, features, alternate names):
  - Trim leading/trailing spaces around each value.
  - Remove empty segments.
  - Alphabetize where required (e.g., counties).

- **Blank fields**:
  - Must be true blanks (no "N/A", "Unknown", or placeholders).

- **Text fields**:
  - Strip leading/trailing whitespace.
  - Normalize line endings.
  - Do not alter case unless vocabulary mapping requires it.

Formatting normalization must not change semantic content.

## 4.4 GPS Validation and Numeric Conversion

**Inputs:** `gps_lat_raw`, `gps_lon_raw` from Resolution / GPS Acquisition.

**Outputs:** Numeric `gps_lat`, `gps_lon` fields in normalized entities.

**Rules:**

- If both `gps_lat_raw` and `gps_lon_raw` are present:
  - Parse as numeric.
  - Validate ranges: `gps_lat` in [-90, 90]; `gps_lon` in [-180, 180].
  - Round to 6 decimal places.
  - On success: set `gps_lat`, `gps_lon`; record in provenance.
  - On failure: log error; leave `gps_lat` / `gps_lon` blank.

- If GPS is missing: leave `gps_lat` / `gps_lon` blank.

Normalization must not attempt to acquire GPS; it only validates and converts.

## 4.5 Plus Code Computation

- Compute only if both `gps_lat` and `gps_lon` are present and valid.
- Use a deterministic Open Location Code implementation.
- Use full 10-character code precision.
- If computation fails: log warning; leave `plus_code` blank.

Normalization must not approximate or infer Plus Codes without valid GPS.

## 4.6 GIS Spatial Lookup — Township and Municipality

**Inputs:** Valid `gps_lat`, `gps_lon`; authoritative GIS boundaries.

**Outputs:** `township` (civil township name); `municipality` (city or village name).

**Rules:**

- Only perform GIS lookup if `gps_lat` and `gps_lon` are present and valid.
- Perform point-in-polygon spatial joins against civil township and municipal boundaries.
- Assign `township` = matched township name (without appending "Township").
- Assign `municipality` = matched municipality name or blank if none.
- If GPS is blank or invalid: leave `township` and `municipality` blank.
- Multi-location entities (Trailthings, Site Networks): do not derive
  township/municipality; leave blank. Use `counties` for geographic context.

GIS lookup is the authoritative source for township and municipality.

## 4.7 County Normalization

- Normalized `counties` field must:
  - Be semicolon-delimited.
  - Be alphabetized.
  - Strip the word "County" from each value.
  - Reflect the resolved county set from Resolution v6.x.

- Single-location entities (Sites, Access Points):
  - Must have exactly one county value.

- Multi-location entities (Trailthings, Site Networks):
  - May have multiple counties.

No entity may be duplicated per county in the normalized output.

## 4.9 Integrity Anchor Validation and Dedup Check

Normalization performs a **last-line-of-defense** deduplication check using
**normalized integrity anchors** defined in per-entity contracts.

**Process:**

1. Compute the integrity anchor for the normalized entity (per entity-type rules).
2. Compare against other entities normalized in the current run and existing entities
   in the Entity Graph.
3. If no match: proceed to upsert.
4. If a match:
   - If either entity carries resolution conflicts → route to Manual Review Queue
     with full diff.
   - If neither carries conflicts → log as a Resolution miss; route both to
     Manual Review Queue.
   - If the match is with an existing graph entity → treat as an update candidate
     per Upsert Engine rules.

Normalization must not merge entities; it only detects collisions and routes them.

## 4.10 Parent/Child Validation

- **Site parent/child**:
  - Parent Site relationships must respect Child Site Rules v6.x.
  - No cycles or self-parenting.
  - Parent Site must exist or be resolvable in the Entity Graph.

- **Access Point parents**:
  - Allowed parent types: Site, Trailthing.
  - Parent IDs must reference valid entities.
  - Site Networks are not valid AP parents.

- **Trailthing parents**:
  - A Trailthing may reference another Trailthing as `parent_id` (self-referential
    hierarchy within entity type).
  - A Trailthing may reference a Site as `site_parent_id`.
  - Parent IDs must reference valid entities in the Entity Graph.
  - No cycles.

Invalid parent relationships must result in errors or holds according to
per-entity contracts.

## 4.11 Error Handling and Classification

- **Warnings**:
  - Unmappable vocabulary values for **optional** vocabulary-governed fields.
  - Minor formatting issues.
  - Plus Code computation failures.
  - GIS lookup failures with valid GPS.
  - Member IDs referencing entities not yet in graph.

- **Fatal Errors (Rejections)**:
  - Missing required fields.
  - Invalid field types that cannot be coerced.
  - Broken integrity anchors.
  - Invalid parent references (cycles, self-parenting).
  - GPS values out of valid range (when required).
  - Unmappable vocabulary values for **required** vocabulary-governed fields.

- **Held Entities**:
  - Access Points missing GPS (policy requires GPS before upsert).
  - Site Networks with unresolved member Site IDs (prefer hold over reject).

All outcomes must be recorded in normalization provenance.

**Blocking gate enforcement**: After all entities in a run are classified, if any
entity is Rejected, the pipeline must halt. All rejections must be surfaced to the
operator and logged in the Audit & Logging Module v6.x before any downstream stage
begins.

------------------------------------------------------------
# 5. PER-ENTITY NORMALIZATION ROUTING

Each entity type has a dedicated Normalization Contract v6.x that refines
cross-entity rules.

## 5.1 Sites

Key normalizations:

- Category, subtype, designation, status (vocabulary).
- Governance, ownership, partner agencies, coordination (text normalization).
- Counties (normalized per §4.7).
- Parent Site (validate against Entity Graph).
- **Habitat Type** — open vocabulary free-text; pass through with whitespace cleanup;
  no vocabulary mapping. See Site Normalization Contract v6.0.
- **Access Notes** — free-text; pass through with whitespace cleanup. See Site
  Normalization Contract v6.0.
- **Last Verified Date** — validate DATE format (YYYY-MM-DD); see Site Normalization
  Contract v6.0.
- **Field Verified** — validate boolean; always false at discovery; see Site
  Normalization Contract v6.0.
- **Features** — apply four-step normalization sequence per Site Normalization
  Contract v6.0 §5.18.
- **Description** — apply redundancy stripping per Site Normalization Contract
  v6.0 §5.10 (IMP-052).
- **Notes** — apply pipeline metadata stripping per Site Normalization Contract
  v6.0 §5.19 (IMP-053); apply provenance prohibition (IMP-014).
- GPS validation → `gps_lat`, `gps_lon`.
- Plus Code computation.
- GIS derivation → `township`, `municipality`.
- Status inference per §4.2a if `status_raw` is blank.

## 5.2 Trailthings

Key normalizations:

- Use type, surface type, origin type (vocabulary — optional; IMP-021).
- Status (vocabulary — optional).
- Difficulty (vocabulary — optional; only if explicitly stated by authoritative source).
- Accessibility (free-text).
- Governance, ownership, partner agencies, coordination (text normalization).
- Counties (normalized per §4.7).
- Length (numeric validation).
- Source term, source hierarchy context (pass through verbatim — no vocabulary mapping).
- Parent Trailthing (validate against Entity Graph; hold if unresolvable).
- Parent Site (validate against Entity Graph).
- Member Trailthing names (resolve to IDs against Entity Graph; log unresolvable).
- Description (ecological/physical character priority per IMP-015).
- Notes (provenance prohibition per IMP-014).
- **No GPS, Plus Code, township, or municipality** (multi-location entities).

See Trailthing Normalization Contract v6.0 for full field-by-field rules.

## 5.3 Site Networks

Key normalizations:

- Network type, org type, status (vocabulary).
- Ownership, governance, partner agencies, coordination (text normalization).
- **Coordination** — free-text; pass through with whitespace cleanup; see Site
  Network Normalization Contract v6.0.
- Counties (normalized per §4.7).
- Member Site IDs (validate against Entity Graph; hold if unresolvable).
- Member count (derived from validated IDs).
- Description (character and mission priority per IMP-015).
- Notes (provenance prohibition per IMP-014).
- **No GPS, Plus Code, township, or municipality** (multi-location entities).

## 5.4 Access Points

Key normalizations:

- Access point type, status (vocabulary).
- Features (semicolon-delimited; vocabulary-governed).
- County (single normalized value per §4.7).
- Address / location description (text clean).
- **Last Verified Date** — validate DATE format (YYYY-MM-DD).
- **Field Verified** — validate boolean; always false at discovery.
- GPS validation → `gps_lat`, `gps_lon` (required by policy).
- Plus Code computation.
- GIS derivation → `township`, `municipality`.
- Parent relationships — allowed types: Site, Trailthing (validate against
  Entity Graph).
- Notes (provenance prohibition per IMP-014).

Access Points with missing or invalid GPS are held rather than rejected.

------------------------------------------------------------
# 6. NORMALIZED ENTITY CONSTRUCTION, PROVENANCE, AND VERSIONING

## 6.1 Normalized Entity Structure

Each Normalized Entity must conform to:

- **Entity Graph Schema v6.x**
- The corresponding **Schema Module v6.x**

Typical blocks include:

- `normalized_entity_id` (internal ID or derived from resolved_entity_id).
- `entity_type`.
- Normalized identity fields (name, counties, labels).
- Normalized organizational fields (ownership, governance, partner agencies,
  coordination).
- Normalized GPS and spatial fields (`gps_lat`, `gps_lon`, `plus_code`,
  `township`, `municipality`).
- Normalized parent/child fields (parent IDs, member IDs).
- Entity-specific payload fields (lengths, types, statuses, features, etc.).
- Normalization provenance block.

## 6.2 Normalization Provenance

For each entity, Normalization must record:

- Normalization run ID.
- Fields modified and how (vocabulary mapping, formatting changes).
- GPS validation results (success/failure/blank).
- Plus Code computation result.
- GIS lookup result (township/municipality derived or blank).
- Integrity anchor status and any collisions detected.
- Parent/child validation results.
- Errors, warnings, and hold reasons.
- Status inference result (`status_inferred`, `inference_basis`) if §4.2a applied.
- Vocabulary failure details for any rejected entity (field name, raw value, reason).
- Unmapped token log entries (for vocabulary expansion candidates at Stage 5).

Provenance must be:

- Append-only (does not overwrite resolution provenance).
- Fully auditable.
- Available to review and QA tools.

## 6.3 Integration Points

Normalization Engine v6.0 integrates with:

- **Resolution Engine v6.x** (input).
- **GPS Acquisition Module v6.x** (input for GPS-updated entities).
- **Schema Modules v6.x** (validation).
- **Vocabulary Modules v6.x** (controlled values).
- **Normalization Contracts v6.x** (per-entity rules).
- **Entity Graph Schema v6.x** (output shape and ID validation).
- **Entity Upsert Engine v6.x** (consumer).
- **GIS Spatial Data** (township and municipality derivation).
- **Audit & Logging Module v6.x** (provenance).

## 6.4 Versioning

- This module is **Normalization Engine v6.0**.
- Any change to cross-entity normalization rules (schema, vocabulary, GPS/GIS,
  integrity anchors, parent/child validation, blocking gate behavior) requires
  a new minor version.
- Per-entity changes that do not affect cross-entity rules are versioned within
  the individual Normalization Contracts v6.x.

------------------------------------------------------------
# END OF NORMALIZATION ENGINE v6.0
