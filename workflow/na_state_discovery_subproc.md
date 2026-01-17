# STATE LANDS DISCOVERY SUB‑PROCEDURE v3.1
(ODNR Divisions, State Parks, State Forests, State Nature Preserves, State Wildlife Areas, Scenic Rivers)

Tier 2 of the Discovery Protocol Module v3.1.

State‑managed lands must be discovered using authoritative ODNR datasets, division‑level
sources, and county‑anchored verification. Ohio’s state lands include parks, forests,
wildlife areas, nature preserves, scenic rivers, and other ODNR‑managed units.

This module defines the **detailed rules** for Tier 2 discovery across all seven
entity types.

------------------------------------------------------------
# 1. PURPOSE
This sub‑procedure defines how the system must:

- Identify all state‑managed Sites
- Identify Sub‑Sites within state Sites
- Identify Trails, Trail Segments, and Trail Networks on state lands
- Identify Site Networks (e.g., Scenic River systems)
- Identify Access Points associated with state Sites
- Distinguish ODNR divisions and co‑management arrangements
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Candidate Records and Discovery Metadata

This module is referenced **only** by the Discovery Protocol Module v3.1.

------------------------------------------------------------
# 2. SCOPE
This sub‑procedure applies to:

- ODNR Division of Parks & Watercraft
- ODNR Division of Forestry
- ODNR Division of Wildlife
- ODNR Division of Natural Areas & Preserves
- ODNR Scenic Rivers Program
- ODNR Division of Mineral Resources (surface‑managed lands only)
- State‑managed easements
- State‑managed recreation areas

It governs the discovery of:

- **Sites** (state parks, forests, preserves, wildlife areas, scenic river units)
- **Sub‑Sites** within state Sites
- **Trails** on state lands
- **Trail Segments** on state lands
- **Trail Networks** (e.g., statewide trail systems)
- **Site Networks** (e.g., Scenic River corridors)
- **Access Points** associated with state Sites

------------------------------------------------------------
# 3. REQUIRED STATE SOURCES (ALL MANDATORY)

## 3.1 ODNR Division of Parks & Watercraft
Check for:
- State parks (→ Sites)
- Campgrounds (→ Sub‑Sites)
- Day‑use areas (→ Sub‑Sites)
- Marinas (→ Sub‑Sites or Access Points)
- Boat ramps (→ Access Points)
- Trails (→ Trails, Trail Segments)

Required sources:
- ODNR park pages
- ODNR park maps
- ODNR GIS datasets

## 3.2 ODNR Division of Forestry
Check for:
- State forests (→ Sites)
- Forest management units (→ Sub‑Sites)
- Forest trails (→ Trails, Trail Segments)

Required sources:
- ODNR forestry pages
- ODNR forest maps
- ODNR GIS datasets

## 3.3 ODNR Division of Wildlife
Check for:
- Wildlife areas (→ Sites)
- Hunting units (→ Sub‑Sites)
- Fishing access points (→ Access Points)
- Wildlife area trails (→ Trails)

Required sources:
- ODNR wildlife area pages
- ODNR wildlife GIS datasets

## 3.4 ODNR Division of Natural Areas & Preserves
Check for:
- State nature preserves (→ Sites)
- Preserve units (→ Sub‑Sites)
- Preserve access points (→ Access Points)
- Preserve trails (→ Trails)

Required sources:
- DNAP preserve pages
- DNAP maps
- DNAP GIS datasets

## 3.5 ODNR Scenic Rivers Program
Check for:
- Scenic River designations (→ Site Networks)
- Scenic River access points (→ Access Points)
- Scenic River segments (→ Trail Segments if linear trails exist)

Required sources:
- Scenic River program pages
- Scenic River maps
- Scenic River GIS datasets

## 3.6 ODNR Mineral Resources
Check for:
- Surface‑managed lands only (→ Sites)
- Public access areas (→ Access Points)

Required sources:
- ODNR mineral resources datasets

------------------------------------------------------------
# 4. COUNTY‑ANCHORED VERIFICATION (MANDATORY)

For each state entity identified, the system must verify:

## 4.1 Parcel Boundaries
- Confirm the entity lies within the county
- Segment multi‑county Sites by county

## 4.2 Management Authority
Record:
- ODNR division
- Co‑management (park district, county, municipal)
- Special agreements (e.g., USACE + ODNR)

## 4.3 Access Points
Identify:
- Boat ramps
- Trailheads
- Parking areas
- Scenic overlooks
- River access points
- Campground entrances

Access Points must be surfaced as **Access Point candidates** and passed to the
Access Point Discovery Sub‑Procedure v3.1.

## 4.4 Naming Consistency
Use the **state‑published name** as the authoritative name.

------------------------------------------------------------
# 5. DECISION RULES FOR ENTITY CREATION

### 5.1 Site Creation
A state‑managed feature becomes a **Site** if:
- It is ODNR‑owned or ODNR‑managed
- It is identity‑bearing (named, mapped, or designated)
- It has public access or recreation infrastructure
- It influences Access Point logic

Examples:
- State parks
- State forests
- Wildlife areas
- Nature preserves
- Scenic River units (if identity‑bearing)

Exclude:
- Administrative offices
- Maintenance yards
- Non‑public parcels with no identity

### 5.2 Sub‑Site Creation
Create a **Sub‑Site** when:
- A named internal unit exists within a state Site
- A campground, day‑use area, or management unit is identity‑bearing

### 5.3 Trail Creation
Create a **Trail** when:
- A named trail appears in ODNR datasets or maps

### 5.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment‑level geometry or identifiers exist

### 5.5 Trail Network Creation
Create a **Trail Network** when:
- A statewide or regional multi‑trail system is documented

Examples:
- Buckeye Trail (if treated as a network)
- Statewide water trail systems

### 5.6 Site Network Creation
Create a **Site Network** when:
- A Scenic River corridor or similar multi‑site designation exists

### 5.7 Access Point Creation
Create an **Access Point** when:
- A visitor‑facing entry location is documented

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

The State Tier **must** surface:

- All state parks
- All state forests
- All wildlife areas
- All nature preserves
- All Scenic Rivers
- All state‑managed trails
- All state‑managed access points
- All identity‑bearing Sub‑Sites

The State Tier **may** surface:

- Statewide trail networks
- Scenic River Site Networks
- State‑managed easements

------------------------------------------------------------
# 7. LOGGING REQUIREMENTS

For each state entity, log:
- ODNR division
- Entity name
- Entity type (Site, Sub‑Site, Trail, Trail Segment, Trail Network, Site Network)
- County
- Source dataset
- URL or reference
- Access type (if applicable)
- Notes on co‑management
- Discovery Tier: **2**
- Uncertainty or conflicts

Each county must also produce:
- State Sites Found
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

### 8.1 State Entities
Name:
Type: Site / Sub‑Site / Trail / Trail Segment / Trail Network / Site Network
Agency: ODNR Division
County:
URL or Source:
Notes:
Discovery Tier: 2

### 8.2 Access Points
Name:
Type: Access Point
Access Point Type (raw):
Parent Entity:
County:
Source:
Notes:
Discovery Tier: 2

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
- This module is **State Lands Discovery Sub‑Procedure v3.1**.
- Updates to ODNR datasets may result in v3.2, v3.3, etc.
- Any change to tier order or high‑level workflow must be made in the Discovery Protocol Module v3.1.

------------------------------------------------------------
# END OF STATE LANDS DISCOVERY SUB‑PROCEDURE v3.1