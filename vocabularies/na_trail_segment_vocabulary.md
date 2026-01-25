# NATURAL AREAS PROJECT — TRAIL SEGMENT VOCABULARY MODULE v4.0
Authoritative, versioned, single‑source‑of‑truth controlled vocabularies  
for all Trail Segment–level fields in the statewide Natural Areas & Trails system.

This module contains:
- All controlled vocabularies used in the Trail Segment Schema v4.0  
- Definitions and rules for each vocabulary  
- Clarifications for ambiguous or overlapping values  

All Trail Segment–related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# 1. SEGMENT TYPE VOCABULARY (Controlled)

## Allowed Values
Linear  
Loop  
Connector  
Access Segment  
Crossing  
Spur  
Other (explicitly named only)

## Rules & Clarifications
- Describes the **geometric or functional form** of the Segment.  
- “Linear” is the default for most Segments.  
- “Loop” applies only when the Segment forms a closed loop by itself.  
- “Connector” links two Trails or two Segments.  
- “Access Segment” provides access from an Access Point to the main corridor.  
- “Crossing” applies to bridges, underpasses, or road crossings mapped as Segments.  
- “Spur” is a short offshoot that does not reconnect.  
- “Other” may be used only when an authoritative source provides a named type not covered above.  
- Must not encode use, surface, or role.  
- Must not encode status or designation.  

------------------------------------------------------------
# 2. SEGMENT SURFACE TYPE VOCABULARY (Controlled)

## Allowed Values
Paved  
Crushed Stone  
Gravel  
Natural Surface  
Boardwalk  
Water  
Mixed  
Other (explicitly named only)

## Rules & Clarifications
- Describes the **actual surface** of the Segment.  
- “Paved” includes asphalt and concrete; these must not appear as separate values.  
- “Natural Surface” includes dirt, soil, grass, or unimproved tread.  
- “Water” applies to water‑based Segments (e.g., mapped water trail reaches).  
- “Mixed” is allowed only when explicitly documented.  
- “Other” may be used only when an authoritative source provides a named surface type not covered above.  
- Must not encode use or origin.  
- Must not encode role or status.  

------------------------------------------------------------
# 3. SEGMENT ROLE VOCABULARY (Controlled)

## Allowed Values
Primary Segment  
Secondary Segment  
Connector Segment  
Access Segment  
Scenic Segment  
Interpretive Segment  
Other (explicitly named only)

## Rules & Clarifications
- Describes the **functional role** of the Segment within the Trail.  
- “Primary Segment” is the mainline corridor.  
- “Secondary Segment” is a subordinate but official part of the Trail.  
- “Connector Segment” links two Trails or two Segments; must not be used for Access Segments.  
- “Access Segment” connects an Access Point to the main corridor.  
- “Scenic Segment” is documented as a scenic or viewpoint corridor.  
- “Interpretive Segment” includes signed interpretive routes or educational loops.  
- “Other” may be used only when an authoritative source provides a named role not covered above.  
- **Segment Role is often blank** because many agencies do not document functional roles at the segment level.  
- Must not encode type, surface, or use.  
- Must not encode status or designation.  

------------------------------------------------------------
# END OF TRAIL SEGMENT VOCABULARY MODULE v4.0