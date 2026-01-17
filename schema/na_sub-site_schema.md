# NATURAL AREAS PROJECT — SUB‑SITE SCHEMA MODULE v1
Authoritative, versioned schema for Sub‑Sites in the statewide Natural Areas & Trails system.

This module defines:
- The Sub‑Site entity type  
- The Sub‑Site fields and authoritative field order  
- Field‑level rules  
- Dependencies on the Sub‑Site Vocabulary Module v1  

This module contains no controlled vocabularies.  
All vocabularies are defined in the Sub‑Site Vocabulary Module v1.

---

# 1. PURPOSE
Sub‑Sites are named, identity‑bearing internal land units contained within a parent Site.  
They represent distinct, meaningful places such as gardens, cemetery sections, historic villages, disc golf courses, and other internal areas that have their own identity but do not rise to the level of a standalone Site.

This schema:
- Establishes the Sub‑Site record structure  
- Defines field‑level rules  
- Ensures consistency across all counties and data sources  
- Provides the foundation for Sub‑Site normalization, discovery, resolution, and TSV output  

This module is authoritative for Sub‑Site structure.

---

# 2. SUB‑SITE FIELDS (AUTHORITATIVE ORDER)

1. **Parent Site**  
2. **Sub‑Site Name**  
3. **Alternate Names**  
4. **Sub‑Site Type**  
5. **Description**  
6. **County**  
7. **GPS Coordinates**  
8. **URL**  
9. **Map Link**  
10. **Notes**  
11. **Source Confidence**  
12. **Verification Status**  
13. **Field Confidence Map**  
14. **Field Verification Map**

This order is absolute and must never change.

---

# 3. FIELD‑BY‑FIELD RULES

---

## 3.1 Parent Site
- Must match the exact **Name** field of a normalized Site.  
- Defines the one‑to‑many relationship between Sites and Sub‑Sites.  
- A Sub‑Site must have exactly one parent Site.  
- Parent–child relationships must be explicitly documented in authoritative sources.  

---

## 3.2 Sub‑Site Name
- Required.  
- Sub‑Sites exist only when they have a documented, identity‑bearing name.  
- Must be the official published name when available.  
- Must be unique within the parent Site.  

---

## 3.3 Alternate Names
- Optional.  
- Comma‑separated or JSON array.  
- Include only documented historical or variant names.  

---

## 3.4 Sub‑Site Type
- Must match a value from the **Sub‑Site Vocabulary Module v1**.  
- Describes the ontological identity of the Sub‑Site (e.g., Garden, Cemetery Section, Disc Golf Course, Historic Village).  
- Must not encode temporary conditions or amenities.  

---

## 3.5 Description
- 1–3 sentences.  
- Must describe identity‑defining characteristics of the Sub‑Site.  
- May include naming history or contextual details.  
- Must not include amenities or temporary conditions.  

---

## 3.6 County
- Optional.  
- Only used when the Sub‑Site is known to be in a different county than the parent Site.  
- Semicolon‑delimit if multiple.  
- Alphabetical order.  
- Must not include the word “County.”  

---

## 3.7 GPS Coordinates
- Optional.  
- Format: `lat,lon`  
- One coordinate pair only.  
- Must be authoritative.  
- Represents the centroid or defining point of the Sub‑Site.  

---

## 3.8 URL
- Optional.  
- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must reference authoritative sources.  

---

## 3.9 Map Link
- Optional.  
- Must be an authoritative map or GIS viewer link.  

---

## 3.10 Notes
- Optional free‑text field.  
- Must not include identity‑defining characteristics.  
- Use for clarifications, temporary conditions, or contextual notes.  

---

## 3.11 Source Confidence
- High / Medium / Low.  
- Represents overall confidence in the Sub‑Site record.  

---

## 3.12 Verification Status
- Verified / Needs Review / Removed.  
- Represents the current verification state of the Sub‑Site record.  

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
A Sub‑Site is valid only if:
- It is a named, identity‑bearing internal land unit.  
- It is explicitly documented in authoritative sources.  
- It is not merely a feature or amenity.  
- It is not a Trail or Trail Segment.  
- It is not a standalone Site.  

If any of these conditions fail, the Sub‑Site must not be created.

---

# 5. MODULE DEPENDENCIES
This module depends on:

- **Sub‑Site Vocabulary Module v1**  
  (for Sub‑Site Type)

All other modules (Normalization, TSV Output, Discovery, Resolution, Orchestration) must reference this schema.

---

# END OF SUB‑SITE SCHEMA MODULE v1