# NATURAL AREAS PROJECT — TRAIL SCHEMA MODULE v1
Authoritative, versioned schema for Trails in the statewide Natural Areas & Trails system.

This module defines:
- The Trail entity type
- The Trail fields and authoritative field order
- Field‑level rules
- Dependencies on the Trail Vocabulary Module v1

This module contains no controlled vocabularies.  
All vocabularies are defined in the Trail Vocabulary Module v1.

---

# 1. PURPOSE
The Trail Schema defines the authoritative structure for representing identity‑bearing linear corridors such as multi‑use trails, hiking trails, bridle trails, water trails, and purpose‑built recreational routes.

This schema:
- Establishes the Trail record structure  
- Defines field‑level rules  
- Ensures consistency across all counties and data sources  
- Provides the foundation for Trail normalization, discovery, resolution, and TSV output  

This module is authoritative for Trail structure.

---

# 2. TRAIL FIELDS (AUTHORITATIVE ORDER)

1. **Trail Name**  
2. **Alternate Names**  
3. **Trail Use Type**  
4. **Trail Surface Type**  
5. **Trail Origin Type**  
6. **Total Length (Miles)**  
7. **Counties Traversed**  
8. **Managing Agency (Primary)**  
9. **Managing Agencies (Secondary)**  
10. **Status**  
11. **Description**  
12. **Trail History**  
13. **URL**  
14. **Map Link**  
15. **Geometry Type**  
16. **Notes**  
17. **Source Confidence**  
18. **Verification Status**  
19. **Field Confidence Map**  
20. **Field Verification Map**

This order is absolute and must never change.

---

# 3. FIELD‑BY‑FIELD RULES

---

## 3.1 Trail Name
- Use the official published name.  
- Must be unique statewide.  
- Do not include unofficial descriptors (those belong in Notes).  

---

## 3.2 Alternate Names
- Optional.  
- Comma‑separated or JSON array.  
- Include only documented historical or variant names.  

---

## 3.3 Trail Use Type
- Must match a value from the **Trail Vocabulary Module v1**.  
- Describes the primary intended use (e.g., Multi‑Use, Hiking, Bridle, Water, MTB).  
- Must not encode surface or origin.  

---

## 3.4 Trail Surface Type
- Must match a value from the **Trail Vocabulary Module v1**.  
- Describes the predominant surface type.  
- Use “Mixed” only when explicitly documented.  

---

## 3.5 Trail Origin Type
- Must match a value from the **Trail Vocabulary Module v1**.  
- Describes the historical or structural origin (e.g., Rail Trail, Canal Towpath, Purpose‑Built).  
- Must not be inferred.  

---

## 3.6 Total Length (Miles)
- Numeric only.  
- Blank if unknown.  
- No estimates.  
- Represents the full length of the Trail, not individual segments.  

---

## 3.7 Counties Traversed
- Semicolon‑delimited list.  
- Alphabetical order.  
- Must include all counties through which the Trail passes.  
- Must not include the word “County.”  

---

## 3.8 Managing Agency (Primary)
- The primary agency responsible for the Trail.  
- Must be an authoritative agency name.  
- Do not infer.  

---

## 3.9 Managing Agencies (Secondary)
- Optional.  
- Semicolon‑delimited or JSON array.  
- Include only documented co‑managers.  

---

## 3.10 Status
- Must match a value from the **Trail Vocabulary Module v1**.  
- Examples: Active, Planned, Under Construction, Gap, Closed.  
- “Gap” refers to a missing or incomplete portion of an otherwise continuous trail.  

---

## 3.11 Description
- 1–3 sentences.  
- Must describe identity‑defining characteristics of the Trail.  
- Must not include segment‑level details.  

---

## 3.12 Trail History
- Dedicated field for historical context.  
- May include origin, construction history, or major changes.  
- Must be factual and sourced.  

---

## 3.13 URL
- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must reference authoritative sources.  

---

## 3.14 Map Link
- Optional.  
- Must be an authoritative map or GIS viewer link.  

---

## 3.15 Geometry Type
- Usually “Linear.”  
- Must match a value from the **Trail Vocabulary Module v1** if applicable.  
- Must not be inferred.  

---

## 3.16 Notes
- Optional free‑text field.  
- Must not include identity‑defining characteristics.  
- Use for clarifications, temporary conditions, or contextual notes.  

---

## 3.17 Source Confidence
- High / Medium / Low.  
- Represents overall confidence in the Trail record.  

---

## 3.18 Verification Status
- Verified / Needs Review / Removed.  
- Represents the current verification state of the Trail record.  

---

## 3.19 Field Confidence Map
- JSON object.  
- Per‑field confidence values.  
- Must follow the structure defined in the Normalization Contract.  

---

## 3.20 Field Verification Map
- JSON object.  
- Per‑field verification values.  
- Must follow the structure defined in the Normalization Contract.  

---

# 4. IDENTITY RULES
A Trail is valid only if:
- It is an identity‑bearing linear corridor.  
- It is documented in authoritative sources.  
- It is distinct from its Trail Segments.  
- It is not merely a feature within a Site.  

If any of these conditions fail, the Trail must not be created.

---

# 5. MODULE DEPENDENCIES
This module depends on:

- **Trail Vocabulary Module v1**  
  (for Trail Use Type, Trail Surface Type, Trail Origin Type, Status, Geometry Type)

All other modules (Normalization, TSV Output, Discovery, Resolution, Orchestration) must reference this schema.

---

# END OF TRAIL SCHEMA MODULE v1