# NATURAL AREAS PROJECT
# COUNTY LANDS DISCOVERY SUB-PROCEDURE v5.0
(Tier 4 — County Governments, County GIS, County Recreation Departments, County-Hosted Municipal/Township Pages)

This module defines the authoritative, deterministic Tier-4 discovery rules for
county-owned, county-managed, and county-hosted natural areas within the v5.0
Raw → Resolution → Normalization → Entity Graph pipeline.

This module supersedes County Lands Discovery Sub-Procedure v4.0.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.0 Vocabulary Modules.

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

The County Lands Discovery Sub-Procedure v5.0 defines how Tier 4 must:

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
- Produce Raw Discovery Records v5.0
- Produce Discovery Metadata v5.0

This module is referenced only by:

- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0

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

## 3.3 County Planning Documents
Check:
- Comprehensive plans
- Greenway plans
- Open space plans
- Trail plans
- Recreation master plans

## 3.4 County Commissioners' Pages
Check for:
- Land acquisitions
- Park resolutions
- Conservation partnerships
- Trail funding approvals

## 3.5 County Tourism / Visitors Bureau
Check for:
- Parks
- Trails
- Natural attractions
- Outdoor recreation assets

## 3.6 County-Hosted Municipal/Township Pages
These count as **authoritative** for municipal/township discovery.
All discoveries from county-hosted pages remain **Tier 4**.

All sources must be logged in **Discovery Metadata v5.0**.

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
Record `maps_raw` for all discovered map URLs (PDF, interactive, GPX, KML).

## 6.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment-level geometry or identifiers exist

## 6.5 Trail Network Creation
Create a **Trail Network** when:
- A county-managed multi-trail system exists
- A greenway corridor spans multiple Trails

## 6.6 Site Network Creation
Create a **Site Network** when:
- A county-managed multi-site system exists
- A conservation or greenway network is formally documented

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

Each county entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.0**
- **Discovery Metadata Specification v5.0**
- The appropriate Schema Module v5.0
- The appropriate Vocabulary Module v5.0

No normalized fields may appear in Tier 4 output.

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
# END OF COUNTY LANDS DISCOVERY SUB-PROCEDURE v5.0
