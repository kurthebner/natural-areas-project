# NATURAL AREAS PROJECT
# NORMALIZATION ENGINE v5.0
(Cross-Entity Normalization Orchestrator for Resolved Entities)

The Normalization Engine v5.0 is the **orchestrator** that transforms
**Resolved Entities** into **Normalized Entities** ready for:

- Entity Graph Schema v5.0
- TSV Output Specifications v5.0

It sits between:

- Resolution Engine v5.0 (input)
- Entity Upsert Engine v5.0 (output)

This module defines:

- Engine responsibilities
- Cross-entity normalization rules
- Per-entity routing
- New v5.0 normalization responsibilities (GPS, GIS derivation)
- Validation requirements
- Integration with Schema & Vocabulary Modules
- Logging and provenance requirements

------------------------------------------------------------
# CHANGES FROM v4.0

- **GPS split**: `gps_primary` string → `gps_lat` + `gps_lon` (numeric, WGS84); engine now responsible for parsing and validation
- **Plus Code**: Now computed from `gps_lat` + `gps_lon` (previously from `gps_primary` string)
- **GIS derivation**: `township` and `municipality` are now populated via GIS spatial lookup during normalization — not collected during discovery
- **County field renamed**: `county_list` → `counties` throughout
- **Governance renamed**: `managing_agency` → `governance`; `secondary_managing_agencies` → `partner_agencies`
- **Access Point fields removed**: `access_level` and `role` dropped — no longer normalized
- **Source fields removed**: `source_primary`, `source_all` removed from entity schemas; tracked in provenance tables only
- Updated all version references to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Normalization Engine v5.0:

- Applies schema rules to all resolved entities
- Applies vocabulary rules to all controlled fields
- Applies formatting rules (including semicolon rules)
- Parses and validates GPS strings into numeric gps_lat / gps_lon
- Computes Plus Codes from gps_lat / gps_lon
- Derives township and municipality via GIS spatial lookup
- Computes Derived Labels
- Validates integrity anchors
- Validates parent/child relationships
- Validates multi-county normalization
- Produces normalized entity objects for all six entity types

It does **not**:

- Discover entities
- Perform fuzzy identity matching or source merging (that is Resolution's responsibility)
- Merge conflicting field values from multiple sources
- Write TSVs directly

------------------------------------------------------------
# 2. INPUTS AND OUTPUTS

## 2.1 Inputs

- Resolved entity objects from Resolution Engine v5.0
- Schema Modules v5.0 (6)
- Vocabulary Modules v5.0 (6)
- Normalization Contracts v5.0 (6)
- Discovery Metadata v5.0 (for provenance and context)
- GIS spatial data (for township and municipality derivation)

## 2.2 Outputs

- Normalized entity objects (one per entity)
- Normalization provenance records
- Validation results (warnings, errors)
- Objects ready for Entity Upsert Engine v5.0

------------------------------------------------------------
# 3. ENGINE WORKFLOW (HIGH-LEVEL)

For each resolved entity:

1. Determine entity type (Site, Trail, Trail Segment, Trail Network, Site Network, Access Point).
2. Route to the appropriate **Normalization Contract v5.0**.
3. Apply:
   - Schema validation
   - Vocabulary normalization
   - Formatting normalization
   - GPS parsing and validation → gps_lat / gps_lon
   - Plus Code computation
   - GIS spatial lookup → township, municipality
   - Derived Label computation
   - **Integrity anchor deduplication check** (last-line-of-defense before upsert)
   - Integrity anchor validation
   - Multi-county normalization
   - Parent/child validation
4. Produce a normalized entity object.
5. Log normalization provenance.
6. Pass normalized entity to Entity Upsert Engine v5.0.

------------------------------------------------------------
# 4. CROSS-ENTITY NORMALIZATION RULES

These rules apply to **all six entity types** unless noted otherwise.

## 4.1 Schema Validation

- All required fields must be present.
- Field types must match Schema Modules v5.0.
- Unknown fields must be ignored or logged as warnings.
- Fields removed in v5.0 (`access_level`, `role`, `source_primary`, `source_all`,
  `network_affiliation`) must be silently dropped if present in resolved records
  from older discovery runs.

## 4.2 Vocabulary Normalization

- All vocabulary-governed fields must:
  - Map to a controlled value from the appropriate Vocabulary Module v5.0
  - Preserve raw value in provenance if mapping is lossy
- Unmappable values:
  - Must be logged as warnings
  - Must not be silently coerced
  - Field left blank if no valid mapping exists

## 4.3 Formatting Rules

- **Semicolon-delimited lists:**
  - Must be trimmed (no leading/trailing spaces)
  - Must not contain empty segments
  - Must be alphabetized where required (counties)
- **Blank fields:**
  - Must be true blanks (no placeholders, no "N/A", no "Unknown")
- **Text fields:**
  - Strip leading/trailing whitespace
  - Normalize line endings
  - Do not alter case unless vocabulary mapping requires it

## 4.4 GPS Parsing and Validation ✨ UPDATED IN v5.0

**Input:** `gps_raw` string in "lat,lon" format from discovery/resolution

**Output:** Numeric `gps_lat` and `gps_lon` fields

**Process:**
1. Parse `gps_raw` string — split on comma
2. Validate both parts are numeric
3. Validate lat is in range [-90, 90]
4. Validate lon is in range [-180, 180]
5. Round to 6 decimal places (≈ 0.1m precision)
6. Assign to `gps_lat` (float) and `gps_lon` (float)

**Error handling:**
- Malformed string (non-numeric, wrong format) → log error, leave gps_lat/gps_lon blank
- Out-of-range values → log error, leave blank
- Missing gps_raw → leave gps_lat/gps_lon blank (valid — GPS not required for most entities during discovery)

**Access Points — GPS required before upsert:**
- Access Points with blank gps_lat/gps_lon after normalization must be flagged
- They may be held pending GPS acquisition rather than rejected outright
- See Access Point Normalization Contract v5.0 for details

## 4.5 Plus Code Computation ✨ UPDATED IN v5.0

**Input:** `gps_lat` and `gps_lon` (numeric, post-validation)

**Output:** `plus_code` string

**Process:**
1. Only compute if both gps_lat and gps_lon are present and valid
2. Compute Open Location Code (Plus Code) from gps_lat / gps_lon
3. Use full 10-character code
4. Assign to `plus_code`

**If GPS is blank:** Leave `plus_code` blank — do not attempt computation.

## 4.6 GIS Spatial Lookup — Township and Municipality ✨ NEW IN v5.0

**Purpose:** Derive township and municipality from GPS coordinates via spatial join against authoritative GIS boundaries.

**Input:** `gps_lat` and `gps_lon` (numeric, post-validation)

**Output:** `township` (civil township name) and `municipality` (city or village name, if applicable)

**Process:**
1. Only run if gps_lat and gps_lon are present and valid
2. Perform point-in-polygon spatial join against:
   - Ohio civil township boundaries (for township)
   - Ohio municipal boundaries — cities and villages (for municipality)
3. Assign matched township name to `township`
4. Assign matched municipality name to `municipality` (blank if point is outside any municipality)
5. Do not append "Township" to township name in the field value

**If GPS is blank:** Leave both `township` and `municipality` blank — do not guess.

**Note:** This is the authoritative source for township and municipality. Discovery records must leave these fields blank. Any township or municipality values collected during discovery are treated as informational only and are overwritten by GIS derivation.

**Multi-location entities (Trails, Trail Networks, Site Networks):**
- Township and municipality derivation is not applicable
- These entities use `counties` for geographic context
- Leave `township` and `municipality` blank for these entity types

## 4.7 Derived Label Computation

- Each entity type has a **Derived Label** rule in its Normalization Contract v5.0.
- Derived Label must:
  - Be deterministic
  - Use normalized fields only
  - Be stable across runs given identical inputs
  - Not be stored — computed at TSV output time

## 4.8 County Normalization ✨ RENAMED IN v5.0 (was county_list)

- `counties` must be:
  - Semicolon-delimited
  - Alphabetized
  - Each value stripped of the word "County" (e.g., "Wood County" → "Wood")
  - Derived from resolved county set
- No entity may be duplicated per county.
- Single-location entities (Sites, Access Points) have exactly one county value.
- Multi-location entities (Trails, Trail Segments, Trail Networks, Site Networks) may have multiple.

## 4.9 Integrity Anchor Deduplication Check ✨ NEW IN v5.0

**Purpose:** Last-line-of-defense deduplication before upsert. Catches cases where the Resolution Engine passed through two separate records for the same real-world entity — either because confidence was below the merge threshold or because the conflict was flagged but not resolved.

**When this runs:** After vocabulary normalization and GPS/GIS derivation, but before upsert. At this point fields are in their final normalized form, making comparison reliable.

**Process:**

For each entity about to be upserted, compare its **integrity anchor** against all entities already normalized in the current run AND against entities already in the Entity Graph:

1. Compute the integrity anchor for the incoming entity (per entity-type rules in Normalization Contracts v5.0)
2. Query for existing entities with matching anchor values
3. If no match → proceed to upsert normally
4. If match found → **collision detected**

**Collision handling:**

A collision means two normalized entities share the same integrity anchor — they are almost certainly the same real-world entity.

- **If one entity came from Resolution with a conflict flag:** Route both back to a **Manual Review Queue** with a diff of their field values. Do not upsert either until resolved.
- **If neither has a conflict flag** (Resolution missed the duplicate): Log as a Resolution miss, route to Manual Review Queue, do not upsert either.
- **If the match is in the Entity Graph** (entity already exists from a prior run): Treat as an update candidate — route to Entity Upsert Engine with `update` intent rather than `insert`.

**What this does NOT do:**

- Does not attempt fuzzy matching — integrity anchors are exact comparisons on normalized values
- Does not merge field values — that remains Resolution's responsibility
- Does not silently discard either record — both are preserved for review

**Manual Review Queue output:**

Each queued collision must include:
- Both entity records in full
- Field-level diff highlighting disagreements
- Source provenance for each field
- Collision type (conflict-flagged / Resolution miss / existing graph entity)

## 4.10 Parent/Child Validation ✨ RENUMBERED FROM 4.9

**Site parent/child:**
- Parent Site relationships must respect Child Site Rules Module v5.0
- Must not create cycles
- Must not create self-parenting
- Parent Site must exist in Entity Graph before child is upserted

**Access Point parents:**
- Must reference valid entities in Entity Graph
- Allowed parent types: Site, Trail, Trail Segment
- Site Networks and Trail Networks are never valid parents

## 4.11 Governance Field Normalization ✨ RENAMED IN v5.0

- v4.0 field `managing_agency` is now `governance`
- v4.0 field `secondary_managing_agencies` is now `partner_agencies`
- Apply standard text normalization (trim, clean encoding)
- No controlled vocabulary — free-text field
- Do not infer from ownership

## 4.12 Removed Fields ✨ v5.0

The following fields from v4.0 are **no longer part of entity schemas** and must be silently dropped during normalization if present:

- `access_level` (Access Points) — removed from schema
- `role` (Access Points) — removed from schema
- `network_affiliation` (Sites, Trails, Trail Segments) — removed; membership tracked via relationship tables
- `source_primary` — removed; tracked in provenance tables
- `source_all` — removed; tracked in provenance tables
- `geometry` — removed from normalized schema; populated in GIS phase only

------------------------------------------------------------
# 5. PER-ENTITY NORMALIZATION ROUTING

## 5.1 Sites

- Use **Site Normalization Contract v5.0**
- Key normalizations:
  - Category, Subtype (vocabulary)
  - Designation, Status (vocabulary)
  - Governance, Partner Agencies (free-text)
  - Ownership (free-text)
  - Counties (alphabetize, strip "County")
  - Parent Site (validate against Entity Graph)
  - Features (semicolon-delimited, validate against vocabulary)
  - Description, Notes (text clean)
  - GPS → gps_lat / gps_lon
  - Plus Code computation
  - GIS derivation → township, municipality
  - Derived Label

## 5.2 Trails

- Use **Trail Normalization Contract v5.0**
- Key normalizations:
  - Trail Use Type, Surface Type, Origin Type (vocabulary)
  - Status, Difficulty (vocabulary)
  - Accessibility (free-text)
  - Governance, Partner Agencies (free-text)
  - Counties (alphabetize, strip "County")
  - Total Length (numeric validation)
  - Maps (rich array — validate url/type/description objects)
  - Alternate Names (semicolon-delimited)
  - Derived Label

## 5.3 Trail Segments

- Use **Trail Segment Normalization Contract v5.0**
- Key normalizations:
  - Segment Type, Surface Type (vocabulary)
  - Status, Difficulty (vocabulary)
  - Accessibility (free-text)
  - Governance (free-text)
  - Counties (alphabetize, strip "County")
  - Length (numeric validation)
  - Geometry (preserve as-is from resolution)
  - Parent Trail (validate against Entity Graph)
  - Maps (rich array)
  - Derived Label

## 5.4 Trail Networks

- Use **Trail Network Normalization Contract v5.0**
- Key normalizations:
  - Network Type, Status (vocabulary)
  - Ownership, Governance, Partner Agencies (free-text)
  - Counties (alphabetize, strip "County")
  - Total Length (numeric validation)
  - Member Trail Count, Member Trail IDs (validate against Entity Graph)
  - Maps (rich array)
  - Derived Label

## 5.5 Site Networks

- Use **Site Network Normalization Contract v5.0**
- Key normalizations:
  - Network Type, Status (vocabulary)
  - Ownership, Governance, Partner Agencies (free-text)
  - Counties (alphabetize, strip "County")
  - Member Count, Member Site IDs (validate against Entity Graph)
  - Derived Label

## 5.6 Access Points

- Use **Access Point Normalization Contract v5.0**
- Key normalizations:
  - Access Point Type, Status (vocabulary)
  - Features (semicolon-delimited, free-text)
  - County (single value, strip "County")
  - Address (text clean)
  - GPS → gps_lat / gps_lon (REQUIRED — flag if missing)
  - Plus Code computation
  - GIS derivation → township, municipality
  - Parent relationships (validate against Entity Graph)
  - Derived Label

------------------------------------------------------------
# 6. MAPS FIELD NORMALIZATION (Trails, Trail Segments, Trail Networks)

The `maps` field in v5.0 uses a **rich array format** for Trail, Trail Segment,
and Trail Network entities. This replaces the simple `map_url` string from v4.0.

**Expected structure per array element:**
```json
{
  "url": "https://...",
  "type": "PDF" | "Interactive" | "Static Image" | "GIS Layer" | "Other",
  "description": "optional free-text description"
}
```

**Normalization rules:**
- Validate that `url` is a well-formed https:// URL
- Validate that `type` matches allowed values
- `description` is optional — blank is valid
- Invalid entries (malformed URL, missing type) → log warning, exclude from normalized output
- Preserve order from resolution — do not sort

**Note:** Sites, Site Networks, and Access Points use simple `map_url` string fields —
the rich array format does not apply to them.

------------------------------------------------------------
# 7. MEMBER ID VALIDATION (Networks)

Trail Networks and Site Networks include member ID fields:
- Trail Networks: `member_trail_ids`
- Site Networks: `member_site_ids`

**Normalization rules:**
- Each ID in the list must reference a valid entity in the Entity Graph
- Invalid IDs → log warning, remove from list
- Update `member_trail_count` / `member_count` to reflect validated list length
- If all member IDs are invalid → log error, flag for review (do not reject — network may precede members)

------------------------------------------------------------
# 8. ERROR HANDLING AND LOGGING

## 8.1 Non-Fatal Errors (Warnings)

- Missing optional fields
- Unmappable vocabulary values
- Minor formatting issues
- GPS present but plus_code computation fails
- Member IDs referencing entities not yet in graph
- Maps entries with missing description

→ Log as warnings in normalization provenance. Entity proceeds to upsert.

## 8.2 Fatal Errors (Rejections)

- Missing required fields
- Invalid field types that cannot be coerced
- Broken integrity anchors
- Invalid parent references (cycles, self-parenting)
- GPS values out of valid range

→ Entity is rejected for upsert, logged as error, and flagged in Audit & Logging.

## 8.3 Held Entities

Some entities are valid but incomplete — they should be held rather than rejected:

- **Access Points with missing GPS** — valid entity, GPS not yet acquired; hold pending GPS
- **Network entities with unresolved member IDs** — valid entity, members may not yet be discovered

→ Log as held. Re-run normalization after dependencies resolve.

## 8.4 Provenance

For each entity, record:

- Normalization run ID
- Fields modified and how
- Vocabularies applied and mappings used
- GPS parsing result (success/failure/blank)
- GIS lookup result (township/municipality derived or blank)
- Plus Code computation result
- Integrity anchor status
- Errors, warnings, and holds

------------------------------------------------------------
# 9. INTEGRATION POINTS

The Normalization Engine v5.0 integrates with:

- **Resolution Engine v5.0** (input)
- **Schema Modules v5.0** (validation — 6 modules)
- **Vocabulary Modules v5.0** (controlled values — 6 modules)
- **Normalization Contracts v5.0** (per-entity rules — 6 contracts)
- **Child Site Rules v5.0** (parent/child validation)
- **Entity Graph Schema v5.0** (output shape and ID validation)
- **Entity Upsert Engine v5.0** (consumer)
- **GIS Spatial Data** (township and municipality derivation)
- **Audit & Logging Module v5.0** (provenance)

------------------------------------------------------------
# 10. VERSIONING

- This module is **Normalization Engine v5.0**.
- Any change to cross-entity rules requires v5.1, v5.2, etc.
- Per-entity changes that do not affect cross-entity rules are versioned
  within the individual Normalization Contracts.

------------------------------------------------------------
# END OF NORMALIZATION ENGINE v5.0
