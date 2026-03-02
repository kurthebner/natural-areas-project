# NATURAL AREAS PROJECT
# COUNTY LANDS DISCOVERY SUB-PROCEDURE v5.2
(Tier 4 — County Governments, County GIS, County Recreation Departments, County-Hosted Municipal/Township Pages)

This module defines the authoritative, deterministic Tier-4 discovery rules for
county-owned, county-managed, and county-hosted natural areas within the v5.x
Raw → Resolution → Normalization → Entity Graph pipeline.

This module supersedes County Lands Discovery Sub-Procedure v5.0.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Updated all cross-module references to v5.x
- Fixed duplicate §3.3 section numbering — NRHP Bridges remains §3.3; County Planning Documents renumbered §3.4 through §3.7
- Updated header version to v5.2

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **OBS-011**: County park districts are Site Networks — §4.5 added; county parks district
  surfaced as Site Network containing member Sites, not as a standalone Site
- **OBS-012**: Cross-county address handling — §4.6 added; sites with addresses in adjacent
  counties should be flagged for GPS and GIS verification
- **OBS-013**: Minimal-data sites rule added to §6.1 — GPS-only sites with no address or
  description are valid records; do not suppress
- **OBS-014**: Planned vs. built infrastructure rule added to §6.1 — planned parks are
  valid if identity-bearing; flag with PLANNED status
- **OBS-028**: NRHP bridge and structure search added to §3 as mandatory step
- **OBS-029**: Full county parks directory fetch requirement added to §3.1 — must fetch
  the top-level directory, not just individual park pages or the district site

------------------------------------------------------------
# 1. PURPOSE

The County Lands Discovery Sub-Procedure v5.x defines how Tier 4 must:

- Identify county-owned or county-managed Sites
- Identify child Sites within county Sites
- Identify county-managed Trails and Trail Segments
- Identify county-managed Trail Networks (rare)
- Identify county-managed Site Networks (rare)
- Identify county-managed Access Points
- Identify county-hosted municipal/township pages
- Distinguish county management from municipal/township co-management
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Discovery Records v5.x
- Produce Discovery Metadata v5.x

This module is referenced only by:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x

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
is the enumeration baseline. Do not start with individual park pages and assume coverage.

Always **fetch** official pages directly — do not rely on search snippets alone.
Read full page content; extract ALL parks, trails, and facilities listed.

## 3.2 County GIS (Primary Authoritative Source)
Check for layers including:
- Parks → Sites
- Open space → Sites
- Conservation lands → Sites
- Trails → Trails, Trail Segments
- Recreation facilities → Sites or child Sites
- Boat launches → Access Points
- Fishing access → Access Points
- Hunting access → Access Points
- County-owned parcels → Sites

## 3.3 National Register of Historic Places (NRHP) — Bridges and Structures
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

All sources must be logged in **Discovery Metadata v5.x**.

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

## 4.5 County Parks Districts → Site Networks
When a county operates a formal parks district (a semi-autonomous governing body with
its own name, board, and branding separate from general county government), surface it
as a **Site Network** containing its member Sites — not as a single standalone Site.

Examples: "Clinton County Park District", "Wood County Park District"

- The district itself → Site Network record
- Each individual park in the district → Site record with `parent_network_id`
- Discovery must enumerate all member parks from the district's own website AND
  the county government site — these sometimes differ

Do not collapse a park district into a single Site. The district is a governance
container, not a physical land unit.

## 4.6 Cross-County Address Handling
When a site's mailing or street address is in an adjacent county, but its physical
footprint or GPS coordinates are in the target county:

- Create the record for the target county based on GPS/physical location
- Record the address county in `identity_notes_raw` as: "Address county: [County]"
- Flag with: `ADDRESS_COUNTY_MISMATCH — verify with GIS`
- Do not exclude a site simply because its address is out-of-county

This is common for large parcels straddling county lines and for rural addresses
that use the nearest town regardless of county.

## 4.7 Minimal-Data Sites
When a site has a name and GPS coordinates but no address, description, or amenity
information:

- Create the record — do not suppress for lack of detail
- Populate all available fields
- Flag with: `MINIMAL_DATA — description and address require field verification`

GPS-only sites are valid discovery records. Suppressing them creates gaps that
are harder to detect and fill than simply carrying a sparse record forward.

## 4.8 Planned vs. Built Infrastructure
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

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 4 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Tier 4 must enumerate:
- All county park listings
- All county trail listings
- All county recreation facility listings
- All county GIS datasets
- All county-hosted municipal/township pages

Always **fetch** listing pages directly — do not rely on search snippets alone.
Extract ALL entities listed, not just prominently featured ones.

## 5.2 Recursive Discovery (URL Propagation)
Tier 4 must recursively follow:
- Internal links within county domains
- Internal links within county-hosted municipal/township pages
- Internal links within county tourism domains

Recursion must stop when:
- The domain is not on the allowlist
- The page is not relevant to Sites, Trails, or Access Points
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

## 6.3 Trail Creation
Create a **Trail** when:
- A named trail appears in county GIS, plans, or recreation pages

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `urls_raw` for all discovered map URLs (PDF, interactive, GPX, KML).

## 6.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment-level geometry or identifiers exist

## 6.5 Trail Network Creation
Create a **Trail Network** when:
- A county-managed multi-trail system exists
- A greenway corridor spans multiple Trails

## 6.6 Site Network Creation
Create a **Site Network** when:
- A formal county parks district exists with multiple member parks
- A conservation or greenway network is formally documented
- A multi-site county recreation system is branded as a unified network

The parks district itself is the Site Network. Its member parks are individual Sites.
Both must be created — neither replaces the other.

## 6.7 Access Point Creation
Create an **Access Point** when:
- A visitor-facing entry location is documented

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.

------------------------------------------------------------
# 7. TIER-SPECIFIC EXPECTATIONS

Tier 4 **must** surface:
- All county-owned or county-managed Sites
- All identity-bearing child Sites
- All county-managed Trails
- All county-managed Trail Segments
- All county-managed Access Points
- All parks, preserves, and trails listed on county-hosted municipal/township pages

Tier 4 **may** surface:
- County-managed Trail Networks
- County-managed Site Networks
- County-managed easements
- Planned parks and trail corridors (if identity-bearing)

------------------------------------------------------------
# 8. METADATA REQUIREMENTS

Each discovered entity must include:

- Full **Discovery Metadata v5.x**
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships (for child Sites and Access Points)
- All geometry (if available)
- `features_raw` for Sites and Access Points (if documented)
- `difficulty_raw` and `accessibility_raw` for Trails and Trail Segments (if explicitly stated)
- `urls_raw` for Trails, Trail Segments, Trail Networks, and Site Networks (map URLs included)

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each county entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- The appropriate Schema Module v5.x
- The appropriate Vocabulary Module v5.x

No normalized fields may appear in Tier 4 output.

------------------------------------------------------------
# 10. INTEGRATION POINTS

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
# 11. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.x
- Discovery Output Specification v5.x
- Discovery Metadata Specification v5.x
- All six entity Discovery Sub-Procedures v5.x
- Child Site Rules Module v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF COUNTY LANDS DISCOVERY SUB-PROCEDURE v5.2
