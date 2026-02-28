# NATURAL AREAS PROJECT
# SITE SCHEMA MODULE v5.2
(Authoritative Structure, Semantic Rules, Identity Anchors, and Validation Requirements for Site Entities)

This module defines the authoritative v5.2 Site Schema, combining:

- Storage-oriented field definitions (Entity Graph-aligned)
- Ontological and semantic field-level rules
- Identity anchors (strict)
- Identity signatures (composite, practical)
- Relationship rules
- Validation rules
- Provenance expectations

This module contains no controlled vocabularies.
All vocabularies are defined in the Site Vocabulary Module v5.x.

This module is authoritative for the structure and semantics of Site entities.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.2

- Added new field: partner_agencies
  - Represents formal, documented co‑operator organizations
  - Distinct from Ownership, Governance, and Coordination
  - Semicolon-delimited string
  - Must be supported by authoritative documentation
- Updated organizational field cluster to four-tier model:
  - ownership
  - governance
  - partner_agencies
  - coordination
- Updated field list, semantic rules, validation rules, and dependencies accordingly
- No breaking changes to identity anchor or identity signature
- No changes to discovery expectations

------------------------------------------------------------
# 1. PURPOSE

A Site is a named, bounded, identity-bearing land unit documented in authoritative sources. Examples include parks, preserves, natural areas, historic sites, cemeteries, campuses, recreation areas, wildlife areas, forests, and conservation lands.

A Site may be:
- A top-level identity-bearing land unit, or
- A child Site (a named, identity-bearing unit within a parent Site), represented by parent_site_id

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
entity_type = "Site"

This value is fixed and non-optional.

------------------------------------------------------------
# 3. IDENTITY MODEL (ANCHOR + SIGNATURE)

## 3.1 Identity Anchor (strict, minimal, ontological)

Top-Level Sites:
- entity_type
- name
- counties

Child Sites:
- entity_type
- name
- counties
- parent_site_id

These fields alone define the ontological identity of a Site.

## 3.2 Identity Signature (composite, practical)

Identity signature fields include:
- name
- counties
- category
- subtype
- designation
- municipality
- township
- ownership
- governance
- partner_agencies
- coordination
- url_primary
- urls

These fields help distinguish similarly-named Sites but do not define identity.

------------------------------------------------------------
# 4. FIELD DEFINITIONS (STORAGE-ORIENTED)

## 4.1 site_id
integer, required (assigned by Upsert Engine)

## 4.2 name
string, required

## 4.3 category
string, optional, must match vocabulary

## 4.4 subtype
string, optional, must match vocabulary for selected category

## 4.5 designation
semicolon-delimited string, optional, must match vocabulary

## 4.6 status
string, optional, must match vocabulary

## 4.7 ownership
string, optional, legal title holder

## 4.8 governance
semicolon-delimited string, optional, managing organization(s)

## 4.9 partner_agencies
NEW in v5.2
- semicolon-delimited string
- optional
- formal, documented co‑operator organizations
- must not duplicate Ownership or Governance
- must be supported by authoritative documentation

## 4.10 coordination
semicolon-delimited string, optional, community or informal partners

## 4.11 description
string, optional

## 4.12 location
string, optional, universal geographic reference

## 4.13 acres
numeric, optional

## 4.14 counties
array (JSON) / semicolon-delimited (TSV), required, alphabetical

## 4.15 municipality
semicolon-delimited string, optional, GIS-derived

## 4.16 township
semicolon-delimited string, optional, GIS-derived

## 4.17 gps_lat
numeric, optional during discovery, required before statewide inclusion

## 4.18 gps_lon
numeric, optional during discovery, required before statewide inclusion

## 4.19 plus_code
string, optional, derived from GPS

## 4.20 features
semicolon-delimited string, optional, must match vocabulary

## 4.21 notes
string, optional

## 4.22 url_primary
string, optional, authoritative URL

## 4.23 urls
array (JSON) / semicolon-delimited (TSV), optional

## 4.24 parent_site_id
integer, optional, FK to sites.site_id

## 4.25 created_at
timestamp, required

## 4.26 updated_at
timestamp, required

------------------------------------------------------------
# 5. FIELD-LEVEL SEMANTIC RULES

## 5.1 Ownership
Legal title only.

## 5.2 Governance
Operational control only.

## 5.3 Partner Agencies
NEW in v5.2
- Formal, documented co‑operators
- Must use exact organization names
- Must not include informal volunteer groups
- Must not duplicate Ownership or Governance

## 5.4 Coordination
Community-based, volunteer, advisory, or informal partners.

## 5.5–5.20
All other semantic rules remain unchanged from v5.0.

------------------------------------------------------------
# 6. DISCOVERY PHASE NOTE

GPS, plus_code, municipality, and township remain non-discovery fields.

------------------------------------------------------------
# 7. IDENTITY RULES

Identity anchor unchanged.
Partner Agencies does not affect identity.

------------------------------------------------------------
# 8. RELATIONSHIP RULES

Unchanged from v5.0.

------------------------------------------------------------
# 9. VALIDATION RULES

Normalization Engine v5.x must validate:
- Vocabulary-controlled fields
- Semicolon formatting
- GPS rules
- No invented data
- Organizational field separation:
  - ownership
  - governance
  - partner_agencies
  - coordination
- Partner Agencies must be supported by authoritative documentation

------------------------------------------------------------
# 10. PROVENANCE RULES

Unchanged from v5.0.

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:
- Site Vocabulary Module v5.x
- Child Site Rules Module v5.x
- Discovery Output Specification v5.x
- Discovery Metadata Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Graph Schema v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF SITE SCHEMA MODULE v5.2