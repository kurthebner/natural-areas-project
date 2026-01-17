# NATURAL AREAS PROJECT — SITE NETWORK SCHEMA MODULE v1
Authoritative, versioned schema for Site Networks in the statewide Natural Areas & Trails system.

This module defines:
- The Site Network entity type
- The Site Network fields and authoritative field order
- Field‑level rules
- Dependencies on the Site Network Vocabulary Module v1

This module contains no controlled vocabularies.
All vocabularies are defined in the Site Network Vocabulary Module v1.

------------------------------------------------------------
# 1. PURPOSE
Site Networks are identity‑bearing umbrella entities that group multiple Sites into a coherent system.
Examples include National Heritage Areas, Local Historic Districts, Scenic River Corridors, and other
multi‑site cultural, historical, or ecological networks.

This schema:
- Establishes the Site Network record structure
- Defines field‑level rules
- Ensures consistency across all counties and data sources
- Provides the foundation for Site Network normalization, discovery, resolution, and TSV output

This module is authoritative for Site Network structure.

------------------------------------------------------------
# 2. SITE NETWORK FIELDS (AUTHORITATIVE ORDER)

1. Site Network Name
2. Alternate Names
3. Network Type
4. Description
5. History
6. Counties Included
7. States Included
8. Managing Agency (Primary)
9. Managing Agencies (Secondary)
10. URL
11. Map Link
12. Notes
13. Source Confidence
14. Verification Status
15. Field Confidence Map
16. Field Verification Map

This order is absolute and must never change.

------------------------------------------------------------
# 3. FIELD‑BY‑FIELD RULES

## 3.1 Site Network Name
- Use the official published name.
- Must be unique statewide.
- Must not include unofficial descriptors.

## 3.2 Alternate Names
- Optional.
- Comma‑separated or JSON array.
- Include only documented historical or variant names.

## 3.3 Network Type
- Must match a value from the Site Network Vocabulary Module v1.
- Describes the classification of the network (e.g., National Heritage Area, Local Historic District,
  Scenic River Corridor).
- Must not encode governance or temporary conditions.

## 3.4 Description
- 1–3 sentences.
- Must describe identity‑defining characteristics of the Site Network.
- Must not include site‑level details.

## 3.5 History
- Dedicated field for historical context.
- May include origin, development history, or major changes.
- Must be factual and sourced.

## 3.6 Counties Included
- Semicolon‑delimited list.
- Alphabetical order.
- Must include all counties through which any part of the network passes.
- Must not include the word “County.”

## 3.7 States Included
- Optional.
- Semicolon‑delimited list.
- Alphabetical order.
- Only used for multi‑state networks.

## 3.8 Managing Agency (Primary)
- The primary agency responsible for the Site Network.
- Must be an authoritative agency name.
- Do not infer.

## 3.9 Managing Agencies (Secondary)
- Optional.
- Semicolon‑delimited or JSON array.
- Include only documented co‑managers.

## 3.10 URL
- Full https:// URLs only.
- Semicolon‑delimit if multiple.
- Must reference authoritative sources.

## 3.11 Map Link
- Optional.
- Must be an authoritative map or GIS viewer link.

## 3.12 Notes
- Optional free‑text field.
- Must not include identity‑defining characteristics.
- Use for clarifications, temporary conditions, or contextual notes.

## 3.13 Source Confidence
- High / Medium / Low.
- Represents overall confidence in the Site Network record.

## 3.14 Verification Status
- Verified / Needs Review / Removed.
- Represents the current verification state of the Site Network record.

## 3.15 Field Confidence Map
- JSON object.
- Per‑field confidence values.
- Must follow the structure defined in the Normalization Contract.

## 3.16 Field Verification Map
- JSON object.
- Per‑field verification values.
- Must follow the structure defined in the Normalization Contract.

------------------------------------------------------------
# 4. IDENTITY RULES
A Site Network is valid only if:
- It is an identity‑bearing umbrella entity composed of multiple Sites.
- It is documented in authoritative sources.
- It is distinct from its member Sites.
- It is not merely a marketing label or informal grouping.

If any of these conditions fail, the Site Network must not be created.

------------------------------------------------------------
# 5. MODULE DEPENDENCIES
This module depends on:

- Site Network Vocabulary Module v1
  (for Network Type)

All other modules (Normalization, TSV Output, Discovery, Resolution, Orchestration)
must reference this schema.

------------------------------------------------------------
# END OF SITE NETWORK SCHEMA MODULE v1