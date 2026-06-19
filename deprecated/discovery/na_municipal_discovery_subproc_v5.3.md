# NATURAL AREAS PROJECT
# MUNICIPAL LANDS DISCOVERY SUB-PROCEDURE v5.3
(Tier 6 — Cities, Villages, Incorporated Municipalities, County-Hosted Municipal Pages, and Municipal Partner Assets)

This module defines the authoritative, deterministic Tier-6 discovery rules for
municipal lands within the v5.x Raw → Resolution → Normalization → Entity Graph pipeline.

This module supersedes Municipal Lands Discovery Sub-Procedure v5.2.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

**This tier has the highest risk of missed entities.**
Municipal discovery requires exhaustive individual-municipality searching.
Small villages must not be skipped or assumed empty based on population.
A village of 500 people can have three parks totaling 20+ acres.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- Expanded Step 3 (Page Fetch) with explicit first-pass capture guidance: description_raw and features_raw must both be extracted during the same park page fetch — no deferred return visits
- Added Step 3 guidance on what municipal park pages typically contain and where to find description text vs. amenity lists
- Added governance_raw contamination warning: GIS park type labels from municipal GIS layers must never be written to governance_raw
- Updated Section 10 (Metadata Requirements) to explicitly list description_raw as a required capture target where present

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Updated all cross-module references to v5.x
- Updated header version to v5.2

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **OBS-018**: Browser-unavailable branch added — municipalities cannot be marked COMPLETE
  without map verification; use PENDING/UNVERIFIED status when browser is not connected
- **OBS-019**: Fallback protocol formalized — empty/absent parks pages require Google Maps,
  Tripadvisor, county GIS parcel search, and grant record search before recording zero
- **OBS-020**: Parks board site check added — semi-autonomous parks boards operate separate
  websites; both city government site AND parks board site must be checked
- **OBS-021**: Map verification step made explicit and mandatory (Step 4); rationale
  documented with New Vienna Gazebo Park case study
- **OBS-022**: Access point scanning added to map verification step — trail access points
  visible on map should be captured during municipal map verification pass
- **OBS-023**: Grant record search added as Step 7 — mandatory for villages with no
  official parks page; documents Martinsville Village Park case study as rationale

------------------------------------------------------------
# CHANGES FROM v4.0

- `role_raw` and `access_level_raw` removed from output — deleted from Access Point schema
- `features_raw` added to output for Access Point and Site amenities
- `difficulty_raw` and `accessibility_raw` added to output for Trails and Trail Segments
- `maps_raw` removed; map URLs now included in `urls_raw`
- `township_raw` and `municipality_raw` explicitly prohibited — GIS-derived only
- **Systematic individual-municipality search protocol** added — every municipality must be individually searched, no exceptions
- **Fetch-over-search rule** formalized — search snippets are insufficient; official pages must be fetched
- **Village-specific search steps** added
- **Documentation of negative results** made explicit and mandatory
- **Red flags checklist** added to assist with completeness verification
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Municipal Lands Discovery Sub-Procedure v5.x defines how Tier 6 must:

- Identify all municipal-owned or municipal-managed Sites
- Identify child Sites within municipal Sites
- Identify Trails, Trail Segments, and Trail Networks managed or branded by municipalities
- Identify Site Networks (e.g., municipal greenway systems)
- Identify Access Points associated with municipal Sites and Trails
- Distinguish municipal management from county, township, district, state, federal, or private co-management
- Handle multi-department governance
- Handle county-hosted municipal pages and official social media
- Handle joint-use facilities
- Avoid false positives from similarly named places
- Log uncertainty, conflicts, and boundary cases
- Produce Raw Discovery Records v5.x
- Produce Discovery Metadata v5.x

This module is referenced only by:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x

------------------------------------------------------------
# 2. SCOPE

This sub-procedure applies to:

- City and village government websites
- Municipal recreation department pages
- Municipal planning documents
- Municipal GIS (if any)
- Municipal meeting minutes
- County-hosted municipal pages
- Municipal tourism or community pages (if official)
- Official municipal social media (conditional)
- Municipal partner pages where the municipality is clearly identified as owner/manager/co-manager

Tier 6 sits **below Township** and **above Conservancy/Private**.

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
- Hidden subpages not linked from the homepage
- Non-indexed pages
- PDF-only listings
- Outdated or partial information

All must be scanned. Always **fetch** the official parks or recreation page directly.
Do not rely on search snippets — they frequently omit entities.

## 3.2 County-Hosted Municipal Pages
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
- Municipal-owned parcels
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

## 3.8 Partner & Joint-Use Sources (Conditional)
Authoritative when municipality is explicitly:
- Owner
- Manager
- Co-manager

Examples:
- School district joint-use parks
- YMCA-operated but city-owned facilities
- University greenways managed by city

------------------------------------------------------------
# 4. SEARCH PROTOCOL (PER MUNICIPALITY)

**Every municipality must be individually searched. No exceptions.**

Municipalities cannot be skipped based on:
- Population size
- Perceived likelihood of having parks
- Prior assumptions
- Time pressure
- Having already found many entities in the county

Small villages frequently have parks. A village of 500 people may have three parks
totaling 20+ acres. Discovery that skips small municipalities is incomplete discovery.

## 4.1 Step 1: Get the Complete Municipality List First

Before searching any municipality, obtain a complete list of ALL municipalities
(cities and villages) in the county. This list is the enumeration baseline.

Required information for each municipality:
- Official name
- Municipality type (city or village)
- Population (for context only — not to skip)
- Official website URL (if known)

Do not begin individual searches until the full list exists.

## 4.2 Step 2: Individual Search (Each Municipality)

For EACH municipality, run:
```
Search: "[Municipality Name] Ohio parks recreation"
Search: "[Municipality Name] Ohio official website"
```

Then fetch any official website or parks/recreation page discovered.

**Important**: Some municipalities operate parks through a semi-autonomous parks board
or recreation commission with its own separate website (e.g., `[city]parks.org` distinct
from `[city]ohio.gov`). Always check both the city government site AND any dedicated
parks department or recreation board site — they frequently contain different information.
If only the government site is checked, parks managed by a semi-autonomous board may be missed.

## 4.3 Step 3: Page Fetch (Mandatory When Official Page Found)

If an official website or parks/recreation page is found:
- **Fetch the full page** using web_fetch
- Read the **entire page content**, not just headers
- Check navigation menus — they may list more parks than main content
- Check linked PDFs and brochures
- Extract ALL parks, trails, and facilities listed

**Never mark a municipality complete based on a search snippet alone.**

### First-Pass Capture — Extract All Available Fields in a Single Fetch ✨ NEW IN v5.3

When fetching an individual park page, extract ALL available fields in one pass. Municipal park pages typically contain most or all of the following in a single page load — do not defer any field to a return visit:

**Identifying fields** (always present):
- `name_raw` — the park's official name as listed
- `category_raw` — type label if stated ("neighborhood park," "nature preserve," etc.)
- `location_raw` — address or geographic description

**Narrative description** (usually the introductory paragraph or "About" section):
- `description_raw` — capture the narrative paragraph(s) verbatim; this is the prose that describes the park's character, ecology, history, or community significance. It is different from an amenity list.
- If no narrative paragraph exists on the page, leave blank — do not invent

**Amenity/features list** (usually icons, bullets, or a "Facilities" section):
- `features_raw` — capture the amenity list verbatim as comma-separated items: "Picnic shelter, restrooms, playground, fishing pond." These are NOT sentences; they are list items.
- If no amenity list is present on the page, leave blank — do not infer

**Organizational fields** (ownership/governance if stated):
- `governance_raw` — managing organization name ONLY. Never include GIS park type labels here (see contamination rule below)

**Additional fields** (when present):
- `acres_raw`, `gps_lat_raw`, `gps_lon_raw`, `urls_raw` (all URLs including PDFs and maps)

**Governance Contamination Rule**: Municipal GIS layers frequently tag parks with administrative classifications (e.g., "Community Park," "Neighborhood Park," "Mini Park"). These are NOT governance — they are category hints. If a GIS source provides both a managing organization and a park type label:
- `governance_raw`: `City of Dublin` ✓
- `governance_raw`: `City of Dublin; GIS park type: Community Park` ✗

Record GIS park type labels in `category_raw` or `identity_notes_raw`, never in `governance_raw`.

**A return visit to a park page you already fetched to collect fields that were available on first visit is a process failure.** One fetch → all fields.

## 4.4 Step 4: Map Verification (Mandatory for All Municipalities)

After fetching official pages, **view Google Maps directly** for every municipality.
Open the map and visually inspect the area — do not search for map references.

Map verification is **mandatory** regardless of what official pages contain, because:
- Parks can appear on Google Maps with no official web presence (e.g., New Vienna Gazebo Park)
- Official websites are frequently incomplete or outdated
- Small parks and neighborhood parks are consistently underrepresented online

**For villages under 1,000 population**: Map verification is especially critical.
Never mark a village as zero parks without viewing the map directly.

**Browser unavailable**: If Claude in Chrome is not connected, do NOT mark municipalities
complete. Flag each unverified municipality as `PENDING/UNVERIFIED — map verification
required` and complete this step in a follow-up session before closing the tier.
"Browser unavailable" is not a valid basis for a zero determination.

**During map verification, also scan for trail access points**: If the map shows
trailhead markers, parking areas, or access points for trails already documented
in higher tiers, capture these as Access Point records linked to the parent trail.
Map verification is the primary method for catching access points not documented
on official pages.

## 4.5 Step 5: Fallback Protocol (When Official Pages Are Empty or Absent)

If the official parks page is empty, events-only, or no official website exists,
run the following fallback searches before recording zero:

1. **Google Maps view** (Step 4 above — mandatory regardless)
2. **Tripadvisor search**: "[Municipality Name] Ohio parks attractions"
3. **County GIS parcel search**: Check for parcels with owner = municipality name
4. **Grant record search** (see Step 6 below)

Document all fallback sources used in the municipality's outcome record.
A zero determination requires evidence from at least two sources, including map verification.

## 4.6 Step 6: Count Verification

If the page mentions:
- "Parks" (plural) → Find at least 2
- "X acres of parks" → Parks found should account for that acreage
- "Multiple locations" → List all locations
- Navigation with N park entries → Extract all N

Mismatches are red flags. Investigate before marking complete.

## 4.7 Step 7: Grant Record Search (Mandatory for Villages with No Official Parks Page)

For any municipality where the official parks page is empty, absent, or events-only,
search local and state grant award records before recording zero:

```
Search: "[Municipality Name] Ohio LEGACY Fund grant park"
Search: "[Municipality Name] Ohio LWCF grant recreation"
Search: "[Municipality Name] Ohio parks recreation fund grant"
Search: "[County] Community Foundation grant [Municipality Name]"
```

Grant records confirm park existence even when no web or map presence exists.
A grant award for "park restoration" or "park improvements" is definitive evidence
that a park exists. Create a raw record for the park and flag it as
`GRANT_CONFIRMED — no web/map presence; park name and location require field verification`.

This step is critical because grant-confirmed parks are completely invisible to
standard web search and sometimes invisible to Google Maps (e.g., Martinsville Village
Park, Clinton County: confirmed by $37,790 LEGACY Fund grant, not found by search or map).

## 4.8 Step 8: Document Results

For each municipality, record the outcome regardless of findings:

If parks found:
```
Municipality: [Name]
Status: COMPLETE
Parks Found: [N]
  1. [Park Name] — [Address/Location]
  2. [Park Name] — [Address/Location]
Source: [URL]
Date: [ISO date]
```

If no parks found (fully verified):
```
Municipality: [Name]
Status: COMPLETE
Parks Found: 0
Evidence: Official website checked; parks/recreation page found; no parks listed.
           Map viewed directly — no park markers found.
           Grant search conducted — no awards found.
           OR: No official website found; [alternative evidence].
Source: [URL or "no website found"]
Date: [ISO date]
```

If browser unavailable (map verification not possible):
```
Municipality: [Name]
Status: PENDING/UNVERIFIED — map verification required
Parks Found: [N confirmed from web sources only]
Evidence: Web search and page fetch complete. Map verification not possible —
           browser (Claude in Chrome) not connected. Must be revisited.
Date: [ISO date]
```

**Never document:**
- "Probably no parks" ❌
- "Likely none — small village" ❌
- "Too small to have parks" ❌
- "Assumed zero" ❌
- "Browser unavailable — marking zero" ❌

Every zero requires documented evidence from both web sources AND map verification.

------------------------------------------------------------
# 5. MUNICIPAL DOMAIN RULES & SPECIAL CASES

## 5.1 Municipal-Owned vs Municipal-Managed
Surface Sites when municipality:
- Owns
- Manages
- Co-manages

Record governance in metadata; do not attempt to resolve conflicts.

## 5.2 Multi-Department Governance
Municipal parks may be under:
- Parks & Recreation
- Public Works
- Utilities
- Planning
- Engineering

All are municipal governance.

## 5.3 Hidden or Non-Indexed Pages
Include if:
- Clearly municipal
- Identity-bearing

## 5.4 Municipal Recreation Assets Without a Recreation Department
Surface identity-bearing:
- Parks
- Trails
- Facilities
- Natural areas

The absence of a recreation department does not mean the absence of parks.

## 5.5 County-Hosted Municipal Pages
Authoritative but remain Tier 6.

## 5.6 Multi-Municipal Sites & Trails
Do not segment. Record all municipalities and counties.

## 5.7 HOA Parks, Private Amenities, Gated Facilities
Exclude unless municipality is explicitly owner/manager.

## 5.8 Business Parks, Corporate Campuses, Plazas
Exclude unless formally designated as municipal parks.

## 5.9 Indoor-Only Facilities
Exclude unless part of a larger identity-bearing Site.

## 5.10 Brownfields, Redevelopment Areas, Future Parks
Include only if identity-bearing and formally designated.

------------------------------------------------------------
# 6. RED FLAGS: INDICATORS OF MISSED ENTITIES

The following patterns suggest you may have missed entities. Investigate before marking a municipality complete.

🚩 Plural without count match:
- Page says "parks" but you only found 1 park
- Page mentions "over X acres of parks" but your parks don't add up

🚩 Navigation vs. content mismatch:
- Navigation menu lists 5 parks; main content describes 3

🚩 Partnership mentions:
- "In partnership with [organization]" — have you searched that organization?

🚩 Vague location descriptions:
- "Multiple locations throughout the municipality" — did you find all of them?

🚩 Infrastructure without attribution:
- Trail ends at "small park" — what is the park's name?

🚩 Cross-references:
- Park A mentions Park B — do you have Park B?

🚩 Acreage claims:
- "20 acres of parkland" — does your list account for it?

------------------------------------------------------------
# 7. ENUMERATIVE + RECURSIVE DISCOVERY RULES

## 7.1 Enumerative Discovery
Enumerate:
- Park listing pages
- Trail listing pages
- Facility listing pages
- Natural area listings
- Map/brochure index pages

Extract ALL first-level entity URLs. Do not stop at the most prominent entries.

## 7.2 Recursive Discovery
Follow internal links for:
- Trails
- Maps
- Facilities
- Access
- Reservations

Respect recursion limits and allowlists.

------------------------------------------------------------
# 8. ENTITY CREATION RULES

## 8.1 Site Creation
Create a Site when:
- Municipal-owned/managed/co-managed
- Identity-bearing
- Public access exists
- Influences Access Point logic

Exclude:
- City halls
- Administrative buildings
- Cemeteries (unless natural areas)
- Maintenance yards

## 8.2 Child Site Creation
Create when:
- Named internal unit exists
- Identity-bearing
- Relevant to navigation/access

Exclude:
- Unnamed amenities
- Temporary zones
- Operational zones

## 8.3 Trail Creation
Surface when:
- Named trail appears on municipal/county pages
- Named in planning documents
- Named in meeting minutes
- Named in GIS

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `urls_raw` for all discovered map URLs.

## 8.4 Trail Segment Creation
Surface when:
- Segment geometry exists
- Segment identifiers exist

## 8.5 Trail Network Creation
Surface when:
- Municipal multi-trail system exists
- Greenway corridor spans multiple Trails

## 8.6 Site Network Creation
Surface when:
- Municipal multi-site system exists
- Conservation/greenway network documented

## 8.7 Access Point Creation
Surface when:
- Appears on municipal pages
- Appears on county-hosted municipal pages
- Appears in planning documents
- Appears in meeting minutes
- Appears in GIS

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.

------------------------------------------------------------
# 9. TIER-SPECIFIC EXPECTATIONS

Tier 6 must surface:
- All municipal Sites
- All identity-bearing child Sites
- All municipal Trails
- All municipal Trail Segments
- All municipal Access Points
- All parks/trails on county-hosted municipal pages
- All identity-bearing greenways
- All identity-bearing joint-use Sites

Tier 6 may surface:
- Trail Networks
- Site Networks
- Municipal easements
- Planned parks/trails (if identity-bearing)
- Utility lands used as parks

Tier 6 must not surface:
- HOA/private amenities
- Indoor-only facilities
- Business parks
- Non-identity-bearing parcels

------------------------------------------------------------
# 10. METADATA REQUIREMENTS

Each entity must include:

- Full **Discovery Metadata v5.x**
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships
- All geometry (if available)
- `description_raw` for Sites and Access Points (if a narrative description exists on the source page)
- `features_raw` for Sites and Access Points (if an amenity/facilities list is documented)
- `difficulty_raw` and `accessibility_raw` for Trails and Trail Segments (if explicitly stated)
- `urls_raw` for Trails, Trail Segments, Trail Networks, and Site Networks (map URLs included)

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 11. OUTPUT REQUIREMENTS

Each municipal entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- The appropriate Schema Module v5.x
- The appropriate Vocabulary Module v5.x

No normalized fields may appear in Tier 6 output.

------------------------------------------------------------
# 12. INTEGRATION POINTS

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
# 13. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.x
- Discovery Output Specification v5.x
- Discovery Metadata Specification v5.x
- All six entity Discovery Sub-Procedures v5.x
- Child Site Rules Module v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF MUNICIPAL LANDS DISCOVERY SUB-PROCEDURE v5.2
