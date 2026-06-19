# NATURAL AREAS PROJECT
# COUNTY LANDS DISCOVERY SUB-PROCEDURE v6.0
(Tier 4 — County Governments, County GIS, County Recreation Departments, County-Hosted Municipal/Township Pages)

This module defines the authoritative, deterministic Tier 4 discovery rules for
county-owned, county-managed, and county-hosted natural areas within the v6.x pipeline.

This module supersedes County Lands Discovery Sub-Procedure v5.5.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v6.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.5 → v6.0

- **Entity type references updated throughout**: Trail, Trail Segment, and Trail
  Network are unified into the single Trailthing entity type. §1 Purpose, §6 Entity
  Creation Rules, §7 Tier-Specific Expectations, and §8 Metadata Requirements
  updated accordingly. §6.3–6.5 (Trail, Trail Segment, Trail Network creation)
  consolidated into §6.3 (Trailthing Creation). §6.6 Site Network renumbered to §6.4;
  §6.7 Access Point renumbered to §6.5.

- **Document Collection added** (§5.4): During Tier 4 discovery, all qualifying
  maps, PDFs, GPX/KML files, GIS exports, and other source documents must be
  downloaded and logged per Discovery Orchestration Module v6.0 §4.

- **All v5.5 rules carried forward**: IMP-099 (County Cemeteries and Golf Courses),
  IMP-029 (Pre-Discovery Checklist), IMP-030 (Captured Source Data),
  OBS-011 (County park districts as Site Networks), OBS-012 (Cross-county address
  handling), OBS-013 (Minimal-data sites), OBS-014 (Planned vs. built infrastructure),
  OBS-028 (NRHP bridges), OBS-029 (Full parks directory fetch).

------------------------------------------------------------
# 1. PURPOSE

The County Lands Discovery Sub-Procedure v6.0 defines how Tier 4 must:

- Identify county-owned or county-managed Sites
- Identify child Sites within county Sites
- Identify county-managed Trailthings
- Identify county-managed Site Networks
- Identify county-managed Access Points
- Identify county-hosted municipal/township pages
- Distinguish county management from municipal/township co-management
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Discovery Records v6.x
- Download and log source documents per the Document Collection System

This module is referenced only by:
- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.0

------------------------------------------------------------
# 2. SCOPE

This sub-procedure applies to:

- County government websites
- County GIS systems
- County recreation departments
- County planning commissions
- County commissioners' pages
- County-hosted municipal/township pages
- County tourism or visitors bureau pages
- County-level trail plans

Tier 4 sits **below District-Level** and **above Township**.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 4 must enumerate and recursively explore the following authoritative sources.

## 3.1 County Government Website
Scan for:
- Parks
- Recreation
- Facilities
- Natural Resources
- Open Space / Conservation
- Trails
- Outdoor Recreation

Include:
- Hidden or unlinked pages
- PDF brochures
- County-hosted municipal/township pages
- Recreation guides

**Always fetch the top-level parks or recreation directory page first** — this is the
full property list. Individual park pages are child pages that add detail; the directory
is the enumeration baseline. Do not start with individual park pages and assume coverage
(OBS-029).

Always **fetch** official pages directly — do not rely on search snippets alone.
Read full page content; extract ALL parks, trails, and facilities listed.

## 3.2 County GIS (Primary Authoritative Source)
Check for layers including:
- Parks → Sites
- Open space → Sites
- Conservation lands → Sites
- Trails → Trailthings
- Recreation facilities → Sites or child Sites
- Boat launches → Access Points
- Fishing access → Access Points
- Hunting access → Access Points
- County-owned parcels → Sites

## 3.3 National Register of Historic Places (NRHP) — Bridges and Structures (OBS-028)
Search the NRHP database for county-located bridges, covered bridges, historic structures,
and historic districts that are accessible to the public and may function as natural area
access points or identity-bearing sites:

```
Search: "[County] County Ohio site:nps.gov/nr OR npgallery.nps.gov"
OR fetch: https://npgallery.nps.gov/AssetDetail/NRIS/{county_code}
```

Focus on:
- Covered bridges → Sites (if visitor-facing) or Access Points
- Historic structures on public land → child Sites of parent parks
- Historic districts on ODNR or county land → child Sites
- Natural features on NRHP (mounds, caves, geological formations) → Sites

Cross-reference with county auditor parcels to confirm public ownership/access.
If an NRHP-listed structure is within an already-documented county park, add it
as a child Site of that park, not a standalone Site.

## 3.4 County Planning Documents
Check:
- Comprehensive plans
- Greenway plans
- Open space plans
- Trail plans
- Recreation master plans

Download qualifying plans per §5.4.

## 3.5 County Commissioners' Pages
Check for:
- Land acquisitions
- Park resolutions
- Conservation partnerships
- Trail funding approvals

## 3.6 County Tourism / Visitors Bureau
Check for:
- Parks
- Trails
- Natural attractions
- Outdoor recreation assets

## 3.7 County-Hosted Municipal/Township Pages
These count as **authoritative** for municipal/township discovery.
All discoveries from county-hosted pages remain **Tier 4**.

All sources must be logged in discovery metadata.

------------------------------------------------------------
# 4. DOMAIN RULES FOR COUNTY DISCOVERY

## 4.1 County-Owned vs County-Managed
A Site may be:
- Owned by the county
- Managed by the county
- Co-managed with municipalities or park districts

All must be surfaced if identity-bearing.

## 4.2 County-Hosted Municipal/Township Pages
If the county hosts municipal/township pages:
- Treat them as authoritative
- Surface all parks, preserves, trails, and facilities listed
- Log the county as the source

Discoveries remain **Tier 4**.

## 4.3 County Recreation Departments
If a recreation department exists:
- Scan all program pages
- Scan all facility pages
- Scan all park listings
- Scan all trail listings
- Scan all brochures and PDFs

## 4.4 County Planning Commissions
Planning documents often contain:
- Unlisted parks
- Planned parks
- Trail corridors
- Access Points

## 4.5 County Parks Districts → Site Networks (OBS-011)
When a county operates a formal parks district (a semi-autonomous governing body with
its own name, board, and branding separate from general county government), surface it
as a **Site Network** containing its member Sites — not as a single standalone Site.

Examples: "Clinton County Park District", "Wood County Park District"

- The district itself → Site Network record
- Each individual park in the district → Site record
- Discovery must enumerate all member parks from the district's own website AND
  the county government site — these sometimes differ

Do not collapse a park district into a single Site. The district is a governance
container, not a physical land unit.

Apply Site Network threshold rules per Site Network Discovery Sub-Procedure v6.0 §3.

## 4.6 Cross-County Address Handling (OBS-012)
When a site's mailing or street address is in an adjacent county, but its physical
footprint or GPS coordinates are in the target county:

- Create the record for the target county based on GPS/physical location
- Record the address county in `identity_notes_raw` as: "Address county: [County]"
- Flag with: `ADDRESS_COUNTY_MISMATCH — verify with GIS`
- Do not exclude a site simply because its address is out-of-county

This is common for large parcels straddling county lines and for rural addresses
that use the nearest town regardless of county.

## 4.7 Minimal-Data Sites (OBS-013)
When a site has a name and GPS coordinates but no address, description, or amenity
information:

- Create the record — do not suppress for lack of detail
- Populate all available fields
- Flag with: `MINIMAL_DATA — description and address require field verification`

GPS-only sites are valid discovery records. Suppressing them creates gaps that
are harder to detect and fill than simply carrying a sparse record forward.

## 4.8 Planned vs. Built Infrastructure (OBS-014)
When a park or trail appears in planning documents but has no confirmed physical
presence:

- Create the record if it is identity-bearing (named, mapped, designated)
- Populate `status_raw` with exactly what the source says (e.g., "planned", "proposed",
  "under construction", "approved")
- Flag with: `PLANNED — physical presence unconfirmed`
- Do not suppress planned parks — they become real parks, and early records
  establish continuity

Exclude only if there is no identity-bearing content (unnamed concept corridor,
undocumented future allocation, etc.).

## 4.9 County Cemeteries and County Golf Courses (IMP-099)

### County Cemeteries

Some Ohio counties own and operate cemeteries directly — distinct from township and
municipal cemeteries. Common types: soldiers' relief cemeteries, county infirmary/
poorhouse cemeteries, and county-designated historic cemeteries.

```
Search: "[County] County Ohio county-owned cemetery
Search: "[County] County Ohio soldiers relief cemetery
Search: "[County] County Ohio infirmary cemetery
```

Also check the county auditor's parcel layer for parcels coded as cemetery owned by
county government. County-owned veterans/soldiers cemeteries → subtype "Veterans
Cemetery". County infirmary cemeteries → subtype "Public Cemetery".

### County Golf Courses

Some Ohio county park districts operate public golf courses. These are Tier 4 entities.

```
Search: "[County] County Ohio golf course parks district
Search: "[County] County Ohio public golf county parks
```

**Classification**: `category: Recreation Facility`, `subtype: Golf Course`.

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 4 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Tier 4 must enumerate:
- All county park listings
- All county Trailthing listings
- All county recreation facility listings
- All county GIS datasets
- All county-hosted municipal/township pages

Always **fetch** listing pages directly — do not rely on search snippets alone.
Extract ALL entities listed, not just prominently featured ones.

**First-Pass Capture**: When fetching a county park or recreation area page, extract
ALL available fields in a single pass — including `description_raw` (the narrative
paragraph describing the site's character, ecology, or significance) and `features_raw`
(the amenity or facilities list). Both fields are typically present on the same page.
A return visit to collect fields that were available on first fetch is a process failure.
See Site Discovery Sub-Procedure v6.0 §7.3 for field definitions and the Description
Quality Gate.

**Pre-Discovery Checklist (IMP-029)**: After enumerating county parks and entities
from listing pages and before fetching individual entity pages, write the full entity
list to the handoff's Pre-Discovery Checklist. A context break between enumeration
and individual fetches should not require re-enumerating from source.

**Captured Source Data (IMP-030)**: When fetching a structured source table (parks
directory with addresses, recreation facility inventory), write it verbatim to the
handoff's Captured Source Data section immediately — do not defer to staging time.

## 5.2 Recursive Discovery (URL Propagation)
Tier 4 must recursively follow:
- Internal links within county domains
- Internal links within county-hosted municipal/township pages
- Internal links within county tourism domains

Recursion must stop when:
- The domain is not on the allowlist
- The page is not relevant to Sites, Trailthings, or Access Points
- The page is administrative or non-recreational

## 5.3 Recursion Allowlist
- *.countyoh.gov
- *.oh.gov (county subdomains)
- *.gis.*
- *.auditor.*
- *.engineer.*
- *.planning.*
- *.visit*. (tourism)
- *.co.*.us (legacy county domains)

## 5.4 Document Collection

During Tier 4 discovery, download all qualifying source documents encountered —
trail maps, park brochures, greenway plans, master plans, GPX/KML files, GIS
exports — and log each in the county document log per **Discovery Orchestration
Module v6.0 §4**.

Particularly valuable documents to capture at Tier 4:
- County parks trail maps and park maps
- Greenway and open space master plans
- Park district brochures and recreation guides
- County trail plan PDFs
- GPX/KML files for county-managed trails

------------------------------------------------------------
# 6. ENTITY CREATION RULES (TIER-SPECIFIC)

## 6.1 Site Creation
Create a **Site** when:
- County-owned or county-managed
- Identity-bearing (named, mapped, or designated)
- Public access or recreation infrastructure exists
- It influences Access Point logic

Exclude:
- Administrative buildings
- Maintenance yards
- Non-public facilities

## 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a county Site
- A recreation area, campground, or management area is identity-bearing
- A special management zone is documented

## 6.3 Trailthing Creation
Create a **Trailthing** when:
- A named trail, trail section, trail system, or trail network appears in
  county GIS, plans, or recreation pages

Capture `source_term_raw` verbatim (how the source describes the entity —
"greenway," "bikeway," "trail system," "connector") and
`source_hierarchy_context_raw` when the source frames the entity in relation
to others. Do not classify the Trailthing as trail vs. trail network vs. trail
segment during discovery — record what the source says.

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by
the source. Record `urls_raw` for all discovered map URLs. Download trail maps
and GPX/KML files per §5.4.

## 6.4 Site Network Creation
Create a **Site Network** when:
- A formal county parks district exists with multiple member parks — see §4.5
- A conservation or greenway network is formally documented
- A multi-site county recreation system is branded as a unified network

Apply the Site Network threshold rules per Site Network Discovery Sub-Procedure
v6.0 §3.

**If no Site Networks qualify at Tier 4:** Document an explicit null-evidence block
before advancing to Access Point creation. Silence is not a null.

```yaml
entity_type_result:
  tier: 4
  governance_level: County
  entity_type: Site Network
  result: null
  sources_checked:
    - [URL or source description]
  reasoning: [why no Site Networks qualify — threshold not met, no qualifying
              county-managed multi-site system found, etc.]
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

Tier 4 **must** surface:
- All county-owned or county-managed Sites
- All identity-bearing child Sites
- All county-managed Trailthings (trails, trail sections, trail systems)
- All county-managed Access Points
- All parks, preserves, and trails listed on county-hosted municipal/township pages

Tier 4 **may** surface:
- County-managed Site Networks
- County-managed easements
- Planned parks and trail corridors (if identity-bearing)

------------------------------------------------------------
# 8. METADATA REQUIREMENTS

Each discovered entity must include:
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships (for child Sites and Access Points)
- `description_raw` for Sites and Access Points (if narrative description
  exists on the source page)
- `features_raw` for Sites and Access Points (if an amenity/facilities list
  is documented)
- `source_term_raw` and `source_hierarchy_context_raw` for Trailthings
- `difficulty_raw` and `accessibility_raw` for Trailthings (only if explicitly
  stated by authoritative source)
- `urls_raw` for all entity types (map URLs included)

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each county entity must output a Raw Discovery Record conforming to:
- The appropriate v6.0 Schema Module
- The appropriate v6.0 Vocabulary Module

No normalized fields may appear in Tier 4 output.

------------------------------------------------------------
# 10. INTEGRATION POINTS

This module integrates with:
- Discovery Orchestration Module v6.0
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- Resolution Engine v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:
- Discovery Orchestration Module v6.0 *(for document collection rules, §4)*
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- Resolution Engine v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF COUNTY LANDS DISCOVERY SUB-PROCEDURE v6.0
