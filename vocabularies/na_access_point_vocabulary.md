# NATURAL AREAS PROJECT — ACCESS POINT VOCABULARY MODULE v3.2.2
Authoritative, versioned, single‑source‑of‑truth controlled vocabularies  
for all Access Point–level fields in the statewide  
Natural Areas & Trails system.

This module contains:
- All controlled vocabularies used in the Access Point Schema v3.2.1  
- Rules for each controlled vocabulary  
- Clarifications for ambiguous or overlapping types  

All Access Point–related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# 1. ACCESS POINT TYPE VOCABULARY (Controlled)

## Allowed Values
Trailhead  
Parking Area  
Boat Ramp  
Watercraft Access Point  
River Access  
Fishing Access  
Bicycle Access  
Snowmobile Access  
Cross Country Ski Access  
Equestrian Access  
Roadside Pull-Off  
Pedestrian Entrance  
Vehicle Entrance  
Transit Access  
Ferry Access  
Shuttle Access  
Administrative Access (restricted)  
Other (explicitly named only)

## Definitions & Rules

### Trailhead
- Primary pedestrian or multi-use entry to a Trail, Trail Segment, or Site-based trail system.

### Parking Area
- Visitor parking area that functions as an access node.

### Boat Ramp
- A constructed, sloped launch surface for trailered or motorized watercraft.

### Watercraft Access Point
- General water access for non‑trailered craft (kayaks, canoes, paddleboards).
- Used when the specific infrastructure type is not documented.

### River Access
- A fallback category for water access when the specific type is unknown.
- Must not be used when “Boat Ramp” or “Watercraft Access Point” is documented.

### Fishing Access
- A documented location where fishing access is explicitly provided.

### Bicycle Access
- A documented bicycle‑specific entry point (e.g., bike‑only entrances).

### Snowmobile Access
- A documented snowmobile entry point.

### Cross Country Ski Access
- A documented XC ski entry point.

### Equestrian Access
- A documented horse‑riding entry point.

### Roadside Pull-Off
- A visitor‑facing pull‑off that functions as an access node.
- Must not be used for scenic overlooks or maintenance turnouts.

### Pedestrian Entrance
- A walk‑in entranceto a Site, Trail, or Trail Segment that is not classified as a Trailhead.

### Vehicle Entrance
- A drivable entrance to a Site, Trail, or Trail Segment.

### Transit Access
- A transit stop that functions as a visitor‑facing access node.

### Ferry Access
- A documented ferry landing that serves as an access node.

### Shuttle Access
- A documented shuttle stop that provides access to a Site or Trail Segment.

### Administrative Access (restricted)
- A documented, restricted‑use access point.
- Must be explicitly labeled as restricted in authoritative sources.

### Other (explicitly named only)
- Used only when an authoritative source provides a named access type  
  that does not fit any other category.
- Must not be used for invented or inferred types.

------------------------------------------------------------
# 2. ACCESS POINT STATUS VOCABULARY (Controlled)

## Allowed Values
Active  
Closed  
Seasonal  
Restricted  

## Rules
- Status must reflect authoritative information.  
- “Restricted” applies only when explicitly stated.  
- Leave blank if status is ambiguous or unverifiable.  
- Status must describe the Access Point itself, not the parent entity.  

------------------------------------------------------------
# END OF ACCESS POINT VOCABULARY MODULE v3.2.2