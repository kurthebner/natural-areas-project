# NORMALIZATION ENGINE v5.8
Cross‑Entity Normalization Orchestrator for Resolved Entities
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# CHANGES FROM v5.7 → v5.8

- **IMP-053 — Notes pipeline metadata detection and stripping**: Added notes metadata
  detection as a required step in §5.1 Sites entity-specific normalization. Before
  writing `notes_raw` to the normalized `notes` field, the Normalization Engine must
  apply pipeline metadata stripping per the Site Normalization Contract v5.5 §5.19
  stripping pattern list. This prevents tier markers, session references, IMP
  cross-references, OBJECTID annotations, GPS pending notes, and discovery run labels
  from persisting in the public-facing `notes` field. Stripped content is not logged
  as an error; the strip is silent and automatic.

- **IMP-049/050/051 — Features normalization sequence formalized**: §5.1 Sites now
  references the explicit four-step features normalization sequence defined in
  Site Normalization Contract v5.5 §5.18. The engine must apply activity detection,
  operational content stripping, named entity detection, and vocabulary mapping in
  that order before writing to `features`.

- **IMP-052 — Description redundancy stripping**: §5.1 Sites now references the
  description redundancy detection and stripping logic in Site Normalization Contract
  v5.5 §5.10. The engine applies the opener strip pass to `description_raw` before
  writing to `description`. Blank output from this pass is not an error condition.

------------------------------------------------------------
# CHANGES FROM v5.6 → v5.7

- **IMP-026 — Vocabulary partial-match specificity ordering**: Added §4.2b documenting
  the required sort order for partial string matching against vocabulary map keys.
  Candidate keys must be sorted by length descending (longest/most specific first)
  before matching. This prevents shorter generic keys (e.g., "park") from shadowing
  longer specific keys (e.g., "state nature preserve") when the raw value contains both
  as substrings. Fix was already applied in the pipeline implementation; this section
  brings the specification into alignment.

------------------------------------------------------------
# CHANGES FROM v5.5 → v5.6

- **IMP-029**: Normalization Engine designated as a mandatory blocking gate —
  no TSV Output or Database Upsert may proceed until all entities have reached
  a normalization outcome. See §1.3 Architectural Role.
- **IMP-029**: §4.2 Vocabulary Normalization restructured to distinguish required
  vs optional vocabulary-governed fields. Unmappable values for required fields
  are now Fatal Errors (rejections), not Warnings. Optional fields retain Warning
  behavior. Per-entity Normalization Contracts v5.x define which fields are required.
- **IMP-029**: New §4.2a Status Inference Rule — for Site entities with blank
  `status_raw`, normalization may infer `status = "Active"` when at least one
  authoritative indicator is present. Inference must be recorded in normalization
  provenance. This is an explicitly permitted exception to the no-invention rule.
- **IMP-029**: §4.11 Error Handling updated — "Unmappable vocabulary values" split:
  required fields → Fatal Errors (Rejections); optional fields → Warnings.

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- Updated module version to v5.5.
- Removed Derived Label computation from Sections 5.2 (Trails), 5.3 (Trail Segments),
  5.4 (Trail Networks), and 5.5 (Site Networks). Derived Label was removed from all
  four entity types in their v5.1 schemas and TSV output specs as a presentation-layer
  concern. Section 4.7 (cross-entity Derived Label rule) has now also been removed
  since Derived Labels have been eliminated from Sites and Access Points as well.
- Corrected "Maps (rich array)" references in Sections 5.2 and 5.3 to reflect that
  maps was simplified to a plain semicolon-delimited URL list at all stages in v5.1.

------------------------------------------------------------
# 1. PURPOSE, SCOPE, AND ARCHITECTURAL ROLE

## 1.1 Purpose

The Normalization Engine v5.8 transforms **Resolved Entities v5.x** into **Normalized Entities v5.8** ready for:

- Entity Graph Schema v5.x
- TSV Output Specifications v5.x

It is the authoritative layer for:

- Schema validation
- Vocabulary normalization
- Formatting normalization
- GPS validation and Plus Code computation
- GIS spatial lookup (township, municipality)
- Integrity anchor validation and last‑line dedup checks
- Parent/child validation

The engine does **not**:

- Discover entities
- Perform fuzzy identity matching or merging
- Acquire GPS (that is the GPS Acquisition Module's responsibility)
- Apply ontology or identity rules (those live in the Resolution Rules Module v5.x)
- Write TSVs or upsert directly to the graph

## 1.2 Scope

Normalization Engine v5.8 governs:

- All six entity types:
  - Site
  - Trail
  - Trail Segment
  - Trail Network
  - Site Network
  - Access Point

- All resolved entities produced by:
  - Resolution Engine v5.x (Pass 1 and Pass 2 for Access Points)
  - GPS Acquisition Module v5.x (for GPS‑updated entities)

- All normalized fields required by:
  - Entity Graph Schema v5.x
  - TSV Output Specifications v5.x

## 1.3 Architectural Role

Normalization sits between:

- **Resolution Engine v5.x / GPS Acquisition Module v5.x** (inputs)
- **Entity Upsert Engine v5.x** (outputs)

Its role is to:

1. **Validate** resolved entities against schema and contracts.
2. **Normalize** vocabulary‑governed fields.
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

Normalization is deterministic and must not infer identity or modify raw resolution decisions.

### Pre- and Intra-Normalization Hold Conditions

Two hold conditions interact with this stage that are not part of normalization logic itself:

**Stage 2c GPS Gate (IMP-069) — pre-normalization filter:** Before this engine runs, the GPS Gate
has already diverted any Site or Access Point that lacks GPS coordinates and does not carry
`gps_unresolvable=true` to `held_entities` with `hold_reason = gps_missing`. Those entities are
**not present in this engine's input set**. If a GPS-missing Site or AP arrives here without that
flag, treat it as a pipeline error, not a normalization decision.

**IMP-086 Held-Entity Child Rule — intra-normalization hold:** After the GPS Gate held list is
finalized at the start of this stage, the engine scans all child entities (Access Points, child
Sites) for parent references pointing to a held entity. Any such child is itself moved to
`held_entities` with `hold_reason = parent_held` before normalization of the remaining entities
proceeds. This is the only hold the Normalization Engine writes directly; all other holds
(`unresolved_parent`, `unresolved_member_ids`) are deferred to the Upsert Engine.

**Canonical HELD_* Vocabulary (IMP-113):** The `held_entities.hold_reason` column accepts only
the following values. Using freeform strings produces unreliable audit queries across county runs.

| `hold_reason` value | Triggering stage | Resolved by |
|---|---|---|
| `gps_missing` | Stage 2c GPS Gate (Sites); Stage 2d (APs) | GPS Acquisition re-run or `gps_unresolvable=true` flag set |
| `parent_held` | Normalization Engine §1 (this stage) | Parent entity released from held status |
| `unresolved_parent` | Upsert Engine — parent ID not found in DB | Partner county pipeline run; manual resolution |
| `unresolved_member_ids` | Upsert Engine — Trail Network member trail IDs not in DB | Member trails upserted in partner county run |
| `cross_county_candidate` | Resolution Engine Phase 0 | Cross-county resolution pass assigns MC ID |
| `cross_county_held` | Cross-county resolution — Scenario A provisional hold | Partner county pipeline run completes |

Held entities are excluded from TSV output by definition. They appear only in the `held_entities`
table, never in any entity TSV file. The Stage 4 TSV writer must verify that no held entity ID
appears in any entity TSV column.

------------------------------------------------------------
# 2. INPUTS, OUTPUTS, AND DEPENDENCIES

## 2.1 Inputs

Normalization Engine v5.8 consumes:

- **Resolved Entities v5.x** from Resolution Engine v5.x:
  - Including merged identity_block, organizational_block, parent_block, metadata_block, and resolution_provenance.

- **GPS‑updated entities** from GPS Acquisition Module v5.x:
  - Entities with `gps_lat_raw` / `gps_lon_raw` and GPS provenance.
  - **Note (IMP-069):** The input set has already been filtered by the Stage 2c GPS Gate.
    Sites and Access Points without GPS and without `gps_unresolvable=true` are absent —
    they were routed to `held_entities` before this module was invoked.

- **Schema Modules v5.x** (6):
  - One per entity type, defining normalized field sets and types.

- **Vocabulary Modules v5.x** (6):
  - Controlled vocabularies for categories, statuses, trail use types, surface types, etc.

- **Normalization Contracts v5.x** (6):
  - Per‑entity normalization rules (required fields, integrity anchors).
  - Each contract designates vocabulary-governed fields as **required** or **optional**.

- **GIS Spatial Data**:
  - Authoritative township and municipal boundaries.

- **Entity Graph Schema v5.x**:
  - For ID validation and parent/child validation.

## 2.2 Outputs

Normalization Engine v5.8 produces:

- **Normalized Entity Objects v5.8**:
  - One per resolved entity, ready for upsert.

- **Normalization Provenance Records**:
  - Field‑level normalization actions, vocabulary mappings, GPS/GIS results, errors, warnings, holds.
  - Includes `status_inferred` and `inference_basis` when §4.2a applies.

- **Validation Results**:
  - Warnings, errors, and hold statuses.

These outputs are consumed by:

- Entity Upsert Engine v5.x
- Audit & Logging
- Review and QA workflows

## 2.3 Dependencies and Boundaries

Normalization depends on:

- Resolution Engine v5.x for identity and merging.
- GPS Acquisition Module v5.x for GPS collection and provenance.
- Resolution Rules Module v5.x indirectly via contracts and schema.

Normalization must not:

- Re‑implement identity logic.
- Override resolution decisions.
- Modify resolution metadata (except to append normalization provenance).

------------------------------------------------------------
# 3. CROSS‑ENTITY NORMALIZATION WORKFLOW

For each Resolved Entity:

1. **Determine entity_type**
   - Site, Trail, Trail Segment, Trail Network, Site Network, Access Point.

2. **Route to the appropriate Normalization Contract v5.x**
   - Each contract defines required fields, integrity anchors, and per‑field rules.
   - Each contract designates which vocabulary-governed fields are required vs optional.

3. **Apply cross‑entity normalization steps**:
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
# 4. CROSS‑ENTITY RULES

These rules apply to all six entity types unless explicitly overridden in a per‑entity contract.

## 4.1 Schema Validation

- All required fields defined in Schema Modules v5.x must be present.
- Field types must match schema (e.g., numeric, string, boolean, list).
- Unknown fields must be ignored or logged as warnings.
- Deprecated fields from earlier versions (e.g., `access_level`, `role`, `network_affiliation`, `source_primary`, `source_all`, `geometry` in normalized schema) must be dropped if present in resolved entities.

Entities failing required‑field checks must be rejected or held according to per‑entity contracts.

## 4.2 Vocabulary Normalization

All vocabulary‑governed fields must map to controlled values from the appropriate Vocabulary Module v5.x. Raw values must be preserved in normalization provenance when mapping is lossy or non‑obvious. Vocabulary normalization must be deterministic and case‑insensitive where appropriate.

Vocabulary-governed fields are classified as **required** or **optional** in each entity's Normalization Contract v5.x.

**Required vocabulary-governed fields — unmappable values:**

- Must be treated as **Fatal Errors** (see §4.11).
- The entity is **rejected** and must not proceed to TSV Output or Database Upsert.
- Must be logged before the pipeline halts.
- Must not be silently coerced or left blank without rejection.

**Optional vocabulary-governed fields — unmappable values:**

- Must be logged as warnings.
- Must not be silently coerced.
- Resulting normalized field is left blank if no valid mapping exists.

If any entity in a run is rejected for a required-field vocabulary failure, the pipeline halts after all entities are classified and surfaces all rejections before any downstream stage proceeds.

## 4.2a Status Inference Rule (Sites Only)

Status inference is an **explicitly permitted exception** to the normalization rule against inventing data. It applies only when `status_raw` is blank or absent for Site entities — meaning the discovery source did not state a status value, not that the value was present but unmappable.

**This rule applies when all of the following are true:**

- `entity_type == "Site"`
- `status_raw` is blank or absent (field not captured at discovery)
- At least one of the following authoritative indicators is present:
  - `url_primary_raw` is a non-blank URL to a current (non-historical) authoritative source
  - `gps_lat_raw` and `gps_lon_raw` are both present from an authoritative GPS acquisition source
  - Discovery metadata records an active listing in a current authoritative source (non-historical tier)

**When all conditions are met:**

- Normalize `status = "Active"`.
- Record in normalization provenance: `"status_inferred": true, "inference_basis": "<which indicator applied>"`.

**When conditions are not met:**

- Leave `status` blank.
- Log: "status_raw absent; inference conditions not met."

**This rule does not apply when:**

- `status_raw` is present but unmappable — treat as a vocabulary error per §4.2 (required field handling).
- The entity type is not Site.
- The entity carries a flag indicating historical closure, demolition, or transfer.

This rule exists because a blank `status_raw` typically reflects a discovery gap, not genuine status ambiguity. A currently operating park's source page rarely states "Status: Active" explicitly. Inference is preferable to leaving required status fields systematically blank for demonstrably active entities.

## 4.2b Vocabulary Partial-Match Specificity Ordering (IMP-026)

When a vocabulary map uses partial string matching (substring containment) to map a raw value to a controlled term, candidate map keys must be evaluated in **descending length order** — longest keys first, shortest keys last.

**Why this is required**: A raw value such as "State Nature Preserve" contains the substring "park" if the map has a "park" → "Park" entry and a "state nature preserve" → "State Nature Preserve" entry. Evaluating in insertion order or arbitrary order risks matching the shorter, more generic key first and producing an incorrect result ("Park" instead of "State Nature Preserve").

**Required matching algorithm:**

1. Collect all candidate keys from the vocabulary map.
2. Sort candidate keys by character length, **descending** (longest first).
3. Iterate through the sorted keys. Return the controlled value for the **first** key that matches (exact match or substring match, per the map's matching mode).
4. If no key matches, follow §4.2 required vs. optional field handling.

**Implementation note**: This sort must be applied at the time of each lookup, not assumed from vocabulary map insertion order. Vocabulary maps are maintained by human editors and insertion order must not be relied upon for correctness.

**Example**:

| Vocabulary map keys (excerpt) | Raw value | Wrong result (insertion order) | Correct result (length-desc order) |
|---|---|---|---|
| "park", "state nature preserve" | "State Nature Preserve" | Park | State Nature Preserve |
| "park", "state park" | "State Park" | Park | State Park |
| "trail", "trail network" | "Trail Network" | Trail | Trail Network |

## 4.3 Formatting Rules

- **Semicolon‑delimited lists** (e.g., counties, features, alternate names):
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

**Inputs:**
- `gps_lat_raw`, `gps_lon_raw` from Resolution / GPS Acquisition.

**Outputs:**
- Numeric `gps_lat`, `gps_lon` fields in normalized entities.

**Rules:**

- If both `gps_lat_raw` and `gps_lon_raw` are present:
  - Parse as numeric.
  - Validate ranges:
    - `gps_lat` in [-90, 90]
    - `gps_lon` in [-180, 180]
  - Round to a consistent precision (e.g., 6 decimal places).
  - On success:
    - Set `gps_lat`, `gps_lon`.
    - Record success in normalization provenance.
  - On failure:
    - Log error.
    - Leave `gps_lat` / `gps_lon` blank.

- If GPS is missing:
  - Leave `gps_lat` / `gps_lon` blank.
  - For Access Points, apply per‑entity rules (often "hold if missing GPS").

Normalization must not attempt to acquire GPS; it only validates and converts.

## 4.5 Plus Code Computation

**Inputs:**
- Valid `gps_lat`, `gps_lon`.

**Outputs:**
- `plus_code` string.

**Rules:**

- Compute Plus Code only if both `gps_lat` and `gps_lon` are present and valid.
- Use a deterministic Open Location Code implementation.
- Use a consistent precision (e.g., full 10‑character code).
- If computation fails:
  - Log warning.
  - Leave `plus_code` blank.

Normalization must not approximate or infer Plus Codes without valid GPS.

## 4.6 GIS Spatial Lookup — Township and Municipality

**Inputs:**
- Valid `gps_lat`, `gps_lon`.
- Authoritative GIS boundaries for townships and municipalities.

**Outputs:**
- `township` (civil township name).
- `municipality` (city or village name, if applicable).

**Rules:**

- Only perform GIS lookup if `gps_lat` and `gps_lon` are present and valid.
- Perform point‑in‑polygon spatial joins against:
  - Civil township boundaries.
  - Municipal boundaries (cities and villages).
- Assign:
  - `township` = matched township name (without appending "Township").
  - `municipality` = matched municipality name or blank if none.
- If GPS is blank or invalid:
  - Leave `township` and `municipality` blank.
- Multi‑location entities (Trails, Trail Networks, Site Networks):
  - Do not derive township/municipality; leave blank.
  - Use `counties` for geographic context.

GIS lookup is the authoritative source for township and municipality; any discovery‑time values are ignored or treated as informational only.

## 4.7 County Normalization

- Normalized `counties` field must:
  - Be semicolon‑delimited.
  - Be alphabetized.
  - Strip the word "County" from each value (e.g., "Wood County" → "Wood").
  - Reflect the resolved county set from Resolution v5.x.

- Single‑location entities (Sites, Access Points):
  - Must have exactly one county value.

- Multi‑location entities (Trails, Trail Segments, Trail Networks, Site Networks):
  - May have multiple counties.

No entity may be duplicated per county in the normalized output.

## 4.9 Integrity Anchor Validation and Dedup Check

Normalization performs a **last‑line‑of‑defense** deduplication check using **normalized integrity anchors** defined in per‑entity contracts.

**Process:**

1. Compute the integrity anchor for the normalized entity (per entity‑type rules).
2. Compare against:
   - Other entities normalized in the current run.
   - Existing entities in the Entity Graph.

3. If no match:
   - Proceed to upsert.

4. If a match:
   - Treat as a collision:
     - If either entity carries resolution conflicts:
       - Route to Manual Review Queue with full diff.
     - If neither carries conflicts:
       - Log as a Resolution miss.
       - Route both to Manual Review Queue.
     - If the match is with an existing graph entity:
       - Treat as an update candidate (per Upsert Engine rules).

Normalization must not merge entities; it only detects collisions and routes them.

## 4.10 Parent/Child Validation

- **Site parent/child**:
  - Parent Site relationships must respect Child Site Rules v5.x.
  - No cycles or self‑parenting.
  - Parent Site must exist or be resolvable in the Entity Graph.

- **Access Point parents**:
  - Allowed parent types: Site, Trail, Trail Segment (per rules).
  - Parent IDs must reference valid entities.
  - Site Networks and Trail Networks are not valid parents.

Invalid parent relationships must result in errors or holds according to per‑entity contracts.

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
  - Invalid parent references (cycles, self‑parenting).
  - GPS values out of valid range (when required).
  - Unmappable vocabulary values for **required** vocabulary-governed fields.

- **Held Entities**:
  - Access Points missing GPS (if policy requires GPS before upsert).
  - Networks with unresolved member IDs (if policy prefers hold over reject).

All outcomes must be recorded in normalization provenance.

**Blocking gate enforcement**: After all entities in a run are classified, if any entity is Rejected, the pipeline must halt. All rejections must be surfaced to the operator and logged in the Audit & Logging Module v5.x before any downstream stage (TSV Output, Database Upsert) begins.

------------------------------------------------------------
# 5. PER‑ENTITY NORMALIZATION ROUTING

Each entity type has a dedicated Normalization Contract v5.x that refines cross‑entity rules.

## 5.1 Sites

Key normalizations:

- Category, subtype, designation, status (vocabulary).
- Governance, ownership, partner agencies, coordination (text normalization; some may be vocabulary‑governed — see site vocabulary §8 if added in future versions).
- Counties (normalized as above).
- Parent Site (validate against Entity Graph).
- **Features** — apply four-step normalization sequence per Site Normalization Contract v5.5 §5.18:
  1. Activity detection and mapping (IMP-049): drop or map pure activity tokens per the activity mapping table
  2. Operational content stripping (IMP-050): strip hours, parking, policies, closures, events, facility sub-detail annotations
  3. Named entity detection (IMP-051): drop tokens that name specific Trail, AP, or child Site entities
  4. Vocabulary mapping: map remaining tokens to vocabulary; alphabetize; semicolon-delimit
- **Description** — apply redundancy stripping per Site Normalization Contract v5.5 §5.10 (IMP-052): strip prohibited openers (acreage+category, location, name restatement); blank if no substantive remainder
- **Notes** — apply pipeline metadata stripping per Site Normalization Contract v5.5 §5.19 (IMP-053): strip session references, IMP references, OBJECTID annotations, GPS pending notes, discovery run labels; preserve source attribution lines and operational content
- GPS validation → `gps_lat`, `gps_lon`.
- Plus Code computation.
- GIS derivation → `township`, `municipality`.
- Status inference per §4.2a if `status_raw` is blank.

## 5.2 Trails

Key normalizations:

- Trail use type, surface type, origin type (vocabulary).
- Status, difficulty (vocabulary).
- Accessibility (free‑text or vocabulary per contract).
- Governance, ownership, partner agencies, coordination (text normalization).
- Counties (normalized).
- Total length (numeric validation).
- Maps (semicolon‑delimited URL list; URL format validation).
- Alternate names (semicolon‑delimited).
- Identity notes (text clean).

## 5.3 Trail Segments

Key normalizations:

- Segment type, surface type (vocabulary).
- Status, difficulty (vocabulary).
- Accessibility (free‑text or vocabulary per contract).
- Governance (text normalization).
- Counties (normalized).
- Segment length (numeric validation).
- Geometry (preserved as‑is if part of normalized schema; validated for format only).
- Parent Trail (validate against Entity Graph).
- Maps (semicolon‑delimited URL list; URL format validation).
- Identity notes (text clean).

## 5.4 Trail Networks

Key normalizations:

- Network type, status (vocabulary).
- Ownership, governance, partner agencies, coordination (text normalization).
- Counties (normalized).
- Total length (numeric validation).
- Member trail IDs (validate against Entity Graph).
- Member trail count (derived from validated IDs).
- Maps (semicolon‑delimited URL list; URL format validation).
- Identity notes (text clean).

## 5.5 Site Networks

Key normalizations:

- Network type, status (vocabulary).
- Ownership, governance, partner agencies, coordination (text normalization).
- Counties (normalized).
- Member site IDs (validate against Entity Graph).
- Member count (derived from validated IDs).
- Identity notes (text clean).

## 5.6 Access Points

Key normalizations:

- Access point type, status (vocabulary).
- Features (semicolon‑delimited; free‑text or vocabulary per contract).
- County (single normalized value).
- Address / location description (text clean).
- GPS validation → `gps_lat`, `gps_lon` (required by policy).
- Plus Code computation.
- GIS derivation → `township`, `municipality`.
- Parent relationships (validate against Entity Graph).

Access Points with missing or invalid GPS may be held rather than rejected, depending on policy.

------------------------------------------------------------
# 6. NORMALIZED ENTITY CONSTRUCTION, PROVENANCE, AND VERSIONING

## 6.1 Normalized Entity Structure

Each Normalized Entity must conform to:

- **Entity Graph Schema v5.x**
- The corresponding **Schema Module v5.x**

Typical blocks include:

- `normalized_entity_id` (internal ID or derived from resolved_entity_id).
- `entity_type`.
- Normalized identity fields (name, counties, labels).
- Normalized organizational fields (ownership, governance, partner agencies, coordination).
- Normalized GPS and spatial fields (`gps_lat`, `gps_lon`, `plus_code`, `township`, `municipality`).
- Normalized parent/child fields (parent IDs, member IDs).
- Entity‑specific payload fields (lengths, types, statuses, maps, features).
- Normalization provenance block.

## 6.2 Normalization Provenance

For each entity, Normalization must record:

- Normalization run ID.
- Fields modified and how (e.g., vocabulary mapping, formatting changes).
- GPS validation results (success/failure/blank).
- Plus Code computation result.
- GIS lookup result (township/municipality derived or blank).
- Integrity anchor status and any collisions detected.
- Parent/child validation results.
- Errors, warnings, and hold reasons.
- Status inference result (`status_inferred`, `inference_basis`) if §4.2a was applied.
- Vocabulary failure details for any rejected entity (field name, raw value, failure reason).

Provenance must be:

- Append‑only (does not overwrite resolution provenance).
- Fully auditable.
- Available to review and QA tools.

## 6.3 Integration Points

Normalization Engine v5.8 integrates with:

- **Resolution Engine v5.x** (input).
- **GPS Acquisition Module v5.x** (input for GPS‑updated entities).
- **Schema Modules v5.x** (validation).
- **Vocabulary Modules v5.x** (controlled values).
- **Normalization Contracts v5.x** (per‑entity rules).
- **Child Site Rules v5.x** (parent/child validation).
- **Entity Graph Schema v5.x** (output shape and ID validation).
- **Entity Upsert Engine v5.x** (consumer).
- **GIS Spatial Data** (township and municipality derivation).
- **Audit & Logging Module v5.x** (provenance).

## 6.4 Versioning

- This module is **Normalization Engine v5.8**.
- Any change to cross‑entity normalization rules (schema, vocabulary, GPS/GIS, integrity anchors, parent/child validation, blocking gate behavior) requires a new minor version (v5.7, v5.8, etc.).
- Per‑entity changes that do not affect cross‑entity rules are versioned within the individual Normalization Contracts v5.x.x.

------------------------------------------------------------
# EN