# NATURAL AREAS PROJECT
# CONSERVANCY & LAND TRUST DISCOVERY SUB‑PROCEDURE v4.0
(Tier 7 — Land Trusts, Conservancies, Foundations, Trail Alliances, Greenway Coalitions, Watershed Nonprofits)

This module defines the authoritative, deterministic Tier‑7 discovery rules for nonprofit conservation landholders within the v4.0 Raw → Resolution → Normalization → Entity Graph pipeline.

It supersedes all v3.x nonprofit discovery logic and is fully aligned with:

- Discovery Protocol Module v4.0
- Discovery Metadata Specification v4.0
- Tier Sub‑Procedure Template v4.0
- Discovery Orchestration Module v4.0

This module contains no controlled vocabularies.  
All vocabularies are defined in the appropriate v4.0 Vocabulary Modules.

------------------------------------------------------------
# 1. PURPOSE

The Conservancy & Land Trust Discovery Sub‑Procedure v4.0 defines how Tier 7 must:

- Identify all nonprofit‑owned or nonprofit‑managed Sites
- Identify child Sites within preserves (Sites with Parent Site populated)
- Identify Trails, Trail Segments, and Trail Networks on nonprofit holdings
- Identify Site Networks (multi‑site conservation systems)
- Identify Access Points associated with nonprofit holdings
- Identify fee‑simple preserves and identity‑bearing conservation easements
- Identify trail corridors, greenways, and linear preserves
- Distinguish public‑access vs. non‑public‑access holdings
- Identify co‑managed Sites and partnership lands
- Handle multi‑organization stewardship and cross‑tier overlaps
- Log uncertainty, conflicts, and boundary cases
- Produce Raw Discovery Records v4.0
- Produce Discovery Metadata v4.0

This module is referenced only by:

- Discovery Protocol Module v4.0
- Discovery Orchestration Module v4.0
- Tier Sub‑Procedure Template v4.0

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to all nonprofit conservation organizations, including:

## 2.1 Land Trusts & Conservancies
- Local, regional, statewide, and national land trusts
- Conservancies and conservation foundations
- Habitat and ecological stewardship organizations

## 2.2 Trail & Greenway Organizations
- Trail alliances
- Greenway coalitions
- Linear corridor nonprofits
- Regional trail partnerships

## 2.3 Watershed & Habitat Organizations
- Watershed groups
- Habitat restoration nonprofits
- River corridor organizations

## 2.4 Conservation Networks
- Land trust consortiums
- Regional conservation partnerships
- Multi‑organization stewardship coalitions

Tier 7 governs discovery of:

- Sites
- Child Sites
- Trails
- Trail Segments
- Trail Networks
- Site Networks
- Access Points

Tier 7 sits below Municipal and above Private & Organization‑Based.

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

Scan all:
- Preserve pages
- Project pages
- Maps
- PDF brochures
- Stewardship reports
- Annual reports (if they list preserves or trails)

## 3.2 Land Trust Alliance (LTA) Directory
Check for:
- Member organizations
- Regional affiliates
- Contact information
- Links to official websites

## 3.3 County Auditor / GIS (Parcel Verification)
Nonprofit holdings may appear as:
- Fee‑simple parcels
- Conservation easements
- Trail easements
- Partnership lands

GIS is required for:
- County boundary confirmation
- Ownership confirmation
- Easement verification
- Access point verification
- Multi‑county boundary detection

## 3.4 Statewide & Regional Conservation Networks
Check:
- ONAPA
- Regional conservation partnerships
- Watershed groups
- Greenway coalitions
- Corridor‑scale conservation initiatives

## 3.5 Federal & State Partners
Nonprofits often partner with:
- ODNR
- USFWS
- USACE
- Park districts
- Counties
- Municipalities

All partnerships must be logged in metadata.

------------------------------------------------------------
# 4. NONPROFIT LAND DISCOVERY CONDITIONS

## 4.1 Fee‑Simple Ownership
Surface as a Site if:
- Owned by the nonprofit
- Identity‑bearing (named, mapped, or designated)
- Public access exists OR the preserve is clearly named/mapped

## 4.2 Conservation Easements
Surface as a Site if:
- Public access exists, OR
- The easement is identity‑bearing, OR
- It contains Trails, overlooks, or Access Points

Exclude:
- Private easements with no public access
- Agricultural easements with no recreation role
- Scenic easements with no access or identity

## 4.3 Trail Corridors & Linear Preserves
Surface as Sites if:
- Named
- Mapped
- Identity‑bearing
- Have one or more Access Points

## 4.4 Multi‑County Holdings
- Do not segment multi‑county Sites
- Record all counties exactly as discovered in `counties_raw`

## 4.5 Co‑Managed Sites
Nonprofits frequently co‑manage Sites with:
- Park districts
- Counties
- Municipalities
- State or federal agencies

Record all governance details in metadata; do not resolve conflicts.

## 4.6 Stewardship‑Only Lands
Exclude if:
- Nonprofit is only a stewardship partner
- No ownership, easement, or identity‑bearing role exists

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

Extract all first‑level entity URLs.

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
- Fee‑simple ownership
- Public‑access conservation easement
- Identity‑bearing easement
- Named trail corridor or greenway
- Appears on nonprofit website or GIS
- Appears in partnership announcements

Exclude:
- Administrative offices
- Stewardship centers not open to the public
- Private easements with no identity‑bearing role

## 6.2 Child Site Creation
Create a child Site when:
- A named internal unit exists within a preserve
- A named natural area, management zone, or recreation area is documented
- A named trail area, overlook area, or habitat unit is identity‑bearing

Do not surface:
- Unnamed amenities
- Unnamed management zones
- Stewardship work areas

## 6.3 Trail Creation
Surface a Trail when:
- A named trail appears on nonprofit maps or brochures
- A named trail appears in partnership announcements
- A named trail appears in county GIS

## 6.4 Trail Segment Creation
Surface Trail Segments when:
- Segment‑level geometry exists in county GIS
- Segment identifiers appear in nonprofit maps

## 6.5 Trail Network Creation
Surface a Trail Network when:
- A nonprofit manages a multi‑trail system
- A greenway corridor includes multiple Trails

## 6.6 Site Network Creation
Surface a Site Network when:
- A nonprofit manages a multi‑site conservation system
- A watershed‑scale or corridor‑scale network is documented

## 6.7 Access Point Creation
Surface an Access Point when:
- It appears on nonprofit maps
- It appears in nonprofit brochures
- It appears in county GIS
- It appears in partnership announcements

Access Points must include raw:
- Name or descriptive label
- Access Point Type
- County list
- Parent entity
- Sources
- Notes

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

Tier 7 must surface:
- All fee‑simple preserves
- All identity‑bearing conservation easements
- All nonprofit‑managed Trails
- All nonprofit‑managed Trail Segments
- All nonprofit‑managed Access Points
- All named trail corridors and greenways
- All multi‑site conservation systems

Tier 7 may surface:
- Nonprofit‑managed Trail Networks
- Nonprofit‑managed Site Networks
- Watershed‑scale or corridor‑scale systems
- Partnership lands (if identity‑bearing)

------------------------------------------------------------
# 8. METADATA REQUIREMENTS

Each discovered entity must include:
- Full Discovery Metadata v4.0
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships
- All geometry (if available)

All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each nonprofit entity must output:
- Raw Discovery Record v4.0
- Discovery Metadata v4.0
- Schema Module v4.0 compliance
- Vocabulary Module v4.0 compliance

Discovery must not:
- Normalize
- Correct
- Dedupe
- Infer
- Invent
- Silently modify

------------------------------------------------------------
# 10. INTEGRATION POINTS

Integrates with:
- Discovery Protocol Module v4.0
- Discovery Orchestration Module v4.0
- Tier Sub‑Procedure Template v4.0
- All Entity Discovery Sub‑Procedures v4.0
- Child Site Rules Module v4.0
- Discovery Metadata Specification v4.0
- Discovery Output Specification v4.0
- Normalization Engine v4.0
- Resolution Engine v4.0
- Entity Upsert Engine v4.0
- TSV Output Specifications v4.0
- Audit & Logging Module v4.0
- County Baseline Module v4.0

------------------------------------------------------------
# 11. VERSIONING

- This module is Conservancy & Land Trust Discovery Sub‑Procedure v4.0.
- Updates to land trust directories or conservation practices may result in v4.1, v4.2, etc.
- Tier order changes must be made in the Discovery Protocol Module v4.0.

------------------------------------------------------------
# END OF CONSERVANCY & LAND TRUST DISCOVERY SUB‑PROCEDURE v4.0