# COUNTY DISCOVERY SUB‑PROCEDURE v3.1
(County Government, County GIS, County Recreation Assets, County‑Hosted Pages)

Tier 4 of the Discovery Protocol Module v3.1.

County‑level discovery is one of the most authoritative and information‑rich tiers.
Counties maintain GIS datasets, recreation pages, planning documents, and in many
cases host municipal or township subpages. This tier must surface all identity‑bearing
county‑managed entities across the full 7‑entity ontology.

This module defines the **detailed rules** for Tier 4 discovery across all seven
entity types.

------------------------------------------------------------
# 1. PURPOSE
This sub‑procedure defines how the system must:

- Identify all county‑owned or county‑managed **Sites**
- Identify county‑managed **Sub‑Sites**
- Identify county‑managed **Trails** and **Trail Segments**
- Identify county‑managed **Trail Networks** (if any)
- Identify county‑managed **Site Networks** (rare but possible)
- Identify county‑managed **Access Points**
- Identify county‑hosted municipal/township pages
- Identify county recreation assets
- Use county GIS as a primary discovery source
- Log uncertainty and boundary cases
- Produce Raw Candidate Records and Discovery Metadata

This module is referenced **only** by the Discovery Protocol Module v3.1.

------------------------------------------------------------
# 2. SCOPE
This sub‑procedure applies to:

- County government websites
- County GIS systems
- County recreation departments
- County planning commissions
- County commissioners’ pages
- County‑hosted municipal/township pages
- County tourism/visitors bureau pages
- County‑level trail plans

It governs discovery of:

- **Sites**
- **Sub‑Sites**
- **Trails**
- **Trail Segments**
- **Trail Networks**
- **Site Networks**
- **Access Points**

This tier sits **below Park Districts** and **above Townships**.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 County Government Website
Check for:
- Parks
- Recreation
- Facilities
- Natural Resources
- Open Space
- Conservation
- Trails
- Outdoor Recreation

Scan all subpages, including:
- Hidden or unlinked pages
- PDF brochures
- County‑hosted municipal/township pages
- County recreation guides

## 3.2 County GIS (Primary Authoritative Source)
Check for layers including:
- Parks (→ Sites)
- Open space (→ Sites)
- Conservation lands (→ Sites)
- Trails (→ Trails, Trail Segments)
- Recreation facilities (→ Sites or Sub‑Sites)
- Boat launches (→ Access Points)
- Fishing access (→ Access Points)
- Hunting access (→ Access Points)
- County‑owned parcels (→ Sites)

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
# 4. SITE DISCOVERY RULES

A county Site must be surfaced if:

### ✔ 4.1 It is owned or managed by the county  
### ✔ 4.2 It appears in county GIS  
### ✔ 4.3 It appears on county recreation pages  
### ✔ 4.4 It appears in county planning documents  
### ✔ 4.5 It is identity‑bearing (named, mapped, or designated)  

### ❌ Exclude:
- Administrative offices
- Maintenance yards
- Non‑public facilities

### 4.6 Multi‑County Sites
If a Site spans multiple counties:
- Create one Raw Candidate Record per county
- Use the same name
- Segment GPS and notes if available

------------------------------------------------------------
# 5. SUB‑SITE DISCOVERY RULES

A Sub‑Site must be surfaced when:
- A named internal unit exists within a county Site
- A recreation area, facility, or natural area is identity‑bearing
- A campground, lake area, or management zone is named

Do **not** surface:
- Amenities (playgrounds, shelters, overlooks)
- Temporary zones
- Unnamed management areas

------------------------------------------------------------
# 6. COUNTY TRAIL SYSTEM DISCOVERY RULES

A county trail system becomes a **Trail** or **Trail Network** if:
- It is named and mapped
- It has one or more Access Points
- It is identity‑bearing
- It is not fully contained within a single park

Segment multi‑county trails by county.

------------------------------------------------------------
# 7. TRAIL SEGMENT DISCOVERY RULES

Surface Trail Segments when:
- Segment‑level geometry exists in county GIS
- Segment identifiers or names appear in maps or plans
- Trails are broken into operational sections

------------------------------------------------------------
# 8. SITE NETWORK DISCOVERY RULES

Surface a **Site Network** when:
- A county‑managed multi‑site system exists
- A greenway corridor spans multiple Sites
- A conservation network is formally documented

These are rare but must be captured.

------------------------------------------------------------
# 9. ACCESS POINT DISCOVERY RULES

County Access Points must be surfaced when:
- They appear in county GIS
- They appear on county recreation maps
- They appear in county brochures
- They appear in county trail plans

Access Points must include:
- Name or descriptive label
- Access Point Type (raw)
- County
- Parent entity (Site, Sub‑Site, Trail, Trail Segment)
- Source(s)
- Notes

These are passed to the Access Point Discovery Sub‑Procedure v3.1.

------------------------------------------------------------
# 10. COUNTY‑HOSTED MUNICIPAL/TOWNSHIP PAGES

If the county hosts municipal or township pages:
- Treat them as authoritative for municipal/township discovery
- Surface any parks, preserves, trails, or facilities listed
- Log the county as the source of the municipal/township information

These discoveries remain **Tier 4** because the county is the authoritative host.

------------------------------------------------------------
# 11. COUNTY‑ANCHORED VERIFICATION (MANDATORY)

For each county entity:

## 11.1 Confirm County Boundaries
- Verify the feature lies within the county
- Segment multi‑county features

## 11.2 Confirm Management Authority
Record:
- County department
- Co‑managers (if any)

## 11.3 Confirm Access Points
Identify:
- Trailheads
- Parking areas
- Boat launches
- Fishing access
- Hunting access
- Scenic overlooks

## 11.4 Naming Consistency
Use the **county‑published name** as authoritative.

------------------------------------------------------------
# 12. LOGGING REQUIREMENTS

For each county entity, log:
- County
- Entity name
- Entity type (Site, Sub‑Site, Trail, Trail Segment, Trail Network, Site Network, Access Point)
- Source dataset
- URL or reference
- Access type (if applicable)
- Notes on co‑management
- Discovery Tier: **4**
- Uncertainty or conflicts

Each county must also produce:
- County Sites Found
- Sub‑Sites Found
- Trails Found
- Trail Segments Found
- Trail Networks Found
- Site Networks Found
- Access Points Found
- County‑Hosted Municipal/Township Pages Used
- Sources Checked
- Notes

------------------------------------------------------------
# 13. OUTPUT FORMAT

### 13.1 County Entities
Name:
Type: Site / Sub‑Site / Trail / Trail Segment / Trail Network / Site Network
County:
URL or Source:
Notes:
Discovery Tier: 4

### 13.2 Access Points
Name:
Type: Access Point
Access Point Type (raw):
Parent Entity:
County:
Source:
Notes:
Discovery Tier: 4

------------------------------------------------------------
# 14. INTEGRATION POINTS

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
# 15. VERSIONING
- This module is **County Discovery Sub‑Procedure v3.1**.
- Updates to county GIS standards or statewide county practices may result in v3.2, v3.3, etc.
- Any change to tier order or high‑level workflow must be made in the Discovery Protocol Module v3.1.

------------------------------------------------------------
# END OF COUNTY DISCOVERY SUB‑PROCEDURE v3.1