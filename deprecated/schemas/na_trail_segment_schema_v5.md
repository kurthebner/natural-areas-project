# NATURAL AREAS PROJECT
# TRAIL SEGMENT SCHEMA MODULE v5.0
(Authoritative Structure, Semantic Rules, and Validation Requirements for Trail Segment Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Segment Vocabulary Module v5.0**.

This module is authoritative for the structure and semantics of **Trail Segment** entities.

------------------------------------------------------------
# CHANGES FROM v4.0

- `GPS Geometry` renamed to `geometry` (more accurate — this is LineString, not GPS point)
- `Managing Agency` renamed to `governance` (consistent with Trail and Site schemas)
- `County List` renamed to `counties` (array in JSON, semicolon-delimited in TSV)
- `Map URL` replaced by `maps` (rich array — following Trail pattern)
- `Parent Trail Network` removed — segment inherits network via parent trail; edge cases via relationship tables
- `segment_type` added (optional — Linear, Loop, Connector, Spur, Crossing, Access Segment)
- `difficulty` added (optional — can vary by segment)
- `accessibility` added (optional — can vary by segment)
- `segment_role` removed from schema and vocabulary (unclear purpose)

------------------------------------------------------------
# 1. PURPOSE

A **Trail Segment** is a continuous, mappable operational portion of a Trail.
Segments represent stretches that differ in surface, management, jurisdiction,
condition, geometry, or operational characteristics.

A Trail Segment is distinct from:
- The parent Trail
- Sites
- Access Points
- Trail Networks
- Site Networks

This schema is authoritative for **Trail Segment structure**.

------------------------------------------------------------
# 2. TRAIL SEGMENT FIELDS (17 FIELDS, AUTHORITATIVE ORDER)

1. **Parent Trail**
2. **Segment Name**
3. **Counties**
4. **Governance**
5. **Segment Length (Miles)**
6. **Surface Type**
7. **Segment Type**
8. **Status**
9. **Difficulty**
10. **Accessibility**
11. **Description**
12. **Notes**
13. **URL**
14. **Maps**
15. **Geometry**
16. **Derived Label** *(computed, not stored)*

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Parent Trail
- Required.
- Must match the exact Trail Name of a normalized Trail.
- Defines the one-to-many relationship between Trails and Trail Segments.
- A Trail Segment must have exactly one parent Trail.
- Must not be inferred from proximity or geometry.
- Resolution Engine v5.0 handles unresolved parent identities.

## 3.2 Segment Name
- Optional.
- Only used when the segment has a documented, identity-bearing name.
- Must be unique within the parent Trail.
- Must not be invented.
- Unnamed segments must leave this field blank.

## 3.3 Counties
- Required.
- Array in JSON; semicolon-delimited in TSV.
- Alphabetical order.
- Must represent all counties the segment physically traverses.
- Must not include the word "County."
- A multi-county segment is one entity — never segmented.

## 3.4 Governance
- The agency or organization responsible for this specific segment.
- Must be an authoritative name.
- Must not be inferred from the parent Trail.
- Semicolon-delimit if multiple.

## 3.5 Segment Length (Miles)
- Numeric only.
- Represents the length of this segment, not the entire Trail.
- Blank if unknown.
- No estimates.

## 3.6 Surface Type
- Must match a value from the Trail Segment Vocabulary Module v5.0.
- Describes the actual surface of this segment.
- Must not encode use type, origin, or role.

## 3.7 Segment Type
- Optional.
- Must match a value from the Trail Segment Vocabulary Module v5.0.
- Describes the geometric or functional form of the segment.
- Allowed values: Linear, Loop, Connector, Spur, Crossing, Access Segment.
- Most segments are Linear — only populate when type is explicitly documented
  or clearly distinct from Linear.
- Must not be inferred from geometry alone.

## 3.8 Status
- Must match a value from the Vocabulary Module v5.0.
- Examples: Active, Planned, Gap, Closed.
- "Gap" refers to a missing or incomplete portion of the Trail.
- Must not be inferred from imagery.

## 3.9 Difficulty
- Optional.
- Must match a value from the Trail Segment Vocabulary Module v5.0
  (e.g., Easy, Moderate, Difficult, Strenuous, Expert).
- Must be explicitly stated by the trail manager or authoritative source.
- Must not be assessed or inferred by the discoverer.
- Blank if not documented.
- Note: Difficulty may differ from the parent Trail's overall difficulty.

## 3.10 Accessibility
- Optional.
- Free-text description of ADA compliance, wheelchair accessibility,
  surface grade, width, and accessible facilities for this segment.
- Record what authoritative sources state.
- Must not be inferred from surface type alone.
- Blank if not documented.
- Note: Accessibility may differ from the parent Trail's overall accessibility.

## 3.11 Description
- Optional.
- 1-3 sentences.
- Must describe identity-defining characteristics of the segment.
- May include surface changes, jurisdictional notes, or contextual details.
- Must not duplicate Trail-level description.
- Must not include amenities or temporary conditions.

## 3.12 Notes
- Optional free-text field.
- Must not include identity-defining characteristics.
- Use for clarifications, temporary conditions, or contextual notes.
- Must not include Access Point details.

## 3.13 URL
- Optional.
- Full https:// URLs only.
- Semicolon-delimit if multiple.
- Must reference authoritative segment-specific sources.
- Leave blank if none exist.
- Tracking parameters must be removed.

## 3.14 Maps
- Optional.
- Array of map objects in JSON.
- Each map object contains:
  - `url` (required): full https:// URL
  - `type` (optional): pdf, interactive, gpx, kml, image
  - `description` (optional): brief description of map content
- In TSV: semicolon-delimited list of URLs only (metadata dropped).
- Leave blank if none.

## 3.15 Geometry
- Optional.
- Must be WKT LineString or GeoJSON LineString stored as text.
- Represents the linear geometry of the segment.
- Must be authoritative.
- No smoothing, simplification, or inferred geometry.
- Populated in GIS phase — not expected during web discovery.
- All geometry conflicts must be preserved in provenance.

## 3.16 Derived Label
- Computed, not stored.
- Must follow Derived Label rules in the Trail Segment Normalization Contract v5.0.
- Must be deterministic and based solely on normalized fields.

------------------------------------------------------------
# 4. IDENTITY RULES

A Trail Segment is valid only if:

- It is a continuous, mappable portion of a Trail.
- It is documented in authoritative sources OR is a functionally distinct
  portion of a trail with a different surface, manager, or status.
- It is distinct from the parent Trail.
- It is not merely a feature or amenity.
- It is not a standalone Trail.
- It is not a synthetic or inferred segment.

If any of these conditions fail, the Trail Segment must not be created.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Parent Trail
- Every Trail Segment must reference exactly one parent Trail.
- Stored as `parent_trail_id` (FK to trails table).

## 5.2 Trail Network Inheritance
- Trail Segments inherit Trail Network membership through their parent Trail.
- Trail Segments do not have a direct network membership field.
- Edge cases where a segment has independent network membership
  are handled via explicit entries in the `trail_network_members` table.

## 5.3 Access Points
- Access Points may reference a Trail Segment as their identity parent.
- A Trail Segment does not list its Access Points.

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- Trail Segment Vocabulary Module v5.0
- Trail Segment Normalization Contract v5.0
- Trail Schema Module v5.0
- Trail Network Schema Module v5.0
- TSV Output Specification (Trail Segments) v5.0
- Resolution Engine v5.0
- Discovery Protocol Module v5.0

------------------------------------------------------------
# END OF TRAIL SEGMENT SCHEMA MODULE v5.0
