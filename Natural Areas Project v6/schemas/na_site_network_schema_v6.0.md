# NATURAL AREAS PROJECT
# SITE NETWORK SCHEMA MODULE v6.0
(Authoritative Structure, Semantic Rules, and Validation Requirements for Site Network Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Site Network Vocabulary Module v6.x**.

This module is authoritative for the structure and semantics of **Site Network** entities.

------------------------------------------------------------
# CHANGES FROM v5.4 → v6.0 (IMP-135)

- **Broadened definition**: Site Networks now include any named organization or
  designation that manages, coordinates, or encompasses two or more Sites in the
  project, documented in authoritative sources. The prior requirement for
  "explicit system-level identity" and "system-level branding distinct from the
  managing organization" is removed. The organization and its collection of
  holdings are understood as the same entity viewed from different angles — not
  two separate things requiring separate tests.

- **Threshold rules added to §4 Identity Rules**: Four explicit rules determine
  when a Site Network record is created, keyed on `network_type` and `org_type`.
  These rules replace the prior gray-area guidance and the SITE_NETWORK_UNCERTAIN
  flag as the primary identity gate.

- **SITE_NETWORK_PROVISIONAL flag added**: Replaces the primary use of
  SITE_NETWORK_UNCERTAIN for early-discovery records. When the first member site
  is cataloged for an organization expected to meet threshold, a provisional Site
  Network record is created immediately with this flag. This preserves
  organizational context gathered during discovery and focuses subsequent
  discovery on finding additional member sites.

- **SITE_NETWORK_UNCERTAIN retained but narrowed**: Now reserved for genuinely
  ambiguous cases where it is unclear which org_type or network_type applies, or
  where the organization's scope cannot be determined from available sources.

- **`coordination` field added** (§3.8, position 8): Captures community-based,
  volunteer, advisory, or informal partners — the fourth tier of the
  organizational model consistent with all other entity types. Field count
  increases from 16 to 17.

- **Governance Entity Role clarified**: Site Network records remain the canonical
  record for the managing organization's primary website URL. This applies to all
  multi-site managers regardless of whether they also qualify as a Named Network
  in the formal designation sense.

- **END marker corrected**: Prior version had `END OF SITE NETWORK SCHEMA MODULE
  v5.2` — now correct.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- **IMP-127** — Corrected `counties` (§3.9) and `states_included` (§3.10) type
  annotations from `Array in JSON; semicolon-delimited in TSV` to `TEXT,
  semicolon-delimited (stored identically in DB and TSV)`.

------------------------------------------------------------
# 1. PURPOSE

A **Site Network** is a named organization or designation that manages,
coordinates, or encompasses two or more Sites in the project, documented
in authoritative sources.

Site Networks serve two complementary purposes:

**Collection identity**: The network has a name and a defined set of member
Sites that belong to it — an NHA, a scenic river corridor, a land trust's
preserve portfolio, a metropark district's parks system.

**Organizational intelligence**: The Site Network record is the canonical
anchor for organization-level information — total member count, aggregate
acreage, primary website URL, org type, service territory — that cannot be
reconstructed by querying individual Site records alone.

These two purposes are not in tension. They are the same entity viewed from
different angles. A metropark district managing 21 parks both *is* an
organization and *has* a collection of parks. Both aspects are captured in
the single Site Network record.

**Examples of Site Networks under this definition:**
- Ohio & Erie Canalway National Heritage Area (federal designation + named collection)
- Little Miami Scenic River Corridor (state designation + corridor of sites)
- Muskingum Watershed Conservancy District Lakes (16-lake unified system)
- Metro Parks Serving Franklin County (multi-county park authority with 21 parks)
- Arc of Appalachia Preserve System (land trust portfolio)
- Black Swamp Conservancy (land trust portfolio)
- Wood County Park District (county park authority)
- Columbus Recreation and Parks Department (municipal dept, 3+ in-scope sites)

**Not Site Networks:**
- A parks department referenced only as the governance body on individual Site
  records, with fewer than the applicable threshold of in-scope member sites
- A single Site with internal child Sites (use parent_site_id, not a network)
- An informal grouping or marketing label with no managing organization
- A Trail Network — Trail Networks are collections of Trails, not Sites

This schema is authoritative for **Site Network structure**.

------------------------------------------------------------
# 2. SITE NETWORK FIELDS (17 FIELDS, AUTHORITATIVE ORDER)

1.  **Network Name**
2.  **Network Type**
3.  **Org Type**
4.  **Status**
5.  **Ownership**
6.  **Governance**
7.  **Partner Agencies**
8.  **Coordination**
9.  **Counties**
10. **States Included**
11. **Member Count**
12. **Member Site IDs**
13. **Description**
14. **Identity Notes**
15. **Notes**
16. **URL**
17. **Network ID**

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Network Name
- Use the official published name of the organization or designation.
- Must be unique statewide (case-insensitive).
- Must not include unofficial descriptors.
- Must align with identity determined by the Resolution Engine.

## 3.2 Network Type
- Must match a value from the Site Network Vocabulary Module v6.x.
- Describes the nature of the Site Network entity.
- For formally designated networks (NHA, scenic corridor, etc.): use the
  designation type.
- For organizational portfolios (park district, land trust, etc.): use the
  type that best describes the collection — typically "Park District System",
  "Land Trust Portfolio", "Conservation Authority Portfolio", or similar.
  Read the vocabulary module for current allowed values.
- Must not encode governance, ownership, or organizational hierarchy.
- Must not be inferred.

## 3.3 Org Type
- Must match a value from the Site Network Vocabulary Module v6.x.
- Classifies the organizational category of the primary governance entity
  responsible for or associated with this network.
- Distinct from Network Type: Network Type describes what the collection is;
  Org Type describes what kind of organization manages it.
- Required for all Site Network records. Leave blank only if no single
  governance entity can be identified.
- Must not be inferred from network_type or member site ownership alone.
- **Org Type is used in threshold enforcement (see §4).**

## 3.4 Status
- Must match a value from the Site Network Vocabulary Module v6.x.
- "Proposed" and "Dissolved" must be explicitly documented.
- Must not be inferred.

## 3.5 Ownership
- Optional.
- Must contain the actual legal name of the entity that owns or legally
  established the network.
- Must not use generic categories (e.g., "County Government").
- Must not encode management or governance.
- Blank if ownership is distributed among member sites, if the network is
  a coordinating or designating body without land ownership, or if unclear.
- Blank is correct and common for formally designated networks (NHAs,
  scenic river corridors, heritage corridors).

## 3.6 Governance
- The primary agency or organization responsible for managing or coordinating
  the network.
- Must be an authoritative name.
- Must not be inferred.
- Must not use generic categories.

## 3.7 Partner Agencies
- Optional.
- Semicolon-delimited list of secondary managing agencies or documented
  organizational partners.
- Must not duplicate Governance.
- Must not include inferred partners.

## 3.8 Coordination
- Optional.
- Semicolon-delimited list of community-based, volunteer, advisory, or
  informal partners associated with the network.
- Distinct from Partner Agencies: Partner Agencies are formal co-managers
  with documented operational roles; Coordination captures friends groups,
  stewardship volunteers, watershed councils, advisory boards, and similar
  informal or community-level partners.
- Must not duplicate Governance or Partner Agencies.
- Must be documented — do not infer coordination relationships.

## 3.9 Counties
- TEXT, semicolon-delimited (stored identically in DB and TSV).
- Alphabetical order.
- Must include all counties in which any member site is located.
- Must not include the word "County."
- One Site Network record regardless of number of counties.

## 3.10 States Included
- Optional.
- TEXT, semicolon-delimited (stored identically in DB and TSV).
- Alphabetical order.
- Only used for multi-state networks.
- Leave blank for Ohio-only networks.
- Must not be inferred.

## 3.11 Member Count
- Optional but strongly recommended.
- Integer representing the number of member Sites.
- Record the officially published count when available.
- May be derived from enumerated member list if not published.
- For provisional records (SITE_NETWORK_PROVISIONAL), reflects only
  confirmed members to date — update as additional members are cataloged.
- Blank if truly unknown.

## 3.12 Member Site IDs
- Optional.
- Semicolon-delimited list of site_id values referencing normalized Site
  entities.
- Populated during normalization as member Sites are resolved.
- May be incomplete during initial discovery — added incrementally.
- Supports bidirectional querying via the site_network_members relationship
  table.

## 3.13 Description
- 1-3 sentences describing the network's identity, scope, and purpose.
- **Priority: character and mission.** Describe what this organization or
  designation actually is and does — its conservation mission, geographic
  territory, or significance. A description that says only "a county park
  district" tells a reader nothing useful.
- For organizational portfolios: describe the organization's mission,
  service territory, and nature of holdings.
- For formal designations: describe the designation's scope, geography,
  and significance.
- May include brief establishment history or origin context.
- Must not include site-level details.
- Must not include amenity inventory or facility lists — those belong on
  individual Site records.

## 3.14 Identity Notes
- Optional free-text field for identity clarifications.
- **SITE_NETWORK_PROVISIONAL** — use when a record is created before the
  applicable member site threshold is met, because the first member site has
  been cataloged and additional members are expected:
  ```
  SITE_NETWORK_PROVISIONAL — [org name] first member site cataloged
  [date]; [N] additional member sites expected. Threshold: [applicable rule].
  ```
- **SITE_NETWORK_UNCERTAIN** — use only when it is genuinely unclear which
  org_type or network_type applies, or when the organization's scope cannot
  be determined from available sources:
  ```
  SITE_NETWORK_UNCERTAIN — [description of specific uncertainty]
  ```
- Also use for: disambiguation notes, alternate names, governance
  verification notes.
- Must not duplicate Description.

## 3.15 Notes
- Optional free-text field for operational and contextual notes.
- Use for: funding notes, boundary clarifications, designation history,
  partnership context, discovery gaps, service territory notes.
- **Customer-facing field — no provenance artifacts.** Pipeline source
  references, IMP numbers, batch load notes, and similar process or
  provenance content must not appear here. That information belongs in
  the provenance tables. Notes must be readable by someone who knows
  nothing about the pipeline.
- Must not include identity-defining characteristics (those belong in
  Description or Identity Notes).

## 3.16 URL
- Full https:// URL to the primary authoritative page for the network or
  managing organization.
- For organizational portfolio records, this is the organization's primary
  website — captured once here and not duplicated across individual Site
  records. Member Site and Trail `governance` fields reference the
  organization by name; the URL is retrieved by joining to this record.
- Semicolon-delimit if multiple authoritative URLs exist, including any
  system-wide map URLs.
- Must not include placeholders or inferred URLs.

## 3.17 Network ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- TEXT in OH-{COUNTY}-{TYPE}-{SEQ} format matching the entity's network_id.
- For multi-county networks: OH-MC-SN-{SEQ} format.
- Enables joins to the site_network_members relationship table.

------------------------------------------------------------
# 4. IDENTITY RULES — WHEN TO CREATE A SITE NETWORK RECORD

A Site Network record is created when **any one of the following four
rules** is satisfied. Rules are checked in order; the first matching rule
governs.

## Rule 1 — Formal Designation (always qualify)

If `network_type` is any formal designation value — National Heritage Area,
Scenic River Corridor, Conservation Corridor, Heritage Corridor, Historic
Corridor, Local Historic District, Ecological Corridor, Cultural Landscape
Network, Watershed Network, or Greenway Network — create the Site Network
record regardless of member site count.

A formally designated entity exists as a network by definition. Member
sites may be zero at discovery time for newly designated networks.

## Rule 2 — Conservation and Land-Holding Organizations (2+ member sites)

If `org_type` is Land Trust, Nonprofit Conservancy, Regional Authority,
County Authority, State Agency, or Federal Agency — create the Site Network
record when **2 or more** member Sites are cataloged.

These organization types are defined by their conservation or land-management
mission. Any such organization managing 2+ project Sites warrants a record.

*Examples: Arc of Appalachia, Black Swamp Conservancy, Metro Parks Serving
Franklin County, Wayne County Park District, Ohio Department of Natural
Resources (for multi-site portfolios within a county).*

## Rule 3 — Municipal Departments (3+ in-scope member sites)

If `org_type` is Municipal Department — create the Site Network record when
**3 or more** in-scope member Sites are cataloged.

"In-scope" means Sites that are natural areas, open space, conservation
lands, trail-connected parks, or other sites of a similar category — not purely 
developed athletic facilities (ballfields, basketball courts, splash pads) 
that contain no natural area component. A site with both a ballfield and a 
nature trail or green space counts as in-scope.

The higher threshold reflects that municipal parks departments often manage
a mix of developed recreation facilities that are outside project scope. The
threshold filters out two-park village departments while capturing genuine
municipal natural areas systems.

## Rule 4 — Other Organizations (3+ member sites, documented rationale)

If `org_type` is Other — create the Site Network record when **3 or more**
member Sites are cataloged, and document in `identity_notes` why a Site
Network record is warranted for this organization type.

## Provisional Records

When the first member Site is cataloged for an organization that is expected
to meet the applicable threshold, **create a provisional Site Network record
immediately** rather than waiting for the threshold to be reached.

Rationale: organizational context gathered during discovery (website URL,
governance name, org type, description, service territory) should be captured
at discovery time, not reconstructed later. The provisional record also
focuses subsequent discovery — if additional member sites are not found, the
provisional record surfaces this gap at tier close.

Flag the record in `identity_notes` with `SITE_NETWORK_PROVISIONAL` and
the applicable threshold rule. Remove the flag when the threshold is met.
If the threshold is not met by the end of full discovery for the county,
evaluate whether the record should be retained (formal designation, or
strong expectation of future members) or removed.

## Records That Must Not Be Created

- A single Site with internal child Sites — use `parent_site_id`, not a network
- An informal grouping or marketing label with no managing organization
- A governance body referenced on Site records but managing fewer than the
  applicable threshold of in-scope Sites in the project
- A Trail Network (collections of Trails belong in the trail_networks table)
- Nested Site Networks — no Site Network may have another Site Network as parent

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
- A Site may belong to more than one Site Network (e.g., a park managed by
  both a county park district and within a scenic river corridor).

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- Site Network Vocabulary Module v6.x
- Site Network Normalization Contract v6.x
- Site Network TSV Output Specification v6.x
- Site Network Discovery Sub-Procedure v6.x
- Resolution Engine v6.x
- Discovery Protocol Module v6.x

------------------------------------------------------------
# END OF SITE NETWORK SCHEMA MODULE v6.0
