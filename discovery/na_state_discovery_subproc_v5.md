# NATURAL AREAS PROJECT
# STATE LANDS DISCOVERY SUB-PROCEDURE v5.1
(Tier 2 — ODNR Divisions, OHC, ODOT, OTIC, State Easements, Scenic Rivers)

This module defines the authoritative, deterministic Tier-2 discovery rules for
state-managed and state-affiliated lands within the v5.0 Raw → Resolution →
Normalization → Entity Graph pipeline.

This module supersedes State Lands Discovery Sub-Procedure v5.0.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.0 Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.0

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
- `maps_raw` added to output for Trails, Trail Segments, and Networks
- `township_raw` and `municipality_raw` explicitly prohibited — GIS-derived only
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The State Lands Discovery Sub-Procedure v5.0 defines how Tier 2 must:

- Identify all state-managed Sites
- Identify child Sites within state Sites
- Identify Trails, Trail Segments, and Trail Networks on state lands
- Identify Site Networks (e.g., Scenic River systems)
- Identify Access Points associated with state Sites
- Distinguish ODNR divisions, OHC, ODOT, EPA/ODA, and co-management arrangements
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Discovery Records v5.0
- Produce Discovery Metadata v5.0

This module is referenced only by:

- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0

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
- Scenic River designations → Site Networks
- Scenic River access points → Access Points
- Scenic River segments → Trail Segments (if linear trails exist)

## 3.6 ODNR Mineral Resources
Required sources:
- ODNR mineral resources datasets

Check for:
- Surface-managed lands → Sites
- Public access areas → Access Points

Always **fetch** official ODNR pages directly — do not rely on search snippets alone.
Extract ALL entities listed on division pages, not just those prominently featured.

All sources must be logged in **Discovery Metadata v5.0**.

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
Record `maps_raw` for all discovered map URLs (PDF, interactive, GPX, KML).

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
- A Scenic River corridor or similar multi-site designation exists

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
# 7. MULTI-COUNTY UNCERTAINTY HANDLING

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
# 8. METADATA REQUIREMENTS

Each discovered entity must include:

- Full **Discovery Metadata v5.0**
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships (for child Sites and Access Points)
- All geometry (if available)
- `features_raw` for Sites and Access Points (if documented)
- `difficulty_raw` and `accessibility_raw` for Trails and Trail Segments (if explicitly stated)
- `maps_raw` for Trails, Trail Segments, Trail Networks, and Site Networks

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each state entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.0**
- **Discovery Metadata Specification v5.0**
- The appropriate Schema Module v5.0
- The appropriate Vocabulary Module v5.0

No normalized fields may appear in Tier 2 output.

------------------------------------------------------------
# 10. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0
- All Entity Discovery Sub-Procedures v5.0
- Child Site Rules Module v5.0
- Discovery Metadata Specification v5.0
- Discovery Output Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Audit & Logging Module v5.0
- County Baseline Module v5.0

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.0
- Discovery Output Specification v5.0
- Discovery Metadata Specification v5.0
- All six entity Discovery Sub-Procedures v5.0
- Child Site Rules Module v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF STATE LANDS DISCOVERY SUB-PROCEDURE v5.0
