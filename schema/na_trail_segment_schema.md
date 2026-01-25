# NATURAL AREAS PROJECT — TRAIL SEGMENT SCHEMA MODULE v4.0
Authoritative, versioned schema for **Trail Segments** in the statewide  
Natural Areas & Trails system.

This module defines:
- The Trail Segment entity type  
- The 14 normalized Trail Segment fields (authoritative order)  
- Field‑level rules  
- Identity rules  
- Dependencies on the Trail Segment Vocabulary Module v4.0  

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Segment Vocabulary Module v4.0**.

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

This schema:
- Establishes the authoritative Trail Segment record structure  
- Defines field‑level rules  
- Ensures consistency across all counties and data sources  
- Supports discovery, resolution, normalization, and TSV output  
- Aligns with the v4.0 identity model and multi‑county rules  

This module is authoritative for **Trail Segment structure**.

------------------------------------------------------------
# 2. TRAIL SEGMENT FIELDS (14 FIELDS, AUTHORITATIVE ORDER)

1. **Parent Trail**  
2. **Segment Name**  
3. **County List**  
4. **Managing Agency**  
5. **Segment Length (Miles)**  
6. **Surface Type**  
7. **Status**  
8. **GPS Geometry**  
9. **Description**  
10. **Notes**  
11. **URL**  
12. **Map URL**  
13. **Derived Label** *(computed during normalization)*  
14. **Parent Trail Network** *(optional)*  

This order is absolute and must never change.

------------------------------------------------------------
# 3. FIELD‑BY‑FIELD RULES

## 3.1 Parent Trail
- Must match the exact **Trail Name** of a normalized Trail.  
- Defines the one‑to‑many relationship between Trails and Trail Segments.  
- A Trail Segment must have exactly one parent Trail.  
- Parent–child relationships must be explicitly documented.  
- No inference from proximity or geometry.  
- Resolution Engine v4.0 handles unresolved parent identities.

## 3.2 Segment Name
- Optional.  
- Only used when the segment has a documented, identity‑bearing name.  
- Must be unique within the parent Trail.  
- Must not be invented.  
- Unnamed segments must leave this field blank.  
- Alternate names appear in Description.

## 3.3 County List
- Required.  
- Must represent the county or counties the segment physically traverses.  
- Semicolon‑delimited.  
- Alphabetized.  
- Must not include the word “County.”  
- Never inferred.  
- A multi‑county segment is **one entity**, never segmented.

## 3.4 Managing Agency
- Must be an authoritative agency name.  
- Represents the agency responsible for this specific segment.  
- Must not be inferred from the parent Trail.  
- Semicolon‑delimit if multiple.

## 3.5 Segment Length (Miles)
- Numeric only.  
- Represents the length of this segment, not the entire Trail.  
- Blank if unknown.  
- No estimates.  
- No inferred lengths from geometry.

## 3.6 Surface Type
- Must match a value from the Trail Segment Vocabulary Module v4.0.  
- Describes the actual surface of the segment.  
- Must not encode use type, origin, or role.

## 3.7 Status
- Must match a value from the Vocabulary Module v4.0.  
- Examples: Active, Planned, Gap, Closed.  
- “Gap” refers to a missing or incomplete portion of the Trail.  
- Must not be inferred from imagery.

## 3.8 GPS Geometry
- Optional.  
- Must be WKT, GeoJSON, or polyline stored as text.  
- Represents the geometry of the segment.  
- Must be authoritative.  
- No smoothing, simplification, or inferred geometry.  
- All geometry conflicts must be preserved in provenance.

## 3.9 Description
- 1–3 sentences.  
- Must describe identity‑defining characteristics of the segment.  
- May include surface changes, jurisdictional notes, or contextual details.  
- Must not duplicate Trail‑level description.  
- Must not include amenities or temporary conditions.

## 3.10 Notes
- Optional free‑text field.  
- Must not include identity‑defining characteristics.  
- Use for clarifications, temporary conditions, or contextual notes.  
- Must not include Access Point details.

## 3.11 URL
- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must reference authoritative segment‑specific sources.  
- Leave blank if none exist.  
- Tracking parameters must be removed.

## 3.12 Map URL
- Full `https://` URL to an authoritative map or GIS viewer.  
- May include PDF maps, static images, or interactive GIS layers.  
- Semicolon‑delimit if multiple.  
- Leave blank if none.

## 3.13 Derived Label
- Computed during normalization (v4.0).  
- Not stored in the database.  
- Must follow Derived Label rules in the Normalization Contract v4.0.  
- Must be deterministic and based solely on normalized fields.

## 3.14 Parent Trail Network
- Optional.  
- Must match the exact **Trail Network Name**.  
- Used only when the segment is a documented member of a Trail Network.  
- Must not be used to represent Trail → Trail Segment relationships.  
- No inferred network membership.

------------------------------------------------------------
# 4. IDENTITY RULES

A Trail Segment is valid only if:
- It is a continuous, mappable portion of a Trail.  
- It is documented in authoritative sources.  
- It is distinct from the parent Trail.  
- It is not merely a feature or amenity.  
- It is not a standalone Trail.  
- It is not a synthetic or inferred segment.  

If any of these conditions fail, the Trail Segment must not be created.

------------------------------------------------------------
# 5. MODULE DEPENDENCIES

This module depends on:

- **Trail Segment Vocabulary Module v4.0**  
- **Trail Segment Normalization Contract v4.0**  
- **Trail Schema Module v4.0**  
- **Trail Network Schema Module v4.0**  
- **TSV Output Specification (Trail Segments) v4.0**  
- **Resolution Engine v4.0**  
- **Discovery Protocol Module v4.0**  

All other modules must reference this schema.

------------------------------------------------------------
# END OF TRAIL SEGMENT SCHEMA MODULE v4.0