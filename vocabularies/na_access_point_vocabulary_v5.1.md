# NATURAL AREAS PROJECT
# ACCESS POINT VOCABULARY MODULE v5.1
(Authoritative Controlled Vocabularies for Access Point Fields)

This module contains all controlled vocabularies for Access Point entities
in the Natural Areas Project v5.x.

All Access Point-related modules must reference this module for vocabulary
authority.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **All cross-module references updated to v5.x**
- **identity_notes field guidance added**: identity_notes_raw at discovery
  feeds the normalized identity_notes field; no controlled vocabulary
- No vocabulary values added or removed

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- No changes to vocabulary values
- Updated to v5.0 references
- Enhanced definitions and clarifications
- Added usage guidance for discovery and normalization

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Access Point Type
- Status

And provides field guidance for free-text fields:
- Features (no controlled vocabulary — free text with metadata)
- Identity Notes (no controlled vocabulary)
- Notes (no controlled vocabulary)

These vocabularies are used across:
- Access Point Discovery Sub-Procedure v5.x (raw capture)
- Resolution Engine v5.x (conflict detection)
- Normalization Engine v5.x (vocabulary mapping)
- Access Point TSV Output Specification v5.x (output format)

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
Primary pedestrian or multi-use entry point to a Trail, Trail Segment, or
Site-based trail system.

**When to use:**
- ✅ Documented as "trailhead" by managing agency
- ✅ Marked as trail system entrance
- ✅ Primary pedestrian access to trail

**When NOT to use:**
- ❌ Every place where trail meets road
- ❌ Internal trail junctions
- ❌ Informal trail access points

**Normalization:**
- "trail head", "trail-head" → "Trailhead"

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

**Normalization:**
- "parking lot", "parking" → "Parking Area"

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

**Normalization:**
- "boat launch ramp" → "Boat Ramp"

---

### Boat Launch

**Definition:**
General motorized watercraft launch point, may or may not have a
constructed ramp.

**When to use:**
- ✅ Documented as "boat launch" without specifying ramp
- ✅ Motorized boat access
- ✅ When "Boat Ramp" is too specific

**When NOT to use:**
- ❌ If source specifies "boat ramp" (use Boat Ramp)
- ❌ Kayak/canoe only (use Watercraft Access Point)

**Normalization:**
- "boat launch" without "ramp" → "Boat Launch"
- "boat launch ramp" → "Boat Ramp"

---

### Watercraft Access Point

**Definition:**
General water access for non-trailered craft (kayaks, canoes,
paddleboards).

**When to use:**
- ✅ Hand-carry watercraft access
- ✅ Kayak/canoe launch
- ✅ Paddleboard access
- ✅ Non-motorized watercraft entry

**When NOT to use:**
- ❌ Boat ramps (use Boat Ramp)
- ❌ Fishing piers without launch capability

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
- ❌ If "Boat Ramp" is documented
- ❌ If "Watercraft Access Point" is documented
- ❌ If "Fishing Access" is documented

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

---

### Snowmobile Access

**Definition:**
Documented snowmobile entry point.

**When to use:**
- ✅ Explicitly documented snowmobile access
- ✅ Snowmobile trail system access point

---

### Cross Country Ski Access

**Definition:**
Documented cross-country ski entry point.

**When to use:**
- ✅ Explicitly documented XC ski access
- ✅ Nordic ski trail system access

---

### Equestrian Access

**Definition:**
Documented horse-riding entry point.

**When to use:**
- ✅ Explicitly documented equestrian access
- ✅ Horse trailer parking with trail access
- ✅ Bridle trail access point

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

**Normalization:**
- "pulloff", "pull off" → "Roadside Pull-Off"

---

### Pedestrian Entrance

**Definition:**
Walk-in entrance to a Site, Trail, or Trail Segment that is not
classified as a Trailhead.

**When to use:**
- ✅ Site entrance (not trail-specific)
- ✅ Park gate or walk-in entrance
- ✅ Path entrance that isn't a designated trailhead

**When NOT to use:**
- ❌ Trail system entrances (use Trailhead)

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

---

### Transit Access

**Definition:**
Transit stop that functions as a visitor-facing access node.

**When to use:**
- ✅ Bus stop serving site/trail
- ✅ Light rail station with site/trail access
- ✅ Documented by transit authority or managing agency

---

### Ferry Access

**Definition:**
Documented ferry landing that serves as an access node.

**When to use:**
- ✅ Ferry landing provides access to site/trail
- ✅ Documented ferry service

---

### Shuttle Access

**Definition:**
Documented shuttle stop that provides access to a Site or Trail.

**When to use:**
- ✅ Shuttle stop serving site/trail
- ✅ Park shuttle system access point

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

---

### Other

**Definition:**
Named access type from authoritative source that doesn't fit any other
category.

**When to use:**
- ✅ Source provides a specific access type name not in vocabulary
- ✅ Is a legitimate, documented access type

**When NOT to use:**
- ❌ Invented categories
- ❌ Inferred types

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary expansion review.

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
Can be left blank if obviously active.

---

### Closed

**Definition:**
Access point is permanently or indefinitely closed.

**When to use:**
- ✅ Explicitly documented as closed
- ✅ Decommissioned access point

**When NOT to use:**
- ❌ Temporary closures (use Notes field)
- ❌ Seasonal closures (use Seasonal)

---

### Seasonal

**Definition:**
Access point operates seasonally.

**When to use:**
- ✅ Documented as seasonal by managing agency
- ✅ "Open May-October" or similar
- ✅ Winter closures

**Discovery guidance:**
Include season details in Notes field.

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

**Discovery guidance:**
Include restriction details in Notes field.

------------------------------------------------------------
# 4. IDENTITY NOTES (Free-Text — No Controlled Vocabulary)

## 4.1 Overview

**Identity Notes is a free-text field — there is no controlled vocabulary.**

Used for identity clarifications that don't belong in Notes.

## 4.2 What to Capture

- Access point type uncertainty (e.g., "source unclear whether this is
  Trailhead or Parking Area — kiosk present but no lot")
- Parent entity assignment uncertainty
- Disambiguation notes (e.g., why this is an Access Point vs. a feature)
- Vocabulary type flags (e.g., "source calls this 'boardwalk access' —
  no vocabulary match, flagged for review")

## 4.3 Discovery vs. Normalization

- **Discovery stage**: capture in `identity_notes_raw`
- **Normalized stage**: surfaced as `identity_notes` field

------------------------------------------------------------
# 5. VOCABULARY NORMALIZATION RULES

## 5.1 Common Mappings

**Access Point Type:**
```
Raw Value                  → Normalized Value
-----------                  ------------------
"trail head"               → "Trailhead"
"trail-head"               → "Trailhead"
"parking lot"              → "Parking Area"
"parking"                  → "Parking Area"
"boat launch ramp"         → "Boat Ramp"
"boat launch"              → "Boat Launch"
"kayak launch"             → "Watercraft Access Point"
"canoe access"             → "Watercraft Access Point"
"XC ski access"            → "Cross Country Ski Access"
"nordic ski access"        → "Cross Country Ski Access"
"horse trailer parking"    → "Equestrian Access"
"pulloff"                  → "Roadside Pull-Off"
"pull off"                 → "Roadside Pull-Off"
```

**Status:**
```
Raw Value                  → Normalized Value
-----------                  ------------------
"open"                     → "Active"
"operational"              → "Active"
"permanently closed"       → "Closed"
"decommissioned"           → "Closed"
"seasonal access"          → "Seasonal"
"permit required"          → "Restricted"
```

## 5.2 Ambiguous Cases

**Require context or manual review:**
- "boat launch" — could be Boat Ramp or Boat Launch
- "river access" — could be River Access, Watercraft Access Point,
  or Fishing Access
- "parking" — could be Parking Area or just amenity note
- "gate" — could be Vehicle Entrance, Administrative Access, or not
  an access point
- "closed" — could be Closed (permanent) or Seasonal (winter only)

**Resolution:**
- Check source context
- Prefer more specific term when context supports it
- Leave blank rather than guess
- Flag in identity_notes if confidence is low

------------------------------------------------------------
# 6. VOCABULARY USAGE RULES

## 6.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or invented terms
2. **Don't infer** — Values must be documented, not inferred from context,
   geometry, or amenities
3. **Leave blank if unclear** — Better no value than wrong value
4. **One value per field** — No multi-value types
5. **Flag new values** — Don't add values; flag for vocabulary expansion

## 6.2 Discovery Phase

- Capture raw values exactly as found in `_raw` fields
- Don't attempt normalization during discovery
- Capture type uncertainty in `identity_notes_raw`

## 6.3 Normalization Phase

- Map raw values to controlled vocabulary
- Handle common variations (see Section 5)
- Flag unrecognized values for review
- Validate against vocabulary list

------------------------------------------------------------
# 7. VOCABULARY VERSIONING

## 7.1 Version History

**v5.1:**
- Cross-module references updated to v5.x
- identity_notes field guidance added
- Other vocabulary type flag guidance added to "Other" definition

**v5.0:**
- Updated from v4.0; no vocabulary changes
- Enhanced definitions and normalization mappings

**v4.0:**
- Initial controlled vocabulary
- Access point types defined
- Status values established

------------------------------------------------------------
# 8. INTEGRATION POINTS

This vocabulary module integrates with:

- **Access Point Schema Module v5.x** (field definitions)
- **Access Point Discovery Sub-Procedure v5.x** (raw capture)
- **Resolution Engine v5.x** (identity matching)
- **Normalization Engine v5.x** (vocabulary mapping)
- **Access Point Normalization Contract v5.x** (normalization rules)
- **Access Point TSV Output Specification v5.x** (output format)

------------------------------------------------------------
# END OF ACCESS POINT VOCABULARY MODULE v5.1
