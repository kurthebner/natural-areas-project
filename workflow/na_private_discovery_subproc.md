# PRIVATE & ORGANIZATION‑BASED DISCOVERY SUB‑PROCEDURE v3.1
(Private Nature Preserves, Camps, Retreat Centers, Scout Camps, Church Camps, Fraternal Lands, HOA Open Space, Corporate Lands)

Tier 8 of the Discovery Protocol Module v3.1.

Private and organization‑based lands form the final tier of discovery. These lands are
highly variable, inconsistently documented, and often partially accessible. Some are
fully public; some are seasonally public; some are private but identity‑bearing; some
are private with no public role.

This module defines the **detailed rules** for Tier 8 discovery across all seven
entity types.

------------------------------------------------------------
# 1. PURPOSE
This sub‑procedure defines how the system must:

- Identify private or organization‑based **Sites**
- Identify **Sub‑Sites** within private holdings
- Identify private **Trails** and **Trail Segments**
- Identify private **Trail Networks** (rare)
- Identify private **Site Networks** (rare)
- Identify private **Access Points** when public or limited access exists
- Distinguish between public, limited, and private access
- Identify identity‑bearing private natural areas
- Identify private preserves owned by nonprofits or foundations
- Log uncertainty and boundary cases
- Produce Raw Candidate Records and Discovery Metadata

This module is referenced **only** by the Discovery Protocol Module v3.1.

------------------------------------------------------------
# 2. SCOPE
This sub‑procedure applies to:

- Private nature preserves
- Private campgrounds
- Church camps
- Scout camps
- Fraternal organization lands
- HOA open space
- Corporate campuses with natural areas
- Private hunting/fishing clubs
- Private retreat centers
- Private trail systems
- Private foundations with land holdings

It governs discovery of:

- **Sites**
- **Sub‑Sites**
- **Trails**
- **Trail Segments**
- **Trail Networks**
- **Site Networks**
- **Access Points**

This tier sits **below Land Trusts & Conservancies** and is the final discovery tier.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 Official Websites
Check for:
- Nature Preserve
- Camp
- Retreat Center
- Outdoor Center
- Hiking Trails
- Natural Area
- Open Space
- Wildlife Area

Scan:
- All facility pages
- All program pages
- All maps
- All PDF brochures

## 3.2 County Auditor / GIS (Parcel Verification)
Private holdings often appear as:
- Private preserves
- Private campgrounds
- Private recreation areas
- HOA open space
- Corporate natural areas

GIS is essential for:
- Confirming county boundaries
- Confirming ownership
- Confirming access points
- Confirming parcel extent

## 3.3 Statewide & Regional Directories
Check:
- Ohio campground directories
- Ohio tourism directories
- Regional recreation guides
- Scout council property lists
- Church camp directories
- Fraternal organization property lists

## 3.4 Organizational Partners
Private lands may appear in:
- Land trust partnership announcements
- County planning documents
- Regional trail plans
- Watershed group projects

## 3.5 Social Media (Conditional)
Private organization social media pages are **not authoritative** unless:
- Explicitly designated as official
- Linked from the organization’s website
- Linked from a county or municipal website

If designated official:
- Scan for park/trail announcements
- Scan for access information

If not designated official → **exclude**.

------------------------------------------------------------
# 4. SITE DISCOVERY RULES

A private or organization‑based Site must be surfaced if:

### ✔ 4.1 It is identity‑bearing  
(named, mapped, or designated)

### ✔ 4.2 It has public or limited public access  
(even if seasonal or fee‑based)

### ✔ 4.3 It appears in authoritative directories  
(e.g., official camp directories, scout council listings)

### ✔ 4.4 It appears in county GIS as a recreation or natural area

### ✔ 4.5 It is a private preserve owned by a nonprofit or foundation

### ✔ 4.6 It is a private trail system with public access

### ✔ 4.7 It is a private campground with natural area components

### ✔ 4.8 It is a private retreat center with trails or natural areas

### ❌ Exclude:
- Private lands with no public access and no identity‑bearing role
- HOA open space with no public access
- Corporate campuses with no public access
- Private hunting clubs with no public access
- Private farms with no recreation role
- Private residences

### 4.9 Limited‑Access Sites
If access is:
- Seasonal
- Fee‑based
- Reservation‑only
- Program‑only

→ **Include**, but record access limitations in Notes.

------------------------------------------------------------
# 5. SUB‑SITE DISCOVERY RULES

Surface a **Sub‑Site** when:
- A named internal unit exists within a private Site
- A named natural area, recreation area, or facility is documented
- A named lake area, trail area, or program area is identity‑bearing

Do **not** surface:
- Amenities without identity
- Temporary zones
- Unnamed management areas

------------------------------------------------------------
# 6. PRIVATE TRAIL SYSTEM DISCOVERY RULES

A private trail system becomes a **Trail** or **Trail Network** if:
- It is named
- It is mapped
- It has public or limited public access
- It is identity‑bearing

Segment multi‑county trails by county.

------------------------------------------------------------
# 7. TRAIL SEGMENT DISCOVERY RULES

Surface **Trail Segments** when:
- Segment‑level geometry exists in county GIS
- Segment identifiers appear in maps or brochures

------------------------------------------------------------
# 8. SITE NETWORK DISCOVERY RULES

Surface a **Site Network** when:
- A private organization manages a multi‑site system
- A corridor‑scale or campus‑scale network is documented

Rare but must be captured.

------------------------------------------------------------
# 9. ACCESS POINT DISCOVERY RULES

Private Access Points must be surfaced when:
- They appear on official maps
- They appear in brochures
- They appear in county GIS
- They appear in directories
- They appear in partnership announcements

Access Points must include:
- Name or descriptive label
- Access Point Type (raw)
- County
- Parent entity (Site, Sub‑Site, Trail, Trail Segment)
- Access level (raw)
- Source(s)
- Notes (including access limitations)

These are passed to the Access Point Discovery Sub‑Procedure v3.1.

------------------------------------------------------------
# 10. ACCESS LEVEL CLASSIFICATION (RAW)

Discovery must record **raw access level**, not normalized values:

- Public
- Limited Public
- Fee‑Based
- Seasonal
- Reservation‑Only
- Program‑Only
- Private (No Access)

Normalization assigns final values.

------------------------------------------------------------
# 11. COUNTY‑ANCHORED VERIFICATION (MANDATORY)

For each private entity:

## 11.1 Confirm County Boundaries
- Verify the feature lies within the county
- Segment multi‑county features

## 11.2 Confirm Ownership
Record:
- Private individual
- Private organization
- Nonprofit
- Foundation
- Fraternal organization
- Church
- Scout council
- HOA
- Corporate entity

## 11.3 Confirm Access Points
Identify:
- Trailheads
- Parking areas
- Boat launches
- Scenic overlooks
- Camp entrances
- Program‑only entrances

## 11.4 Naming Consistency
Use the **organization’s published name** as authoritative.

------------------------------------------------------------
# 12. LOGGING REQUIREMENTS

For each private entity, log:
- Organization name
- Entity name
- Entity type (Site, Sub‑Site, Trail, Trail Segment, Trail Network, Site Network, Access Point)
- County
- Ownership type
- Access level (raw)
- Source dataset
- URL or reference
- Notes on access limitations
- Discovery Tier: **8**
- Uncertainty or conflicts

Each county must also produce:
- Private Sites Found
- Sub‑Sites Found
- Trails Found
- Trail Segments Found
- Trail Networks Found
- Site Networks Found
- Access Points Found
- Private Trail Systems Found
- Sources Checked
- Notes

------------------------------------------------------------
# 13. OUTPUT FORMAT

### 13.1 Private Entities
Name:
Type: Site / Sub‑Site / Trail / Trail Segment / Trail Network / Site Network
Organization:
County:
Ownership Type:
Access Level (raw):
URL or Source:
Notes:
Discovery Tier: 8

### 13.2 Access Points
Name:
Type: Access Point
Access Point Type (raw):
Parent Entity:
Organization:
County:
Access Level (raw):
Source:
Notes:
Discovery Tier: 8

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
- This module is **Private & Organization‑Based Discovery Sub‑Procedure v3.1**.
- Updates to private recreation directories or organizational practices may result in v3.2, v3.3, etc.
- Any change to tier order or high‑level workflow must be made in the Discovery Protocol Module v3.1.

------------------------------------------------------------
# END OF PRIVATE & ORGANIZATION‑BASED DISCOVERY SUB‑PROCEDURE v3.1