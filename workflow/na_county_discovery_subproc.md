# NATURAL AREAS PROJECT — COUNTY LANDS DISCOVERY SUB‑PROCEDURE v3.2.2  
(County Governments, County GIS, County Recreation Departments, County‑Hosted Municipal/Township Pages)

Tier 4 of the **Discovery Protocol Module v3.2.2**.

Counties in Ohio vary widely in capacity, GIS sophistication, and recreation infrastructure.  
Some maintain robust GIS systems and recreation departments; others rely on minimal web  
presence or county‑hosted municipal/township pages. County GIS is often the most  
authoritative source for park boundaries, trail alignments, and access infrastructure.

This module defines the **authoritative, deterministic rules** for Tier 4 discovery  
across all six entity types.

------------------------------------------------------------
# 1. PURPOSE

This sub‑procedure defines how the system must:

- Identify county‑owned or county‑managed **Sites**  
- Identify county‑managed **child Sites** (Sites with Parent Site populated)  
- Identify county‑managed **Trails** and **Trail Segments**  
- Identify county‑managed **Trail Networks** (rare)  
- Identify county‑managed **Site Networks** (rare)  
- Identify county‑managed **Access Points**  
- Identify county‑hosted municipal/township pages  
- Distinguish county management from municipal/township co‑management  
- Avoid false positives from similarly named places  
- Log uncertainty and boundary cases  
- Produce Raw Candidate Records and Discovery Metadata v3.2.2  

This module is referenced **only** by the Discovery Protocol Module v3.2.2.

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to:

- County government websites  
- County GIS systems  
- County recreation departments  
- County planning commissions  
- County commissioners’ pages  
- County‑hosted municipal/township pages  
- County tourism or visitors bureau pages  
- County‑level trail plans  

It governs discovery of:

- **Sites**  
- **Child Sites**  
- **Trails**  
- **Trail Segments**  
- **Trail Networks**  
- **Site Networks**  
- **Access Points**  

This tier sits **below District‑Level Public Landholders** and **above Township**.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 County Government Website
Scan for:

- Parks  
- Recreation  
- Facilities  
- Natural Resources  
- Open Space / Conservation  
- Trails  
- Outdoor Recreation  

Include:

- Hidden or unlinked pages  
- PDF brochures  
- County‑hosted municipal/township pages  
- Recreation guides  

## 3.2 County GIS (Primary Authoritative Source)
Check for layers including:

- Parks → Sites  
- Open space → Sites  
- Conservation lands → Sites  
- Trails → Trails, Trail Segments  
- Recreation facilities → Sites or child Sites  
- Boat launches → Access Points  
- Fishing access → Access Points  
- Hunting access → Access Points  
- County‑owned parcels → Sites  

## 3.3 County Planning Documents
Check:

- Comprehensive plans  
- Greenway plans  
- Open space plans  
- Trail plans  
- Recreation master plans  

## 3.4 County Commissioners’ Pages
Check for:

- Land acquisitions  
- Park resolutions  
- Conservation partnerships  
- Trail funding approvals  

## 3.5 County Tourism / Visitors Bureau
Check for:

- Parks  
- Trails  
- Natural attractions  
- Outdoor recreation assets  

## 3.6 County‑Hosted Municipal/Township Pages
These count as **authoritative** for municipal/township discovery.

------------------------------------------------------------
# 4. COUNTY LAND DISCOVERY CONDITIONS

County discovery must account for:

## 4.1 County‑Owned vs County‑Managed
A Site may be:

- Owned by the county  
- Managed by the county  
- Co‑managed with municipalities or park districts  

All must be surfaced if identity‑bearing.

## 4.2 County‑Hosted Municipal/Township Pages
If the county hosts municipal/township pages:

- Treat them as authoritative  
- Surface all parks, preserves, trails, and facilities listed  
- Log the county as the source  

Discoveries remain **Tier 4**.

## 4.3 County Recreation Departments
If a recreation department exists:

- Scan all program pages  
- Scan all facility pages  
- Scan all park listings  
- Scan all trail listings  
- Scan all brochures and PDFs  

## 4.4 County Planning Commissions
Planning documents often contain:

- Unlisted parks  
- Planned parks  
- Trail corridors  
- Access Points  

------------------------------------------------------------
# 5. TIER‑ANCHORED VERIFICATION (MANDATORY)

## 5.1 Confirm County Boundaries
- Verify the feature lies within the county  
- **Record all counties in `counties_raw`**  
- **Do NOT segment multi‑county features**  

## 5.2 Confirm Management Authority
Record:

- County department  
- Co‑managers (if any)  

## 5.3 Confirm Access Points
Identify:

- Trailheads  
- Parking areas  
- Boat launches  
- Fishing access  
- Hunting access  
- Scenic overlooks  

Access Points must be surfaced as **Access Point candidates** and passed to the  
**Access Point Discovery Sub‑Procedure v3.2.2**.

## 5.4 Naming
Record names **exactly as discovered**.  
If multiple names appear → record all in metadata.

------------------------------------------------------------
# 6. DECISION RULES FOR ENTITY CREATION

### 6.1 Site Creation
A county feature becomes a **Site** if:

- County‑owned or county‑managed  
- Identity‑bearing (named, mapped, or designated)  
- Public access or recreation infrastructure exists  
- It influences Access Point logic  

Exclude:

- Administrative buildings  
- Maintenance yards  
- Non‑public facilities  

### 6.2 Child Site Creation
Create a **child Site** when:

- A named internal unit exists within a county Site  
- A recreation area, campground, or management area is identity‑bearing  
- A special management zone is documented  

### 6.3 Trail Creation
Create a **Trail** when:

- A named trail appears in county GIS, plans, or recreation pages  

### 6.4 Trail Segment Creation
Create a **Trail Segment** when:

- Segment‑level geometry or identifiers exist  

### 6.5 Trail Network Creation
Create a **Trail Network** when:

- A county‑managed multi‑trail system exists  
- A greenway corridor spans multiple Trails  

### 6.6 Site Network Creation
Create a **Site Network** when:

- A county‑managed multi‑site system exists  
- A conservation or greenway network is formally documented  

### 6.7 Access Point Creation
Create an **Access Point** when:

- A visitor‑facing entry location is documented  

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

The County Tier **must** surface:

- All county‑owned or county‑managed Sites  
- All identity‑bearing child Sites  
- All county‑managed Trails  
- All county‑managed Trail Segments  
- All county‑managed Access Points  
- All parks, preserves, and trails listed on county‑hosted municipal/township pages  

The County Tier **may** surface:

- County‑managed Trail Networks  
- County‑managed Site Networks  
- County‑managed easements  
- Planned parks and trail corridors (if identity‑bearing)  

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

Each county entity must output a **Raw Candidate Record** conforming to:

- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- The appropriate Schema Module v3.2.2  
- The appropriate Vocabulary Module v3.2.2**  

No normalized fields may appear in Tier 4 output.

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

- This module is **County Lands Discovery Sub‑Procedure v3.2.2**.  
- Updates to county GIS standards or statewide county practices may result in v3.3, v3.4, etc.  
- Any change to tier order or workflow must be made in the  
  **Discovery Protocol Module v3.2.2**.

------------------------------------------------------------
# END OF COUNTY LANDS DISCOVERY SUB‑PROCEDURE v3.2.2