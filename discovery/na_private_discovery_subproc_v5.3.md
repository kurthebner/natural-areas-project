# NATURAL AREAS PROJECT
# PRIVATE & ORGANIZATION-BASED DISCOVERY SUB-PROCEDURE v5.7
(Tier 8 — Private Nature Preserves, Camps, Retreat Centers, Scout Camps, Church Camps, Fraternal Lands, HOA Open Space, Corporate Lands, Golf Courses, Cemeteries)

This module defines the authoritative, deterministic Tier-8 discovery rules for
private and organization-based lands within the v5.x Raw → Resolution → Normalization →
Entity Graph pipeline.

This module supersedes Private & Organization-Based Discovery Sub-Procedure v5.4.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.6 → v5.7

- **IMP-111 — Cemetery completeness: GNIS enumeration mandatory**: Added mandatory
  GNIS county cemetery enumeration as the first step in the §5.1 cemetery section.
  Before running any cemetery search queries, the USGS GNIS county cemetery list must
  be consulted to establish a complete baseline of all registered cemetery place names.

  Three sources in priority order:
  1. **OhioGenealogyExpress.com** (Ohio-specific, updated weekly):
     `https://ohiogenealogyexpress.com/{county}/{county}co_cems.htm`
     77 cemeteries listed for Hancock County; county name in URL is lowercase.
  2. **PeopleLegacy** (GPS on individual cemetery pages):
     `https://peoplelegacy.net/cemeteries/OH/{County_Name}_County/`
  3. **USGS GNIS Ohio state file** (authoritative, 7,414 statewide):
     download and filter by county FIPS + feature class Cemetery

  Each GNIS cemetery name is cross-referenced against the staging YAML. Any cemetery
  not already staged in Tiers 2–7 becomes a required T8 evaluation target. GNIS-only
  names with no corroborating source are staged with `status: Closed` or
  `identity_notes_raw: "GNIS-only — unconfirmed active status"`. GNIS list must be
  written to handoff Captured Source Data (IMP-030).

  Added **Private Cemetery** to §2 Scope: covers for-profit cemetery companies,
  historical association cemeteries, and unmanaged named burial grounds not covered by
  Church Cemetery, Family Cemetery, or any government tier.

------------------------------------------------------------
# CHANGES FROM v5.5 → v5.6

- **IMP-110 — All Golf Courses In Scope**: Extended §2 Scope to include ALL golf courses
  regardless of access model — public, semi-private, members-only, and closed. The previous
  scope covered only private/country-club golf courses (IMP-099). Public-access golf courses
  operated by private entities fall through T4/T6 discovery because they are not
  government-managed; they must be captured at T8.

  Added mandatory **Golf Course Enumeration** step to §5.1: before any direct searches,
  enumerate all golf courses in the county using:
  1. PGA of America course finder (pga.com/play → state → county filter)
  2. County CVB/tourism bureau golf page (if it exists)
  Cross-reference both sources. Each course confirmed in the county is a required
  discovery target.

  Updated §2 Scope: "Golf courses — all types, regardless of access" (replaces
  "Private golf courses" from IMP-099).

  Updated §4 Conditions: Golf courses are always in scope regardless of access model.
  Do not apply the "no public access → exclude" rule to golf courses.

  Updated §5.1: mandatory two-step Golf Course Enumeration added before any direct
  searches: (1) PGA.com course finder filtered by county; (2) county CVB/tourism golf
  page. Every confirmed course is a required target.

  Updated status vocabulary for golf courses: `Active` (open play), `Closed` (permanently
  ceased operation), or record access conditions in `identity_notes_raw` (members-only,
  semi-private, etc.).

  Closed golf courses must still be staged with `status: Closed` — land use history is
  relevant for parcel tracking. (IMP-110)

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- **IMP-099 — Church/Family Cemeteries and Private Golf Courses**: Extended §2 Scope to
  include church cemeteries, family cemeteries, and private golf courses. Added search
  queries to §5.1 Method 1 for church/religious organization cemeteries (including
  Find A Grave and county auditor parcel layer verification), family/private cemeteries,
  and private/semi-private golf courses. Private golf courses use status "No Public Entry"
  or "Access Permit Required" per access level.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- **IMP-029**: Added Pre-Discovery Checklist cross-reference to §6.1 — after identifying
  private organizations and sites from listing and directory pages and before fetching
  individual property pages, the entity list must be written to the handoff's Pre-Discovery
  Checklist. Prevents redundant re-enumeration after context breaks.
- **IMP-030**: Added Captured Source Data cross-reference to §6.1 — when a structured
  source table (camp directory, preserve listing with addresses or acreages) is fetched,
  it must be written verbatim to the handoff's Captured Source Data section immediately,
  not deferred to staging time.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- Added `description_raw` to Metadata Requirements — must be captured when a narrative description exists on the source page; distinct from `features_raw`
- Added first-pass capture rule to §6.1: when fetching a private site or organization page, extract description_raw and features_raw in the same fetch — no deferred return visits
- Bumped version to v5.3

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Updated all cross-module references to v5.x
- Updated header version to v5.2

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **OBS-026**: Governance verification rule added to §4 — county lists mix tiers; always
  verify governance independently before assigning Tier 8
- **OBS-027**: Boundary overlap flag protocol added to §4.3 — when private parcel overlaps
  with known public land, flag as BOUNDARY_OVERLAP for GIS verification
- **OBS-030**: Hunting preserve and agritourism search queries added to §5.1
- **OBS-031**: NRHP features within Tier-8 parcels rule added to §7.1 — NRHP-listed
  features on private land with public access create child Site records

------------------------------------------------------------
# 1. PURPOSE

The Private & Organization-Based Discovery Sub-Procedure v5.x defines how Tier 8 must:

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
- Produce Raw Discovery Records v5.x
- Produce Discovery Metadata v5.x

This module is referenced only by:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x

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
- **Church cemeteries** — cemeteries owned and operated by a religious congregation or parish (IMP-099)
- **Family cemeteries** — named private burial grounds on private property, including farm family plots (IMP-099)
- **Private cemeteries** — for-profit cemetery companies, historical association cemeteries, memorial parks, and any named burial ground not managed by a government entity and not fitting Church or Family Cemetery classification (IMP-111)
- **Golf courses — all types** — public, semi-private, members-only, country club, and invitation-only courses, including closed/former courses (IMP-099, IMP-110). All golf courses are in scope regardless of access model.

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

All sources must be logged in **Discovery Metadata v5.x**.

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

**Exception — Golf Courses (IMP-110):** Golf courses are ALWAYS in scope regardless of access model. Do not apply the "no public access → exclude" rule to golf courses. A members-only country club with zero public access is still a required discovery target.

## 4.1 Limited-Access Sites
If access is:
- Seasonal
- Fee-based
- Reservation-only
- Program-only

→ Include, but record access limitations in `identity_notes_raw` and metadata.

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

**Cemetery completeness check — GNIS enumeration** (mandatory — IMP-111):

This step runs BEFORE any cemetery search queries. Its purpose is to establish a
complete county-level baseline of all registered cemetery place names so that
individual search queries can be targeted at gaps rather than open-ended.

**Step 1 — Access the county cemetery list** (use all three sources; cross-reference):

1. **OhioGenealogyExpress.com county cemetery index** (Ohio-specific — use first):
   URL pattern: `https://ohiogenealogyexpress.com/{county}/{county}co_cems.htm`
   Example: `https://ohiogenealogyexpress.com/hancock/hancockco_cems.htm`
   County name in URL is lowercase with no spaces (hancock, wood, allen, putnam, etc.).
   Run by Sharon Wick, updated weekly. Lists all transcribed cemeteries by name for the
   county. Coverage for Hancock County: 77 named cemeteries. Also check the county main
   page (`https://ohiogenealogyexpress.com/{county}/`) for adjoining county links and
   additional data sections (church records, localities, etc.) that may name cemeteries.
   Site-wide freefind search: `https://search.freefind.com/find.html?id=29505058&query=cemetery+{county}`

2. **PeopleLegacy county cemetery directory** (GPS on individual pages):
   URL pattern: `https://peoplelegacy.net/cemeteries/OH/{County_Name}_County/`
   Example: `https://peoplelegacy.net/cemeteries/OH/Hancock_County/`
   Lists cemeteries alphabetically and by city with GPS, working hours, and burial records
   on individual cemetery pages. Use to supplement OhioGenealogyExpress and to acquire GPS.

3. **USGS GNIS Ohio state file** (authoritative — use when other sources yield thin results):
   Download from `https://www.usgs.gov/tools/geographic-names-information-system-gnis`
   → Downloads → State files → Ohio. Filter rows where `FEATURE_CLASS = Cemetery`
   AND `COUNTY_NUMERIC` = county FIPS (e.g., 059 for Hancock, 173 for Wood).
   Covers 7,414 Ohio cemeteries statewide; use to catch any names absent from sources 1–2.

**Step 2 — Write the GNIS list to the handoff** (IMP-030):
Write the county's complete GNIS cemetery name list to the handoff's Captured Source
Data section immediately upon retrieval. Do not defer.

**Step 3 — Cross-reference against staging YAML:**
For each cemetery name in the GNIS list:
- If already staged at any tier (T2–T7) → skip; mark confirmed in handoff table
- If not staged → evaluate governance and stage accordingly:
  - Government owner missed at T4/T5/T6 → add to that tier; note the miss
  - Church/parish owner → stage as T8 Church Cemetery (§2)
  - Family/farm name → stage as T8 Family Cemetery (§2)
  - For-profit operator or historical association → stage as T8 Private Cemetery (§2)
  - Owner unknown / no corroborating source found → stage as T8 with:
    `identity_notes_raw: "GNIS-only — active status unconfirmed; verify before upsert"`
    `status: Closed` (default unless confirmed active)

**Step 4 — Historical/defunct GNIS entries:**
GNIS `status: Historical` entries represent former cemetery locations that may be
unmarked, converted, or absorbed into other parcels. Stage with `status: Closed`.
These are still required discovery candidates — do not skip.

---

**Church cemeteries, family cemeteries, and private cemeteries** (mandatory — these are
commonly missed and not fully captured by GNIS enumeration alone):
- "[County] Ohio church cemetery"
- "[County] Ohio Catholic cemetery parish"
- "[County] Ohio Lutheran Baptist Methodist cemetery"
- "[County] Ohio family cemetery private"
- **Find A Grave** ([findagrave.com](https://www.findagrave.com)): Browse by county →
  filter by cemetery type → identify church-named, family-named, and memorial park
  cemeteries not already captured at Tiers 4–6 or in the GNIS list
- **County auditor parcel layer**: Filter for CEM-coded parcels with private/church
  ownership — these are not captured by township or municipal searches; may also
  surface cemeteries not yet in GNIS

Church cemetery classification: `category: Cemetery`, `subtype: Church Cemetery`.
Family cemetery: `subtype: Family Cemetery`. Private/for-profit cemetery:
`subtype: Private Cemetery`. Governance/ownership must reference the specific
congregation, family name, or operating company.

**Golf courses — ALL types** (mandatory — IMP-110):

**Step 1 — Enumerate before searching.** Before running direct searches, enumerate all golf courses in the county using two authoritative directories:
1. **PGA of America course finder**: pga.com/play → select state → filter by county. Export or record every listed course name, address, and access type.
2. **County CVB/tourism bureau golf page**: Most counties publish a golf page listing all local courses. Fetch it directly. Cross-reference against the PGA list.

Every course confirmed in the county from either source is a required discovery target.

**Step 2 — Direct searches for any courses not in directories:**
- "[County] Ohio golf course"
- "[County] Ohio country club golf"
- "[County] Ohio golf club tee times"
- "[County] Ohio golf course closed" (catches former courses not in active directories)

**Step 3 — Stage all confirmed courses.** All golf courses are in scope regardless of access model:
- Public courses (open tee times) → `status: Active`, `identity_notes_raw: "Public access — open tee times"`
- Semi-private courses (member priority, public tee times available) → `status: Active`, `identity_notes_raw: "Semi-private — public tee times available"`
- Members-only / country club → `status: Active`, `identity_notes_raw: "Members-only — no public tee times"` (do NOT use `status: No Public Entry` for golf courses; use Active + note)
- Closed/former courses → `status: Closed`, document closure year in `identity_notes_raw`

`category: Recreation Facility`, `subtype: Golf Course` for all golf courses. Record the course name, operator/governance, hole count, address, and any public access conditions in `identity_notes_raw`. Acreage from county auditor parcel if available.

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

**First-Pass Capture**: When fetching a private site, camp, or preserve page, extract ALL available fields in a single pass — including `description_raw` (the narrative paragraph describing the site's character, ecology, or significance) and `features_raw` (the amenity or facilities list). Both fields are typically present on the same page. A return visit to collect fields that were available on first fetch is a process failure. See `na_site_discovery_subproc.md` §7.3 for field definitions, source guidance, and the Description Quality Gate (IMP-032).

**Pre-Discovery Checklist (IMP-029)**: After identifying private organizations and sites from listing and directory pages and before fetching individual property pages, write the full entity list to the handoff's **Pre-Discovery Checklist**. A context break between enumeration and individual fetches should not require re-enumerating from source. See na-discovery skill.

**Captured Source Data (IMP-030)**: When fetching a structured source table (camp directory, private preserve listing with addresses or acreages), write it verbatim to the handoff's **Captured Source Data** section immediately — do not defer to staging time. See na-discovery skill.

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
- If the NRHP feature has no public access → add as a note in `identity_notes_raw`:
  "NRHP-listed feature on property: [name], [NRHP ref]"
- Do not create a standalone Site for a non-public NRHP feature on private land

When a standalone NRHP listing exists on private land with documented public
access (e.g., a mound accessible via easement), create it as a Tier-8 Site
directly. Cross-reference the NRHP record number in `identity_notes_raw`.

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
Record `urls_raw` for all discovered map URLs.

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
Record access limitations in `identity_notes_raw` (e.g., seasonal, fee-based, reservation-only).
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
- Access limitations recorded in `identity_notes_raw`
- Raw ownership type in `ownership_raw`

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 10. OUTPUT REQUIREMENTS

Each private or organization-based entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- The appropriate Schema Module v5.x
- The appropriate Vocabulary Module v5.x

No normalized fields may appear in Tier 8 output.

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
# END OF PRIVATE & ORGANIZATION-BASED DISCOVERY SUB-PROCEDURE v5.6
