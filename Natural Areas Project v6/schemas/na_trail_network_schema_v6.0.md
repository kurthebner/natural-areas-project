# NATURAL AREAS PROJECT
# TRAIL NETWORK SCHEMA MODULE v6.0
(Authoritative Structure, Semantic Rules, and Validation Requirements for Trail Network Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Network Vocabulary Module v6.x**.

This module is authoritative for the structure and semantics of
**Trail Network** entities.

------------------------------------------------------------
# CHANGES FROM v5.3 → v6.0 (IMP-008)

- **`org_type` field added** (§3.3, position 3): Classifies the organizational
  category of the primary governance entity. Purely descriptive — org_type carries
  no threshold or identity-gate function for Trail Networks. Added for consistency
  with the organizational model and to enable org-level queries. Vocabulary defined
  in Trail Network Vocabulary Module v6.x.

- **`coordination` field added** (§3.8, position 8): Captures community-based,
  volunteer, advisory, or informal partners — the fourth tier of the organizational
  model, consistent with all other entity types. Field count increases from 17 to 19.

- **Identity rules rewritten** (§4): Trail Networks are system-identity-first
  entities. The organizing principle is the trail system, not the managing
  organization. Common management or governance alone is not sufficient to create
  a Trail Network record — the system must be explicitly documented with its own
  name and membership. This is a deliberate asymmetry with Site Networks, which
  are org-intelligence-first. Trail Networks and Site Networks share a name but
  serve different purposes and are governed by different identity tests.

- **Org-portfolio Trail Networks clarified** (§4): An organization managing
  multiple trails may warrant a Trail Network record, but only when it has
  deliberately assembled those trails into a named system with documented identity
  — its own name, map, or membership framing. Mere ownership or management of
  multiple trails is not sufficient.

- **Trail Network vs. trail_site_relationships** (§5): Trail Networks document
  trail system membership (which Trails belong to this network). The
  trail_site_relationships table (formerly trail_parents) documents trail-site
  associations (which Sites a Trail passes through or is access-dependent on).
  These are separate concerns in separate tables.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- **IMP-127** — Corrected `counties` (§3.9) and `states_included` (§3.10) type
  annotations to `TEXT, semicolon-delimited`.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **IMP-126** — Corrected stale `integer` type annotation on Network ID (§3.19)
  to `TEXT` with explicit `OH-{COUNTY}-{TYPE}-{SEQ}` format note.

------------------------------------------------------------
# 1. PURPOSE

A **Trail Network** is a named, identity-bearing umbrella entity composed of
multiple Trails. It exists because the *collection of trails* has been explicitly
assembled and documented as a system — not because a single organization manages
multiple trails.

Examples include:
- Regional greenway systems
- Water trail networks
- Statewide trail systems
- County or municipal trail systems with explicit network identity
- Multi-jurisdictional trail corridors
- Equestrian trail systems

A Trail Network is distinct from:
- Individual Trails and Trail Segments
- Sites and Site Networks
- Access Points
- A park or preserve that contains multiple trails (those trails relate to the
  Site via trail_site_relationships, not via a Trail Network)

**Trail Networks and Site Networks are different kinds of entities.** Site Networks
are organized around the managing organization — the org is the anchor, the sites
are its holdings. Trail Networks are organized around the trail system — the system
identity is the anchor, the managing organization is secondary. This asymmetry is
intentional. Do not attempt to make Trail Network rules mirror Site Network rules.

This schema is authoritative for **Trail Network structure**.

------------------------------------------------------------
# 2. TRAIL NETWORK FIELDS (19 FIELDS, AUTHORITATIVE ORDER)

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
11. **Total Length (Miles)**
12. **Member Trail Count**
13. **Member Trail IDs**
14. **Description**
15. **Identity Notes**
16. **Notes**
17. **URL**
18. **Maps**
19. **Network ID**

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Network Name
- Use the official published name of the trail system.
- Must be unique statewide (case-insensitive).
- Must not include unofficial descriptors.
- Must not encode hierarchy or governance.
- Must align with identity determined by the Resolution Engine.

## 3.2 Network Type
- Must match a value from the Trail Network Vocabulary Module v6.x.
- Describes the identity-bearing type of the Trail Network.
- Must not encode governance, ownership, or management.
- Must not be inferred from member count or geographic extent.

## 3.3 Org Type
- Must match a value from the Trail Network Vocabulary Module v6.x.
- Classifies the organizational category of the primary governance entity
  responsible for coordinating or managing this network.
- **Descriptive only** — org_type carries no threshold or identity-gate
  function for Trail Networks. A Trail Network is not created because of
  an organization's holdings; org_type simply describes what kind of
  organization manages the system that qualifies on its own identity merits.
- Optional. Leave blank if the governing organization does not clearly fit
  any vocabulary value, or if governance is distributed across multiple
  organizations without a single primary coordinator.
- Must not be inferred from network_type or member trail governance alone.

## 3.4 Status
- Must match a value from the Trail Network Vocabulary Module v6.x.
- "Planned" must be explicitly documented.
- "Partially Open" applies when portions are complete but gaps exist.
- Must not be inferred.

## 3.5 Ownership
- Optional.
- Must contain the actual legal name of the entity that owns or legally
  established the network corridor.
- Must not use generic categories.
- Blank when ownership is distributed across multiple agencies or when
  the network is a coordinating body without land ownership.
- Blank is correct and common — many trail networks are coordinating or
  designating bodies, not land owners.

## 3.6 Governance
- The primary agency or organization responsible for coordinating or
  managing the Trail Network.
- Must be an authoritative name.
- Must not encode ownership or hierarchy.
- Must not be inferred.

## 3.7 Partner Agencies
- Optional.
- Semicolon-delimited list of secondary managing agencies, land managers,
  or documented organizational partners.
- Important for networks that cross multiple jurisdictions.
- Must not duplicate Governance.
- Must not include inferred partners.

## 3.8 Coordination
- Optional.
- Semicolon-delimited list of community-based, volunteer, advisory, or
  informal partners associated with the network.
- Distinct from Partner Agencies: Partner Agencies are formal co-managers
  with documented operational roles; Coordination captures trail stewardship
  volunteers, friends groups, trail associations, advisory boards, and
  similar informal or community-level partners.
- Must not duplicate Governance or Partner Agencies.
- Must be documented — do not infer coordination relationships.

## 3.9 Counties
- TEXT, semicolon-delimited (stored identically in DB and TSV).
- Alphabetical order.
- Must include all counties through which any member trail passes.
- Must not include the word "County."
- One Trail Network record regardless of number of counties.
- Must not include inferred counties.

## 3.10 States Included
- Optional.
- TEXT, semicolon-delimited (stored identically in DB and TSV).
- Alphabetical order.
- Only used for multi-state networks.
- Blank for Ohio-only networks — do not write "Ohio."
- Must not include inferred states.

## 3.11 Total Length (Miles)
- Optional.
- Numeric only.
- Use officially published total length when available.
- Never compute by summing member trail lengths unless an authoritative
  source does so explicitly.
- Blank if unknown or undocumented.

## 3.12 Member Trail Count
- Optional but strongly recommended.
- Integer representing the number of member Trails.
- Record the officially published count when available.
- May be derived from an enumerated member list if count is not published.
- For multi-county networks with partial membership documented so far,
  reflects confirmed members to date — update as additional counties are
  processed (see §5.2).
- Blank if truly unknown.

## 3.13 Member Trail IDs
- Optional.
- Semicolon-delimited list of trail_id values referencing normalized Trail
  entities.
- Populated during normalization as member Trails are resolved.
- May be incomplete for multi-county networks during initial discovery.
- Supports bidirectional querying via the trail_network_members relationship
  table.

## 3.14 Description
- 1-3 sentences describing the network's identity, scope, and purpose.
- Must describe identity-defining characteristics: purpose, geographic
  scope, character of the system.
- May include brief establishment history or origin context.
- Must not include Trail-level or Segment-level details.
- Must not include temporary conditions.

## 3.15 Identity Notes
- Optional free-text field for identity clarifications.
- Use for: network vs. trail boundary questions (is this a Trail or a
  Trail Network?), name conflicts, membership uncertainty, vocabulary
  type flags, partial membership status for multi-county networks.
- **Partial membership flag** (multi-county networks):
  ```
  PARTIAL MEMBERSHIP: Only [County] County member trails documented
  as of [date]. Additional member trails expected from [County2],
  [County3] county sessions.
  ```
- Must not duplicate Notes content.

## 3.16 Notes
- Optional free-text field.
- Use for: gap documentation, planning status, partial completion notes,
  funding status, contextual clarifications.
- Must not include identity-defining characteristics.
- Must not include Trail-level or Segment-level details.

## 3.17 URL
- Full https:// URLs only.
- Semicolon-delimit if multiple authoritative URLs.
- Must reference authoritative sources.
- Tracking parameters must be removed.

## 3.18 Maps
- Optional.
- Semicolon-delimited list of URLs to network map resources.
- Trail Networks are linear spatial systems — multiple map formats
  (PDF strip maps, interactive viewers, GPX/KML files) are common and
  expected.
- Distinct from URL — maps are navigation and geometry resources.
- Tracking parameters must be removed.
- Leave blank if none.

## 3.19 Network ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- TEXT in OH-{COUNTY}-{TYPE}-{SEQ} format matching the entity's network_id.
- TN designates a Trail Network.
- For multi-county networks: OH-MC-TN-{SEQ} format.
- Enables joins to the trail_network_members relationship table.

------------------------------------------------------------
# 4. IDENTITY RULES — WHEN TO CREATE A TRAIL NETWORK RECORD

## 4.1 The Standard

A Trail Network record is created when **all of the following are true**:

1. **Two or more named Trails** are explicitly grouped together.
2. The grouping has a **stable, identity-bearing name** — not a temporary
   project label, informal description, or marketing slogan.
3. An **authoritative source** documents the grouping — the managing or
   coordinating organization presents these trails as a unified system.
4. The member Trails have **their own individual identities** — they are
   named Trails in their own right, not unnamed segments of a single trail.
5. The network is **not a single Trail with multiple Segments** — length
   and complexity alone do not make something a network.
6. The network is **distinct from its member Trails** — the network name
   is not simply the name of one of its member trails.

If any condition fails, do not create a Trail Network record.

## 4.2 Common Qualifying Cases

- A regional greenway system with a published system map and named member
  trails (e.g., a blueways network with multiple named water trails)
- A statewide trail system with explicitly grouped member trails
- A county or municipal trail system where the managing agency publishes
  an explicit "trail system" map identifying named member trails
- A multi-trail corridor where a coordinating organization names and
  maps the combined system
- A metropark district's trail system — but only if the district explicitly
  presents its trails under a single system name and map; the mere existence
  of multiple trails within the district's parks does not qualify

## 4.3 Common Non-Qualifying Cases

- Multiple trails within a single park or preserve — these are Trails
  with trail_site_relationships to their parent Site, not a Trail Network
- A single long trail that crosses multiple counties — length and
  multi-county extent do not make a trail a network
- Trails that share governance or land management without a named system
  identity — common management is not system identity
- A trail described informally as part of a "system" in marketing or
  promotional materials without authoritative system documentation

## 4.4 Org-Portfolio Trail Networks

An organization managing multiple trails may warrant a Trail Network record,
but only when the organization has deliberately assembled those trails into
a named system with its own documented identity — its own name, published
membership, system map, or explicit "X trails in our Y system" framing.

The organization's mere ownership or management of multiple trails is not
sufficient. The system identity must be documented by an authoritative source.

This is a deliberate asymmetry with Site Networks. For Site Networks, the
managing organization is the anchor — a qualifying organization managing
2+ sites gets a record. For Trail Networks, the system identity is the
anchor — the organization earns a Trail Network record only by creating
and documenting a named system.

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

## 5.2 Multi-County Trail Networks
- Trail Networks whose member trails span multiple counties are created
  during the first county session that encounters the network (IMP-046).
- At creation, populate `member_trail_ids` with only the trails documented
  in the current county session. Flag partial membership in `identity_notes`
  using the PARTIAL MEMBERSHIP format defined in §3.15.
- The Trail Network TSV row lives in the first county's spreadsheet folder.
  It is not duplicated in subsequent county folders.
- When subsequent county sessions discover additional member trails, add
  entries to `trail_network_members` and update `member_trail_ids` and
  `member_trail_count`. Remove the PARTIAL MEMBERSHIP flag when all expected
  county sessions have been processed.

## 5.3 Trail Segment Inheritance
- Trail Segments do not directly belong to Trail Networks.
- Segments inherit network membership through their parent Trail.

## 5.4 Trail Networks and trail_site_relationships
- Trail Networks document which Trails are members of a system.
- The `trail_site_relationships` table (see na_trail_site_relationships_schema)
  documents which Sites a Trail passes through or is access-dependent on.
- These are separate concerns. A Trail may be a member of a Trail Network
  AND have trail_site_relationships rows for Sites along its route.
  These relationships are recorded independently in their respective tables.

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- Trail Network Vocabulary Module v6.x
- Trail Network Normalization Contract v6.x
- Trail Network TSV Output Specification v6.x
- Trail Network Discovery Sub-Procedure v6.x
- Trail Schema Module v6.x
- Trail Segment Schema Module v6.x
- na_trail_site_relationships_schema v6.x
- Resolution Engine v6.x
- Discovery Protocol Module v6.x

------------------------------------------------------------
# END OF TRAIL NETWORK SCHEMA MODULE v6.0
