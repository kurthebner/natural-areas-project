# NATURAL AREAS PROJECT
# MUNICIPAL LANDS DISCOVERY SUB-PROCEDURE v5.8
(Tier 6 — Cities, Villages, Incorporated Municipalities, County-Hosted Municipal Pages, and Municipal Partner Assets)

This module defines the authoritative, deterministic Tier-6 discovery rules for
municipal lands within the v5.x Raw → Resolution → Normalization → Entity Graph pipeline.

This module supersedes Municipal Lands Discovery Sub-Procedure v5.7.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

**This tier has the highest risk of missed entities.**
Municipal discovery requires exhaustive individual-municipality searching.
Small villages must not be skipped or assumed empty based on population.
A village of 500 people can have three parks totaling 20+ acres.

------------------------------------------------------------
# CHANGES FROM v5.7 → v5.8

- Added **features staging prohibition** to §4.3 Step 3 (IMP-027): During discovery,
  write only to `features_raw` — never to `features`. Placeholder text is prohibited
  in `features_raw`. If the source provides no amenity list, leave `features_raw` blank.
- Added **§5.12 MORPC Import Field Mapping** (IMP-028): Defines the correct field
  mapping when importing from the MORPC Parks & Open Space layer or any GIS source
  that provides both managing organization and park type metadata. GIS park type must
  go to `category_raw`, never to `governance_raw`.

------------------------------------------------------------
# CHANGES FROM v5.6 → v5.7

- Added §4.3b JS-Rendered / FacetWP Paginated Listing Pages (IMP-013): When a
  parks listing page uses JavaScript rendering or lazy pagination (FacetWP, infinite
  scroll, etc.), all pages must be iterated before the listing is treated as complete.
  Recognition criteria, iteration procedure, and discovery metadata documentation
  requirements specified.
- Updated §4.4 Map Verification with multi-municipality ordering rule (IMP-015):
  In counties with multiple adjacent municipalities, complete all municipal web
  discovery for all municipalities before running map verification. Map verification
  runs as a single consolidated pass after all web discovery is complete, not
  per-municipality as web discovery proceeds.

------------------------------------------------------------
# CHANGES FROM v5.5 → v5.6

- Added §4.3a CivicPlus Empty Category Page Protocol (IMP-017): When a CivicPlus
  CMS category page (pocket parks, open spaces, etc.) loads blank due to JS rendering
  failure, three ordered fallbacks are required before flagging PENDING — Facilities
  page filter, Document Center PDFs, city ArcGIS parks layer. A municipality with
  unresolved blank CivicPlus pages must not be marked complete.

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- Added cross-tier trail handling (IMP-011):
  - §5.6 Multi-Municipal Sites & Trails expanded with cross-tier trail rule —
    when a trail is primarily managed by a non-municipal tier (Tier 2–5), Tier 6
    must still stage a discovery record; `identity_notes_raw` must flag the
    managing tier; Resolution handles canonicalization.
  - §8.3 Trail Creation expanded with cross-tier trail note and flagging requirement.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- Added §5.11 Columbus Recreation & Parks (CRP) Naming Convention — documenting the systematic
  "Parkland" vs. "Park" suffix discrepancy between CRP source data and regional GPS sources
  (MORPC, county GIS). Discovery must capture `name_raw` exactly as listed on the CRP website;
  normalization handles the suffix conversion (see Site Normalization Contract v5.4 §5.1).
  CRP URL slug patterns documented as a known matching hazard.

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

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (ALL MANDATORY)

## 3.1 Municipal Website (If Exists)
Always fetch; never rely on search snippet alone.

Required checks:
- Parks/Recreation page
- Facilities listing
- Trails and paths
- Nature areas
- Open space
- Meeting minutes (for planned or recently acquired parks)
- Capital improvement plans (for future parks)
- GIS or mapping tools

## 3.2 County-Hosted Municipal Pages
Some municipalities have no independent website; their official pages are hosted by the county.

Always check:
- County GIS portal for municipal parks layers
- County Auditor for parcel ownership by municipality name
- County planning documents referencing municipal parks

## 3.3 Municipal Recreation Departments
Some municipalities have semi-autonomous parks boards or recreation commissions with
separate websites. Always check BOTH:

- City government site (e.g., cityofX.gov/parks)
- Parks board site (e.g., Xparks.org or Xrecreation.org)

Never assume both sites contain the same information.

## 3.4 Municipal Planning Documents
Search:
- Comprehensive plans
- Greenspace/open space plans
- Trails master plans
- Capital improvement plans

These often contain parks and trails not yet on the city website.

## 3.5 Municipal Meeting Minutes
Search for parks mentioned in:
- Parks & Recreation committee minutes
- City council minutes
- Planning commission minutes

## 3.6 Municipal GIS (If Exists)
Check for:
- Parks layers
- Trails layers
- Open space layers
- Future parks or planned trails

**Governance contamination rule**: GIS layers frequently tag parks with administrative
classifications (e.g., "Community Park," "Neighborhood Park"). Record these in
`category_raw` or `identity_notes_raw`, never in `governance_raw`.

## 3.7 Municipal Social Media (Conditional)
Include only if:
- Official government account (not resident account)
- Contains identity-bearing parks or trail names not found elsewhere

## 3.8 Partner & Joint-Use Sources (Conditional)
Check when:
- Municipality references a joint-use agreement
- Municipality references a shared trail system
- Municipality references parks maintained by another entity

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
- **STAGING FIELD PROHIBITION (IMP-027)**: Write only to `features_raw` — never to `features`. The normalized `features` field is populated exclusively by the Normalization Engine. Writing to `features` directly bypasses normalization and will produce schema violations. Additionally, placeholder text (e.g., "GIS-documented; amenities require individual verification") is prohibited in `features_raw` — leave it blank instead, and note the gap in `identity_notes_raw`.

**Organizational fields** (ownership/governance if stated):
- `governance_raw` — managing organization name ONLY. Never include GIS park type labels here (see contamination rule below)

**Additional fields** (when present):
- `acres_raw`, `gps_lat_raw`, `gps_lon_raw`, `urls_raw` (all URLs including PDFs and maps)

**Governance Contamination Rule**: Municipal GIS layers frequently tag parks with administrative classifications (e.g., "Community Park," "Neighborhood Park," "Mini Park"). These are NOT governance — they are category hints. If a GIS source provides both a managing organization and a park type label:
- `governance_raw`: `City of Dublin` ✓
- `governance_raw`: `City of Dublin; GIS park type: Community Park` ✗

Record GIS park type labels in `category_raw` or `identity_notes_raw`, never in `governance_raw`.

**A return visit to a park page you already fetched to collect fields that were available on first visit is a process failure.** One fetch → all fields.

## 4.3a CivicPlus Empty Category Page Protocol (IMP-017)

CivicPlus is a widely-used municipal CMS. Some CivicPlus sites render category pages
(pocket parks, open spaces, neighborhood parks) as blank headings — a JavaScript
rendering failure that causes the page to load with a category title and no content.
This is not evidence that the category is empty. It is a rendering failure.

**How to recognize a blank CivicPlus category page:**

- The page title or breadcrumb contains a category name (e.g., "Pocket Parks",
  "Open Spaces", "Neighborhood Parks")
- The page body contains no park entries — only a heading or navigation element
- The URL follows a CivicPlus pattern such as `/facilities/`, `/parks/`,
  `/departments/parks-and-recreation/`, or similar
- The domain uses a known CivicPlus subdomain pattern (e.g., `*civicplus.com`,
  or a city domain with CivicPlus CMS structure)

**When a CivicPlus category page loads blank, apply the following fallbacks in order:**

**Fallback 1 — Facilities page filter**

Navigate to the municipality's Facilities listing page (usually at `/facilities/`)
and use the category filter to select the relevant category (e.g., "Parks",
"Open Spaces", "Pocket Parks"). CivicPlus Facilities pages often render correctly
even when category sub-pages fail.

If park records appear → extract all and proceed normally.
If the Facilities page is also blank → proceed to Fallback 2.

**Fallback 2 — Document Center PDFs**

Navigate to the municipality's CivicPlus Document Center (usually at
`/document-center/` or `/departments/parks/documents/`). Search for:
- Park brochures, trail maps, or facility guides
- Park master plans or recreational assessments
- Parks and recreation department annual reports

These documents frequently list parks by category that the CMS fails to render.
Extract any park records found in documents.

If no relevant documents exist → proceed to Fallback 3.

**Fallback 3 — City ArcGIS parks layer**

Search for the municipality's ArcGIS parks or open space layer:
```
Search: "[Municipality Name] Ohio ArcGIS parks open space"
Search: "[Municipality Name] Ohio GIS parks layer"
```

Many CivicPlus municipalities also publish their parks data via ArcGIS Online or
an ArcGIS Hub. The GIS layer is authoritative for park existence and boundaries
even when the CMS fails to render the parks page.

If a parks GIS layer exists → extract all park records as Tier 6 discovery records.

**If all three fallbacks fail:**

- Record the municipality status as `PENDING — CivicPlus category page blank;
  fallbacks exhausted; manual verification required`
- Do **not** mark the municipality COMPLETE
- Do **not** record zero parks based solely on a blank CivicPlus page
- Flag for follow-up in the next session with browser access
- Document all three fallback attempts in discovery metadata

**A municipality with unresolved blank CivicPlus pages must not be marked complete.**

## 4.3b JS-Rendered / FacetWP Paginated Listing Pages (IMP-013)

Some municipal parks listing pages use JavaScript rendering or lazy pagination
(FacetWP, infinite scroll, numbered page controls, and similar frameworks). Standard
WebFetch retrieves only the first page of results. Treating that first page as the
complete listing is a discovery failure when pagination is present.

**How to recognize a JS-paginated listing page:**

- The page shows a subset of parks with a count indicator (e.g., "Showing 1–12 of 47
  parks") and a "Load More", "Next Page", or numbered page control
- FacetWP pages typically show a page count in the filter/facet bar and may display
  a spinner or "loading" state when additional results are requested
- The page URL does not change between page loads — additional results are rendered
  in place by JavaScript
- Infinite scroll pages load additional results as you scroll toward the bottom

**When a JS-paginated listing page is detected:**

1. **Use browser JS to iterate all pages.** Click "Load More" or page controls
   programmatically, or trigger the underlying FacetWP API call for each page,
   until all results are visible.
2. **Verify the final record count.** If the page states a total (e.g., "47 parks"),
   confirm that the number of extracted records matches the stated total. A mismatch
   indicates pages were missed.
3. **Document the method in discovery metadata.** Record the pagination type and
   iteration method used, e.g.:
   - `"FacetWP — 4 pages iterated via browser JS click-through"`
   - `"Infinite scroll — scrolled to bottom 6 times until no new results loaded"`
   - `"Load More button — clicked 3 times to reveal all 47 parks"`

**Do NOT:**
- Treat the first-page result as complete when pagination indicators are visible
- Assume that only the most prominently featured parks are the complete listing
- Skip this step because the first page appears to contain the "main" parks

If browser JS is unavailable and pagination cannot be iterated, flag the municipality
as `PENDING — JS-paginated listing; full iteration requires browser access` and return
in a follow-up session. Do not mark the municipality complete.

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

**Multi-municipality ordering rule (IMP-015)**: In counties with multiple adjacent
municipalities, do **not** run map verification per municipality as web discovery
proceeds. Instead:

1. Complete Steps 2, 3, 4.3a, and 4.3b for **all** municipalities in the county first.
2. Then run map verification as a **single consolidated pass** across all jurisdictions.

Running map verification per municipality risks false positives — parks in adjacent
un-cataloged jurisdictions appear on the map during verification of a specific
municipality and may be incorrectly attributed to the wrong jurisdiction. The
consolidated pass is performed after all web discovery is complete, so the full
picture of what has already been cataloged is available, making attributions accurate.

This ordering rule applies only to counties with two or more adjacent municipalities.
Single-municipality counties and isolated municipalities may be verified individually.

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

The absence of a recreation department does not mean the absence of parks.

## 5.5 County-Hosted Municipal Pages
Authoritative but remain Tier 6.

## 5.6 Multi-Municipal Sites & Trails
Do not segment. Record all municipalities and counties.

**Cross-tier trails**: When a named trail is documented on municipal sources but is
primarily managed by a non-municipal entity (e.g., a metro park district at Tier 3,
an ODNR trail at Tier 2, or a county trail at Tier 4), stage a Tier 6 record for the
trail regardless. Add to `identity_notes_raw`:
`"Cross-tier trail — primary manager is [tier name / entity name]; Tier 6 documents this trail"`

Do not suppress the Tier 6 record on the assumption that the managing tier will cover it.
Resolution merges cross-tier records and assigns canonical status to the managing tier.
See Discovery Protocol v5.5 §18 and §8.3 below.

## 5.7 HOA Parks, Private Amenities, Gated Facilities
Exclude unless municipality is explicitly owner/manager.

## 5.8 Business Parks, Corporate Campuses, Plazas
Exclude unless formally designated as municipal parks.

## 5.9 Indoor-Only Facilities
Exclude unless part of a larger identity-bearing Site.

## 5.10 Brownfields, Redevelopment Areas, Future Parks
Include only if identity-bearing and formally designated.

## 5.11 Columbus Recreation & Parks (CRP) Naming Convention ✨ NEW IN v5.4

Columbus Recreation & Parks (columbusrecparks.com) systematically names parcel-level land
holdings with a "Parkland" suffix (e.g., "Amberfield Parkland", "Gender Road Parkland",
"Dysart Run and East Broad Parkland"). Regional sources — MORPC Parks & Open Space layer,
Franklin County GIS, and most other external references — use the "Park" suffix for the
same entities (e.g., "Amberfield Park").

**Discovery rule**: Capture `name_raw` exactly as listed on the CRP source page. Do not
normalize the suffix during discovery. The Site Normalization Contract v5.4 §5.1 handles
"Parkland" → "Park" conversion at normalization time.

**GPS matching hazard**: The Parkland/Park discrepancy causes score degradation during GPS
name-matching at Stage 3. The pipeline's name normalization function must apply the suffix
conversion before scoring. Sites scoring in the 85–92 range that end in "Parkland" should
be manually reviewed for this cause before being marked unmatched.

**CRP URL slug patterns**: CRP URL slugs do not always match the park name. Known divergence
patterns documented in IMP-041:
- Abbreviations: "Ave" in name → "ave" in slug (e.g., "brentnell-ave-parkland")
- Abbreviations: "East" in name → "e" in slug (e.g., "dysart-run-and-e-broad-parkland")
- Apostrophe handling: "Frank's" → "franks", "Hayden's" → "haydens"
- Typos in slug: "Crescent" → "cresent" (CRP site error)

Any CRP park that returns a 404 during batch scraping requires manual URL verification
before being recorded as having no web presence.

## 5.12 MORPC Import Field Mapping ✨ NEW IN v5.8 (IMP-028)

The MORPC Parks & Open Space layer (and similar regional GIS layers) provides both
a managing organization name and a park type classification for each feature. These
two metadata items must be written to separate fields — they must never be combined
into `governance_raw`.

**Correct field mapping for MORPC (and equivalent GIS layer) imports:**

| GIS attribute | Staging field | Example value |
|---|---|---|
| Managing organization | `governance_raw` | `City of Dublin` |
| GIS park type label | `category_raw` | `Community Park` |
| Import provenance | `identity_notes_raw` | `Source: MORPC Parks layer` |

**Prohibited pattern:**
```
governance_raw: "City of Dublin; GIS park type: Community Park"  ✗
```

**Required pattern:**
```
governance_raw: "City of Dublin"  ✓
category_raw: "Community Park"    ✓
```

GIS park type labels (Community Park, Neighborhood Park, Mini Park, Open Space, etc.)
are administrative classification hints, not governance identifiers. The Normalization
Engine uses `category_raw` to derive the `category` field. If `governance_raw` contains
a GIS park type label, the normalization step will attempt to parse it as an organization
name, which will fail or produce corrupt output.

This rule applies to all batch import scripts (MORPC, county auditor GIS, municipal GIS
layers, ArcGIS feature exports). Any import script must map GIS park type to `category_raw`
and managing organization to `governance_raw` as separate write operations.

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
- GIS data layers
- Planning document park lists

## 7.2 Recursive Discovery
Follow:
- Internal links within official municipal domains
- Links to partner agency pages where municipality is explicitly referenced as owner/manager

Stop when:
- Domain is not on allowlist
- Page is administrative or non-recreational
- Page is clearly another jurisdiction's content

------------------------------------------------------------
# 8. ENTITY CREATION RULES

## 8.1 Site Creation
Surface when:
- Municipal-owned or municipal-managed
- Identity-bearing (named, mapped, or designated)
- Public access or recreation infrastructure present

Exclude:
- Administrative buildings
- Maintenance yards
- Non-public parcels with no identity
- Pure infrastructure (pump stations, utility easements)

## 8.2 Child Site Creation
Surface when:
- Named internal unit within a municipal Site
- Meets Child Site Rules Module v5.x

## 8.3 Trail Creation
Surface when:
- Named trail appears on municipal/county pages
- Named in planning documents
- Named in meeting minutes
- Named in GIS

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `urls_raw` for all discovered map URLs.

**Cross-tier trails**: When a named trail appearing on municipal sources is primarily
managed by a non-municipal entity (Tier 2–5), Tier 6 must still stage a discovery record.

- Record `governance_raw` exactly as stated on the municipal source. If the municipal
  page identifies the actual managing entity (e.g., "Maintained by Metro Parks"), record
  that value — not "City of X."
- Add to `identity_notes_raw`: `"Cross-tier trail — primary manager is [entity name / Tier N]; Tier 6 documentation"`
- Do not defer to the managing tier or suppress the Tier 6 record.
- Resolution Engine v5.5 §11.8 merges cross-tier trail records and assigns canonical status
  to the management tier's record.

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
# END OF MUNICIPAL LANDS DISCOVERY SUB-PROCEDURE v5.5
