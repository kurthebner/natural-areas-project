# NATURAL AREAS PROJECT
# TRAIL SEGMENT NORMALIZATION CONTRACT v5.0
(Authoritative Field-Level Rules for Normalizing Resolved Trail Segment Entities)

This module defines the v5.0 normalization rules applied by the
Normalization Engine v5.0 to transform Resolved Trail Segment entities into
Normalized Trail Segment Objects v5.0 ready for insertion into the
Entity Graph Schema v5.0.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Trail Segment Vocabulary Module v5.0**.

This contract is authoritative for Trail Segment normalization only.

------------------------------------------------------------
# CHANGES FROM v4.0

- **`GPS_Geometry` → `geometry`**: Renamed for accuracy — this is a LineString, not a GPS point; stored in `entity_geometry` table only
- **`Managing_Agency` → `governance`**: Renamed for consistency with Trail and Site schemas
- **`County_List` → `counties`**: Renamed; alphabetized array
- **`Map_URL` → `maps`**: Rich array format (url / type / description objects), following Trail pattern
- **`Parent_Trail_Network` removed**: Segment inherits network membership via parent Trail; relationship tables handle edge cases
- **`segment_role` removed**: Field removed from schema and vocabulary
- **`segment_type` added**: Optional — Linear, Loop, Connector, Spur, Crossing, Access Segment
- **`difficulty` added**: Optional — only from authoritative sources; may differ from parent Trail
- **`accessibility` added**: Optional free-text; segment-specific only
- **No GPS point field**: Trail Segments use geometry (LineString), not a single GPS coordinate
- **No township/municipality**: Multi-location entities — these fields do not apply
- **Derived Label**: Computed at TSV output time, NOT during normalization (changed from v4.0)
- Updated all version references to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Trail Segment Normalization Contract v5.0 defines:

- How a Resolved Trail Segment is transformed into a Normalized Trail Segment
- How each Trail Segment Schema v5.0 field is validated and normalized
- How Segment Type, Surface Type, Status, and Difficulty are normalized
- How Accessibility free-text is handled
- How parent Trail relationships are validated
- How geometry is handled
- How the Maps rich array is validated
- How normalization interacts with the **Normalization Engine v5.0**
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the **Entity Upsert Engine v5.0**

Normalization must:

- Never invent data
- Never infer parent Trail, segment type, or difficulty
- Never silently correct malformed values
- Always log normalization decisions

Derived Label is not computed here.
It is computed only during TSV output.

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From **Resolution Engine v5.0**, including:

- resolved identity key
- resolved entity_type = "Trail Segment"
- resolved parent_trail
- resolved county set
- resolved governance
- resolved surface_type, segment_type, status
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.0
Including:

- segment_name_raw
- parent_trail_raw
- counties_raw
- governance_raw
- segment_length_miles_raw
- surface_type_raw
- segment_type_raw
- status_raw
- difficulty_raw
- accessibility_raw
- description_raw
- notes_raw
- url_raw
- maps_raw (array of url/type/description objects)
- geometry_raw (LineString geometry)
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Removed from v4.0 raw inputs:**
- segment_role_raw — field no longer exists
- parent_trail_network_raw — field no longer exists

**Not applicable for Trail Segments:**
- No gps_raw (segments use geometry, not a single GPS point)
- No address (segments have no single address)
- No township, municipality (multi-location entities)

## 2.3 Normalization Engine Outputs (Pre-Populated)
Trail Segments do not use GPS or GIS derivation — the Normalization Engine
does not pre-populate gps_lat, gps_lon, township, or municipality for this entity type.

Geometry is handled separately (see Section 5.13).

## 2.4 Vocabulary Modules v5.0
- Trail Segment Vocabulary Module v5.0 (Segment Type, Surface Type, Status, Difficulty)

## 2.5 Schema Modules v5.0
- Trail Segment Schema Module v5.0
- Trail Schema Module v5.0 (for parent Trail validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Trail Segment Object v5.0** conforming to the Trail Segment Schema Module v5.0
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.0**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1. Receive Resolved Trail Segment from Normalization Engine v5.0
2. Validate identity and entity_type = "Trail Segment"
3. Normalize Parent Trail
4. Normalize Segment Name
5. Normalize Counties
6. Normalize Governance
7. Normalize Segment Length
8. Normalize Surface Type
9. Normalize Segment Type
10. Normalize Status
11. Normalize Difficulty
12. Normalize Accessibility
13. Normalize Description
14. Normalize Notes
15. Normalize URL
16. Normalize Maps (rich array)
17. Validate Geometry
18. Run integrity anchor deduplication check (via Normalization Engine)
19. Validate against Trail Segment Schema v5.0
20. Emit Normalized Trail Segment + provenance

If any critical step fails → return error to Normalization Engine v5.0.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Parent Trail

- Required.
- Must match the exact normalized Trail Name of a Trail entity in the Entity Graph.
- A Trail Segment must have exactly one parent Trail.
- If parent Trail unresolved → Resolution Engine v5.0 handles identity resolution.
- Never infer parentage from proximity, geometry, or naming alone.
- If parent Trail not yet in Entity Graph → hold segment with `hold_reason = unresolved_parent`.

**Provenance:** Log all parent resolution decisions and conflicts.

---

## 5.2 Segment Name

- Optional — only used when the segment has a documented, identity-bearing name.
- Use name_raw with minimal whitespace cleanup.
- Must be unique within the parent Trail.
- Unnamed segments → leave blank; Derived Label constructed from parent Trail name + sequence at TSV output.
- Never invent names.
- Never infer names from geometry or map labels alone.

**Provenance:** Log all name conflicts and corrections.

---

## 5.3 Counties ✨ RENAMED FROM v4.0 (was `County_List`)

- Required.
- Must match official Ohio county names.
- Alphabetized.
- Semicolon-delimited.
- Omit the word "County".
- A multi-county segment is **one entity** — never segmented.
- All counties traversed must be represented.

---

## 5.4 Governance ✨ RENAMED FROM v4.0 (was `Managing_Agency`)

- Must contain the **actual name(s)** of the operational managing organization(s).
- Semicolon-delimit if multiple managers are formally documented.
- Must not use generic categories.
- Must not encode ownership, designation, or access rules.
- Leave blank if unverifiable.

**Note:** Governance at the segment level may differ from the parent Trail's governance. Only populate if segment-specific governance documentation exists. Do not inherit from parent Trail unless explicitly documented.

---

## 5.5 Segment Length (Miles)

- Numeric only — no units, no ranges, no approximation symbols.
- Never estimate.
- If sources conflict → use most authoritative source.
- Leave blank if unknown.

---

## 5.6 Surface Type

- Must match a controlled value from Trail Segment Vocabulary Module v5.0.
- Describes the predominant surface type of this segment.
- One value only.
- Surface type is often the **primary reason a segment exists** — document carefully.
- Never infer from imagery alone.

**Common normalization mappings:**
- "asphalt" → "Paved"
- "crushed limestone" → "Crushed Stone"
- "dirt trail" → "Natural Surface"
- See Trail Segment Vocabulary Module v5.0 for full mapping table.

---

## 5.7 Segment Type ✨ NEW IN v5.0

- Must match a controlled value from Trail Segment Vocabulary Module v5.0.
- Optional — leave blank if not clearly documentable.
- Allowed values: Linear, Loop, Connector, Spur, Crossing, Access Segment.
- Never infer from geometry alone without authoritative documentation.

**Usage guidance:**
- **Linear** — the default for straightforward through-segments
- **Loop** — only when segment forms a documented loop
- **Connector** — explicitly documented connecting segment between two trails or systems
- **Spur** — documented branch off the main trail
- **Crossing** — road, rail, or waterway crossing
- **Access Segment** — dedicated segment providing access to a trailhead or facility

---

## 5.8 Status

- Must match a controlled value from Trail Segment Vocabulary Module v5.0.
- Describes the status of this segment specifically — may differ from parent Trail.
- "Closed" = permanently closed only.
- "Gap" applies when this segment represents a documented missing portion of the trail.
- "Proposed" must be explicitly documented.
- Never infer from imagery.
- Temporary closures → Notes.

---

## 5.9 Difficulty ✨ NEW IN v5.0

- Must match a controlled value from Trail Segment Vocabulary Module v5.0.
- Optional — leave blank if not documented by authoritative source.
- **CRITICAL:** Only populate from explicit authoritative source ratings.
  - ❌ Do not assess difficulty yourself
  - ❌ Do not infer from length, elevation, or surface type
  - ✅ Only record when managing agency explicitly rates this segment
- **Segment-specific rule:** Do not inherit from parent Trail unless explicitly documented.
  - A segment may be rated Easy while the parent Trail is rated Difficult.
  - Only populate if segment-specific difficulty documentation exists.

---

## 5.10 Accessibility ✨ NEW IN v5.0

- Free-text — no controlled vocabulary.
- Optional — leave blank if no accessibility information is documented for this specific segment.
- **Segment-specific rule:** Do not inherit from parent Trail unless explicitly stated.
  - A segment may be ADA accessible while the parent Trail is not.
- Must not be inferred from surface type alone.
- Record the accessibility description as documented by the authoritative source.

**Examples of valid values:**
- "ADA accessible; paved surface, grades under 5%"
- "Wheelchair accessible for entire length"
- "Not ADA compliant; natural surface with variable grades"

---

## 5.11 Description

- 1-3 sentences.
- Must describe identity-defining characteristics of this segment specifically.
- Include naming history and alternate identifiers if documented.
- Must not include amenities or temporary conditions.
- Must not duplicate parent Trail description.
- Must not contradict controlled fields.

---

## 5.12 Notes

- Optional free text.
- Use for: temporary closures, surface conditions, access restrictions, construction updates, gap details.
- Must not include identity-defining characteristics (those belong in Description).
- Must not include Access Point details.
- Must not contradict controlled fields.

---

## 5.13 URL

- Full https:// URL to primary authoritative source for this segment.
- Single value.
- May reference parent Trail page if no segment-specific URL exists.
- Remove tracking parameters.
- Leave blank if no URL available.

---

## 5.14 Maps ✨ NEW IN v5.0 (replaces `Map_URL`)

The `maps` field is a **rich array** — each element is an object with:
- `url` (required) — full https:// URL
- `type` (required) — one of: PDF, Interactive, Static Image, GIS Layer, Other
- `description` (optional) — brief description of what the map shows

**Normalization rules:**
- Validate each element: url must be well-formed https://; type must match allowed values
- Remove elements with malformed URLs — log as warning
- Remove elements with missing type — log as warning
- `description` may be blank — that is valid
- Preserve order from resolution — do not sort
- Semicolon-delimited in TSV output (urls only); full array in JSON

---

## 5.15 Geometry ✨ RENAMED FROM v4.0 (was `GPS_Geometry`)

**Trail Segments use LineString geometry, not a GPS point.**

- Stored in `entity_geometry` table only — not in the `trail_segments` core table.
- Use `geometry_resolved` exactly as provided — do not simplify, smooth, or alter.
- Preserve coordinate precision.
- If geometry is malformed → leave blank, log error, flag for review.
- All geometry conflicts must be preserved in provenance.
- Geometry is populated in the GIS phase — may be blank at initial normalization.

**Note:** There is no gps_lat / gps_lon for Trail Segments. GPS point fields do not apply to this entity type.

---

## 5.16 Parent Trail Network ✨ REMOVED IN v5.0

- `Parent_Trail_Network` is no longer a field in the Trail Segment schema.
- Segment inherits network membership via its parent Trail.
- Edge cases handled via relationship tables.
- If network affiliation values are present in resolved records from older discovery runs → silently drop.

---

## 5.17 Segment Role ✨ REMOVED IN v5.0

- `segment_role` is no longer a field in the Trail Segment schema or vocabulary.
- If segment role values are present in resolved records from older discovery runs → silently drop.

------------------------------------------------------------
# 6. MULTI-COUNTY NORMALIZATION RULES

- A Trail Segment spanning multiple counties produces **one normalized entity**.
- `counties` must include all counties traversed, alphabetized, semicolon-delimited.
- Never segment multi-county Trail Segments.
- No township or municipality fields — not applicable to multi-location entities.

------------------------------------------------------------
# 7. IDENTITY ANCHOR VALIDATION

The integrity anchor for Trail Segments is:
`entity_type` + `parent_trail` + `segment_name` + `counties`

For unnamed segments:
`entity_type` + `parent_trail` + `counties` + `surface_type` (or geometry hash)

This contract must verify:
- `parent_trail` is present and references a valid Trail entity
- `counties` is a valid, alphabetized list
- Anchor is unique within the parent Trail

The Normalization Engine v5.0 runs the deduplication check after this validation.

---

**Note on unnamed segments:** Unnamed segments within the same parent Trail and
county set must be distinguished by surface_type or geometry. If two unnamed
segments share the same anchor → flag as potential duplicate for manual review.

------------------------------------------------------------
# 8. VALIDATION LOGIC

Normalization must validate:

- All vocabulary-controlled fields map to valid values
- Segment Length: numeric only, no units
- Counties: alphabetized, semicolon-delimited, "County" stripped
- Maps array: each element has valid url and type
- Geometry: valid GeoJSON LineString or blank
- Parent Trail: references valid entity in Entity Graph
- Semicolon formatting: trimmed, no empty segments
- No invented data
- Blank fields are true blanks
- No delimiter characters inside field values

If any field fails validation:
- Surface as warning or error (per severity)
- Do not silently correct
- Log in normalization provenance

------------------------------------------------------------
# 9. DELIMITER INTEGRITY REQUIREMENTS

Normalization must ensure:

- Blank fields are true blanks
- No spaces between semicolons and values
- No trailing spaces or newlines within fields
- No collapsed delimiters (consecutive semicolons)
- No missing delimiters in multi-value fields

All anomalies must be logged.

------------------------------------------------------------
# 10. CONFLICT HANDLING

### 10.1 Conflicting Names
- Use the most authoritative source.
- Record alternates in Description.
- Log conflict.

### 10.2 Conflicting Length
- Use the most authoritative source (managing agency preferred).
- If conflict persists → log, use highest-authority value, flag for review.

### 10.3 Conflicting Surface Type, Segment Type, or Status
- Use authoritative trail system sources.
- If unclear → leave blank, flag uncertainty.

### 10.4 Conflicting Difficulty
- If sources disagree → leave blank, log conflict.
- Never average or choose arbitrarily.

### 10.5 Conflicting Geometry
- Preserve all geometry claims in provenance.
- Use the most authoritative geometry (agency GIS preferred).
- If unclear → log conflict, flag for review.

### 10.6 Conflicting Parent Trail
- Do not assign a parent until conflict is resolved.
- Surface to Resolution Engine.

------------------------------------------------------------
# 11. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate segment length.
- Never infer segment type, surface type, or difficulty.
- Never infer parent Trail from proximity or geometry alone.
- Never populate governance from parent Trail without explicit documentation.
- Never populate difficulty or accessibility from parent Trail without explicit documentation.

------------------------------------------------------------
# 12. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied
- Parent Trail resolution decision
- Geometry validation result
- All difficulty and accessibility sources
- Maps array validation results
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Trail Segment Vocabulary Module v5.0
- Trail Segment Schema Module v5.0
- Trail Schema Module v5.0 (for parent Trail validation)
- Discovery Output Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Graph Schema v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF TRAIL SEGMENT NORMALIZATION CONTRACT v5.0
