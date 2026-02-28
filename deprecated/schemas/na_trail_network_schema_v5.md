# NATURAL AREAS PROJECT
# TRAIL NETWORK SCHEMA MODULE v5.0
(Authoritative Structure, Semantic Rules, and Validation Requirements for Trail Network Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Network Vocabulary Module v5.0**.

This module is authoritative for the structure and semantics of **Trail Network** entities.

------------------------------------------------------------
# CHANGES FROM v4.0

- `alternate_names` removed — rarely documented; variants noted in description
- `history` removed — merged into description
- `county_list` renamed to `counties` (array)
- `primary_managing_agency` renamed to `governance`
- `secondary_managing_agencies` renamed to `partner_agencies`
- `map_url` replaced by `maps` (rich array — Trail Networks are spatial; multiple map formats common)
- `status` added (was missing from v4.0 — clearly needed)
- `ownership` added (optional — meaningful for single-owner networks)
- `total_length_miles` added (optional — important metric, usually published)
- `member_trail_count` added (number of member Trails)
- `member_trail_ids` added (array linking to member Trail IDs)

------------------------------------------------------------
# 1. PURPOSE

A **Trail Network** is a named, identity-bearing umbrella entity composed of
multiple Trails. Examples include:

- Regional greenway systems
- National Scenic Trail systems
- Water trail networks
- Statewide trail systems
- County or municipal trail networks
- Multi-jurisdictional trail systems

A Trail Network is distinct from Individual Trails, Trail Segments, Sites,
Access Points, and Site Networks.

This schema is authoritative for **Trail Network structure**.

------------------------------------------------------------
# 2. TRAIL NETWORK FIELDS (15 FIELDS, AUTHORITATIVE ORDER)

1. **Network Name**
2. **Network Type**
3. **Status**
4. **Ownership**
5. **Governance**
6. **Partner Agencies**
7. **Counties**
8. **States Included**
9. **Total Length (Miles)**
10. **Member Trail Count**
11. **Member Trail IDs**
12. **Description**
13. **Notes**
14. **URL**
15. **Maps**
16. **Derived Label** *(computed, not stored)*

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Network Name
- Use the official published name.
- Must be unique statewide (case-insensitive).
- Must not include unofficial descriptors.
- Must not encode hierarchy or governance.
- Must align with identity determined by the Resolution Engine v5.0.

## 3.2 Network Type
- Must match a value from the Trail Network Vocabulary Module v5.0.
- Describes the identity-bearing type of the Trail Network.
- Must not encode governance, ownership, or management.
- Must not encode geographic scope beyond what is inherent in the network's identity.
- Must not be inferred from number of trails or geographic extent.

## 3.3 Status
- Must match a value from the Trail Network Vocabulary Module v5.0.
- Describes the network's current operational status.
- Examples: Active, Planned, Partial, Inactive.
- "Planned" must be explicitly documented.
- "Partial" applies when portions are complete but gaps exist.
- Must not be inferred.

## 3.4 Ownership
- Optional.
- Must contain the actual legal name of the entity that owns or
  legally established the network.
- Must not use generic categories.
- Blank when ownership is distributed across multiple agencies or
  when the network is a coordinating body without land ownership.
- Must be supported by authoritative documentation.

## 3.5 Governance
- The primary agency or organization responsible for coordinating
  or managing the Trail Network.
- Must be an authoritative name.
- Must not encode ownership or hierarchy.
- Must not be inferred.

## 3.6 Partner Agencies
- Optional.
- Semicolon-delimited list of secondary managing agencies, land managers,
  or documented organizational partners.
- Important for networks that cross multiple jurisdictions.
- Must not duplicate Governance.
- Must not include inferred partners.

## 3.7 Counties
- Array in JSON; semicolon-delimited in TSV.
- Alphabetical order.
- Must include all counties through which any part of the network passes.
- Must not include the word "County."
- Must follow the universal multi-county rule v5.0:
  - One Trail Network record regardless of number of counties.
- Must not include inferred counties.

## 3.8 States Included
- Optional.
- Array in JSON; semicolon-delimited in TSV.
- Alphabetical order.
- Only used for multi-state networks.
- Must not include inferred states.

## 3.9 Total Length (Miles)
- Optional.
- Numeric only.
- Represents the total documented length of all member trails.
- Use officially published length when available.
- Note in normalization if computed vs. published lengths differ.
- Blank if unknown or undocumented.

## 3.10 Member Trail Count
- Optional but strongly recommended.
- Integer representing the number of member Trails.
- Record the officially published count when available.
- May be estimated from enumerated member list if not published.
- Blank if truly unknown.

## 3.11 Member Trail IDs
- Optional.
- Array of trail_id values referencing normalized Trail entities.
- Populated during normalization as member Trails are resolved.
- May be incomplete during initial discovery — added incrementally.
- Supports bidirectional querying:
  - All Trails in a network: query member_trail_ids
  - All networks for a Trail: query trail_network_members relationship table

## 3.12 Description
- 1-3 sentences.
- Must describe identity-defining characteristics of the Trail Network.
- May include brief establishment history or origin context.
- Must not include Trail-level or Segment-level details.
- Must not include temporary conditions.

## 3.13 Notes
- Optional free-text field.
- Must not include identity-defining characteristics.
- Use for clarifications, gaps, planned extensions, or contextual notes.
- Must not include Trail-level or Segment-level details.

## 3.14 URL
- Full https:// URLs only.
- Semicolon-delimit if multiple authoritative URLs.
- Must reference authoritative sources.
- Tracking parameters must be removed.

## 3.15 Maps
- Optional.
- Array of map objects in JSON.
- Trail Networks are linear spatial systems — multiple map formats expected.
- Each map object contains:
  - `url` (required): full https:// URL
  - `type` (optional): pdf, interactive, gpx, kml, image
  - `description` (optional): brief description of map content
- In TSV: semicolon-delimited list of URLs only (metadata dropped).
- Leave blank if none.

## 3.16 Derived Label
- Computed, not stored.
- Formula defined in Trail Network Normalization Contract v5.0.
- Must be deterministic and based solely on normalized fields.
- Must not include parentheses, trailing punctuation, or additional descriptors.

------------------------------------------------------------
# 4. IDENTITY RULES

A Trail Network is valid only if:

- It is an identity-bearing umbrella entity composed of multiple Trails.
- It is documented in authoritative sources.
- It is distinct from its member Trails.
- It is not merely a marketing label or informal grouping.
- It does **not** have a parent Trail Network (v5.0 ontology rule).
- It does **not** serve as a parent for Trail Segments or Access Points directly.
- It is not a synthetic or inferred network.

If any of these conditions fail, the Trail Network must not be created.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Member Trails
- Membership stored in `trail_network_members` relationship table:
  - `network_id` (FK to trail_networks)
  - `trail_id` (FK to trails)
- `member_trail_ids` field is a convenience cache of trail_id values.
- Queryable both ways:
  - All Trails in a network: `SELECT trail_id FROM trail_network_members WHERE network_id = X`
  - All networks for a Trail: `SELECT network_id FROM trail_network_members WHERE trail_id = Y`

## 5.2 Trail Segment Inheritance
- Trail Segments do not directly belong to Trail Networks.
- Segments inherit network membership through their parent Trail.

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- Trail Network Vocabulary Module v5.0
- Trail Network Normalization Contract v5.0
- Trail Schema Module v5.0
- Trail Segment Schema Module v5.0
- TSV Output Specification (Trail Networks) v5.0
- Resolution Engine v5.0
- Discovery Protocol Module v5.0

------------------------------------------------------------
# END OF TRAIL NETWORK SCHEMA MODULE v5.0
