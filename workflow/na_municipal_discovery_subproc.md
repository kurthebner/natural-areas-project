# NATURAL AREAS PROJECT — MUNICIPAL LANDS DISCOVERY SUB‑PROCEDURE v3.2.2  
(Cities, Villages, Incorporated Municipalities, and County‑Hosted Municipal Pages)

Tier 6 of the **Discovery Protocol Module v3.2.2**.

Municipalities in Ohio vary dramatically in size, capacity, and web presence.  
Some maintain full parks & recreation departments; others have no recreation pages  
at all. Municipal parks may exist even when no recreation department exists, and  
many municipal parks are hidden on non‑indexed subpages.

This module defines the **authoritative, deterministic rules** for Tier 6 discovery  
across all six entity types.

------------------------------------------------------------
# 1. PURPOSE

This sub‑procedure defines how the system must:

- Identify municipal‑owned or municipal‑managed **Sites**  
- Identify municipal‑managed **child Sites**  
- Identify municipal‑managed **Trails** and **Trail Segments**  
- Identify municipal‑managed **Trail Networks** (rare)  
- Identify municipal‑managed **Site Networks** (rare)  
- Identify municipal‑managed **Access Points**  
- Identify municipal parks even when no recreation department exists  
- Identify municipal pages hosted by the county  
- Surface uncertainty and conflicts  
- Produce Raw Candidate Records and Discovery Metadata v3.2.2  

This module is referenced **only** by the Discovery Protocol Module v3.2.2.

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to:

- City and village government websites  
- Municipal recreation department pages  
- Municipal planning documents  
- Municipal GIS (rare)  
- Municipal meeting minutes  
- County‑hosted municipal pages  
- Municipal tourism or community pages  
- Official municipal social media (conditional)  

It governs discovery of:

- **Sites**  
- **Child Sites**  
- **Trails**  
- **Trail Segments**  
- **Trail Networks**  
- **Site Networks**  
- **Access Points**  

This tier sits **below Township** and **above Land Trust & Conservancy**.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 Municipal Website (If Exists)
Scan for:
- Parks  
- Recreation  
- Facilities  
- Community  
- Open Space / Green Space  
- Playgrounds  
- Shelters  
- Picnic Areas  
- Natural Areas  
- Trails  

Municipal websites often contain:
- Hidden subpages  
- Non‑indexed pages  
- PDF‑only listings  
- Outdated or partial information  

All must be scanned.

## 3.2 County‑Hosted Municipal Pages
If the county hosts municipal pages:
- Treat them as authoritative  
- Scan for parks, preserves, trails, facilities  
- Log the county as the source  

Discoveries remain **Tier 6** because the municipality is the governing entity.

## 3.3 Municipal Recreation Departments
If a recreation department exists:
- Scan all program pages  
- Scan all facility pages  
- Scan all park listings  
- Scan all trail listings  
- Scan all brochures and PDFs  

## 3.4 Municipal Planning Documents
Check for:
- Comprehensive plans  
- Parks & recreation master plans  
- Greenway plans  
- Open space plans  
- Trail plans  

These often contain:
- Unlisted parks  
- Planned parks  
- Trail corridors  
- Access Points  

## 3.5 Municipal Meeting Minutes
Scan for:
- Land purchases  
- Park dedications  
- Trail agreements  
- Conservation partnerships  
- Recreation facility improvements  

## 3.6 Municipal GIS (If Exists)
Check for:
- Municipal‑owned parcels  
- Recreation layers  

## 3.7 Municipal Social Media (Conditional)
Municipal social media is **authoritative only if**:
- Explicitly designated as official by the municipality, OR  
- Linked from the municipal website, OR  
- Linked from the county website  

If official:
- Scan for park announcements  
- Facility openings  
- Trail access information  

If not official → **exclude**.

------------------------------------------------------------
# 4. MUNICIPAL LAND DISCOVERY CONDITIONS

## 4.1 Municipal‑Owned vs Municipal‑Managed
A Site may be:
- Owned by the municipality  
- Managed by the municipality  
- Co‑managed with counties or park districts  

All must be surfaced if identity‑bearing.

## 4.2 Hidden or Non‑Indexed Pages
Municipal parks may appear on:
- Unlinked HTML pages  
- PDF brochures  
- Archived pages  

These must be included if authoritative.

## 4.3 Municipal Recreation Assets Without a Recreation Department
Even if no recreation department exists:
- Parks  
- Trails  
- Facilities  
- Natural areas  

must still be surfaced if identity‑bearing.

## 4.4 County‑Hosted Municipal Pages
These are authoritative for municipal discovery but remain **Tier 6**.

------------------------------------------------------------
# 5. TIER‑ANCHORED VERIFICATION (MANDATORY)

## 5.1 Confirm Municipal Boundaries
- Verify the feature lies within the municipality  
- Record all counties in `counties_raw`  
- Do NOT segment multi‑municipal or multi‑county features  

## 5.2 Confirm Management Authority
Record:
- Municipality name  
- Co‑managers (if any)  

## 5.3 Confirm Access Points
Identify:
- Trailheads  
- Parking areas  
- Boat launches  
- Fishing access  
- Scenic overlooks  
- Playgrounds  
- Shelters  

Access Points must be surfaced as **Access Point candidates** and passed to the  
**Access Point Discovery Sub‑Procedure v3.2.2**.

## 5.4 Naming
Use the **municipal‑published name** as authoritative.  
If multiple names appear → record all in metadata.

------------------------------------------------------------
# 6. DECISION RULES FOR ENTITY CREATION

### 6.1 Site Creation
A municipal feature becomes a **Site** if:
- Municipal‑owned or municipal‑managed  
- Identity‑bearing (named, mapped, or designated)  
- Public access or recreation infrastructure exists  
- It influences Access Point logic  

Exclude:
- City halls  
- Administrative buildings  
- Cemeteries (unless designated natural areas)  
- Maintenance yards  

### 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a municipal Site  
- A recreation area, facility, or natural area is identity‑bearing  
- A playground, shelter area, or lake area is formally named  

Do **not** surface:
- Amenities without identity  
- Temporary zones  
- Unnamed management areas  

### 6.3 Trail Creation
Surface a **Trail** when:
- A named trail appears on municipal or county‑hosted pages  
- A named trail appears in planning documents  
- A named trail appears in meeting minutes  
- A named trail appears in municipal GIS (rare)  

### 6.4 Trail Segment Creation
Surface **Trail Segments** when:
- Segment‑level geometry exists in municipal or county GIS  
- Segment identifiers appear in maps or plans  

### 6.5 Trail Network Creation
Surface a **Trail Network** when:
- A municipal‑managed multi‑trail system exists  
- A greenway corridor spans multiple Trails  

Rare but must be captured.

### 6.6 Site Network Creation
Surface a **Site Network** when:
- A municipal‑managed multi‑site system exists  
- A conservation or greenway network is formally documented  

Very rare but must be captured.

### 6.7 Access Point Creation
Surface an **Access Point** when:
- It appears on municipal pages  
- It appears on county‑hosted municipal pages  
- It appears in municipal planning documents  
- It appears in municipal meeting minutes  
- It appears in municipal GIS (rare)  

Access Points must include raw values only:
- Name or descriptive label  
- Access Point Type (raw)  
- Municipality  
- County list (raw)  
- Parent entity (Site, child Site, Trail, Trail Segment)  
- Source(s)  
- Notes  

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

The Municipal Tier **must** surface:
- All municipal‑owned or municipal‑managed Sites  
- All identity‑bearing child Sites  
- All municipal‑managed Trails  
- All municipal‑managed Trail Segments  
- All municipal‑managed Access Points  
- All parks, preserves, and trails listed on county‑hosted municipal pages  

The Municipal Tier **may** surface:
- Municipal‑managed Trail Networks  
- Municipal‑managed Site Networks  
- Municipal‑managed easements  
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

Each municipal entity must output a **Raw Candidate Record** conforming to:
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- The appropriate Schema Module v3.2.2  
- The appropriate Vocabulary Module v3.2.2  

No normalized fields may appear in Tier 6 output.

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

- This module is **Municipal Lands Discovery Sub‑Procedure v3.2.2**.  
- Updates to municipal governance practices or statewide municipal directories may result in v3.3, v3.4, etc.  
- Any change to tier order or workflow must be made in the  
  **Discovery Protocol Module v3.2.2**.

------------------------------------------------------------
# END OF MUNICIPAL LANDS DISCOVERY SUB‑PROCEDURE v3.2.2