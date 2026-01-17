# PARK DISTRICT LANDS DISCOVERY SUB‑PROCEDURE v3.1
(Park Districts, Metro Parks, Joint Recreation Districts)

Tier 3 of the Discovery Protocol Module v3.1.

Park districts and metro parks must be discovered using authoritative district‑level
sources, county‑anchored verification, and the full 7‑entity ontology. Ohio’s park
districts vary widely in size, governance, and documentation quality, but all must be
processed consistently.

This module defines the **detailed rules** for Tier 3 discovery across all seven
entity types.

------------------------------------------------------------
# 1. PURPOSE
This sub‑procedure defines how the system must:

- Identify all park district Sites
- Identify Sub‑Sites within district Sites
- Identify Trails, Trail Segments, and Trail Networks managed by districts
- Identify Site Networks (if district‑managed)
- Identify Access Points associated with district Sites
- Distinguish district management from municipal/county co‑management
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Candidate Records and Discovery Metadata

This module is referenced **only** by the Discovery Protocol Module v3.1.

------------------------------------------------------------
# 2. SCOPE
This sub‑procedure applies to:

- County park districts
- Metro parks systems
- Joint recreation districts
- Multi‑county park districts
- Park districts with special jurisdictions (e.g., watershed districts)

It governs the discovery of:

- **Sites** (parks, preserves, natural areas, recreation areas)
- **Sub‑Sites** within district Sites
- **Trails** on district lands
- **Trail Segments** on district lands
- **Trail Networks** (district‑managed multi‑trail systems)
- **Site Networks** (district‑managed multi‑site systems)
- **Access Points** associated with district Sites

------------------------------------------------------------
# 3. REQUIRED PARK DISTRICT SOURCES (ALL MANDATORY)

## 3.1 Official Park District Website
Check for:
- Park lists (→ Sites)
- Facility lists (→ Sub‑Sites)
- Trail pages (→ Trails)
- Trail maps (→ Trails, Trail Segments)
- Access point listings (→ Access Points)
- District‑managed programs or networks (→ Site Networks or Trail Networks)

## 3.2 Park District GIS
Check for:
- Park boundaries (→ Sites)
- Internal units (→ Sub‑Sites)
- Trail geometry (→ Trails, Trail Segments)
- Access point layers (→ Access Points)

## 3.3 Park District Brochures & Maps
Check for:
- Named parks (→ Sites)
- Named areas within parks (→ Sub‑Sites)
- Named trails (→ Trails)
- Trailheads, parking, boat access (→ Access Points)

## 3.4 County Auditor / County GIS
Check for:
- Parcels owned by the park district (→ Sites)
- Parcels leased or co‑managed (→ Sites or Sub‑Sites)

## 3.5 Partner Agencies
Check for:
- Co‑managed parks
- Joint recreation districts
- Shared trail systems

------------------------------------------------------------
# 4. COUNTY‑ANCHORED VERIFICATION (MANDATORY)

For each district entity identified, the system must verify:

## 4.1 Parcel Boundaries
- Confirm the entity lies within the county
- Segment multi‑county Sites by county

## 4.2 Management Authority
Record:
- Park district name
- Co‑management (municipal, township, county)
- Special agreements (e.g., ODNR + district)

## 4.3 Access Points
Identify:
- Trailheads
- Parking areas
- Boat ramps
- Scenic overlooks
- Recreation area entrances

Access Points must be surfaced as **Access Point candidates** and passed to the
Access Point Discovery Sub‑Procedure v3.1.

## 4.4 Naming Consistency
Use the **park district name** as the authoritative name.

------------------------------------------------------------
# 5. DECISION RULES FOR ENTITY CREATION

### 5.1 Site Creation
A district‑managed feature becomes a **Site** if:
- It is district‑owned or district‑managed
- It is identity‑bearing (named, mapped, or designated)
- It has public access or recreation infrastructure
- It influences Access Point logic

Examples:
- Parks
- Preserves
- Natural areas
- Recreation areas
- Greenway corridors (if identity‑bearing)

Exclude:
- Administrative offices
- Maintenance yards
- Non‑public parcels with no identity

### 5.2 Sub‑Site Creation
Create a **Sub‑Site** when:
- A named internal unit exists within a district Site
- A recreation area, campground, or facility is identity‑bearing

### 5.3 Trail Creation
Create a **Trail** when:
- A named trail appears in district datasets or maps

### 5.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment‑level geometry or identifiers exist

### 5.5 Trail Network Creation
Create a **Trail Network** when:
- A district‑managed multi‑trail system exists

Examples:
- Greenway systems
- Multi‑trail loops
- District‑wide trail networks

### 5.6 Site Network Creation
Create a **Site Network** when:
- A district‑managed multi‑site system exists

Examples:
- Watershed‑scale park networks
- District‑wide conservation networks

### 5.7 Access Point Creation
Create an **Access Point** when:
- A visitor‑facing entry location is documented

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

The Park District Tier **must** surface:

- All district‑managed Sites
- All identity‑bearing Sub‑Sites
- All district‑managed Trails
- All district‑managed Trail Segments
- All district‑managed Access Points

The Park District Tier **may** surface:

- District‑managed Trail Networks
- District‑managed Site Networks
- District‑managed easements

------------------------------------------------------------
# 7. LOGGING REQUIREMENTS

For each district entity, log:
- Park district name
- Entity name
- Entity type (Site, Sub‑Site, Trail, Trail Segment, Trail Network, Site Network)
- County
- Source dataset
- URL or reference
- Access type (if applicable)
- Notes on co‑management
- Discovery Tier: **3**
- Uncertainty or conflicts

Each county must also produce:
- District Sites Found
- Sub‑Sites Found
- Trails Found
- Trail Segments Found
- Trail Networks Found
- Site Networks Found
- Access Points Found
- Sources Checked
- Notes

------------------------------------------------------------
# 8. OUTPUT FORMAT

### 8.1 District Entities
Name:
Type: Site / Sub‑Site / Trail / Trail Segment / Trail Network / Site Network
Agency: Park District
County:
URL or Source:
Notes:
Discovery Tier: 3

### 8.2 Access Points
Name:
Type: Access Point
Access Point Type (raw):
Parent Entity:
County:
Source:
Notes:
Discovery Tier: 3

------------------------------------------------------------
# 9. INTEGRATION POINTS

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
# 10. VERSIONING
- This module is **Park District Lands Discovery Sub‑Procedure v3.1**.
- Updates to district datasets may result in v3.2, v3.3, etc.
- Any change to tier order or high‑level workflow must be made in the Discovery Protocol Module v3.1.

------------------------------------------------------------
# END OF PARK DISTRICT LANDS DISCOVERY SUB‑PROCEDURE v3.1