# NATURAL AREAS PROJECT
# TOWNSHIP LANDS DISCOVERY SUB-PROCEDURE v5.1
(Tier 5 — Ohio Townships, Township Websites, County-Hosted Township Pages, Township Recreation Assets)

This module defines the authoritative, deterministic Tier-5 discovery rules for
township-owned and township-managed natural areas within the v5.x Raw → Resolution →
Normalization → Entity Graph pipeline.

This module supersedes Township Lands Discovery Sub-Procedure v4.0.

Townships in Ohio vary dramatically in capacity, documentation quality, and web presence.
Some maintain full recreation pages; others have no website at all. Township parks may be
hidden on non-indexed subpages, embedded PDFs, or county-hosted pages.

**Do not skip townships based on size or assumed population.**
Townships with no recreation department may still own or manage parks, trails, or open space.
Every township must be individually verified.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- Updated all cross-module references to v5.x
- Updated header version to v5.1

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `role_raw` and `access_level_raw` removed from output — deleted from Access Point schema
- `features_raw` added to output for Access Point and Site amenities
- `difficulty_raw` and `accessibility_raw` added to output for Trails and Trail Segments
- `maps_raw` removed; map URLs now included in `urls_raw`
- `township_raw` and `municipality_raw` explicitly prohibited — GIS-derived only
- **Systematic individual-search requirement** added — every township must be searched individually
- **Fetch-over-search rule** added — official pages must be fetched; snippets are insufficient
- **Documentation of negative results** made explicit
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Township Lands Discovery Sub-Procedure v5.x defines how Tier 5 must:

- Identify township-owned or township-managed Sites
- Identify township-managed child Sites
- Identify township-managed Trails and Trail Segments
- Identify township-managed Trail Networks (rare)
- Identify township-managed Site Networks (rare)
- Identify township-managed Access Points
- Identify township recreation assets even when no recreation department exists
- Identify township pages hosted by the county
- Surface uncertainty and conflicts
- Produce Raw Discovery Records v5.x
- Produce Discovery Metadata v5.x

This module is referenced only by:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x

------------------------------------------------------------
# 2. SCOPE

This sub-procedure applies to:

- Township government websites
- Township recreation pages (if any)
- Township-hosted or county-hosted subpages
- Township planning documents (rare)
- Township GIS layers (rare)
- Township meeting minutes (for land acquisitions)
- Official township social media (conditional)

Tier 5 sits **below County** and **above Municipal**.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 5 must enumerate and recursively explore the following authoritative sources.

## 3.1 Complete Township List (Required First Step)

Before searching, obtain a complete list of all townships in the county.
This list is the enumeration baseline — every township on it must be searched.

Do not rely on memory or partial lists.
Missing a township from the list means missing everything in that township.

## 3.2 Township Website (If Exists)
Scan for:
- Parks
- Recreation
- Facilities
- Community
- Open Space / Green Space
- Playgrounds
- Shelters
- Picnic Areas

Township websites often contain:
- Hidden subpages
- Non-indexed pages
- PDF-only listings
- Outdated or partial information

All must be scanned. Always **fetch** the official page — do not rely on search snippets.

## 3.3 County-Hosted Township Pages
If the county hosts township pages:
- Treat them as authoritative
- Scan for parks, preserves, trails, facilities
- Log the county as the source

Discoveries remain **Tier 5** because the township is the governing entity.

## 3.4 Township Meeting Minutes
Scan for:
- Land purchases
- Park dedications
- Trail agreements
- Conservation partnerships
- Recreation facility improvements

## 3.5 Township GIS (If Exists)
Check for:
- Township-owned parcels
- Recreation layers

## 3.6 Township Social Media (Conditional)
Township social media is authoritative only if:
- Explicitly designated as official by the township, OR
- Linked from the township website, OR
- Linked from the county website

If official:
- Scan for park announcements
- Facility openings
- Trail access information

If not official → exclude.

All sources must be logged in **Discovery Metadata v5.x**.

------------------------------------------------------------
# 4. SEARCH PROTOCOL (PER TOWNSHIP)

Each township must be searched individually and completely. No exceptions.

## 4.1 Step 1: Initial Search
Search: "[Township Name] [County] Ohio parks recreation"

Do not skip based on expected results. Small townships can have parks.

## 4.2 Step 2: Official Website Discovery
Search: "[Township Name] Ohio township website"
Look for: .gov, .us, or official township domains

## 4.3 Step 3: Page Fetch (Mandatory)
If an official website or parks page is found:
- **Fetch the full page** using web_fetch
- Do not rely on search snippets
- Read the entire page content
- Extract ALL parks, trails, and facilities listed
- Check navigation menus — they may list more parks than the main content

## 4.4 Step 4: Verify Counts
If the page mentions "parks" (plural), you must find at least two.
If the page mentions acreage, the parks you find should account for it.
Mismatches indicate you may have missed something — look again.

## 4.5 Step 5: Document Results
Whether parks are found or not, document the result:

```
Township: [Name]
Status: COMPLETE
Method: [web fetch / search / no website found]
Parks Found: [N]
Evidence: [source URL or "no website found; county confirms no township parks"]
Date: [ISO date]
```

**Never document as "probably no parks" or "too small to have parks."**
Document evidence, not assumptions.

------------------------------------------------------------
# 5. DOMAIN RULES FOR TOWNSHIP DISCOVERY

## 5.1 Township-Owned vs Township-Managed
A Site may be:
- Owned by the township
- Managed by the township
- Co-managed with counties or park districts

All must be surfaced if identity-bearing.

## 5.2 No Recreation Department
Even if no recreation department exists, the township may still own:
- Parks
- Trails
- Open space
- Natural areas

These must still be surfaced if identity-bearing.

## 5.3 Common Pattern: Township Defers to Park District
In Ohio, many townships do not maintain separate park systems and instead rely on
county park districts for resident recreation services.

If a township states this explicitly:
- Record "0 township-owned parks" in discovery notes
- Include the stated evidence (e.g., "Township website states: 'Parks are provided by [County] Park District'")
- Mark the township as COMPLETE

Do not mark as zero without evidence. Evidence of zero is still evidence.

## 5.4 County-Hosted Township Pages
These are authoritative for township discovery but remain **Tier 5**.

------------------------------------------------------------
# 6. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 5 must use both enumerative and recursive discovery.

## 6.1 Enumerative Discovery (Listing Pages)
Tier 5 must enumerate:
- All township park listings
- All township recreation pages
- All township facility listings
- All township PDFs
- All county-hosted township pages

## 6.2 Recursive Discovery (URL Propagation)
Tier 5 must recursively follow:
- Internal links within township domains
- Internal links within county-hosted township pages
- Internal links within township-linked social media (if official)

Recursion must stop when:
- The domain is not on the allowlist
- The page is not relevant to Sites, Trails, or Access Points
- The page is administrative or non-recreational

## 6.3 Recursion Allowlist
- *.township.*
- *.townshipoh.gov
- *.oh.gov (township subdomains)
- *.countyoh.gov (county-hosted township pages)
- *.co.*.us (legacy township domains)
- *.facebook.com/* (only if official)

------------------------------------------------------------
# 7. ENTITY CREATION RULES (TIER-SPECIFIC)

## 7.1 Site Creation
Create a **Site** when:
- Township-owned or township-managed
- Identity-bearing (named, mapped, or designated)
- Public access or recreation infrastructure exists
- It influences Access Point logic

Exclude:
- Township halls
- Administrative buildings
- Cemeteries (unless designated natural areas)
- Maintenance yards

## 7.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a township Site
- A recreation area, facility, or natural area is identity-bearing
- A playground, shelter area, or lake area is formally named

Do not surface:
- Amenities without identity
- Temporary zones
- Unnamed management areas

## 7.3 Trail Creation
Surface a **Trail** when:
- A named trail appears on township or county-hosted pages
- A named trail appears in meeting minutes
- A named trail appears in township GIS (rare)

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `urls_raw` for all discovered map URLs.

## 7.4 Trail Segment Creation
Surface **Trail Segments** when:
- Segment-level geometry exists in township or county GIS
- Segment identifiers appear in maps or plans

## 7.5 Trail Network Creation
Surface a **Trail Network** when:
- A township-managed multi-trail system exists
- A greenway corridor spans multiple Trails

Rare but must be captured.

## 7.6 Site Network Creation
Surface a **Site Network** when:
- A township-managed multi-site system exists
- A conservation or greenway network is formally documented

Very rare but must be captured.

## 7.7 Access Point Creation
Surface an **Access Point** when:
- It appears on township pages
- It appears on county-hosted township pages
- It appears in township meeting minutes
- It appears in township GIS (rare)

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.

------------------------------------------------------------
# 8. TIER-SPECIFIC EXPECTATIONS

Tier 5 **must** surface:
- All township-owned or township-managed Sites
- All identity-bearing child Sites
- All township-managed Trails
- All township-managed Trail Segments
- All township-managed Access Points
- All parks, preserves, and trails listed on county-hosted township pages

Tier 5 **may** surface:
- Township-managed Trail Networks
- Township-managed Site Networks
- Township-managed easements
- Planned parks and trail corridors (if identity-bearing)

------------------------------------------------------------
# 9. METADATA REQUIREMENTS

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
# 10. OUTPUT REQUIREMENTS

Each township entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- The appropriate Schema Module v5.x
- The appropriate Vocabulary Module v5.x

No normalized fields may appear in Tier 5 output.

------------------------------------------------------------
# 11. INTEGRATION POINTS

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
# 12. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.x
- Discovery Output Specification v5.x
- Discovery Metadata Specification v5.x
- All six entity Discovery Sub-Procedures v5.x
- Child Site Rules Module v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF TOWNSHIP LANDS DISCOVERY SUB-PROCEDURE v5.1
