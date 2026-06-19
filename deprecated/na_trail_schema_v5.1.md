# NATURAL AREAS PROJECT
# TRAIL SCHEMA MODULE v5.2
(Authoritative Structure, Semantic Rules, Identity Anchors, and Validation Requirements for Trail Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Vocabulary Module v5.x**.

This module is authoritative for the structure and semantics of **Trail** entities.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **IMP-054 — §5.4 Parent Site relationship added**: Documents the `trail_parents`
  relationship table that models Trail-to-Site containment. A Trail wholly contained
  within a single named Site (governance aligns, trail's access and legal existence
  depend on the site) receives a `trail_parents` row linking `trail_id` to
  `parent_site_id`. Extra-limital Trails (crossing multiple governance units, spanning
  multiple parks, or otherwise not wholly contained within one Site) do not receive a
  row; their site association is expressed through the `governance` field.
  See also `na_trail_parent_site_schema_v5.1.md` for the full schema specification.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Derived Label removed**: No longer computed or stored — presentation-layer
  concern only; consistent with Site entity architectural decision
- **identity_notes added**: Separate normalized field for identity
  clarifications, distinct from notes
- **maps simplified**: Rich array format (url/type/description objects)
  replaced by plain semicolon-delimited URL list at all stages; type and
  description metadata dropped
- **Field count corrected**: 18 fields (v5.0 header incorrectly stated 19;
  body listed 18 named fields plus Trail ID undocumented; v5.1 states
  authoritative count of 18)
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `network_affiliation` removed — membership tracked via relationship tables
- `Parent Trail Network` removed — membership tracked via relationship tables
- `counties_traversed` renamed to `counties`
- `primary_managing_agency` renamed to `governance`
- `secondary_managing_agencies` renamed to `partner_agencies`
- `map_url` replaced by `maps` (rich array — simplified to URL list in v5.1)
- `difficulty` added (optional — record from authoritative sources only)
- `accessibility` added (optional — free-text)
- `alternate_names` retained
- `trail_history` retained as separate field

------------------------------------------------------------
# 1. PURPOSE

A **Trail** is a named, identity-bearing linear corridor documented in
authoritative sources. Examples include:

- Multi-use paved trails
- Hiking trails
- Bridle trails
- Water trails
- Mountain bike trails
- Rail trails
- Canal towpath trails
- Purpose-built recreational routes

A Trail is distinct from Trail Segments, Sites, Access Points, Trail
Networks, and Site Networks.

This schema is authoritative for **Trail structure**.

------------------------------------------------------------
# 2. TRAIL FIELDS (18 FIELDS, AUTHORITATIVE ORDER)

1.  **Trail Name**
2.  **Alternate Names**
3.  **Trail Use Type**
4.  **Trail Surface Type**
5.  **Trail Origin Type**
6.  **Total Length (Miles)**
7.  **Counties**
8.  **Governance**
9.  **Partner Agencies**
10. **Status**
11. **Difficulty**
12. **Accessibility**
13. **Description**
14. **Trail History**
15. **Identity Notes**
16. **Notes**
17. **URL**
18. **Maps**
19. **Trail ID**

Trail Network membership is stored in the `trail_network_members`
relationship table, not as a field in the Trail record.

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Trail Name
- Use the official published name.
- Must be unique statewide (case-insensitive).
- Must not include unofficial descriptors.
- Must align with identity determined by the Resolution Engine v5.x.

## 3.2 Alternate Names
- Optional.
- Array in JSON; semicolon-delimited in TSV.
- Include only documented historical or variant names, abbreviations, or
  formally used alternate designations.
- Must not include marketing names or slogans.
- Must not include invented or speculative names.
- Must not repeat Trail Name.

## 3.3 Trail Use Type
- Must match a value from the Trail Vocabulary Module v5.x.
- Describes the primary intended use.
- Must not encode surface or origin.
- Must not be inferred.

## 3.4 Trail Surface Type
- Must match a value from the Trail Vocabulary Module v5.x.
- Describes the predominant surface type.
- Use "Mixed" only when explicitly documented.
- Must not encode use type or origin.

## 3.5 Trail Origin Type
- Must match a value from the Trail Vocabulary Module v5.x.
- Describes the historical or structural origin.
- Must not be inferred.

## 3.6 Total Length (Miles)
- Numeric only.
- Represents the total documented length of the trail.
- Blank if unknown or undocumented.
- No estimates.

## 3.7 Counties
- Array in JSON; semicolon-delimited in TSV.
- Alphabetical order.
- Must include all counties through which any part of the trail passes.
- Must not include the word "County."
- Must not be inferred from geometry.

## 3.8 Governance
- The primary agency or organization responsible for managing the trail.
- Must be an authoritative name.
- Must not be inferred.
- Semicolon-delimit if multiple co-managers with equal authority.

## 3.9 Partner Agencies
- Optional.
- Semicolon-delimited list of secondary managing agencies or land
  managers.
- Must not duplicate Governance.
- Must not include inferred partners.

## 3.10 Status
- Must match a value from the Trail Vocabulary Module v5.x.
- Must describe the trail's current operational status.
- Must not be inferred.

## 3.11 Difficulty
- Optional.
- Must match a value from the Trail Vocabulary Module v5.x.
- Must be explicitly stated by the trail manager or an authoritative
  source.
- Must not be assessed or inferred by the discoverer.
- Blank if not documented.

## 3.12 Accessibility
- Optional.
- Free-text description of ADA compliance, wheelchair accessibility,
  surface grade, width, and accessible facilities.
- Record what authoritative sources state.
- Must not be inferred from surface type or trail use alone.
- Blank if not documented.

## 3.13 Description
- 1-3 sentences.
- Must describe identity-defining characteristics of the trail.
- Must not include temporary conditions, governance, or amenity details.

## 3.14 Trail History
- Optional.
- 1-3 sentences of factual, documented historical context.
- May include: rail corridor origin, canal conversion, historic
  designation, established date, former names, or major route changes.
- Must be factual and sourced.
- Must not include speculative or inferred history.

## 3.15 Identity Notes
- Optional free-text field for identity clarifications.
- Use for: disambiguation notes, trail vs. trail segment boundary
  questions, alternate name conflicts, network membership uncertainty,
  flag rationale.
- Must not duplicate Notes content.
- Must not include operational or contextual notes (those go in Notes).

## 3.16 Notes
- Optional free-text field.
- Must not include identity-defining characteristics.
- Use for: temporary closures, access restrictions, seasonal notes,
  parking details, gap locations, construction updates.

## 3.17 URL
- Full https:// URL to the primary authoritative source.
- Semicolon-delimit if multiple authoritative URLs.
- Tracking parameters must be removed.

## 3.18 Maps
- Optional.
- Semicolon-delimited list of URLs to trail map resources.
- Includes: PDF maps, GPX files, KML files, interactive map viewers,
  GIS layers, elevation profiles.
- Distinct from URL — maps are navigation and geometry resources;
  URL is the trail's web presence.
- Leave blank if none.

## 3.19 Trail ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- Must be a valid integer matching the entity's trail_id.
- Enables joins to the trail_network_members relationship table.

------------------------------------------------------------
# 4. IDENTITY RULES

A Trail is valid only if:

- It is a named, identity-bearing linear corridor.
- It is documented in authoritative sources.
- It is distinct from its parent Trail Network (if any).
- It is not merely a path, route suggestion, or unnamed connection.
- It is not a Trail Segment, Site, or Access Point.
- It is not a synthetic or inferred entity.

If any identity condition fails, the Trail must not be created.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Network Membership
- Trail Network membership stored in `trail_network_members`
  relationship table.
- Queryable both ways: all Trails in a network; all networks for a Trail.
- Not encoded as a field in the Trail record.

## 5.2 Trail Segments
- Trail Segments reference their parent Trail via `parent_trail_id`.
- A Trail does not list its segments.
- Downward relationships handled by the Resolution Engine v5.x.

## 5.3 Access Points
- Access Points reference their parent Trail via
  `identity_parent_entity_id`.
- A Trail does not list its Access Points.

## 5.4 Parent Site (IMP-054)
- Trails wholly contained within a single named Site may have a `trail_parents` row
  in the `trail_parents` relationship table linking `trail_id` to `parent_site_id`.
- A Trail does not encode this relationship in any of its own fields — the relationship
  is stored exclusively in the `trail_parents` table.

**Containment criteria** — all three conditions must hold:
1. The Trail is physically and geographically wholly within the Site's boundary.
2. The Trail's governance aligns with the Site's governance (same managing entity).
3. The Trail's access and legal existence depend on the Site (a visitor accesses the trail via the site; the trail cannot be accessed independently).

**Extra-limital Trails** — a Trail must NOT have a `trail_parents` row if any of the following are true:
- The Trail crosses multiple governance units or Sites.
- The Trail spans multiple parks (e.g., a greenway passing through several Metro Parks).
- The Trail is a water trail, rail trail, or other corridor trail with an existence independent of any single site.
- Governance is multi-entity and no single site is the primary container.

For extra-limital Trails, site association is expressed in the `governance` field only.

**Identity Notes requirement**: Any Trail with a `trail_parents` row must have `identity_notes`
containing the statement: `Contained within [Site Name] ([site_id]).`

Full schema for the `trail_parents` table: see `na_trail_parent_site_schema_v5.1.md`.

------------------------------------------------------------
# 6. DISCOVERY PHASE NOTE

The following fields require GIS phase work and are not expected
during web discovery:

- `geometry` — LineString/MultiLineString; populated in GIS phase

Discoverers should note map URLs and GPX/KML links in the `maps` field
to facilitate GIS phase geometry acquisition.

------------------------------------------------------------
# 7. MODULE DEPENDENCIES

This module depends on:

- Trail Vocabulary Module v5.x
- Trail Normalization Contract v5.x
- Trail Network Schema Module v5.x
- Trail Segment Schema Module v5.x
- TSV Output Specification (Trails) v5.x
- Resolution Engine v5.x
- Discovery Protocol Module v5.x

------------------------------------------------------------
# END OF TRAIL SCHEMA MODULE v5.1
