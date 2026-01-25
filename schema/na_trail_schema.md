# NATURAL AREAS PROJECT — TRAIL SCHEMA MODULE v4.0
Authoritative, versioned schema for **Trails** in the statewide  
Natural Areas & Trails system.

This module defines:
- The Trail entity type  
- The 18 normalized Trail fields (authoritative order)  
- Field‑level rules  
- Identity rules  
- Dependencies on the Trail Vocabulary Module v4.0  

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Vocabulary Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

A **Trail** is a named, identity‑bearing linear corridor documented in  
authoritative sources. Examples include:

- Multi‑use trails  
- Hiking trails  
- Bridle trails  
- Water trails  
- Mountain bike trails  
- Purpose‑built recreational routes  

A Trail is distinct from:

- Trail Segments  
- Sites  
- Access Points  
- Trail Networks  
- Site Networks  

This schema:
- Establishes the authoritative Trail record structure  
- Defines field‑level rules  
- Ensures consistency across all counties and data sources  
- Supports discovery, resolution, normalization, TSV output, and the Entity Graph  

This module is authoritative for **Trail structure**.

------------------------------------------------------------
# 2. TRAIL FIELDS (18 FIELDS, AUTHORITATIVE ORDER)

1. **Trail Name**  
2. **Alternate Names**  
3. **Trail Use Type**  
4. **Trail Surface Type**  
5. **Trail Origin Type**  
6. **Total Length (Miles)**  
7. **Counties Traversed**  
8. **Primary Managing Agency**  
9. **Secondary Managing Agencies**  
10. **Status**  
11. **Description**  
12. **Trail History**  
13. **URL**  
14. **Map URL**  
15. **Notes**  
16. **Network Affiliation**  
17. **Derived Label** *(computed, not stored)*  
18. **Parent Trail Network** *(optional)*  

This order is absolute and must never change.

------------------------------------------------------------
# 3. FIELD‑BY‑FIELD RULES

## 3.1 Trail Name
- Use the official published name.  
- Must be unique statewide (case‑insensitive).  
- Must not include unofficial descriptors.  
- Must match the identity determined by the **Resolution Module v4.0**.

## 3.2 Alternate Names
- Optional.  
- Semicolon‑delimited list.  
- Include only documented historical or variant names.  
- Must not include marketing names or slogans.

## 3.3 Trail Use Type
- Must match a value from the Trail Vocabulary Module v4.0.  
- Describes the primary intended use (e.g., Multi‑Use, Hiking, Bridle, Water, MTB).  
- Must not encode surface or origin.  
- Must not be inferred.

## 3.4 Trail Surface Type
- Must match a value from the Vocabulary Module v4.0.  
- Describes the predominant surface type.  
- Use “Mixed” only when explicitly documented.

## 3.5 Trail Origin Type
- Must match a value from the Vocabulary Module v4.0.  
- Describes the historical or structural origin (e.g., Rail Trail, Canal Towpath, Purpose‑Built).  
- Must not be inferred.

## 3.6 Total Length (Miles)
- Numeric only.  
- Blank if unknown.  
- No estimates.  
- Represents the full length of the Trail, not individual segments.

## 3.7 Counties Traversed
- Semicolon‑delimited list.  
- Alphabetical order.  
- Must include all counties through which the Trail passes.  
- Must follow the **universal multi‑county rule v4.0**:  
  - No segmentation  
  - One Trail record regardless of number of counties  
  - Raw county list preserved in Discovery Metadata  
  - Normalized list alphabetized and semicolon‑delimited  
- Must not include the word “County.”

## 3.8 Primary Managing Agency
- The primary agency responsible for the Trail.  
- Must be an authoritative agency name.  
- Must not be inferred.  
- Must align with Resolution Module v4.0 if conflicts exist.

## 3.9 Secondary Managing Agencies
- Optional.  
- Semicolon‑delimited list.  
- Include only documented co‑managers.  
- Must not duplicate the primary agency.

## 3.10 Status
- Must match a value from the Vocabulary Module v4.0.  
- Examples: Active, Planned, Under Construction, Gap, Closed.  
- “Gap” refers to a missing or incomplete portion of an otherwise continuous trail.

## 3.11 Description
- 1–3 sentences.  
- Must describe identity‑defining characteristics of the Trail.  
- Must not include segment‑level details.  
- Must not include Access Point details.

## 3.12 Trail History
- Optional.  
- May include origin, construction history, or major changes.  
- Must be factual and sourced.

## 3.13 URL
- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must reference authoritative sources.  
- No placeholders or inferred URLs.

## 3.14 Map URL
- Full `https://` URL to an authoritative map or GIS viewer.  
- May include PDF maps, static images, or interactive GIS layers.  
- Semicolon‑delimit if multiple.  
- Leave blank if none.

## 3.15 Notes
- Optional free‑text field.  
- Must not include identity‑defining characteristics.  
- Use for clarifications, temporary conditions, or contextual notes.

## 3.16 Network Affiliation
- Optional.  
- Semicolon‑delimited list.  
- Represents formal, documented affiliations with Trail Networks or regional systems.  
- Must not encode hierarchy or ownership.  
- Must not duplicate the Parent Trail Network field.  
- Use only for non‑hierarchical affiliations.

## 3.17 Derived Label
- Computed, not stored.  
- Formula (v4.0):  
  **Trail Use Type + " — " + Primary Managing Agency + " — " + Status**  
- Must match normalized field values exactly.  
- Must follow Derived Label rules in the Normalization Contract v4.0.  
- Must not include parentheses, punctuation, or additional descriptors.

## 3.18 Parent Trail Network
- Optional.  
- Must match the exact **Trail Network Name**.  
- Used only when the Trail is a documented member of a Trail Network.  
- Must not be used to represent Trail Segments.  
- A Trail may have at most one Parent Trail Network.  
- Must align with Resolution Module v4.0 if conflicts exist.

------------------------------------------------------------
# 4. IDENTITY RULES

A Trail is valid only if:
- It is an identity‑bearing linear corridor.  
- It is documented in authoritative sources.  
- It is distinct from its Trail Segments.  
- It is not merely a feature within a Site.  
- It satisfies the identity rules in the **Resolution Module v4.0**.  

If any of these conditions fail, the Trail must not be created.

------------------------------------------------------------
# 5. MODULE DEPENDENCIES

This module depends on:

- **Trail Vocabulary Module v4.0**  
  (Trail Use Type, Trail Surface Type, Trail Origin Type, Status)  
- **Trail Segment Schema Module v4.0**  
- **Trail Segment Vocabulary Module v4.0**  
- **Trail Network Schema Module v4.0**  
- **Normalization Contract v4.0**  
- **TSV Output Specification v4.0**  
- **Resolution Module v4.0**  
- **Discovery Protocol Module v4.0**  

All other modules must reference this schema.

------------------------------------------------------------
# END OF TRAIL SCHEMA MODULE v4.0