# NATURAL AREAS PROJECT — TRAIL SEGMENT SCHEMA MODULE v1
Authoritative, versioned schema for Trail Segments in the statewide Natural Areas & Trails system.

This module defines:
- The Trail Segment entity type  
- The Trail Segment fields and authoritative field order  
- Field‑level rules  
- Dependencies on the Trail Segment Vocabulary Module v1  

This module contains no controlled vocabularies.  
All vocabularies are defined in the Trail Segment Vocabulary Module v1.

---

# 1. PURPOSE
Trail Segments are operational portions of a Trail.  
They represent continuous, mappable stretches of a Trail that may differ in surface, management, condition, or jurisdiction.

This schema:
- Establishes the Trail Segment record structure  
- Defines field‑level rules  
- Ensures consistency across all counties and data sources  
- Provides the foundation for Trail Segment normalization, discovery, resolution, and TSV output  

This module is authoritative for Trail Segment structure.

---

# 2. TRAIL SEGMENT FIELDS (AUTHORITATIVE ORDER)

1. **Parent Trail**  
2. **Segment Name**  
3. **County**  
4. **Managing Agency**  
5. **Segment Length (Miles)**  
6. **Surface Type**  
7. **Status**  
8. **GPS Geometry**  
9. **Description**  
10. **Notes**  
11. **Source Confidence**  
12. **Verification Status**  
13. **Field Confidence Map**  
14. **Field Verification Map**

This order is absolute and must never change.

---

# 3. FIELD‑BY‑FIELD RULES

---

## 3.1 Parent Trail
- Must match the exact **Trail Name** of a normalized Trail.  
- Defines the one‑to‑many relationship between Trails and Trail Segments.  
- A Trail Segment must have exactly one parent Trail.  
- Parent–child relationships must be explicitly documented in authoritative sources.  

---

## 3.2 Segment Name
- Optional.  
- Only used when the segment has a documented, identity‑bearing name.  
- Must be unique within the parent Trail.  
- Must not be invented.  
- Unnamed segments must leave this field blank.  

---

## 3.3 County
- Required.  
- Must represent the county or counties the segment physically traverses.  
- Semicolon‑delimit if multiple.  
- Alphabetical order.  
- Must not include the word “County.”  

---

## 3.4 Managing Agency
- Must be an authoritative agency name.  
- Represents the agency responsible for this specific segment.  
- Must not be inferred from the parent Trail.  

---

## 3.5 Segment Length (Miles)
- Numeric only.  
- Represents the length of this segment, not the entire Trail.  
- Blank if unknown.  
- No estimates.  

---

## 3.6 Surface Type
- Must match a value from the **Trail Segment Vocabulary Module v1**.  
- Describes the actual surface of the segment (e.g., Paved, Crushed Stone, Natural).  
- Must not encode use type or origin.  

---

## 3.7 Status
- Must match a value from the **Trail Segment Vocabulary Module v1**.  
- Examples: Active, Planned, Gap, Closed.  
- “Gap” refers to a missing or incomplete portion of the Trail.  

---

## 3.8 GPS Geometry
- Optional.  
- Must be WKT, GeoJSON, or polyline stored as text.  
- Represents the geometry of the segment.  
- Must be authoritative.  

---

## 3.9 Description
- 1–3 sentences.  
- Must describe identity‑defining characteristics of the segment.  
- May include surface changes, jurisdictional notes, or contextual details.  
- Must not duplicate Trail‑level description.  

---

## 3.10 Notes
- Optional free‑text field.  
- Must not include identity‑defining characteristics.  
- Use for clarifications, temporary conditions, or contextual notes.  

---

## 3.11 Source Confidence
- High / Medium / Low.  
- Represents overall confidence in the Trail Segment record.  

---

## 3.12 Verification Status
- Verified / Needs Review / Removed.  
- Represents the current verification state of the Trail Segment record.  

---

## 3.13 Field Confidence Map
- JSON object.  
- Per‑field confidence values.  
- Must follow the structure defined in the Normalization Contract.  

---

## 3.14 Field Verification Map
- JSON object.  
- Per‑field verification values.  
- Must follow the structure defined in the Normalization Contract.  

---

# 4. IDENTITY RULES
A Trail Segment is valid only if:
- It is a continuous, mappable portion of a Trail.  
- It is documented in authoritative sources.  
- It is distinct from the parent Trail.  
- It is not merely a feature or amenity.  
- It is not a standalone Trail.  

If any of these conditions fail, the Trail Segment must not be created.

---

# 5. MODULE DEPENDENCIES
This module depends on:

- **Trail Segment Vocabulary Module v1**  
  (for Surface Type and Status)

All other modules (Normalization, TSV Output, Discovery, Resolution, Orchestration) must reference this schema.

---

# END OF TRAIL SEGMENT SCHEMA MODULE v1