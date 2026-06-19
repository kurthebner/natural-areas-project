# NATURAL AREAS PROJECT
# PRIVATE & ORGANIZATION-BASED DISCOVERY SUB-PROCEDURE v5.0
(Tier 8 — Private Nature Preserves, Camps, Retreat Centers, Scout Camps, Church Camps, Fraternal Lands, HOA Open Space, Corporate Lands)

This module defines the authoritative, deterministic Tier-8 discovery rules for
private and organization-based lands within the v5.0 Raw → Resolution → Normalization →
Entity Graph pipeline.

This module supersedes Private & Organization-Based Discovery Sub-Procedure v4.0.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.0 Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v4.0

- `role_raw` and `access_level_raw` removed from output — deleted from Access Point schema
- `features_raw` added to output for Access Point and Site amenities
- `difficulty_raw` and `accessibility_raw` added to output for Trails and Trail Segments
- `maps_raw` added to output for Trails, Trail Segments, and Networks
- `township_raw` and `municipality_raw` explicitly prohibited — GIS-derived only
- **Cross-reference discovery** added — partnership mentions in previous tiers must be investigated
- **Multi-method search strategy** formalized
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Private & Organization-Based Discovery Sub-Procedure v5.0 defines how Tier 8 must:

- Identify private or organization-based Sites
- Identify child Sites within private holdings
- Identify Trails, Trail Segments, and Trail Networks on private lands
- Identify Site Networks (rare but possible)
- Identify Access Points associated with private holdings
- Distinguish public, limited, and private access
- Identify identity-bearing private natural areas
- Identify private preserves owned by nonprofits or foundations
- Identify private trail systems with public or limited access
- Handle multi-county private holdings
- Log uncertainty, conflicts, and boundary cases
- Produce Raw Discovery Records v5.0
- Produce Discovery Metadata v5.0

This module is referenced only by:

- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0

------------------------------------------------------------
# 2. SCOPE

This sub-procedure applies to:

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
- University natural areas and research preserves

Tier 8 is the final discovery tier. It must surface all identity-bearing private lands
relevant to recreation, access, or natural area identity.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 8 must enumerate and recursively explore all authoritative private-sector sources.

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

Always **fetch** official pages directly — do not rely on search snippets alone.

Scan all:
- Facility pages
- Program pages
- Maps
- PDF brochures
- Reservation pages (if they reveal identity-bearing Sites or child Sites)

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
- Multi-county detection

## 3.3 Statewide & Regional Directories
Check:
- Ohio campground directories
- Ohio tourism directories
- Regional recreation guides
- Scout council property lists
- Church camp directories
- Fraternal organization property lists
- University natural area listings

## 3.4 Cross-Reference from Previous Tiers
Any private organization mentioned in Tiers 1–7 must be investigated here.

Examples of cross-reference triggers:
- "In partnership with [Scout Camp]"
- "Managed by [Private Foundation]"
- "Trail connecting to [Private Preserve]"
- "[University] natural area"
- Donor-named facilities or preserves (may have associated foundations)

Each trigger requires a dedicated search for that organization's holdings in the county.

## 3.5 Organizational Partners
Private lands may appear in:
- Land trust partnership announcements
- County planning documents
- Regional trail plans
- Watershed group projects

## 3.6 Social Media (Conditional)
Private organization social media is authoritative only if:
- Explicitly designated as official, OR
- Linked from the organization's website, OR
- Linked from a county or municipal website

If official:
- Scan for trail announcements
- Scan for access information
- Scan for seasonal closures or access restrictions

If not official → exclude.

All sources must be logged in **Discovery Metadata v5.0**.

------------------------------------------------------------
# 4. PRIVATE LAND DISCOVERY CONDITIONS

A private or organization-based Site must be surfaced if:

✔ Identity-bearing (named, mapped, or designated)
✔ Public or limited public access (seasonal, fee-based, reservation-only, program-only)
✔ Appears in authoritative directories
✔ Appears in county GIS as a recreation or natural area
✔ Is a private preserve owned by a nonprofit or foundation
✔ Is a private trail system with public or limited access
✔ Is a private campground with natural area components
✔ Is a private retreat center with trails or natural areas
✔ Is a university natural area or research preserve with visitor access

Exclude:
- Private lands with no public access and no identity-bearing role
- HOA open space with no public access
- Corporate campuses with no public access
- Private hunting clubs with no public access
- Private farms with no recreation role
- Private residences

## 4.1 Limited-Access Sites
If access is:
- Seasonal
- Fee-based
- Reservation-only
- Program-only

→ Include, but record access limitations in `notes_raw` and metadata.

## 4.2 Multi-County Sites
- Do not segment multi-county Sites
- Record all counties exactly as discovered in `counties_raw`

------------------------------------------------------------
# 5. MULTI-METHOD SEARCH STRATEGY

Private entities are the hardest to find because they are not centralized in
government databases, often have limited web presence, and may not market broadly.

Use all four methods for each county.

## 5.1 Method 1: Direct Searches
Run targeted searches:
- "[County] Ohio private nature center"
- "[County] Ohio private preserve"
- "[County] Ohio nonprofit nature"
- "university natural area [County] Ohio"
- "scout camp [County] Ohio"
- "church camp [County] Ohio"
- "retreat center trails [County] Ohio"

## 5.2 Method 2: Cross-Reference from Prior Tiers
Review all entities discovered in Tiers 1–7 for:
- Partnership mentions
- Affiliated facilities
- "In partnership with..." language
- Donor names (may have associated foundations)
- Trail connections to off-site properties

Each mention is a discovery lead. Follow it.

## 5.3 Method 3: Specific Organization Searches
Search known regional organizations:
- "[The Nature Conservancy] [County] Ohio"
- "[Audubon Society] [County] Ohio"
- "[Local Land Trust] [County] Ohio"
- "[Major University] natural areas [County]"
- "[Scout Council] camps [County] Ohio"

## 5.4 Method 4: Comprehensive Website Fetch
For any discovered private entity:
- Fetch the full website homepage
- Fetch "properties," "preserves," or "locations" pages
- Look for property lists and maps
- Extract ALL locations, not just highlighted ones

------------------------------------------------------------
# 6. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 8 must use both enumerative and recursive discovery.

## 6.1 Enumerative Discovery (Listing Pages)
Enumerate:
- Camp listings
- Preserve listings
- Trail listings
- Facility listings
- Map index pages
- Directory-linked pages

Extract ALL first-level entity URLs.

## 6.2 Recursive Discovery (URL Propagation)
Follow internal links for:
- Trails
- Maps
- Access
- Facilities
- Natural areas
- Program areas

Respect recursion limits and allowlists.

------------------------------------------------------------
# 7. ENTITY CREATION RULES

## 7.1 Site Creation
A private feature becomes a Site if:
- Identity-bearing
- Public or limited public access exists
- Appears in authoritative directories
- Appears in county GIS as a recreation/natural area
- Is a private preserve owned by a nonprofit or foundation
- Is a private trail system with public access
- Is a private campground with natural area components
- Is a private retreat center with trails or natural areas
- Is a university natural area or research preserve with access

Exclude:
- Administrative offices
- Indoor-only facilities
- Private easements with no identity-bearing role

## 7.2 Child Site Creation
Create a child Site when:
- A named internal unit exists within a private Site
- A named natural area, recreation area, or facility is documented
- A named lake area, trail area, or program area is identity-bearing

Do not surface:
- Unnamed amenities
- Temporary zones
- Unnamed management areas

## 7.3 Trail Creation
Surface a Trail when:
- A named trail appears on official maps or brochures
- A named trail appears in directories
- A named trail appears in county GIS
- A named trail appears in partnership announcements

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `maps_raw` for all discovered map URLs.

## 7.4 Trail Segment Creation
Surface Trail Segments when:
- Segment-level geometry exists in county GIS
- Segment identifiers appear in maps or brochures

## 7.5 Trail Network Creation
Surface a Trail Network when:
- A private organization manages a multi-trail system
- A corridor-scale or campus-scale network is documented

## 7.6 Site Network Creation
Surface a Site Network when:
- A private organization manages a multi-site system
- A corridor-scale or campus-scale network is documented

## 7.7 Access Point Creation
Surface an Access Point when:
- It appears on official maps
- It appears in brochures
- It appears in county GIS
- It appears in directories
- It appears in partnership announcements

Record `features_raw` for all documented amenities at the access point.
Record access limitations in `notes_raw` (e.g., seasonal, fee-based, reservation-only).
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.

------------------------------------------------------------
# 8. TIER-SPECIFIC EXPECTATIONS

Tier 8 must surface:
- All identity-bearing private Sites
- All identity-bearing child Sites
- All private Trails
- All private Trail Segments
- All private Access Points
- All private trail systems with public or limited access
- All private preserves owned by nonprofits or foundations
- All university natural areas and research preserves with visitor access
- All organizations referenced in partnership mentions from Tiers 1–7

Tier 8 may surface:
- Private Trail Networks
- Private Site Networks
- Corridor-scale or campus-scale systems
- Partnership lands (if identity-bearing)

Tier 8 must not surface:
- Non-identity-bearing private lands
- HOA/private amenities with no public access
- Corporate campuses with no public access
- Private hunting clubs with no public access

------------------------------------------------------------
# 9. METADATA REQUIREMENTS

Each discovered entity must include:

- Full **Discovery Metadata v5.0**
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships
- All geometry (if available)
- `features_raw` for Sites and Access Points (if documented)
- `difficulty_raw` and `accessibility_raw` for Trails and Trail Segments (if explicitly stated)
- `maps_raw` for Trails, Trail Segments, Trail Networks, and Site Networks
- Access limitations recorded in `notes_raw`
- Raw ownership type in `ownership_raw`

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 10. OUTPUT REQUIREMENTS

Each private or organization-based entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.0**
- **Discovery Metadata Specification v5.0**
- The appropriate Schema Module v5.0
- The appropriate Vocabulary Module v5.0

No normalized fields may appear in Tier 8 output.

------------------------------------------------------------
# 11. INTEGRATION POINTS

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
# 12. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.0
- Discovery Output Specification v5.0
- Discovery Metadata Specification v5.0
- All six entity Discovery Sub-Procedures v5.0
- Child Site Rules Module v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF PRIVATE & ORGANIZATION-BASED DISCOVERY SUB-PROCEDURE v5.0
