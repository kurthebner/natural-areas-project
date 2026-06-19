# NATURAL AREAS PROJECT
# TOWNSHIP LANDS DISCOVERY SUB-PROCEDURE v5.6
(Tier 5 — Ohio Townships, Township Websites, County-Hosted Township Pages, Township Recreation Assets)

This module defines the authoritative, deterministic Tier-5 discovery rules for
township-owned and township-managed natural areas within the v5.x Raw → Resolution →
Normalization → Entity Graph pipeline.

This module supersedes Township Lands Discovery Sub-Procedure v5.5.

Townships in Ohio vary dramatically in capacity, documentation quality, and web presence.
Some maintain full recreation pages; others have no website at all. Township parks may be
hidden on non-indexed subpages, embedded PDFs, or county-hosted pages.

**Do not skip townships based on size or assumed population.**
Townships with no recreation department may still own or manage parks, trails, or open space.
Every township must be individually verified.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.5 → v5.6

- **IMP-099 — Township Cemeteries — Mandatory Enumeration**: Added §5.6 defining
  mandatory discovery of all township-owned cemeteries. Includes required search queries
  (OTA roster trustee website column, Ohio CDRC, Find A Grave, county auditor parcel
  layer), classification rules (`category: Cemetery`, subtype per Site Vocabulary §7.4),
  status guidance (Active vs. Abandoned), and multiple-cemetery handling.

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- **IMP-029**: Added Pre-Discovery Checklist cross-reference to §3.1 — once the township
  list is built from the OTA roster, it must be written to the handoff's Pre-Discovery
  Checklist before beginning individual township searches. Prevents reconstructing the
  enumeration list after context breaks.
- **IMP-030**: Added Captured Source Data cross-reference to §4.3 — when a township page
  contains a structured source table (parks list with addresses, facility directory), it
  must be written verbatim to the handoff's Captured Source Data section immediately, not
  deferred to staging time.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- **Added §3.1a OTA Active Township Roster (IMP-005)**: The Ohio Township Association
  2022–2023 Official Roster (`Townships_Officials2022-2023.xlsx`) is the authoritative
  active-township cross-reference for Tier 5 discovery. §3.1 updated to require roster
  lookup before discovery begins.

- **Added §5.5 Defunct Township Handling (IMP-005)**: Protocol for identifying,
  confirming, documenting, and closing townships that have been fully dissolved or
  absorbed into municipalities. A township absent from the OTA roster is a defunct
  candidate. Confirmation procedure, zero-record handling, discovery note format, and
  COMPLETE closure rules specified.

- **Updated §10 What Not To Do**: Added defunct handling anti-patterns.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- **Added §4.2a Wrong-County Website Verification (IMP-012)**: Ohio search results for
  common township names (Sharon, Jefferson, Perry, Plain, Washington, Madison, Jackson,
  Liberty, Union, Monroe, etc.) frequently return same-named townships in other counties.
  §4.2a defines a mandatory county verification check before any township website may be
  treated as authoritative for the target county. Verification methods and failure handling
  are specified. §4.2 updated to reference §4.2a. §9 "What Not To Do" list updated.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Added `description_raw` to Metadata Requirements — must be captured when a narrative description exists on the source page; distinct from `features_raw`
- Added first-pass capture rule to §4.3 Step 3: when fetching a township park page, extract description_raw and features_raw in the same fetch — no deferred return visits
- Bumped version to v5.2

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

The Township Lands Discovery Sub-Procedure v5.3 defines how Tier 5 must:

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

The primary source for the complete township list is the OTA Active Township Roster
(see §3.1a). Supplement with the county auditor's website or county GIS if needed,
but cross-reference every township found against §3.1a before beginning discovery.

After building the township list, apply the defunct-candidate check in §5.5 before
beginning individual township searches.

**Pre-Discovery Checklist (IMP-029)**: Once the township list is built, write it to the
handoff's **Pre-Discovery Checklist** before beginning individual township searches.
Include the OTA website URL for each township if known (see §3.1a column reference).
A context break after list-building should not require reconstructing the enumeration
from the OTA roster. See na-discovery skill.

## 3.1a OTA Active Township Roster (IMP-005)

**Source:** Ohio Township Association 2022–2023 Official Roster
**File:** `Townships_Officials2022-2023.xlsx` (project root)
**Coverage:** 1,307 active townships across all 88 Ohio counties

This spreadsheet is the authoritative roster of all legally active Ohio townships as
of 2022–2023. It lists every township that has active trustees and a fiscal officer.
Dissolved or absorbed townships are not present — their absence is the signal.

**How to use it:**

1. Filter the spreadsheet to the target county (`County Name` column).
2. The filtered rows define the active township list for that county.
3. Any township that appears in county GIS, TIGER/Line MCDs, or a county baseline
   but is **absent from this roster** is a defunct candidate — apply §5.5.

**Column reference:**

| Column | Content |
|---|---|
| County Name | Ohio county name (filter on this) |
| Township Name | Township name (use for enumeration baseline) |
| 2020 Census | 2020 population (all active townships have non-zero values) |
| Website | Township website URL if known (364 of 1,307 have one) |
| Fiscal Officer / Trustees | Names for wrong-county website verification (§4.2a check 3) |

**Note on the trustee name check (§4.2a):** The OTA roster's fiscal officer and
trustee names can serve as the authoritative cross-reference for §4.2a step 3
(trustee names disambiguation), eliminating the need to look up Board of Elections
records for most cases.

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
Search: "[Township Name] [County] Ohio township website"

Always include the county name in the search. This reduces but does not eliminate
wrong-county results for common township names.

Look for: .gov, .us, or official township domains.

**Before treating any website as authoritative, apply the county verification check
in §4.2a.**

## 4.2a Wrong-County Website Verification (IMP-012)

Ohio search results for common township names frequently return same-named townships
in other counties. This is a known hazard, not an edge case. The following township
names commonly appear in multiple Ohio counties and are high-risk for wrong-county
results:

- Sharon, Jefferson, Perry, Plain, Washington, Madison, Jackson, Liberty, Union,
  Monroe, Franklin, Clinton, Harrison, Pleasant, Salem, Blendon, Delaware, Butler,
  Wayne, Lawrence, Lake, Mifflin, Green, Brown, Pike

**Any township whose name appears on this list must be verified before its website
is treated as authoritative. All other townships should also be verified — the list
above is illustrative, not exhaustive.**

### Verification procedure

After finding a candidate website, verify that it belongs to the target township
in the target county before fetching it for discovery purposes. Apply the following
checks in order, stopping at the first conclusive result:

**1. Domain check** — Does the domain name contain the county name or a
county-specific abbreviation?
- Example: `sharontownship.franklincountyohio.gov` ✅ conclusively Franklin County
- Example: `sharontownship.mediacountyohio.gov` ✅ conclusively Medina County (wrong county — discard)
- Example: `sharontownshipohio.com` ⚠️ ambiguous — proceed to next check

**2. Page header / contact address check** — Fetch the homepage and look for:
- A county name in the page header, footer, or "About" section
- A mailing address containing the county name or a city/zip known to be in the target county
- A phone number with an area code consistent with the target county's geography

If the county is named explicitly and it matches the target county → verified ✅
If the county is named and it does not match → wrong county, discard ❌
If no county is named → proceed to next check

**3. Trustee names / elected officials check** — If the township website lists
its trustees or fiscal officer by name, cross-reference against the target county's
Board of Elections records or the county auditor's website. Trustee names are
county-specific and are a reliable disambiguation signal.

**4. Geographic content check** — If the website mentions specific roads, parks,
neighborhoods, or neighboring jurisdictions, verify that those places are in the
target county.

### Failure handling

If all four checks are inconclusive and county identity cannot be confirmed:

- Do **not** treat the website as authoritative for the target county
- Record in discovery metadata: `"Township website found but county identity
  unverified — skipped; source: [URL]"`
- Continue to §4.3 using the county-hosted township page or other authoritative
  sources
- Do **not** mark the township COMPLETE based on an unverified website

### Recording verified vs. unverified sources

- Verified website: record as authoritative; proceed with full fetch (§4.3)
- Wrong-county website: record in discovery metadata as discarded; note the actual
  county if identifiable; do not extract any data from it
- Unverified website: record as skipped per §4.2a; do not extract data

Wrong-county data extracted from an unverified website and staged as a discovery
record is a data integrity failure. Verification is mandatory, not optional.

## 4.3 Step 3: Page Fetch (Mandatory)
If an official website or parks page is found **and verified per §4.2a**:
- **Fetch the full page** using web_fetch
- Do not rely on search snippets
- Read the entire page content
- Extract ALL parks, trails, and facilities listed
- Check navigation menus — they may list more parks than the main content

**First-Pass Capture**: When fetching a township park or recreation page, extract ALL available fields in a single pass — including `description_raw` (the narrative paragraph describing the site's character, ecology, or significance) and `features_raw` (the amenity or facilities list). Both fields are typically present on the same page. A return visit to collect fields that were available on first fetch is a process failure. See `na_site_discovery_subproc.md` §7.3 for field definitions, source guidance, and the Description Quality Gate (IMP-032).

**Captured Source Data (IMP-030)**: When a township page contains a structured source table (parks list with addresses, facility directory), write it verbatim to the handoff's **Captured Source Data** section immediately — do not defer to staging time. See na-discovery skill.

## 4.4 Step 4: Verify Counts
If the page mentions "parks" (plural), you must find at least two.
If the page mentions acreage, the parks you find should account for it.
Mismatches indicate you may have missed something — look again.

## 4.5 Step 5: Document Results
Whether parks are found or not, document the result:

```
Township: [Name]
Status: COMPLETE
Method: [web fetch / search / no website found / website found but unverified per §4.2a]
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

## 5.5 Defunct Township Handling (IMP-005)

A **defunct township** is an Ohio township that has been fully dissolved by law or
completely absorbed into a municipality and no longer has a functioning government.
Defunct townships produce zero entity records. They must still be explicitly
documented and closed in the session log.

### Identification

A township is a **defunct candidate** if it appears in any of the following sources
but is **absent from the OTA Active Township Roster** (§3.1a):

- County bootstrap baseline
- County GIS or TIGER/Line MCD boundaries
- County auditor's parcel layer
- Historical records or prior discovery sessions

**Presence in the OTA roster = active. Absence = defunct candidate requiring
confirmation.** Do not mark a township defunct based on absence alone — confirm
before closing.

### Confirmation procedure

Apply these checks in order to confirm defunct status:

**1. Ohio Secretary of State records** — Search the SOS website for the township
name and county. A dissolved township typically has no active government entity
registration.

**2. County auditor or county engineer records** — The county auditor's website may
reference absorption into a municipality, a dissolution date, or simply list the
township as inactive.

**3. County GIS / TIGER note** — If a TIGER/Line MCD boundary exists but shows the
full geographic area overlapping with an incorporated city or village, dissolution
into that municipality is the likely explanation.

**4. Ohio Revised Code context** — Township dissolution in Ohio occurs under ORC
Chapter 504 (limited home rule) and ORC §§ 503.01–503.99 (merger/consolidation).
A dissolved township's territory is absorbed into the incorporating municipality.

If confirmation is inconclusive after these four checks, do **not** mark defunct.
Instead, flag the township as `PENDING — DEFUNCT CANDIDATE` in the session log and
note what was checked. This prevents premature closure of a township that may simply
have a sparse web presence.

### What to record

When a township is confirmed defunct:

- **Zero entity records** — do not create any Sites, Trails, or Access Points
- **Discovery note** documenting the historical context:

```
Township: [Name]
Status: COMPLETE
Outcome: DEFUNCT
Method: OTA roster cross-reference + [confirmation source]
Entity records produced: 0
Notes: [Township Name] Township was dissolved/absorbed into [Municipality] on
  approximately [date if known]. No active township government exists. Territory
  is now governed by [Municipality]. OTA 2022-2023 roster confirms absence.
Date: [ISO date]
```

- **Status vocabulary value:** `status = "Defunct"` (Vocabulary Module v5.2 §5)

### Pipeline handling

A defunct township produces no YAML staging records. The session log entry is
sufficient. The township appears in the county's Tier 5 completion record as DEFUNCT
with zero entities, which is a valid completion state — not a gap.

Do **not** flag a defunct township as a data quality issue. Document it and move on.

## 5.6 Township Cemeteries — Mandatory Enumeration (IMP-099)

Township cemeteries are one of the most common Tier 5 entity types in Ohio. Virtually every Ohio township owns and maintains at least one cemetery, and many own several. They are frequently omitted from discovery because they do not appear on parks pages — they require a separate, dedicated search.

**For every township**, run the following regardless of whether the township has parks:

```
Search: "[Township Name] Township [County] Ohio cemetery
Search: "[Township Name] Township cemetery trustees Ohio
```

Also check:
- The township website's full navigation — look for a "Cemetery" or "Cemeteries" section (separate from Parks)
- The OTA roster trustee/fiscal officer contact info — call or email if the website is sparse
- **Ohio Cemetery Dispute Resolution Commission (CDRC)** listings — the state maintains records of registered cemeteries by county
- **Find A Grave** ([findagrave.com](https://www.findagrave.com)) — search by township name and county to identify named cemeteries; use for confirmation and identity, not as a sole source
- **County auditor parcel layer** — filter for parcels coded as cemetery (often labeled "CEM" or similar)

**Classification**: `category: Cemetery`, subtype per Site Vocabulary v5.6 §7.4 inference rules. Most township-owned cemeteries will resolve to **"Public Cemetery"** unless name evidence supports a more specific subtype.

**Status**: Active cemeteries still accepting burials → "Active". Well-maintained historic cemeteries (no new burials but maintained) → "Active". Untended, overgrown, or abandoned → "Abandoned".

**Multiple cemeteries per township**: Each named cemetery is a separate Site record. Do not collapse multiple cemeteries into one record. If names are missing, use the parcel identifier as a provisional name and flag with `IDENTITY_UNCONFIRMED`.

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
- `description_raw` for Sites and Access Points (if a narrative description exists on the source page)
- `features_raw` for Sites and Access Points (if an amenity/facilities list is documented)
- `difficulty_raw` and `accessibility_raw` for Trails and Trail Segments (if explicitly stated)
- `urls_raw` for Trails, Trail Segments, Trail Networks, and Site Networks (map URLs included)

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 10. WHAT NOT TO DO (CRITICAL)

- ❌ Don't treat a township website as authoritative without county verification (§4.2a)
- ❌ Don't rely on search snippets — always fetch the official page
- ❌ Don't skip townships based on size or assumed population
- ❌ Don't mark a township COMPLETE based on an unverified website
- ❌ Don't extract data from a wrong-county or unverified township website
- ❌ Don't record `township_raw` or `municipality_raw` — GIS-derived only
- ❌ Don't document results as assumptions ("probably no parks")
- ❌ Don't defer field capture — extract description_raw and features_raw in the first fetch
- ❌ Don't mark a township defunct based solely on OTA roster absence — confirm first (§5.5)
- ❌ Don't flag a confirmed defunct township as a data quality issue — it is a valid COMPLETE state
- ❌ Don't skip the OTA roster cross-reference before beginning Tier 5 discovery

------------------------------------------------------------
# 11. OUTPUT REQUIREMENTS

Each township entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- The appropriate Schema Module v5.x
- The appropriate Vocabulary Module v5.x

No normalized fields may appear in Tier 5 output.

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
# END OF TOWNSHIP LANDS DISCOVERY SUB-PROCEDURE v5.5
