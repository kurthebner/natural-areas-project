# NORMALIZATION ENGINE v5.5  
Cross‑Entity Normalization Orchestrator for Resolved Entities  
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- Updated module version to v5.5.
- Removed Derived Label computation from Sections 5.2 (Trails), 5.3 (Trail Segments),
  5.4 (Trail Networks), and 5.5 (Site Networks). Derived Label was removed from all
  four entity types in their v5.1 schemas and TSV output specs as a presentation-layer
  concern. Section 4.7 (cross-entity Derived Label rule) is retained as it still
  applies to Sites and Access Points.
- Corrected "Maps (rich array)" references in Sections 5.2 and 5.3 to reflect that
  maps was simplified to a plain semicolon-delimited URL list at all stages in v5.1.

------------------------------------------------------------
# 1. PURPOSE, SCOPE, AND ARCHITECTURAL ROLE

## 1.1 Purpose

The Normalization Engine v5.5 transforms **Resolved Entities v5.x** into **Normalized Entities v5.5** ready for:

- Entity Graph Schema v5.x  
- TSV Output Specifications v5.x  

It is the authoritative layer for:

- Schema validation  
- Vocabulary normalization  
- Formatting normalization  
- GPS validation and Plus Code computation  
- GIS spatial lookup (township, municipality)  
- Derived label computation  
- Integrity anchor validation and last‑line dedup checks  
- Parent/child validation  

The engine does **not**:

- Discover entities  
- Perform fuzzy identity matching or merging  
- Acquire GPS (that is the GPS Acquisition Module’s responsibility)  
- Apply ontology or identity rules (those live in the Resolution Rules Module v5.x)  
- Write TSVs or upsert directly to the graph  

## 1.2 Scope

Normalization Engine v5.5 governs:

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
6. **Compute derived labels** for TSV output.  
7. **Validate integrity anchors and parent/child relationships**.  
8. **Produce normalized entities** with full normalization provenance.

Normalization is deterministic and must not infer identity or modify raw resolution decisions.

------------------------------------------------------------
# 2. INPUTS, OUTPUTS, AND DEPENDENCIES

## 2.1 Inputs

Normalization Engine v5.5 consumes:

- **Resolved Entities v5.x** from Resolution Engine v5.x:
  - Including merged identity_block, organizational_block, parent_block, metadata_block, and resolution_provenance.

- **GPS‑updated entities** from GPS Acquisition Module v5.x:
  - Entities with `gps_lat_raw` / `gps_lon_raw` and GPS provenance.

- **Schema Modules v5.x** (6):
  - One per entity type, defining normalized field sets and types.

- **Vocabulary Modules v5.x** (6):
  - Controlled vocabularies for categories, statuses, trail use types, surface types, etc.

- **Normalization Contracts v5.x** (6):
  - Per‑entity normalization rules (required fields, derived labels, integrity anchors).

- **GIS Spatial Data**:
  - Authoritative township and municipal boundaries.

- **Entity Graph Schema v5.x**:
  - For ID validation and parent/child validation.

## 2.2 Outputs

Normalization Engine v5.5 produces:

- **Normalized Entity Objects v5.5**:
  - One per resolved entity, ready for upsert.

- **Normalization Provenance Records**:
  - Field‑level normalization actions, vocabulary mappings, GPS/GIS results, errors, warnings, holds.

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

For each Resolved Entity v5.5:

1. **Determine entity_type**  
   - Site, Trail, Trail Segment, Trail Network, Site Network, Access Point.

2. **Route to the appropriate Normalization Contract v5.x**  
   - Each contract defines required fields, integrity anchors, derived labels, and per‑field rules.

3. **Apply cross‑entity normalization steps**:
   - Schema validation  
   - Vocabulary normalization  
   - Formatting normalization  
   - GPS validation and numeric conversion  
   - Plus Code computation  
   - GIS spatial lookup (township, municipality)  
   - Derived label computation  
   - Integrity anchor validation and dedup check  
   - Parent/child validation  

4. **Construct the normalized entity object**:
   - Populate normalized fields according to schema.  
   - Attach normalization provenance.  

5. **Classify outcome**:
   - Normalized (ready for upsert)  
   - Rejected (fatal errors)  
   - Held (valid but incomplete; dependencies unresolved)  

6. **Emit outputs**:
   - Normalized entity  
   - Provenance  
   - Validation status  

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

- All vocabulary‑governed fields must map to controlled values from the appropriate Vocabulary Module v5.x.  
- Raw values must be preserved in normalization provenance when mapping is lossy or non‑obvious.  
- Unmappable values:
  - Must be logged as warnings.  
  - Must not be silently coerced.  
  - Resulting normalized field is left blank if no valid mapping exists.  

Vocabulary normalization must be deterministic and case‑insensitive where appropriate.

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
  - For Access Points, apply per‑entity rules (often “hold if missing GPS”).  

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
  - `township` = matched township name (without appending “Township”).  
  - `municipality` = matched municipality name or blank if none.  
- If GPS is blank or invalid:
  - Leave `township` and `municipality` blank.  
- Multi‑location entities (Trails, Trail Networks, Site Networks):
  - Do not derive township/municipality; leave blank.  
  - Use `counties` for geographic context.  

GIS lookup is the authoritative source for township and municipality; any discovery‑time values are ignored or treated as informational only.

## 4.7 Derived Label Computation

- Each entity type has a Derived Label rule defined in its Normalization Contract v5.x.  
- Derived Labels:
  - Use normalized fields only.  
  - Are deterministic and stable across runs.  
  - Are computed at normalization time and/or TSV output time.  
  - Are not stored as primary fields in the graph (unless explicitly required).  

Derived Labels must not depend on non‑deterministic data.

## 4.8 County Normalization

- Normalized `counties` field must:
  - Be semicolon‑delimited.  
  - Be alphabetized.  
  - Strip the word “County” from each value (e.g., "Wood County" → "Wood").  
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
  - Unmappable vocabulary values.  
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

- **Held Entities**:
  - Access Points missing GPS (if policy requires GPS before upsert).  
  - Networks with unresolved member IDs (if policy prefers hold over reject).  

All outcomes must be recorded in normalization provenance.

------------------------------------------------------------
# 5. PER‑ENTITY NORMALIZATION ROUTING

Each entity type has a dedicated Normalization Contract v5.x that refines cross‑entity rules.

## 5.1 Sites

Key normalizations:

- Category, subtype, designation, status (vocabulary).  
- Governance, ownership, partner agencies, coordination (text normalization; some may be vocabulary‑governed depending on v5.5 design).  
- Counties (normalized as above).  
- Parent Site (validate against Entity Graph).  
- Features (semicolon‑delimited; vocabulary or free‑text per contract).  
- Description and notes (text clean).  
- GPS validation → `gps_lat`, `gps_lon`.  
- Plus Code computation.  
- GIS derivation → `township`, `municipality`.  
- Derived Label computation.

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
- Derived Label computation.  

Access Points with missing or invalid GPS may be held rather than rejected, depending on policy.

------------------------------------------------------------
# 6. NORMALIZED ENTITY CONSTRUCTION, PROVENANCE, AND VERSIONING

## 6.1 Normalized Entity Structure

Each Normalized Entity v5.5 must conform to:

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

Provenance must be:

- Append‑only (does not overwrite resolution provenance).  
- Fully auditable.  
- Available to review and QA tools.

## 6.3 Integration Points

Normalization Engine v5.5 integrates with:

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

- This module is **Normalization Engine v5.5**.  
- Any change to cross‑entity normalization rules (schema, vocabulary, GPS/GIS, integrity anchors, parent/child validation) requires a new minor version (v5.6, v5.7, etc.).  
- Per‑entity changes that do not affect cross‑entity rules are versioned within the individual Normalization Contracts v5.x.x.  

------------------------------------------------------------
# END OF NORMALIZATION ENGINE v5.5