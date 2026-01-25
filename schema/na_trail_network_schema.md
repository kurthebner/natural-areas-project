# NATURAL AREAS PROJECT — TRAIL NETWORK SCHEMA MODULE v4.0
Authoritative, versioned schema for **Trail Networks** in the statewide  
Natural Areas & Trails system.

This module defines:
- The Trail Network entity type  
- The 13 normalized Trail Network fields (authoritative order)  
- Field‑level rules  
- Identity rules  
- Dependencies on the Trail Network Vocabulary Module v4.0  

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Network Vocabulary Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

A **Trail Network** is a named, identity‑bearing umbrella entity composed of  
multiple Trails. Examples include:

- Regional greenway systems  
- National scenic trail systems  
- Water trail networks  
- Multi‑county or multi‑state trail systems  

A Trail Network is distinct from:

- Individual Trails  
- Trail Segments  
- Sites  
- Access Points  
- Site Networks  

This schema:
- Establishes the authoritative Trail Network record structure  
- Defines field‑level rules  
- Ensures consistency across all counties and data sources  
- Supports discovery, resolution, normalization, and TSV output  
- Aligns with the v4.0 identity model and multi‑county rules  

This module is authoritative for **Trail Network structure**.

------------------------------------------------------------
# 2. TRAIL NETWORK FIELDS (13 FIELDS, AUTHORITATIVE ORDER)

1. **Trail Network Name**  
2. **Alternate Names**  
3. **Network Type**  
4. **Description**  
5. **History**  
6. **County List**  
7. **States Included**  
8. **Primary Managing Agency**  
9. **Secondary Managing Agencies**  
10. **URL**  
11. **Map URL**  
12. **Notes**  
13. **Derived Label** *(computed during normalization)*  

This order is absolute and must never change.

------------------------------------------------------------
# 3. FIELD‑BY‑FIELD RULES

## 3.1 Trail Network Name
- Use the official published name.  
- Must be unique statewide.  
- Uniqueness is **case‑insensitive**.  
- Must not include unofficial descriptors.  
- Must not duplicate or synonymize another Trail Network name.  
- Must not encode hierarchy or governance.

## 3.2 Alternate Names
- Optional.  
- Semicolon‑delimited list.  
- Include only documented historical or variant names.  
- Must not include marketing names or slogans.  
- Must not include abbreviations unless documented.

## 3.3 Network Type
- Must match a value from the Trail Network Vocabulary Module v4.0.  
- Describes the identity‑bearing classification of the network.  
- Must not encode governance, hierarchy, or temporary conditions.  
- Must not encode geographic scope beyond what is inherent in the identity.

## 3.4 Description
- 1–3 sentences.  
- Must describe identity‑defining characteristics of the Trail Network.  
- Must not include Trail‑level or Segment‑level details.  
- Must not include amenities or temporary conditions.

## 3.5 History
- Optional.  
- May include origin, development history, or major changes.  
- Must be factual and sourced.  
- Must not include speculative or inferred history.

## 3.6 County List
- Semicolon‑delimited list.  
- Alphabetical order.  
- Must include all counties through which any part of the network passes.  
- Must not include the word “County.”  
- Must follow the **v4.0 universal multi‑county rule**:  
  - One entity per network  
  - Alphabetized, semicolon‑delimited list  
  - No segmentation of multi‑county entities  
  - No inferred counties  

## 3.7 States Included
- Optional.  
- Semicolon‑delimited list.  
- Alphabetical order.  
- Only used for multi‑state networks.  
- Must not include inferred states.

## 3.8 Primary Managing Agency
- The primary agency responsible for the Trail Network.  
- Must be an authoritative agency name.  
- Must not be inferred.  
- Must not encode governance hierarchy.

## 3.9 Secondary Managing Agencies
- Optional.  
- Semicolon‑delimited list.  
- Include only documented co‑managers.  
- Must not duplicate the primary agency.  
- Must not include inferred partners.

## 3.10 URL
- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must reference authoritative sources.  
- Tracking parameters must be removed.

## 3.11 Map URL
- Full `https://` URL to an authoritative map or GIS viewer.  
- May include PDF maps, static images, or interactive GIS layers.  
- Semicolon‑delimit if multiple.  
- Leave blank if none.

## 3.12 Notes
- Optional free‑text field.  
- Must not include identity‑defining characteristics.  
- Use for clarifications, temporary conditions, or contextual notes.  
- Must not include Trail‑level or Segment‑level details.

## 3.13 Derived Label
- Computed during normalization (v4.0).  
- Not stored in the database.  
- Formula defined in the Trail Network Normalization Contract v4.0.  
- Must be deterministic and based solely on normalized fields.  
- Must not include parentheses, punctuation, or additional descriptors.

------------------------------------------------------------
# 4. IDENTITY RULES

A Trail Network is valid only if:
- It is an identity‑bearing umbrella entity composed of multiple Trails.  
- It is documented in authoritative sources.  
- It is distinct from its member Trails.  
- It is not merely a marketing label or informal grouping.  
- It does **not** have a parent Trail Network (v4.0 ontology rule).  
- It does **not** serve as a parent for Trail Segments or Access Points.  
- It is not a synthetic or inferred network.  

If any of these conditions fail, the Trail Network must not be created.

------------------------------------------------------------
# 5. MODULE DEPENDENCIES

This module depends on:

- **Trail Network Vocabulary Module v4.0**  
- **Trail Network Normalization Contract v4.0**  
- **Trail Schema Module v4.0**  
- **Trail Segment Schema Module v4.0**  
- **TSV Output Specification (Trail Networks) v4.0**  
- **Resolution Engine v4.0**  
- **Discovery Protocol Module v4.0**  

All other modules must reference this schema.

------------------------------------------------------------
# END OF TRAIL NETWORK SCHEMA MODULE v4.0