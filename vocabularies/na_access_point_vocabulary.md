# NATURAL AREAS PROJECT — ACCESS POINT VOCABULARY MODULE v4.0
Authoritative, versioned, single‑source‑of‑truth controlled vocabularies  
for all Access Point–level fields in the statewide  
Natural Areas & Trails system.

This module contains:
- All controlled vocabularies used in the Access Point Schema v4.0  
- Definitions and rules for each vocabulary  
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
Roadside Pull‑Off  
Pedestrian Entrance  
Vehicle Entrance  
Transit Access  
Ferry Access  
Shuttle Access  
Administrative Access (restricted)  
Other (explicitly named only)

## Definitions & Rules

### Trailhead
- Primary pedestrian or multi‑use entry to a Trail, Trail Segment, or Site‑based trail system.  
- Must be documented as a trail‑system entrance.

### Parking Area
- Visitor parking area that functions as an access node.  
- Must not be used for internal parking lots that do not provide access.

### Boat Ramp
- A constructed, sloped launch surface for trailered or motorized watercraft.  
- Must be explicitly documented.

### Watercraft Access Point
- General water access for non‑trailered craft (kayaks, canoes, paddleboards).  
- Used only when the specific infrastructure type is documented or when “Boat Ramp” is not applicable.

### River Access
- A fallback category for water access when the specific type is unknown.  
- Must not be used when “Boat Ramp” or “Watercraft Access Point” is documented.

### Fishing Access
- A documented location where fishing access is explicitly provided.  
- Must not be inferred from proximity to water.

### Bicycle Access
- A documented bicycle‑specific entry point (e.g., bike‑only entrances).  
- Must not be inferred from trail type.

### Snowmobile Access
- A documented snowmobile entry point.

### Cross Country Ski Access
- A documented XC ski entry point.

### Equestrian Access
- A documented horse‑riding entry point.

### Roadside Pull‑Off
- A visitor‑facing pull‑off that functions as an access node.  
- Must not be used for scenic overlooks or maintenance turnouts.

### Pedestrian Entrance
- A walk‑in entrance to a Site, Trail, or Trail Segment that is not classified as a Trailhead.  
- Must be documented as an entrance.

### Vehicle Entrance
- A drivable entrance to a Site, Trail, or Trail Segment.  
- Must not be used for maintenance‑only gates unless explicitly documented.

### Transit Access
- A transit stop that functions as a visitor‑facing access node.  
- Must be documented by a transit authority or managing agency.

### Ferry Access
- A documented ferry landing that serves as an access node.

### Shuttle Access
- A documented shuttle stop that provides access to a Site or Trail Segment.

### Administrative Access (restricted)
- A documented, restricted‑use access point.  
- Must be explicitly labeled as restricted in authoritative sources.  
- Must not be used for assumed or inferred restrictions.

### Other (explicitly named only)
- Used only when an authoritative source provides a named access type  
  that does not fit any other category.  
- Must not be used for invented, inferred, or convenience categories.  
- Must include the authoritative name exactly as written.

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
- “Seasonal” must be documented as seasonal by the managing agency.  
- Leave blank if status is ambiguous or unverifiable.  
- Status must describe the **Access Point itself**, not the parent entity.  
- Must not encode temporary conditions (e.g., construction, weather closures).  
- Must not be inferred from trail or site status.

------------------------------------------------------------
# 3. VOCABULARY RULES (Universal v4.0)

- All values must be used exactly as written.  
- No synonyms, abbreviations, or invented terms.  
- Vocabulary values must not be inferred from context, geometry, or amenities.  
- If an Access Point does not clearly match a value, leave the field blank and flag for review.  
- New values may be added only through a versioned update to this module.  
- All Access Point–related modules (Discovery, Resolution, Normalization, TSV Output)  
  must reference this vocabulary.

------------------------------------------------------------
# END OF ACCESS POINT VOCABULARY MODULE v4.0