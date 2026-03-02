# NATURAL AREAS PROJECT
# TRAIL SEGMENT NORMALIZATION CONTRACT v5.1
(Authoritative Field-Level Rules for Normalizing Resolved Trail Segment Entities)

This module defines the v5.1 normalization rules applied by the
Normalization Engine v5.x to transform Resolved Trail Segment entities
into Normalized Trail Segment Objects ready for insertion into the
Entity Graph.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Trail Segment Vocabulary Module v5.x**.

This contract is authoritative for Trail Segment normalization only.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **identity_notes added**: New normalized field surfaced from
  identity_notes_raw; distinct from notes; used for identity
  clarifications, segment vs. trail boundary questions, shared-corridor
  documentation, and parent Trail assignment uncertainty
- **maps simplified**: Rich array format (url/type/description objects)
  replaced by plain semicolon-delimited URL list; object validation
  steps removed; URL-only validation applies; consistent with Trail
- **Derived Label removed**: No longer computed or stored at any stage
- **Raw input field renames**:
  - notes_raw → identity_notes_raw (identity clarifications)
  - url_all → urls_raw (all URLs)
  - url_primary → url_primary_raw
  - maps_raw object array → plain URL list
- **Normalization workflow updated**: Steps revised for removed and
  added fields; maps object validation replaced with URL list validation
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `GPS_Geometry` → `geometry` — renamed; LineString, not GPS point
- `Managing_Agency` → `governance` — renamed
- `County_List` → `counties` — renamed; alphabetized array
- `Map_URL` → `maps` — rich array (simplified to URL list in v5.1)
- `Parent_Trail_Network` removed
- `segment_role` removed
- `segment_type` added
- `difficulty` added — segment-specific, authoritative sources only
- `accessibility` added — segment-specific free-text

------------------------------------------------------------
# 1. PURPOSE

The Trail Segment Normalization Contract v5.1 defines:

- How a Resolved Trail Segment is transformed into a Normalized Trail
  Segment
- How each Trail Segment Schema v5.x field is validated and normalized
- How Segment Type, Surface Type, Status, and Difficulty are normalized
- How Accessibility free-text is handled
- How Identity Notes are surfaced from identity_notes_raw
- How parent Trail relationships are validated
- How geometry is handled
- How the Maps URL list is validated
- How normalization interacts with the Normalization Engine v5.x
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the Entity Upsert Engine v5.x

Normalization must:
- Never invent data
- Never infer parent Trail, segment type, or difficulty
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v5.x, including:

- resolved identity key
- resolved entity_type = "Trail Segment"
- resolved parent_trail
- resolved county set
- resolved governance
- resolved surface_type, segment_type, status
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.1
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
- identity_notes_raw
- url_primary_raw
- urls_raw (all URLs)
- maps_raw (semicolon-delimited URL list)
- geometry_raw (LineString geometry)
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Removed from v5.0 raw inputs:**
- notes_raw — renamed to identity_notes_raw
- url_raw — renamed to url_primary_raw
- url_all — renamed to urls_raw
- maps_raw object array — replaced by URL list

**Not applicable for Trail Segments:**
- No gps_lat_raw, gps_lon_raw — segments use LineString geometry, not
  a single GPS point
- No address — segments have no single address
- No township, municipality — multi-location entities

## 2.3 Vocabulary Modules v5.x
- Trail Segment Vocabulary Module v5.x (Segment Type, Surface Type,
  Status, Difficulty)

## 2.4 Schema Modules v5.x
- Trail Segment Schema Module v5.x
- Trail Schema Module v5.x (for parent Trail validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Trail Segment Object v5.1** conforming to the Trail
  Segment Schema Module v5.x
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.x**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1.  Receive Resolved Trail Segment from Normalization Engine v5.x
2.  Validate identity and entity_type = "Trail Segment"
3.  Normalize Parent Trail
4.  Normalize Segment Name
5.  Normalize Counties
6.  Normalize Governance
7.  Normalize Segment Length
8.  Normalize Surface Type
9.  Normalize Segment Type
10. Normalize Status
11. Normalize Difficulty
12. Normalize Accessibility
13. Normalize Description
14. Normalize Identity Notes
15. Normalize Notes
16. Normalize URL
17. Normalize Maps (URL list)
18. Validate Geometry
19. Run integrity anchor deduplication check (via Normalization Engine)
20. Validate against Trail Segment Schema v5.x
21. Emit Normalized Trail Segment + provenance

If any critical step fails → return error to Normalization Engine v5.x.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Parent Trail

- Required.
- Must match the exact normalized Trail Name of a Trail entity in the
  Entity Graph.
- A Trail Segment must have exactly one parent Trail.
- If parent Trail is unresolved → Resolution Engine v5.x handles
  identity resolution.
- Never infer parentage from proximity, geometry, or naming alone.
- If parent Trail is not yet in Entity Graph → hold segment with
  `hold_reason = unresolved_parent`.

**Provenance:** Log all parent resolution decisions and conflicts.

---

## 5.2 Segment Name

- Optional — only used when the segment has a documented,
  identity-bearing name.
- Minimal whitespace cleanup only.
- Must be unique within the parent Trail.
- Unnamed segments → leave blank.
- Never invent names.
- Never infer names from geometry or map labels alone.

---

## 5.3 Counties

- Required.
- Must match official Ohio county names.
- Alphabetized.
- Semicolon-delimited.
- Omit the word "County."
- A multi-county segment is **one entity** — never further segmented.

---

## 5.4 Governance

- Must contain the **actual name(s)** of the operational managing
  organization(s) for this specific segment.
- Semicolon-delimit if multiple managers.
- Must not use generic categories.
- **Segment-specific rule:** Do not inherit governance from the parent
  Trail without explicit documentation. Governance at the segment level
  may differ.
- Leave blank if no segment-specific governance documentation exists.

---

## 5.5 Segment Length (Miles)

- Numeric only — no units, no ranges, no approximation symbols.
- Represents the length of this segment, not the entire Trail.
- Never estimate.
- If sources conflict → use most authoritative source; log conflict.
- Leave blank if unknown.

---

## 5.6 Surface Type

- Must match a controlled value from Trail Segment Vocabulary Module
  v5.x.
- Describes the predominant surface type of this segment.
- One value only.
- Surface type is often the **primary reason a segment exists** —
  document carefully.
- Never infer from imagery alone.

**Common normalization mappings:**
- "asphalt" → "Paved"
- "crushed limestone" → "Crushed Stone"
- "dirt trail" → "Natural Surface"
- See Trail Segment Vocabulary Module v5.x for full mapping table.

---

## 5.7 Segment Type

- Must match a controlled value from Trail Segment Vocabulary Module
  v5.x.
- Optional — leave blank if not clearly documentable.
- Never infer from geometry alone without authoritative documentation.
- "Linear" is the default; only populate when type is explicitly
  documented or clearly distinct.

---

## 5.8 Status

- Must match a controlled value from Trail Segment Vocabulary Module
  v5.x.
- Describes the status of this segment specifically — may differ from
  parent Trail.
- "Closed" = permanently or indefinitely closed only.
- "Gap" applies when this segment represents a documented missing
  portion of the trail.
- "Planned" must be explicitly documented.
- Never infer from imagery.
- Temporary closures → Notes.

---

## 5.9 Difficulty

- Must match a controlled value from Trail Segment Vocabulary Module
  v5.x.
- Optional — leave blank if not documented for this specific segment.
- **CRITICAL:** Only populate from explicit authoritative source
  ratings — never assess yourself, never infer.
- **Segment-specific rule:** Do not inherit from parent Trail unless
  explicitly documented. A segment may be rated differently than the
  parent Trail's overall rating.

---

## 5.10 Accessibility

- Free-text — no controlled vocabulary.
- Optional — leave blank if no accessibility information is documented
  for this specific segment.
- **Segment-specific rule:** Do not inherit from parent Trail without
  explicit documentation.
- Must not be inferred from surface type alone.

---

## 5.11 Description

- 1-3 sentences describing identity-defining characteristics of this
  segment specifically.
- Must not duplicate parent Trail description.
- Must not include amenities or temporary conditions.
- Must not contradict controlled fields.

---

## 5.12 Identity Notes

Surfaced from `identity_notes_raw` at discovery stage.

**Use for:**
- Segment vs. trail boundary questions
- Segment name conflicts or ambiguities
- Shared-corridor documentation
- Parent Trail assignment uncertainty
- Vocabulary type flags (e.g., "source calls this a 'section' —
  unclear if named segment or informal reference")
- Notes added during Resolution or Normalization passes

**Rules:**
- Must not duplicate Notes content
- Must not contain operational or contextual notes (those go in Notes)
- Preserve uncertainty flags — do not resolve silently

---

## 5.13 Notes

- Optional free text.
- Use for: temporary closures, surface condition details, access
  restrictions, construction updates, gap details.
- Must not include identity-defining characteristics.
- Must not include Access Point details.
- Must not contradict controlled fields.

---

## 5.14 URL

- Full https:// URL to primary authoritative source for this segment.
- Single value.
- May reference parent Trail page if no segment-specific URL exists.
- Remove tracking parameters.
- Leave blank if no URL available.

---

## 5.15 Maps

- Semicolon-delimited list of URLs to segment map resources.
- Includes: PDF maps, GPX files, KML files, interactive map viewers,
  GIS layers, elevation profiles.
- Each URL must be well-formed https://.
- Remove malformed URLs — log as warning.
- Remove duplicates.
- No embedded metadata (type, description) — URLs only.
- Leave blank if none.

**Validation rules:**
- Each entry must be a well-formed https:// URL
- No embedded metadata
- No empty segments (no consecutive semicolons)

---

## 5.16 Geometry

**Trail Segments use LineString geometry, not a GPS point.**

- Stored in `entity_geometry` table only — not in the core
  `trail_segments` table.
- Use `geometry_resolved` exactly as provided — do not simplify,
  smooth, or alter.
- Preserve coordinate precision.
- If geometry is malformed → leave blank, log error, flag for review.
- All geometry conflicts must be preserved in provenance.
- Geometry is populated in the GIS phase — may be blank at initial
  normalization.

**Note:** There is no gps_lat / gps_lon for Trail Segments. GPS point
fields do not apply to this entity type.

---

## 5.17 Parent Trail Network — REMOVED IN v5.0

- `Parent_Trail_Network` is no longer a field in the Trail Segment
  schema.
- Segment inherits network membership via its parent Trail.
- Edge cases handled via relationship tables.
- If present in older resolved records → silently drop.

---

## 5.18 Segment Role — REMOVED IN v5.0

- `segment_role` is no longer a field.
- If present in older resolved records → silently drop.

------------------------------------------------------------
# 6. MULTI-COUNTY NORMALIZATION RULES

- A Trail Segment spanning multiple counties produces **one normalized
  entity**.
- `counties` must include all counties traversed, alphabetized,
  semicolon-delimited.
- Never segment multi-county Trail Segments.
- No township or municipality fields — not applicable to multi-location
  entities.

------------------------------------------------------------
# 7. IDENTITY ANCHOR VALIDATION

The integrity anchor for Trail Segments is:
`entity_type` + `parent_trail` + `segment_name` + `counties`

For unnamed segments:
`entity_type` + `parent_trail` + `counties` + `surface_type`
(or geometry hash)

This contract must verify:
- `parent_trail` is present and references a valid Trail entity
- `counties` is a valid, alphabetized list
- Anchor is unique within the parent Trail

The Normalization Engine v5.x runs the deduplication check after this
validation.

**Note on unnamed segments:** Unnamed segments within the same parent
Trail and county set must be distinguished by surface_type or geometry.
If two unnamed segments share the same anchor → flag as potential
duplicate for manual review.

------------------------------------------------------------
# 8. VALIDATION LOGIC

Normalization must validate:

- All vocabulary-controlled fields map to valid values
- Segment Length: numeric only, no units
- Counties: alphabetized, semicolon-delimited, "County" stripped
- Maps: each entry is a well-formed https:// URL; no embedded metadata
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
- Record alternates in Identity Notes.
- Log conflict.

### 10.2 Conflicting Length
- Use the most authoritative source; log conflict.

### 10.3 Conflicting Surface Type, Segment Type, or Status
- Use authoritative trail system sources.
- If unclear → leave blank, flag in identity_notes.

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
- Log in identity_notes.

------------------------------------------------------------
# 11. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate segment length.
- Never infer segment type, surface type, or difficulty.
- Never infer parent Trail from proximity or geometry alone.
- Never populate governance from parent Trail without explicit
  documentation.
- Never populate difficulty or accessibility from parent Trail without
  explicit segment-level documentation.

------------------------------------------------------------
# 12. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied
- Parent Trail resolution decision
- Geometry validation result
- All difficulty and accessibility sources
- Maps URL validation results (valid/invalid URLs, duplicates removed)
- Identity Notes content surfaced from identity_notes_raw
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Trail Segment Vocabulary Module v5.x
- Trail Segment Schema Module v5.x
- Trail Schema Module v5.x (for parent Trail validation)
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Upsert Engine v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF TRAIL SEGMENT NORMALIZATION CONTRACT v5.1
