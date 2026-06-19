# NATURAL AREAS PROJECT
# TRAIL SEGMENT SCHEMA MODULE v5.3
(Authoritative Structure, Semantic Rules, and Validation Requirements for Trail Segment Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Segment Vocabulary Module v5.x**.

This module is authoritative for the structure and semantics of
**Trail Segment** entities.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- **IMP-127** — Corrected `counties` (§3.3) type annotation from `Array in JSON;
  semicolon-delimited in TSV` to `TEXT, semicolon-delimited (stored identically in DB
  and TSV)`. SQLite has no native array type; the field is stored as semicolon-delimited
  TEXT in the database.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **IMP-126** — Corrected stale `integer` type annotation on Segment ID (§3.17) to
  `TEXT` with explicit `OH-{COUNTY}-{TYPE}-{SEQ}` format note. DB schema was already
  correct; this fixes documentation drift introduced before the IMP-107 global ID
  migration.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Derived Label removed**: No longer computed or stored — presentation-
  layer concern only; consistent with Site entity architectural decision
- **identity_notes added**: Separate normalized field for identity
  clarifications, distinct from notes; surfaced from identity_notes_raw
- **maps simplified**: Rich array format (url/type/description objects)
  replaced by plain semicolon-delimited URL list at all stages; type and
  description metadata dropped; consistent with Trail entity
- **Field count corrected**: v5.0 header stated "17 FIELDS" but body
  listed 16 named fields with Segment ID undocumented; v5.1 states
  authoritative count of 17 fields
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `GPS Geometry` renamed to `geometry` (LineString, not GPS point)
- `Managing Agency` renamed to `governance`
- `County List` renamed to `counties`
- `Map URL` replaced by `maps` (simplified to URL list in v5.1)
- `Parent Trail Network` removed — segment inherits network via parent
  Trail; edge cases via relationship tables
- `segment_type` added
- `difficulty` added
- `accessibility` added
- `segment_role` removed

------------------------------------------------------------
# 1. PURPOSE

A **Trail Segment** is a continuous, mappable operational portion of a
Trail. Segments represent stretches that differ in surface, management,
jurisdiction, condition, geometry, or operational characteristics.

A Trail Segment is distinct from:
- The parent Trail
- Sites
- Access Points
- Trail Networks
- Site Networks

This schema is authoritative for **Trail Segment structure**.

------------------------------------------------------------
# 2. TRAIL SEGMENT FIELDS (17 FIELDS, AUTHORITATIVE ORDER)

1.  **Parent Trail**
2.  **Segment Name**
3.  **Counties**
4.  **Governance**
5.  **Segment Length (Miles)**
6.  **Surface Type**
7.  **Segment Type**
8.  **Status**
9.  **Difficulty**
10. **Accessibility**
11. **Description**
12. **Identity Notes**
13. **Notes**
14. **URL**
15. **Maps**
16. **Geometry**
17. **Segment ID**

Trail Network membership is inherited via the parent Trail and stored
in the `trail_network_members` relationship table. It is not encoded
as a field in the Trail Segment record.

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Parent Trail
- Required.
- Must match the exact Trail Name of a normalized Trail.
- A Trail Segment must have exactly one parent Trail.
- Must not be inferred from proximity or geometry.
- Resolution Engine v5.x handles unresolved parent identities.

## 3.2 Segment Name
- Optional.
- Only used when the segment has a documented, identity-bearing name.
- Must be unique within the parent Trail.
- Must not be invented.
- Unnamed segments must leave this field blank.

## 3.3 Counties
- Required.
- TEXT, semicolon-delimited (stored identically in DB and TSV).
- Alphabetical order.
- Must represent all counties the segment physically traverses.
- Must not include the word "County."
- A multi-county segment is one entity — never further segmented.

## 3.4 Governance
- The agency or organization responsible for this specific segment.
- Must be an authoritative name.
- Must not be inferred from the parent Trail's governance.
- Semicolon-delimit if multiple.
- Leave blank if no segment-specific governance documentation exists.

## 3.5 Segment Length (Miles)
- Numeric only.
- Represents the length of this segment, not the entire Trail.
- Blank if unknown.
- No estimates.

## 3.6 Surface Type
- Must match a value from the Trail Segment Vocabulary Module v5.x.
- Describes the actual surface of this segment.
- Must not encode use type, origin, or role.

## 3.7 Segment Type
- Optional.
- Must match a value from the Trail Segment Vocabulary Module v5.x.
- Describes the geometric or functional form of the segment.
- Allowed values: Linear, Loop, Connector, Spur, Crossing, Access
  Segment, Other.
- Most segments are Linear — only populate when type is explicitly
  documented or clearly distinct from Linear.
- Must not be inferred from geometry alone.

## 3.8 Status
- Must match a value from the Trail Segment Vocabulary Module v5.x.
- Examples: Active, Planned, Gap, Closed.
- "Gap" refers to a missing or incomplete portion of the Trail.
- Must not be inferred from imagery.

## 3.9 Difficulty
- Optional.
- Must match a value from the Trail Segment Vocabulary Module v5.x.
- Must be explicitly stated by the trail manager or authoritative
  source.
- Must not be assessed or inferred.
- Blank if not documented.
- Must not be inherited from parent Trail without explicit documentation.

## 3.10 Accessibility
- Optional.
- Free-text description of ADA compliance, wheelchair accessibility,
  surface grade, width, and accessible facilities for this segment.
- Record what authoritative sources state.
- Must not be inferred from surface type alone.
- Must not be inherited from parent Trail without explicit documentation.
- Blank if not documented for this specific segment.

## 3.11 Description
- Optional.
- 1-3 sentences.
- Must describe identity-defining characteristics of this segment.
- May include surface changes, jurisdictional notes, or contextual
  details specific to this segment.
- Must not duplicate Trail-level description.
- Must not include amenities or temporary conditions.

## 3.12 Identity Notes
- Optional free-text field for identity clarifications.
- Use for: segment vs. trail boundary questions, segment name
  conflicts, shared-corridor documentation, parent Trail assignment
  uncertainty, vocabulary type flags.
- Must not duplicate Notes content.
- Must not include operational or contextual notes (those go in Notes).

## 3.13 Notes
- Optional free-text field.
- Must not include identity-defining characteristics.
- Use for: temporary conditions, surface condition details, access
  restrictions, construction updates, gap details.
- Must not include Access Point details.

## 3.14 URL
- Optional.
- Full https:// URLs only.
- Semicolon-delimit if multiple.
- Must reference authoritative segment-specific sources.
- Leave blank if none exist.
- Tracking parameters must be removed.

## 3.15 Maps
- Optional.
- Semicolon-delimited list of URLs to segment map resources.
- Includes: PDF maps, GPX files, KML files, interactive map viewers,
  GIS layers, elevation profiles.
- Distinct from URL — maps are navigation and geometry resources.
- Leave blank if none.

## 3.16 Geometry
- Optional.
- Must be WKT LineString or GeoJSON LineString stored as text.
- Represents the linear geometry of the segment.
- Must be authoritative — no smoothing, simplification, or inferred
  geometry.
- Populated in GIS phase — not expected during web discovery.
- All geometry conflicts must be preserved in provenance.

## 3.17 Segment ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- Must be a valid TEXT ID in OH-{COUNTY}-{TYPE}-{SEQ} format matching the entity's segment_id.

------------------------------------------------------------
# 4. IDENTITY RULES

A Trail Segment is valid only if:

- It is a continuous, mappable portion of a Trail.
- It is documented in authoritative sources OR is a functionally
  distinct portion of a trail with a different surface, manager, or
  status.
- It is distinct from the parent Trail.
- It is not merely a feature or amenity.
- It is not a standalone Trail.
- It is not a synthetic or inferred segment.

If any condition fails, the Trail Segment must not be created.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Parent Trail
- Every Trail Segment must reference exactly one parent Trail.
- Stored as `parent_trail_id` (FK to trails table).

## 5.2 Trail Network Inheritance
- Trail Segments inherit Trail Network membership through their parent
  Trail.
- Trail Segments do not have a direct network membership field.
- Edge cases where a segment has independent network membership are
  handled via explicit entries in the `trail_network_members` table.

## 5.3 Access Points
- Access Points may reference a Trail Segment as their identity parent.
- A Trail Segment does not list its Access Points.

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- Trail Segment Vocabulary Module v5.x
- Trail Segment Normalization Contract v5.x
- Trail Schema Module v5.x
- Trail Network Schema Module v5.x
- TSV Output Specification (Trail Segments) v5.x
- Resolution Engine v5.x
- Discovery Protocol Module v5.x

------------------------------------------------------------
# END OF TRAIL SEGMENT SCHEMA MODULE v5.1
