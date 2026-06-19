# NATURAL AREAS PROJECT
# PRIVATE & ORGANIZATION-BASED DISCOVERY SUB-PROCEDURE v6.0
(Tier 8 — Private Nature Preserves, Camps, Retreat Centers, Scout Camps, Church Camps, Fraternal Lands, HOA Open Space, Corporate Lands, Golf Courses, Cemeteries)

This module defines the authoritative, deterministic Tier 8 discovery rules for
private and organization-based lands within the v6.x pipeline.

This module supersedes Private & Organization-Based Discovery Sub-Procedure v5.7.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v6.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.7 → v6.0

- **Entity type references updated throughout**: Trail, Trail Segment, and Trail
  Network are unified into the single Trailthing entity type. §1 Purpose, §7 Entity
  Creation Rules, §8 Tier-Specific Expectations, and §9 Metadata Requirements
  updated accordingly. §7.3–7.5 (Trail, Trail Segment, Trail Network creation)
  consolidated into §7.3 (Trailthing Creation). §7.6 Site Network renumbered to §7.4;
  §7.7 Access Point renumbered to §7.5.

- **Document Collection added** (§6.3): During Tier 8 discovery, all qualifying
  maps, PDFs, GPX/KML files, and other source documents must be downloaded and logged
  per Discovery Orchestration Module v6.0 §4.

- **All v5.7 rules carried forward**: IMP-111 (GNIS cemetery enumeration), IMP-110
  (All golf courses in scope), IMP-099 (Church/Family cemeteries and private golf
  courses), IMP-029 (Pre-Discovery Checklist), IMP-030 (Captured Source Data),
  OBS-026 (Governance verification), OBS-027 (Boundary overlap flag protocol),
  OBS-030 (Hunting preserve and agritourism searches), OBS-031 (NRHP features on
  private land).

------------------------------------------------------------
# 1. PURPOSE

The Private & Organization-Based Discovery Sub-Procedure v6.0 defines how Tier 8 must:

- Identify private or organization-based Sites
- Identify child Sites within private holdings
- Identify Trailthings on private lands
- Identify Site Networks (rare but possible)
- Identify Access Points associated with private holdings
- Distinguish public, limited, and private access
- Identify identity-bearing private natural areas
- Identify private preserves owned by nonprofits or foundations
- Identify private trail systems with public or limited access
- Handle multi-county private holdings
- Log uncertainty, conflicts, and boundary cases
- Produce Raw Discovery Records v6.x
- Download and log source documents per the Document Collection System

This module is referenced only by:
- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.0

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
- PDF brochures (download per §6.3)
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

All sources must be logged in discovery metadata.

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

**Exception — Golf Courses (IMP-110):** Golf courses are ALWAYS in scope regardless
of access model. Do not apply the "no public access → exclude" rule to golf courses.
A members-only country club with zero public access is still a required discovery target.

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

## 4.3 Governance Verification Before Tier Assignment (OBS-026)
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

## 4.4 Boundary Overlap Flag Protocol (OBS-027)
When a private parcel appears to overlap with a known public land unit based on
GPS coordinates or GIS review:

- Do not suppress the private entity
- Do not assume the GPS is wrong
- Flag with: `BOUNDARY_OVERLAP — parcel overlaps with [entity name]; GIS verification required`
- Document both the private parcel information and the overlapping public entity
- Resolution and normalization will arbitrate using authoritative GIS data

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

**Hunting preserves and agritourism** (mandatory — these are commonly missed) (OBS-030):
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

Private hunting preserves with public/fee access are valid Tier 8 Sites even when
their primary use is commercial. Many also maintain trail systems and natural areas.

**Cemetery completeness check — GNIS enumeration** (mandatory — IMP-111):

This step runs BEFORE any cemetery search queries. Its purpose is to establish a
complete county-level baseline of all registered cemetery place names so that
individual search queries can be targeted at gaps rather than open-ended.

**Step 1 — Access the county cemetery list** (use all three sources; cross-reference):

1. **OhioGenealogyExpress.com county cemetery index** (Ohio-specific — use first):
   URL pattern: `https://ohiogenealogyexpress.com/{county}/{county}co_cems.htm`
   Example: `https://ohiogenealogyexpress.com/hancock/hancockco_cems.htm`
   County name in URL is lowercase with no spaces. Run by Sharon Wick, updated weekly.
   Also check the county main page for adjoining county links and additional data.
   Site-wide freefind search: `https://search.freefind.com/find.html?id=29505058&query=cemetery+{county}`

2. **PeopleLegacy county cemetery directory** (GPS on individual pages):
   URL pattern: `https://peoplelegacy.net/cemeteries/OH/{County_Name}_County/`
   Example: `https://peoplelegacy.net/cemeteries/OH/Hancock_County/`
   Lists cemeteries alphabetically and by city with GPS, working hours, and burial
   records on individual cemetery pages. Use to supplement OhioGenealogyExpress
   and to acquire GPS.

3. **USGS GNIS Ohio state file** (authoritative — use when other sources yield thin results):
   Download from `https://www.usgs.gov/tools/geographic-names-information-system-gnis`
   → Downloads → State files → Ohio. Filter rows where `FEATURE_CLASS = Cemetery`
   AND `COUNTY_NUMERIC` = county FIPS. Covers 7,414 Ohio cemeteries statewide.

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
- **Find A Grave** (findagrave.com): Browse by county → filter by cemetery type →
  identify church-named, family-named, and memorial park cemeteries not already
  captured at Tiers 4–6 or in the GNIS list
- **County auditor parcel layer**: Filter for CEM-coded parcels with private/church
  ownership — these are not captured by township or municipal searches; may also
  surface cemeteries not yet in GNIS

Church cemetery classification: `category: Cemetery`, `subtype: Church Cemetery`.
Family cemetery: `subtype: Family Cemetery`. Private/for-profit cemetery:
`subtype: Private Cemetery`. Governance/ownership must reference the specific
congregation, family name, or operating company.

**Golf courses — ALL types** (mandatory — IMP-110):

**Step 1 — Enumerate before searching.** Before running direct searches, enumerate
all golf courses in the county using two authoritative directories:
1. **PGA of America course finder**: pga.com/play → select state → filter by county.
   Export or record every listed course name, address, and access type.
2. **County CVB/tourism bureau golf page**: Most counties publish a golf page listing
   all local courses. Fetch it directly. Cross-reference against the PGA list.

Every course confirmed in the county from either source is a required discovery target.

**Step 2 — Direct searches for any courses not in directories:**
- "[County] Ohio golf course"
- "[County] Ohio country club golf"
- "[County] Ohio golf club tee times"
- "[County] Ohio golf course closed" (catches former courses not in active directories)

**Step 3 — Stage all confirmed courses.** All golf courses are in scope regardless of
access model:
- Public courses → `status: Active`, `identity_notes_raw: "Public access — open tee times"`
- Semi-private → `status: Active`, `identity_notes_raw: "Semi-private — public tee times available"`
- Members-only → `status: Active`, `identity_notes_raw: "Members-only — no public tee times"`
- Closed/former → `status: Closed`, document closure year in `identity_notes_raw`

`category: Recreation Facility`, `subtype: Golf Course` for all golf courses. Record
the course name, operator/governance, hole count, address, and any public access
conditions in `identity_notes_raw`. Acreage from county auditor parcel if available.

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
- Trailthing listings
- Facility listings
- Map index pages
- Directory-linked pages

Extract ALL first-level entity URLs.

**First-Pass Capture**: When fetching a private site, camp, or preserve page, extract
ALL available fields in a single pass — including `description_raw` (the narrative
paragraph describing the site's character, ecology, or significance) and `features_raw`
(the amenity or facilities list). Both fields are typically present on the same page.
A return visit to collect fields that were available on first fetch is a process failure.
See Site Discovery Sub-Procedure v6.0 §7.3 for field definitions and the Description
Quality Gate.

**Pre-Discovery Checklist (IMP-029)**: After identifying private organizations and
sites from listing and directory pages and before fetching individual property pages,
write the full entity list to the handoff's Pre-Discovery Checklist. A context break
between enumeration and individual fetches should not require re-enumerating from source.

**Captured Source Data (IMP-030)**: When fetching a structured source table (camp
directory, private preserve listing with addresses or acreages), write it verbatim to
the handoff's Captured Source Data section immediately — do not defer to staging time.

## 6.2 Recursive Discovery (URL Propagation)
Follow internal links for:
- Trailthings
- Maps
- Access
- Facilities
- Natural areas
- Program areas

Respect recursion limits and allowlists.

## 6.3 Document Collection

During Tier 8 discovery, download all qualifying source documents encountered —
trail maps, preserve brochures, camp maps, GPX/KML files — and log each in the
county document log per **Discovery Orchestration Module v6.0 §4**.

Particularly valuable documents to capture at Tier 8:
- Private preserve trail maps and visitor guides
- Camp maps showing trail systems and natural areas
- Scout camp trail maps

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

**NRHP Features Within Private Parcels** (OBS-031): When a National Register of
Historic Places listing (mound, archaeological site, historic structure, historic
district) exists within or on a private parcel that is already being documented as
a Tier 8 Site:
- If the NRHP feature has public visitor access → create a child Site record
- If the NRHP feature has no public access → add as a note in `identity_notes_raw`:
  "NRHP-listed feature on property: [name], [NRHP ref]"
- Do not create a standalone Site for a non-public NRHP feature on private land

When a standalone NRHP listing exists on private land with documented public
access (e.g., a mound accessible via easement), create it as a Tier 8 Site
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

## 7.3 Trailthing Creation
Create a **Trailthing** when:
- A named trail, trail section, trail system, or trail network appears on official
  maps or brochures, in directories, in county GIS, or in partnership announcements

Capture `source_term_raw` verbatim (how the source describes the entity) and
`source_hierarchy_context_raw` when the source frames the entity in relation to
others. Do not classify the Trailthing as trail vs. trail network vs. trail segment
during discovery — record what the source says.

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the
source. Record `urls_raw` for all discovered map URLs. Download trail maps and
GPX/KML files per §6.3.

## 7.4 Site Network Creation
Create a **Site Network** when:
- A private organization manages a multi-site system
- A corridor-scale or campus-scale network is documented

Apply Site Network threshold rules per Site Network Discovery Sub-Procedure v6.0 §3.

**If no Site Networks qualify at Tier 8:** Document an explicit null-evidence block
before advancing to Access Point creation. Silence is not a null.

```yaml
entity_type_result:
  tier: 8
  governance_level: Private
  entity_type: Site Network
  result: null
  sources_checked:
    - [URL or source description]
  reasoning: [why no Site Networks qualify — threshold not met, no qualifying
              private multi-site system found, etc.]
```

At minimum, two sources must be checked before concluding null.

## 7.5 Access Point Creation
Create an **Access Point** when:
- It appears on official maps
- It appears in brochures
- It appears in county GIS
- It appears in directories
- It appears in partnership announcements

Record `features_raw` for all documented amenities at the access point.
Record access limitations in `identity_notes_raw` (e.g., seasonal, fee-based, reservation-only).
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.
Populate `last_verified_date` with today's date; set `field_verified: false`.

------------------------------------------------------------
# 8. TIER-SPECIFIC EXPECTATIONS

Tier 8 must surface:
- All identity-bearing private Sites
- All identity-bearing child Sites
- All private Trailthings (trails, trail sections, trail systems)
- All private Access Points
- All private trail systems with public or limited access
- All private preserves owned by nonprofits or foundations
- All university natural areas and research preserves with visitor access
- All organizations referenced in partnership mentions from Tiers 1–7

Tier 8 may surface:
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
- Access limitations recorded in `identity_notes_raw`
- Raw ownership type in `ownership_raw`

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 10. OUTPUT REQUIREMENTS

Each private or organization-based entity must output a Raw Discovery Record
conforming to:
- The appropriate v6.0 Schema Module
- The appropriate v6.0 Vocabulary Module

No normalized fields may appear in Tier 8 output.

------------------------------------------------------------
# 11. INTEGRATION POINTS

This module integrates with:
- Discovery Orchestration Module v6.0
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- Resolution Engine v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:
- Discovery Orchestration Module v6.0 *(for document collection rules, §4)*
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- Resolution Engine v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF PRIVATE & ORGANIZATION-BASED DISCOVERY SUB-PROCEDURE v6.0
