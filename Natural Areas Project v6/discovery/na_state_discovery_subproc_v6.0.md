# NATURAL AREAS PROJECT
# STATE LANDS DISCOVERY SUB-PROCEDURE v6.0
(Tier 2 — ODNR Divisions, OHC, ODOT, OTIC, State Easements, Scenic Rivers, Public Universities)

This module defines the authoritative, deterministic Tier 2 discovery rules for
state-managed and state-affiliated lands within the v6.x pipeline.

This module supersedes State Lands Discovery Sub-Procedure v5.7.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v6.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.7 → v6.0

- **Entity type references updated throughout**: Trail, Trail Segment, and Trail
  Network are unified into the single Trailthing entity type. §6.3–6.5 (Trail,
  Trail Segment, Trail Network creation) consolidated into §6.3 (Trailthing
  Creation). §3.1, §3.2, §3.3, §3.4, §3.5 source checklists updated. §4.6
  Water Trail Tier Assignment updated: "Trail entity" → "Trailthing entity."
  §7 Tier-Specific Expectations updated. §9 Metadata Requirements updated.

- **Section numbering corrected**: v5.7 §4 had 4.1–4.4, then 4.6, then 4.5
  (OTIC and Water Trail were out of order from their version histories). v6.0
  renumbers to logical order: 4.1 OHC, 4.2 ODOT, 4.3 EPA/DEFA, 4.4 ODA,
  4.5 OTIC, 4.6 Water Trail Tier Assignment, 4.7 Public University Natural Areas.

- **Document Collection added** (§5.4): During Tier 2 discovery, all qualifying
  maps, PDFs, GIS exports, and other source documents must be downloaded and
  logged per Discovery Orchestration Module v6.0 §4. ODNR maps, brochures, and
  wildlife hunting/fishing area PDFs are particularly important to capture.

- **All v5.7 rules carried forward**: IMP-132 (ODNR Ohio Lake Map Resource),
  IMP-133 (SORP), IMP-029 (Pre-Discovery Checklist), IMP-030 (Captured Source
  Data), IMP-003 (Public University Natural Areas), IMP-008 (Scenic River entity
  type), IMP-009 (Water Trail Tier Assignment), OBS-006 (Multi-County Uncertainty).

------------------------------------------------------------
# 1. PURPOSE

The State Lands Discovery Sub-Procedure v6.0 defines how Tier 2 must:

- Identify all state-managed Sites
- Identify child Sites within state Sites
- Identify Trailthings on state lands
- Identify Site Networks
- Identify Access Points associated with state Sites and Trailthings
- Distinguish ODNR divisions, OHC, ODOT, EPA/ODA, and co-management arrangements
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Discovery Records v6.x
- Download and log source documents per the Document Collection System

This module is referenced only by:
- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.0

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
- **Public universities** (nature preserves, arboreta, research wetlands,
  open-access natural areas on campus) — see §4.7

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

NOTE: JavaScript-rendered page. Use Claude in Chrome for interactive browsing,
or reference the division-specific listing pages below for text-parseable results.
Results from this step define the expected entity inventory for the county before
division-level searches begin.

## 3.1 ODNR Division of Parks & Watercraft
Required sources:
- ODNR park pages
- ODNR park maps (download qualifying maps per §5.4)
- ODNR GIS datasets

Check for:
- State parks → Sites
- Campgrounds → child Sites
- Day-use areas → child Sites
- Marinas → child Sites or Access Points
- Boat ramps → Access Points
- Named trails → Trailthings

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
- ODNR forest maps (download qualifying maps per §5.4)
- ODNR GIS datasets

Check for:
- State forests → Sites
- Forest management units → child Sites
- Named forest trails → Trailthings

## 3.3 ODNR Division of Wildlife
Required sources:
- ODNR wildlife area pages
- ODNR wildlife GIS datasets
- **HUNTING AREA MAPS** (mandatory):
  `https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/hunting-area-maps`
  Search for the county name in the table. Captures multi-county wildlife areas
  that may not appear in county-specific searches. Contains 150+ entries including:
  Wildlife Area, Public Hunting Area, Field Trial Area, Education Area - No Hunting,
  Wildlife Agreement Area, Recreation Area. **Download PDF maps for confirmed areas
  per §5.4.**
- **FISHING LAKE MAPS** (mandatory):
  `https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/fishing-lake-maps`
  Search for county name. ODNR-managed fishing lakes are identity-bearing sites and
  may include access points (boat ramps, fishing piers). **Download PDF maps per §5.4.**
- **RIVER & STREAM FISHING MAPS** (mandatory):
  `https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/river-stream-fishing-maps`
  Search for county name. Named fishing reaches may generate:
  - Access Points (fishing access, boat ramps)
  - Trailthing records (if paddling trails are documented)
  - Sites (if ODNR has designated a named area)
  **Download PDF maps per §5.4.**
- **ODNR OHIO LAKE MAP RESOURCE** (mandatory for wildlife area and fishing lake GPS):
  `https://experience.arcgis.com/experience/2a39044c75b04e68872564b4c6ec0638`
  ArcGIS Experience viewer mapping all ODNR Division of Wildlife–managed fishing
  lakes and associated access features across Ohio. Use to acquire GPS centroids
  for DOW-managed fishing lakes and wildlife areas that do not appear in OSM or
  resolve cleanly via Nominatim. Cross-check entity name against the layer's
  SITE_NAME attribute; confirm county match before accepting. Also useful for
  confirming county placement of multi-county wildlife areas.
  See GPS Acquisition Module v6.x (or v5.x) §5.9 for GPS provenance protocol
  (`acquisition_method: "odnr_lake_map"`).

Check for:
- Wildlife areas → Sites
- Hunting units → child Sites
- Fishing access points → Access Points
- Named wildlife area trails → Trailthings

## 3.4 ODNR Division of Natural Areas & Preserves (DNAP)
Required sources:
- DNAP preserve pages
- DNAP maps (download qualifying maps per §5.4)
- DNAP GIS datasets

Check for:
- State nature preserves → Sites
- Preserve units → child Sites
- Preserve access points → Access Points
- Named preserve trails → Trailthings

## 3.5 ODNR Scenic Rivers Program
Required sources:
- Scenic River program pages
- Scenic River maps (download qualifying maps per §5.4)
- Scenic River GIS datasets

Check for:
- **Scenic River designations → Sites** (category=Water Site, subtype=River,
  designation=State Scenic River and/or National Wild and Scenic River as
  applicable). Do NOT create Site Networks for scenic river designations — the
  scenic designation is a legal status attribute handled by the Designation field,
  parallel to State Nature Preserve and NNL. See Discovery Protocol v6.x for
  the full rule.
- **Scenic River access points → Access Points** (parented to the scenic river
  Site)
- **Water trail entities within a scenic river corridor → Trailthing records**
  (separate from the Water Site; flag overlapping records — see §4.6)

## 3.6 ODNR Mineral Resources
Required sources:
- ODNR mineral resources datasets

Check for:
- Surface-managed lands → Sites
- Public access areas → Access Points

Always **fetch** official ODNR pages directly — do not rely on search snippets
alone. Extract ALL entities listed on division pages.

## 3.7 State-Owned Real Property (SORP) — Cross-Agency Enumeration and GPS Source

The State of Ohio maintains a comprehensive inventory of all state-owned real
property through the Department of Administrative Services (DAS) / Ohio Geographic
Reference and Index System (OGrIP). SORP covers all state agencies — ODNR, OHC,
ODOT, state universities, and others — in a single cross-agency parcel dataset.

**Program URL:**
```
https://das.ohio.gov/technology-and-strategy/ogrip/projects/sorp
```

**ArcGIS Export Tool:**
```
https://experience.arcgis.com/experience/802e2079e2e4448e819cee71e4fefe92/page/State-Owned-Property-Data-Export-Tool
```

**Project asset:** `SORP_Parcels_2023.csv` — statewide SORP export at the project
root. Filter by county FIPS or county name for targeted lookups. Note the 2023
data year in GPS provenance when coordinates are sourced from this file.

### When to Use

1. **Enumeration completeness check** — after working through individual division
   listing pages (§3.1–§3.6), query SORP for the county to confirm no state-owned
   parcels are absent from the entity list.
2. **GPS / centroid acquisition** — for state entities not in OSM and not
   geocodable via Nominatim. SORP parcel records carry centroid coordinates.
   See GPS Acquisition Module v6.x (or v5.x) §5.9 for the full SORP GPS workflow
   (`acquisition_method: "sorp_gis"`).
3. **County ambiguity resolution** — for multi-parcel or border-adjacent state
   holdings, SORP provides parcel-level county assignment.

### Limitations

- SORP records ownership, not managed public access. A parcel in SORP does not
  confirm public access; verify access independently.
- SORP data is updated periodically. Verify managing agency for recently
  transferred parcels.
- The project CSV (`SORP_Parcels_2023.csv`) is a 2023 snapshot; note the data
  year in GPS provenance metadata.

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
  **Cross-reference first**: Filter `ODOT rest stops baseline.xlsx` (v6 project
  root) by County column to identify known rest areas in the current county
  before web discovery. Use the website to verify current amenities and confirm
  any new rest areas not yet in the baseline.
  Rest areas with outdoor recreation features are identity-bearing Sites:
  - Dog trails → Trailthing record
  - Storybook Trails → Trailthing record
  - Native plant areas → feature note on Site record
  Rest areas without outdoor/recreation features: document but do not create
  Site records (administrative facilities only). Ohio is refreshing all rest
  areas through 2026; new amenities are being added continuously.

Check for:
- Scenic overlooks → Sites or Access Points
- State-managed bikeway corridors → Trailthings
- Multi-use paths along state routes → Trailthings
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

## 4.5 Ohio Turnpike & Infrastructure Commission (OTIC)
Required sources (only if county has Ohio Turnpike / I-80/90 access):
- `https://www.ohioturnpike.org/travelers/service-plazas`

The Ohio Turnpike runs along I-80/90 in northern Ohio only. Skip this source
entirely for counties without Turnpike access — OTIC is irrelevant to most counties.

Check for:
- Service plazas with outdoor recreation amenities → Sites
- Outdoor walking areas, dog areas → Trailthing records

OTIC is a quasi-state authority separate from ODOT.

NOTE: `ohioturnpike.org` is not on the standard recursion allowlist. Add it
conditionally when the county has Turnpike access (see §5.3).

## 4.6 Water Trail Tier Assignment — IMP-009

ODNR designates water trails (e.g., Ohio Water Trails program) at the state
level. Active management is frequently performed by a local government, metro
park, conservancy, or non-profit.

**Mandatory pre-discovery source — check at the start of every county run:**
`https://ohiodnr.gov/discover-and-learn/land-water/rivers-streams-wetlands/ohio-water-trails`
This page lists all current ODNR-designated water trails with links to paddling
guide PDFs. Cross-check the county's waterways against this list before closing
Tier 2. Download the relevant paddling guide PDF per §5.4 for any trail that
passes through the county. Note: a water trail may pass through multiple counties
— check all rivers and streams in the county, not only those with county-name
matches in the trail title.

**Rule: Management tier governs.**

- A water trail designated by ODNR but managed by a metro park district → Tier 3.
- A water trail designated by ODNR but managed by a municipality → Tier 6.
- A water trail designated by ODNR but managed by a conservancy → Tier 7.
- A water trail designated and managed by ODNR itself → Tier 2.

The ODNR state designation is a status attribute, not a tier assignment. It is
captured in the Trailthing entity's `status_raw` or `identity_notes_raw` — not
in the tier assignment.

**Do not create a Tier 2 record for a water trail** solely because ODNR issued
the designation. Create the record at the managing entity's tier and record ODNR
as the designating authority in `identity_notes_raw`.

**Overlap with scenic river Sites**: A water trail that runs through a scenic
river corridor produces separate entities — the Water Site (scenic river) and the
Trailthing (water trail). These are related but distinct entities. Flag overlapping
records in `identity_notes_raw`. Resolution and normalization will handle the
relationship.

## 4.7 Public University Natural Areas — IMP-003

Public universities in Ohio are state institutions — created by state charter,
governed by state-appointed trustees, and funded by state appropriations. Their
natural areas are Tier 2 entities.

**Scope:** Discover during Tier 2 any public university natural areas that are:
- Open to the public (all or most of the time), or
- Formally designated (State Nature Preserve, National Natural Landmark, etc.), or
- Documented as a named natural area, nature preserve, arboretum, or research
  wetland with distinct identity on the university's official website

**Out of scope at Tier 2:**
- Private universities — if encountered, stage at Tier 8 (Private)
- Generic campus green space without a distinct natural areas identity (lawns,
  quads, athletic fields)
- Lab buildings or facilities that happen to have outdoor components

**Field mapping:**
- `governance_raw`: the university name (e.g., "The Ohio State University")
- `ownership_raw`: "State of Ohio"
- `category_raw`: as stated — typically "Nature Preserve," "Arboretum,"
  "Research Wetland," or "Natural Area"
- `discovery_tier`: 2

**Authoritative sources:** Check the university's official website for a natural
areas, arboretum, or environmental/sustainability section. Also check:
- ODNR DNAP designations (some university preserves are State Nature Preserves)
- NNL registry (some university research sites are National Natural Landmarks)

**ODNR-designated university preserves:** If a university nature preserve is also
a State Nature Preserve, ODNR DNAP will list it. Discovery from either source is
valid; do not create duplicate records.

**Private universities:** If a private university has a formally designated natural
area encountered during Tier 2 ODNR discovery, stage it at Tier 2 with the
designation noted and flag in `identity_notes_raw` that ownership is private. Do
not otherwise search private university websites at Tier 2.

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

**First-Pass Capture:** When fetching a state unit or recreation area page,
extract ALL available fields in a single pass — including `description_raw`
and `features_raw`. Both fields are typically present on the same page. A
return visit to collect fields available on first fetch is a process failure.
See Site Discovery Sub-Procedure v6.0 §7.3 for field definitions and the
Description Quality Gate.

**Pre-Discovery Checklist (IMP-029):** After enumerating state units from
listing pages and before fetching individual entity pages, write the full
entity list to the handoff's Pre-Discovery Checklist.

**Captured Source Data (IMP-030):** When fetching a structured source table
(ODNR property directory, preserve inventory, unit listing), write it verbatim
to the handoff's Captured Source Data section immediately.

## 5.2 Recursive Discovery (URL Propagation)
Tier 2 must recursively follow:
- Internal links within *.ohiodnr.gov
- Internal links within *.ohiohistory.org
- Internal links within *.transportation.ohio.gov
- Internal links within *.epa.ohio.gov (conditional)
- Internal links within *.agri.ohio.gov (conditional)

Recursion must stop when:
- The domain is not on the allowlist
- The page is not relevant to Sites, Trailthings, or Access Points
- The page is administrative or non-recreational

## 5.3 Recursion Allowlist
- *.ohiodnr.gov
- *.ohiohistory.org
- *.transportation.ohio.gov
- *.epa.ohio.gov
- *.agri.ohio.gov
- *.ohioturnpike.org (conditional — only if county has Turnpike / I-80/90 access)

## 5.4 Document Collection

During Tier 2 discovery, download all qualifying source documents and log each
in the county document log per **Discovery Orchestration Module v6.0 §4**.

Tier 2 produces the most varied and valuable downloadable source material of
any tier. Particularly important documents to capture:
- ODNR hunting area maps (PDF) — one per wildlife area; from §3.3 mandatory source
- ODNR fishing lake maps (PDF) — from §3.3 mandatory source
- ODNR state park trail maps (PDF)
- ODNR state forest trail maps (PDF)
- ODNR nature preserve brochures and maps (PDF)
- Scenic River corridor maps (PDF)
- Water trail paddling guides (PDF) — especially if the county has documented
  water trails
- GPX/KML files for state-managed trails
- ODNR GIS layer exports when downloaded

------------------------------------------------------------
# 6. ENTITY CREATION RULES (TIER-SPECIFIC)

## 6.1 Site Creation
Create a **Site** when:
- ODNR-owned, ODNR-managed, OHC-managed, or ODOT-managed
- Identity-bearing (named, mapped, or designated)
- Public access or recreation infrastructure exists

Exclude:
- Administrative offices
- Maintenance yards
- Non-public parcels with no identity

## 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a state Site
- A campground, day-use area, or management unit is identity-bearing
- A preserve unit or forest management zone is documented

## 6.3 Trailthing Creation
Create a **Trailthing** when:
- A named trail, trail section, trail system, or water trail appears in
  ODNR, OHC, or ODOT datasets or maps

Capture `source_term_raw` verbatim and `source_hierarchy_context_raw` when
the source frames the entity in relation to others. Do not classify the
Trailthing as trail vs. trail network vs. trail segment during discovery.

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated.
Download trail maps, paddling guides, and GPX/KML files per §5.4.

## 6.4 Site Network Creation
Create a **Site Network** when:
- A multi-site state designation exists that functions as an umbrella over
  distinct Sites and meets the threshold rules in Site Network Discovery
  Sub-Procedure v6.0 §3

Note: Scenic River designations are **not** Site Networks. They are Sites
(category=Water Site, subtype=River). See §3.5.

**If no Site Networks qualify at Tier 2:** Document an explicit null-evidence block
before advancing to Access Point creation. Silence is not a null.

```yaml
entity_type_result:
  tier: 2
  governance_level: State
  entity_type: Site Network
  result: null
  sources_checked:
    - [URL or source description]
  reasoning: [why no Site Networks qualify — threshold not met, no qualifying
              state-level multi-site designation found, etc.]
```

At minimum, two sources must be checked before concluding null.

## 6.5 Access Point Creation
Create an **Access Point** when:
- A visitor-facing entry location is documented

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.
Populate `last_verified_date` with today's date; set `field_verified: false`.

------------------------------------------------------------
# 7. TIER-SPECIFIC EXPECTATIONS

Tier 2 **must** surface:
- All state parks
- All state forests
- All wildlife areas
- All state nature preserves
- All Scenic River Sites
- All OHC-managed state memorials and preserves
- All ODOT scenic overlooks and state-managed bikeways/trails
- All state-managed Trailthings
- All state-managed Access Points
- All identity-bearing child Sites
- All public university natural areas in the county

Tier 2 **may** surface:
- Statewide or regional Trailthing systems
- State Site Networks (multi-site designations)
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
3. Populate the uncertainty block: "County distribution uncertain — GIS
   verification required"
4. Flag with: `GIS_VERIFY_COUNTY`
5. Do not attempt to resolve — normalization and GIS will arbitrate

This applies especially to:
- Wildlife areas with multiple management units across county lines
- State forests with non-contiguous parcels
- Scenic River designations crossing multiple counties

------------------------------------------------------------
# 9. METADATA REQUIREMENTS

Each discovered entity must include:
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships (for child Sites and Access Points)
- `description_raw` for Sites and Access Points (if narrative description exists)
- `features_raw` for Sites and Access Points (if amenity/facilities list exists)
- `source_term_raw` and `source_hierarchy_context_raw` for Trailthings
- `difficulty_raw` and `accessibility_raw` for Trailthings (only if explicitly stated)
- `urls_raw` for all entity types (map URLs included)

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 10. OUTPUT REQUIREMENTS

Each state entity must output a Raw Discovery Record conforming to:
- The appropriate v6.0 Schema Module
- The appropriate v6.0 Vocabulary Module

No normalized fields may appear in Tier 2 output.

------------------------------------------------------------
# 11. INTEGRATION POINTS

This module integrates with:
- Discovery Orchestration Module v6.0
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- Resolution Engine v6.x *(or v5.x)*
- GPS Acquisition Module v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:
- Discovery Orchestration Module v6.0 *(for document collection rules, §4)*
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- GPS Acquisition Module v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF STATE LANDS DISCOVERY SUB-PROCEDURE v6.0
