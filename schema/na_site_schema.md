# NATURAL AREAS PROJECT — SITE SCHEMA MODULE v2.0
Authoritative, versioned schema for Sites in the statewide Natural Areas & Trails system.

This module defines:
- The Site entity type  
- The 20 Site fields (updated authoritative order)  
- Field‑level rules  
- Identity rules  
- Dependencies on the Site Vocabulary Module v2  

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v2.

---

# 1. PURPOSE
Sites are identity‑bearing land units such as parks, preserves, natural areas, historic sites, cemeteries, campuses, recreation areas, wildlife areas, forests, and conservation lands.

Sites are **not**:
- Trails  
- Trail Segments  
- Access Points  
- Trail Networks  
- Area Networks  
- Sub‑Sites (these are separate entities)

This schema:
- Establishes the authoritative Site record structure  
- Defines field‑level rules  
- Ensures consistency across all counties and data sources  
- Provides the foundation for normalization, TSV output, discovery, and resolution  

This module is authoritative for Site structure.

---

# 2. SITE FIELDS (20 FIELDS, AUTHORITATIVE ORDER)

1. **Name**  
2. **Category**  
3. **Subtype**  
4. **Designation**  
5. **Ownership**  
6. **Management**  
7. **Coordination**  
8. **Description**  
9. **Status**  
10. **Address**  
11. **Acres**  
12. **Location**  
13. **County**  
14. **GPS Coordinates**  
15. **Plus Code**  
16. **Features**  
17. **Notes**  
18. **URL**  
19. **Derived Label** (computed, not stored)  
20. **Parent Site**  

This order is absolute and must never change.

---

# 3. FIELD‑BY‑FIELD RULES

---

## 3.1 Name
- Use the official published name when available.  
- Must be unique within the dataset.  
- Do not include descriptive or unofficial names (those belong in Notes).  

---

## 3.2 Category
- Must match a value from the **Site Vocabulary Module v2**.  
- Must express the ontological identity of the Site.  
- Must not encode governance, ownership, or temporary conditions.  
- Category determines whether Subtype is allowed.  

---

## 3.3 Subtype
- Optional.  
- If present, must match the Category‑dependent lists in the **Site Vocabulary Module v2**.  
- Must represent a stable, identity‑bearing land unit.  
- Must not describe habitat conditions or temporary states.  

---

## 3.4 Designation
- Must match a value from the **Site Vocabulary Module v2**.  
- Use only when explicitly stated in authoritative sources.  
- Do not infer designation.  
- Do not combine multiple designations unless explicitly documented.  

---

## 3.5 Ownership
- Use the official agency or organization name.  
- Do not infer ownership.  
- Must not be blank unless truly unknown.  

---

## 3.6 Management
- Use the official managing agency.  
- Semicolon‑delimit multiple managers.  
- If same as Ownership, repeat explicitly.  

---

## 3.7 Coordination
- Use only when coordination is formally recognized.  
- Leave blank if none.  

---

## 3.8 Description
- 1–3 sentences.  
- Must describe identity‑defining ecological, historical, or cultural characteristics.  
- May include naming history and former names.  
- Must not include amenities or temporary conditions.  

---

## 3.9 Status
- Must match a value from the **Site Vocabulary Module v2**.  
- “Closed” = permanently closed as the entity described.  
- “Proposed” must be officially referenced.  

---

## 3.10 Address
- Leave blank if no formal address exists.  
- Must not include invented street numbers.  

---

## 3.11 Acres
- Numeric only.  
- Leave blank if unknown.  
- No estimates.  

---

## 3.12 Location
- Municipality or township only.  
- Semicolon‑delimit if multiple.  
- Must not include county names.  

---

## 3.13 County
- List all counties the Site spans.  
- Alphabetical.  
- Semicolon‑delimited.  
- Do not include the word “County.”  

---

## 3.14 GPS Coordinates
- Format: `lat,lon`  
- One coordinate pair only.  
- No space after comma.  
- Must be authoritative.  

---

## 3.15 Plus Code
- Derived from accepted GPS coordinates.  
- Blank if GPS is blank.  

---

## 3.16 Features
- Semicolon‑delimited list.  
- Must match values from the **Site Vocabulary Module v2**.  
- Features describe internal components, not identity‑bearing land units.  
- Named Trails, Trail Segments, and Access Points are **never** Features.  
- Minor connectors belong in Notes, not Features.  

---

## 3.17 Notes
- Optional free‑text field.  
- Must not include identity‑defining ecology.  
- Must not include internal features.  
- Use for temporary closures, access restrictions, historical notes, or clarifications.  

---

## 3.18 URL
- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must be authoritative.  

---

## 3.19 Derived Label
- Computed, not stored.  
- Formula: **Category + Ownership + Designation**  
- Must follow the Derived Label rules in the Normalization Contract.  

---

## 3.20 Parent Site
- Leave blank for top‑level Sites.  
- Must match the official Name of the parent Site.  
- A Site may have only one parent.  
- Parent–child relationships must be explicit in authoritative sources.  
- Must not be used to represent Trails, Trail Segments, or Access Points.  

---

# 4. IDENTITY RULES
A Site is valid only if:
- It is an identity‑bearing land unit.  
- It is documented in authoritative sources.  
- It is not a Trail, Trail Segment, Access Point, Trail Network, or Site Network.  
- It is not merely a feature or amenity.  
- It is not a Sub‑Site unless Parent Site is populated.  

If any of these conditions fail, the Site must not be created.

---

# 5. MODULE DEPENDENCIES
This module depends on:

- **Site Vocabulary Module v2**  
  (for Category, Subtype, Designation, Status, Features)

All other modules (Normalization, TSV Output, Discovery, Resolution, Orchestration) must reference this schema.

---

# END OF SITE SCHEMA MODULE v2.0