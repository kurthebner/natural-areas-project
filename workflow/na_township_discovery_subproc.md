# NATURAL AREAS PROJECT — TOWNSHIP LANDS DISCOVERY SUB‑PROCEDURE v3.2.2  
(Ohio Townships, Township Websites, Township‑Hosted Pages, Township Recreation Assets)

Tier 5 of the **Discovery Protocol Module v3.2.2**.

Townships in Ohio vary widely in capacity, web presence, and documentation.  
Some maintain full recreation pages; others have no website at all. Township parks  
may exist even when no recreation department exists, and many township parks are  
hidden on non‑indexed subpages.

This module defines the **authoritative, deterministic rules** for Tier 5 discovery  
across all six entity types.

------------------------------------------------------------
# 1. PURPOSE

This sub‑procedure defines how the system must:

- Identify township‑owned or township‑managed **Sites**  
- Identify township‑managed **child Sites**  
- Identify township‑managed **Trails** and **Trail Segments**  
- Identify township‑managed **Trail Networks** (rare)  
- Identify township‑managed **Site Networks** (rare)  
- Identify township‑managed **Access Points**  
- Identify township recreation assets even when no recreation department exists  
- Identify township pages hosted by the county  
- Surface uncertainty and conflicts  
- Produce Raw Candidate Records and Discovery Metadata v3.2.2  

This module is referenced **only** by the Discovery Protocol Module v3.2.2.

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to:

- Township government websites  
- Township recreation pages (if any)  
- Township‑hosted or county‑hosted subpages  
- Township planning documents (rare)  
- Township GIS layers (rare)  
- Township meeting minutes (for land acquisitions)  
- Official township social media (conditional)  

It governs discovery of:

- **Sites**  
- **Child Sites**  
- **Trails**  
- **Trail Segments**  
- **Trail Networks**  
- **Site Networks**  
- **Access Points**  

This tier sits **below County** and **above Municipal**.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 Township Website (If Exists)
Check for:
- Parks  
- Recreation  
- Facilities  
- Community  
- Open Space / Green Space  
- Playgrounds  
- Shelters  
- Picnic Areas  

Township websites often contain:
- Hidden subpages  
- Non‑indexed pages  
- PDF‑only listings  
- Outdated or partial information  

All must be scanned.

## 3.2 County‑Hosted Township Pages
If the county hosts township pages:
- Treat them as authoritative  
- Scan for parks, preserves, trails, facilities  
- Log the county as the source  

Discoveries remain **Tier 5** because the township is the governing entity.

## 3.3 Township Meeting Minutes
Scan for:
- Land purchases  
- Park dedications  
- Trail agreements  
- Conservation partnerships  
- Recreation facility improvements  

## 3.4 Township GIS (If Exists)
Check for:
- Township‑owned parcels  
- Recreation layers  

## 3.5 Township Social Media (Conditional)
Township social media is **authoritative only if**:
- Explicitly designated as official by the township, OR  
- Linked from the township website, OR  
- Linked from the county website  

If official:
- Scan for park announcements  
- Facility openings  
- Trail access information  

If not official → **exclude**.

------------------------------------------------------------
# 4. TOWNSHIP LAND DISCOVERY CONDITIONS

## 4.1 Township‑Owned vs Township‑Managed
A Site may be:
- Owned by the township  
- Managed by the township  
- Co‑managed with counties or park districts  

All must be surfaced if identity‑bearing.

## 4.2 Hidden or Non‑Indexed Pages
Township parks may appear on:
- Unlinked HTML pages  
- PDF brochures  
- Archived pages  

These must be included if authoritative.

## 4.3 Township Recreation Assets Without a Recreation Department
Even if no recreation department exists:
- Parks  
- Trails  
- Facilities  
- Natural areas  

must still be surfaced if identity‑bearing.

## 4.4 County‑Hosted Township Pages
These are authoritative for township discovery but remain **Tier 5**.

------------------------------------------------------------
# 5. TIER‑ANCHORED VERIFICATION (MANDATORY)

## 5.1 Confirm Township Boundaries
- Verify the feature lies within the township  
- Record all counties in `counties_raw`  
- Do NOT segment multi‑township or multi‑county features  

## 5.2 Confirm Management Authority
Record:
- Township name  
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
Use the **township‑published name** as authoritative.  
If multiple names appear → record all in metadata.

------------------------------------------------------------
# 6. DECISION RULES FOR ENTITY CREATION

### 6.1 Site Creation
A township feature becomes a **Site** if:
- Township‑owned or township‑managed  
- Identity‑bearing (named, mapped, or designated)  
- Public access or recreation infrastructure exists  
- It influences Access Point logic  

Exclude:
- Township halls  
- Administrative buildings  
- Cemeteries (unless designated natural areas)  
- Maintenance yards  

### 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a township Site  
- A recreation area, facility, or natural area is identity‑bearing  
- A playground, shelter area, or lake area is formally named  

Do **not** surface:
- Amenities without identity  
- Temporary zones  
- Unnamed management areas  

### 6.3 Trail Creation
Surface a **Trail** when:
- A named trail appears on township or county‑hosted pages  
- A named trail appears in meeting minutes  
- A named trail appears in township GIS (rare)  

### 6.4 Trail Segment Creation
Surface **Trail Segments** when:
- Segment‑level geometry exists in township or county GIS  
- Segment identifiers appear in maps or plans  

### 6.5 Trail Network Creation
Surface a **Trail Network** when:
- A township‑managed multi‑trail system exists  
- A greenway corridor spans multiple Trails  

Rare but must be captured.

### 6.6 Site Network Creation
Surface a **Site Network** when:
- A township‑managed multi‑site system exists  
- A conservation or greenway network is formally documented  

Very rare but must be captured.

### 6.7 Access Point Creation
Surface an **Access Point** when:
- It appears on township pages  
- It appears on county‑hosted township pages  
- It appears in township meeting minutes  
- It appears in township GIS (rare)  

Access Points must include raw values only:
- Name or descriptive label  
- Access Point Type (raw)  
- Township  
- County list (raw)  
- Parent entity (Site, child Site, Trail, Trail Segment)  
- Source(s)  
- Notes  

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

The Township Tier **must** surface:
- All township‑owned or township‑managed Sites  
- All identity‑bearing child Sites  
- All township‑managed Trails  
- All township‑managed Trail Segments  
- All township‑managed Access Points  
- All parks, preserves, and trails listed on county‑hosted township pages  

The Township Tier **may** surface:
- Township‑managed Trail Networks  
- Township‑managed Site Networks  
- Township‑managed easements  
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

Each township entity must output a **Raw Candidate Record** conforming to:
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- The appropriate Schema Module v3.2.2  
- The appropriate Vocabulary Module v3.2.2  

No normalized fields may appear in Tier 5 output.

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

- This module is **Township Lands Discovery Sub‑Procedure v3.2.2**.  
- Updates to township governance practices or statewide township directories may result in v3.3, v3.4, etc.  
- Any change to tier order or workflow must be made in the  
  **Discovery Protocol Module v3.2.2**.

------------------------------------------------------------
# END OF TOWNSHIP LANDS DISCOVERY SUB‑PROCEDURE v3.2.2