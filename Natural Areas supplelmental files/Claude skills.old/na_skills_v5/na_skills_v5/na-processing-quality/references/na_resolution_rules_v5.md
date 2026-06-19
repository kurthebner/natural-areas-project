# NATURAL AREAS PROJECT
# RESOLUTION RULES MODULE v5.0
(Authoritative Entity-Type and Category Decision Rules for All Six Entity Types)

This module defines the authoritative decision rules for resolving entity type,
category classification, and boundary cases across all six entity types during
the discovery → resolution → normalization pipeline.

This module is the companion to the Resolution Engine v5.0. The Resolution Engine
defines HOW resolution works (matching, merging, conflict detection). This module
defines WHAT decisions are made when entity type or category is ambiguous.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v5.0.

------------------------------------------------------------
# CHANGES FROM v4.0

- Module extracted from Resolution Module v4.0 (Sections 2–11)
- `child_site_rules` reference updated to v5.0
- `county_list` → `counties` field name updated
- `managing_agency` → `governance` field name updated
- `access_level` and `role` removed from Access Point rules (fields deprecated in v5.0)
- Trail Segment `segment_type` values updated to v5.0 vocabulary
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- General principles that govern all entity-type decisions
- Entity-type resolution rules (what qualifies as each entity type)
- Category-level edge cases for Sites
- Trail-related edge cases
- Ecological edge cases for Sites
- Access Point edge cases
- Internal parcel and child Site rules
- Trail Segment identity rules
- Network resolution rules
- Conflict override rules

These rules are authoritative. When any other module is ambiguous about entity
type or category, this module decides.

------------------------------------------------------------
# 2. GENERAL PRINCIPLES (APPLIES TO ALL ENTITIES)

## 2.1 Identity First
Classification is based on ontological identity — what the thing IS — not
amenities, activities, or marketing language.

## 2.2 Governance ≠ Category
Ownership or management never determines Category or entity type. A county-owned
trail is still a Trail. A state-owned parking area is still an Access Point.

## 2.3 Ecology Belongs in Description
Ecological character never determines Category or entity type.
Ecology informs Description, not identity.

## 2.4 Features Are Not Entities
Amenities (picnic shelters, playgrounds, restrooms) never determine entity type.
If something is an amenity, it belongs in features_raw, not as an entity.

## 2.5 When in Doubt, Choose the More General Identity
If an object could be two entity types, choose the broader identity unless a
formal designation dictates otherwise.

## 2.6 Never Infer Governance
Ownership, governance, and designation must never be inferred.
Ambiguity triggers a conflict flag, not a guess.

## 2.7 Identity-Bearing Units May Be Split
Large parks, forests, preserves, and trail systems may contain internal
identity-bearing units. These become child Sites when they meet the criteria
in the Child Site Rules Module v5.0.

## 2.8 Access Points Are Never Sites
Trailheads, boat ramps, parking areas, and entrances are Access Points, not Sites.

## 2.9 Trails Are Not Sites
Named trails are Trails, not Sites.

## 2.10 Trail Segments Are Not Trails
Segments are identity-bearing subdivisions of Trails.

## 2.11 Trail Segments Are Never Features
If something qualifies as a Trail Segment, it is always an entity.
Non-identity-bearing path fragments are geometry, not Features.

## 2.12 Networks Are Not Trails or Sites
Networks are collections of Trails or Sites, not physical land units.

## 2.13 Provenance Always Wins
When sources conflict, the system relies on provenance metadata:
- Tier precedence
- Source system
- Discovery path
- Raw values

------------------------------------------------------------
# 3. ENTITY-TYPE RESOLUTION RULES

These rules determine what entity type a discovered or baseline object becomes.

## 3.1 Site
A Site is a named, bounded, physical land unit with its own identity.
It has governance, a physical presence, and is recognized as a distinct place
by authoritative sources.

## 3.2 Child Site
A child Site is a named, bounded, identity-bearing unit within a parent Site
that meets the criteria in the Child Site Rules Module v5.0.
It is represented as a Site with a `parent_site_id` value, not a separate entity type.

## 3.3 Access Point
A visitor-facing location of entry to a Site, Trail, or Trail Segment.
Includes parking areas, trailheads, boat launches, and documented entrances.

## 3.4 Trail
A named, linear, identity-bearing route. Must be named and recognized as a
distinct trail by authoritative sources.

## 3.5 Trail Segment
A named or identity-bearing subdivision of a Trail. See Section 9 for identity rules.

## 3.6 Trail Network
A collection of Trails with a shared identity. Must be documented as a network.
Must not be inferred. See Section 10.

## 3.7 Site Network
A collection of Sites with a shared identity. Must be documented as a network.
Must not be inferred. See Section 10.

------------------------------------------------------------
# 4. CATEGORY-LEVEL EDGE CASES (SITES)

## 4.1 Boardwalk
- Not an entity — Feature

## 4.2 Natural Play Area
- Not an entity — Feature

## 4.3 Paved Path / Multi-Use Path
- Trail if named and identity-bearing
- Otherwise geometry (not an entity)

## 4.4 Linear Park
- Category: Park
- Subtype: Linear Park

## 4.5 Greenway
- Category: Greenway Corridor

## 4.6 Stormwater Green with Ecological Identity
- Category: Natural Area or Conservation Area

## 4.7 Stormwater Basin with No Ecological Identity
- Excluded — not an entity

## 4.8 Reservoir Property
- Category: Water Site or Reservoir

## 4.9 Cemetery with Natural Area
- Category: Cemetery
- Ecological identity → Description only

## 4.10 Mitigation Bank
- Category: Conservation Area

## 4.11 Unnamed Natural Area in GIS
- Category: Natural Area
- Name: best available GIS label

## 4.12 Internal Natural Areas within Parks
- Category: Natural Area
- `parent_site_id` assigned

## 4.13 Campgrounds
- Category: Camp
- Only if natural-area identity is present; otherwise Feature

## 4.14 Water Access Sites
- Category: Water Access Site

------------------------------------------------------------
# 5. TRAIL-RELATED EDGE CASES

## 5.1 Trailhead vs. Trail Access Point
- Both are Access Points — entity type does not differ by name

## 5.2 Bikeway Access Point
- Access Point only if tied to a documented bikeway system

## 5.3 Connector Trail vs. Spur
- Connector = links two or more trail systems
- Spur = dead-end branch off a primary trail
- Both are Trail Segments or Trails depending on identity

## 5.4 Loop Trails
- Entity type: Trail
- `segment_type`: Loop (when applied to a Segment)

## 5.5 Internal Trail Segments
- Entity type: Trail Segment

## 5.6 Greenway Trails
- Entity type: Trail
- `trail_type_raw`: Trail Corridor

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

## 7.3 Scenic Pull-Offs
- Access Points if they function as documented visitor entrances
- Otherwise Feature

## 7.4 Internal Amenities
- Features unless they function as documented entrances

## 7.5 Trail Intersections
- Geometry, not entities

## 7.6 Administrative Access
- Access Point only if documented by the managing agency

------------------------------------------------------------
# 8. INTERNAL PARCEL RULE (SITES + CHILD SITES)

A Site or child Site must be:

- Named
- Physical (occupies real-world space)
- Bounded (has discernible extent)
- Identity-bearing (recognized as a distinct place)
- Stable (not temporary or transient)

If any condition is not met, it is a Feature, not an entity.

Child Site determination must follow the Child Site Rules Module v5.0.

------------------------------------------------------------
# 9. TRAIL SEGMENT IDENTITY RULE

A Trail Segment must be:

- Named, OR
- Identity-bearing (recognized by the managing agency), OR
- A formally defined segment, OR
- A loop, spur, connector, or internal segment with operational meaning

If a path fragment is:

- Unnamed
- Not identity-bearing
- Not operationally meaningful
- Not recognized by the managing agency

...it is geometry, not a Trail Segment entity.

------------------------------------------------------------
# 10. NETWORK RESOLUTION RULES

## 10.1 Trail Networks
- Must be explicitly documented as a network by authoritative sources
- Must contain Trails (not just geometry)
- Must not be inferred from geographic proximity or common management

## 10.2 Site Networks
- Must be explicitly documented as a network by authoritative sources
- Must contain Sites
- Must not be inferred from geographic proximity or common management

------------------------------------------------------------
# 11. CONFLICT OVERRIDE RULES

## 11.1 Tier Precedence
Lower-numbered tiers override higher-numbered tiers.
Tier 1 (Federal) > Tier 2 (State) > ... > Tier 8 (Private) > Tier 0 (Baseline).

## 11.2 Category Conflicts
This module overrides all other modules on category decisions.

## 11.3 Governance Conflicts
Normalization Engine rules apply unless ambiguous; this module decides ambiguous cases.

## 11.4 Entity-Type Conflicts
This module determines final entity type.

## 11.5 Ecological Identity Conflicts
Ecology informs Description only. Never used to determine Category.

## 11.6 Parent Site Conflicts
Child Site Rules Module v5.0 governs; this module decides edge cases.

## 11.7 Multi-County Conflicts

For all six entity types:
- Each entity must be represented as one record, regardless of counties spanned
- The `counties` field must contain all applicable counties, semicolon-delimited, alphabetized
- No entity may be duplicated or segmented based on county boundaries
- Boundary metadata preserved in provenance
- No inference permitted — only documented county assignments may be used

## 11.8 Parent–Child Identity Conflicts

A child Site may not override or redefine the identity of its parent Site.

If an internal unit appears to have equal or greater identity than the parent,
this module determines whether:
- The internal unit is actually the true Site
- The former parent becomes a child Site or Feature

Identity precedence is determined by authoritative naming, not size or prominence.

## 11.9 Provenance Conflicts
When sources disagree, resolution relies on:
- Tier precedence
- Source system authority
- Discovery path
- Raw field values
- Extraction method

Conflicts are logged. This module does not silently resolve provenance conflicts —
it surfaces them for the normalization decision rules.

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- All six Schema Modules v5.0
- All six Vocabulary Modules v5.0
- Resolution Engine v5.0
- Child Site Rules Module v5.0
- Normalization Engine v5.0

------------------------------------------------------------
# END OF RESOLUTION RULES MODULE v5.0
