# MUNICIPAL DISCOVERY SUB‑PROCEDURE v3.1
(Cities, Villages, Incorporated Municipalities, and County‑Hosted Municipal Pages)

Tier 6 of the Discovery Protocol Module v3.1.

Municipalities in Ohio vary dramatically in size, capacity, and web presence. Some
maintain full parks & recreation departments; others have no recreation pages at all.
Municipal parks may exist even when no recreation department exists, and many
municipal parks are hidden on non‑indexed subpages.

This module defines the **detailed rules** for Tier 6 discovery across all seven
entity types.

------------------------------------------------------------
# 1. PURPOSE
This sub‑procedure defines how the system must:

- Identify municipal‑owned or municipal‑managed **Sites**
- Identify municipal‑managed **Sub‑Sites**
- Identify municipal‑managed **Trails** and **Trail Segments**
- Identify municipal‑managed **Trail Networks** (rare)
- Identify municipal‑managed **Site Networks** (rare)
- Identify municipal‑managed **Access Points**
- Identify municipal parks even when no recreation department exists
- Identify municipal pages hosted by the county
- Surface uncertainty and conflicts
- Produce Raw Candidate Records and Discovery Metadata

This module is referenced **only** by the Discovery Protocol Module v3.1.

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
- **Sub‑Sites**
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
- Open Space
- Green Space
- Playground
- Shelter
- Picnic Area
- Natural Area
- Trail

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
Municipal Facebook pages are **not authoritative** unless:
- Explicitly designated as official by the municipality  
- Linked from the municipal website  
- Linked from the county website  

If designated official:
- Scan for park announcements
- Facility openings
- Trail access information

If not designated official → **exclude**.

------------------------------------------------------------
# 4. SITE DISCOVERY RULES

A municipal Site must be surfaced if:

### ✔ 4.1 It is owned or managed by the municipality  
### ✔ 4.2 It appears on the municipal website  
### ✔ 4.3 It appears on a county‑hosted municipal page  
### ✔ 4.4 It appears in municipal planning documents  
### ✔ 4.5 It appears in municipal meeting minutes  
### ✔ 4.6 It is identity‑bearing (named, mapped, or designated)  

### ❌ Exclude:
- City halls
- Administrative buildings
- Cemeteries (unless designated natural areas)
- Maintenance yards

### 4.7 Hidden or Non‑Indexed Pages
Municipal parks may appear on:
- Unlinked HTML pages
- PDF brochures
- Old or archived pages

These must be included if authoritative.

------------------------------------------------------------
# 5. SUB‑SITE DISCOVERY RULES

A Sub‑Site must be surfaced when:
- A named internal unit exists within a municipal Site
- A recreation area, facility, or natural area is identity‑bearing
- A playground, shelter area, or lake area is formally named

Do **not** surface:
- Amenities without identity
- Temporary zones
- Unnamed management areas

------------------------------------------------------------
# 6. TRAIL DISCOVERY RULES

Surface a **Trail** when:
- A named trail appears on municipal or county‑hosted pages
- A named trail appears in planning documents
- A named trail appears in meeting minutes
- A named trail appears in municipal GIS (rare)

------------------------------------------------------------
# 7. TRAIL SEGMENT DISCOVERY RULES

Surface **Trail Segments** when:
- Segment‑level geometry exists in municipal or county GIS
- Segment identifiers appear in maps or plans

------------------------------------------------------------
# 8. TRAIL NETWORK DISCOVERY RULES

Surface a **Trail Network** when:
- A municipal‑managed multi‑trail system exists
- A greenway corridor spans multiple Trails

Rare but must be captured.

------------------------------------------------------------
# 9. SITE NETWORK DISCOVERY RULES

Surface a **Site Network** when:
- A municipal‑managed multi‑site system exists
- A conservation or greenway network is formally documented

Very rare but must be captured.

------------------------------------------------------------
# 10. ACCESS POINT DISCOVERY RULES

Municipal Access Points must be surfaced when:
- They appear on municipal pages
- They appear on county‑hosted municipal pages
- They appear in municipal planning documents
- They appear in municipal meeting minutes
- They appear in municipal GIS (rare)

Access Points must include:
- Name or descriptive label
- Access Point Type (raw)
- Municipality
- County
- Parent entity (Site, Sub‑Site, Trail, Trail Segment)
- Source(s)
- Notes

These are passed to the Access Point Discovery Sub‑Procedure v3.1.

------------------------------------------------------------
# 11. MUNICIPAL‑ANCHORED VERIFICATION (MANDATORY)

For each municipal entity:

## 11.1 Confirm Municipal Boundaries
- Verify the feature lies within the municipality
- Segment multi‑municipal features

## 11.2 Confirm Management Authority
Record:
- Municipality name
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
Use the **municipal‑published name** as authoritative.

------------------------------------------------------------
# 12. LOGGING REQUIREMENTS

For each municipal entity, log:
- Municipality
- Entity name
- Entity type (Site, Sub‑Site, Trail, Trail Segment, Trail Network, Site Network, Access Point)
- Source dataset
- URL or reference
- Access type (if applicable)
- Notes on co‑management
- Discovery Tier: **6**
- Uncertainty or conflicts

Each county must also produce:
- Municipal Sites Found
- Sub‑Sites Found
- Trails Found
- Trail Segments Found
- Trail Networks Found
- Site Networks Found
- Access Points Found
- Municipal Pages Used
- Municipal Planning Documents Used
- Municipal Meeting Minutes Used
- Sources Checked
- Notes

------------------------------------------------------------
# 13. OUTPUT FORMAT

### 13.1 Municipal Entities
Name:
Type: Site / Sub‑Site / Trail / Trail Segment / Trail Network / Site Network
Municipality:
County:
URL or Source:
Notes:
Discovery Tier: 6

### 13.2 Access Points
Name:
Type: Access Point
Access Point Type (raw):
Parent Entity:
Municipality:
County:
Source:
Notes:
Discovery Tier: 6

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
- This module is **Municipal Discovery Sub‑Procedure v3.1**.
- Updates to municipal governance practices or statewide municipal directories may result in v3.2, v3.3, etc.
- Any change to tier order or high‑level workflow must be made in the Discovery Protocol Module v3.1.

------------------------------------------------------------
# END OF MUNICIPAL DISCOVERY SUB‑PROCEDURE v3.1