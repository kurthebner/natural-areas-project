# NATURAL AREAS PROJECT
# MUNICIPAL LANDS DISCOVERY SUB‑PROCEDURE v4.0
(Tier 6 — Cities, Villages, Incorporated Municipalities, County‑Hosted Municipal Pages, and Municipal Partner Assets)

This module defines the authoritative, deterministic Tier‑6 discovery rules for municipal lands within the v4.0 Raw → Resolution → Normalization → Entity Graph pipeline.

It supersedes all v3.x municipal discovery logic and all interim v3.3.x drafts.  
It is fully aligned with:

- Discovery Protocol Module v4.0
- Discovery Metadata Specification v4.0
- Tier Sub‑Procedure Template v4.0
- Discovery Orchestration Module v4.0

This module contains no controlled vocabularies.  
All vocabularies are defined in the appropriate v4.0 Vocabulary Modules.

------------------------------------------------------------
# 1. PURPOSE

The Municipal Lands Discovery Sub‑Procedure v4.0 defines how Tier 6 must:

- Identify all municipal‑owned or municipal‑managed Sites
- Identify child Sites within municipal Sites
- Identify Trails, Trail Segments, and Trail Networks managed or branded by municipalities
- Identify Site Networks (e.g., municipal greenway systems)
- Identify Access Points associated with municipal Sites and Trails
- Distinguish municipal management from county, township, district, state, federal, or private co‑management
- Handle multi‑department governance
- Handle county‑hosted municipal pages and official social media
- Handle joint‑use facilities
- Avoid false positives from similarly named places
- Log uncertainty, conflicts, and boundary cases
- Produce Raw Discovery Records v4.0
- Produce Discovery Metadata v4.0

This module is referenced only by:

- Discovery Protocol Module v4.0
- Discovery Orchestration Module v4.0
- Tier Sub‑Procedure Template v4.0

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to:

- City and village government websites
- Municipal recreation department pages
- Municipal planning documents
- Municipal GIS (if any)
- Municipal meeting minutes
- County‑hosted municipal pages
- Municipal tourism or community pages (if official)
- Official municipal social media (conditional)
- Municipal partner pages where the municipality is clearly identified as owner/manager/co‑manager

It governs discovery of:

- Sites
- Child Sites
- Trails
- Trail Segments
- Trail Networks
- Site Networks
- Access Points

Tier 6 sits below Township and above Conservancy/Private.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (ALL MANDATORY)

## 3.1 Municipal Website (If Exists)
Scan for:
- Parks
- Recreation
- Facilities
- Community
- Open Space / Green Space
- Natural Areas
- Trails / Pathways / Bikeways
- Greenways / Corridors
- Waterfront / Riverfront
- Sports complexes
- Community centers

Municipal websites often contain:
- Hidden subpages
- Non‑indexed pages
- PDF‑only listings
- Outdated or partial information

All must be scanned.

## 3.2 County‑Hosted Municipal Pages
Treat as authoritative for municipal discovery.
Discoveries remain Tier 6.

## 3.3 Municipal Recreation Departments
Scan:
- Program pages
- Facility pages
- Park listings
- Trail listings
- Brochures and PDFs

## 3.4 Municipal Planning Documents
Scan:
- Comprehensive plans
- Parks & recreation master plans
- Greenway plans
- Open space plans
- Trail plans
- Corridor plans

## 3.5 Municipal Meeting Minutes
Scan for:
- Land purchases
- Park dedications
- Trail agreements
- Conservation partnerships
- Facility improvements

## 3.6 Municipal GIS (If Exists)
Check for:
- Municipal‑owned parcels
- Park/open space layers
- Trail layers
- Recreation facility layers
- Easement layers

## 3.7 Municipal Social Media (Conditional)
Authoritative only if:
- Officially designated, OR
- Linked from municipal or county website

Scan for:
- Park announcements
- Facility openings
- Trail access information

## 3.8 Partner & Joint‑Use Sources (Conditional)
Authoritative when municipality is explicitly:
- Owner
- Manager
- Co‑manager

Examples:
- School district joint‑use parks
- YMCA‑operated but city‑owned facilities
- University greenways managed by city

------------------------------------------------------------
# 4. MUNICIPAL DOMAIN RULES & SPECIAL CASES

## 4.1 Municipal‑Owned vs Municipal‑Managed
Surface Sites when municipality:
- Owns
- Manages
- Co‑manages

Record governance in metadata.

## 4.2 Multi‑Department Governance
Municipal parks may be under:
- Parks & Recreation
- Public Works
- Utilities
- Planning
- Engineering

All are municipal governance.

## 4.3 Hidden or Non‑Indexed Pages
Include if:
- Clearly municipal
- Identity‑bearing

## 4.4 Municipal Recreation Assets Without a Recreation Department
Surface identity‑bearing:
- Parks
- Trails
- Facilities
- Natural areas

## 4.5 County‑Hosted Municipal Pages
Authoritative but remain Tier 6.

## 4.6 Multi‑Municipal Sites & Trails
Do not segment.
Record all municipalities and counties.

## 4.7 HOA Parks, Private Amenities, Gated Facilities
Exclude unless municipality is explicitly owner/manager.

## 4.8 Business Parks, Corporate Campuses, Plazas
Exclude unless formally designated as municipal parks.

## 4.9 Indoor‑Only Facilities
Exclude unless part of a larger identity‑bearing Site.

## 4.10 Brownfields, Redevelopment Areas, Future Parks
Include only if identity‑bearing and formally designated.

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

## 5.1 Enumerative Discovery
Enumerate:
- Park listing pages
- Trail listing pages
- Facility listing pages
- Natural area listings
- Map/brochure index pages

Extract all first‑level entity URLs.

## 5.2 Recursive Discovery
Follow internal links for:
- Trails
- Maps
- Facilities
- Access
- Reservations

Respect recursion limits and allowlists.

------------------------------------------------------------
# 6. ENTITY CREATION RULES

## 6.1 Site Creation
Create a Site when:
- Municipal‑owned/managed/co‑managed
- Identity‑bearing
- Public access exists
- Influences Access Point logic

Exclude:
- City halls
- Administrative buildings
- Cemeteries (unless natural areas)
- Maintenance yards

## 6.2 Child Site Creation
Create when:
- Named internal unit exists
- Identity‑bearing
- Relevant to navigation/access

Exclude:
- Unnamed amenities
- Temporary zones
- Operational zones

## 6.3 Trail Creation
Surface when:
- Named trail appears on municipal/county pages
- Named in planning documents
- Named in meeting minutes
- Named in GIS

## 6.4 Trail Segment Creation
Surface when:
- Segment geometry exists
- Segment identifiers exist

## 6.5 Trail Network Creation
Surface when:
- Municipal multi‑trail system exists
- Greenway corridor spans multiple Trails

## 6.6 Site Network Creation
Surface when:
- Municipal multi‑site system exists
- Conservation/greenway network documented

## 6.7 Access Point Creation
Surface when:
- Appears on municipal pages
- Appears on county‑hosted municipal pages
- Appears in planning documents
- Appears in meeting minutes
- Appears in GIS

Access Points must include raw:
- Name/label
- Access Point Type
- Municipality
- County list
- Parent entity
- Sources
- Notes

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

Tier 6 must surface:
- All municipal Sites
- All identity‑bearing child Sites
- All municipal Trails
- All municipal Trail Segments
- All municipal Access Points
- All parks/trails on county‑hosted municipal pages
- All identity‑bearing greenways
- All identity‑bearing joint‑use Sites

Tier 6 may surface:
- Trail Networks
- Site Networks
- Municipal easements
- Planned parks/trails (if identity‑bearing)
- Utility lands used as parks

Tier 6 must not surface:
- HOA/private amenities
- Indoor‑only facilities
- Business parks
- Non‑identity‑bearing parcels

------------------------------------------------------------
# 8. METADATA REQUIREMENTS

Each entity must include:
- Full Discovery Metadata v4.0
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships
- All geometry (if available)

All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each municipal entity must output:
- Raw Discovery Record v4.0
- Discovery Metadata v4.0
- Schema Module v4.0 compliance
- Vocabulary Module v4.0 compliance

Discovery must not:
- Normalize
- Correct
- Dedupe
- Infer
- Invent
- Silently modify

------------------------------------------------------------
# 10. INTEGRATION POINTS

Integrates with:
- Discovery Protocol Module v4.0
- Discovery Orchestration Module v4.0
- Tier Sub‑Procedure Template v4.0
- All Entity Discovery Sub‑Procedures v4.0
- Child Site Rules Module v4.0
- Discovery Metadata Specification v4.0
- Discovery Output Specification v4.0
- Normalization Engine v4.0
- Resolution Engine v4.0
- Entity Upsert Engine v4.0
- TSV Output Specifications v4.0
- Audit & Logging Module v4.0
- County Baseline Module v4.0

------------------------------------------------------------
# 11. VERSIONING

- This module is Municipal Lands Discovery Sub‑Procedure v4.0.
- Updates may produce v4.1, v4.2, etc.
- Tier order changes must be made in the Discovery Protocol Module v4.0.

------------------------------------------------------------
# END OF MUNICIPAL LANDS DISCOVERY SUB‑PROCEDURE v4.0