# NATURAL AREAS PROJECT — STATE LANDS DISCOVERY SUB‑PROCEDURE v3.2.2  
(ODNR Divisions, OHC, ODOT, State Easements, Scenic Rivers)

Tier 2 of the **Discovery Protocol Module v3.2.2**.

State‑managed lands must be discovered using authoritative ODNR datasets,  
division‑level sources, quasi‑state sources, and county‑anchored verification.  
Ohio’s state lands include parks, forests, wildlife areas, nature preserves,  
scenic rivers, and other ODNR‑managed or state‑affiliated units.  

This module defines the **authoritative, deterministic rules** for Tier 2 discovery  
across all six entity types.

------------------------------------------------------------
# 1. PURPOSE

This sub‑procedure defines how the system must:

- Identify all state‑managed Sites  
- Identify **child Sites** within state Sites (Sites with Parent Site populated)  
- Identify Trails, Trail Segments, and Trail Networks on state lands  
- Identify Site Networks (e.g., Scenic River systems)  
- Identify Access Points associated with state Sites  
- Distinguish ODNR divisions, OHC, ODOT, and co‑management arrangements  
- Avoid false positives from similarly named places  
- Log uncertainty and boundary cases  
- Produce Raw Candidate Records and Discovery Metadata v3.2.2  

This module is referenced **only** by the Discovery Protocol Module v3.2.2.

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to:

### Primary State Agencies
- ODNR Division of Parks & Watercraft  
- ODNR Division of Forestry  
- ODNR Division of Wildlife  
- ODNR Division of Natural Areas & Preserves  
- ODNR Scenic Rivers Program  
- ODNR Division of Mineral Resources (surface‑managed lands only)

### Quasi‑State Organizations
- **Ohio History Connection (OHC)**  
  (state memorials, archaeological preserves, historic landscapes)

### Other State‑Level Landholders
- **ODOT** (scenic overlooks, bikeway corridors, mitigation lands)  
- **EPA / DEFA** (mitigation lands; conditional)  
- **ODA** (agricultural easements; conditional)

### State‑Managed Easements
- Conservation easements  
- Scenic River easements  
- ODNR‑managed access easements  

This tier governs discovery of:

- **Sites**  
- **Child Sites**  
- **Trails**  
- **Trail Segments**  
- **Trail Networks**  
- **Site Networks**  
- **Access Points**  

This tier sits **below Federal** and **above Park District**.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 ODNR Division of Parks & Watercraft
Check for:
- State parks → Sites  
- Campgrounds → child Sites  
- Day‑use areas → child Sites  
- Marinas → child Sites or Access Points  
- Boat ramps → Access Points  
- Trails → Trails, Trail Segments  

Sources:
- ODNR park pages  
- ODNR park maps  
- ODNR GIS datasets  

## 3.2 ODNR Division of Forestry
Check for:
- State forests → Sites  
- Forest management units → child Sites  
- Forest trails → Trails, Trail Segments  

Sources:
- ODNR forestry pages  
- ODNR forest maps  
- ODNR GIS datasets  

## 3.3 ODNR Division of Wildlife
Check for:
- Wildlife areas → Sites  
- Hunting units → child Sites  
- Fishing access points → Access Points  
- Wildlife area trails → Trails  

Sources:
- ODNR wildlife area pages  
- ODNR wildlife GIS datasets  

## 3.4 ODNR Division of Natural Areas & Preserves
Check for:
- State nature preserves → Sites  
- Preserve units → child Sites  
- Preserve access points → Access Points  
- Preserve trails → Trails  

Sources:
- DNAP preserve pages  
- DNAP maps  
- DNAP GIS datasets  

## 3.5 ODNR Scenic Rivers Program
Check for:
- Scenic River designations → Site Networks  
- Scenic River access points → Access Points  
- Scenic River segments → Trail Segments (if linear trails exist)  

Sources:
- Scenic River program pages  
- Scenic River maps  
- Scenic River GIS datasets  

## 3.6 ODNR Mineral Resources
Check for:
- Surface‑managed lands → Sites  
- Public access areas → Access Points  

Sources:
- ODNR mineral resources datasets  

------------------------------------------------------------
# 4. STATE LAND DISCOVERY CONDITIONS

## 4.1 Ohio History Connection (OHC)
Check for:
- State memorials → Sites  
- Archaeological preserves → Sites  
- Historic landscapes → Sites  
- Mound sites → Sites  
- Cultural preserves → Sites  

Sources:
- OHC site pages  
- OHC GIS datasets  
- National Register listings (cross‑reference only)  

## 4.2 ODOT
Check for:
- Scenic overlooks → Sites or Access Points  
- State‑managed bikeway corridors → Trails  
- Multi‑use paths along state routes → Trails  
- Mitigation lands → Sites (if identity‑bearing)  

Sources:
- ODOT GIS  
- ODOT project pages  
- ODOT bikeway datasets  

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
# 5. TIER‑ANCHORED VERIFICATION (MANDATORY)

## 5.1 Confirm Boundaries
- Verify the feature lies within the county  
- Record all counties exactly as discovered in `counties_raw`  
- **Do NOT segment multi‑county Sites**  
- Normalization alphabetizes and semicolon‑delimits the county list  

## 5.2 Confirm Management Authority
Record:
- ODNR division  
- OHC  
- ODOT  
- EPA / ODA (if applicable)  
- Co‑management (park district, county, municipal)  

## 5.3 Confirm Access Points
Identify:
- Boat ramps  
- Trailheads  
- Parking areas  
- Scenic overlooks  
- River access points  
- Campground entrances  

Access Points must be surfaced as **Access Point candidates** and passed to the  
**Access Point Discovery Sub‑Procedure v3.2.2**.

## 5.4 Naming
Record names **exactly as discovered**.  
If multiple names appear → record all in metadata.

------------------------------------------------------------
# 6. DECISION RULES FOR ENTITY CREATION

### 6.1 Site Creation
A state‑managed feature becomes a **Site** if:
- ODNR‑owned, ODNR‑managed, OHC‑managed, or ODOT‑managed  
- Identity‑bearing (named, mapped, or designated)  
- Public access or recreation infrastructure exists  
- Influences Access Point logic  

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

The State Tier **must** surface:
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

The State Tier **may** surface:
- Statewide trail networks  
- Scenic River Site Networks  
- State‑managed easements  
- EPA/ODA conservation lands (conditional)  

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

Each state entity must output a **Raw Candidate Record** conforming to:
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- The appropriate Schema Module v3.2.2  
- The appropriate Vocabulary Module v3.2.2  

No normalized fields may appear in Tier 2 output.

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

- This module is **State Lands Discovery Sub‑Procedure v3.2.2**.  
- Updates to ODNR, OHC, ODOT, EPA, or ODA datasets may result in v3.3, v3.4, etc.  
- Any change to tier order or workflow must be made in the  
  **Discovery Protocol Module v3.2.2**.

------------------------------------------------------------
# END OF STATE LANDS DISCOVERY SUB‑PROCEDURE v3.2.2