# NATURAL AREAS PROJECT — SITE SCHEMA MODULE v1
Authoritative, versioned schema for Sites in the statewide Natural Areas & Trails system.

This module defines:
- The Site entity type
- The 25 Site fields
- Field‑level rules
- Dependencies on the Site Vocabulary Module v1

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v1.

---

# 1. PURPOSE
The Site Schema defines the authoritative structure for representing parks, preserves, natural areas, trail systems, trail segments, historic sites, internal features, and related land units.

This schema:
- Establishes the 25‑field Site record structure  
- Defines field‑level rules  
- Ensures consistency across all counties and data sources  
- Provides the foundation for normalization, TSV output, discovery, and resolution  

This module is authoritative for Site structure.

---

# 2. SITE FIELDS (25 FIELDS, AUTHORITATIVE ORDER)

1. Name  
2. Category  
3. Subtype  
4. Designation  
5. Ownership  
6. Management  
7. Coordination  
8. Description  
9. Status  
10. Address  
11. Acres  
12. Location  
13. County  
14. GPS Coordinates  
15. Plus Code  
16. Trail Role  
17. Parent Trail Name  
18. Trail Segment Type  
19. Trail Access Type  
20. Trail Length (Miles)  
21. Features  
22. Notes  
23. URL  
24. Derived Label  
25. Parent Site  

This order is absolute and must never change.

---

# 3. FIELD‑BY‑FIELD RULES

---

## 3.1 Name
- Use the official published name when available.  
- Do not include descriptive or unofficial names (those belong in Notes).  
- Must be unique within the dataset.  

---

## 3.2 Category
- Must match a value from the **Site Vocabulary Module v1**.  
- Must express the ontological identity of the site.  
- Must not encode governance, ownership, or temporary conditions.  
- Category determines whether Subtype is allowed.  

---

## 3.3 Subtype
- Optional.  
- If present, must match the Category‑dependent lists in the **Site Vocabulary Module v1**.  
- Must represent a stable, identity‑bearing land unit.  
- Must not describe habitat conditions or temporary states.  

---

## 3.4 Designation
- Must match a value from the **Site Vocabulary Module v1**.  
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
- Must describe identity‑defining ecological or historical characteristics.  
- May include naming history and former names.  
- Must not include amenities or temporary conditions.  

---

## 3.9 Status
- Must match a value from the **Site Vocabulary Module v1**.  
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
- List all counties the site spans.  
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

## 3.16 Trail Role
- Must match a value from the **Site Vocabulary Module v1**.  
- Must reflect the site’s relationship to a trail network.  
- Use “None” when the site has no trail identity.  

---

## 3.17 Parent Trail Name
- Required for segments and spurs.  
- Blank otherwise.  
- Must match the official name of the parent trail.  

---

## 3.18 Trail Segment Type
- Must match a value from the **Site Vocabulary Module v1**.  
- Use only when Trail Role = Trail Segment.  
- Use “None” when not applicable.  

---

## 3.19 Trail Access Type
- Must match a value from the **Site Vocabulary Module v1**.  
- Use only when the site functions as a trail access location.  
- Use “None” when not applicable.  

---

## 3.20 Trail Length (Miles)
- Numeric only.  
- Blank for non‑trail sites.  
- No estimates.  
- No units.  

---

## 3.21 Features
- Semicolon‑delimited list.  
- Must match values from the **Site Vocabulary Module v1**.  
- Features describe internal components, not identity‑bearing land units.  
- Named trails are never Features.  
- Unnamed trails use the trail‑related Feature terms.  
- Minor connectors belong in Notes, not Features.  

---

## 3.22 Notes
- Optional free‑text field.  
- Must not include identity‑defining ecology.  
- Must not include internal features.  
- Use for temporary closures, access restrictions, historical notes, or clarifications.  

---

## 3.23 URL
- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must be authoritative.  

---

## 3.24 Derived Label
- Computed, not stored.  
- Formula: **Category + Ownership + Designation**  
- Must follow the Derived Label rules in the Normalization Contract.  

---

## 3.25 Parent Site
- Leave blank for top‑level sites.  
- Must match the official Name of the parent site.  
- A site may have only one parent.  
- Parent–child relationships must be explicit in authoritative sources.  

---

# 4. MODULE DEPENDENCIES
This module depends on:

- **Site Vocabulary Module v1**  
  (for Category, Subtype, Designation, Status, Trail Role, Trail Segment Type, Trail Access Type, Features)

All other modules (Normalization, TSV Output, Discovery, Resolution, Orchestration) must reference this schema.

---

# END OF SITE SCHEMA MODULE v1