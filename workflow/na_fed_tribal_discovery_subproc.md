# FEDERAL & TRIBAL LANDS DISCOVERY SUB‑PROCEDURE v3.1
(USFS, NPS, USFWS, USACE, BLM, DoD, Tribal Lands)

Tier 1 of the Discovery Protocol Module v3.1.

Federal and tribal lands must be discovered using authoritative federal datasets and
county‑anchored verification. Ohio contains several types of federal lands (National
Forest, National Wildlife Refuges, National Park units, USACE reservoirs, DoD
installations), but these are unevenly distributed across the state.

Ohio has **no federally recognized tribal reservations or trust lands**, but tribal
cultural sites and tribal fee‑simple ownership may exist.

This module defines the **detailed rules** for Tier 1 discovery across all seven
entity types.

------------------------------------------------------------
# 1. PURPOSE
This sub‑procedure defines how the system must:

- Identify all federal Sites
- Identify tribal lands and tribal ownership
- Identify tribal cultural sites
- Identify Trails, Trail Segments, and Trail Networks on federal lands
- Identify Sub‑Sites within federal Sites
- Identify Access Points associated with federal or tribal Sites
- Distinguish federal management from state/local co‑management
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Candidate Records and Discovery Metadata

This module is referenced **only** by the Discovery Protocol Module v3.1.

------------------------------------------------------------
# 2. SCOPE
This sub‑procedure applies to:

- U.S. Forest Service (USFS)
- National Park Service (NPS)
- U.S. Fish & Wildlife Service (USFWS)
- U.S. Army Corps of Engineers (USACE)
- Bureau of Land Management (BLM)
- Department of Defense (DoD)
- Tribal trust land registries
- Tribal fee‑simple ownership
- Tribal cultural sites

It governs the discovery of:

- **Sites** (federal or tribal)
- **Sub‑Sites** within federal Sites
- **Trails** on federal lands
- **Trail Segments** on federal lands
- **Trail Networks** (if federally designated)
- **Site Networks** (e.g., National Heritage Areas)
- **Access Points** associated with federal or tribal Sites

------------------------------------------------------------
# 3. REQUIRED FEDERAL SOURCES (ALL MANDATORY)

## 3.1 U.S. Forest Service (USFS)
Ohio’s only National Forest: **Wayne National Forest**

Required checks:
- Forest boundary datasets
- Recreation areas (→ Sites or Sub‑Sites)
- Trailheads (→ Access Points)
- Campgrounds (→ Sub‑Sites or Access Points)
- Special management areas (→ Sub‑Sites)
- USFS recreation maps
- USFS trail datasets (→ Trails, Trail Segments)

## 3.2 National Park Service (NPS)
Check for all NPS unit types:
- National Parks
- National Historical Parks
- National Monuments
- National Memorials
- National Historic Sites
- National Battlefields
- National Heritage Areas (→ Site Networks)

Required sources:
- NPS unit pages
- NPS boundary datasets
- NPS recreation maps
- NPS trail datasets

## 3.3 U.S. Fish & Wildlife Service (USFWS)
Check for:
- National Wildlife Refuges
- Waterfowl Production Areas
- Conservation easements
- Refuge‑managed access points

Required sources:
- USFWS refuge pages
- USFWS boundary datasets
- USFWS recreation maps
- USFWS trail datasets

## 3.4 U.S. Army Corps of Engineers (USACE)
Check for:
- Reservoirs
- Flood control lands
- Recreation areas
- Boat ramps
- Campgrounds
- Trails

Required sources:
- USACE project pages
- USACE recreation maps
- USACE facility datasets

## 3.5 Bureau of Land Management (BLM)
Ohio has:
- Minimal BLM mineral rights holdings
- No BLM recreation areas
- No BLM surface‑managed lands

Still required:
- BLM parcel datasets
- BLM easement datasets
- BLM mineral rights datasets

## 3.6 Department of Defense (DoD)
Check for:
- Military bases
- Training areas
- Formerly Used Defense Sites (FUDS)
- Restricted lands

Required sources:
- DoD installation datasets
- FUDS datasets
- DoD environmental restoration maps

------------------------------------------------------------
# 4. TRIBAL LAND DISCOVERY

Ohio has **no federally recognized tribal reservations or trust lands**, but the system must still check:

## 4.1 Tribal Trust Lands
- Check federal tribal land registries
- If none found → record “None in Ohio”

## 4.2 Tribal Reservations
- Check BIA datasets
- If none found → record “None in Ohio”

## 4.3 Tribal Fee‑Simple Ownership
Check county auditor / GIS for parcels owned by:
- Federally recognized tribes
- Tribal corporations
- Tribal cultural organizations

If found → record as **Site: Tribal Land (Fee‑Simple)**.

## 4.4 Tribal Cultural Sites
These are **not tribal lands**, but may be relevant:
- Mound sites
- Archaeological sites
- Cultural landscapes
- Burial grounds

Record as:
**“Cultural Site — not tribal land”**
unless ownership indicates otherwise.

------------------------------------------------------------
# 5. COUNTY‑ANCHORED VERIFICATION (MANDATORY)

For each federal or tribal entity identified, the system must verify:

## 5.1 Parcel Boundaries
- Confirm the entity lies within the county
- Segment multi‑county Sites by county

## 5.2 Management Authority
Record:
- Federal
- State co‑management
- Local co‑management

## 5.3 Access Points
Identify:
- Boat ramps
- Trailheads
- Scenic overlooks
- Recreation areas
- Parking areas

Access Points must be surfaced as **Access Point candidates** and passed to the
Access Point Discovery Sub‑Procedure v3.1.

## 5.4 Naming Consistency
Use the **federal name** as the authoritative name.

------------------------------------------------------------
# 6. DECISION RULES FOR ENTITY CREATION

### 6.1 Site Creation
A federal or tribal feature becomes a **Site** if:
- It is federally owned or federally managed
- It is identity‑bearing (named, mapped, or designated)
- It has public access or recreation infrastructure
- It influences Access Point logic

Exclude:
- Federal office buildings
- Federal courthouses
- Post offices
- BLM mineral rights with no surface access
- DoD administrative buildings

### 6.2 Sub‑Site Creation
Create a **Sub‑Site** when:
- A named internal unit exists within a federal Site
- A recreation area, campground, or management area is identity‑bearing

### 6.3 Trail Creation
Create a **Trail** when:
- A named trail appears in federal datasets or maps

### 6.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment‑level geometry or identifiers exist

### 6.5 Trail Network Creation
Create a **Trail Network** when:
- A federally designated multi‑trail system exists (e.g., North Country Trail)

### 6.6 Site Network Creation
Create a **Site Network** when:
- A National Heritage Area or similar multi‑site federal designation exists

### 6.7 Access Point Creation
Create an **Access Point** when:
- A visitor‑facing entry location is documented

------------------------------------------------------------
# 7. LOGGING REQUIREMENTS

For each federal or tribal entity, log:
- Agency
- Entity name
- Entity type (Site, Sub‑Site, Trail, Trail Segment, Trail Network, Site Network)
- County
- Source dataset
- URL or reference
- Access type (if applicable)
- Notes on co‑management
- Discovery Tier: **1**
- Uncertainty or conflicts

Each county must also produce:
- Federal Sites Found
- Tribal Lands Found
- Tribal Cultural Sites
- Trails Found
- Trail Segments Found
- Trail Networks Found
- Site Networks Found
- Access Points Found
- Sources Checked
- Notes

------------------------------------------------------------
# 8. OUTPUT FORMAT

### 8.1 Federal or Tribal Entities
Name:
Type: Site / Sub‑Site / Trail / Trail Segment / Trail Network / Site Network / Tribal Land / Tribal Cultural Site
Agency:
County:
URL or Source:
Notes:
Discovery Tier: 1

### 8.2 Access Points
Name:
Type: Access Point
Access Point Type (raw):
Parent Entity:
County:
Source:
Notes:
Discovery Tier: 1

------------------------------------------------------------
# 9. INTEGRATION POINTS

This module integrates with:
- Discovery Protocol Module v3.1
- Site Discovery Sub‑Procedure v3.1
- Sub‑Site Discovery Sub‑Procedure v1
- Trail Discovery Sub‑Procedure v1
- Trail Segment Discovery Sub‑Procedure v1
- Trail Network Discovery Sub‑Procedure v1
- Site Network Discovery Sub‑Procedure v1
- Access Point Discovery Sub‑Procedure v3.1
- Discovery Metadata Specification v1.0
- Audit & Logging Module v1.1
- County Baseline Module v1.1
- Resolution Module v1

No other module may reference this sub‑procedure directly.

------------------------------------------------------------
# 10. VERSIONING
- This module is **Federal & Tribal Lands Discovery Sub‑Procedure v3.1**.
- Updates to federal datasets or tribal registries may result in v3.2, v3.3, etc.
- Any change to tier order or high‑level workflow must be made in the Discovery Protocol Module v3.1.

------------------------------------------------------------
# END OF FEDERAL & TRIBAL LANDS DISCOVERY SUB‑PROCEDURE v3.1