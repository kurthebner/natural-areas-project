# NATURAL AREAS PROJECT
# TRAIL NETWORK SCHEMA MODULE v5.3
(Authoritative Structure, Semantic Rules, and Validation Requirements for Trail Network Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Network Vocabulary Module v5.x**.

This module is authoritative for the structure and semantics of
**Trail Network** entities.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- **IMP-127** — Corrected `counties` (§3.7) and `states_included` (§3.8) type
  annotations from `Array in JSON; semicolon-delimited in TSV` to `TEXT,
  semicolon-delimited (stored identically in DB and TSV)`. SQLite has no native array
  type; both fields are stored as semicolon-delimited TEXT in the database.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **IMP-126** — Corrected stale `integer` type annotation on Network ID (§3.17) to
  `TEXT` with explicit `OH-{COUNTY}-{TYPE}-{SEQ}` format note. DB schema was already
  correct; this fixes documentation drift introduced before the IMP-107 global ID
  migration.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Derived Label removed**: No longer computed or stored — presentation-
  layer concern only; consistent with Site entity architectural decision
- **identity_notes added**: Separate normalized field for identity
  clarifications, distinct from notes; surfaced from identity_notes_raw
- **maps simplified**: Rich array format (url/type/description objects)
  replaced by plain semicolon-delimited URL list at all stages; type and
  description metadata dropped; consistent with Trail and Trail Segment
- **Field count**: 16 named fields (was 15 named + Derived Label computed):
  removed Derived Label, added identity_notes; Network ID added for
  authoritative count of 17 total output fields (see TSV spec)
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `alternate_names` removed — variants noted in description
- `history` removed — merged into description
- `county_list` renamed to `counties`
- `primary_managing_agency` renamed to `governance`
- `secondary_managing_agencies` renamed to `partner_agencies`
- `map_url` replaced by `maps` (simplified to URL list in v5.1)
- `status` added
- `ownership` added
- `total_length_miles` added
- `member_trail_count` added
- `member_trail_ids` added

------------------------------------------------------------
# 1. PURPOSE

A **Trail Network** is a named, identity-bearing umbrella entity
composed of multiple Trails. Examples include:

- Regional greenway systems
- National Scenic Trail systems
- Water trail networks
- Statewide trail systems
- County or municipal trail networks
- Multi-jurisdictional trail systems

A Trail Network is distinct from Individual Trails, Trail Segments,
Sites, Access Points, and Site Networks.

This schema is authoritative for **Trail Network structure**.

------------------------------------------------------------
# 2. TRAIL NETWORK FIELDS (16 FIELDS, AUTHORITATIVE ORDER)

1.  **Network Name**
2.  **Network Type**
3.  **Status**
4.  **Ownership**
5.  **Governance**
6.  **Partner Agencies**
7.  **Counties**
8.  **States Included**
9.  **Total Length (Miles)**
10. **Member Trail Count**
11. **Member Trail IDs**
12. **Description**
13. **Identity Notes**
14. **Notes**
15. **URL**
16. **Maps**
17. **Network ID**

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Network Name
- Use the official published name.
- Must be unique statewide (case-insensitive).
- Must not include unofficial descriptors.
- Must not encode hierarchy or governance.
- Must align with identity determined by the Resolution Engine v5.x.

## 3.2 Network Type
- Must match a value from the Trail Network Vocabulary Module v5.x.
- Describes the identity-bearing type of the Trail Network.
- Must not encode governance, ownership, or management.
- Must not be inferred from number of trails or geographic extent.

## 3.3 Status
- Must match a value from the Trail Network Vocabulary Module v5.x.
- Describes the network's current operational status.
- "Planned" must be explicitly documented.
- "Partially Open" applies when portions are complete but gaps exist.
- Must not be inferred.

## 3.4 Ownership
- Optional.
- Must contain the actual legal name of the entity that owns or
  legally established the network.
- Must not use generic categories.
- Blank when ownership is distributed across multiple agencies or
  when the network is a coordinating body without land ownership.
- Blank is correct and common for this field.

## 3.5 Governance
- The primary agency or organization responsible for coordinating
  or managing the Trail Network.
- Must be an authoritative name.
- Must not encode ownership or hierarchy.
- Must not be inferred.

## 3.6 Partner Agencies
- Optional.
- Semicolon-delimited list of secondary managing agencies, land
  managers, or documented organizational partners.
- Important for networks that cross multiple jurisdictions.
- Must not duplicate Governance.
- Must not include inferred partners.

## 3.7 Counties
- TEXT, semicolon-delimited (stored identically in DB and TSV).
- Alphabetical order.
- Must include all counties through which any part of the network
  passes.
- Must not include the word "County."
- One Trail Network record regardless of number of counties.
- Must not include inferred counties.

## 3.8 States Included
- Optional.
- TEXT, semicolon-delimited (stored identically in DB and TSV).
- Alphabetical order.
- Only used for multi-state networks.
- Blank for Ohio-only networks — do not write "Ohio."
- Must not include inferred states.

## 3.9 Total Length (Miles)
- Optional.
- Numeric only.
- Represents the total documented length of all member trails.
- Use officially published length when available.
- Never compute by summing member trail lengths unless source does so.
- Blank if unknown or undocumented.

## 3.10 Member Trail Count
- Optional but strongly recommended.
- Integer representing the number of member Trails.
- Record the officially published count when available.
- May be estimated from an enumerated member list if count is not
  published.
- Blank if truly unknown.

## 3.11 Member Trail IDs
- Optional.
- Array of trail_id values referencing normalized Trail entities.
- Populated during normalization as member Trails are resolved.
- May be incomplete during initial discovery.
- Supports bidirectional querying via `trail_network_members`
  relationship table.

## 3.12 Description
- 1-3 sentences.
- Must describe identity-defining characteristics of the Trail
  Network: purpose, geographic scope, character.
- May include brief establishment history or origin context
  (formerly a separate `history` field — now merged here).
- Must not include Trail-level or Segment-level details.
- Must not include temporary conditions.

## 3.13 Identity Notes
- Optional free-text field for identity clarifications.
- Use for: network vs. trail boundary questions (e.g., is this a
  Trail or a Trail Network?), name conflicts, membership uncertainty,
  vocabulary type flags.
- Must not duplicate Notes content.
- Must not include operational or contextual notes (those go in
  Notes).

## 3.14 Notes
- Optional free-text field.
- Must not include identity-defining characteristics.
- Use for: gap documentation, planning status, partial completion
  notes, funding status, contextual clarifications.
- Must not include Trail-level or Segment-level details.

## 3.15 URL
- Full https:// URLs only.
- Semicolon-delimit if multiple authoritative URLs.
- Must reference authoritative sources.
- Tracking parameters must be removed.

## 3.16 Maps
- Optional.
- Semicolon-delimited list of URLs to network map resources.
- Trail Networks are linear spatial systems — multiple map formats
  (PDF strip maps, interactive viewers, GPX/KML files) are common.
- Distinct from URL — maps are navigation and geometry resources.
- Leave blank if none.

## 3.17 Network ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- Must be a valid TEXT ID in OH-{COUNTY}-{TYPE}-{SEQ} format matching the entity's network_id.
- Enables joins to the `trail_network_members` relationship table.

------------------------------------------------------------
# 4. IDENTITY RULES

A Trail Network is valid only if:

- It is an identity-bearing umbrella entity composed of multiple
  Trails.
- It is documented in authoritative sources.
- It is distinct from its member Trails.
- It is not merely a marketing label or informal grouping.
- It does NOT have a parent Trail Network (v5.x ontology rule).
- It does NOT serve as a parent for Trail Segments or Access Points
  directly.
- It is not a synthetic or inferred network.

If any condition fails, the Trail Network must not be created.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Member Trails
- Membership stored in `trail_network_members` relationship table:
  - `network_id` (FK to trail_networks)
  - `trail_id` (FK to trails)
- `member_trail_ids` field is a convenience cache of trail_id values.
- Queryable both ways.

## 5.2 Trail Segment Inheritance
- Trail Segments do not directly belong to Trail Networks.
- Segments inherit network membership through their parent Trail.

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- Trail Network Vocabulary Module v5.x
- Trail Network Normalization Contract v5.x
- Trail Schema Module v5.x
- Trail Segment Schema Module v5.x
- TSV Output Specification (Trail Networks) v5.x
- Resolution Engine v5.x
- Discovery Protocol Module v5.x

------------------------------------------------------------
# END OF TRAIL NETWORK SCHEMA MODULE v5.1
