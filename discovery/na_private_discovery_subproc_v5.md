# NATURAL AREAS PROJECT
# PRIVATE & ORGANIZATION-BASED DISCOVERY SUB-PROCEDURE v5.1
(Tier 8 — Private Nature Preserves, Camps, Retreat Centers, Scout Camps, Church Camps, Fraternal Lands, HOA Open Space, Corporate Lands)

This module defines the authoritative, deterministic Tier-8 discovery rules for
private and organization-based lands within the v5.0 Raw → Resolution → Normalization →
Entity Graph pipeline.

This module supersedes Private & Organization-Based Discovery Sub-Procedure v5.0.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.0 Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.0

- **OBS-026**: Governance verification rule added to §4 — county lists mix tiers; always
  verify governance independently before assigning Tier 8
- **OBS-027**: Boundary overlap flag protocol added to §4.3 — when private parcel overlaps
  with known public land, flag as BOUNDARY_OVERLAP for GIS verification
- **OBS-030**: Hunting preserve and agritourism search queries added to §5.1
- **OBS-031**: NRHP features within Tier-8 parcels rule added to §7.1 — NRHP-listed
  features on private land with public access create child Site records

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

## 4.3 Governance Verification Before Tier Assignment
County recreation websites, visitor bureau listings, and tourism directories
frequently list sites from multiple governance tiers in a single mixed list.
A site appearing on a county website does NOT mean it is Tier 8 (private) —
it may be Tier 4 (county), Tier 5 (township), Tier 6 (municipal), or Tier 7
(conservancy).

**Before assigning Tier 8**, verify governance independently:
1. Check county auditor for parcel owner
2. If owner is a government body → assign to the appropriate tier, not Tier 8
3. If owner is a nonprofit → assign Tier 7, not Tier 8
4. If owner is a private individual or for-profit entity → assign Tier 8

Record the governance verification source in metadata. Do not assign Tier 8
by default when governance is unclear.

## 4.4 Boundary Overlap Flag Protocol
When a private parcel appears to overlap with a known public land unit (state
forest, wildlife area, county park, etc.) based on GPS coordinates or GIS review:

- Do not suppress the private entity
- Do not assume the GPS is wrong
- Flag with: `BOUNDARY_OVERLAP — parcel overlaps with [entity name]; GIS verification required`
- Document both the private parcel information and the overlapping public entity
- Resolution and normalization will arbitrate using authoritative GIS data

Boundary overlaps are common where private inholdings exist within public land
units, where easements cross public-private boundaries, and where addressing
systems assign addresses in adjacent parcels.

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

**Hunting preserves and agritourism** (mandatory — these are commonly missed):
- "[County] Ohio hunting preserve"
- "[County] Ohio fee hunting land"
- "[County] Ohio pheasant farm hunting"
- "[County] Ohio deer hunting preserve"
- "[County] Ohio agritourism"
- "[County] Ohio farm trails"
- "[County] Ohio pick your own farm trails"

Also check:
- **ODNR Licensed Hunting Preserves Registry**: Search ODNR website for the
  county's licensed hunting preserves. ODNR licenses private hunting preserves
  and maintains a registry. These are frequently missed because they don't appear
  in standard park or recreation searches.
- Ohio Agritourism Association member directory (if available)

Private hunting preserves with public/fee access are valid Tier-8 Sites even when
their primary use is commercial. Many also maintain trail systems and natural areas.

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

**NRHP Features Within Private Parcels**: When a National Register of Historic
Places listing (mound, archaeological site, historic structure, historic district)
exists within or on a private parcel that is already being documented as a Tier-8
Site:
- If the NRHP feature has public visitor access → create a child Site record
  with `parent_site_id` pointing to the private parcel Site
- If the NRHP feature has no public access → add as a note in `notes_raw`:
  "NRHP-listed feature on property: [name], [NRHP ref]"
- Do not create a standalone Site for a non-public NRHP feature on private land

When a standalone NRHP listing exists on private land with documented public
access (e.g., a mound accessible via easement), create it as a Tier-8 Site
directly. Cross-reference the NRHP record number in `notes_raw`.

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
