# NATURAL AREAS PROJECT
# CONSERVANCY & LAND TRUST DISCOVERY SUB-PROCEDURE v5.6
(Tier 7 — Land Trusts, Conservancies, Foundations, Trail Alliances, Greenway Coalitions, Watershed Nonprofits)

This module defines the authoritative, deterministic Tier-7 discovery rules for
nonprofit conservation landholders within the v5.x Raw → Resolution → Normalization →
Entity Graph pipeline.

This module supersedes Conservancy & Land Trust Discovery Sub-Procedure v5.5.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.5 → v5.6

- **IMP-134**: Added §4.5 Southwest Ohio — Cardinal Land Conservancy entry for Hamilton,
  Clinton, Brown, and Clermont counties. 18 preserves total; 4 with public access at time
  of documentation (2026-05-23). Access verification guidance added. County run history
  table seeded with Wood County (NULL — outside service territory).

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- **IMP-130**: Added §4 Known Organizations — Running Inventory, modeled on State
  sub-procedure §4 format. Each major T7 organization in Ohio gets a named subsection
  with explicit URLs, service territory, applicability rules, and a cumulative county
  run history table. Prevents re-researching the same organization on every county run.
  Existing §4–§11 renumbered to §5–§12. Internal cross-reference "See §4.7" updated to
  "See §5.7"; changelog references updated accordingly.
- **IMP-130**: Updated §3.2 — added LTA directory URL. Updated §3.5 — added forward
  reference to new §4 for known Ohio organizations.
- **IMP-130**: Added ACRES Land Trust as a mandatory check for the 5 northernmost Ohio
  counties on the Indiana border (Williams, Defiance, Paulding, Van Wert, Mercer).
  See §4.3.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- **IMP-029**: Added Pre-Discovery Checklist cross-reference to §6.1 — after enumerating
  organizations and preserves from listing pages and before fetching individual preserve
  pages, the entity list must be written to the handoff's Pre-Discovery Checklist. Prevents
  redundant re-enumeration after context breaks.
- **IMP-030**: Added Captured Source Data cross-reference to §6.1 — when a structured
  source table (preserve directory, property listing with addresses or acreages) is fetched,
  it must be written verbatim to the handoff's Captured Source Data section immediately,
  not deferred to staging time.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- Added `description_raw` to Metadata Requirements — must be captured when a narrative description exists on the source page; distinct from `features_raw`
- Added first-pass capture rule to §6.1: when fetching a preserve or property page, extract description_raw and features_raw in the same fetch — no deferred return visits
- Bumped version to v5.3

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Updated all cross-module references to v5.x
- Updated header version to v5.2

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **OBS-024**: Trail coalition disambiguation added to §2.2 and new §5.7 — trail
  alliances that maintain trails are NOT the owner/manager; ownership must be
  confirmed before creating a Tier-7 entity
- **OBS-025**: Grant-confirmed preserve status flag added to §7.1 — preserves confirmed
  by grant records but absent from current website receive GRANT_CONFIRMED status flag
- **URL-10**: ONAPA preserve map added to §3.5 as mandatory cross-check source

------------------------------------------------------------
# 1. PURPOSE

The Conservancy & Land Trust Discovery Sub-Procedure v5.x defines how Tier 7 must:

- Identify all nonprofit-owned or nonprofit-managed Sites
- Identify child Sites within preserves
- Identify Trails, Trail Segments, and Trail Networks on nonprofit holdings
- Identify Site Networks (multi-site conservation systems)
- Identify Access Points associated with nonprofit holdings
- Identify fee-simple preserves and identity-bearing conservation easements
- Identify trail corridors, greenways, and linear preserves
- Distinguish public-access vs. non-public-access holdings
- Identify co-managed Sites and partnership lands
- Handle multi-organization stewardship and cross-tier overlaps
- Log uncertainty, conflicts, and boundary cases
- Produce Raw Discovery Records v5.x
- Produce Discovery Metadata v5.x

This module is referenced only by:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x

------------------------------------------------------------
# 2. SCOPE

This sub-procedure applies to all nonprofit conservation organizations, including:

## 2.1 Land Trusts & Conservancies
- Local, regional, statewide, and national land trusts
- Conservancies and conservation foundations
- Habitat and ecological stewardship organizations

## 2.2 Trail & Greenway Organizations
- Trail alliances
- Greenway coalitions
- Linear corridor nonprofits
- Regional trail partnerships

**IMPORTANT — Trail Coalition ≠ Trail Owner**: Trail alliances and coalitions
frequently maintain, promote, and advocate for trails without owning or managing
the underlying land. Before creating a Tier-7 entity for a trail alliance or
coalition, confirm that the organization:
- Owns fee-simple land, OR
- Holds a formal management agreement or easement, OR
- Is explicitly the named manager/steward of the land

If the alliance only maintains or promotes trails owned by a county, park district,
or state agency → the trail belongs to the owning tier, not Tier 7.
Record the alliance in `partner_agencies_raw` of the owning entity instead.
See §5.7 for detailed disambiguation rules.

## 2.3 Watershed & Habitat Organizations
- Watershed groups
- Habitat restoration nonprofits
- River corridor organizations

## 2.4 Conservation Networks
- Land trust consortiums
- Regional conservation partnerships
- Multi-organization stewardship coalitions

Tier 7 sits **below Municipal** and **above Private & Organization-Based**.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 7 must enumerate and recursively explore all authoritative nonprofit sources.

## 3.1 Official Nonprofit Websites
Scan for:
- Preserves
- Protected lands
- Conservation areas
- Nature preserves
- Public access information
- Hiking trails
- Stewardship information

Always **fetch** the official properties or preserves page directly — do not rely on
search snippets, which frequently omit smaller or lesser-known holdings.

Scan all:
- Preserve pages
- Project pages
- Maps
- PDF brochures
- Stewardship reports
- Annual reports (if they list preserves or trails)

## 3.2 Land Trust Alliance (LTA) Directory
**Required source:**
```
https://landtrustalliance.org/land-trusts/explore/
```
Check for:
- Member organizations operating in the county
- Regional affiliates
- Contact information
- Links to official websites

## 3.3 County Auditor / GIS (Parcel Verification)
Nonprofit holdings may appear as:
- Fee-simple parcels
- Conservation easements
- Trail easements
- Partnership lands

GIS is required for:
- County boundary confirmation
- Ownership confirmation
- Easement verification
- Access point verification
- Multi-county boundary detection

## 3.4 Cross-Reference from Other Tiers
Any partnership mention discovered in Tiers 1–6 must be investigated here.

Examples of cross-reference triggers:
- "In partnership with [Land Trust]"
- "Managed by [Conservancy]"
- "Trail maintained by [Alliance]"
- "Conservation easement held by [Foundation]"

Each trigger requires a dedicated search for that organization's holdings in the county.

## 3.5 Statewide & Regional Conservation Networks
Check:
- **ONAPA (Ohio Natural Areas and Preserves Association) — MANDATORY**:
  `https://www.onapa.org/preserves`
  The ONAPA preserve map includes nonprofit-owned preserves across Ohio. Search for
  the target county. ONAPA members often have limited web presence and do not appear
  in standard searches. This is the primary cross-check for Tier-7 completeness.
  If a preserve appears on the ONAPA map but has no matching entity in your records,
  investigate before closing the tier.
- **Known organizations with county run history**: See §4 for organizations identified
  during prior county runs, with explicit URLs, service territories, and cumulative
  results. Includes ACRES Land Trust (§4.3, mandatory for Indiana-border counties),
  Black Swamp Conservancy (§4.2), TNC Ohio (§4.1), NORTA (§4.4), and others.
- Regional conservation partnerships
- Watershed groups
- Greenway coalitions
- Corridor-scale conservation initiatives

## 3.6 Federal & State Partners
Nonprofits often partner with:
- ODNR
- USFWS
- USACE
- Park districts
- Counties
- Municipalities

All partnerships must be logged in metadata.

All sources must be logged in **Discovery Metadata v5.x**.

------------------------------------------------------------
# 4. KNOWN ORGANIZATIONS — RUNNING INVENTORY

This section catalogs nonprofit conservation organizations identified during Ohio county
runs. Each entry includes explicit source URLs, service territory, applicability rules,
and a cumulative county run history. Consult this section at the start of every T7 run
before beginning §3.1–§3.6 discovery.

For organizations not listed here, proceed with the standard §3.1–§3.6 discovery
approach. When a new organization is discovered during a county run, add it here and
log the discovery in the improvement tracker.

------------------------------------------------------------
## 4.1 Statewide Organizations

### The Nature Conservancy — Ohio Chapter (TNC)
**Required sources:**
```
https://www.nature.org/en-us/get-involved/how-to-help/places-we-protect/ohio/
```
Check the Ohio page for all preserves listed for the target county. TNC preserves
are typically fee-simple, publicly accessible, and identity-bearing. Trail maps and
GPS coordinates are often available on individual preserve pages.

Check for:
- Fee-simple nature preserves
- Trails and trail systems on TNC land
- Partnership lands co-managed with ODNR or other agencies

| County | Run Result |
|--------|-----------|
| Lucas | Kitty Todd Nature Preserve — T7 entity created (3 trails, ~1,000 acres oak savanna) |
| Ottawa | Great Egret Marsh — found; deferred (1.7 acres; access status uncertain at run time) |

---

### Buckeye Trail Association (BTA)
BTA is a trail advocacy and maintenance organization, not a land owner. Before creating
a T7 entity for any BTA-associated trail, apply full §5.7 disambiguation. BTA typically
does not hold fee-simple title or formal management agreements — the underlying land
is almost always owned by a county park district, state agency, or other host tier.

If BTA is named as a partner on a county park or state trail segment, record BTA in
`partner_agencies_raw` of the owning entity — do not create a T7 entity.

Exception: If a specific BTA segment has a confirmed formal trail easement or fee-simple
ownership by BTA, create the T7 entity with the evidence documented.

| County | Run Result |
|--------|-----------|
| Paulding | NULL — BTA advocacy only; Buckeye Trail segments owned by host agencies |
| Putnam | NULL — BTA advocacy only |

------------------------------------------------------------
## 4.2 Northwestern Ohio / Black Swamp Region

### Black Swamp Conservancy (BSC)
**Required sources:**
```
https://blackswamp.org/properties/land-we-own/
https://blackswamp.org/properties/land-we-protect/
```
BSC is the primary T7 land trust for northwestern Ohio. The "land-we-own" page lists
fee-simple preserves; the "land-we-protect" page lists conservation easements. Both
must be checked. Some easements are identity-bearing with public access.

**Service area:** Erie, Fulton, Henry, Lucas, Ottawa, Putnam, Sandusky, Seneca,
Van Wert, Williams, Wood counties.

Check for:
- Named nature preserves (fee-simple)
- Identity-bearing conservation easements with public access
- Trail networks within preserves

| County | Run Result |
|--------|-----------|
| Ottawa | Nehls Memorial Nature Preserve (fee-simple), Port Clinton Lakefront Preserve (BSC easement) — T7 entities created |
| Lucas | NULL |
| Paulding | NULL |
| Henry | NULL |
| Putnam | NULL |

---

### West Central Ohio Land Conservancy (WCOLC)
**Required sources:**
```
https://www.wcolc.org/land-protection
```
WCOLC focuses on agricultural and natural land protection in west-central Ohio.
Most holdings are agricultural easements without public access or identity-bearing
roles. Check the properties page for any holdings with public access or named preserves.

**Service area:** Auglaize, Darke, Hardin, Logan, Mercer, Miami, Shelby, and
adjacent counties.

Check for:
- Named nature preserves with public access
- Conservation easements that are identity-bearing

| County | Run Result |
|--------|-----------|
| Paulding | NULL — agricultural easements only, no public access |
| Putnam | NULL — agricultural easements only, no public access |

------------------------------------------------------------
## 4.3 Ohio–Indiana Border Counties (MANDATORY)

**Applies to:** Williams, Defiance, Paulding, Van Wert, Mercer counties only.

This check is MANDATORY for all five counties regardless of whether a prior search
surfaces the organization. ACRES has limited Ohio web presence and will not appear
in standard searches.

### ACRES Land Trust
**Required sources:**
```
https://acreslandtrust.org/preserves/
```
ACRES is based in Fort Wayne, Indiana, and serves northeastern Indiana and
northwestern Ohio. Check the preserves page for any holdings in the target county.
Some preserves may be closed to public access — create a T7 entity regardless and
set `status_raw` accordingly.

If a preserve is listed as closed: create a T7 entity with `status_raw` set to
"CLOSED — no public access at time of discovery" and document the closure and
source in `identity_notes_raw`.

| County | Run Result |
|--------|-----------|
| Paulding | Flat Rock Creek Nature Preserve — T7 entity created (CLOSED — no public access at time of run) |
| Lucas | NULL (outside ACRES primary service territory) |

------------------------------------------------------------
## 4.4 Trail Management Organizations

### NORTA (Northwest Ohio Rails-to-Trails Association)
**Required sources:**
```
https://northcountrytrail.org/trail/affiliates/norta/
```
Verify NORTA's own website URL at run time (may vary). NORTA owns the
Wabash Cannonball Trail rail corridor in several northwestern Ohio counties.
Unlike most trail coalitions, NORTA holds fee-simple title in at least some
counties — always confirm ownership via county auditor before applying the
§5.7 coalition exclusion.

Check for:
- Wabash Cannonball Trail segments in the target county (North Fork and South Fork)
- Any other rail-to-trail corridors owned by NORTA
- Trailheads and access points

| County | Run Result |
|--------|-----------|
| Henry | Wabash Cannonball Trail (Henry County portion) — T7 entity created; NORTA confirmed owner |
| Fulton | Wabash Cannonball Trail (Fulton County portion) — T7 entity created |

---

### Maumee Valley Heritage Corridor (MVHC)
**Required sources:** Verify current website URL at run time.

MVHC is a regional trail and heritage organization in the Maumee River corridor.
Apply full §5.7 disambiguation — confirm whether MVHC holds ownership or management
agreements before creating a T7 entity.

| County | Run Result |
|--------|-----------|
| Paulding | NULL |

---

### PARC Inc. (Fulton County)
**Required sources:** County auditor; verify organization website at run time.

PARC Inc. is a Fulton County nonprofit that holds ownership or management agreements
for specific park properties. Applicability is limited to Fulton County.

| County | Run Result |
|--------|-----------|
| Fulton | Pettisville Township Community Park — T7 entity created (PARC Inc. management confirmed) |

------------------------------------------------------------
## 4.5 Southwest Ohio

### Cardinal Land Conservancy
**Required sources:**
```
https://www.cardinallandconservancy.org/cardinal-preserves/
```
Cardinal Land Conservancy is the primary T7 land trust for the southwestern Ohio
counties along the Ohio–Kentucky border corridor.

**Service area:** Hamilton, Clinton, Brown, and Clermont counties.

Check for:
- Named nature preserves (fee-simple and conservation easement)
- Preserves with public access — not all Cardinal preserves are open to the public;
  verify access status on individual preserve pages before setting `status_raw`
- Trail records within preserves that have documented public access

**Note on access:** As of documentation (2026-05-23), Cardinal holds 18 preserves
total, of which 4 are documented as having public access. Create T7 entities for all
named, identity-bearing preserves regardless of public access status; set `status_raw`
to "No public access" or equivalent for closed preserves and document the source.

| County | Run Result |
|--------|-----------|
| Wood | NULL — outside Cardinal service territory |

------------------------------------------------------------
# 5. NONPROFIT LAND DISCOVERY CONDITIONS

## 5.1 Fee-Simple Ownership
Surface as a Site if:
- Owned by the nonprofit
- Identity-bearing (named, mapped, or designated)
- Public access exists OR the preserve is clearly named/mapped

## 5.2 Conservation Easements
Surface as a Site if:
- Public access exists, OR
- The easement is identity-bearing, OR
- It contains Trails, overlooks, or Access Points

Exclude:
- Private easements with no public access
- Agricultural easements with no recreation role
- Scenic easements with no access or identity

## 5.3 Trail Corridors & Linear Preserves
Surface as Sites if:
- Named
- Mapped
- Identity-bearing
- Have one or more Access Points

## 5.4 Multi-County Holdings
- Do not segment multi-county Sites
- Record all counties exactly as discovered in `counties_raw`

## 5.5 Co-Managed Sites
Nonprofits frequently co-manage Sites with:
- Park districts
- Counties
- Municipalities
- State or federal agencies

Record all governance details in metadata; do not attempt to resolve conflicts.

## 5.6 Stewardship-Only Lands
Exclude if:
- Nonprofit is only a stewardship partner
- No ownership, easement, or identity-bearing role exists

## 5.7 Trail Coalition vs. Trail Owner Disambiguation
When a trail alliance or greenway coalition is encountered, determine before creating
a Tier-7 entity whether the organization is the **owner/manager** or only a
**maintenance/advocacy partner**:

**Evidence of ownership/management (Tier-7 entity appropriate):**
- Organization holds fee-simple title (verify in county auditor)
- Organization is named as manager in a formal management agreement
- Organization holds a trail easement
- Organization's website describes the land as "our preserve" or "our trail"
- Grant award names the organization as the project sponsor/owner

**Evidence of maintenance/advocacy only (Tier-7 entity NOT appropriate):**
- Organization "maintains" or "promotes" a trail owned by a county or park district
- Organization's website says "partners with [county]" or "maintains trails in [park]"
- County or park district is the named landowner in auditor records
- Trail appears in a lower-tier entity's park inventory

If ownership is ambiguous: create a Tier-7 entity with `ownership_raw` flagged as
"UNCERTAIN — trail coalition; ownership verification required" and document the
ambiguity in `identity_notes_raw`.

------------------------------------------------------------
# 6. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 7 must use both enumerative and recursive discovery.

## 6.1 Enumerative Discovery (Listing Pages)
Enumerate:
- Preserve listings
- Protected land listings
- Trail listings
- Project listings
- Map index pages
- Conservation area directories

Always **fetch** listing pages directly — do not rely on search snippets.
Extract ALL entities listed, not just prominently featured ones.

**First-Pass Capture**: When fetching a preserve or property page, extract ALL available fields in a single pass — including `description_raw` (the narrative paragraph describing the site's character, ecology, or significance) and `features_raw` (the amenity or facilities list). Both fields are typically present on the same page. A return visit to collect fields that were available on first fetch is a process failure. See `na_site_discovery_subproc.md` §7.3 for field definitions, source guidance, and the Description Quality Gate (IMP-032).

**Pre-Discovery Checklist (IMP-029)**: After enumerating organizations and preserves from listing pages and before fetching individual preserve pages, write the full entity list to the handoff's **Pre-Discovery Checklist**. A context break between enumeration and individual fetches should not require re-enumerating from source. See na-discovery skill.

**Captured Source Data (IMP-030)**: When fetching a structured source table (preserve directory, property listing with addresses or acreages), write it verbatim to the handoff's **Captured Source Data** section immediately — do not defer to staging time. See na-discovery skill.

## 6.2 Recursive Discovery (URL Propagation)
Follow internal links for:
- Trails
- Maps
- Access
- Stewardship details
- Habitat units
- Management zones

Respect recursion limits and allowlists.

------------------------------------------------------------
# 7. ENTITY CREATION RULES

## 7.1 Site Creation
A nonprofit feature becomes a Site if:
- Fee-simple ownership
- Public-access conservation easement
- Identity-bearing easement
- Named trail corridor or greenway
- Appears on nonprofit website or GIS
- Appears in partnership announcements

Exclude:
- Administrative offices
- Stewardship centers not open to the public
- Private easements with no identity-bearing role

**Grant-Confirmed Preserves**: If a preserve is confirmed by grant award records
(LWCF, LEGACY Fund, Ohio PARD, county foundation) but is absent from the
organization's current website:
- Create the record — do not suppress
- Populate all fields available from the grant record (name, location, acreage, date)
- Set `status_raw` to: "GRANT_CONFIRMED — absent from current website; may be under
  development, renamed, or website outdated"
- Flag with: `GRANT_CONFIRMED`
- Document the grant source in `identity_notes_raw`

Grant-confirmed preserves are real. Their absence from the current website reflects
a documentation gap, not a non-existence. Clinton County example: Martinsville Village
Park confirmed by LEGACY Fund grant — not findable by web search or map at time of discovery.

## 7.2 Child Site Creation
Create a child Site when:
- A named internal unit exists within a preserve
- A named natural area, management zone, or recreation area is documented
- A named trail area, overlook area, or habitat unit is identity-bearing

Do not surface:
- Unnamed amenities
- Unnamed management zones
- Stewardship work areas

## 7.3 Trail Creation
Surface a Trail when:
- A named trail appears on nonprofit maps or brochures
- A named trail appears in partnership announcements
- A named trail appears in county GIS

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `urls_raw` for all discovered map URLs.

## 7.4 Trail Segment Creation
Surface Trail Segments when:
- Segment-level geometry exists in county GIS
- Segment identifiers appear in nonprofit maps

## 7.5 Trail Network Creation
Surface a Trail Network when:
- A nonprofit manages a multi-trail system
- A greenway corridor includes multiple Trails

## 7.6 Site Network Creation
Surface a Site Network when:
- A nonprofit manages a multi-site conservation system
- A watershed-scale or corridor-scale network is documented

## 7.7 Access Point Creation
Surface an Access Point when:
- It appears on nonprofit maps
- It appears in nonprofit brochures
- It appears in county GIS
- It appears in partnership announcements

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.

------------------------------------------------------------
# 8. TIER-SPECIFIC EXPECTATIONS

Tier 7 must surface:
- All fee-simple preserves
- All identity-bearing conservation easements
- All nonprofit-managed Trails
- All nonprofit-managed Trail Segments
- All nonprofit-managed Access Points
- All named trail corridors and greenways
- All multi-site conservation systems
- All organizations referenced in partnership mentions from Tiers 1–6

Tier 7 may surface:
- Nonprofit-managed Trail Networks
- Nonprofit-managed Site Networks
- Watershed-scale or corridor-scale systems
- Partnership lands (if identity-bearing)

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

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 10. OUTPUT REQUIREMENTS

Each nonprofit entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- The appropriate Schema Module v5.x
- The appropriate Vocabulary Module v5.x

No normalized fields may appear in Tier 7 output.

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
# END OF CONSERVANCY & LAND TRUST DISCOVERY SUB-PROCEDURE v5.6
