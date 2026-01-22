# NATURAL AREAS PROJECT — SITE SCHEMA MODULE v3.2.2
Authoritative, versioned schema for **Sites** in the statewide  
Natural Areas & Trails system.

This module defines:
- The Site entity type  
- The 22 normalized Site fields (authoritative order)  
- Field‑level rules  
- Category definitions (ontological identity)  
- Identity rules  
- Parent Site rules  
- Derived Label rules  
- Dependencies on the Site Vocabulary Module v3.2  

This module contains **no controlled vocabularies**.  
All vocabularies are defined in the **Site Vocabulary Module v3.2**.

------------------------------------------------------------
# 1. PURPOSE

A **Site** is a named, bounded, identity‑bearing land unit documented in  
authoritative sources. Examples include parks, preserves, natural areas,  
historic sites, cemeteries, campuses, recreation areas, wildlife areas,  
forests, and conservation lands.

Sites are **not**:
- Trails  
- Trail Segments  
- Access Points  
- Trail Networks  
- Site Networks  
- Features or amenities  

A Site may be:
- A **top‑level** identity‑bearing land unit, or  
- A **child Site** (a named, identity‑bearing unit within a parent Site),  
  represented by the **Parent Site** field  

This schema:
- Establishes the authoritative Site record structure  
- Defines field‑level rules  
- Encodes the ontological meaning of Category and Subtype  
- Ensures consistency across all counties and data sources  
- Provides the foundation for discovery, normalization, resolution, and TSV output  

This module is authoritative for **Site structure and semantics**.

------------------------------------------------------------
# 2. SITE FIELDS (22 FIELDS, AUTHORITATIVE ORDER)

1. **Name**  
2. **Category**  
3. **Subtype**  
4. **Designation**  
5. **Ownership**  
6. **Management**  
7. **Coordination**  
8. **Network Affiliation**  
9. **Description**  
10. **Status**  
11. **Address**  
12. **Acres**  
13. **Location**  
14. **County**  
15. **GPS Coordinates**  
16. **Plus Code**  
17. **Features**  
18. **Notes**  
19. **URL**  
20. **Map URL**  
21. **Derived Label** *(computed, not stored)*  
22. **Parent Site**  

This order is absolute and must never change.

------------------------------------------------------------
# 3. CATEGORY DEFINITIONS (ONTOLOGICAL IDENTITY)

Category expresses **what the Site is** at the highest level.  
It is the primary identity label and must align with these definitions.

*(All Category definitions from v3.2.2 remain unchanged and authoritative.)*

------------------------------------------------------------
# 4. FIELD‑BY‑FIELD RULES

## 4.1 Name
- Use official published name  
- Must be unique statewide  
- Uniqueness is **case‑insensitive**  
- Must not include descriptive or unofficial names  
- Must not add Category/Subtype/Designation unless official  

## 4.2 Category
- Must match Vocabulary Module  
- Must align with semantic definitions  
- Must not encode governance, ownership, or temporary conditions  

## 4.3 Subtype
- Optional  
- Must match Category‑dependent lists  
- Must align with semantic meaning  
- Must not describe habitat or features  

## 4.4 Designation
**Concept:** formal legal or administrative status.

- Must match Vocabulary Module  
- Use only when explicitly documented  
- Must not be inferred  
- Must not duplicate Category or Subtype  
- Must not encode ownership, governance, or temporary conditions  
- Must not include marketing or informal labels  
- Multiple designations: semicolon‑delimit + alphabetize  
- Must apply to the **Site**, not a trail/network/institution  

## 4.5 Ownership
**Concept:** legal title.

- Must reflect legal owner  
- Must use official legal names  
- Must not encode management, category, designation, or temporary conditions  
- Must not list personal names  
- Must be based on authoritative sources  
- Must not be inferred from signage or assumptions  
- Multiple owners: semicolon‑delimit + alphabetize  
- Unknown: use “Unknown” + explain in Notes  

## 4.6 Management
**Concept:** operational control.

- Must reflect managing entity  
- Must use official names  
- Must not encode ownership, category, designation, or access rules  
- Must be documented  
- Multiple managers: semicolon‑delimit + alphabetize  
- If same as Ownership, repeat explicitly  
- Unknown: use “Unknown” + explain in Notes  

## 4.7 Coordination
**Concept:** documented partnership.

- Must be officially documented  
- Must not duplicate Ownership or Management  
- Must not encode category, designation, access rules, or temporary volunteer activity  
- Allowed types: government partners, land trusts, nonprofits, academic institutions, private entities  
- Multiple partners: semicolon‑delimit + alphabetize  
- May be blank  

## 4.8 Network Affiliation
- Semicolon‑delimited  
- Must be formally documented  
- Must not encode hierarchy, ownership, or parentage  
- Must not imply parent–child relationships  

## 4.9 Description
**Concept:** identity.

- 1–3 sentences  
- Must describe what the Site *is*  
- Must express defining ecological, cultural, historical, or physical character  
- Must not include governance, ownership, designation, parcel IDs, URLs, or operational nuance  
- Must not contradict controlled fields  
- Visitor‑facing, stable  

## 4.10 Status
- Must match Vocabulary Module  
- Must be explicitly documented  
- Must not be inferred from imagery  
- Describes the **Site**, not Trails or Access Points  
- Must not encode ownership or governance  
- “Closed” = permanently closed  
- “Proposed” must be officially referenced  

## 4.11 Address
- Blank if no formal address  
- Must not include invented numbers  
- Must not include coordinates  

## 4.12 Acres
- Numeric only  
- Blank if unknown  
- No estimates or ranges  

## 4.13 Location
**Concept:** concise, human‑readable geographic reference.

- One phrase or sentence  
- Must not include county names  
- Must not include identity‑bearing terms  
- Must not include governance or access rules  
- Must not include full addresses or coordinates  
- Allowed: roads, intersections, municipalities, townships, geographic features, directional cues, placement within larger complexes  

## 4.14 County
- List all counties  
- Alphabetical  
- Semicolon‑delimited  
- No “County” in the field  
- Multi‑county Sites must have one record  
- Must follow **v3.2.2 multi‑county normalization rules**:  
  - Raw county list preserved in Discovery Metadata  
  - Normalized list alphabetized  
  - No segmentation of multi‑county Sites  

## 4.15 GPS Coordinates
- Format: `lat,lon`  
- One pair only  
- No space after comma  
- Must be authoritative  

## 4.16 Plus Code
- Derived from **normalized** GPS  
- Blank if GPS blank  

## 4.17 Features
- Semicolon‑delimited  
- Must match Features vocabulary  
- Features = internal components, not identity‑bearing units  
- Trails, Trail Segments, Access Points, and Sub‑Sites are **never** Features  

## 4.18 Notes
**Concept:** context.

- Free‑text, multi‑paragraph allowed  
- Must not contradict controlled fields  
- Must not contain identity‑bearing information  
- Must not contain governance or ownership  
- May include clarifications, exceptions, boundary notes, access nuance, historical names, parcel IDs, citations, URLs, multi‑entity relationships  
- Must not contain speculation or personal opinions  
- Non‑identity‑bearing  

## 4.19 URL
- Full `https://` URLs  
- Semicolon‑delimit if multiple  
- Must be authoritative  

## 4.20 Map URL
- Full `https://` URLs  
- May include PDFs, static images, GIS viewers  
- Semicolon‑delimit if multiple  

## 4.21 Derived Label
- Computed, not stored  
- Formula (v3.2.2):  
  **Category + " — " + (Ownership if not Unknown, else Management) + " — " + Designation**  
- Must follow Normalization Contract  
- Regenerate when any component changes  

## 4.22 Parent Site
- Blank for top‑level Sites  
- Must match exact Name of parent  
- Only one parent allowed  
- Must be explicitly documented  
- Must not represent Trails or Access Points  
- Must not be inferred from signage, layout, or assumptions  

------------------------------------------------------------
# 5. IDENTITY RULES

A Site is valid only if:
- It is named  
- It is bounded  
- It is identity‑bearing  
- It is documented in authoritative sources  
- It is not a Trail, Trail Segment, Access Point, Trail Network, or Site Network  
- It is not merely a feature or amenity  
- If Parent Site is populated, the Site must follow Sub‑Site Rules v3.2  

**Core distinction:**  
- **Description = identity**  
- **Notes = context**  

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- **Site Vocabulary Module v3.2**  
- **Sub‑Site Rules Module v3.2**  
- **Normalization Contract v3.2.2**  
- **TSV Output Specification v3.2.2**  
- **Resolution Module v3.2**  
- **Discovery Protocol Module v3.2.2**  

All other modules must reference this schema.

------------------------------------------------------------
# END OF SITE SCHEMA MODULE v3.2.2