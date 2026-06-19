# NATURAL AREAS PROJECT
# MUNICIPAL LANDS DISCOVERY SUB-PROCEDURE v6.0
(Tier 6 — Cities, Villages, Incorporated Municipalities, County-Hosted Municipal Pages, and Municipal Partner Assets)

This module defines the authoritative, deterministic Tier 6 discovery rules for
municipal lands within the v6.x pipeline.

This module supersedes Municipal Lands Discovery Sub-Procedure v5.12.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v6.x Vocabulary Modules.

**This tier has the highest risk of missed entities.**
Municipal discovery requires exhaustive individual-municipality searching.
Small villages must not be skipped or assumed empty based on population.
A village of 500 people can have three parks totaling 20+ acres.

------------------------------------------------------------
# CHANGES FROM v5.12 → v6.0

- **Entity type references updated throughout**: Trail, Trail Segment, and Trail
  Network are unified into the single Trailthing entity type. §1 Purpose, §8 Entity
  Creation Rules, §9 Tier-Specific Expectations, and §10 Metadata Requirements
  updated accordingly. §8.3–8.5 (Trail, Trail Segment, Trail Network creation)
  consolidated into §8.3 (Trailthing Creation). §8.6 Site Network renumbered to §8.4;
  §8.7 Access Point renumbered to §8.5.

- **Document Collection added** (§7.3): During Tier 6 discovery, all qualifying
  maps, PDFs, GPX/KML files, GIS exports, and other source documents must be
  downloaded and logged per Discovery Orchestration Module v6.0 §4.

- **All v5.12 rules carried forward**: IMP-099 (Municipal Cemeteries and Golf Courses),
  IMP-032 (Description Quality Gate), IMP-029 (Pre-Discovery Checklist), IMP-030
  (Captured Source Data), IMP-031 (GPS capture during map verification), IMP-001
  (Large Municipality Batching), IMP-027 (Features staging prohibition), IMP-028
  (MORPC Import Field Mapping), IMP-013 (JS-Rendered Paginated Listing Pages),
  IMP-015 (Multi-municipality map verification ordering), IMP-017 (CivicPlus Empty
  Category Page Protocol), IMP-011 (Cross-tier trail handling).

------------------------------------------------------------
# 1. PURPOSE

The Municipal Lands Discovery Sub-Procedure v6.0 defines how Tier 6 must:

- Identify all municipal-owned or municipal-managed Sites
- Identify child Sites within municipal Sites
- Identify Trailthings managed or branded by municipalities
- Identify Site Networks (e.g., municipal greenway systems)
- Identify Access Points associated with municipal Sites and Trailthings
- Distinguish municipal management from county, township, district, state, federal, or private co-management
- Handle multi-department governance
- Handle county-hosted municipal pages and official social media
- Handle joint-use facilities
- Avoid false positives from similarly named places
- Log uncertainty, conflicts, and boundary cases
- Produce Raw Discovery Records v6.x
- Download and log source documents per the Document Collection System

This module is referenced only by:
- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.0

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

**Write this list to the handoff document's Pre-Discovery Checklist section before
beginning any individual municipality searches (IMP-029).** The pre-discovery
checklist is a durable record that survives context breaks — if the session ends
mid-tier, the next session resumes directly from the checklist rather than
reconstructing the municipality list from scratch.

Do not begin individual searches until the full list exists and is written to the handoff.

## 4.2 Step 2: Individual Search (Each Municipality)

For EACH municipality, run:
```
Search: "[Municipality Name] Ohio parks recreation"
Search: "[Municipality Name] Ohio official website"
```

Then fetch any official website or parks/recreation page discovered.

**Cemeteries and golf courses — additional mandatory searches (IMP-099)**: Municipal
cemeteries and municipal golf courses are frequently not listed on parks pages. Run
these searches separately for every municipality:

```
Search: "[Municipality Name] Ohio municipal cemetery
Search: "[Municipality Name] Ohio city cemetery
Search: "[Municipality Name] Ohio golf course municipal
```

Also check the municipal website navigation directly for a "Cemetery" or "Golf Course"
section — these are often in a separate department from Parks & Recreation (e.g., under
Public Works or City Services). Municipal cemeteries → `category: Cemetery`, subtype
"Public Cemetery" unless name evidence indicates otherwise. Municipal golf courses →
`category: Recreation Facility`, `subtype: Golf Course`.

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

### First-Pass Capture — Extract All Available Fields in a Single Fetch

When fetching an individual park page, extract ALL available fields in one pass.
Municipal park pages typically contain most or all of the following in a single page
load — do not defer any field to a return visit:

**Identifying fields** (always present):
- `name_raw` — the park's official name as listed
- `category_raw` — type label if stated ("neighborhood park," "nature preserve," etc.)
- `location_raw` — address or geographic description

**Narrative description** (usually the introductory paragraph or "About" section):
- `description_raw` — capture the narrative paragraph(s) verbatim; this is the prose
  that describes the park's character, ecology, history, or community significance.
  It is different from an amenity list.
- If no narrative paragraph exists on the page, leave blank — do not invent
- **DESCRIPTION QUALITY GATE (IMP-032)**: Before staging, apply the stripping test —
  remove the park name, location, governance, category, and acreage from the text.
  If nothing substantive remains, the source description has zero information value;
  leave `description_raw` blank. "X Park is a neighborhood park in [City], Ohio."
  is a blank. See Site Discovery Sub-Procedure v6.0 §7.3 for the full quality gate
  and examples table.

**Amenity/features list** (usually icons, bullets, or a "Facilities" section):
- `features_raw` — capture the amenity list verbatim as comma-separated items:
  "Picnic shelter, restrooms, playground, fishing pond." These are NOT sentences;
  they are list items.
- If no amenity list is present on the page, leave blank — do not infer
- **STAGING FIELD PROHIBITION (IMP-027)**: Write only to `features_raw` — never to
  `features`. The normalized `features` field is populated exclusively by the
  Normalization Engine. Additionally, placeholder text is prohibited in `features_raw`
  — leave it blank instead, and note the gap in `identity_notes_raw`.

**Organizational fields** (ownership/governance if stated):
- `governance_raw` — managing organization name ONLY. Never include GIS park type
  labels here.

**Additional fields** (when present):
- `acres_raw`, `gps_lat_raw`, `gps_lon_raw`, `urls_raw` (all URLs including PDFs and maps)

**Governance Contamination Rule**: Municipal GIS layers frequently tag parks with
administrative classifications (e.g., "Community Park," "Neighborhood Park,"
"Mini Park"). These are NOT governance — they are category hints.
- `governance_raw`: `City of Dublin` ✓
- `governance_raw`: `City of Dublin; GIS park type: Community Park` ✗

Record GIS park type labels in `category_raw` or `identity_notes_raw`, never in
`governance_raw`.

**A return visit to a park page you already fetched to collect fields that were
available on first visit is a process failure.** One fetch → all fields.

### Source Table Capture — Write to Handoff Immediately (IMP-030)

When a source page contains a **structured table of parks with names and addresses**
(e.g., a city Adopt-a-Park page, a parks department facilities table, a recreation
master plan appendix), that table must be written verbatim to the handoff document's
**Captured Source Data** section at the time of fetching — not only to the staging YAML.

**Why this matters**: Chat context does not survive session boundaries. If the session
ends between discovery and staging, all address data from the source page is lost
and must be re-fetched. Writing the table to the handoff eliminates that re-fetch.

**Minimum format** (adapt as needed):
```
Source: [URL] (fetched YYYY-MM-DD)
| Park Name | Address | GPS Lat | GPS Lon |
|-----------|---------|---------|---------|
| Park A    | 123 Main St | — | — |
| Park B    | Oak and 5th  | — | — |
```

A source table fetch without a corresponding handoff entry is a process failure
equivalent to failing to stage the records.

## 4.3a CivicPlus Empty Category Page Protocol (IMP-017)

CivicPlus is a widely-used municipal CMS. Some CivicPlus sites render category pages
(pocket parks, open spaces, neighborhood parks) as blank headings — a JavaScript
rendering failure. This is not evidence that the category is empty.

**When a CivicPlus category page loads blank, apply the following fallbacks in order:**

**Fallback 1 — Facilities page filter**

Navigate to the municipality's Facilities listing page (usually at `/facilities/`)
and use the category filter to select the relevant category. CivicPlus Facilities
pages often render correctly even when category sub-pages fail.

If park records appear → extract all and proceed normally.
If the Facilities page is also blank → proceed to Fallback 2.

**Fallback 2 — Document Center PDFs**

Navigate to the municipality's CivicPlus Document Center. Search for park brochures,
trail maps, facility guides, master plans, or annual reports. These frequently list
parks by category that the CMS fails to render. Download qualifying documents per §7.3.

If no relevant documents exist → proceed to Fallback 3.

**Fallback 3 — City ArcGIS parks layer**

Search:
```
Search: "[Municipality Name] Ohio ArcGIS parks open space"
Search: "[Municipality Name] Ohio GIS parks layer"
```

If a parks GIS layer exists → extract all park records as Tier 6 discovery records.

**If all three fallbacks fail:**

- Record the municipality status as `PENDING — CivicPlus category page blank;
  fallbacks exhausted; manual verification required`
- Do **not** mark the municipality COMPLETE
- Do **not** record zero parks based solely on a blank CivicPlus page

**A municipality with unresolved blank CivicPlus pages must not be marked complete.**

## 4.3b JS-Rendered / FacetWP Paginated Listing Pages (IMP-013)

Some municipal parks listing pages use JavaScript rendering or lazy pagination.
Standard WebFetch retrieves only the first page of results.

**When a JS-paginated listing page is detected:**

1. Use browser JS to iterate all pages until all results are visible.
2. Verify the final record count matches any stated total.
3. Document the method in discovery metadata (e.g., `"FacetWP — 4 pages iterated
   via browser JS click-through"`).

**Do NOT** treat the first-page result as complete when pagination indicators are visible.

If browser JS is unavailable and pagination cannot be iterated, flag the municipality
as `PENDING — JS-paginated listing; full iteration requires browser access` and do not
mark it complete.

## 4.4 Step 4: Map Verification (Mandatory for All Municipalities)

After fetching official pages, **view Google Maps directly** for every municipality.
Open the map and visually inspect the area — do not search for map references.

Map verification is **mandatory** regardless of what official pages contain, because:
- Parks can appear on Google Maps with no official web presence
- Official websites are frequently incomplete or outdated
- Small parks and neighborhood parks are consistently underrepresented online

**For villages under 1,000 population**: Map verification is especially critical.
Never mark a village as zero parks without viewing the map directly.

**Browser unavailable**: If Claude in Chrome is not connected, do NOT mark municipalities
complete. Flag each as `PENDING/UNVERIFIED — map verification required`.

**During map verification, also scan for trail access points**: If the map shows
trailhead markers, parking areas, or access points for trails already documented
in higher tiers, capture these as Access Point records.

**GPS capture during map verification (IMP-031)**: When you click into a Google Maps
entity detail card to confirm an entity's identity, **capture the GPS coordinates from
the page URL at the same time**. The URL format `@LAT,LON,ZOOMz` contains decimal
coordinates. Write these to the Captured Source Data table in the handoff and to
`gps_lat_raw` / `gps_lon_raw` in the staging record. Annotate in `identity_notes_raw`:
`"GPS from Google Maps detail card during map verification — treat as approximate until
GPS acquisition pass confirmation."`

**Multi-municipality ordering rule (IMP-015)**: In counties with multiple adjacent
municipalities, do **not** run map verification per municipality as web discovery
proceeds. Instead:

1. Complete Steps 2, 3, 4.3a, and 4.3b for **all** municipalities in the county first.
2. Then run map verification as a **single consolidated pass** across all jurisdictions.

This prevents false attributions — parks in adjacent un-cataloged jurisdictions visible
on the map during verification of a specific municipality.

This ordering rule applies only to counties with two or more adjacent municipalities.

## 4.5 Step 5: Fallback Protocol (When Official Pages Are Empty or Absent)

If the official parks page is empty, events-only, or no official website exists,
run the following fallback searches before recording zero:

1. **Google Maps view** (Step 4 above — mandatory regardless)
2. **Tripadvisor search**: "[Municipality Name] Ohio parks attractions"
3. **County GIS parcel search**: Check for parcels with owner = municipality name
4. **Grant record search** (see Step 7 below)

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
search grant award records before recording zero:

```
Search: "[Municipality Name] Ohio LEGACY Fund grant park"
Search: "[Municipality Name] Ohio LWCF grant recreation"
Search: "[Municipality Name] Ohio parks recreation fund grant"
Search: "[County] Community Foundation grant [Municipality Name]"
```

Grant records confirm park existence even when no web or map presence exists.
A grant award for "park restoration" or "park improvements" is definitive evidence
that a park exists. Create a raw record and flag it as:
`GRANT_CONFIRMED — no web/map presence; park name and location require field verification`

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

## 5.6 Multi-Municipal Sites & Trailthings
Do not segment. Record all municipalities and counties.

**Cross-tier Trailthings**: When a named trail is documented on municipal sources but is
primarily managed by a non-municipal entity (e.g., a metro park district at Tier 3,
an ODNR trail at Tier 2, or a county trail at Tier 4), stage a Tier 6 record for the
Trailthing regardless. Add to `identity_notes_raw`:
`"Cross-tier trail — primary manager is [tier name / entity name]; Tier 6 documents this trail"`

Do not suppress the Tier 6 record on the assumption that the managing tier will cover it.
Resolution merges cross-tier records and assigns canonical status to the managing tier.

## 5.7 HOA Parks, Private Amenities, Gated Facilities
Exclude unless municipality is explicitly owner/manager.

## 5.8 Business Parks, Corporate Campuses, Plazas
Exclude unless formally designated as municipal parks.

## 5.9 Indoor-Only Facilities
Exclude unless part of a larger identity-bearing Site.

## 5.10 Brownfields, Redevelopment Areas, Future Parks
Include only if identity-bearing and formally designated.

## 5.11 Columbus Recreation & Parks (CRP) Naming Convention

Columbus Recreation & Parks (columbusrecparks.com) systematically names parcel-level
land holdings with a "Parkland" suffix (e.g., "Amberfield Parkland"). Regional sources
— MORPC Parks & Open Space layer, Franklin County GIS — use the "Park" suffix for the
same entities.

**Discovery rule**: Capture `name_raw` exactly as listed on the CRP source page. Do not
normalize the suffix during discovery. Normalization handles "Parkland" → "Park" conversion.

**GPS matching hazard**: The Parkland/Park discrepancy causes score degradation during
GPS name-matching. Sites scoring in the 85–92 range that end in "Parkland" should be
manually reviewed for this cause before being marked unmatched.

## 5.12 MORPC Import Field Mapping (IMP-028)

The MORPC Parks & Open Space layer (and similar regional GIS layers) provides both
a managing organization name and a park type classification. These must be written
to separate fields:

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

This rule applies to all batch import scripts.

## 5.13 Large Municipality Batching Protocol (IMP-001)

### 5.13.1 Trigger

A municipality requires batched discovery when it has **more than 100 parks**. This
threshold applies to all entity types combined. For known large cities (Columbus,
Cleveland, Cincinnati, Toledo, Akron, Dayton), assume batching is required before
beginning.

### 5.13.2 Core Approach

Discovery proceeds alphabetically in batches of 100 parks. Alphabetical order is
determined by the park's name as it appears on the official parks listing page.

### 5.13.3 Mandatory Pre-Discovery Enumeration

Before any detail-page fetching begins:

1. Fetch all pages of the parks listing (following JS pagination rules per §4.3b).
2. Record all park names in the order they appear, then sort alphabetically.
3. Count the total. If ≤ 100, abandon batching and proceed as a normal municipality.
4. Divide the sorted list into consecutive groups of 100:
   - Batch 1: parks 1–100
   - Batch 2: parks 101–200
   - etc. (final batch may be smaller than 100)
5. Record the alphabetical range of each batch (first and last park name).
6. Document the batch plan in the session log before any detail fetching begins.

### 5.13.4 Batch Labeling Convention

```
[Municipality Name] — Batch [N] ([First Park Name] → [Last Park Name])
```

Examples:
```
Columbus (CRP) — Batch 1 (Alum Creek Parkland → Driving Park)
Columbus (CRP) — Batch 2 (East Broad Street Parkland → Kinnear Park)
```

### 5.13.5 Staging File Conventions

All batches for a single municipality write to the **same staging YAML file**. Each
entity record must have a `---` separator. Batch transitions do not require any
special delimiter beyond the standard per-record `---`.

In discovery metadata (session log entry for each batch), record:

```yaml
municipality: "Columbus"
municipality_batch: "Batch 1 (Alum Creek Parkland → Driving Park)"
batch_status: complete   # or: in_progress | pending
parks_in_batch: 100
parks_fetched: 100
```

### 5.13.6 Session Log Requirements

Maintain a running session log entry for each batch:
- Batch label and park range
- Total parks enumerated in batch
- Parks successfully fetched and staged
- Parks skipped (404, access block, etc.) with reason
- Batch status: `complete` or `in_progress`

### 5.13.7 Baseline Tracking Across Batches

Baseline seeds for the municipality are tracked across all batches collectively.
Do not flag seeds as unconfirmed until all batches for the municipality are done.

### 5.13.8 Map Verification

Map verification for a large municipality runs as a single pass after **all batches
are complete** — not after each batch.

### 5.13.9 Completion Criterion

A large municipality is **complete** when:
1. All batches are marked `complete` in the session log.
2. All batches are accounted for in the staging YAML.
3. Map verification pass has been completed.
4. All baseline seeds are confirmed or flagged.

------------------------------------------------------------
# 6. RED FLAGS: INDICATORS OF MISSED ENTITIES

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
- Trailthing listing pages
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

## 7.3 Document Collection

During Tier 6 discovery, download all qualifying source documents encountered —
trail maps, park brochures, greenway plans, master plans, GPX/KML files — and log
each in the county document log per **Discovery Orchestration Module v6.0 §4**.

Particularly valuable documents to capture at Tier 6:
- Municipal parks trail maps
- Greenway and bikeway maps
- Parks master plans and recreation master plans
- Park brochures and visitor guides
- GPX/KML files for municipal trails

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
- Meets Child Site Rules per Site Discovery Sub-Procedure v6.0

## 8.3 Trailthing Creation
Surface when:
- Named trail, trail section, trail system, or trail network appears on
  municipal/county pages, in planning documents, in meeting minutes, or in GIS

Capture `source_term_raw` verbatim (how the source describes the entity) and
`source_hierarchy_context_raw` when the source frames the entity in relation to
others. Do not classify the Trailthing as trail vs. trail network vs. trail segment
during discovery — record what the source says.

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the
source. Record `urls_raw` for all discovered map URLs. Download trail maps and
GPX/KML files per §7.3.

**Cross-tier Trailthings**: When a named trail appearing on municipal sources is
primarily managed by a non-municipal entity (Tier 2–5), Tier 6 must still stage a
discovery record.

- Record `governance_raw` exactly as stated on the municipal source. If the municipal
  page identifies the actual managing entity (e.g., "Maintained by Metro Parks"), record
  that value — not "City of X."
- Add to `identity_notes_raw`: `"Cross-tier trail — primary manager is [entity name / Tier N]; Tier 6 documentation"`
- Do not defer to the managing tier or suppress the Tier 6 record.
- Resolution Engine merges cross-tier Trailthing records and assigns canonical status
  to the management tier's record.

## 8.4 Site Network Creation
Surface when:
- Municipal multi-site system exists
- Conservation/greenway network documented

Apply Site Network threshold rules per Site Network Discovery Sub-Procedure v6.0 §3.

**If no Site Networks qualify at Tier 6:** Document an explicit null-evidence block
before advancing to Access Point creation. Silence is not a null.

```yaml
entity_type_result:
  tier: 6
  governance_level: Municipal
  entity_type: Site Network
  result: null
  sources_checked:
    - [URL or source description]
  reasoning: [why no Site Networks qualify — threshold not met; municipality
              manages fewer than 3 in-scope sites; no qualifying system found, etc.]
```

At minimum, two sources must be checked before concluding null.

## 8.5 Access Point Creation
Surface when:
- Appears on municipal pages
- Appears on county-hosted municipal pages
- Appears in planning documents
- Appears in meeting minutes
- Appears in GIS

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.
Populate `last_verified_date` with today's date; set `field_verified: false`.

------------------------------------------------------------
# 9. TIER-SPECIFIC EXPECTATIONS

Tier 6 must surface:
- All municipal Sites
- All identity-bearing child Sites
- All municipal Trailthings (trails, trail sections, trail systems)
- All municipal Access Points
- All parks/trails on county-hosted municipal pages
- All identity-bearing greenways
- All identity-bearing joint-use Sites

Tier 6 may surface:
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
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships
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
# 11. OUTPUT REQUIREMENTS

Each municipal entity must output a Raw Discovery Record conforming to:
- The appropriate v6.0 Schema Module
- The appropriate v6.0 Vocabulary Module

No normalized fields may appear in Tier 6 output.

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
# END OF MUNICIPAL LANDS DISCOVERY SUB-PROCEDURE v6.0
