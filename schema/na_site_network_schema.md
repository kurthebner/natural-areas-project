# NATURAL AREAS PROJECT — SITE NETWORK SCHEMA MODULE v4.0
Authoritative, versioned schema for **Site Networks** in the statewide  
Natural Areas & Trails system.

This module defines:
- The Site Network entity type  
- The 15 normalized Site Network fields (authoritative order)  
- Field‑level rules  
- Identity rules  
- Dependencies on the Site Network Vocabulary Module v4.0  

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Site Network Vocabulary Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

A **Site Network** is a named, identity‑bearing umbrella entity composed of  
multiple Sites, documented in authoritative sources and distinct from:

- Individual Sites  
- Trails and Trail Networks  
- Access Points  
- Trail Segments  

Examples include:
- National Heritage Areas  
- Local Historic Districts  
- Scenic River Corridors  
- Watershed‑scale conservation networks  
- Multi‑site conservation or cultural systems  

This schema:
- Establishes the authoritative Site Network record structure  
- Defines field‑level rules  
- Ensures consistency across all counties and data sources  
- Supports discovery, resolution, normalization, TSV output, and the Entity Graph  

This module is authoritative for **Site Network structure**.

------------------------------------------------------------
# 2. SITE NETWORK FIELDS (15 FIELDS, AUTHORITATIVE ORDER)

1. **Network Name**  
2. **Alternate Names**  
3. **Network Type**  
4. **Status**  
5. **Counties Traversed**  
6. **States Included**  
7. **Primary Managing Agency**  
8. **Secondary Managing Agencies**  
9. **Network Affiliation**  
10. **Description**  
11. **History**  
12. **URL**  
13. **Map URL**  
14. **Notes**  
15. **Derived Label** *(computed, not stored)*  

This order is absolute and must never change.

------------------------------------------------------------
# 3. FIELD‑BY‑FIELD RULES

## 3.1 Network Name
- Use the official published name.  
- Must be unique statewide (case‑insensitive).  
- Must not include unofficial descriptors.  
- Must align with identity determined by the **Resolution Module v4.0**.

## 3.2 Alternate Names
- Optional.  
- Semicolon‑delimited list.  
- Include only documented historical or variant names.  
- Must not include invented or speculative names.

## 3.3 Network Type
- Must match a value from the Site Network Vocabulary Module v4.0.  
- Must describe the identity‑bearing classification of the network.  
- Must not encode governance, ownership, or hierarchy.

## 3.4 Status
- Must match a value from the Site Network Vocabulary Module v4.0.  
- “Proposed” must be explicitly documented.  
- Must not be inferred.

## 3.5 Counties Traversed
- Semicolon‑delimited list.  
- Alphabetical order.  
- Must include all counties through which any part of the network passes.  
- Must follow the **universal multi‑county rule v4.0**:  
  - One Site Network record regardless of number of counties  
  - Raw county list preserved in Discovery Metadata  
  - Normalized list alphabetized and semicolon‑delimited  
  - No segmentation of multi‑county entities  
- Must not include the word “County.”

## 3.6 States Included
- Semicolon‑delimited list of states, if multi‑state.  
- Alphabetical order.  
- Leave blank for Ohio‑only networks.  
- Must follow v4.0 normalization rules.  
- Must not be inferred.

## 3.7 Primary Managing Agency
- Use the authoritative primary managing agency.  
- Must not be inferred.  
- Must align with Resolution Module v4.0 if conflicts exist.

## 3.8 Secondary Managing Agencies
- Optional.  
- Semicolon‑delimited list.  
- Include only documented co‑managers.  
- Must not duplicate the primary managing agency.

## 3.9 Network Affiliation
- Optional.  
- Semicolon‑delimited list.  
- Represents formal affiliations with larger regional, federal, or thematic systems.  
- Must not encode hierarchy, ownership, or parentage.  
- Must not duplicate Network Type.  
- Use only for non‑hierarchical affiliations.

## 3.10 Description
- 1–3 sentences describing the network’s identity, scope, and purpose.  
- Must not include site‑level details.  
- Must not include Access Point or Trail details.

## 3.11 History
- Optional.  
- 1–3 sentences of factual, documented historical context.  
- May include origin, designation history, or major changes.  
- Must not include interpretive or speculative content.

## 3.12 URL
- Full `https://` URL to the primary authoritative network page.  
- Semicolon‑delimit if multiple.  
- Must not include placeholders or inferred URLs.

## 3.13 Map URL
- Full `https://` URL to an authoritative map or GIS viewer.  
- May include PDF maps, static images, or interactive GIS layers.  
- Semicolon‑delimit if multiple.  
- Leave blank if none.

## 3.14 Notes
- Optional free‑text field for clarifications or contextual notes.  
- Must not include identity‑defining characteristics.  
- Must not include site‑level or trail‑level details.

## 3.15 Derived Label
- Computed, not stored.  
- Formula (v4.0):  
  **Network Type + " — " + Primary Managing Agency**  
- Must match normalized field values exactly.  
- Must follow Derived Label rules in the Site Network Normalization Contract v4.0.  
- Must not include parentheses, trailing punctuation, or additional descriptors.

------------------------------------------------------------
# 4. IDENTITY RULES

A Site Network is valid only if:
- It is explicitly documented as a multi‑site system.  
- It has a stable, identity‑bearing name.  
- It is composed of two or more Sites.  
- It is distinct from its member Sites.  
- It is not merely a marketing label or informal grouping.  
- It satisfies the identity rules in the **Resolution Module v4.0**.  
- It does **not** have a parent Site Network, Trail Network, or Site.  
- It does **not** serve as a parent for Trails, Trail Segments, or Access Points.  

If any of these conditions fail, the Site Network must not be created.

------------------------------------------------------------
# 5. MODULE DEPENDENCIES

This module depends on:
- **Site Network Vocabulary Module v4.0**  
- **Site Network Normalization Contract v4.0**  
- **Site Network TSV Output Specification v4.0**  
- **Site Network Discovery Sub‑Procedure v4.0**  
- **Resolution Module v4.0**  
- **Discovery Protocol Module v4.0**  

All other modules must reference this schema.

------------------------------------------------------------
# END OF SITE NETWORK SCHEMA MODULE v4.0