# NATURAL AREAS PROJECT — FEDERAL & TRIBAL LANDS DISCOVERY SUB‑PROCEDURE v3.2.2  
(USFS, NPS, USFWS, USACE, BLM, DoD, Tribal Lands)

Tier 1 of the **Discovery Protocol Module v3.2.2**.

Federal and tribal lands must be discovered using authoritative federal datasets and  
county‑anchored verification. Ohio contains several types of federal lands—National  
Forest, National Wildlife Refuges, National Park units, USACE reservoirs, and DoD  
installations—but these are unevenly distributed across the state.  

Ohio has **no federally recognized tribal reservations or trust lands**, but tribal  
cultural sites and tribal fee‑simple ownership may exist.  

This module defines the **authoritative, deterministic rules** for Tier 1 discovery  
across all six entity types.

------------------------------------------------------------
# 1. PURPOSE

This sub‑procedure defines how the system must:

- Identify all federal Sites  
- Identify tribal lands and tribal ownership  
- Identify tribal cultural Sites  
- Identify Trails, Trail Segments, and Trail Networks on federal lands  
- Identify **child Sites** within federal Sites (Sites with Parent Site populated)  
- Identify Access Points associated with federal or tribal Sites  
- Distinguish federal management from state/local co‑management  
- Avoid false positives from similarly named places  
- Log uncertainty and boundary cases  
- Produce Raw Candidate Records and Discovery Metadata v3.2.2  

This module is referenced **only** by the Discovery Protocol Module v3.2.2.

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

It governs discovery of:

- **Sites** (federal or tribal)  
- **Child Sites**  
- **Trails**  
- **Trail Segments**  
- **Trail Networks**  
- **Site Networks**  
- **Access Points**  

This tier sits **above State** and is the highest tier in the discovery hierarchy.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 U.S. Forest Service (USFS)
Ohio’s only National Forest: **Wayne National Forest**

Check for:
- Forest boundary datasets  
- Recreation areas → Sites or child Sites  
- Trailheads → Access Points  
- Campgrounds → child Sites or Access Points  
- Special management areas → child Sites  
- USFS recreation maps  
- USFS trail datasets → Trails, Trail Segments  

## 3.2 National Park Service (NPS)
Check for all NPS unit types:
- National Parks  
- National Historical Parks  
- National Monuments  
- National Memorials  
- National Historic Sites  
- National Battlefields  
- National Heritage Areas → Site Networks  

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

All sources must be logged in **Discovery Metadata v3.2.2**.

------------------------------------------------------------
# 4. FEDERAL & TRIBAL DISCOVERY CONDITIONS

## 4.1 Tribal Trust Lands
- Check federal tribal land registries  
- If none found → record “None in Ohio” in metadata  

## 4.2 Tribal Reservations
- Check BIA datasets  
- If none found → record “None in Ohio” in metadata  

## 4.3 Tribal Fee‑Simple Ownership
Check county auditor / GIS for parcels owned by:
- Federally recognized tribes  
- Tribal corporations  
- Tribal cultural organizations  

If found → record as a **Site**, with tribal classification stored in metadata.

## 4.4 Tribal Cultural Sites
These are **not tribal lands**, but may be relevant:
- Mound sites  
- Archaeological sites  
- Cultural landscapes  
- Burial grounds  

Record as **Sites**, with “Cultural Site — not tribal land” stored in metadata.

------------------------------------------------------------
# 5. TIER‑ANCHORED VERIFICATION (MANDATORY)

## 5.1 Confirm Boundaries
- Verify the feature lies within the county  
- **Record all counties in `counties_raw`**  
- **Do NOT segment multi‑county entities**  

## 5.2 Confirm Management Authority
Record:
- Federal agency  
- State co‑management  
- Local co‑management  

## 5.3 Confirm Access Points
Identify:
- Boat ramps  
- Trailheads  
- Scenic overlooks  
- Recreation areas  
- Parking areas  

Access Points must be surfaced as **Access Point candidates** and passed to the  
**Access Point Discovery Sub‑Procedure v3.2.2**.

## 5.4 Naming
Record names **exactly as discovered**.  
If multiple names appear → record all in metadata.

------------------------------------------------------------
# 6. DECISION RULES FOR ENTITY CREATION

### 6.1 Site Creation
A federal or tribal feature becomes a **Site** if:
- Federally owned or federally managed  
- Identity‑bearing (named, mapped, or designated)  
- Public access or recreation infrastructure exists  
- It influences Access Point logic  

Exclude:
- Federal office buildings  
- Federal courthouses  
- Post offices  
- BLM mineral rights with no surface access  
- DoD administrative buildings  

### 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a federal Site  
- A recreation area, campground, or management area is identity‑bearing  
- A special management zone is documented  

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
# 7. TIER‑SPECIFIC EXPECTATIONS

The Federal Tier **must** surface:
- All federal Sites  
- All tribal Sites (if any)  
- All child Sites within federal Sites  
- All federal Trails  
- All federal Trail Segments  
- All federally designated Trail Networks  
- All federal Site Networks  
- All federal or tribal Access Points  
- All tribal cultural Sites  

The Federal Tier **may** surface:
- BLM mineral rights Sites (if identity‑bearing)  
- DoD recreation areas (if public access exists)  
- Federal easements (if identity‑bearing)  

The Federal Tier **must not** surface:
- Administrative buildings  
- Non‑public federal facilities  
- Non‑identity‑bearing parcels  
- Tribal cultural Sites as tribal land  

------------------------------------------------------------
# 8. LOGGING REQUIREMENTS

Each discovered entity must include:
- Full **Discovery Metadata v3.2.2**  
- All raw source references  
- All counties (raw)  
- All conflicts and uncertainties  
- All parent relationships (for child Sites and Access Points)  
- All geometry (if available)  

All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each federal or tribal entity must output a **Raw Candidate Record** conforming to:
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- The appropriate Schema Module v3.2.2  
- The appropriate Vocabulary Module v3.2.2  

No normalized fields may appear in Tier 1 output.

------------------------------------------------------------
# 10. INTEGRATION POINTS

This module integrates with:
- **Discovery Protocol Module v3.2.2**  
- **Discovery Orchestration Module v3.2.2**  
- **Site Discovery Sub‑Procedure v3.2.2**  
- **Trail Discovery Sub‑Procedure v3.2.2**  
- **Trail Segment Discovery Sub‑Procedure v3.2.2**  
- **Trail Network Discovery Sub‑Procedure v3.2.2**  
- **Site Network Discovery Sub‑Procedure v3.2.2**  
- **Access Point Discovery Sub‑Procedure v3.2.2**  
- **Child Site Rules Module v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- **Discovery Output Specification v3.2.2**  
- **Normalization Contracts v3.2.2**  
- **Resolution Module v3.2.2**  
- **TSV Output Specifications v3.2.2**  
- **Audit & Logging Module v3.2.2**  
- **County Baseline Module v3.2.2**  

No other module may reference this sub‑procedure directly.

------------------------------------------------------------
# 11. VERSIONING

- This module is **Federal & Tribal Lands Discovery Sub‑Procedure v3.2.2**.  
- Updates to federal datasets or tribal registries may result in v3.3, v3.4, etc.  
- Any change to tier order or workflow must be made in the  
  **Discovery Protocol Module v3.2.2**.

------------------------------------------------------------
# END OF FEDERAL & TRIBAL LANDS DISCOVERY SUB‑PROCEDURE v3.2.2