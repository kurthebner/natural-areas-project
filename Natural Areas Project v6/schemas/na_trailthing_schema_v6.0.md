# NATURAL AREAS PROJECT
# TRAILTHING SCHEMA MODULE v6.0
(Authoritative Structure, Semantic Rules, and Validation Requirements for Trailthing Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trailthing Vocabulary Module v6.x**.

This module is authoritative for the structure and semantics of **Trailthing** entities.

------------------------------------------------------------
# WHAT IS A TRAILTHING

"Trailthing" is a working name for the unified interim entity type that replaces
Trail, Trail Segment, and Trail Network in the v6.x architecture.

The name is intentional. "Trailthing" carries no semantic implication about whether
the entity is a trail, a trail system, a trail network, a segment, a connector, a
route, or any other sub-classification. That classification is deferred — it will
emerge from data, not from schema.

When this document and other v6 modules say **Trailthing**, they mean this unified
entity type.

When they say **trail**, **trail network**, **trail segment**, **greenway**, **route**,
or any other term, they are referring to real-world things as authoritative sources
describe them — not to schema entity types.

This distinction is critical during discovery: the discoverer's job is to capture
what authoritative sources say, not to decide which kind of Trailthing something is.

------------------------------------------------------------
# SUPERSEDES

This module supersedes:
- Trail Schema Module v5.x (and any v6.x draft)
- Trail Segment Schema Module v5.x (and any v6.x draft)
- Trail Network Schema Module v6.0 (`na_trail_network_schema_v6.0.md`)

Those modules remain in the repository as reference material for the design decisions
they document. For active discovery and normalization under v6.x, this module is
authoritative.

------------------------------------------------------------
# 1. PURPOSE

A **Trailthing** is any named, identity-bearing trail-related entity documented in
authoritative sources — including but not limited to what would previously have been
classified as a Trail, Trail Segment, or Trail Network.

Examples include:
- A named regional trail system or greenway network
- A named water trail or blueway
- A named hiking, biking, equestrian, or multi-use trail
- A named section, segment, or reach of a larger trail
- A named connector trail, spur trail, or loop trail
- A named trail corridor, route, or hub
- A statewide trail system or national scenic trail system
- A heritage trail within a National Heritage Area or scenic corridor

A Trailthing is distinct from:
- Sites and Site Networks (place-based entities, not linear corridors or trail systems)
- Access Points (entry point entities, not linear corridors)

**The organizing principle**: A Trailthing is created whenever an authoritative source
documents a named trail-related entity. The hierarchical relationship between
Trailthings — which is a system, which is a member trail, which is a section — is
captured through the `parent_id` field and the `source_term` / `source_hierarchy_context`
fields, not through entity type classification. Classification will be determined
systematically once sufficient data has been collected across county runs.

This schema is authoritative for **Trailthing structure**.

------------------------------------------------------------
# 2. TRAILTHING FIELDS (28 FIELDS, AUTHORITATIVE ORDER)

**Identity**
1.  Name
2.  Alternate Names
3.  Source Term
4.  Source Hierarchy Context

**Hierarchy**
5.  Parent ID
6.  Site Parent ID
7.  Parent Site Network ID

**Character**
8.  Use Type
9.  Surface Type
10. Origin Type
11. Org Type

**Status**
12. Status
13. Difficulty
14. Accessibility

**Organization**
15. Ownership
16. Governance
17. Partner Agencies
18. Coordination

**Geography**
19. Counties
20. States Included
21. Total Length (Miles)

**Documentation**
22. Description
23. Trail History
24. Identity Notes
25. Notes
26. URL
27. Maps

**ID**
28. Trailthing ID

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Name
- Use the official published name exactly as found in the authoritative source.
- Must be unique statewide (case-insensitive).
- Must not include unofficial descriptors.
- Must align with identity determined by the Resolution Engine v6.x.

## 3.2 Alternate Names
- Optional.
- TEXT, semicolon-delimited.
- Include only documented historical names, variant names, abbreviations, or
  formally used alternate designations.
- Must not include marketing names or slogans.
- Must not repeat Name.

## 3.3 Source Term
- The exact word or phrase the authoritative source uses to describe what kind
  of entity this is.
- Examples: "regional trail system," "greenway," "water trail network," "connector
  trail," "spur," "loop trail," "blueway," "trail hub," "route," "corridor,"
  "rail-trail," "heritage trail," "section," "reach."
- Free text. Verbatim from source. Do not normalize or map to a controlled vocabulary.
- This field is the primary input for future Trailthing hierarchy pattern analysis.
  Consistent, verbatim capture across all county runs is essential.
- Leave blank only if the source provides no descriptive term — do not invent one.

## 3.4 Source Hierarchy Context
- Optional.
- How the authoritative source frames this entity in relation to other entities.
- Captures relational framing: "part of the X System," "one of seven member trails,"
  "a section of the Y Trail," "connecting A Park and B Park," "the northern reach of
  the Z Blueway."
- Free text. Verbatim or close paraphrase from source.
- Do not interpret or classify — record what the source says.
- Leave blank if the source provides no hierarchical context.

## 3.5 Parent ID
- Optional.
- The Trailthing ID (OH-{COUNTY}-TT-{SEQ} or OH-MC-TT-{SEQ}) of the parent
  Trailthing entity.
- Populate when the authoritative source explicitly frames this entity as a
  component, member, section, or part of another Trailthing-type entity.
- Must not be inferred from geography, governance, or name similarity alone.
- A Trailthing may have at most one parent Trailthing.
- Leave blank for top-level entities — systems or standalone Trailthings with
  no documented parent relationship.

## 3.6 Site Parent ID
- Optional.
- FK to the sites table (site_id).
- Populate when the authoritative source explicitly frames this Trailthing as
  contained within, or primarily accessed via, a specific named site — and the
  Trailthing's access and legal existence depend on that site.
- Must not be inferred from proximity, geography, or shared governance alone.
- Must not be populated for Trailthings that merely pass through or are adjacent
  to a site without access dependency.
- Leave blank for extra-limital Trailthings that cross multiple sites or have
  an existence independent of any single site.

## 3.7 Parent Site Network ID
- Optional.
- FK to the site_networks table (network_id).
- Populate when the authoritative source explicitly frames this Trailthing as a
  member or component of a Site Network — for example, a heritage trail within a
  National Heritage Area, or a water trail within a scenic river corridor.
- Must not be inferred.
- A Trailthing with parent_site_network_id populated must have identity_notes
  containing: `Member of [Site Network Name] ([network_id]).`

## 3.8 Use Type
- Optional.
- Must match a value from the Trailthing Vocabulary Module v6.x.
- Describes the primary intended use of this Trailthing.
- Most applicable to leaf-level navigable Trailthings. System-level Trailthings
  may leave blank or use "Multi-Use" if the system explicitly encompasses multiple
  use types.
- Must not be inferred.

## 3.9 Surface Type
- Optional.
- Must match a value from the Trailthing Vocabulary Module v6.x.
- Describes the predominant surface type.
- Use "Mixed" only when explicitly documented by an authoritative source.
- Must not encode use type or origin.
- **Unnamed surface variation is Notes territory, not entity territory.**
  A trail whose surface changes from paved to crushed limestone mid-route
  does not require multiple Trailthing records. Document the variation in
  Notes. Physical geometry at this granularity is GIS phase work, not
  discovery work. Only create separate child Trailthings for surface
  variation when the source itself names and documents those sections as
  distinct identity-bearing entities.

## 3.10 Origin Type
- Optional.
- Must match a value from the Trailthing Vocabulary Module v6.x.
- Describes the historical or structural origin of this Trailthing.
- Examples: Rail-Trail, Canal Towpath, Purpose-Built, Former Roadway.
- Must not be inferred.

## 3.11 Org Type
- Optional.
- Must match a value from the Trailthing Vocabulary Module v6.x.
- Classifies the organizational category of the primary governance entity
  responsible for coordinating or managing this Trailthing.
- **Descriptive only** — carries no threshold or identity-gate function.
- Most applicable to system-level Trailthings. Leaf-level Trailthings may leave
  blank unless explicitly documented.
- Must not be inferred from use_type, origin_type, or governance name alone.

## 3.12 Status
- Must match a value from the Trailthing Vocabulary Module v6.x.
- Describes the current operational status of the Trailthing as a whole.
- "Planned," "Gap," and "Closed" must be explicitly documented.
- Must not be inferred.
- **Unnamed status variation is Notes territory, not entity territory.**
  A trail that is open along most of its length but has a closed section
  does not require multiple Trailthing records. Document the variation in
  Notes. Only create separate child Trailthings for status variation when
  the source itself names and documents those sections as distinct
  identity-bearing entities.

## 3.13 Difficulty
- Optional.
- Must match a value from the Trailthing Vocabulary Module v6.x.
- Must be explicitly stated by the trail manager or an authoritative source.
- Must not be assessed or inferred by the discoverer.
- Blank if not documented.

## 3.14 Accessibility
- Optional.
- Free-text description of ADA compliance, wheelchair accessibility, surface
  grade, width, and accessible facilities.
- Record what authoritative sources state.
- Must not be inferred from surface type or use type alone.
- Blank if not documented.

## 3.15 Ownership
- Optional.
- Legal name of the entity that owns the corridor, system, or right-of-way.
- Must not use generic categories.
- Blank when ownership is distributed across multiple entities, when the
  Trailthing is a coordinating or designating body without land ownership,
  or when unclear.
- Blank is correct and common — many trail systems are coordinating or
  designating bodies rather than land owners.

## 3.16 Governance
- The primary agency or organization responsible for managing or coordinating
  this Trailthing.
- Must be an authoritative name.
- Must not be inferred.
- Semicolon-delimit if multiple co-managers with genuinely equal authority.
- **Unnamed governance variation is Notes territory, not entity territory.**
  A trail that passes through sections managed by different agencies does
  not require multiple Trailthing records. Document the variation in Notes.
  Only create separate child Trailthings for governance variation when the
  source itself names and documents those sections as distinct
  identity-bearing entities.

## 3.17 Partner Agencies
- Optional.
- Semicolon-delimited list of secondary managing agencies or documented
  organizational partners.
- Must not duplicate Governance.
- Must not include inferred partners.

## 3.18 Coordination
- Optional.
- Semicolon-delimited list of community-based, volunteer, advisory, or informal
  partners associated with this Trailthing.
- Distinct from Partner Agencies: Partner Agencies are formal co-managers with
  documented operational roles; Coordination captures trail stewardship volunteers,
  friends groups, trail associations, advisory boards, and similar informal or
  community-level partners.
- Must not duplicate Governance or Partner Agencies.
- Must be documented — do not infer coordination relationships.

## 3.19 Counties
- TEXT, semicolon-delimited (stored identically in DB and TSV).
- Alphabetical order.
- Must include all counties through which any part of this Trailthing passes or
  in which it exists.
- Must not include the word "County."
- One Trailthing record regardless of number of counties.
- Must not include inferred counties.

## 3.20 States Included
- Optional.
- TEXT, semicolon-delimited.
- Alphabetical order.
- Only used for multi-state Trailthings.
- Blank for Ohio-only Trailthings — do not write "Ohio."
- Must not include inferred states.

## 3.21 Total Length (Miles)
- Optional.
- Numeric only.
- Use officially published total length when available.
- Never compute by summing child Trailthing lengths unless an authoritative
  source explicitly does so.
- Blank if unknown or undocumented.

## 3.22 Description
- 1-3 sentences describing the Trailthing's identity, scope, and character.
- **Priority: physical and ecological character.** Describe what the corridor
  or system is like — its terrain, setting, natural context, and defining
  character. A description that says only "a multi-use trail" tells a reader
  nothing about the experience or environment.
- Must describe identity-defining characteristics: purpose, geographic scope,
  use, notable features of the system or corridor.
- May include brief establishment history or origin context.
- **Amenity inventory belongs in Notes, not here.** Description is not a list
  of facilities. "Features a pavilion, restrooms, and parking" belongs in Notes
  if it belongs anywhere — not in Description.
- Must not include temporary conditions.
- Must not duplicate content from Source Term, Source Hierarchy Context, or
  Identity Notes.

## 3.23 Trail History
- Optional.
- 1-3 sentences of factual, documented historical context.
- Use for: rail corridor origin, canal conversion, federal designation history,
  established date, former names, or major route changes.
- Must be factual and sourced.
- Must not include speculative or inferred history.

## 3.24 Identity Notes
- Optional free-text field for identity clarifications.
- Use for: hierarchy uncertainty, name conflicts, cross-entity relationship
  notes, membership uncertainty, flag rationale.
- **TRAIL_HIERARCHY_UNCERTAIN** — use when the source framing is ambiguous about
  whether this Trailthing is a system-level entity, a navigable trail, or a
  component of something larger:
  ```
  TRAIL_HIERARCHY_UNCERTAIN — [description of specific ambiguity and source evidence]
  ```
- **PARTIAL MEMBERSHIP** — for multi-county Trailthings where not all child
  Trailthings have yet been documented:
  ```
  PARTIAL MEMBERSHIP: Only [County] County child Trailthings documented
  as of [date]. Additional members expected from [County2], [County3] sessions.
  ```
- Must not duplicate Notes content.

## 3.25 Notes
- Optional free-text field.
- Use for: gap documentation, planning status, partial completion notes, access
  restrictions, seasonal conditions, funding context, amenity details that don't
  belong in Description.
- **Use for unnamed variation along a Trailthing's corridor** — surface changes,
  governance handoffs between agencies, sections with different status (a closed
  segment, a gap, a planned extension). This is the correct home for physical and
  operational variation that does not rise to the level of a named, source-documented
  entity. Do not create child Trailthings to represent this variation; document it
  here instead.
- **Customer-facing field — no provenance artifacts.** Pipeline source references,
  IMP numbers, batch load notes, GPS source citations, and similar process or
  provenance content must not appear here. That information belongs in the
  provenance tables. Notes must be readable by someone who knows nothing about
  the pipeline.
- Must not include identity-defining characteristics (those belong in Description
  or Identity Notes).

## 3.26 URL
- Full https:// URLs only.
- Semicolon-delimit if multiple authoritative URLs.
- Must reference authoritative sources.
- Tracking parameters must be removed.

## 3.27 Maps
- Optional.
- Semicolon-delimited list of URLs to map resources.
- Includes: PDF trail maps, GPX/KML files, interactive map viewers, GIS layers,
  strip maps, elevation profiles.
- Distinct from URL — maps are navigation and geometry resources; URL is the
  Trailthing's web presence.
- Leave blank if none.

## 3.28 Trailthing ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- TEXT in OH-{COUNTY}-TT-{SEQ} format.
- For multi-county Trailthings: OH-MC-TT-{SEQ} format.
- Enables joins to the trailthing_hierarchy relationship table and cross-entity
  parent relationship tables.

------------------------------------------------------------
# 4. IDENTITY RULES — WHEN TO CREATE A TRAILTHING RECORD

## 4.1 The Standard

A Trailthing record is created when **all of the following are true**:

1. An authoritative source documents a named entity that is a trail, trail system,
   trail network, trail section, greenway, water trail, or similar linear recreational
   corridor or system.
2. The entity has a stable, documented name — not a temporary project label,
   informal description, or marketing slogan.
3. The entity is not a Site, Site Network, or Access Point.
4. The entity is not a synthetic or inferred entity.

**Do not attempt to determine** during discovery whether the Trailthing is a trail,
trail network, trail segment, or any other sub-classification. Capture `source_term`
and `source_hierarchy_context` to preserve how the authoritative source describes
the entity, and record parent relationships only when the source explicitly documents
them.

## 4.2 Common Qualifying Cases

- A named regional greenway system or trail network with a published map or
  membership documentation
- A named water trail, blueway, or paddling route
- A named hiking, biking, equestrian, or multi-use trail
- A named section, reach, or segment when the source names and documents it
  distinctly
- A named connector trail, spur, or loop
- A named heritage trail within a National Heritage Area or scenic corridor
- A statewide or national trail system with documented identity

## 4.3 Common Non-Qualifying Cases

- An unnamed path, route suggestion, or informal connection
- A trail described only informally in marketing materials with no authoritative
  documentation of a distinct identity
- An unnamed path within a site that the managing agency has not documented as
  a distinct trail
- A synthetic entity assembled from geographic proximity rather than documented
  source identity

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Trailthing Hierarchy (parent_id)
- The `trailthing_hierarchy` relationship table stores parent-child relationships:
  - `parent_id` (FK to trailthings)
  - `child_id` (FK to trailthings)
- `parent_id` on the Trailthing record is a convenience field — the relationship
  table is authoritative.
- A Trailthing may have at most one parent Trailthing.
- A Trailthing may have any number of child Trailthings.
- Hierarchy depth is not constrained — a system may contain multiple levels of
  named entities.
- **Do not infer hierarchy** from geography, governance, or name similarity.
  Only record parent_id when the authoritative source explicitly frames the
  relationship.

## 5.2 Site Parent (site_parent_id)
- Records the FK to the sites table when a Trailthing is explicitly contained
  within and access-dependent on a specific site.
- A Trailthing with site_parent_id populated must have identity_notes containing:
  `Contained within [Site Name] ([site_id]).`
- A Trailthing must NOT have site_parent_id populated if it crosses multiple
  sites, spans multiple governance units, or has an existence independent of
  any single site.

## 5.3 Site Network Parent (parent_site_network_id)
- Records when a Trailthing is an explicit member of a Site Network.
- FK to the site_networks table (network_id).
- The referenced Site Network record does not yet carry member_trailthing_ids —
  this will be added in a future revision per IMP-010.

## 5.4 Multi-County Trailthings
- Created during the first county session that encounters the Trailthing,
  consistent with IMP-046.
- At creation, document partial membership in identity_notes using the
  PARTIAL MEMBERSHIP format defined in §3.25.
- The Trailthing record lives in the first county's spreadsheet folder.
  Not duplicated in subsequent county folders.
- When subsequent county sessions discover additional child Trailthings, add
  entries to trailthing_hierarchy and update parent_id references on child records.
  Remove the PARTIAL MEMBERSHIP flag when all expected county sessions have
  been processed.

## 5.5 Access Points
- Access Points may reference a Trailthing as their identity parent via
  `identity_parent_entity_id`.
- A Trailthing does not list its Access Points.

------------------------------------------------------------
# 6. DISCOVERY GUIDANCE

## 6.1 What to Capture

During discovery, record everything the authoritative source tells you without
pre-classifying the entity's position in a hierarchy:

- Capture `source_term` verbatim — "trail system," "greenway," "water trail,"
  "section," "hub," "route," "connector," whatever the source says
- Capture `source_hierarchy_context` when the source describes how this entity
  relates to other entities
- Record `parent_id` only when the source explicitly states this entity is a
  component of another documented Trailthing
- Record `site_parent_id` only when the source explicitly states this entity is
  contained within and access-dependent on a specific site
- Record `parent_site_network_id` only when the source explicitly frames this
  entity as a member of a Site Network

## 6.2 What Not to Decide

During discovery, **do not decide**:
- Whether this Trailthing is a "trail network" vs. a "trail" vs. a "trail segment"
- Whether a child Trailthing "should" be a trail or a segment
- Whether a parent Trailthing "should" be a trail network or a trail
- What level in a hierarchy this Trailthing occupies

These decisions will be made systematically after sufficient data has been collected
across county runs (target: 30 counties under v6, per IMP-007). The source_term and
source_hierarchy_context fields, populated consistently, will provide the empirical
basis for those decisions.

## 6.3 Entity Type Sequence Within Tiers

Within each discovery tier, process entity types in this order:

**Sites → Trailthings → Site Networks → Access Points**

Trail Networks, Trails, and Trail Segments are no longer processed as separate
entity types. All are captured as Trailthings.

------------------------------------------------------------
# 7. TSV OUTPUT NOTE

The authoritative TSV output specification for Trailthings is
`na_tsv_output_trailthing_v6.0.md`. That specification defines 31 TSV fields:
the 28 schema fields minus 3 name-pairing fields added for human readability
(`parent_name`, `site_parent_name`, `parent_site_network_name`), plus the
Trailthing ID. See that module for canonical field order, delimiter rules, and
validation requirements.

Note: the TSV spec was written before the External Parent Type field was removed
from the schema. The TSV field count (31) and the schema field count (28) are
consistent: 28 schema fields + 3 TSV-only name-pair fields = 31.

------------------------------------------------------------
# 8. MODULE DEPENDENCIES

This module depends on:

- Trailthing Vocabulary Module v6.x *(pending — use Trail Vocabulary Module v5.x
  for Use Type, Surface Type, Origin Type, Status, Difficulty; Trail Network
  Vocabulary Module v5.x for Org Type until v6 vocabulary is written)*
- Trailthing Normalization Contract v6.x *(pending)*
- Trailthing TSV Output Specification v6.x *(pending)*
- Trailthing Discovery Sub-Procedure v6.x *(pending)*
- Site Schema Module v6.x *(or v5.x — for site_parent_id references)*
- Site Network Schema Module v6.0 *(for parent_site_network_id references)*
- Resolution Engine v6.x *(or v5.x)*
- Discovery Protocol Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF TRAILTHING SCHEMA MODULE v6.0
