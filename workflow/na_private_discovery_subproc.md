# NATURAL AREAS PROJECT
# PRIVATE & ORGANIZATION‑BASED DISCOVERY SUB‑PROCEDURE v4.0
(Tier 8 — Private Nature Preserves, Camps, Retreat Centers, Scout Camps, Church Camps, Fraternal Lands, HOA Open Space, Corporate Lands)

This module defines the authoritative, deterministic Tier‑8 discovery rules for private and organization‑based lands within the v4.0 Raw → Resolution → Normalization → Entity Graph pipeline.

It supersedes all v3.x private‑tier logic and is fully aligned with:

- Discovery Protocol Module v4.0
- Discovery Metadata Specification v4.0
- Tier Sub‑Procedure Template v4.0
- Discovery Orchestration Module v4.0

This module contains no controlled vocabularies.  
All vocabularies are defined in the appropriate v4.0 Vocabulary Modules.

------------------------------------------------------------
# 1. PURPOSE

The Private & Organization‑Based Discovery Sub‑Procedure v4.0 defines how Tier 8 must:

- Identify private or organization‑based Sites
- Identify child Sites within private holdings
- Identify Trails, Trail Segments, and Trail Networks on private lands
- Identify Site Networks (rare but possible)
- Identify Access Points associated with private holdings
- Distinguish public, limited, and private access levels
- Identify identity‑bearing private natural areas
- Identify private preserves owned by nonprofits or foundations
- Identify private trail systems with public or limited access
- Handle multi‑county private holdings
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

- Private nature preserves
- Private campgrounds
- Church camps
- Scout camps
- Fraternal organization lands
- HOA open space
- Corporate campuses with natural areas
- Private hunting/fishing clubs
- Private retreat centers
- Private trail systems
- Private foundations with land holdings

Tier 8 governs discovery of:

- Sites
- Child Sites
- Trails
- Trail Segments
- Trail Networks
- Site Networks
- Access Points

Tier 8 is the final discovery tier and must surface all identity‑bearing private lands relevant to recreation, access, or natural area identity.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 8 must enumerate and recursively explore all authoritative private‑sector sources.

## 3.1 Official Websites
Scan for:
- Nature preserve
- Camp
- Retreat center
- Outdoor center
- Hiking trails
- Natural area
- Open space
- Wildlife area

Scan all:
- Facility pages
- Program pages
- Maps
- PDF brochures
- Reservation pages (if they reveal identity‑bearing Sites or child Sites)

## 3.2 County Auditor / GIS (Parcel Verification)
Private holdings often appear as:
- Private preserves
- Private campgrounds
- Private recreation areas
- HOA open space
- Corporate natural areas

GIS is required for:
- County boundary confirmation
- Ownership confirmation
- Access point verification
- Parcel extent verification
- Multi‑county detection

## 3.3 Statewide & Regional Directories
Check:
- Ohio campground directories
- Ohio tourism directories
- Regional recreation guides
- Scout council property lists
- Church camp directories
- Fraternal organization property lists

## 3.4 Organizational Partners
Private lands may appear in:
- Land trust partnership announcements
- County planning documents
- Regional trail plans
- Watershed group projects

## 3.5 Social Media (Conditional)
Private organization social media is authoritative only if:
- Explicitly designated as official, OR
- Linked from the organization’s website, OR
- Linked from a county or municipal website

If official:
- Scan for trail announcements
- Scan for access information
- Scan for seasonal closures or access restrictions

If not official → exclude.

------------------------------------------------------------
# 4. PRIVATE LAND DISCOVERY CONDITIONS

A private or organization‑based Site must be surfaced if:

### ✔ Identity‑bearing (named, mapped, or designated)  
### ✔ Public or limited public access (seasonal, fee‑based, reservation‑only, program‑only)  
### ✔ Appears in authoritative directories  
### ✔ Appears in county GIS as a recreation or natural area  
### ✔ Is a private preserve owned by a nonprofit or foundation  
### ✔ Is a private trail system with public or limited access  
### ✔ Is a private campground with natural area components  
### ✔ Is a private retreat center with trails or natural areas  

### ❌ Exclude:
- Private lands with no public access and no identity‑bearing role
- HOA open space with no public access
- Corporate campuses with no public access
- Private hunting clubs with no public access
- Private farms with no recreation role
- Private residences

## 4.9 Limited‑Access Sites
If access is:
- Seasonal
- Fee‑based
- Reservation‑only
- Program‑only

→ Include, but record access limitations in metadata.

## 4.10 Multi‑County Sites
- Do not segment multi‑county Sites
- Record all counties exactly as discovered in `counties_raw`

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 8 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Enumerate:
- Camp listings
- Preserve listings
- Trail listings
- Facility listings
- Map index pages
- Directory‑linked pages

Extract all first‑level entity URLs.

## 5.2 Recursive Discovery (URL Propagation)
Follow internal links for:
- Trails
- Maps
- Access
- Facilities
- Natural areas
- Program areas

Respect recursion limits and allowlists.

------------------------------------------------------------
# 6. ENTITY CREATION RULES

## 6.1 Site Creation
A private feature becomes a Site if:
- Identity‑bearing
- Public or limited public access exists
- Appears in authoritative directories
- Appears in county GIS as a recreation/natural area
- Is a private preserve owned by a nonprofit or foundation
- Is a private trail system with public access
- Is a private campground with natural area components
- Is a private retreat center with trails or natural areas

Exclude:
- Administrative offices
- Indoor‑only facilities
- Private easements with no identity‑bearing role

## 6.2 Child Site Creation
Create a child Site when:
- A named internal unit exists within a private Site
- A named natural area, recreation area, or facility is documented
- A named lake area, trail area, or program area is identity‑bearing

Do not surface:
- Unnamed amenities
- Temporary zones
- Unnamed management areas

## 6.3 Trail Creation
Surface a Trail when:
- A named trail appears on official maps or brochures
- A named trail appears in directories
- A named trail appears in county GIS
- A named trail appears in partnership announcements

## 6.4 Trail Segment Creation
Surface Trail Segments when:
- Segment‑level geometry exists in county GIS
- Segment identifiers appear in maps or brochures

## 6.5 Trail Network Creation
Surface a Trail Network when:
- A private organization manages a multi‑trail system
- A corridor‑scale or campus‑scale network is documented

## 6.6 Site Network Creation
Surface a Site Network when:
- A private organization manages a multi‑site system
- A corridor‑scale or campus‑scale network is documented

## 6.7 Access Point Creation
Surface an Access Point when:
- It appears on official maps
- It appears in brochures
- It appears in county GIS
- It appears in directories
- It appears in partnership announcements

Access Points must include raw:
- Name or descriptive label
- Access Point Type
- County list
- Parent entity
- Access level
- Sources
- Notes (including access limitations)

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

Tier 8 must surface:
- All identity‑bearing private Sites
- All identity‑bearing child Sites
- All private Trails
- All private Trail Segments
- All private Access Points
- All private trail systems with public or limited access
- All private preserves owned by nonprofits or foundations

Tier 8 may surface:
- Private Trail Networks
- Private Site Networks
- Corridor‑scale or campus‑scale systems
- Partnership lands (if identity‑bearing)

Tier 8 must not surface:
- Non‑identity‑bearing private lands
- HOA/private amenities with no public access
- Corporate campuses with no public access
- Private hunting clubs with no public access

------------------------------------------------------------
# 8. METADATA REQUIREMENTS

Each discovered entity must include:
- Full Discovery Metadata v4.0
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships
- All geometry (if available)
- Raw access level
- Raw ownership type

All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each private or organization‑based entity must output:
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

- This module is Private & Organization‑Based Discovery Sub‑Procedure v4.0.
- Updates to private recreation directories or organizational practices may result in v4.1, v4.2, etc.
- Tier order changes must be made in the Discovery Protocol Module v4.0.

------------------------------------------------------------
# END OF PRIVATE & ORGANIZATION‑BASED DISCOVERY SUB‑PROCEDURE v4.0