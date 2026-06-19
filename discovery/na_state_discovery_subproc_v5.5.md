# NATURAL AREAS PROJECT
# STATE LANDS DISCOVERY SUB-PROCEDURE v5.7
(Tier 2 — ODNR Divisions, OHC, ODOT, OTIC, State Easements, Scenic Rivers, Public Universities)

This module defines the authoritative, deterministic Tier-2 discovery rules for
state-managed and state-affiliated lands within the v5.x Raw → Resolution →
Normalization → Entity Graph pipeline.

This module supersedes State Lands Discovery Sub-Procedure v5.6.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.6 → v5.7

- **IMP-132**: Added ODNR Ohio Lake Map Resource to §3.3 Division of Wildlife — new
  mandatory GIS source for fishing lake and wildlife area centroids. Documents ArcGIS
  Experience URL and cross-references na_gps_acquisition §5.9 for GPS workflow.
- **IMP-133**: Added §3.7 State-Owned Real Property (SORP) — new mandatory cross-agency
  enumeration and GPS source. Documents SORP program URL, ArcGIS Export Tool URL, project
  CSV asset (`SORP_Parcels_2023.csv`), when to use (enumeration completeness, GPS acquisition,
  county ambiguity), and data limitations.

------------------------------------------------------------
# CHANGES FROM v5.5 → v5.6

- **IMP-029**: Added Pre-Discovery Checklist cross-reference to §5.1 — after enumerating
  state units and agencies from listing pages and before fetching individual entity pages,
  the entity list must be written to the handoff's Pre-Discovery Checklist. Prevents
  redundant re-enumeration after context breaks.
- **IMP-030**: Added Captured Source Data cross-reference to §5.1 — when a structured
  source table (ODNR property directory, preserve inventory, unit listing with addresses)
  is fetched, it must be written verbatim to the handoff's Captured Source Data section
  immediately, not deferred to staging time.

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- **IMP-003 — Public university natural areas**: Added §2.3 entry and §4.7 (Public
  University Natural Areas). Public universities are state institutions; their natural
  areas, nature preserves, arboreta, and research wetlands that are open to the public
  or formally designated are Tier 2 entities. `governance_raw` captures the university
  name; `ownership_raw` captures the state. Private universities are excluded from
  Tier 2 — they fall to Tier 8 if encountered.
- **Fixed duplicate §4.5 numbering**: Water Trail Tier Assignment (added in v5.4 with
  incorrect §4.5 number) renumbered to §4.6. OTIC retains §4.5 (original assignment
  from v5.1). Public university section added as §4.7.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- Updated §3.5 ODNR Scenic Rivers Program — IMP-008: corrected entity type for scenic river
  designations from Site Network to Site (category=Water Site, subtype=River,
  designation=State Scenic River or National Wild and Scenic River). The scenic designation
  is a legal status attribute, parallel to State Nature Preserve and NNL, not a category.
- Updated §6.6 Site Network Creation to remove Scenic River corridors as an example
  (they are now Sites, not Site Networks).
- Added §4.5 Water Trail Tier Assignment — IMP-009: management tier governs for
  state-designated, locally-managed water trails; the ODNR designation is a status attribute
  captured in the `designation` field of the Trail entity.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- Added `description_raw` to Metadata Requirements — must be captured when a narrative description exists on the source page; distinct from `features_raw`
- Added first-pass capture rule to §5.1: when fetching a state unit page, extract description_raw and features_raw in the same fetch — no deferred return visits
- Bumped version to v5.3

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Updated all cross-module references to v5.x
- Fixed duplicate section numbering (Multi-County Uncertainty was §7, now §8)
- Updated header version to v5.2

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **URL-01**: Added §3.0 ODNR Find-a-Property as mandatory primary enumeration tool
- **URL-02**: Added Hunting Area Maps to §3.3 Division of Wildlife
- **URL-03**: Added Fishing Lake Maps to §3.3 Division of Wildlife
- **URL-04**: Added River & Stream Fishing Maps to §3.3 Division of Wildlife
- **URL-06**: Added ODNR Historic Places to §4.1 OHC
- **URL-07**: Added ODNR New Deal Era Sites to §4.1 OHC
- **URL-08**: Added ODOT Rest Areas to §4.2 ODOT
- **URL-09**: Added new §4.5 Ohio Turnpike & Infrastructure Commission (OTIC)
- **URL-09**: Added ohioturnpike.org (conditional) to §5.3 recursion allowlist
- **URL-11**: Added Cardinal Collection to §3.1 Parks & Watercraft as supplemental source
- **OBS-006**: Added §7 Multi-County Uncertainty Handling with GIS_VERIFY_COUNTY flag

------------------------------------------------------------
# CHANGES FROM v4.0

- `role_raw` and `access_level_raw` removed from output — deleted from Access Point schema
- `features_raw` added to output for Access Point and Site amenities
- `difficulty_raw` and `accessibility_raw` added to output for Trails and Trail Segments
- `maps_raw` removed; map URLs now included in `urls_raw`
- `township_raw` and `municipality_raw` explicitly prohibited — GIS-derived only
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The State Lands Discovery Sub-Procedure v5.x defines how Tier 2 must:

- Identify all state-managed Sites
- Identify child Sites within state Sites
- Identify Trails, Trail Segments, and Trail Networks on state lands
- Identify Site Networks (e.g., Scenic River systems)
- Identify Access Points associated with state Sites
- Distinguish ODNR divisions, OHC, ODOT, EPA/ODA, and co-management arrangements
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Discovery Records v5.x
- Produce Discovery Metadata v5.x

This module is referenced only by:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x

------------------------------------------------------------
# 2. SCOPE

This sub-procedure applies to all state-level landholders and affiliated entities.

## 2.1 Primary State Agencies
- ODNR Division of Parks & Watercraft
- ODNR Division of Forestry
- ODNR Division of Wildlife
- ODNR Division of Natural Areas & Preserves
- ODNR Scenic Rivers Program
- ODNR Division of Mineral Resources (surface-managed lands only)

## 2.2 Quasi-State Organizations
- **Ohio History Connection (OHC)**
  (state memorials, archaeological preserves, historic landscapes)

## 2.3 Other State-Level Landholders
- **ODOT** (scenic overlooks, bikeway corridors, mitigation lands)
- **EPA / DEFA** (mitigation lands; conditional)
- **ODA** (agricultural easements; conditional)
- **Public universities** (nature preserves, arboreta, research wetlands, open-access natural areas on campus) — see §4.7

## 2.4 State-Managed Easements
- Conservation easements
- Scenic River easements
- ODNR-managed access easements

Tier 2 sits **below Federal** and **above District-Level**.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 2 must enumerate and recursively explore the following authoritative sources.

## 3.0 ODNR Find-a-Property (Primary Enumeration Tool — Run First)

Before working through individual ODNR divisions, enumerate all ODNR-managed
properties in the county using the Find-a-Property search with each property type.
This is the fastest way to confirm whether any ODNR entity exists in the county
and prevents gaps from division-specific searches missing cross-listed properties.

URL pattern:
```
https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/find-a-property-search?type={TYPE}
```

Known type values (search each for the county):
- `Wildlife%20Area`
- `State%20Park`
- `State%20Forest`
- `State%20Nature%20Preserve`
- `Scenic%20River`

NOTE: This is a JavaScript-rendered page. Use Claude in Chrome for interactive
browsing, or reference the division-specific listing pages below for text-parseable
results. Results from this step define the expected entity inventory for the county
before division-level searches begin.

## 3.1 ODNR Division of Parks & Watercraft
Required sources:
- ODNR park pages
- ODNR park maps
- ODNR GIS datasets

Check for:
- State parks → Sites
- Campgrounds → child Sites
- Day-use areas → child Sites
- Marinas → child Sites or Access Points
- Boat ramps → Access Points
- Trails → Trails, Trail Segments

Supplemental source (child Sites and historic features):
- **THE CARDINAL COLLECTION**:
  `https://hub.catalogit.app/the-cardinal-collection`
  ODNR's digital archive on CatalogIt. Search for the county's state park(s) to
  identify named internal features: cemeteries, historic structures, CCC features.
  These are candidate child Sites. Not a property inventory — use as a cross-check
  after primary discovery is complete.

## 3.2 ODNR Division of Forestry
Required sources:
- ODNR forestry pages
- ODNR forest maps
- ODNR GIS datasets

Check for:
- State forests → Sites
- Forest management units → child Sites
- Forest trails → Trails, Trail Segments

## 3.3 ODNR Division of Wildlife
Required sources:
- ODNR wildlife area pages
- ODNR wildlife GIS datasets
- **HUNTING AREA MAPS** (mandatory):
  `https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/hunting-area-maps`
  Search for the county name in the table. Captures multi-county wildlife areas
  that may not appear in county-specific searches. Contains 150+ entries including:
  Wildlife Area, Public Hunting Area, Field Trial Area, Education Area - No Hunting,
  Wildlife Agreement Area, Recreation Area. Download PDF maps for confirmed areas.
- **FISHING LAKE MAPS** (mandatory):
  `https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/fishing-lake-maps`
  Search for county name. ODNR-managed fishing lakes are identity-bearing sites and
  may include access points (boat ramps, fishing piers).
- **RIVER & STREAM FISHING MAPS** (mandatory):
  `https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/river-stream-fishing-maps`
  Search for county name. Named fishing reaches may generate:
    - Access Points (fishing access, boat ramps)
    - Trail records (if paddling trails are documented)
    - Sites (if ODNR has designated a named area)
- **ODNR OHIO LAKE MAP RESOURCE** (mandatory for wildlife area and fishing lake GPS):
  `https://experience.arcgis.com/experience/2a39044c75b04e68872564b4c6ec0638`
  ArcGIS Experience viewer mapping all ODNR Division of Wildlife–managed fishing lakes and
  associated access features across Ohio. Use to acquire GPS centroids for DOW-managed fishing
  lakes and wildlife areas that do not appear in OSM or resolve cleanly via Nominatim.
  Cross-check entity name against the layer's SITE_NAME attribute; confirm county match before
  accepting. Also useful for confirming county placement of multi-county wildlife areas.
  See na_gps_acquisition.md §5.9 for GPS provenance protocol (`acquisition_method: "odnr_lake_map"`).

Check for:
- Wildlife areas → Sites
- Hunting units → child Sites
- Fishing access points → Access Points
- Wildlife area trails → Trails

## 3.4 ODNR Division of Natural Areas & Preserves (DNAP)
Required sources:
- DNAP preserve pages
- DNAP maps
- DNAP GIS datasets

Check for:
- State nature preserves → Sites
- Preserve units → child Sites
- Preserve access points → Access Points
- Preserve trails → Trails

## 3.5 ODNR Scenic Rivers Program
Required sources:
- Scenic River program pages
- Scenic River maps
- Scenic River GIS datasets

Check for:
- **Scenic River designations → Sites** (category=Water Site, subtype=River,
  designation=State Scenic River and/or National Wild and Scenic River as applicable).
  Do NOT create Site Networks for scenic river designations — the scenic designation is a
  legal status attribute handled by the Designation field, parallel to State Nature Preserve
  and NNL. See Discovery Protocol v5.x §17.2 for the full rule.
- **Scenic River access points → Access Points** (parented to the scenic river Site)
- **Water trail entities within a scenic river corridor → Trail or Trail Segment records**
  (separate from the Water Site; flag overlapping records — see §4.5)

## 3.6 ODNR Mineral Resources
Required sources:
- ODNR mineral resources datasets

Check for:
- Surface-managed lands → Sites
- Public access areas → Access Points

Always **fetch** official ODNR pages directly — do not rely on search snippets alone.
Extract ALL entities listed on division pages, not just those prominently featured.

## 3.7 State-Owned Real Property (SORP) — Cross-Agency Enumeration and GPS Source ✨ NEW IN v5.7 (IMP-133)

The State of Ohio maintains a comprehensive inventory of all state-owned real property through
the Department of Administrative Services (DAS) / Ohio Geographic Reference and Index System
(OGrIP). SORP covers all state agencies — ODNR, OHC, ODOT, state universities, and others —
in a single cross-agency parcel dataset.

**Program URL** (background, data dictionary, and update schedule):
```
https://das.ohio.gov/technology-and-strategy/ogrip/projects/sorp
```

**ArcGIS Export Tool** (download tabular parcel data filtered by county or agency):
```
https://experience.arcgis.com/experience/802e2079e2e4448e819cee71e4fefe92/page/State-Owned-Property-Data-Export-Tool
```

**Project asset**: `SORP_Parcels_2023.csv` — statewide SORP export at the project root.
Filter by county FIPS or county name for targeted lookups. Note the 2023 data year in GPS
provenance when coordinates are sourced from this file.

### When to Use

1. **Enumeration completeness check** — after working through individual division listing
   pages (§3.1–§3.6), query SORP for the county to confirm no state-owned parcels are
   absent from the entity list.
2. **GPS / centroid acquisition** — for state entities not in OSM and not geocodable via
   Nominatim. SORP parcel records carry centroid coordinates (or polygon from which a centroid
   can be derived); this is an acceptable GPS representative point. See na_gps_acquisition.md §5.9
   for the full SORP GPS workflow (`acquisition_method: "sorp_gis"`).
3. **County ambiguity resolution** — for multi-parcel or border-adjacent state holdings,
   SORP provides parcel-level county assignment to arbitrate the primary county.

### Limitations

- SORP records ownership, not managed public access. A parcel in SORP does not confirm public
  access; verify access independently from the managing agency's website or signage.
- SORP data is updated periodically. Verify managing agency for recently transferred parcels
  against the current division page.
- The project CSV (`SORP_Parcels_2023.csv`) is a 2023 snapshot; always note the data year
  in GPS provenance metadata.

All sources must be logged in **Discovery Metadata v5.x**.

------------------------------------------------------------
# 4. DOMAIN RULES FOR STATE LAND DISCOVERY

## 4.1 Ohio History Connection (OHC)
Required sources:
- OHC site pages
- OHC GIS datasets
- National Register listings (cross-reference only)
- **ODNR HISTORIC PLACES** (mandatory):
  `https://ohiodnr.gov/go-and-do/see-the-sights/historic-places/lets-get-historic-sites`
  NOTE: JavaScript-rendered — use Claude in Chrome or cross-reference with NRHP.
  Captures cemeteries, mounds, and historic structures on ODNR land. These are
  distinct from OHC holdings and may not appear in OHC or NRHP searches.
- **ODNR NEW DEAL ERA SITES** (mandatory when county has state parks or forests):
  `https://ohiodnr.gov/go-and-do/see-the-sights/historic-places/new-deal-era-sites/new-deal-era-sites`
  NOTE: JavaScript-rendered — use Claude in Chrome or cross-reference with NRHP.
  New Deal sites (CCC camps, WPA shelters, historic districts) are candidate child
  Sites within state parks and forests. May be NRHP-listed.

Check for:
- State memorials → Sites
- Archaeological preserves → Sites
- Historic landscapes → Sites
- Mound sites → Sites
- Cultural preserves → Sites

## 4.2 ODOT
Required sources:
- ODOT GIS
- ODOT project pages
- ODOT bikeway datasets
- **ODOT REST AREAS** (mandatory):
  `https://www.transportation.ohio.gov/traveling/rest-areas`
  NOTE: JavaScript-rendered map — use Claude in Chrome or search for county.
  Rest areas with outdoor recreation features are identity-bearing Sites:
    - Dog trails → Trail record
    - Storybook Trails → Trail record
    - Native plant areas → feature note on Site record
  Rest areas without outdoor/recreation features: document but do not create
  Site records (administrative facilities only). Ohio is refreshing all rest
  areas through 2026; new amenities are being added continuously.

Check for:
- Scenic overlooks → Sites or Access Points
- State-managed bikeway corridors → Trails
- Multi-use paths along state routes → Trails
- Mitigation lands → Sites (if identity-bearing)

## 4.3 EPA / DEFA (Conditional)
Include only if:
- Public access exists
- The site is identity-bearing
- The site is managed as a natural area

Examples:
- Wetland mitigation sites
- Stream restoration sites

## 4.4 ODA (Conditional)
Include only if:
- Identity-bearing
- Public access exists
- Managed for conservation

Examples:
- Demonstration farms
- Conservation areas

## 4.6 Water Trail Tier Assignment ✨ NEW IN v5.4 (renumbered v5.5)

ODNR designates water trails (e.g., Ohio Water Trails program) at the state level. Active
management is frequently performed by a local government, metro park, conservancy, or
non-profit.

**Rule: Management tier governs.**

- A water trail designated by ODNR but managed by a metro park district → Tier 3.
- A water trail designated by ODNR but managed by a municipality → Tier 6.
- A water trail designated by ODNR but managed by a conservancy → Tier 7.
- A water trail designated and managed by ODNR itself → Tier 2.

The ODNR state designation is a status attribute, not a tier assignment. It is captured
in the trail entity's `designation` field (or equivalent controlled vocabulary field for
Trail entities) — not in the tier assignment.

**Do not create a Tier 2 record for a water trail** solely because ODNR issued the
designation. Create the record at the managing entity's tier and record ODNR as the
designating authority in `identity_notes_raw` and `designation`.

**Overlap with scenic river Sites**: A water trail that runs through a scenic river
corridor produces separate entities — the Water Site (scenic river) and the Trail or
Trail Segment (water trail). These are related but distinct entities. Flag overlapping
records in `identity_notes_raw`. Resolution and normalization will handle the relationship.
This intersection is flagged for full protocol development when water trail discovery begins.

## 4.5 Ohio Turnpike & Infrastructure Commission (OTIC)
Required sources (only if county has Ohio Turnpike / I-80/90 access):
- `https://www.ohioturnpike.org/travelers/service-plazas`

The Ohio Turnpike runs along I-80/90 in northern Ohio only. Skip this source
entirely for counties without Turnpike access — OTIC is irrelevant to most counties.

Check for:
- Service plazas with outdoor recreation amenities → Sites
- Outdoor walking areas, dog areas → Trail records
- OTIC is a quasi-state authority separate from ODOT.

NOTE: `ohioturnpike.org` is not on the standard recursion allowlist. Add it
conditionally when the county has Turnpike access (see §5.3).

## 4.7 Public University Natural Areas ✨ NEW IN v5.5 (IMP-003)

Public universities in Ohio are state institutions — created by state charter, governed
by state-appointed trustees, and funded by state appropriations. Their natural areas are
Tier 2 entities.

**Scope**: Discover during Tier 2 any public university natural areas that are:
- Open to the public (all or most of the time), or
- Formally designated (State Nature Preserve, National Natural Landmark, etc.), or
- Documented as a named natural area, nature preserve, arboretum, or research wetland
  with distinct identity on the university's official website.

**Out of scope at Tier 2**:
- Private universities — if encountered, stage at Tier 8 (Private).
- Generic campus green space without a distinct natural areas identity (lawns, quads,
  athletic fields). These are not Sites.
- Lab buildings or facilities that happen to have outdoor components.

**Field mapping**:
- `governance_raw`: the university's name (e.g., "The Ohio State University", "Ohio University")
- `ownership_raw`: "State of Ohio" (public university land is state-owned)
- `category_raw`: as stated by the university — typically "Nature Preserve," "Arboretum,"
  "Research Wetland," or "Natural Area"
- `discovery_tier`: 2

**Authoritative sources**: Check the university's official website for a natural areas,
arboretum, or environmental/sustainability section. Also check:
- ODNR DNAP designations (some university preserves are State Nature Preserves)
- NNL registry (some university research sites are National Natural Landmarks)

**Special case — ODNR-designated university preserves**: If a university nature preserve
is also designated as a State Nature Preserve, ODNR DNAP will list it. Discovery from
either source is valid; do not create duplicate records. The Tier 2 record captures both
the university governance and the ODNR designation in `designation`.

**Private universities**: If a private university has a formally designated natural area
(State Nature Preserve, NNL) encountered during Tier 2 ODNR discovery, stage it at
Tier 2 with the designation noted, and flag in `identity_notes_raw` that ownership is
private. Do not otherwise search private university websites at Tier 2.

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 2 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Tier 2 must enumerate:
- All ODNR division listing pages
- All OHC site listings
- All ODOT bikeway and scenic overlook listings
- All state-managed easement listings
- All state-level GIS datasets

Always **fetch** listing pages directly — do not rely on search snippets alone.
Extract ALL entities listed, including those only briefly mentioned.

**First-Pass Capture**: When fetching a state unit or recreation area page, extract ALL available fields in a single pass — including `description_raw` (the narrative paragraph describing the site's character, ecology, or significance) and `features_raw` (the amenity or facilities list). Both fields are typically present on the same page. A return visit to collect fields that were available on first fetch is a process failure. See `na_site_discovery_subproc.md` §7.3 for field definitions, source guidance, and the Description Quality Gate (IMP-032).

**Pre-Discovery Checklist (IMP-029)**: After enumerating state units and agencies from listing pages and before fetching individual entity pages, write the full entity list to the handoff's **Pre-Discovery Checklist**. A context break between enumeration and individual fetches should not require re-enumerating from source. See na-discovery skill.

**Captured Source Data (IMP-030)**: When fetching a structured source table (ODNR property directory, preserve inventory, unit listing with addresses), write it verbatim to the handoff's **Captured Source Data** section immediately — do not defer to staging time. See na-discovery skill.

## 5.2 Recursive Discovery (URL Propagation)
Tier 2 must recursively follow:
- Internal links within *.ohiodnr.gov
- Internal links within *.ohiohistory.org
- Internal links within *.transportation.ohio.gov
- Internal links within *.epa.ohio.gov (conditional)
- Internal links within *.agri.ohio.gov (conditional)

Recursion must stop when:
- The domain is not on the allowlist
- The page is not relevant to Sites, Trails, or Access Points
- The page is administrative or non-recreational

## 5.3 Recursion Allowlist
- *.ohiodnr.gov
- *.ohiohistory.org
- *.transportation.ohio.gov
- *.epa.ohio.gov
- *.agri.ohio.gov
- *.ohioturnpike.org (conditional — only if county has Turnpike / I-80/90 access)

------------------------------------------------------------
# 6. ENTITY CREATION RULES (TIER-SPECIFIC)

## 6.1 Site Creation
Create a **Site** when:
- ODNR-owned, ODNR-managed, OHC-managed, or ODOT-managed
- Identity-bearing (named, mapped, or designated)
- Public access or recreation infrastructure exists
- It influences Access Point logic

Exclude:
- Administrative offices
- Maintenance yards
- Non-public parcels with no identity

## 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a state Site
- A campground, day-use area, or management unit is identity-bearing
- A preserve unit or forest management zone is documented

## 6.3 Trail Creation
Create a **Trail** when:
- A named trail appears in ODNR, OHC, or ODOT datasets or maps

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `urls_raw` for all discovered map URLs (PDF, interactive, GPX, KML).

## 6.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment-level geometry or identifiers exist

## 6.5 Trail Network Creation
Create a **Trail Network** when:
- A statewide or regional multi-trail system is documented

Examples:
- Buckeye Trail (if treated as a network)
- Statewide water trail systems

## 6.6 Site Network Creation
Create a **Site Network** when:
- A multi-site state designation exists that functions as an umbrella over distinct Sites

Note: Scenic River designations are **not** Site Networks. They are Sites (category=Water
Site, subtype=River). See §3.5 and Discovery Protocol v5.x §17.2.

## 6.7 Access Point Creation
Create an **Access Point** when:
- A visitor-facing entry location is documented

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.

------------------------------------------------------------
# 7. TIER-SPECIFIC EXPECTATIONS

Tier 2 **must** surface:
- All state parks
- All state forests
- All wildlife areas
- All nature preserves
- All Scenic Rivers
- All OHC-managed state memorials and preserves
- All ODOT scenic overlooks and state-managed bikeways
- All state-managed trails
- All state-managed access points
- All identity-bearing child Sites

Tier 2 **may** surface:
- Statewide trail networks
- Scenic River Site Networks
- State-managed easements
- EPA/ODA conservation lands (conditional)

------------------------------------------------------------
# 8. MULTI-COUNTY UNCERTAINTY HANDLING

Some state entities have genuinely ambiguous county distribution — for example,
a wildlife area whose headquarters address is in one county but whose primary
features and acreage are in adjacent counties.

When county distribution is uncertain:

1. Record `county_primary` as the county containing the headquarters address
2. Set `counties_raw` to all suspected counties
3. Populate the uncertainty block with: "County distribution uncertain — GIS verification required"
4. Flag with the standard tag: `GIS_VERIFY_COUNTY`
5. Do not attempt to resolve — normalization and GIS will arbitrate

This applies especially to:
- Wildlife areas with multiple management units across county lines
- State forests with non-contiguous parcels
- Scenic River designations crossing multiple counties

------------------------------------------------------------
# 9. METADATA REQUIREMENTS

Each discovered entity must include:

- Full **Discovery Metadata v5.x**
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships (for child Sites and Access Points)
- All geometry (if available)
- `description_raw` for Sites and Access Points (if a narrative description exists on the source page)
- `features_raw` for Sites and Access Points (if an amenity/facilities list is documented)
- `difficulty_raw` and `accessibility_raw` for Trails and Trail Segments (if explicitly stated)
- `urls_raw` for Trails, Trail Segments, Trail Networks, and Site Networks (map URLs included)

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 10. OUTPUT REQUIREMENTS

Each state entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- The appropriate Schema Module v5.x
- The appropriate Vocabulary Module v5.x

No normalized fields may appear in Tier 2 output.

------------------------------------------------------------
# 11. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x
- All Entity Discovery Sub-Procedures v5.x
- Child Site Rules Module v5.x
- Discovery Metadata Specification v5.x
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Audit & Logging Module v5.x
- County Baseline Module v5.x

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.x
- Discovery Output Specification v5.x
- Discovery Metadata Specification v5.x
- All six entity Discovery Sub-Procedures v5.x
- Child Site Rules Module v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF STATE LANDS DISCOVERY SUB-PROCEDURE v5.7
