# NATURAL AREAS PROJECT
# FEDERAL & TRIBAL LANDS DISCOVERY SUB‑PROCEDURE v4.0
(Tier 1 — U.S. Federal Agencies & Tribal Lands)

This module defines the authoritative, deterministic Tier‑1 discovery rules for
federal and tribal lands within the v4.0 Raw → Resolution → Normalization →
Entity Graph pipeline.

This document supersedes all v3.x federal/tribal discovery logic.  
It introduces enumerative + recursive discovery, raw‑layer output, and
provenance‑driven extraction.

This module contains no controlled vocabularies.  
All vocabularies are defined in the appropriate v4.0 Vocabulary Modules.

------------------------------------------------------------
# 1. PURPOSE

The Federal & Tribal Lands Discovery Sub‑Procedure v4.0 defines how Tier 1 must:

- Identify all federal Sites  
- Identify tribal lands, tribal ownership, and tribal cultural Sites  
- Identify Trails, Trail Segments, and Trail Networks on federal lands  
- Identify child Sites within federal Sites  
- Identify Access Points associated with federal or tribal Sites  
- Distinguish federal management from state/local co‑management  
- Avoid false positives from similarly named places  
- Log uncertainty and boundary cases  
- Produce Raw Discovery Records v4.0  
- Produce Discovery Metadata v4.0  

This module is referenced only by:

- Discovery Protocol Module v4.0  
- Discovery Orchestration Module v4.0  
- Tier Sub‑Procedure Template v4.0  

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to all federal agencies and tribal land categories:

- U.S. Forest Service (USFS)  
- National Park Service (NPS)  
- U.S. Fish & Wildlife Service (USFWS)  
- U.S. Army Corps of Engineers (USACE)  
- Bureau of Land Management (BLM)  
- Department of Defense (DoD)  
- Tribal trust land registries  
- Tribal fee‑simple ownership  
- Tribal cultural Sites  

It governs discovery of:

- Sites (federal or tribal)  
- Child Sites  
- Trails  
- Trail Segments  
- Trail Networks  
- Site Networks  
- Access Points  

Tier 1 is the highest‑authority tier in the discovery hierarchy.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 1 must enumerate and recursively explore the following authoritative sources.

## 3.1 U.S. Forest Service (USFS)
Ohio’s only National Forest: **Wayne National Forest**

Required sources:
- Forest boundary datasets  
- Recreation area pages  
- USFS trail datasets  
- USFS recreation maps  
- Special management area datasets  
- Campground datasets  
- Trailhead datasets  

## 3.2 National Park Service (NPS)
Required sources:
- NPS unit pages  
- NPS boundary datasets  
- NPS recreation maps  
- NPS trail datasets  
- National Heritage Area documentation  

## 3.3 U.S. Fish & Wildlife Service (USFWS)
Required sources:
- Refuge pages  
- Refuge boundary datasets  
- USFWS recreation maps  
- USFWS trail datasets  
- Waterfowl Production Area datasets  

## 3.4 U.S. Army Corps of Engineers (USACE)
Required sources:
- USACE project pages  
- USACE recreation maps  
- USACE facility datasets  
- Boat ramp datasets  
- Campground datasets  

## 3.5 Bureau of Land Management (BLM)
Ohio has minimal BLM surface holdings.

Required sources:
- BLM parcel datasets  
- BLM easement datasets  
- BLM mineral rights datasets  

## 3.6 Department of Defense (DoD)
Required sources:
- DoD installation datasets  
- FUDS datasets  
- DoD environmental restoration maps  

All sources must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 4. DOMAIN RULES FOR FEDERAL & TRIBAL DISCOVERY

## 4.1 Tribal Trust Lands
- Check federal tribal land registries.  
- If none exist in Ohio → record “None in Ohio” in metadata.  

## 4.2 Tribal Reservations
- Check BIA datasets.  
- If none exist in Ohio → record “None in Ohio” in metadata.  

## 4.3 Tribal Fee‑Simple Ownership
Check county auditor / GIS for parcels owned by:
- Federally recognized tribes  
- Tribal corporations  
- Tribal cultural organizations  

If found → record as a **Site**, with tribal classification in metadata.

## 4.4 Tribal Cultural Sites
These are **not tribal lands**, but must be discovered:
- Mound sites  
- Archaeological sites  
- Cultural landscapes  
- Burial grounds  

Record as **Sites**, with metadata noting “Cultural Site — not tribal land.”

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 1 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Tier 1 must enumerate:
- All federal unit listing pages  
- All recreation area listings  
- All trail listings  
- All facility listings  
- All boundary datasets  

## 5.2 Recursive Discovery (URL Propagation)
Tier 1 must recursively follow:
- Internal links within federal domains  
- Internal links within tribal registries  
- Internal links within USACE project pages  

Recursion must stop when:
- The domain is not on the allowlist  
- The page is not relevant to Sites, Trails, or Access Points  
- The page is a non‑recreational administrative page  

## 5.3 Recursion Allowlist
- *.nps.gov  
- *.fs.usda.gov  
- *.fws.gov  
- *.usace.army.mil  
- *.blm.gov  
- *.defense.gov  
- *.bia.gov  

------------------------------------------------------------
# 6. ENTITY CREATION RULES (TIER‑SPECIFIC)

### 6.1 Site Creation
Create a **Site** when:
- Federally owned or federally managed  
- Identity‑bearing (named, mapped, or designated)  
- Public access or recreation infrastructure exists  
- It influences Access Point logic  

Exclude:
- Federal office buildings  
- Courthouses  
- Post offices  
- Non‑recreational DoD facilities  
- BLM mineral rights with no surface access  

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

Tier 1 **must** surface:
- All federal Sites  
- All tribal Sites (if any)  
- All child Sites within federal Sites  
- All federal Trails  
- All federal Trail Segments  
- All federally designated Trail Networks  
- All federal Site Networks  
- All federal or tribal Access Points  
- All tribal cultural Sites  

Tier 1 **may** surface:
- BLM mineral rights Sites (if identity‑bearing)  
- DoD recreation areas (if public access exists)  
- Federal easements (if identity‑bearing)  

Tier 1 **must not** surface:
- Administrative buildings  
- Non‑public federal facilities  
- Non‑identity‑bearing parcels  
- Tribal cultural Sites as tribal land  

------------------------------------------------------------
# 8. METADATA REQUIREMENTS

Each discovered entity must include:

- Full **Discovery Metadata v4.0**  
- All raw source references  
- All counties (raw)  
- All conflicts and uncertainties  
- All parent relationships (for child Sites and Access Points)  
- All geometry (if available)  

All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each federal or tribal entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v4.0**  
- **Discovery Metadata Specification v4.0**  
- The appropriate Schema Module v4.0  
- The appropriate Vocabulary Module v4.0  

No normalized fields may appear in Tier 1 output.

------------------------------------------------------------
# 10. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v4.0  
- Discovery Orchestration Module v4.0  
- Tier Sub‑Procedure Template v4.0  
- All Entity Discovery Sub‑Procedures v4.0  
- Child Site Rules Module v4.0  
- Discovery Metadata Specification v4.0  
- Discovery Output Specification v4.0  
- Resolution Engine v4.0  
- Normalization Engine v4.0  
- TSV Output Specifications v4.0  
- Audit & Logging Module v4.0  
- County Baseline Module v4.0  

------------------------------------------------------------
# 11. VERSIONING

- This module is **Federal & Tribal Lands Discovery Sub‑Procedure v4.0**.  
- Updates to federal datasets or tribal registries may result in v4.1, v4.2, etc.  
- Any change to tier order or workflow must be made in the Discovery Protocol Module v4.0.

------------------------------------------------------------
# END OF FEDERAL & TRIBAL LANDS DISCOVERY SUB‑PROCEDURE v4.0