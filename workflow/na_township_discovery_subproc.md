# TOWNSHIP DISCOVERY SUB‑PROCEDURE v3.1
(Ohio Townships, Township Websites, Township‑Hosted Pages, Township Recreation Assets)

Tier 5 of the Discovery Protocol Module v3.1.

Townships in Ohio vary widely in capacity, web presence, and documentation. Some
maintain full recreation pages; others have no website at all. Township parks may
exist even when no recreation department exists, and many township parks are hidden
on non‑indexed subpages.

This module defines the **detailed rules** for Tier 5 discovery across all seven
entity types.

------------------------------------------------------------
# 1. PURPOSE
This sub‑procedure defines how the system must:

- Identify township‑owned or township‑managed **Sites**
- Identify township‑managed **Sub‑Sites**
- Identify township‑managed **Trails** and **Trail Segments**
- Identify township‑managed **Trail Networks** (rare)
- Identify township‑managed **Site Networks** (rare)
- Identify township‑managed **Access Points**
- Identify township recreation assets even when no recreation department exists
- Identify township pages hosted by the county
- Surface uncertainty and conflicts
- Produce Raw Candidate Records and Discovery Metadata

This module is referenced **only** by the Discovery Protocol Module v3.1.

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
- **Sub‑Sites**
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
- Open Space
- Green Space
- Playground
- Shelter
- Picnic Area

Township websites often have:
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
Township Facebook pages are **not authoritative** unless:
- Explicitly designated as official by the township  
- Linked from the township website  
- Linked from the county website  

If designated official:
- Scan for park announcements
- Facility openings
- Trail access information

If not designated official → **exclude**.

------------------------------------------------------------
# 4. SITE DISCOVERY RULES

A township Site must be surfaced if:

### ✔ 4.1 It is owned or managed by the township  
### ✔ 4.2 It appears on the township website  
### ✔ 4.3 It appears on a county‑hosted township page  
### ✔ 4.4 It appears in township meeting minutes  
### ✔ 4.5 It is identity‑bearing (named, mapped, or designated)  

### ❌ Exclude:
- Township halls
- Administrative buildings
- Cemeteries (unless designated natural areas)
- Maintenance yards

### 4.6 Hidden or Non‑Indexed Pages
Township parks may appear on:
- Unlinked HTML pages
- PDF brochures
- Old or archived pages

These must be included if authoritative.

------------------------------------------------------------
# 5. SUB‑SITE DISCOVERY RULES

A Sub‑Site must be surfaced when:
- A named internal unit exists within a township Site
- A recreation area, facility, or natural area is identity‑bearing
- A playground, shelter area, or lake area is formally named

Do **not** surface:
- Amenities without identity
- Temporary zones
- Unnamed management areas

------------------------------------------------------------
# 6. TRAIL DISCOVERY RULES

Surface a **Trail** when:
- A named trail appears on township or county‑hosted pages
- A named trail appears in meeting minutes
- A named trail appears in township GIS (rare)

------------------------------------------------------------
# 7. TRAIL SEGMENT DISCOVERY RULES

Surface **Trail Segments** when:
- Segment‑level geometry exists in township or county GIS
- Segment identifiers appear in maps or plans

------------------------------------------------------------
# 8. TRAIL NETWORK DISCOVERY RULES

Surface a **Trail Network** when:
- A township‑managed multi‑trail system exists
- A greenway corridor spans multiple Trails

Rare but must be captured.

------------------------------------------------------------
# 9. SITE NETWORK DISCOVERY RULES

Surface a **Site Network** when:
- A township‑managed multi‑site system exists
- A conservation or greenway network is formally documented

Very rare but must be captured.

------------------------------------------------------------
# 10. ACCESS POINT DISCOVERY RULES

Township Access Points must be surfaced when:
- They appear on township pages
- They appear on county‑hosted township pages
- They appear in township meeting minutes
- They appear in township GIS (rare)

Access Points must include:
- Name or descriptive label
- Access Point Type (raw)
- Township
- County
- Parent entity (Site, Sub‑Site, Trail, Trail Segment)
- Source(s)
- Notes

These are passed to the Access Point Discovery Sub‑Procedure v3.1.

------------------------------------------------------------
# 11. TOWNSHIP‑ANCHORED VERIFICATION (MANDATORY)

For each township entity:

## 11.1 Confirm Township Boundaries
- Verify the feature lies within the township
- Segment multi‑township features

## 11.2 Confirm Management Authority
Record:
- Township name
- Co‑managers (if any)

## 11.3 Confirm Access Points
Identify:
- Trailheads
- Parking areas
- Boat launches
- Fishing access
- Scenic overlooks
- Playgrounds
- Shelters

## 11.4 Naming Consistency
Use the **township‑published name** as authoritative.

------------------------------------------------------------
# 12. LOGGING REQUIREMENTS

For each township entity, log:
- Township
- Entity name
- Entity type (Site, Sub‑Site, Trail, Trail Segment, Trail Network, Site Network, Access Point)
- Source dataset
- URL or reference
- Access type (if applicable)
- Notes on co‑management
- Discovery Tier: **5**
- Uncertainty or conflicts

Each county must also produce:
- Township Sites Found
- Sub‑Sites Found
- Trails Found
- Trail Segments Found
- Trail Networks Found
- Site Networks Found
- Access Points Found
- Township Pages Used
- Township Meeting Minutes Used
- Sources Checked
- Notes

------------------------------------------------------------
# 13. OUTPUT FORMAT

### 13.1 Township Entities
Name:
Type: Site / Sub‑Site / Trail / Trail Segment / Trail Network / Site Network
Township:
County:
URL or Source:
Notes:
Discovery Tier: 5

### 13.2 Access Points
Name:
Type: Access Point
Access Point Type (raw):
Parent Entity:
Township:
County:
Source:
Notes:
Discovery Tier: 5

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
- This module is **Township Discovery Sub‑Procedure v3.1**.
- Updates to township governance practices or statewide township directories may result in v3.2, v3.3, etc.
- Any change to tier order or high‑level workflow must be made in the Discovery Protocol Module v3.1.

------------------------------------------------------------
# END OF TOWNSHIP DISCOVERY SUB‑PROCEDURE v3.1