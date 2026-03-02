# NATURAL AREAS PROJECT
# CONSERVANCY & LAND TRUST DISCOVERY SUB-PROCEDURE v5.2
(Tier 7 — Land Trusts, Conservancies, Foundations, Trail Alliances, Greenway Coalitions, Watershed Nonprofits)

This module defines the authoritative, deterministic Tier-7 discovery rules for
nonprofit conservation landholders within the v5.x Raw → Resolution → Normalization →
Entity Graph pipeline.

This module supersedes Conservancy & Land Trust Discovery Sub-Procedure v5.0.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Updated all cross-module references to v5.x
- Updated header version to v5.2

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **OBS-024**: Trail coalition disambiguation added to §2.2 and new §4.7 — trail
  alliances that maintain trails are NOT the owner/manager; ownership must be
  confirmed before creating a Tier-7 entity
- **OBS-025**: Grant-confirmed preserve status flag added to §6.1 — preserves confirmed
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
See §4.7 for detailed disambiguation rules.

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
# 4. NONPROFIT LAND DISCOVERY CONDITIONS

## 4.1 Fee-Simple Ownership
Surface as a Site if:
- Owned by the nonprofit
- Identity-bearing (named, mapped, or designated)
- Public access exists OR the preserve is clearly named/mapped

## 4.2 Conservation Easements
Surface as a Site if:
- Public access exists, OR
- The easement is identity-bearing, OR
- It contains Trails, overlooks, or Access Points

Exclude:
- Private easements with no public access
- Agricultural easements with no recreation role
- Scenic easements with no access or identity

## 4.3 Trail Corridors & Linear Preserves
Surface as Sites if:
- Named
- Mapped
- Identity-bearing
- Have one or more Access Points

## 4.4 Multi-County Holdings
- Do not segment multi-county Sites
- Record all counties exactly as discovered in `counties_raw`

## 4.5 Co-Managed Sites
Nonprofits frequently co-manage Sites with:
- Park districts
- Counties
- Municipalities
- State or federal agencies

Record all governance details in metadata; do not attempt to resolve conflicts.

## 4.6 Stewardship-Only Lands
Exclude if:
- Nonprofit is only a stewardship partner
- No ownership, easement, or identity-bearing role exists

## 4.7 Trail Coalition vs. Trail Owner Disambiguation
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
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 7 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Enumerate:
- Preserve listings
- Protected land listings
- Trail listings
- Project listings
- Map index pages
- Conservation area directories

Always **fetch** listing pages directly — do not rely on search snippets.
Extract ALL entities listed, not just prominently featured ones.

## 5.2 Recursive Discovery (URL Propagation)
Follow internal links for:
- Trails
- Maps
- Access
- Stewardship details
- Habitat units
- Management zones

Respect recursion limits and allowlists.

------------------------------------------------------------
# 6. ENTITY CREATION RULES

## 6.1 Site Creation
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

## 6.2 Child Site Creation
Create a child Site when:
- A named internal unit exists within a preserve
- A named natural area, management zone, or recreation area is documented
- A named trail area, overlook area, or habitat unit is identity-bearing

Do not surface:
- Unnamed amenities
- Unnamed management zones
- Stewardship work areas

## 6.3 Trail Creation
Surface a Trail when:
- A named trail appears on nonprofit maps or brochures
- A named trail appears in partnership announcements
- A named trail appears in county GIS

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `urls_raw` for all discovered map URLs.

## 6.4 Trail Segment Creation
Surface Trail Segments when:
- Segment-level geometry exists in county GIS
- Segment identifiers appear in nonprofit maps

## 6.5 Trail Network Creation
Surface a Trail Network when:
- A nonprofit manages a multi-trail system
- A greenway corridor includes multiple Trails

## 6.6 Site Network Creation
Surface a Site Network when:
- A nonprofit manages a multi-site conservation system
- A watershed-scale or corridor-scale network is documented

## 6.7 Access Point Creation
Surface an Access Point when:
- It appears on nonprofit maps
- It appears in nonprofit brochures
- It appears in county GIS
- It appears in partnership announcements

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.

------------------------------------------------------------
# 7. TIER-SPECIFIC EXPECTATIONS

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
# 8. METADATA REQUIREMENTS

Each discovered entity must include:

- Full **Discovery Metadata v5.x**
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships
- All geometry (if available)
- `features_raw` for Sites and Access Points (if documented)
- `difficulty_raw` and `accessibility_raw` for Trails and Trail Segments (if explicitly stated)
- `urls_raw` for Trails, Trail Segments, Trail Networks, and Site Networks (map URLs included)

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each nonprofit entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- The appropriate Schema Module v5.x
- The appropriate Vocabulary Module v5.x

No normalized fields may appear in Tier 7 output.

------------------------------------------------------------
# 10. INTEGRATION POINTS

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
# 11. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.x
- Discovery Output Specification v5.x
- Discovery Metadata Specification v5.x
- All six entity Discovery Sub-Procedures v5.x
- Child Site Rules Module v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF CONSERVANCY & LAND TRUST DISCOVERY SUB-PROCEDURE v5.2
