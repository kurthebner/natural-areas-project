# NATURAL AREAS PROJECT
# RESOLUTION MODULE v4.0
(Authoritative System‑Wide Decision Framework for Entity Identity, Conflict Resolution, and Cross‑Tier Alignment)

This module defines the authoritative, deterministic rules for resolving all ambiguous,
borderline, conflicting, or multi‑identity cases across **all six entity types** during
the Raw → Resolution → Normalization → Entity Graph pipeline.

This module contains no controlled vocabularies.  
All vocabularies are defined in the respective Vocabulary Modules v4.0.

This module overrides ambiguity in all other modules.

------------------------------------------------------------
# 1. PURPOSE

The Resolution Module v4.0 defines how the system resolves all ambiguous or
borderline cases that arise during:

- Discovery (what counts as each entity type)
- Entity‑type determination (Site vs. Trail vs. Access Point, etc.)
- Classification across all six entities (including Site categories, Trail and Segment types, and Access Point roles)
- Parent Site assignment (child Sites)
- Multi‑county interpretation
- Network membership interpretation
- Cross‑tier conflict reconciliation
- Provenance‑aware identity merging
- Integration with the Entity Graph

This module ensures:

- Zero improvisation  
- Zero silent assumptions  
- Deterministic, repeatable decisions  
- Full alignment with Schema Modules, Vocabulary Modules, Discovery Protocol v4.0,
  Discovery Metadata Specification v4.0, Normalization Engine v4.0, and TSV Output Specifications v4.0  
- Full preservation of raw discovery values  
- Full provenance‑driven conflict handling  

------------------------------------------------------------
# 2. GENERAL PRINCIPLES (APPLIES TO ALL ENTITIES)

## 2.1 Identity First
Classification is based on **ontological identity**, not amenities, activities, or marketing language.

## 2.2 Governance ≠ Category
Ownership or management never determines Category or entity type.

## 2.3 Ecology Belongs in Description
Ecological character never determines Category or entity type.  
Ecology informs **Description**, not identity.

## 2.4 Features Are Not Entities
Amenities never determine entity type.  
If something is an amenity, it belongs in **Features**, not as an entity.

## 2.5 When in Doubt, Choose the More General Identity
If an object could be two things, choose the broader identity unless a formal designation dictates otherwise.

## 2.6 Never Infer Governance
Ownership, Management, and Designation must never be inferred.  
Ambiguity triggers a flag, not a guess.

## 2.7 Identity‑Bearing Units May Be Split
Large parks, forests, preserves, and trail systems may contain internal identity‑bearing units.  
These become **child Sites** when they meet the criteria in the **Child Site Rules Module v4.0**.

## 2.8 Access Points Are Never Sites
Trailheads, boat ramps, parking areas, and entrances are **Access Points**, not Sites.

## 2.9 Trails Are Not Sites
Named trails are **Trails**, not Sites.

## 2.10 Trail Segments Are Not Trails
Segments are identity‑bearing subdivisions of Trails.

## 2.11 Trail Segments Are Never Features
If something qualifies as a Trail Segment, it is always an entity.  
Non‑identity‑bearing path fragments are **geometry**, not Features.

## 2.12 Networks Are Not Trails or Sites
Networks are collections of Trails or Sites, not physical land units.

## 2.13 Provenance Always Wins
When sources conflict, the system must rely on provenance metadata:
- Tier precedence  
- Source system  
- Discovery path  
- Extraction method  
- Raw values  

------------------------------------------------------------
# 3. ENTITY‑TYPE RESOLUTION RULES

These rules determine what entity type a baseline or discovered object becomes.

## 3.1 Site
A Site is a **named, bounded, physical land unit** with its own identity.

## 3.2 Child Site
A child Site is a named, bounded, identity‑bearing unit **within a parent Site**  
that meets the criteria in the **Child Site Rules Module v4.0**.  
It is represented as a **Site with a Parent Site value**, not a separate entity type.

## 3.3 Access Point
A visitor‑facing location of entry to a Site, Trail, or Trail Segment.

## 3.4 Trail
A **named, linear, identity‑bearing route**.

## 3.5 Trail Segment
A **named or identity‑bearing subdivision** of a Trail.

## 3.6 Trail Network
A **collection of Trails** with a shared identity.

## 3.7 Site Network
A **collection of Sites** with a shared identity.

------------------------------------------------------------
# 4. CATEGORY‑LEVEL EDGE CASES (SITES)

## 4.1 Boardwalk
- Feature

## 4.2 Natural Play Area
- Feature

## 4.3 Paved Path / Multi‑Use Path
- Trail if named and identity‑bearing  
- Otherwise geometry

## 4.4 Linear Park
- Category: Park  
- Subtype: Linear Park

## 4.5 Greenway
- Category: Greenway Corridor

## 4.6 Stormwater Green with Ecological Identity
- Category: Natural Area or Conservation Area

## 4.7 Stormwater Basin with No Ecological Identity
- Excluded

## 4.8 Reservoir Property
- Category: Water Site or Reservoir

## 4.9 Cemetery with Natural Area
- Category: Cemetery  
- Ecological identity → Description

## 4.10 Mitigation Bank
- Category: Conservation Area

## 4.11 Unnamed Natural Area in GIS
- Category: Natural Area  
- Name: best available GIS label

## 4.12 Internal Natural Areas within Parks
- Category: Natural Area  
- Parent Site assigned

## 4.13 Campgrounds
- Category: Camp  
- Only if natural‑area identity present

## 4.14 Water Access Sites
- Category: Water Access Site

------------------------------------------------------------
# 5. TRAIL‑RELATED EDGE CASES

## 5.1 Trailhead vs. Trail Access Point
- Both are Access Points

## 5.2 Bikeway Access Point
- Only if tied to a bikeway system

## 5.3 Connector Trail vs. Spur
- Connector = links systems  
- Spur = dead‑end

## 5.4 Loop Trails
- Trail  
- Segment Type: Loop

## 5.5 Internal Trail Segments
- Trail Segment

## 5.6 Greenway Trails
- Trail Corridor

------------------------------------------------------------
# 6. ECOLOGICAL EDGE CASES (SITES)

## 6.1 Buffer Zones
- Category: Buffer Zone

## 6.2 Restoration Areas
- Category: Conservation Area

## 6.3 Successional Habitat
- Category: Natural Area

## 6.4 Floodplain Forest
- Category: Natural Area

## 6.5 Wetland Complexes
- Category: Natural Area

------------------------------------------------------------
# 7. ACCESS POINT EDGE CASES

## 7.1 Parking Lots
- Access Points

## 7.2 Boat Ramps
- Access Points

## 7.3 Scenic Pull‑Offs
- Access Points if they function as entrances

## 7.4 Internal Amenities
- Features unless functioning as entrances

## 7.5 Trail Intersections
- Geometry, not entities

## 7.6 Administrative Access
- Access Point only if documented

------------------------------------------------------------
# 8. INTERNAL PARCEL RULE (SITES + CHILD SITES)

A Site or child Site must be:

- Named  
- Physical  
- Bounded  
- Identity‑bearing  
- Stable  

If not, it is a Feature.

Child Site determination must follow the **Child Site Rules Module v4.0**.

------------------------------------------------------------
# 9. TRAIL SEGMENT IDENTITY RULE

A Trail Segment must be:

- Named OR  
- Identity‑bearing OR  
- A formally defined segment OR  
- A loop, spur, connector, or internal segment with operational meaning  

If a path fragment is:

- Unnamed  
- Not identity‑bearing  
- Not operationally meaningful  
- Not recognized by the managing agency  

…it is **geometry**, not a Trail Segment.

------------------------------------------------------------
# 10. NETWORK RESOLUTION RULES

## 10.1 Trail Networks
- Must be documented as a network  
- Must contain Trails  
- Must not be inferred  

## 10.2 Site Networks
- Must be documented as a network  
- Must contain Sites  
- Must not be inferred  

------------------------------------------------------------
# 11. CONFLICT RESOLUTION OVERRIDES

## 11.1 Tier Precedence
Lower‑numbered tiers override higher‑numbered tiers.

## 11.2 Category Conflicts
Resolution Module overrides all other modules.

## 11.3 Ownership / Management Conflicts
Normalization rules apply unless ambiguous → Resolution decides.

## 11.4 Trail Role Conflicts
Resolution overrides all other modules.

## 11.5 Ecological Identity Conflicts
Ecology informs Description only.

## 11.6 Entity‑Type Conflicts
Resolution determines final entity type.

## 11.7 Parent Site Conflicts
Resolution applies the **Child Site Rules Module v4.0**.

## 11.8 Multi‑County Conflicts (Universal Rule)

For all six entity types:

- Each entity must be represented as **one record**, regardless of the number of counties it spans.
- The county list must contain **all applicable counties**, formatted as a **semicolon‑delimited, alphabetized list**.
- No entity may be duplicated or segmented based on county boundaries.
- Boundary metadata must be preserved in Discovery Metadata.
- If authoritative sources disagree, Resolution determines the final county list.
- No inference is permitted; only documented county assignments may be used.

## 11.9 Parent–Child Identity Conflicts

A child Site may not override or redefine the identity of its parent Site.

If an internal unit appears to have equal or greater identity than the parent, Resolution determines whether:

- the internal unit is actually the true Site, and  
- the former parent becomes a child Site or a Feature.  

Identity precedence is determined by authoritative naming, not size or prominence.

## 11.10 Provenance Conflicts
Resolution uses:

- Tier precedence  
- Source system  
- Discovery path  
- Extraction method  
- Raw values  

## 11.11 Developer Preview TSVs
Preview TSVs generated during Discovery are non‑authoritative.  
Resolution must rely only on Raw Discovery Records and Discovery Metadata.

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- All six Schema Modules v4.0  
- All six Vocabulary Modules v4.0  
- All six Normalization Modules v4.0  
- Discovery Protocol Module v4.0  
- Discovery Orchestration Module v4.0  
- County Baseline Module v4.0  
- Processing Orchestration Module v4.0  
- **Child Site Rules Module v4.0**  
- Audit & Logging Module v4.0  

------------------------------------------------------------
# END OF RESOLUTION MODULE v4.0