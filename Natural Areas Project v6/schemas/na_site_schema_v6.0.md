# NATURAL AREAS PROJECT
# SITE SCHEMA MODULE v6.0
(Authoritative Structure, Semantic Rules, and Validation Requirements for Site Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Site Vocabulary Module v6.x**.

This module is authoritative for the structure and semantics of **Site** entities.

------------------------------------------------------------
# CHANGES FROM v5.4 → v6.0

- **Four new fields added** (IMP-011, IMP-012, IMP-013):
  - `habitat_type` — ecological/natural character of the site; open vocabulary
    initially; separate from Features (§3.11)
  - `access_notes` — seasonal access restrictions, public access status, and
    access caveats; replaces ad hoc use of Notes for access information (§3.12)
  - `last_verified_date` — date the record was last confirmed accurate against
    an authoritative source (§3.28)
  - `field_verified` — boolean; default false; set true when the user has
    physically visited the site (§3.29)
  - Field count: 26 → 30

- **Description field mandate tightened** (IMP-015): ecological and physical
  character is the priority; amenity inventory belongs in Features, not
  Description (§3.10)

- **Notes field scope tightened** (IMP-014): Notes is a customer-facing field;
  pipeline provenance artifacts must not appear here (§3.22)

- **Field-by-field rules substantially expanded**: v5.4 field definitions were
  minimal. v6.0 provides explicit guidance, what-to-do / what-not-to-do rules,
  and discovery notes for every field — consistent with Trailthing Schema v6.0
  style.

------------------------------------------------------------
# 1. PURPOSE

A **Site** is a named, bounded, identity-bearing land unit documented in
authoritative sources.

Examples include: parks, nature preserves, natural areas, wildlife areas,
state forests, historic sites, cemeteries, campuses, recreation areas,
conservation lands, greenways (when place-based rather than corridor-based),
and similar bounded land units managed or protected by a public or private entity.

A Site may be:
- A **top-level** identity-bearing land unit (standalone), or
- A **child Site** — a named, identity-bearing unit within a parent Site,
  linked via `parent_site_id`

A Site is distinct from:
- Trailthings (linear corridor entities — trails, trail systems, water trails)
- Site Networks (organizational collections of Sites)
- Access Points (entry point entities)

**The organizing principle**: A Site record is created whenever an authoritative
source documents a named, bounded land unit with a managed or protected identity.
The Site is the fundamental unit of the project's spatial inventory.

This schema is authoritative for **Site structure**.

------------------------------------------------------------
# 2. SITE FIELDS (31 FIELDS, AUTHORITATIVE ORDER)

**Identity**
1.  Name
2.  Category
3.  Subtype
4.  Designation

**Status**
5.  Status

**Organization**
6.  Ownership
7.  Governance
8.  Partner Agencies
9.  Coordination

**Character**
10. Description
11. Habitat Type
12. Features
13. Access Notes

**Geography**
14. Location
15. Acres
16. Counties
17. Municipality
18. Township
19. GPS Lat
20. GPS Lon
21. Plus Code

**Documentation**
22. Notes
23. URL Primary
24. URLs

**Verification**
25. Last Verified Date
26. Field Verified

**Hierarchy**
27. Parent Site ID

**ID**
28. Site ID
29. Created At
30. Updated At

**External IDs**
31. eBird Hotspot ID

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Name
- Use the official published name exactly as found in the authoritative source.
- Must be unique statewide (case-insensitive).
- Must not include unofficial descriptors or governance names.
- Must not include the word "County" as part of a governance qualifier.
- Must align with identity determined by the Resolution Engine v6.x.

## 3.2 Category
- Must match a value from the Site Vocabulary Module v6.x.
- Describes the primary land use or character category of the Site.
- Must reflect what the site actually is — not a GIS layer classification label.
- **GIS park type labels** ("Community Park", "Neighborhood Park", "Regional
  Park") are NOT Category values. They describe park system tier, not the
  site's fundamental character. Record GIS type labels in Identity Notes during
  discovery; they do not flow to Category.
- Must not be inferred from governance or ownership alone.

## 3.3 Subtype
- Optional.
- Must match a value from the Site Vocabulary Module v6.x for the selected
  Category.
- Provides finer-grained classification within a Category.
- Leave blank if no applicable subtype is documented or if the Category has
  no defined subtypes.
- Must not be inferred.

## 3.4 Designation
- Optional.
- Semicolon-delimited; must match values from the Site Vocabulary Module v6.x.
- Records formal designations the site holds — federal, state, or local
  protective or recognition designations.
- A site may hold multiple designations simultaneously.
- Must be explicitly documented — do not infer from governance, category, or
  land management practices.
- Examples: State Nature Preserve, National Natural Landmark, National Register
  of Historic Places, National Wildlife Refuge.

## 3.5 Status
- Optional.
- Must match a value from the Site Vocabulary Module v6.x.
- Records the current operational or management status of the Site.
- "Closed" and "Inactive" must be explicitly documented.
- Must not be inferred.
- Leave blank if the site is clearly active and no other status is documented.

## 3.6 Ownership
- Optional.
- Legal name of the entity that holds title to the land.
- Must use the full legal name — not abbreviations or generic categories.
- Must not encode governance, management, or program identity.
- Blank when ownership is distributed across multiple entities, when unclear,
  or when the site is a legal right-of-way without a single fee owner.

## 3.7 Governance
- The primary agency or organization responsible for managing the site.
- Must be an authoritative name — the organization's exact name, not a
  program label or GIS classification.
- Must not include GIS park type labels, tier labels, or programmatic names
  that do not correspond to a managing entity.
- Semicolon-delimit only when multiple co-managers have genuinely equal
  documented authority. This is rare — when in doubt, use Partner Agencies
  for secondary managers.
- Must not be inferred.

## 3.8 Partner Agencies
- Optional.
- Semicolon-delimited list of formal, documented co-operator organizations.
- Distinct from Governance: Governance is the primary manager; Partner Agencies
  are documented secondary co-operators with defined operational roles.
- Must use exact organization names.
- Must not include informal volunteer groups (those go in Coordination).
- Must not duplicate Governance.
- Must be supported by authoritative documentation — do not infer from
  adjacency or historical relationships.

## 3.9 Coordination
- Optional.
- Semicolon-delimited list of community-based, volunteer, advisory, or informal
  partners associated with this site.
- Distinct from Partner Agencies: Partner Agencies are formal co-managers with
  documented operational roles; Coordination captures friends groups, stewardship
  volunteers, advisory boards, and similar informal or community-level partners.
- Must not duplicate Governance or Partner Agencies.
- Must be documented — do not infer coordination relationships.

## 3.10 Description
- Optional, but strongly recommended for substantive natural areas.
- 1–4 sentences describing the site's character, ecological context, and
  significance.
- **Priority: ecological and physical character.** Description should answer:
  what kind of land is this, what is its ecological character, what makes it
  notable? A description that says only "a community park" or "a county park
  with trails" tells a reader nothing about the site's character.
- Good description elements: land cover type (woodland, wetland, prairie,
  riparian corridor), topography, notable ecological features, conservation
  significance, approximate scale and setting.
- May include brief establishment history, protection status narrative, or
  significant ecological context.
- **Amenity inventory belongs in Features, not here.** "Features a pavilion,
  restrooms, and a playground" is not Description — it is an amenity list.
  Amenities belong in the Features field.
- Must not be a restatement of governance, ownership, or designation fields.
- Must not include temporary conditions.
- Must not duplicate Notes content.

## 3.11 Habitat Type
- Optional.
- **New in v6.0** (IMP-011).
- Free text. Open vocabulary — do not normalize or map to a controlled list
  during v6.x. The vocabulary will be tightened after sufficient county runs
  have established what values are realistic in Ohio.
- Captures the ecological or natural character of the site — what kind of
  habitat or land cover type defines it.
- This field answers queries that Features cannot cleanly answer: "find all
  sites with wetland habitat," "find all riparian corridor sites," "find all
  old-growth woodland sites."
- **Examples of good values:**
  - "Wet prairie remnant"
  - "Oak-hickory woodland"
  - "Riparian corridor"
  - "Emergent wetland"
  - "Glacial lake"
  - "Shrub-scrub wetland"
  - "Limestone glade"
  - "Old-growth beech-maple forest"
  - "Mixed upland forest"
- **What NOT to put here:**
  - ❌ Amenities ("pavilion", "playground") — those go in Features
  - ❌ Activities ("hiking", "fishing") — those go in Features or are dropped
  - ❌ Governance or management labels ("ODNR Division of Wildlife") — those
    go in Governance
  - ❌ Category labels ("park", "preserve") — those go in Category
- Blank is acceptable for sites with no meaningful ecological character (e.g.,
  cemeteries, purely developed sites) or where ecological type is undocumented.
- Populate during discovery from authoritative source description when possible.
  May also be populated during a remediation or field verification pass.

## 3.12 Access Notes
- Optional.
- **New in v6.0** (IMP-012).
- Free text.
- Captures access information that doesn't fit other fields:
  - Seasonal access restrictions (hunting season closures, nesting season
    trail closures, seasonal road conditions)
  - Public access status detail ("open to public with permit," "day use only,"
    "no motorized vehicles," "limited hours: dawn to dusk," "no public trail
    access — conservation easement only")
  - Physical access caveats ("accessible from CR-4 only; no on-site parking,"
    "boat-in access only")
  - Temporary closures with known end dates
- Must be factual and sourced — do not infer access conditions.
- Blank if no access caveats are documented.
- Do not duplicate Status. Status captures the overall operational state of
  the site; Access Notes captures specific access conditions within an active site.

## 3.13 Location
- Optional.
- Universal geographic reference — a human-readable description of where the
  site is located, suitable for finding it without GPS.
- Include: road address, nearest intersection, township, nearest community,
  or other standard geographic reference.
- Must not include directions (turn-by-turn navigation belongs in Access Notes
  or a URL).
- Blank for sites where GPS alone is the location reference.

## 3.14 Acres
- Optional.
- Numeric only — do not include units.
- Use the officially published acreage when available.
- Never compute or estimate from GIS geometry — only record documented acreage.
- Blank if unknown or unpublished.

## 3.15 Counties
- TEXT, semicolon-delimited (stored identically in DB and TSV).
- Alphabetical order.
- Required.
- Must include all counties in which any part of the site is located.
- Must not include the word "County."
- One Site record regardless of number of counties.
- Must not include inferred counties.

## 3.16 Municipality
- Optional.
- GIS-derived only — do not populate during discovery.
- Semicolon-delimited; alphabetical order.
- The incorporated municipality or municipalities in which the site is located.
- Populated by the GIS pipeline using the Ohio MCD point-in-polygon lookup.
- Blank for sites in unincorporated township territory.

## 3.17 Township
- Optional.
- GIS-derived only — do not populate during discovery.
- Semicolon-delimited; alphabetical order.
- The civil township(s) in which the site is located.
- Populated by the GIS pipeline.
- Do not populate from source text — GIS is the only authoritative source.

## 3.18 GPS Lat
- Numeric, optional during discovery, required before statewide inclusion.
- WGS 84 decimal degrees, north positive.
- Must be explicitly stated by or derived from an authoritative source —
  never estimated, inferred, or geocoded from a street address.
- Applies the centroid of the site's primary accessible area when the site
  lacks a single documented point.
- Sites without GPS → held_entities with hold_reason "gps_missing" unless
  `gps_unresolvable = true`.

## 3.19 GPS Lon
- Numeric, optional during discovery, required before statewide inclusion.
- WGS 84 decimal degrees, west negative (Ohio values are negative).
- Same sourcing rules as GPS Lat.

## 3.20 Plus Code
- Optional.
- Derived from GPS Lat/GPS Lon — never entered manually.
- Populated by the pipeline utility (`na_plus_code.py`).
- Blank until GPS is populated.

## 3.21 Features
- Optional.
- Semicolon-delimited; must match values from the Site Vocabulary Module v6.x;
  alphabetized.
- Records the notable physical attributes, infrastructure, and ecological
  features of the site as a controlled vocabulary list.
- **Source during discovery**: raw amenity list from authoritative source —
  bullets, icons, amenity tables. Not narrative prose.
- **Activities are prohibited** (hiking, fishing, birdwatching, etc.) — they
  do not describe physical features. Map to physical infrastructure where
  possible (fishing → fishing access or boat launch) or drop.
- **Named Trail or Access Point entities are prohibited** — those are separate
  entity records.
- **Ecological character belongs in Habitat Type, not Features** — "wetland"
  and "riparian" can appear in Features when explicitly listed by the source,
  but Habitat Type is the primary field for ecological character queries.
- Must not include narrative prose — Features is a list, not sentences.
- Blank if no documented features.

## 3.22 Notes
- Optional.
- Free text.
- Use for: operational context, discovery gaps, historical context not covered
  by Description, caveats about record completeness, boundary notes.
- **Customer-facing field — no provenance artifacts.** Pipeline source
  references (MORPC batch, IMP numbers, GPS acquisition source, batch load
  dates), pipeline mechanic notes, and similar process or provenance content
  must not appear here. That information belongs in the provenance tables.
  Notes must be readable by someone who knows nothing about the pipeline.
- Must not include access information — that belongs in Access Notes.
- Must not include amenity inventory — that belongs in Features.
- Must not include ecological character — that belongs in Description or
  Habitat Type.
- Must not duplicate Description, Habitat Type, or Access Notes.

## 3.23 URL Primary
- Full https:// URL to the primary authoritative page for the site.
- For sites managed by organizations that have a Site Network record, the
  primary URL for the organization appears on the Site Network record. This
  field captures the site-specific page, if one exists.
- Must reference an authoritative source — not a third-party review or
  aggregator page.
- Tracking parameters must be removed.
- Blank if no authoritative URL exists.

## 3.24 URLs
- Optional.
- TEXT, semicolon-delimited.
- Secondary or supplementary URLs — maps, permit pages, park brochures,
  GIS layer references, state agency pages, etc.
- Must not repeat URL Primary.
- Tracking parameters must be removed.

## 3.25 Last Verified Date
- Optional.
- **New in v6.0** (IMP-013).
- DATE field (YYYY-MM-DD).
- Records the date the site record was last confirmed accurate against an
  authoritative source.
- Populate or update whenever a session actively reviews and confirms the
  record — whether during discovery, a re-check pass, or field verification.
- Does not need to be updated on pipeline re-runs that do not involve active
  record review.
- Enables staleness detection: records without a recent Last Verified Date
  are candidates for verification priority.
- Blank for records that have never been explicitly verified (batch-loaded
  records may start blank).

## 3.26 Field Verified
- Boolean, default false.
- **New in v6.0** (IMP-013).
- Set to true when the user has physically visited the site and confirmed
  its existence, access, and general character.
- Does not require exhaustive data collection — a site visit that confirms
  the site is real, accessible, and generally as described is sufficient to
  set this flag.
- Enables visit planning queries: `WHERE field_verified = false` surfaces
  sites not yet personally confirmed.
- Never set to true based on web review alone — only physical visit.
- Once set to true, do not reset to false unless the site has materially
  changed.

## 3.27 Parent Site ID
- Optional.
- FK to sites.site_id — must match OH-{COUNTY}-S-{SEQ} format.
- Populate when this Site is a named, identity-bearing unit explicitly
  contained within and part of a larger parent Site (e.g., a named natural
  area within a larger park complex).
- Must be documented by an authoritative source — not inferred from
  geographic containment or shared governance.
- A Site with parent_site_id populated must have Identity Notes containing:
  `Child of [Parent Site Name] ([parent_site_id]).`
- Must not be used for Site Network membership — that is modeled via
  `site_network_members`.

## 3.28 Site ID
- TEXT, required for referential integrity and downstream processing.
- Format: OH-{COUNTY}-S-{SEQ} (e.g., OH-OTT-S-001).
- Assigned by the Upsert Engine — not populated during discovery.
- For multi-county sites: OH-MC-S-{SEQ} format.
- Enables joins to all relationship tables (site_network_members,
  site_parent, access_point_parents, trailthing site_parent_id).

## 3.29 Created At
- TEXT, required; ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ, UTC).
- Set by the Upsert Engine at first insertion — never overwritten.

## 3.30 Updated At
- TEXT, required; ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ, UTC).
- Updated by the Upsert Engine on every upsert — ON CONFLICT DO UPDATE.

## 3.31 eBird Hotspot ID
- Optional. TEXT. Nullable.
- The eBird hotspot identifier for the corresponding eBird location, if one exists.
- Format: the eBird location code, typically `L` followed by digits (e.g., `L123456`).
- Captured during discovery when the site has a known eBird hotspot. Verify on
  the eBird Explore map (https://ebird.org/explore) — search by site name or
  navigate to the site's GPS location.
- Enables direct linking from this Site record to eBird sighting data and hotspot
  checklists in external systems.
- Leave blank when no eBird hotspot exists for this site or when one cannot be
  confirmed during discovery. Do not invent or infer.
- Not normalized — pass through verbatim from discovery.

------------------------------------------------------------
# 4. IDENTITY RULES — WHEN TO CREATE A SITE RECORD

## 4.1 The Standard

A Site record is created when **all of the following are true**:

1. An authoritative source documents a named, bounded land unit.
2. The entity has a stable, documented name — not a temporary project label,
   informal description, or purely internal inventory designation.
3. The entity is managed, owned, or protected by a public or private
   organization with documented stewardship responsibility.
4. The entity is not a Trailthing, Site Network, or Access Point.
5. The entity is not a synthetic or inferred entity.

## 4.2 Common Qualifying Cases

- Named park, preserve, wildlife area, or natural area with a documented
  managing organization
- Named cemetery with documented management
- Named campus, arboretum, or botanical garden with public access or
  conservation component
- Named historic site with documented protection or management
- Child Site — a named unit within a larger park complex, explicitly
  identified as a distinct area in authoritative sources
- A conservation easement tract with a published name and documented
  managing land trust

## 4.3 Common Non-Qualifying Cases

- An unnamed parcel or tract referenced only by ownership or acreage
- A programmatic label ("ODNR Wildlife Area") without a documented named
  site within the county
- A GIS parcel that corresponds to no named managed entity in authoritative
  sources
- A trail corridor or greenway where the primary identity is linear rather
  than place-based (use Trailthing)
- A neighborhood or subdivision with incidental green space but no documented
  natural area management

## 4.4 Identity Anchor

Top-Level Sites:
- entity_type + name + counties

Child Sites:
- entity_type + name + counties + parent_site_id

These fields alone define the ontological identity of a Site.
The Resolution Engine uses identity signatures (§4.5) to detect conflicts
and merge candidates.

## 4.5 Identity Signature

The following fields contribute to conflict detection:
- name, counties, category, subtype, designation
- municipality, township
- ownership, governance, partner_agencies
- url_primary, urls

These fields help distinguish similarly-named Sites but do not define identity.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Child Sites (parent_site_id)
- Child Sites are named, identity-bearing units within a larger parent Site.
- Parent-child relationships model genuine physical containment with documented
  separate identity — not organizational hierarchy.
- A Child Site may itself be a parent to further child Sites (unlimited nesting
  depth), provided each level has a documented name and identity.
- The `site_parent` relationship table stores these relationships.
- `parent_site_id` on the Site record is the canonical reference.

## 5.2 Site Network Membership (site_network_members)
- Sites belong to Site Networks via the `site_network_members` relationship table.
- A Site may belong to more than one Site Network simultaneously.
- Site Network membership does not affect the Site's identity or parent_site_id.
- Do not use parent_site_id to model network membership.

## 5.3 Access Points (access_point_parents)
- Access Points reference their parent Site via `access_point_parents`.
- A Site does not list its Access Points — the relationship is queried from
  the access_point_parents table.

## 5.4 Trailthings (site_parent_id on Trailthing)
- Trailthings that are access-dependent on a specific site reference it via
  `site_parent_id` on the Trailthing record.
- A Site does not list its child Trailthings — the relationship is queried
  from the trailthings table WHERE site_parent_id = [site_id].

------------------------------------------------------------
# 6. DISCOVERY GUIDANCE

## 6.1 What to Capture

During discovery, record everything the authoritative source tells you about
the site. Prioritize:

- Site name — exactly as documented
- Governance — the managing organization's exact name
- Description — narrative prose about character; ecological terms especially
- Habitat Type — any ecological or land cover language in the source
- Features — amenity list, icon list, or facilities list from source; verbatim
- Access Notes — any access restrictions, hours, permit requirements
- Acreage — only if explicitly published
- GPS coordinates — only if explicitly stated in the source
- URL — the site-specific authoritative page

## 6.2 What NOT to Populate During Discovery

- `municipality` and `township` — GIS-derived; always blank at discovery
- `plus_code` — GPS-derived; blank until pipeline run
- `site_id` — assigned by Upsert Engine
- `created_at` / `updated_at` — assigned by Upsert Engine

## 6.3 Raw Discovery Record Fields

The staging YAML uses `_raw` suffix fields during discovery:

```
name_raw:
category_raw:
subtype_raw:
designation_raw:
status_raw:
ownership_raw:
governance_raw:
partner_agencies_raw:
coordination_raw:
description_raw:
habitat_type_raw:
features_raw:
access_notes_raw:
location_raw:
acres_raw:
counties_raw: []
gps_lat_raw:
gps_lon_raw:
notes_raw:
urls_raw: []
identity_notes_raw:
discovery_tier:
seeded_from_baseline:
baseline_id:
last_verified_date:
field_verified:
```

**Notes on specific raw fields:**
- `governance_raw` — must contain only the managing organization's name; never
  GIS park type labels
- `description_raw` — narrative prose; not an amenity list
- `features_raw` — amenity LIST from source (bullets, icons); not sentences
- `habitat_type_raw` — any ecological/habitat language from the source; verbatim
- `access_notes_raw` — access restrictions and caveats; not general description
- `gps_lat_raw` / `gps_lon_raw` — only if explicitly stated by the source; never
  estimated or geocoded
- `township_raw` — always blank; GIS-derived only
- `municipality_raw` — always blank; GIS-derived only
- `last_verified_date` — no _raw suffix; date is authoritative as entered
- `field_verified` — no _raw suffix; boolean is authoritative as entered

## 6.4 Entity Type Sequence Within Tiers

Within each discovery tier, process entity types in this order:

**Sites → Trailthings → Site Networks → Access Points**

------------------------------------------------------------
# 7. FIELD SCOPE BOUNDARIES — QUICK REFERENCE

| Information Type | Correct Field |
|---|---|
| Ecological character, land cover type, habitat | `habitat_type` |
| Amenity list, facilities | `features` |
| Narrative about character, significance | `description` |
| Access restrictions, hours, permit requirements | `access_notes` |
| Operational context, discovery gaps, historical notes | `notes` |
| Identity flags, disambiguation | `identity_notes` |
| Managing org name | `governance` |
| Legal title holder | `ownership` |
| Formal protective designations | `designation` |
| Pipeline provenance, IMP numbers, source notes | **provenance tables only** |

------------------------------------------------------------
# 8. MODULE DEPENDENCIES

This module depends on:

- Site Vocabulary Module v6.x *(pending — use Site Vocabulary Module v5.x
  until v6 version is written)*
- Site Normalization Contract v6.x *(pending)*
- Site TSV Output Specification v6.x *(pending — use v5.x spec; note four
  new fields are not yet in TSV spec)*
- Site Discovery Sub-Procedure v6.x *(pending)*
- Resolution Engine v6.x *(or v5.x)*
- Normalization Engine v6.x *(or v5.x)*
- Site Network Schema Module v6.0 *(for site_network_members relationship)*
- Trailthing Schema Module v6.0 *(for site_parent_id on Trailthing)*

------------------------------------------------------------
# END OF SITE SCHEMA MODULE v6.0
