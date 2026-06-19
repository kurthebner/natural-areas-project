# NATURAL AREAS PROJECT
# ACCESS POINT VOCABULARY MODULE v6.0
(Authoritative Controlled Vocabularies for Access Point Fields)

This module contains all controlled vocabularies for Access Point entities
in the Natural Areas Project v6.x.

All Access Point-related modules must reference this module for vocabulary
authority.

------------------------------------------------------------
# CHANGES FROM v5.3 → v6.0

- **Identity Parent Entity Type updated** (§4): References to "Trail" and
  "Trail Segment" as parent entity types replaced with "Trailthing" throughout,
  consistent with the Trailthing unified entity type in v6.x.

- **Last Verified Date and Field Verified guidance added** (§5, IMP-013).

- **Notes field guidance tightened** (§6, IMP-014): Customer-facing field;
  provenance artifacts prohibited. Correct scope formalized.

- **All v5.3 controlled vocabularies carried forward unchanged**: Access Point
  Type and Status values are identical to v5.3. No values added or removed.

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Access Point Type (§2)
- Status (§3)

And provides field guidance for free-text fields:
- Features (§4)
- Identity Notes (§4)
- Notes (§6)
- Last Verified Date / Field Verified (§5)

These vocabularies are used across:
- Access Point Discovery Sub-Procedure v6.x (raw capture)
- Resolution Engine v6.x (conflict detection)
- Normalization Engine v6.x (vocabulary mapping)
- Access Point TSV Output Specification v6.x (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from geometry, amenities, or context
- If no documented value matches, leave the field blank

**Note on water trail-specific types:** "Hazard Portage" (§2) is the one
ap_type where inference from physical context is permitted — a documented
dam or low-head weir on an active water trail with a mandatory carry
qualifies even if the source does not use the word "portage."

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
- Hazard Portage

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
Primary pedestrian or multi-use entry point to a Trailthing or Site-based
trail system.

**When to use:**
- ✅ Documented as "trailhead" by managing agency
- ✅ Marked as trail system entrance
- ✅ Primary pedestrian access to trail

**When NOT to use:**
- ❌ Every place where a trail meets a road
- ❌ Internal trail junctions
- ❌ Informal trail access points without documentation

**Compound Type Rule — Trailhead + Parking Area:**
When an access point serves as both a Trailhead and a Parking Area, trail
access takes precedence:
- `ap_type = "Trailhead"`
- Parking represented in `features` as "Parking Area" (with count if documented:
  "Parking Area (8 spaces)")
- Compound values such as "Trailhead/Parking" or "Trailhead & Parking" in
  `ap_type` are **never valid**

**Reverse case — Parking Area with trail access:**
When a Parking Area is the primary function and trail access is secondary:
- `ap_type = "Parking Area"`
- Add "Trailhead" to features only if the source explicitly designates it as a
  trailhead. Do not add "Trailhead" to features based solely on proximity to a trail.

**Normalization:**
- "trail head," "trail-head" → "Trailhead"
- "trailhead/parking," "trailhead & parking," "trailhead with parking" → "Trailhead"
  (parking → features)

---

### Parking Area

**Definition:**
Visitor parking area that functions as an access node to a site or trail.

**When to use:**
- ✅ Documented parking serving as access point
- ✅ Parking lot designated as site or trail entry
- ✅ Parking area is the primary access method

**When NOT to use:**
- ❌ Internal parking not serving as an entry point
- ❌ Overflow parking without navigational access function
- ❌ Maintenance vehicle parking

**Normalization:** "parking lot," "parking" → "Parking Area"

---

### Boat Ramp

**Definition:**
Constructed, sloped launch surface for trailered or motorized watercraft.

**When to use:**
- ✅ Paved or constructed ramp explicitly documented
- ✅ Designed for trailered boats
- ✅ Explicitly documented as "boat ramp" or "boat launch ramp"

**When NOT to use:**
- ❌ Hand-carry kayak access (use Watercraft Access Point)
- ❌ Unimproved shoreline access

**Normalization:** "boat launch ramp" → "Boat Ramp"

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

**Normalization:** "boat launch" (without "ramp") → "Boat Launch"

---

### Watercraft Access Point

**Definition:**
Water access for non-trailered craft — kayaks, canoes, paddleboards.

**When to use:**
- ✅ Hand-carry watercraft access
- ✅ Kayak or canoe launch
- ✅ Paddleboard access
- ✅ Non-motorized watercraft entry

**When NOT to use:**
- ❌ Boat ramps (use Boat Ramp)
- ❌ Fishing piers without launch capability

**Normalization:** "kayak launch," "canoe access," "canoe launch," "kayak/canoe
access" → "Watercraft Access Point"

---

### River Access

**Definition:**
Fallback category for water access when the specific type is unknown or
does not fit a more specific value.

**When to use:**
- ✅ Source says "river access" generically
- ✅ Water access type unclear from documentation
- ✅ When no more specific water access type applies

**When NOT to use:**
- ❌ If "Boat Ramp" is documented
- ❌ If "Watercraft Access Point" is documented
- ❌ If "Fishing Access" is documented
- ❌ If the point is a mandatory portage (use Hazard Portage)

---

### Fishing Access

**Definition:**
Documented location where fishing access is explicitly provided — a pier,
platform, or shore access point designated for fishing.

**When to use:**
- ✅ Explicitly documented as "fishing access" or "fishing pier"
- ✅ Designated fishing access point

**When NOT to use:**
- ❌ Any shoreline where fishing might occur
- ❌ Inferred from proximity to water or fishing area designation

---

### Hazard Portage

**Definition:**
A mandatory carry-around point on a water trail where paddlers must exit
the water, carry their watercraft overland, and re-enter below the hazard.
Typically at dams, low-head weirs, diversion structures, or other
navigational obstructions that cannot be safely run.

**When to use:**
- ✅ Dam or low-head weir requiring mandatory exit and carry
- ✅ Navigational hazard documented by managing agency, water trail guide,
  or MORPC as a required portage
- ✅ Source uses "portage," "carry," "hazard," "take-out / put-in around [dam]"
- ✅ Even if source does not use the word "portage" — any point where a trail
  guide directs paddlers to leave the water at a dam or weir qualifies

**When NOT to use:**
- ❌ Optional alternate routes around difficult water
- ❌ General paddle-around points without mandatory exit
- ❌ Recreational takeout points unrelated to hazards

**Notes field requirement:**
Always populate `notes` for Hazard Portage records with:
- Name and type of hazard (e.g., "Griggs Dam — low-head dam, mandatory
  portage on river left")
- Carry distance and difficulty if documented
- Re-entry point location if documented
- Safety warnings from the source

**Co-location rule:**
If a recreational access point and a Hazard Portage share the same physical
location (e.g., a park boat ramp just above a dam), create two separate Access
Point records. Note the co-location in `identity_notes` on both records.

**Normalization:**
- "portage," "mandatory portage," "carry," "required carry" → "Hazard Portage"
- "dam portage," "dam carry" → "Hazard Portage"
- "low-head weir portage," "weir carry" → "Hazard Portage"
- "hazard" (in water trail context) → "Hazard Portage"

---

### Bicycle Access

**Definition:**
Documented bicycle-specific entry point — a bike-only entrance or a
documented bicycle access point where cyclists enter separately from
pedestrians or vehicles.

**When to use:**
- ✅ Bike-only entrance documented
- ✅ Explicitly documented bicycle access point
- ✅ Bike path connection point

**When NOT to use:**
- ❌ Multi-use trailhead accessible by bike (use Trailhead)
- ❌ Inferred from existence of a nearby bike trail

---

### Snowmobile Access

**Definition:**
Documented snowmobile entry point to a trail system or site.

**When to use:**
- ✅ Explicitly documented snowmobile access
- ✅ Snowmobile trail system access point

---

### Cross Country Ski Access

**Definition:**
Documented cross-country ski entry point.

**When to use:**
- ✅ Explicitly documented XC ski access
- ✅ Nordic ski trail system access point

**Normalization:** "XC ski access," "nordic ski access" → "Cross Country Ski Access"

---

### Equestrian Access

**Definition:**
Documented horse-riding entry point — horse trailer parking with trail
access, bridle trail access point, or equestrian staging area.

**When to use:**
- ✅ Explicitly documented equestrian access
- ✅ Horse trailer parking with documented trail access
- ✅ Bridle trail access point

**Normalization:** "horse trailer parking" → "Equestrian Access"

---

### Roadside Pull-Off

**Definition:**
Visitor-facing roadside pull-off that functions as an access node to a
site or trail.

**When to use:**
- ✅ Documented roadside access point
- ✅ Pull-off serving as trailhead or site access
- ✅ Scenic overlook with documented trail or site access

**When NOT to use:**
- ❌ Scenic overlooks without trail or site access
- ❌ Maintenance turnouts
- ❌ Emergency pull-offs

**Normalization:** "pulloff," "pull off" → "Roadside Pull-Off"

---

### Pedestrian Entrance

**Definition:**
Walk-in entrance to a Site or Trailthing that is not classified as a
Trailhead — a park gate, path entrance, or walk-in entry point.

**When to use:**
- ✅ Site entrance (not trail-system-specific)
- ✅ Park gate or walk-in entrance
- ✅ Path entrance not designated as a trailhead

**When NOT to use:**
- ❌ Trail system entrances (use Trailhead)

---

### Vehicle Entrance

**Definition:**
Drivable entrance to a Site or Trailthing.

**When to use:**
- ✅ Main gate for vehicle access
- ✅ Entrance road to site
- ✅ Vehicle-accessible entry point

**When NOT to use:**
- ❌ Maintenance-only gates (use Administrative Access)

---

### Transit Access

**Definition:**
Transit stop that functions as a visitor-facing access node to a site
or trail.

**When to use:**
- ✅ Bus stop documented as serving a site or trail
- ✅ Light rail station with documented site or trail access
- ✅ Documented by transit authority or managing agency

---

### Ferry Access

**Definition:**
Ferry landing that serves as a documented access node to a site or trail.

**When to use:**
- ✅ Ferry landing provides documented access to site or trail

---

### Shuttle Access

**Definition:**
Shuttle stop that provides documented access to a Site or Trailthing.

**When to use:**
- ✅ Park shuttle system access point
- ✅ Shuttle stop documented as serving a site or trail

---

### Administrative Access

**Definition:**
Documented, restricted-use access point — staff-only, administrative,
or maintenance access.

**When to use:**
- ✅ Explicitly labeled as restricted or staff-only
- ✅ Administrative or maintenance entrance with documented restrictions

**When NOT to use:**
- ❌ Assumed or inferred restrictions
- ❌ Temporary closures

---

### Other

**Definition:**
Named access type from an authoritative source that does not fit any
other category.

**Discovery guidance:**
Record raw term in `identity_notes_raw`. Flag for vocabulary expansion review.
Do not use "Other" for ambiguous cases where a vocabulary value likely applies —
use the best fit or leave blank.

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
Access point is currently open and operational under normal conditions.

**Discovery guidance:**
Can be left blank if obviously active — Active is the default.

**Normalization:** "open," "operational" → "Active"

---

### Closed

**Definition:**
Access point is permanently or indefinitely closed.

**When to use:**
- ✅ Explicitly documented as closed or decommissioned

**When NOT to use:**
- ❌ Temporary closures (document in Notes)
- ❌ Seasonal closures (use Seasonal)

**Normalization:** "permanently closed," "decommissioned" → "Closed"

---

### Seasonal

**Definition:**
Access point operates on a seasonal schedule — open part of the year,
closed the rest.

**When to use:**
- ✅ Documented seasonal operation
- ✅ "Open May–October" or similar
- ✅ Winter closures with documented opening dates

**Discovery guidance:**
Document season details in Notes (e.g., "Open Memorial Day through Labor Day").

**Normalization:** "seasonal access," "open seasonally" → "Seasonal"

---

### Restricted

**Definition:**
Access point has documented restrictions on use — permit required,
membership required, or documented access limitations.

**When to use:**
- ✅ Explicitly documented as restricted
- ✅ Permit required for entry
- ✅ Membership or reservation required

**When NOT to use:**
- ❌ Assumed restrictions
- ❌ Inferred from access point type

**Discovery guidance:**
Document restriction details in Notes.

**Normalization:** "permit required," "reservation required" → "Restricted"

------------------------------------------------------------
# 4. FEATURES (Free-Text — No Controlled Vocabulary)

## 4.1 Overview

Features at an Access Point is a **free-text field with no controlled
vocabulary**. It uses a list format with optional metadata annotations
in parentheses.

This is distinct from the Site Features field, which uses a controlled
vocabulary. Access Point features are access-point-specific amenities
that do not warrant a full controlled vocabulary.

## 4.2 What to Capture

Facilities and amenities physically present at this access point —
not at the parent entity, not inferred.

**Common values and annotation patterns:**
- "Parking Area" — bare entry
- "Parking Area (12 spaces)" — with count
- "Parking Area (12 spaces, 2 ADA)" — with ADA detail
- "Restrooms" — year-round
- "Vault Toilet" — pit toilet / seasonal restroom
- "Kiosk" — information kiosk
- "Picnic Table" or "Picnic Tables (3)"
- "Bike Rack"
- "Boat Ramp" — when present as a secondary facility at a non-Boat Ramp AP
- "Trailhead" — when parking area AP has a documented designated trailhead nearby
- "Fee Station"
- "Horse Trailer Parking"
- "Information Board"
- "Trail Map Dispenser"
- "Dumpster"
- "Recycling"

## 4.3 What NOT to Capture

- ❌ Features of the parent entity — document those on the parent record
- ❌ Features not physically at this access point
- ❌ Inferred features
- ❌ Narrative prose — Features is a list, not sentences

------------------------------------------------------------
# 5. LAST VERIFIED DATE AND FIELD VERIFIED

## 5.1 Last Verified Date

`last_verified_date` — DATE field (YYYY-MM-DD). No controlled vocabulary.

Particularly important for Access Points: GPS precision, parking availability,
seasonal hours, and fee information change more frequently than most other
entity fields. A stale access point record can actively mislead visitors.

Populate at discovery time with the current date. Update during any
subsequent verification pass.

## 5.2 Field Verified

`field_verified` — boolean, default false.

Set to true when the user has physically visited this specific access point
and confirmed its existence, location, and basic character. Field verification
of an Access Point is distinct from field verification of its parent entity —
verify each separately.

Access Points are especially valuable candidates for field verification because
GPS coordinates from web sources are often imprecise or placed at the parent
entity centroid rather than the actual entry point.

------------------------------------------------------------
# 6. NOTES (Free-Text — No Controlled Vocabulary)

## 6.1 Overview

Notes is a customer-facing free-text field. There is no controlled vocabulary.

## 6.2 What to Capture

Operational details specific to this access point:
- Gate hours ("Open dawn to dusk; gate locked at sunset")
- Seasonal conditions ("Road to trailhead unpaved; impassable after heavy rain")
- Parking constraints ("Overflow parking available at adjacent church lot on
  weekends with permission")
- Surface or grade issues ("Steep descent to boat ramp; difficult for trailers
  over 20 ft")
- Fees ("$5 day use fee; exact change or credit card at kiosk")
- Signage or visibility ("No trailhead sign visible from road; look for brown
  post at gravel pull-off")
- Permit requirements ("Permit required for group use of shelter; contact park
  office")
- Safety warnings — especially for Hazard Portage records (always populate)

## 6.3 What NOT to Capture

- ❌ **Pipeline provenance artifacts** — source citations, IMP numbers, GPS
  acquisition source, batch load notes. Notes is readable by someone who
  knows nothing about the pipeline. Provenance belongs in the provenance
  tables.
- ❌ Features (those go in the Features field)
- ❌ Parent entity information (that belongs on the parent record)
- ❌ Identity flags or type uncertainty (those go in Identity Notes)

------------------------------------------------------------
# 7. IDENTITY NOTES (Free-Text — No Controlled Vocabulary)

## 7.1 Overview

Identity Notes is a free-text field used for identity clarifications —
not operational content.

## 7.2 What to Capture

- Access point type uncertainty ("source unclear whether this is Trailhead
  or Parking Area — kiosk present but no dedicated lot")
- Parent entity assignment uncertainty
- Disambiguation notes (why this is an Access Point vs. a site feature)
- Vocabulary type flags ("source calls this 'boardwalk access' — no vocabulary
  match, flagged for review")
- Co-location notes for Hazard Portage records sharing a physical location
  with a recreational access point

## 7.3 Discovery vs. Normalization

- **Discovery stage**: capture in `identity_notes_raw`
- **Normalized stage**: surfaced as `identity_notes` field

------------------------------------------------------------
# 8. VOCABULARY NORMALIZATION RULES

## 8.1 Access Point Type Normalization Mapping

| Raw Value | Maps To | Notes |
|---|---|---|
| "trail head" / "trail-head" | Trailhead | Case/hyphen normalization |
| "trailhead/parking" / "trailhead & parking" / "trailhead with parking" | Trailhead | Parking → features |
| "parking lot" / "parking" | Parking Area | Standard synonyms |
| "boat launch ramp" | Boat Ramp | Ramp specified |
| "boat launch" (no "ramp") | Boat Launch | Generic motorized launch |
| "kayak launch" / "canoe access" / "canoe launch" | Watercraft Access Point | Non-motorized |
| "kayak/canoe access" | Watercraft Access Point | Non-motorized |
| "XC ski access" / "nordic ski access" | Cross Country Ski Access | Standard synonyms |
| "horse trailer parking" | Equestrian Access | Standard synonym |
| "pulloff" / "pull off" | Roadside Pull-Off | Formatting normalization |
| "portage" / "mandatory portage" / "carry" / "required carry" | Hazard Portage | Water trail context |
| "dam portage" / "dam carry" | Hazard Portage | Standard synonyms |
| "low-head weir portage" / "weir carry" | Hazard Portage | Standard synonyms |
| "hazard" (water trail context) | Hazard Portage | Context-dependent |
| Empty string ("") | null | Empty string is not a valid blank |
| Compound or slash-delimited value | **REVIEW** | Single-value field; apply compound type rules |
| Any value not in §2.1 and not in this table | **null-and-log** | Flag "ap_type OOV: [value]" for review |

## 8.2 Status Normalization Mapping

| Raw Value | Maps To | Notes |
|---|---|---|
| "open" / "operational" | Active | Standard synonyms |
| "permanently closed" / "decommissioned" | Closed | Standard synonyms |
| "seasonal access" / "open seasonally" | Seasonal | Standard synonyms |
| "permit required" / "reservation required" | Restricted | Standard synonyms |
| "closed" (without "permanently") | **REVIEW** | Could be Closed or Seasonal; check source |
| Empty string ("") | null | Empty string is not a valid blank |
| Any value not in §3.1 and not in this table | **null-and-log** | Flag "status OOV: [value]" |

## 8.3 Ambiguous Cases Requiring Context

| Raw Value / Situation | Ambiguity | Resolution |
|---|---|---|
| "boat launch" | Boat Ramp vs. Boat Launch | Check if ramp is specified; if not → Boat Launch |
| "river access" | River Access vs. more specific type | Check for documented boat ramp, kayak launch, or fishing access; if none → River Access |
| "parking" | Parking Area (ap_type) vs. amenity note | Is this the primary function of the record or a feature of another AP? Primary function → ap_type; secondary → features |
| "gate" | Vehicle Entrance vs. Administrative Access vs. not an AP | Check if visitor-facing; staff-only → Administrative Access; visitor-facing → Vehicle Entrance; not an AP → don't create record |
| "carry" | Hazard Portage vs. informal portage note | Confirm water trail context and mandatory nature |

## 8.4 Single-Value Enforcement

`ap_type` and `status` are single-value fields. When a compound value cannot
be resolved to a single canonical value:
1. Set field to blank
2. Append to identity_notes: "[field] compound value: '[raw]' — could not
   resolve; flagged for review"
3. Write raw value to normalization_provenance as "compound_value_stripped"

------------------------------------------------------------
# 9. VOCABULARY USAGE RULES

## 9.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or invented terms
2. **Don't infer** — Values must be documented, not inferred from context
   (exception: Hazard Portage per §2.2)
3. **Leave blank if unclear** — Better no value than wrong value
4. **One value per field** — No compound types in `ap_type` or `status`
5. **Flag new values** — Do not add values; flag for vocabulary expansion

## 9.2 Discovery Phase

- Capture raw values exactly as found in `_raw` fields
- Do not attempt normalization during discovery
- Capture type uncertainty in `identity_notes_raw`
- Never populate `township` or `municipality` at discovery

## 9.3 Normalization Phase

- Apply §8.x mapping tables to all controlled fields
- Handle compound values per §8.4
- Convert empty strings to null per §8.4
- Null-and-log unmappable values
- Surface REVIEW items for human resolution before TSV output

------------------------------------------------------------
# 10. MODULE DEPENDENCIES

This vocabulary module integrates with:

- Access Point Schema Module v6.0 (field definitions)
- Access Point Discovery Sub-Procedure v6.x (raw capture)
- Resolution Engine v6.x (conflict detection)
- Normalization Engine v6.x (vocabulary mapping)
- Access Point Normalization Contract v6.x (normalization rules)
- Access Point TSV Output Specification v6.x (output format)

------------------------------------------------------------
# END OF ACCESS POINT VOCABULARY MODULE v6.0
