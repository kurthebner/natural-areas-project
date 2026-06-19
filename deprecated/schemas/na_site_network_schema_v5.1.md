# NATURAL AREAS PROJECT
# SITE NETWORK SCHEMA MODULE v5.1
(Authoritative Structure, Semantic Rules, and Validation Requirements for Site Network Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Site Network Vocabulary Module v5.x**.

This module is authoritative for the structure and semantics of **Site Network** entities.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Derived Label removed**: No longer computed or stored — presentation-layer concern only
- **Map URL removed**: Map URLs now captured in urls_raw at discovery stage and url at normalized stage
- **identity_notes added**: Separate normalized field for identity clarifications, distinct from notes
- **Field count corrected**: Header now correctly states 15 fields (was incorrectly stated as 13)
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `alternate_names` removed — rarely documented; variants noted in description
- `history` removed — merged into description
- `network_affiliation` removed — cleaner architecture without nested network affiliations
- `counties_traversed` renamed to `counties` (array)
- `primary_managing_agency` renamed to `governance`
- `secondary_managing_agencies` renamed to `partner_agencies`
- `ownership` added (who legally owns or established the network)
- `member_count` added (number of member Sites)
- `member_site_ids` added (array linking to member Site IDs)

------------------------------------------------------------
# 1. PURPOSE

A **Site Network** is a named, identity-bearing umbrella entity composed of
multiple Sites, documented in authoritative sources and distinct from:

- Individual Sites
- Trails and Trail Networks
- Access Points
- Trail Segments

Examples include:
- National Heritage Areas
- Local Historic Districts
- Scenic River Corridors
- Watershed-scale conservation networks
- County park district systems (when explicitly branded as a unified system)
- Municipal park systems (when explicitly branded as a unified system)
- Land trust preserve networks
- Multi-site conservation or cultural systems

**Identity threshold**: A Site Network requires explicit system-level identity —
the organization or designation must present itself as a named system or network
in authoritative sources, not merely manage multiple sites. Evidence includes:
a system name distinct from the managing organization's name, a system map, a
membership or passport program, or explicit "X parks in the Y system" language.

When uncertain whether a candidate meets this threshold, err on the side of
inclusion and flag with `SITE_NETWORK_UNCERTAIN` for Resolution to arbitrate.

This schema is authoritative for **Site Network structure**.

------------------------------------------------------------
# 2. SITE NETWORK FIELDS (15 FIELDS, AUTHORITATIVE ORDER)

1.  **Network Name**
2.  **Network Type**
3.  **Status**
4.  **Ownership**
5.  **Governance**
6.  **Partner Agencies**
7.  **Counties**
8.  **States Included**
9.  **Member Count**
10. **Member Site IDs**
11. **Description**
12. **Identity Notes**
13. **Notes**
14. **URL**
15. **Network ID**

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Network Name
- Use the official published name.
- Must be unique statewide (case-insensitive).
- Must not include unofficial descriptors.
- Must align with identity determined by the Resolution Engine v5.x.

## 3.2 Network Type
- Must match a value from the Site Network Vocabulary Module v5.x.
- Must describe the identity-bearing classification of the network.
- Must not encode governance, ownership, or hierarchy.
- Must not be inferred.

## 3.3 Status
- Must match a value from the Site Network Vocabulary Module v5.x.
- "Proposed" and "Dissolved" must be explicitly documented.
- Must not be inferred.

## 3.4 Ownership
- Optional.
- Must contain the actual legal name of the entity that owns or
  legally established the network.
- Must not use generic categories (e.g., "County Government").
- Must not encode management or governance.
- Must be supported by authoritative documentation.
- Blank if ownership is distributed among member sites, if the network
  is a coordinating or designating body without land ownership, or if unclear.
- Blank is correct and common for formally designated networks
  (NHAs, scenic river corridors, heritage corridors).

## 3.5 Governance
- The primary agency or organization responsible for coordinating
  or managing the network.
- Must be an authoritative name.
- Must not be inferred.
- Must not use generic categories.

## 3.6 Partner Agencies
- Optional.
- Semicolon-delimited list of secondary managing agencies or
  documented organizational partners.
- Must not duplicate Governance.
- Must not include inferred partners.

## 3.7 Counties
- Array in JSON; semicolon-delimited in TSV.
- Alphabetical order.
- Must include all counties through which any part of the network passes.
- Must not include the word "County."
- Must follow the universal multi-county rule: one Site Network record
  regardless of number of counties.

## 3.8 States Included
- Optional.
- Array in JSON; semicolon-delimited in TSV.
- Alphabetical order.
- Only used for multi-state networks.
- Leave blank for Ohio-only networks.
- Must not be inferred.

## 3.9 Member Count
- Optional but strongly recommended.
- Integer representing the number of member Sites.
- Record the officially published count when available.
- May be estimated from enumerated member list if not published.
- Blank if truly unknown.

## 3.10 Member Site IDs
- Optional.
- Array of site_id values referencing normalized Site entities.
- Populated during normalization as member Sites are resolved.
- May be incomplete during initial discovery — added incrementally.
- Supports bidirectional querying via the site_network_members relationship table.

## 3.11 Description
- 1-3 sentences describing the network's identity, scope, and purpose.
- May include brief establishment history or origin context.
- Must not include site-level details.
- Must not include Access Point or Trail details.

## 3.12 Identity Notes
- Optional free-text field for identity clarifications.
- Use for: disambiguation notes, alternate names, system identity uncertainty,
  governance verification notes, flag rationale.
- Must not duplicate Description.
- Must not include operational or contextual notes (those go in Notes).

## 3.13 Notes
- Optional free-text field for operational and contextual notes.
- Use for: funding notes, boundary clarifications, designation history,
  partnership context, discovery gaps.
- Must not include identity-defining characteristics (those go in Description
  or Identity Notes).
- Must not include site-level or trail-level details.

## 3.14 URL
- Full https:// URL to the primary authoritative network page.
- Semicolon-delimit if multiple authoritative URLs exist, including
  any map URLs (system-wide maps, GIS viewers, PDF maps).
- Must not include placeholders or inferred URLs.

## 3.15 Network ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- Must be a valid integer matching the entity's network_id.
- Enables joins to the site_network_members relationship table.

------------------------------------------------------------
# 4. IDENTITY RULES

A Site Network is valid only if:

- It is explicitly documented as a multi-site system, OR
- A managing organization presents its holdings as a unified system
  with a name, map, or programmatic identity in authoritative sources.
- It has a stable, identity-bearing name.
- It is composed of two or more Sites.
- It is distinct from its member Sites.
- It is not merely a marketing label or informal grouping.
- It satisfies the identity rules in the Resolution Engine v5.x.
- It does **not** have a parent Site Network.
- It does **not** serve as a parent for Trails, Trail Segments, or Access Points.

When uncertain, include the candidate and flag with:
`SITE_NETWORK_UNCERTAIN — governance body or identity-bearing system;
verify system-level branding before final classification`

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Member Sites
- Membership stored in `site_network_members` relationship table:
  - `network_id` (FK to site_networks)
  - `site_id` (FK to sites)
- `member_site_ids` field is a convenience cache of site_id values
  from this table.
- Queryable both ways:
  - All Sites in a network: `SELECT site_id FROM site_network_members WHERE network_id = X`
  - All networks for a Site: `SELECT network_id FROM site_network_members WHERE site_id = Y`

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- Site Network Vocabulary Module v5.x
- Site Network Normalization Contract v5.x
- Site Network TSV Output Specification v5.x
- Site Network Discovery Sub-Procedure v5.x
- Resolution Engine v5.x
- Discovery Protocol Module v5.x

------------------------------------------------------------
# END OF SITE NETWORK SCHEMA MODULE v5.1
