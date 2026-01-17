# LAND TRUST & CONSERVANCY DISCOVERY SUB‑PROCEDURE v3.1
(Land Trusts, Conservancies, Foundations, Nonprofit Conservation Organizations)

Tier 7 of the Discovery Protocol Module v3.1.

Land trusts and conservancies are essential contributors to Ohio’s natural areas
landscape. They hold fee‑simple preserves, conservation easements, trail corridors,
and partnership lands. Their holdings are often **not** represented in county or
state datasets, making this tier critical.

This module defines the **detailed rules** for Tier 7 discovery across all seven
entity types.

------------------------------------------------------------
# 1. PURPOSE
This sub‑procedure defines how the system must:

- Identify all land trust and conservancy **Sites**
- Identify **Sub‑Sites** within land trust preserves
- Identify **Trails** and **Trail Segments** on land trust holdings
- Identify **Trail Networks** (rare but possible)
- Identify **Site Networks** (e.g., multi‑site conservation corridors)
- Identify **Access Points** associated with land trust holdings
- Identify fee‑simple preserves
- Identify conservation easements that qualify as Sites
- Identify trail corridors and greenways
- Distinguish between public‑access and non‑public‑access holdings
- Identify co‑managed Sites
- Log uncertainty and boundary cases
- Produce Raw Candidate Records and Discovery Metadata

This module is referenced **only** by the Discovery Protocol Module v3.1.

------------------------------------------------------------
# 2. SCOPE
This sub‑procedure applies to:

- Local land trusts
- Regional land trusts
- Statewide land trusts
- National land trusts
- Conservancies and foundations
- Nonprofit conservation organizations
- Land trust consortiums and alliances

It governs discovery of:

- **Sites**
- **Sub‑Sites**
- **Trails**
- **Trail Segments**
- **Trail Networks**
- **Site Networks**
- **Access Points**

This tier sits **below Municipal** and **above Private & Organization‑Based**.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 Land Trust Official Websites
Check for:
- Preserves
- Protected Lands
- Our Lands
- Conservation Areas
- Nature Preserves
- Public Access
- Hiking Trails
- Stewardship

Scan:
- All preserve pages
- All project pages
- All maps
- All PDF brochures
- All stewardship reports

## 3.2 Land Trust Alliance (LTA) Directory
Check for:
- Member organizations
- Regional affiliates
- Contact information
- Links to official websites

## 3.3 County Auditor / GIS (Parcel Verification)
Land trust holdings often appear as:
- Fee‑simple parcels
- Conservation easements
- Trail easements
- Partnership lands

GIS is essential for:
- Confirming county boundaries
- Confirming ownership
- Confirming easement status
- Confirming access points

## 3.4 Statewide & Regional Conservation Networks
Check:
- ONAPA
- Regional conservation partnerships
- Watershed groups
- Greenway coalitions

These often list:
- Co‑managed preserves
- Joint acquisitions
- Trail corridors

## 3.5 Federal & State Partners
Land trusts often partner with:
- ODNR
- USFWS
- USACE
- Local park districts
- Municipalities

These partnerships must be logged.

------------------------------------------------------------
# 4. SITE DISCOVERY RULES

A land trust Site must be surfaced if:

### ✔ 4.1 It is owned in fee‑simple by the land trust  
### ✔ 4.2 It is a conservation easement with **public access**  
### ✔ 4.3 It is a conservation easement with **identity‑bearing status**  
### ✔ 4.4 It appears on the land trust website  
### ✔ 4.5 It appears in county GIS as land‑trust‑owned  
### ✔ 4.6 It appears in partnership announcements  
### ✔ 4.7 It is identity‑bearing (named, mapped, or designated)  

### ❌ Exclude:
- Conservation easements with **no public access** and **no identity‑bearing role**
- Private lands with land trust covenants but no public role
- Administrative offices
- Stewardship centers not open to the public

### 4.8 Multi‑County Sites
If a Site spans multiple counties:
- Create one Raw Candidate Record per county
- Use the same name
- Segment GPS and notes if available

------------------------------------------------------------
# 5. SUB‑SITE DISCOVERY RULES

Surface a **Sub‑Site** when:
- A named internal unit exists within a preserve
- A named natural area, management zone, or recreation area is documented
- A named trail area, overlook area, or habitat unit is identity‑bearing

Do **not** surface:
- Amenities
- Unnamed management zones
- Stewardship work areas

------------------------------------------------------------
# 6. CONSERVATION EASEMENT RULES

A conservation easement becomes a **Site** only if:
- It has public access
- It is identity‑bearing
- It is named or mapped
- It has a trail, overlook, or access point
- It is part of a greenway or corridor

Exclude:
- Private easements with no public access
- Agricultural easements with no recreation role
- Scenic easements with no access

------------------------------------------------------------
# 7. TRAIL CORRIDOR DISCOVERY RULES

Land trusts often hold:
- Trail easements
- Greenway corridors
- Linear preserves

A trail corridor becomes a **Site** if:
- It is named
- It is mapped
- It has one or more Access Points
- It is identity‑bearing

Segment multi‑county corridors by county.

------------------------------------------------------------
# 8. TRAIL DISCOVERY RULES

Surface a **Trail** when:
- A named trail appears on land trust maps or brochures
- A named trail appears in partnership announcements
- A named trail appears in county GIS

------------------------------------------------------------
# 9. TRAIL SEGMENT DISCOVERY RULES

Surface **Trail Segments** when:
- Segment‑level geometry exists in county GIS
- Segment identifiers appear in land trust maps

------------------------------------------------------------
# 10. TRAIL NETWORK DISCOVERY RULES

Surface a **Trail Network** when:
- A land trust manages a multi‑trail system
- A greenway corridor includes multiple Trails

Rare but must be captured.

------------------------------------------------------------
# 11. SITE NETWORK DISCOVERY RULES

Surface a **Site Network** when:
- A land trust manages a multi‑site conservation system
- A watershed‑scale or corridor‑scale network is documented

------------------------------------------------------------
# 12. ACCESS POINT DISCOVERY RULES

Land trust Access Points must be surfaced when:
- They appear on land trust maps
- They appear in land trust brochures
- They appear in county GIS
- They appear in partnership announcements

Access Points must include:
- Name or descriptive label
- Access Point Type (raw)
- County
- Parent entity (Site, Sub‑Site, Trail, Trail Segment)
- Source(s)
- Notes

These are passed to the Access Point Discovery Sub‑Procedure v3.1.

------------------------------------------------------------
# 13. CO‑MANAGEMENT RULES

Land trust Sites are often co‑managed with:
- Park districts
- Municipalities
- Counties
- ODNR
- Federal agencies

Record:
- Primary manager
- Co‑managers
- Notes on stewardship agreements

------------------------------------------------------------
# 14. COUNTY‑ANCHORED VERIFICATION (MANDATORY)

For each land trust entity:

## 14.1 Confirm County Boundaries
- Verify the feature lies within the county
- Segment multi‑county features

## 14.2 Confirm Ownership or Easement Status
Record:
- Fee‑simple
- Conservation easement
- Trail easement
- Partnership land

## 14.3 Confirm Access Points
Identify:
- Trailheads
- Parking areas
- Boat launches
- Scenic overlooks

## 14.4 Naming Consistency
Use the **land trust‑published name** as authoritative.

------------------------------------------------------------
# 15. LOGGING REQUIREMENTS

For each land trust entity, log:
- Land trust name
- Entity name
- Entity type (Site, Sub‑Site, Trail, Trail Segment, Trail Network, Site Network, Access Point)
- County
- Ownership type
- Source dataset
- URL or reference
- Access type (if applicable)
- Notes on co‑management
- Discovery Tier: **7**
- Uncertainty or conflicts

Each county must also produce:
- Land Trust Sites Found
- Sub‑Sites Found
- Trails Found
- Trail Segments Found
- Trail Networks Found
- Site Networks Found
- Access Points Found
- Conservation Easements Considered
- Trail Corridors Found
- Sources Checked
- Notes

------------------------------------------------------------
# 16. OUTPUT FORMAT

### 16.1 Land Trust Entities
Name:
Type: Site / Sub‑Site / Trail / Trail Segment / Trail Network / Site Network
Land Trust:
County:
Ownership Type:
URL or Source:
Notes:
Discovery Tier: 7

### 16.2 Access Points
Name:
Type: Access Point
Access Point Type (raw):
Parent Entity:
Land Trust:
County:
Source:
Notes:
Discovery Tier: 7

------------------------------------------------------------
# 17. INTEGRATION POINTS

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
# 18. VERSIONING
- This module is **Land Trust & Conservancy Discovery Sub‑Procedure v3.1**.
- Updates to land trust directories or conservation practices may result in v3.2, v3.3, etc.
- Any change to tier order or high‑level workflow must be made in the Discovery Protocol Module v3.1.

------------------------------------------------------------
# END OF LAND TRUST & CONSERVANCY DISCOVERY SUB‑PROCEDURE v3.1