# NATURAL AREAS PROJECT  
# SITE SCHEMA MODULE v4.0  
(Authoritative Structure, Semantic Rules, Identity Anchors, and Validation Requirements for Site Entities)

This module defines the authoritative **v4.0 Site Schema**, combining:

- Storage‑oriented field definitions (Entity Graph–aligned)  
- Ontological and semantic field‑level rules  
- Identity anchors (strict)  
- Identity signatures (composite, practical)  
- Relationship rules  
- Validation rules  
- Provenance expectations  

This module contains **no controlled vocabularies**.  
All vocabularies are defined in the **Site Vocabulary Module v4.0**.

This module is authoritative for the structure and semantics of **Site** entities.

------------------------------------------------------------
# 1. PURPOSE

A **Site** is a named, bounded, identity‑bearing land unit documented in authoritative sources.  
Examples include parks, preserves, natural areas, historic sites, cemeteries, campuses, recreation areas, wildlife areas, forests, and conservation lands.

A Site may be:

- A **top‑level** identity‑bearing land unit, or  
- A **child Site** (a named, identity‑bearing unit within a parent Site), represented by `parent_site_id`

This schema:

- Defines the authoritative field list for normalized Site entities  
- Encodes the ontological meaning of Category, Subtype, Designation, and Status  
- Defines semantic rules for Description, Features, Notes, and Location  
- Establishes identity anchors and identity signatures  
- Ensures consistency across all counties and data sources  
- Provides the foundation for discovery, resolution, normalization, upsert, and TSV output  

------------------------------------------------------------
# 2. ENTITY TYPE

All entities conforming to this schema must have:  
`entity_type = "Site"`

This value is fixed and non‑optional.

------------------------------------------------------------
# 3. IDENTITY MODEL (ANCHOR + SIGNATURE)

## 3.1 Identity Anchor (strict, minimal, ontological)

The identity anchor defines the **true identity** of a Site.  
It must be stable, non‑inferential, and derivable from authoritative sources.

### Top‑Level Sites
`entity_type = "Site"`  
`name`  
`county_list`

### Child Sites
`entity_type = "Site"`  
`name`  
`county_list`  
`parent_site_id`

These fields alone define the ontological identity of a Site.

---

## 3.2 Identity Signature (composite, practical)

The identity signature is a **collection of fields** that, taken together, help distinguish similarly‑named Sites and prevent accidental merges.

Identity signature fields include:

- name  
- county_list  
- category  
- subtype  
- designation  
- municipality  
- township  
- ownership  
- governance  
- coordination  
- network_affiliation  
- url_primary  
- url_all  
- source_primary  
- source_all  

These fields:

- are **not** identity‑defining  
- **may** be missing  
- **may** be insufficient alone  
- **collectively** help distinguish entities  
- are used by the Resolution Engine v4.0 for matching confidence  
- are preserved by the Normalization Engine v4.0  

------------------------------------------------------------
# 4. FIELD DEFINITIONS (STORAGE‑ORIENTED)

Each field includes:  
- Type  
- Required/Optional  
- Constraints  

---

## 4.1 `site_id`
- Type: integer (surrogate key)  
- Required for storage (assigned by Upsert Engine)

## 4.2 `name`
- Type: string  
- Required

## 4.3 `category`
- Type: string  
- Optional  
- Must match Category vocabulary

## 4.4 `subtype`
- Type: string  
- Optional  
- Must match Subtype vocabulary for the selected Category

## 4.5 `designation`
- Type: semicolon‑delimited string  
- Optional  
- Must match Designation vocabulary

## 4.6 `status`
- Type: string  
- Optional  
- Must match Status vocabulary

## 4.7 `ownership`
- Type: string  
- Optional  
- Must contain the **actual legal name** of the owning entity  
- Must not use generic categories (e.g., “State Government”)  
- Must not encode management, governance, or designation  
- Must be supported by authoritative documentation

## 4.8 `governance`
- Type: semicolon‑delimited string  
- Optional  
- Must contain the **actual name(s)** of the managing organization(s)  
- Must not use generic categories (e.g., “Municipal Agency”)  
- Must not encode ownership or designation  
- Must be explicitly documented

## 4.9 `coordination`
- Type: semicolon‑delimited string  
- Optional  
- Must contain the **actual names** of documented partner organizations  
- Must not use generic categories  
- Must not duplicate Ownership or Governance  
- Must be supported by authoritative documentation

## 4.10 `network_affiliation`
- Type: semicolon‑delimited string  
- Optional

## 4.11 `description`
- Type: string  
- Optional

## 4.12 `address`
- Type: string  
- Optional

## 4.13 `acres`
- Type: numeric  
- Optional

## 4.14 `location`
- Type: string  
- Optional  
- Human‑readable, non‑authoritative

## 4.15 `municipality`
- Type: semicolon‑delimited string  
- Optional

## 4.16 `township`
- Type: semicolon‑delimited string  
- Optional

## 4.17 `county_list`
- Type: semicolon‑delimited string  
- Required

## 4.18 `gps_primary`
- Type: string (`lat,lon`)  
- Optional

## 4.19 `plus_code`
- Type: string  
- Optional

## 4.20 `features`
- Type: semicolon‑delimited string  
- Optional  
- Must match Features vocabulary

## 4.21 `notes`
- Type: string  
- Optional

## 4.22 `url_primary`
- Type: string  
- Optional

## 4.23 `url_all`
- Type: semicolon‑delimited string  
- Optional

## 4.24 `parent_site_id`
- Type: integer (FK to `sites.site_id`)  
- Optional

## 4.25 `geometry`
- Type: WKT or SpatiaLite geometry blob  
- Optional

## 4.26 `source_primary`
- Type: string  
- Optional

## 4.27 `source_all`
- Type: semicolon‑delimited string  
- Optional

## 4.28 `created_at`
- Type: timestamp  
- Required

## 4.29 `updated_at`
- Type: timestamp  
- Required

## 4.30 `run_id`
- Type: integer (FK to `run_metadata.run_id`)  
- Required

------------------------------------------------------------
# 5. FIELD‑LEVEL SEMANTIC RULES (ONTOLOGY‑ORIENTED)

## 5.1 Name
- Must be the official published name  
- Must not include descriptive or unofficial names  
- Must not append Category/Subtype/Designation unless official  
- Must not be inferred from amenities or features

## 5.2 Category
- Expresses what the Site *is* at the highest ontological level  
- Must match vocabulary values  
- Must not encode governance, ownership, or temporary conditions

## 5.3 Subtype
- Optional  
- Must match Category‑dependent subtype lists  
- Must not describe habitat, features, or temporary states

## 5.4 Designation
- Formal legal or administrative status  
- Must be explicitly documented  
- Must not duplicate Category or Subtype  
- Must not encode ownership, governance, or temporary conditions  
- Must not include marketing or informal labels

## 5.5 Ownership
- Represents **legal title**  
- Must use the exact legal name of the owning entity  
- Must not use generic categories  
- Must not encode management, governance, designation, or temporary conditions  
- Must not be inferred from signage alone  
- Must be supported by authoritative documentation

## 5.6 Governance (Management)
- Represents **operational control**  
- Must use the exact name of the managing organization  
- Must not encode ownership, category, designation, or access rules  
- Must be explicitly documented  
- Multiple managers allowed only if formally documented

## 5.7 Coordination
- Represents **documented partnerships**  
- Must use the exact names of partner organizations  
- Must not duplicate Ownership or Governance  
- Must not encode category, designation, access rules, or temporary volunteer activity  
- Must be supported by authoritative documentation

## 5.8 Network Affiliation
- Must be formally documented  
- Must not encode hierarchy, ownership, or parentage  
- Must not imply parent–child relationships

## 5.9 Description
- Identity‑defining ecological, cultural, historical, or physical character  
- 1–3 sentences  
- Must not include governance, ownership, designation, parcel IDs, URLs, or operational nuance  
- Must not contradict controlled fields

## 5.10 Status
- Must be explicitly documented  
- Must not be inferred from imagery  
- “Closed” = permanently closed  
- “Proposed” must be officially referenced

## 5.11 Address
- Must not include invented numbers  
- Must not include coordinates

## 5.12 Acres
- Numeric only  
- No estimates or ranges

## 5.13 Location
- Human‑readable geographic reference  
- Must not include county names  
- Must not include identity‑bearing terms  
- Must not include governance or access rules  
- Must not include full addresses or coordinates

## 5.14 County List
- Alphabetical  
- Semicolon‑delimited  
- Multi‑county Sites must have one record

## 5.15 GPS Coordinates
- One authoritative pair only  
- No placeholders  
- No unverifiable coordinates

## 5.16 Plus Code
- Derived from normalized GPS only

## 5.17 Features
- Internal components only  
- Must match vocabulary values  
- Trails, Trail Segments, Access Points, and Sub‑Sites are never Features

## 5.18 Notes
- Context, not identity  
- Must not contradict controlled fields  
- Must not contain identity‑bearing information  
- May include clarifications, exceptions, boundary notes, access nuance, historical names, parcel IDs, citations, URLs

## 5.19 URLs
- Must be authoritative  
- Full https:// URLs only

## 5.20 Parent Site
- Must be explicitly documented  
- Must not be inferred from signage or layout  
- Must not represent Trails or Access Points

------------------------------------------------------------
# 6. IDENTITY RULES

A Site is valid only if:

- It is named  
- It is bounded  
- It is identity‑bearing  
- It is documented in authoritative sources  
- It is not a Trail, Trail Segment, Access Point, Trail Network, or Site Network  
- It is not merely a feature or amenity  
- If `parent_site_id` is populated, the Site must follow **Child Site Rules Module v4.0**

**Core distinction:**  
- **Description = identity**  
- **Notes = context**

------------------------------------------------------------
# 7. RELATIONSHIP RULES

### 7.1 Parent Site
- Zero or one parent  
- Must follow Child Site Rules Module v4.0  
- Must reference a valid Site ID  
- Must not create cycles

### 7.2 Networks
- Network affiliation does not imply parentage  
- Network membership stored in relationship tables

------------------------------------------------------------
# 8. VALIDATION RULES

Normalization Engine v4.0 must validate:

- Required fields present  
- Vocabulary‑controlled fields valid  
- Semicolon formatting  
- GPS format  
- Plus Code generation  
- No invented data  
- No placeholder values  
- No delimiter characters inside fields  
- Parent Site validity  
- Identity anchor integrity  
- Ownership, Governance, and Coordination use **real names**, not categories

------------------------------------------------------------
# 9. PROVENANCE RULES

Provenance is stored in:

- `discovery_provenance`  
- `resolution_provenance`  
- `normalization_provenance`

Normalization Engine v4.0 must populate these tables.

------------------------------------------------------------
# 10. MODULE DEPENDENCIES

This module depends on:

- Site Vocabulary Module v4.0  
- Child Site Rules Module v4.0  
- Discovery Output Specification v4.0  
- Discovery Metadata Specification v4.0  
- Resolution Engine v4.0  
- Normalization Engine v4.0  
- Entity Graph Schema v4.0  
- Audit & Logging Module v4.0  

------------------------------------------------------------
# END OF SITE SCHEMA MODULE v4.0