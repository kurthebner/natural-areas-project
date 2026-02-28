# NATURAL AREAS PROJECT
# SITE SCHEMA MODULE v5.0
(Authoritative Structure, Semantic Rules, Identity Anchors, and Validation Requirements for Site Entities)

This module defines the authoritative **v5.0 Site Schema**, combining:

- Storage-oriented field definitions (Entity Graph-aligned)
- Ontological and semantic field-level rules
- Identity anchors (strict)
- Identity signatures (composite, practical)
- Relationship rules
- Validation rules
- Provenance expectations

This module contains **no controlled vocabularies**.
All vocabularies are defined in the **Site Vocabulary Module v5.0**.

This module is authoritative for the structure and semantics of **Site** entities.

------------------------------------------------------------
# CHANGES FROM v4.0

- `address` removed — merged into `location` (universal field)
- `location` retained as universal geographic reference field
- `gps_primary` replaced by `gps_lat` and `gps_lon` (numeric)
- `network_affiliation` removed — membership tracked via relationship tables
- `source_primary` and `source_all` removed — provenance tracked via provenance tables
- `geometry` removed from normalized schema — populated in GIS phase only
- `url_primary` retained; `url_all` replaced by `urls` array
- `county_list` renamed to `counties`
- `municipality` and `township` retained — populated via GIS spatial lookup during normalization, not during discovery
- `features` retained as semicolon-delimited list (no categorization)
- Identity signature updated to reflect removed fields
- `run_id` removed from normalized schema — tracked in provenance tables

------------------------------------------------------------
# 1. PURPOSE

A **Site** is a named, bounded, identity-bearing land unit documented in authoritative sources.
Examples include parks, preserves, natural areas, historic sites, cemeteries, campuses,
recreation areas, wildlife areas, forests, and conservation lands.

A Site may be:

- A **top-level** identity-bearing land unit, or
- A **child Site** (a named, identity-bearing unit within a parent Site), represented by `parent_site_id`

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

This value is fixed and non-optional.

------------------------------------------------------------
# 3. IDENTITY MODEL (ANCHOR + SIGNATURE)

## 3.1 Identity Anchor (strict, minimal, ontological)

The identity anchor defines the **true identity** of a Site.
It must be stable, non-inferential, and derivable from authoritative sources.

### Top-Level Sites
`entity_type = "Site"`
`name`
`counties`

### Child Sites
`entity_type = "Site"`
`name`
`counties`
`parent_site_id`

These fields alone define the ontological identity of a Site.

## 3.2 Identity Signature (composite, practical)

The identity signature is a collection of fields that, taken together, help distinguish
similarly-named Sites and prevent accidental merges.

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
- coordination
- url_primary
- urls

These fields:

- are **not** identity-defining
- **may** be missing
- **may** be insufficient alone
- **collectively** help distinguish entities
- are used by the Resolution Engine v5.0 for matching confidence
- are preserved by the Normalization Engine v5.0

------------------------------------------------------------
# 4. FIELD DEFINITIONS (STORAGE-ORIENTED)

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
- Type: semicolon-delimited string
- Optional
- Must match Designation vocabulary

## 4.6 `status`
- Type: string
- Optional
- Must match Status vocabulary

## 4.7 `ownership`
- Type: string
- Optional
- Must contain the actual legal name of the owning entity
- Must not use generic categories (e.g., "State Government")
- Must not encode management, governance, or designation
- Must be supported by authoritative documentation

## 4.8 `governance`
- Type: semicolon-delimited string
- Optional
- Must contain the actual name(s) of the managing organization(s)
- Must not use generic categories (e.g., "Municipal Agency")
- Must not encode ownership or designation
- Must be explicitly documented

## 4.9 `coordination`
- Type: semicolon-delimited string
- Optional
- Must contain the actual names of documented partner organizations
- Must not use generic categories
- Must not duplicate Ownership or Governance
- Must be supported by authoritative documentation

## 4.10 `description`
- Type: string
- Optional

## 4.11 `location`
- Type: string
- Optional
- Universal geographic reference field
- Accepts full street address OR general geographic description
- Examples: "18331 Carter Road, Bowling Green, OH 43402"
           "Mile marker 47 on State Route 6"
           "East shore of Metzger Marsh, north of State Route 2"

## 4.12 `acres`
- Type: numeric
- Optional

## 4.13 `counties`
- Type: array (JSON) / semicolon-delimited string (TSV)
- Required
- Alphabetical order
- Must not include the word "County"

## 4.14 `municipality`
- Type: semicolon-delimited string
- Optional
- Populated via GIS spatial lookup during normalization
- Not collected during web discovery
- Represents the municipality (city or village) in which the Site resides

## 4.15 `township`
- Type: semicolon-delimited string
- Optional
- Populated via GIS spatial lookup during normalization
- Not collected during web discovery
- Represents the civil township in which the Site resides

## 4.16 `gps_lat`
- Type: numeric (decimal degrees, WGS84)
- Optional during discovery
- Required before inclusion in statewide database
- Must not be invented or inferred

## 4.17 `gps_lon`
- Type: numeric (decimal degrees, WGS84)
- Optional during discovery
- Required before inclusion in statewide database
- Must not be invented or inferred

## 4.18 `plus_code`
- Type: string
- Optional
- Derived from accepted gps_lat and gps_lon values
- Required once GPS is present
- Blank if GPS is blank

## 4.19 `features`
- Type: semicolon-delimited string
- Optional
- Must match Features vocabulary
- Flat list, no categorization
- Metadata may appear in parentheses: "restrooms (ADA accessible)"

## 4.20 `notes`
- Type: string
- Optional

## 4.21 `url_primary`
- Type: string
- Optional
- Full https:// URL to primary authoritative source

## 4.22 `urls`
- Type: array (JSON) / semicolon-delimited string (TSV)
- Optional
- Additional URLs beyond url_primary
- May include non-official sources of value

## 4.23 `parent_site_id`
- Type: integer (FK to `sites.site_id`)
- Optional
- Required for child Sites

## 4.24 `created_at`
- Type: timestamp
- Required

## 4.25 `updated_at`
- Type: timestamp
- Required

------------------------------------------------------------
# 5. FIELD-LEVEL SEMANTIC RULES (ONTOLOGY-ORIENTED)

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
- Must match Category-dependent subtype lists
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

## 5.6 Governance
- Represents **operational control**
- Must use the exact name(s) of the managing organization(s)
- Multiple managers allowed only if formally documented
- Must not encode ownership, category, designation, or access rules
- Must be explicitly documented

## 5.7 Coordination
- Represents **documented partnerships**
- Must use exact names of partner organizations
- Must not duplicate Ownership or Governance
- Must not encode category, designation, access rules, or temporary volunteer activity
- Must be supported by authoritative documentation

## 5.8 Description
- Identity-defining ecological, cultural, historical, or physical character
- 1-3 sentences
- Must not include governance, ownership, designation, parcel IDs, URLs, or operational nuance
- Must not contradict controlled fields

## 5.9 Status
- Must be explicitly documented
- Must not be inferred from imagery
- "Closed" = permanently closed
- "Proposed" must be officially referenced

## 5.10 Location
- Universal geographic reference field
- Use full street address when available
- Use general geographic description when address unavailable
- Must not include county names
- Must not encode governance or access rules

## 5.11 Acres
- Numeric only
- No estimates or ranges

## 5.12 Counties
- Alphabetical
- Array in JSON; semicolon-delimited in TSV
- Multi-county Sites must have one record
- Must not include the word "County"

## 5.13 Municipality
- Must represent the city or village in which the Site resides
- Populated via GIS spatial lookup — never invented or guessed
- Blank if unverifiable or outside any municipality

## 5.14 Township
- Must represent the civil township in which the Site resides
- Populated via GIS spatial lookup — never invented or guessed
- Blank if unverifiable

## 5.15 GPS
- gps_lat and gps_lon must represent a single authoritative coordinate pair
- No placeholders
- No unverifiable coordinates
- Both must be present or both must be blank

## 5.16 Plus Code
- Derived from normalized gps_lat and gps_lon only
- Never manually entered

## 5.17 Features
- Internal components only
- Must match vocabulary values
- Trails, Trail Segments, Access Points, and Child Sites are never Features
- Semicolon-delimited flat list; no categorization
- Metadata in parentheses permitted: "picnic tables (6)"

## 5.18 Notes
- Context, not identity
- Must not contradict controlled fields
- Must not contain identity-bearing information
- May include clarifications, exceptions, boundary notes, access nuance,
  historical names, parcel IDs, citations, URLs

## 5.19 URLs
- Must be authoritative or documented
- Full https:// URLs only
- url_primary = primary authoritative source
- urls = additional sources of value (may include non-official)

## 5.20 Parent Site
- Must be explicitly documented
- Must not be inferred from signage or layout
- Must not represent Trails or Access Points

------------------------------------------------------------
# 6. DISCOVERY PHASE NOTE

The following fields are **not collected during web discovery**:

- `gps_lat`, `gps_lon` — assigned via batch geocoding post-discovery
- `plus_code` — computed from GPS coordinates
- `municipality` — derived via GIS spatial lookup during normalization
- `township` — derived via GIS spatial lookup during normalization

Discoverers should leave these fields blank. They are populated in
subsequent pipeline phases.

------------------------------------------------------------
# 7. IDENTITY RULES

A Site is valid only if:

- It is named
- It is bounded
- It is identity-bearing
- It is documented in authoritative sources
- It is not a Trail, Trail Segment, Access Point, Trail Network, or Site Network
- It is not merely a feature or amenity
- If `parent_site_id` is populated, the Site must follow **Child Site Rules Module v5.0**

**Core distinction:**
- **Description = identity**
- **Notes = context**

------------------------------------------------------------
# 8. RELATIONSHIP RULES

### 8.1 Parent Site
- Zero or one parent
- Must follow Child Site Rules Module v5.0
- Must reference a valid Site ID
- Must not create cycles

### 8.2 Network Membership
- Network membership stored in `site_network_members` relationship table
- Queryable both ways: all Sites in a network; all networks for a Site
- Not encoded as a field in the Site record

------------------------------------------------------------
# 9. VALIDATION RULES

Normalization Engine v5.0 must validate:

- Required fields present
- Vocabulary-controlled fields valid
- Semicolon formatting for multi-value fields
- GPS format: both lat and lon present, or both blank
- Numeric types: gps_lat, gps_lon, acres
- Plus Code generation from GPS
- No invented data
- No placeholder values
- No delimiter characters inside fields
- Parent Site validity
- Identity anchor integrity
- Ownership, Governance, and Coordination use real names, not categories

------------------------------------------------------------
# 10. PROVENANCE RULES

Provenance is stored in:

- `discovery_provenance`
- `resolution_provenance`
- `normalization_provenance`

Normalization Engine v5.0 must populate these tables.

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- Site Vocabulary Module v5.0
- Child Site Rules Module v5.0
- Discovery Output Specification v5.0
- Discovery Metadata Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Graph Schema v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF SITE SCHEMA MODULE v5.0
