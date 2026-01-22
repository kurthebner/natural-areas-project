# NATURAL AREAS PROJECT — DISTRICT‑LEVEL PUBLIC LANDHOLDERS DISCOVERY SUB‑PROCEDURE v3.2.2  
(Park Districts, Metro Parks, Joint Recreation Districts, Conservancy Districts, Watershed Districts, Special Districts)

Tier 3 of the **Discovery Protocol Module v3.2.2**.

District‑level public landholders in Ohio include park districts, metro parks, joint  
recreation districts, conservancy districts, watershed districts, and other special  
districts with statutory authority to own, manage, or operate natural areas, parks,  
trails, lakes, flood‑control lands, and recreation infrastructure. These districts  
vary widely in size, governance, and documentation, and may span multiple counties.

This module defines the **authoritative, deterministic rules** for Tier 3 discovery  
across all six entity types.

------------------------------------------------------------
# 1. PURPOSE

This sub‑procedure defines how the system must:

- Identify all district‑managed **Sites**  
- Identify **child Sites** within district Sites (Sites with Parent Site populated)  
- Identify district‑managed **Trails**, **Trail Segments**, and **Trail Networks**  
- Identify district‑managed **Site Networks**  
- Identify **Access Points** associated with district Sites and Trails  
- Distinguish district management from municipal, township, county, or state co‑management  
- Identify conservancy district lands, watershed district lands, and flood‑control lands  
- Avoid false positives from similarly named places  
- Log uncertainty and boundary cases  
- Produce Raw Candidate Records and Discovery Metadata v3.2.2  

This module is referenced **only** by the Discovery Protocol Module v3.2.2.

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to:

### Park & Recreation Districts
- County park districts  
- Metro parks systems  
- Joint recreation districts  

### Conservancy & Watershed Districts
- Muskingum Watershed Conservancy District (MWCD)  
- Miami Conservancy District  
- Joint conservancy districts  
- Watershed districts  
- Flood‑control districts  

### Special Districts
- Districts with statutory authority to own/manage natural areas  
- Districts managing lakes, reservoirs, or floodplain corridors  
- Districts with recreation or conservation mandates  

This tier governs discovery of:

- **Sites**  
- **Child Sites**  
- **Trails**  
- **Trail Segments**  
- **Trail Networks**  
- **Site Networks**  
- **Access Points**  

This tier sits **below State** and **above County**.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 Official District Website
Check for:
- Park or property lists → Sites  
- Facility lists → child Sites  
- Trail pages → Trails  
- Trail maps → Trails, Trail Segments  
- Access point listings → Access Points  
- District‑managed programs or networks → Site Networks, Trail Networks  

## 3.2 District GIS
Check for:
- District boundaries → Sites  
- Internal units → child Sites  
- Trail geometry → Trails, Trail Segments  
- Access point layers → Access Points  

## 3.3 District Brochures & Maps
Check for:
- Named parks → Sites  
- Named internal areas → child Sites  
- Named trails → Trails  
- Trailheads, parking, boat access → Access Points  

## 3.4 County Auditor / County GIS
Check for:
- Parcels owned by the district → Sites  
- Parcels leased or co‑managed → Sites or child Sites  

## 3.5 Partner Agencies
Check for:
- Co‑managed parks  
- Joint recreation districts  
- Shared trail systems  
- USACE partnerships (e.g., MWCD lakes)  

All sources must be logged in **Discovery Metadata v3.2.2**.

------------------------------------------------------------
# 4. DISTRICT‑LEVEL DISCOVERY CONDITIONS

## 4.1 Multi‑County Districts
Districts may span multiple counties.  
- **Do NOT segment multi‑county Sites**  
- Record all counties in `counties_raw`  

## 4.2 Conservancy Districts
Examples: MWCD, Miami Conservancy District  
Check for:
- Lakes and reservoirs → Sites  
- Recreation areas → Sites or child Sites  
- Shoreline access → Access Points  
- Flood‑control lands → Sites  
- Multi‑site lake systems → Site Networks  
- Multi‑trail lake corridors → Trail Networks  

## 4.3 Watershed & Flood‑Control Districts
Check for:
- Floodplain corridors → Sites  
- River access → Access Points  
- Multi‑county river systems → Site Networks  
- District‑managed trails → Trails  

## 4.4 Co‑Management
Districts may co‑manage Sites with:
- Municipalities  
- Townships  
- Counties  
- ODNR  
- USACE  

Record all co‑management in metadata.

------------------------------------------------------------
# 5. TIER‑ANCHORED VERIFICATION (MANDATORY)

## 5.1 Confirm Boundaries
- Verify the feature lies within the county  
- Record **all counties** in `counties_raw`  
- **Do NOT segment multi‑county entities**  
- Normalization alphabetizes and semicolon‑delimits the county list  

## 5.2 Confirm Management Authority
Record:
- District name  
- District type (park district, conservancy district, watershed district, etc.)  
- Co‑management (municipal, township, county, ODNR, USACE)  

## 5.3 Confirm Access Points
Identify:
- Trailheads  
- Parking areas  
- Boat ramps  
- Scenic overlooks  
- Recreation area entrances  
- Shoreline access points  
- River access points  

Access Points must be surfaced as **Access Point candidates** and passed to the  
**Access Point Discovery Sub‑Procedure v3.2.2**.

## 5.4 Naming
Use the **district‑published name** as authoritative.  
If multiple names appear → record all in metadata.

------------------------------------------------------------
# 6. DECISION RULES FOR ENTITY CREATION

### 6.1 Site Creation
Create a **Site** when:
- District‑owned or district‑managed  
- Identity‑bearing (named, mapped, or designated)  
- Public access or recreation infrastructure exists  
- It influences Access Point logic  

Exclude:
- Administrative offices  
- Maintenance yards  
- Non‑public parcels with no identity  

### 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a district Site  
- It meets the **Child Site Rules Module v3.2.2**  

### 6.3 Trail Creation
Create a **Trail** when:
- A named trail appears in district datasets or maps  

### 6.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment‑level geometry or identifiers exist  

### 6.5 Trail Network Creation
Create a **Trail Network** when:
- A district‑managed multi‑trail system exists  
- A multi‑lake or multi‑river corridor trail system exists  

### 6.6 Site Network Creation
Create a **Site Network** when:
- A district‑managed multi‑site system exists  
- A multi‑lake or multi‑river system is documented  

### 6.7 Access Point Creation
Create an **Access Point** when:
- A visitor‑facing entry location is documented  

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

The District‑Level Tier **must** surface:
- All district‑managed Sites  
- All identity‑bearing child Sites  
- All district‑managed Trails  
- All district‑managed Trail Segments  
- All district‑managed Access Points  
- All conservancy district Sites (e.g., MWCD lakes, recreation areas)  
- All watershed/flood‑control district Sites  

The District‑Level Tier **may** surface:
- District‑managed Trail Networks  
- District‑managed Site Networks  
- District‑managed easements  
- Flood‑control corridors  
- Multi‑lake or multi‑river systems  

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

Each district‑level entity must output a **Raw Candidate Record** conforming to:
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- The appropriate Schema Module v3.2.2  
- The appropriate Vocabulary Module v3.2.2  

No normalized fields may appear in Tier 3 output.

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

- This module is **District‑Level Public Landholders Discovery Sub‑Procedure v3.2.2**.  
- Updates to district governance or datasets may result in v3.3, v3.4, etc.  
- Any change to tier order or workflow must be made in the  
  **Discovery Protocol Module v3.2.2**.

------------------------------------------------------------
# END OF DISTRICT‑LEVEL PUBLIC LANDHOLDERS DISCOVERY SUB‑PROCEDURE v3.2.2