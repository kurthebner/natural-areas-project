# NATURAL AREAS PROJECT
# TOWNSHIP LANDS DISCOVERY SUB-PROCEDURE v6.0
(Tier 5 — Ohio Townships, Township Websites, County-Hosted Township Pages, Township Recreation Assets)

This module defines the authoritative, deterministic Tier 5 discovery rules for
township-owned and township-managed natural areas within the v6.x pipeline.

This module supersedes Township Lands Discovery Sub-Procedure v5.6.

Townships in Ohio vary dramatically in capacity, documentation quality, and web presence.
Some maintain full recreation pages; others have no website at all. Township parks may be
hidden on non-indexed subpages, embedded PDFs, or county-hosted pages.

**Do not skip townships based on size or assumed population.**
Townships with no recreation department may still own or manage parks, trails, or open space.
Every township must be individually verified.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v6.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.6 → v6.0

- **Entity type references updated throughout**: Trail, Trail Segment, and Trail
  Network are unified into the single Trailthing entity type. §1 Purpose, §7 Entity
  Creation Rules, §8 Tier-Specific Expectations, and §9 Metadata Requirements
  updated accordingly. §7.3–7.5 (Trail, Trail Segment, Trail Network creation)
  consolidated into §7.3 (Trailthing Creation). §7.6 Site Network renumbered to §7.4;
  §7.7 Access Point renumbered to §7.5.

- **§7.1 Site Creation exclusion list corrected**: v5.6 §7.1 listed "Cemeteries (unless
  designated natural areas)" as excluded from site creation, which directly contradicted
  §5.6's mandatory township cemetery enumeration. In v6.0, cemeteries are removed from
  the exclusion list — they are valid Sites governed by §5.6.

- **Document Collection added** (§6.4): During Tier 5 discovery, all qualifying
  maps, PDFs, GPX/KML files, GIS exports, and other source documents must be
  downloaded and logged per Discovery Orchestration Module v6.0 §4.

- **All v5.6 rules carried forward**: IMP-099 (Township Cemeteries), IMP-029
  (Pre-Discovery Checklist), IMP-030 (Captured Source Data), IMP-005 (OTA Active
  Township Roster, defunct handling), IMP-012 (Wrong-County Website Verification).

------------------------------------------------------------
# 1. PURPOSE

The Township Lands Discovery Sub-Procedure v6.0 defines how Tier 5 must:

- Identify township-owned or township-managed Sites
- Identify township-managed child Sites
- Identify township-managed Trailthings
- Identify township-managed Site Networks (rare)
- Identify township-managed Access Points
- Identify township recreation assets even when no recreation department exists
- Identify township pages hosted by the county
- Surface uncertainty and conflicts
- Produce Raw Discovery Records v6.x
- Download and log source documents per the Document Collection System

This module is referenced only by:
- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.0

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
handoff's Pre-Discovery Checklist before beginning individual township searches.
Include the OTA website URL for each township if known (see §3.1a column reference).
A context break after list-building should not require reconstructing the enumeration
from the OTA roster.

## 3.1a OTA Active Township Roster (IMP-005)

**Source:** Ohio Township Association 2022–2023 Official Roster
**File:** `Townships_Officials2022-2023.xlsx` (project root, v5 folder)
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

All sources must be logged in discovery metadata.

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
its trustees or fiscal officer by name, cross-reference against the OTA roster
(§3.1a) for the target county. Trustee names are county-specific and are a reliable
disambiguation signal.

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

**First-Pass Capture**: When fetching a township park or recreation page, extract ALL
available fields in a single pass — including `description_raw` (the narrative paragraph
describing the site's character, ecology, or significance) and `features_raw` (the amenity
or facilities list). Both fields are typically present on the same page. A return visit
to collect fields that were available on first fetch is a process failure. See Site
Discovery Sub-Procedure v6.0 §7.3 for field definitions and the Description Quality Gate.

**Captured Source Data (IMP-030)**: When a township page contains a structured source
table (parks list with addresses, facility directory), write it verbatim to the handoff's
Captured Source Data section immediately — do not defer to staging time.

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

- **Zero entity records** — do not create any Sites, Trailthings, or Access Points
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

### Pipeline handling

A defunct township produces no YAML staging records. The session log entry is
sufficient. The township appears in the county's Tier 5 completion record as DEFUNCT
with zero entities, which is a valid completion state — not a gap.

Do **not** flag a confirmed defunct township as a data quality issue. Document it
and move on.

## 5.6 Township Cemeteries — Mandatory Enumeration (IMP-099)

Township cemeteries are one of the most common Tier 5 entity types in Ohio. Virtually
every Ohio township owns and maintains at least one cemetery, and many own several. They
are frequently omitted from discovery because they do not appear on parks pages — they
require a separate, dedicated search.

**For every township**, run the following regardless of whether the township has parks:

```
Search: "[Township Name] Township [County] Ohio cemetery
Search: "[Township Name] Township cemetery trustees Ohio
```

Also check:
- The township website's full navigation — look for a "Cemetery" or "Cemeteries"
  section (separate from Parks)
- The OTA roster trustee/fiscal officer contact info — call or email if the website
  is sparse
- **Ohio Cemetery Dispute Resolution Commission (CDRC)** listings — the state
  maintains records of registered cemeteries by county
- **Find A Grave** (findagrave.com) — search by township name and county to identify
  named cemeteries; use for confirmation and identity, not as a sole source
- **County auditor parcel layer** — filter for parcels coded as cemetery (often
  labeled "CEM" or similar)

**Classification**: `category: Cemetery`, subtype per Site Vocabulary v6.0 inference
rules. Most township-owned cemeteries will resolve to **"Public Cemetery"** unless
name evidence supports a more specific subtype.

**Status**: Active cemeteries still accepting burials → "Active". Well-maintained
historic cemeteries (no new burials but maintained) → "Active". Untended, overgrown,
or abandoned → "Abandoned".

**Multiple cemeteries per township**: Each named cemetery is a separate Site record.
Do not collapse multiple cemeteries into one record. If names are missing, use the
parcel identifier as a provisional name and flag with `IDENTITY_UNCONFIRMED`.

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
- The page is not relevant to Sites, Trailthings, or Access Points
- The page is administrative or non-recreational

## 6.3 Recursion Allowlist
- *.township.*
- *.townshipoh.gov
- *.oh.gov (township subdomains)
- *.countyoh.gov (county-hosted township pages)
- *.co.*.us (legacy township domains)
- *.facebook.com/* (only if official)

## 6.4 Document Collection

During Tier 5 discovery, download all qualifying source documents encountered —
trail maps, park brochures, PDFs — and log each in the county document log per
**Discovery Orchestration Module v6.0 §4**.

Township documentation is typically sparse. Capture what exists; do not expect the
volume seen at Tier 1–3. Particularly valuable at Tier 5:
- Township park maps or trail maps (rare but valuable when present)
- Township recreation guides
- PDF cemetery listings or cemetery maps

------------------------------------------------------------
# 7. ENTITY CREATION RULES (TIER-SPECIFIC)

## 7.1 Site Creation
Create a **Site** when:
- Township-owned or township-managed
- Identity-bearing (named, mapped, or designated)
- Public access or recreation infrastructure exists, OR
- It is a township cemetery (see §5.6)
- It influences Access Point logic

Exclude:
- Township halls
- Administrative buildings
- Maintenance yards
- Non-public parcels with no identity

## 7.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a township Site
- A recreation area, facility, or natural area is identity-bearing
- A playground, shelter area, or lake area is formally named

Do not surface:
- Amenities without identity
- Temporary zones
- Unnamed management areas

## 7.3 Trailthing Creation
Create a **Trailthing** when:
- A named trail, trail section, trail system, or trail network appears on township
  or county-hosted pages, in meeting minutes, or in township GIS

Capture `source_term_raw` verbatim (how the source describes the entity) and
`source_hierarchy_context_raw` when the source frames the entity in relation to
others. Do not classify the Trailthing as trail vs. trail network vs. trail segment
during discovery — record what the source says.

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the
source. Record `urls_raw` for all discovered map URLs.

## 7.4 Site Network Creation
Create a **Site Network** when:
- A township-managed multi-site system exists
- A conservation or greenway network is formally documented

Very rare but must be captured. Apply Site Network threshold rules per Site Network
Discovery Sub-Procedure v6.0 §3.

**If no Site Networks qualify at Tier 5:** Document an explicit null-evidence block
before advancing to Access Point creation. Township-level Site Networks are rare —
a null result is expected in most counties and is correct. But it must be documented.

```yaml
entity_type_result:
  tier: 5
  governance_level: Township
  entity_type: Site Network
  result: null
  sources_checked:
    - [URL or source description]
  reasoning: [why no Site Networks qualify — no qualifying township-managed
              multi-site system found; threshold not met, etc.]
```

At minimum, two sources must be checked before concluding null.

## 7.5 Access Point Creation
Create an **Access Point** when:
- It appears on township pages
- It appears on county-hosted township pages
- It appears in township meeting minutes
- It appears in township GIS (rare)

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.
Populate `last_verified_date` with today's date; set `field_verified: false`.

------------------------------------------------------------
# 8. TIER-SPECIFIC EXPECTATIONS

Tier 5 **must** surface:
- All township-owned or township-managed Sites (including cemeteries per §5.6)
- All identity-bearing child Sites
- All township-managed Trailthings (trails, trail sections, trail systems)
- All township-managed Access Points
- All parks, preserves, and trails listed on county-hosted township pages

Tier 5 **may** surface:
- Township-managed Site Networks
- Township-managed easements
- Planned parks and trail corridors (if identity-bearing)

------------------------------------------------------------
# 9. METADATA REQUIREMENTS

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
- ❌ Don't skip the township cemetery search — it is mandatory for every township (§5.6)

------------------------------------------------------------
# 11. OUTPUT REQUIREMENTS

Each township entity must output a Raw Discovery Record conforming to:
- The appropriate v6.0 Schema Module
- The appropriate v6.0 Vocabulary Module

No normalized fields may appear in Tier 5 output.

------------------------------------------------------------
# 12. INTEGRATION POINTS

This module integrates with:
- Discovery Orchestration Module v6.0
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- Resolution Engine v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:
- Discovery Orchestration Module v6.0 *(for document collection rules, §4)*
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- Resolution Engine v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF TOWNSHIP LANDS DISCOVERY SUB-PROCEDURE v6.0
