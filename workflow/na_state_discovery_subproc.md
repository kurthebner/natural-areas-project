# NATURAL AREAS PROJECT
# STATE LANDS DISCOVERY SUB‑PROCEDURE v4.0
(Tier 2 — ODNR Divisions, OHC, ODOT, State Easements, Scenic Rivers)

This module defines the authoritative, deterministic Tier‑2 discovery rules for
state‑managed and state‑affiliated lands within the v4.0 Raw → Resolution →
Normalization → Entity Graph pipeline.

This document supersedes all v3.x state‑tier discovery logic.

This module contains no controlled vocabularies.  
All vocabularies are defined in the appropriate v4.0 Vocabulary Modules.

------------------------------------------------------------
# 1. PURPOSE

The State Lands Discovery Sub‑Procedure v4.0 defines how Tier 2 must:

- Identify all state‑managed Sites  
- Identify child Sites within state Sites  
- Identify Trails, Trail Segments, and Trail Networks on state lands  
- Identify Site Networks (e.g., Scenic River systems)  
- Identify Access Points associated with state Sites  
- Distinguish ODNR divisions, OHC, ODOT, EPA/ODA, and co‑management arrangements  
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

This sub‑procedure applies to all state‑level landholders and affiliated entities.

## 2.1 Primary State Agencies
- ODNR Division of Parks & Watercraft  
- ODNR Division of Forestry  
- ODNR Division of Wildlife  
- ODNR Division of Natural Areas & Preserves  
- ODNR Scenic Rivers Program  
- ODNR Division of Mineral Resources (surface‑managed lands only)

## 2.2 Quasi‑State Organizations
- **Ohio History Connection (OHC)**  
  (state memorials, archaeological preserves, historic landscapes)

## 2.3 Other State‑Level Landholders
- **ODOT** (scenic overlooks, bikeway corridors, mitigation lands)  
- **EPA / DEFA** (mitigation lands; conditional)  
- **ODA** (agricultural easements; conditional)

## 2.4 State‑Managed Easements
- Conservation easements  
- Scenic River easements  
- ODNR‑managed access easements  

This tier governs discovery of:

- Sites  
- Child Sites  
- Trails  
- Trail Segments  
- Trail Networks  
- Site Networks  
- Access Points  

Tier 2 sits **below Federal** and **above Park District**.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 2 must enumerate and recursively explore the following authoritative sources.

## 3.1 ODNR Division of Parks & Watercraft
Required sources:
- ODNR park pages  
- ODNR park maps  
- ODNR GIS datasets  

Check for:
- State parks → Sites  
- Campgrounds → child Sites  
- Day‑use areas → child Sites  
- Marinas → child Sites or Access Points  
- Boat ramps → Access Points  
- Trails → Trails, Trail Segments  

## 3.2 ODNR Division of Forestry
Required sources:
- ODNR forestry pages  
- ODNR forest maps  
- ODNR GIS datasets  

Check for:
- State forests → Sites  
- Forest management units → child Sites  
- Forest trails → Trails, Trail Segments  

## 3.3 ODNR Division of Wildlife
Required sources:
- ODNR wildlife area pages  
- ODNR wildlife GIS datasets  

Check for:
- Wildlife areas → Sites  
- Hunting units → child Sites  
- Fishing access points → Access Points  
- Wildlife area trails → Trails  

## 3.4 ODNR Division of Natural Areas & Preserves (DNAP)
Required sources:
- DNAP preserve pages  
- DNAP maps  
- DNAP GIS datasets  

Check for:
- State nature preserves → Sites  
- Preserve units → child Sites  
- Preserve access points → Access Points  
- Preserve trails → Trails  

## 3.5 ODNR Scenic Rivers Program
Required sources:
- Scenic River program pages  
- Scenic River maps  
- Scenic River GIS datasets  

Check for:
- Scenic River designations → Site Networks  
- Scenic River access points → Access Points  
- Scenic River segments → Trail Segments (if linear trails exist)  

## 3.6 ODNR Mineral Resources
Required sources:
- ODNR mineral resources datasets  

Check for:
- Surface‑managed lands → Sites  
- Public access areas → Access Points  

------------------------------------------------------------
# 4. DOMAIN RULES FOR STATE LAND DISCOVERY

## 4.1 Ohio History Connection (OHC)
Required sources:
- OHC site pages  
- OHC GIS datasets  
- National Register listings (cross‑reference only)

Check for:
- State memorials → Sites  
- Archaeological preserves → Sites  
- Historic landscapes → Sites  
- Mound sites → Sites  
- Cultural preserves → Sites  

## 4.2 ODOT
Required sources:
- ODOT GIS  
- ODOT project pages  
- ODOT bikeway datasets  

Check for:
- Scenic overlooks → Sites or Access Points  
- State‑managed bikeway corridors → Trails  
- Multi‑use paths along state routes → Trails  
- Mitigation lands → Sites (if identity‑bearing)  

## 4.3 EPA / DEFA (Conditional)
Include only if:
- Public access exists  
- The site is identity‑bearing  
- The site is managed as a natural area  

Examples:
- Wetland mitigation sites  
- Stream restoration sites  

## 4.4 ODA (Conditional)
Include only if:
- Identity‑bearing  
- Public access exists  
- Managed for conservation  

Examples:
- Demonstration farms  
- Conservation areas  

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 2 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Tier 2 must enumerate:
- All ODNR division listing pages  
- All OHC site listings  
- All ODOT bikeway and scenic overlook listings  
- All state‑managed easement listings  
- All state‑level GIS datasets  

## 5.2 Recursive Discovery (URL Propagation)
Tier 2 must recursively follow:
- Internal links within *.ohiodnr.gov  
- Internal links within *.ohiohistory.org  
- Internal links within *.transportation.ohio.gov  
- Internal links within *.epa.ohio.gov (conditional)  
- Internal links within *.agri.ohio.gov (conditional)  

Recursion must stop when:
- The domain is not on the allowlist  
- The page is not relevant to Sites, Trails, or Access Points  
- The page is administrative or non‑recreational  

## 5.3 Recursion Allowlist
- *.ohiodnr.gov  
- *.ohiohistory.org  
- *.transportation.ohio.gov  
- *.epa.ohio.gov  
- *.agri.ohio.gov  

------------------------------------------------------------
# 6. ENTITY CREATION RULES (TIER‑SPECIFIC)

### 6.1 Site Creation
Create a **Site** when:
- ODNR‑owned, ODNR‑managed, OHC‑managed, or ODOT‑managed  
- Identity‑bearing (named, mapped, or designated)  
- Public access or recreation infrastructure exists  
- It influences Access Point logic  

Exclude:
- Administrative offices  
- Maintenance yards  
- Non‑public parcels with no identity  

### 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a state Site  
- A campground, day‑use area, or management unit is identity‑bearing  
- A preserve unit or forest management zone is documented  

### 6.3 Trail Creation
Create a **Trail** when:
- A named trail appears in ODNR, OHC, or ODOT datasets or maps  

### 6.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment‑level geometry or identifiers exist  

### 6.5 Trail Network Creation
Create a **Trail Network** when:
- A statewide or regional multi‑trail system is documented  

Examples:
- Buckeye Trail (if treated as a network)  
- Statewide water trail systems  

### 6.6 Site Network Creation
Create a **Site Network** when:
- A Scenic River corridor or similar multi‑site designation exists  

### 6.7 Access Point Creation
Create an **Access Point** when:
- A visitor‑facing entry location is documented  

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

Tier 2 **must** surface:
- All state parks  
- All state forests  
- All wildlife areas  
- All nature preserves  
- All Scenic Rivers  
- All OHC‑managed state memorials and preserves  
- All ODOT scenic overlooks and state‑managed bikeways  
- All state‑managed trails  
- All state‑managed access points  
- All identity‑bearing child Sites  

Tier 2 **may** surface:
- Statewide trail networks  
- Scenic River Site Networks  
- State‑managed easements  
- EPA/ODA conservation lands (conditional)  

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

Each state entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v4.0**  
- **Discovery Metadata Specification v4.0**  
- The appropriate Schema Module v4.0  
- The appropriate Vocabulary Module v4.0  

No normalized fields may appear in Tier 2 output.

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

- This module is **State Lands Discovery Sub‑Procedure v4.0**.  
- Updates to ODNR, OHC, ODOT, EPA, or ODA datasets may result in v4.1, v4.2, etc.  
- Any change to tier order or workflow must be made in the Discovery Protocol Module v4.0.

------------------------------------------------------------
# END OF STATE LANDS DISCOVERY SUB‑PROCEDURE v4.0