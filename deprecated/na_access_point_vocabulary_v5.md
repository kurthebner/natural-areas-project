# NATURAL AREAS PROJECT
# ACCESS POINT VOCABULARY MODULE v5.0
(Authoritative Controlled Vocabularies for Access Point Fields)

This module contains all controlled vocabularies for Access Point entities
in the Natural Areas Project v5.0.

All Access Point-related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# CHANGES FROM v4.0

- No changes to vocabulary values
- Updated to v5.0 references
- Enhanced definitions and clarifications
- Added usage guidance for discovery and normalization

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Access Point Type
- Status

These vocabularies are used across:
- Discovery Sub-Procedure v5.0 (raw capture)
- Resolution Engine v5.0 (conflict detection)
- Normalization Engine v5.0 (vocabulary mapping)
- TSV Output Specification v5.0 (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from geometry, amenities, or context
- If no documented value matches, leave field blank

------------------------------------------------------------
# 2. ACCESS POINT TYPE VOCABULARY (Controlled)

## 2.1 Allowed Values

**Primary access types:**
- Trailhead
- Parking Area

**Water access types:**
- Boat Ramp
- Boat Launch
- Watercraft Access Point
- River Access
- Fishing Access

**Activity-specific access types:**
- Bicycle Access
- Snowmobile Access
- Cross Country Ski Access
- Equestrian Access

**Infrastructure access types:**
- Roadside Pull-Off
- Pedestrian Entrance
- Vehicle Entrance

**Transit access types:**
- Transit Access
- Ferry Access
- Shuttle Access

**Special access types:**
- Administrative Access

**Fallback:**
- Other

------------------------------------------------------------
## 2.2 Definitions & Usage Rules

### Trailhead

**Definition:**
Primary pedestrian or multi-use entry point to a Trail, Trail Segment, or Site-based trail system.

**When to use:**
- ✅ Documented as "trailhead" by managing agency
- ✅ Marked as trail system entrance
- ✅ Primary pedestrian access to trail

**When NOT to use:**
- ❌ Every place where trail meets road
- ❌ Internal trail junctions
- ❌ Informal trail access points

**Discovery guidance:**
Record as "Trailhead" when source explicitly uses this term or clearly designates as primary trail entrance.

**Normalization:**
- Map variations: "trail head", "trail-head" → "Trailhead"
- Don't infer from map symbols alone

---

### Parking Area

**Definition:**
Visitor parking area that functions as an access node.

**When to use:**
- ✅ Documented parking serving as access point
- ✅ Parking lot designated as site/trail entry
- ✅ Parking area is the primary access method

**When NOT to use:**
- ❌ Internal parking not serving as entry point
- ❌ Overflow parking
- ❌ Maintenance vehicle parking

**Discovery guidance:**
Only record if parking area serves access function, not just "parking exists."

**Normalization:**
- Map variations: "parking lot", "parking" → "Parking Area"

---

### Boat Ramp

**Definition:**
Constructed, sloped launch surface for trailered or motorized watercraft.

**When to use:**
- ✅ Paved or constructed ramp
- ✅ Designed for trailered boats
- ✅ Explicitly documented as "boat ramp" or "boat launch ramp"

**When NOT to use:**
- ❌ Hand-carry kayak access (use Watercraft Access Point)
- ❌ Unimproved shoreline access

**Discovery guidance:**
Use when source clearly indicates constructed ramp infrastructure.

**Normalization:**
- "boat launch" may mean Boat Ramp or Boat Launch - check context
- "ramp" alone → need more context

---

### Boat Launch

**Definition:**
General motorized watercraft launch point, may or may not have constructed ramp.

**When to use:**
- ✅ Documented as "boat launch" without specifying ramp
- ✅ Motorized boat access
- ✅ When "Boat Ramp" too specific

**When NOT to use:**
- ❌ If source specifies "boat ramp" (use Boat Ramp)
- ❌ Kayak/canoe only (use Watercraft Access Point)

**Normalization:**
- "boat launch" without "ramp" → "Boat Launch"
- "boat launch ramp" → "Boat Ramp"

---

### Watercraft Access Point

**Definition:**
General water access for non-trailered craft (kayaks, canoes, paddleboards).

**When to use:**
- ✅ Hand-carry watercraft access
- ✅ Kayak/canoe launch
- ✅ Paddleboard access
- ✅ Non-motorized watercraft entry

**When NOT to use:**
- ❌ Boat ramps (use Boat Ramp)
- ❌ Fishing piers without launch capability

**Discovery guidance:**
Use when source indicates kayak, canoe, or hand-carry watercraft access.

**Normalization:**
- "kayak launch", "canoe access" → "Watercraft Access Point"

---

### River Access

**Definition:**
Fallback category for water access when specific type is unknown.

**When to use:**
- ✅ Source says "river access" generically
- ✅ Water access type unclear from documentation
- ✅ When more specific terms don't apply

**When NOT to use:**
- ❌ If "Boat Ramp" documented (use that)
- ❌ If "Watercraft Access Point" documented (use that)
- ❌ If "Fishing Access" documented (use that)

**Discovery guidance:**
Only use when source is vague about access type. Prefer specific types when possible.

---

### Fishing Access

**Definition:**
Documented location where fishing access is explicitly provided.

**When to use:**
- ✅ Explicitly documented as "fishing access"
- ✅ Designated fishing access point
- ✅ Fishing pier or platform serving as access

**When NOT to use:**
- ❌ Any shoreline where fishing might occur
- ❌ Inferred from proximity to water
- ❌ Trailhead that happens to be near water

**Discovery guidance:**
Only use when source explicitly designates fishing access.

---

### Bicycle Access

**Definition:**
Documented bicycle-specific entry point.

**When to use:**
- ✅ Bike-only entrance
- ✅ Explicitly documented bicycle access point
- ✅ Bike path connection point

**When NOT to use:**
- ❌ Multi-use trailhead accessible by bike (use Trailhead)
- ❌ Inferred from bike trail existence

**Discovery guidance:**
Use only for bicycle-specific access points, not general access that happens to allow bikes.

---

### Snowmobile Access

**Definition:**
Documented snowmobile entry point.

**When to use:**
- ✅ Explicitly documented snowmobile access
- ✅ Snowmobile trail system access point

**Discovery guidance:**
Must be documented; don't infer from trail type.

---

### Cross Country Ski Access

**Definition:**
Documented cross-country ski entry point.

**When to use:**
- ✅ Explicitly documented XC ski access
- ✅ Nordic ski trail system access

**Discovery guidance:**
Must be documented; don't infer from trail type.

---

### Equestrian Access

**Definition:**
Documented horse-riding entry point.

**When to use:**
- ✅ Explicitly documented equestrian access
- ✅ Horse trailer parking with trail access
- ✅ Bridle trail access point

**Discovery guidance:**
Must be documented; don't infer from trail type.

---

### Roadside Pull-Off

**Definition:**
Visitor-facing pull-off that functions as an access node.

**When to use:**
- ✅ Documented roadside access point
- ✅ Pull-off serving as trailhead or site access
- ✅ Scenic overlook with trail access

**When NOT to use:**
- ❌ Scenic overlooks without trail/site access
- ❌ Maintenance turnouts
- ❌ Emergency pull-offs

**Discovery guidance:**
Must serve access function, not just viewing.

---

### Pedestrian Entrance

**Definition:**
Walk-in entrance to a Site, Trail, or Trail Segment that is not classified as a Trailhead.

**When to use:**
- ✅ Site entrance (not trail-specific)
- ✅ Park gate or walk-in entrance
- ✅ Path entrance that isn't a designated trailhead

**When NOT to use:**
- ❌ Trail system entrances (use Trailhead)

**Discovery guidance:**
Use for site-level pedestrian access, not trail system access.

---

### Vehicle Entrance

**Definition:**
Drivable entrance to a Site, Trail, or Trail Segment.

**When to use:**
- ✅ Main gate for vehicle access
- ✅ Entrance road to site
- ✅ Vehicle-accessible entry point

**When NOT to use:**
- ❌ Maintenance-only gates (use Administrative Access)
- ❌ Unless explicitly documented for visitor use

**Discovery guidance:**
Must be documented as visitor-accessible vehicle entrance.

---

### Transit Access

**Definition:**
Transit stop that functions as a visitor-facing access node.

**When to use:**
- ✅ Bus stop serving site/trail
- ✅ Light rail station with site/trail access
- ✅ Documented by transit authority or managing agency

**Discovery guidance:**
Must be documented relationship between transit stop and site/trail.

---

### Ferry Access

**Definition:**
Documented ferry landing that serves as an access node.

**When to use:**
- ✅ Ferry landing provides access to site/trail
- ✅ Documented ferry service

**Discovery guidance:**
Must be documented ferry service, not just boat dock.

---

### Shuttle Access

**Definition:**
Documented shuttle stop that provides access to a Site or Trail.

**When to use:**
- ✅ Shuttle stop serving site/trail
- ✅ Park shuttle system access point

**Discovery guidance:**
Must be documented shuttle service.

---

### Administrative Access

**Definition:**
Documented, restricted-use access point.

**When to use:**
- ✅ Explicitly labeled as restricted or staff-only
- ✅ Administrative or maintenance entrance
- ✅ Documented access restrictions

**When NOT to use:**
- ❌ Assumed or inferred restrictions
- ❌ Temporary closures

**Discovery guidance:**
Must be explicitly documented as restricted. Don't infer.

---

### Other

**Definition:**
Named access type from authoritative source that doesn't fit any other category.

**When to use:**
- ✅ Source provides specific access type name
- ✅ Doesn't match any controlled vocabulary term
- ✅ Is a legitimate, documented access type

**When NOT to use:**
- ❌ Invented categories
- ❌ Convenience groupings
- ❌ Inferred types

**Discovery guidance:**
Include authoritative name exactly as written in notes. Flag for vocabulary expansion review.

**Example:**
Source says "Accessible Viewing Platform with Trail Access" - doesn't fit vocabulary.
Record as: type = "Other", notes = "Accessible Viewing Platform with Trail Access (source term)"

------------------------------------------------------------
# 3. STATUS VOCABULARY (Controlled)

## 3.1 Allowed Values

- Active
- Closed
- Seasonal
- Restricted

------------------------------------------------------------
## 3.2 Definitions & Usage Rules

### Active

**Definition:**
Access point is currently open and operational.

**When to use:**
- ✅ Explicitly documented as open/active
- ✅ Default status when no restrictions documented

**Discovery guidance:**
Can be left blank if obviously active. Use explicitly when differentiating from other access points with different status.

---

### Closed

**Definition:**
Access point is permanently or indefinitely closed.

**When to use:**
- ✅ Explicitly documented as closed
- ✅ Decommissioned access point

**When NOT to use:**
- ❌ Temporary closures (use notes field)
- ❌ Seasonal closures (use Seasonal)

**Discovery guidance:**
Must be explicitly documented as closed.

---

### Seasonal

**Definition:**
Access point operates seasonally.

**When to use:**
- ✅ Documented as seasonal by managing agency
- ✅ "Open May-October" or similar
- ✅ Winter closures

**Discovery guidance:**
Must be explicitly documented as seasonal. Include season details in notes field.

**Example:**
Status: "Seasonal"
Notes: "Open April 1 - November 30"

---

### Restricted

**Definition:**
Access point has documented restrictions on use.

**When to use:**
- ✅ Explicitly labeled as restricted
- ✅ Permit required
- ✅ Membership required
- ✅ Documented access limitations

**When NOT to use:**
- ❌ Assumed restrictions
- ❌ Inferred from access point type
- ❌ Private property without documented public access

**Discovery guidance:**
Must be explicitly documented. Include restriction details in notes field.

**Example:**
Status: "Restricted"
Notes: "Permit required, available at ranger station"

------------------------------------------------------------
# 4. VOCABULARY NORMALIZATION RULES

## 4.1 Common Mappings

**Access Point Type:**
```
Raw Value               → Normalized Value
-----------------         ------------------
"trail head"            → "Trailhead"
"trail-head"            → "Trailhead"
"parking lot"           → "Parking Area"
"parking"               → "Parking Area"
"boat launch ramp"      → "Boat Ramp"
"boat launch"           → "Boat Launch"
"kayak launch"          → "Watercraft Access Point"
"canoe access"          → "Watercraft Access Point"
"XC ski access"         → "Cross Country Ski Access"
"nordic ski access"     → "Cross Country Ski Access"
"horse trailer parking" → "Equestrian Access"
"pulloff"               → "Roadside Pull-Off"
"pull off"              → "Roadside Pull-Off"
```

**Status:**
```
Raw Value          → Normalized Value
-----------          ------------------
"open"             → "Active"
"operational"      → "Active"
"permanently closed" → "Closed"
"decommissioned"   → "Closed"
"seasonal access"  → "Seasonal"
"permit required"  → "Restricted"
```

## 4.2 Ambiguous Cases

**Require context or manual review:**
- "boat launch" - could be Boat Ramp or Boat Launch
- "river access" - could be River Access, Watercraft Access Point, or Fishing Access
- "parking" - could be Parking Area or just amenity note
- "gate" - could be Vehicle Entrance, Administrative Access, or not an access point
- "closed" - could be Closed (permanent) or Seasonal (winter only)

**Resolution:**
- Check source context
- Look for additional descriptors
- When unclear, prefer more general term
- Flag for review if confidence low

------------------------------------------------------------
# 5. VOCABULARY USAGE RULES

## 5.1 Universal Rules

1. **Use exactly as written** - No synonyms, abbreviations, or invented terms
2. **Don't infer** - Values must be documented, not inferred from context, geometry, or amenities
3. **Leave blank if unclear** - Better to have no value than wrong value
4. **One value per field** - No multi-value types (use most specific single type)
5. **Flag new values** - Don't add values; flag for vocabulary expansion

## 5.2 Discovery Phase

- Capture raw values exactly as found
- Don't attempt normalization during discovery
- Record raw variations in access_point_type_raw

## 5.3 Normalization Phase

- Map raw values to controlled vocabulary
- Handle common variations (see 4.1)
- Flag unrecognized values for review
- Validate against vocabulary list

## 5.4 When Vocabulary Doesn't Fit

**If authoritative source uses term not in vocabulary:**

1. **Discovery:** Record raw term exactly
2. **Normalization:** Map to closest vocabulary match OR leave blank and flag
3. **Flag for review:** Add to vocabulary expansion queue
4. **Document:** Include original term in notes field

**Example:**
Source: "Accessible Boardwalk Access Point"
- access_point_type_raw: "Accessible Boardwalk Access Point"
- access_point_type: "Pedestrian Entrance" (closest match)
- notes: "Source term: 'Accessible Boardwalk Access Point'"
- flagged: true (for vocabulary expansion review)

------------------------------------------------------------
# 6. VOCABULARY VERSIONING

## 6.1 Adding New Values

**Process:**
1. Identify recurring terms not in vocabulary
2. Verify terms are authoritative (not invented)
3. Define clear criteria for new term
4. Update vocabulary module with new version
5. Document in changelog

## 6.2 Deprecating Values

**Process:**
1. Identify unused or problematic terms
2. Define replacement term(s)
3. Create migration mapping
4. Update vocabulary module
5. Re-run normalization for affected records

## 6.3 Version History

**v5.0:**
- Updated from v4.0
- No vocabulary changes
- Enhanced definitions
- Added normalization mappings

**v4.0:**
- Initial controlled vocabulary
- Access point types defined
- Status values established

------------------------------------------------------------
# 7. INTEGRATION POINTS

This vocabulary module integrates with:

- **Access Point Schema Module v5.0** (field definitions)
- **Access Point Discovery Sub-Procedure v5.0** (raw capture)
- **Resolution Engine v5.0** (identity matching)
- **Normalization Engine v5.0** (vocabulary mapping)
- **TSV Output Specification v5.0** (output format)

------------------------------------------------------------
# END OF ACCESS POINT VOCABULARY MODULE v5.0
