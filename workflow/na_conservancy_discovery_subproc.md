# NATURAL AREAS PROJECT — NONPROFIT CONSERVATION LANDHOLDERS DISCOVERY SUB‑PROCEDURE v3.2.2  
(Land Trusts, Conservancies, Foundations, Trail Alliances, Greenway Coalitions, Watershed Nonprofits)

Tier 7 of the **Discovery Protocol Module v3.2.2**.

Nonprofit conservation organizations in Ohio include land trusts, conservancies,  
foundations, watershed groups, trail alliances, and regional greenway coalitions.  
These organizations hold fee‑simple preserves, conservation easements, trail  
corridors, and partnership lands. Their holdings are often absent from county or  
state datasets, making Tier 7 essential for statewide completeness.

This module defines the **authoritative, deterministic rules** for Tier 7 discovery  
across all six ontology entity types.

------------------------------------------------------------
# 1. PURPOSE

This sub‑procedure defines how the system must:

- Identify all nonprofit conservation **Sites**  
- Identify **child Sites** within preserves (Sites with Parent Site populated)  
- Identify **Trails**, **Trail Segments**, and **Trail Networks** on nonprofit holdings  
- Identify **Site Networks** (multi‑site conservation systems)  
- Identify **Access Points** associated with nonprofit holdings  
- Identify fee‑simple preserves and qualifying conservation easements  
- Identify trail corridors, greenways, and linear preserves  
- Distinguish public‑access vs. non‑public‑access holdings  
- Identify co‑managed Sites  
- Log uncertainty and boundary cases  
- Produce Raw Candidate Records and Discovery Metadata v3.2.2  

This module is referenced only by the Discovery Protocol Module v3.2.2.

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to:

### Land Trusts & Conservancies
- Local, regional, statewide, and national land trusts  
- Conservancies and conservation foundations  

### Trail & Greenway Organizations
- Trail alliances  
- Greenway coalitions  
- Linear corridor nonprofits  

### Watershed & Habitat Organizations
- Watershed groups  
- Habitat restoration nonprofits  
- Ecological stewardship organizations  

### Conservation Networks
- Land trust consortiums and alliances  
- Regional conservation partnerships  

It governs discovery of:

- **Sites**  
- **Child Sites**  
- **Trails**  
- **Trail Segments**  
- **Trail Networks**  
- **Site Networks**  
- **Access Points**  

This tier sits **below Municipal** and **above Private & Organization‑Based**.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 Official Nonprofit Websites
Scan for:
- Preserves  
- Protected lands  
- Conservation areas  
- Nature preserves  
- Public access  
- Hiking trails  
- Stewardship information  

Scan all:
- Preserve pages  
- Project pages  
- Maps  
- PDF brochures  
- Stewardship reports  

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

## 3.4 Statewide & Regional Conservation Networks
Check:
- ONAPA  
- Regional conservation partnerships  
- Watershed groups  
- Greenway coalitions  

## 3.5 Federal & State Partners
Nonprofits often partner with:
- ODNR  
- USFWS  
- USACE  
- Park districts  
- Municipalities  

All partnerships must be logged in metadata.

------------------------------------------------------------
# 4. NONPROFIT LAND DISCOVERY CONDITIONS

## 4.1 Fee‑Simple Ownership
Surface as a **Site** if:
- Owned by the nonprofit  
- Identity‑bearing  
- Public access exists OR the preserve is named/mapped  

## 4.2 Conservation Easements
Surface as a **Site** if:
- Public access exists, OR  
- The easement is identity‑bearing, OR  
- It contains trails, overlooks, or access points  

Exclude:
- Private easements with no public access  
- Agricultural easements with no recreation role  
- Scenic easements with no access  

## 4.3 Trail Corridors & Linear Preserves
Surface as **Sites** if:
- Named  
- Mapped  
- Identity‑bearing  
- Have one or more Access Points  

## 4.4 Multi‑County Holdings
- **Record all counties exactly as discovered in `counties_raw`**  
- **Do NOT segment multi‑county Sites**  

------------------------------------------------------------
# 5. TIER‑ANCHORED VERIFICATION (MANDATORY)

## 5.1 Confirm County Boundaries
- Verify the feature lies within the county  
- Record all counties in metadata  
- Do NOT segment multi‑county features  

## 5.2 Confirm Ownership or Easement Status
Record:
- Fee‑simple  
- Conservation easement  
- Trail easement  
- Partnership land  

## 5.3 Confirm Access Points
Identify:
- Trailheads  
- Parking areas  
- Boat launches  
- Scenic overlooks  

## 5.4 Naming
Use the **nonprofit‑published name** as authoritative.  
If multiple names appear → record all in metadata.

------------------------------------------------------------
# 6. DECISION RULES FOR ENTITY CREATION

### 6.1 Site Creation
A nonprofit feature becomes a **Site** if:
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

### 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a preserve  
- A named natural area, management zone, or recreation area is documented  
- A named trail area, overlook area, or habitat unit is identity‑bearing  

Do **not** surface:
- Amenities  
- Unnamed management zones  
- Stewardship work areas  

### 6.3 Trail Creation
Surface a **Trail** when:
- A named trail appears on nonprofit maps or brochures  
- A named trail appears in partnership announcements  
- A named trail appears in county GIS  

### 6.4 Trail Segment Creation
Surface **Trail Segments** when:
- Segment‑level geometry exists in county GIS  
- Segment identifiers appear in nonprofit maps  

### 6.5 Trail Network Creation
Surface a **Trail Network** when:
- A nonprofit manages a multi‑trail system  
- A greenway corridor includes multiple Trails  

### 6.6 Site Network Creation
Surface a **Site Network** when:
- A nonprofit manages a multi‑site conservation system  
- A watershed‑scale or corridor‑scale network is documented  

### 6.7 Access Point Creation
Surface an **Access Point** when:
- It appears on nonprofit maps  
- It appears in nonprofit brochures  
- It appears in county GIS  
- It appears in partnership announcements  

Access Points must include raw values only:
- Name or descriptive label  
- Access Point Type (raw)  
- County list (raw)  
- Parent entity  
- Source(s)  
- Notes  

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

The Nonprofit Tier **must** surface:
- All fee‑simple preserves  
- All identity‑bearing conservation easements  
- All nonprofit‑managed Trails  
- All nonprofit‑managed Trail Segments  
- All nonprofit‑managed Access Points  
- All named trail corridors and greenways  
- All multi‑site conservation systems  

The Nonprofit Tier **may** surface:
- Nonprofit‑managed Trail Networks  
- Nonprofit‑managed Site Networks  
- Watershed‑scale or corridor‑scale systems  
- Partnership lands (if identity‑bearing)  

------------------------------------------------------------
# 8. LOGGING REQUIREMENTS

Each discovered entity must include:
- Full **Discovery Metadata v3.2.2**  
- All raw source references  
- All counties (raw)  
- All conflicts and uncertainties  
- All parent relationships  
- All geometry (if available)  

All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each nonprofit entity must output a **Raw Candidate Record** conforming to:
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- The appropriate Schema Module v3.2.2  
- The appropriate Vocabulary Module v3.2.2  

No normalized fields may appear in Tier 7 output.

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

- This module is **Nonprofit Conservation Landholders Discovery Sub‑Procedure v3.2.2**.  
- Updates to land trust directories or conservation practices may result in v3.3, v3.4, etc.  
- Any change to tier order or workflow must be made in the  
  **Discovery Protocol Module v3.2.2**.

------------------------------------------------------------
# END OF NONPROFIT CONSERVATION LANDHOLDERS DISCOVERY SUB‑PROCEDURE v3.2.2