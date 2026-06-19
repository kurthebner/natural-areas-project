# NATURAL AREAS PROJECT
# WATER TRAIL DISCOVERY SUB-PROCEDURE v5.1
(Authoritative Protocol for Discovering and Typing Water Trail Entities)

This sub-procedure governs the discovery of all entities associated with
water trails and navigable waterways in the Natural Areas Project v5.x.
It consolidates rules previously scattered across IMP-008, IMP-009,
IMP-019, and IMP-044 into a single authoritative module.

Read this sub-procedure in full before beginning water trail discovery
in any county. Do not rely on handoff summaries or session memory for
water trail entity typing rules.

------------------------------------------------------------
# CHANGES FROM v5.0

**v5.1 — Initial release (IMP-103, 2026-05-07):**
- New module consolidating all water trail entity typing, qualification,
  GPS, and Access Point rules previously scattered across multiple IMPs.
- Supersedes water trail guidance in:
  - IMP-008 (scenic river entity type)
  - IMP-009 (water trail tier assignment)
  - IMP-019 (Water Site category)
  - IMP-044 (Hazard Portage AP type)

------------------------------------------------------------
# 1. PURPOSE AND SCOPE

This sub-procedure covers:

1. **Entity typing** — which entities a waterway or water trail produces
2. **Qualification threshold** — when a paddling route earns a Trail entity
3. **Trail Segments** — when and how to segment a water trail
4. **Discovery sources** — where to look for water trail entities
5. **Discovery workflow** — how to execute water trail discovery efficiently
6. **GPS and address rules** — which entities need GPS, which need addresses
7. **Access Point rules** — Watercraft Access Points and Hazard Portages
8. **Multi-county handling** — how cross-county water trails are discovered

**Scope:** This sub-procedure applies to all Ohio navigable waterways
including rivers, creeks, lakes, reservoirs, and canals where one or
more natural areas entities may exist.

**Not covered here:** GPS acquisition mechanics (see
`discovery/na_gps_acquisition_v5.x.md`), Access Point vocabulary
definitions (see `vocabularies/na_access_point_vocabulary_v5.x.md`),
Trail normalization rules (see `normalization/na_trail_normalization_v5.x.md`).

------------------------------------------------------------
# 2. ENTITY TYPING RULES

A single waterway may produce multiple independent entities. The presence
of one entity type does not imply or exclude others. Assess each type
independently before concluding null.

## 2.1 Water Site

**Definition:** A body of water with formal ecological, scenic, or
regulatory significance. Does NOT require paddling infrastructure, a
named trail, or any Access Points.

**When to create:**
- ✅ State Scenic River designation (Ohio EPA / ODNR)
- ✅ National Wild and Scenic River designation
- ✅ Significant named lake, reservoir, or impoundment managed as a
     natural area or recreation destination
- ✅ Named river reach formally designated as a natural or cultural
     resource by a managing entity

**When NOT to create:**
- ❌ A river segment mentioned only in the context of a paddling trail
     with no independent designation or significance
- ❌ A drainage ditch, unnamed creek, or ephemeral waterway
- ❌ A reservoir whose only public relevance is as a water supply
     (no recreation, no designation)

**Field mapping:**
- entity_type: Site
- category: Water Site
- subtype: River / Lake / Reservoir / Canal (as documented)
- designation: State Scenic River / National Wild and Scenic River
  / other (as documented)
- governance_raw: managing agency name
- notes: document designation source and date if available

**Key rule — intentional absence of trail:**
Many designated scenic rivers have no paddling trail by design.
Corridor protection and water quality preservation often deliberately
limit public access. The absence of a Trail entity is correct and
expected for these rivers. Do not create a Trail entity unless the
qualification threshold in §3 is met independently.

---

## 2.2 Trail (use_type: Paddling)

**Definition:** A formally named, designated paddling route published
by a managing entity, with documented public access points.

**Qualification threshold (§3 defines this fully):**
Full qualification requires a published formal name from a managing
entity plus at least two documented Access Points.

**When to create:**
- ✅ ODNR-designated water trail with published name and map
- ✅ County or regional park district paddling route with formal
     name, published map, and at least two public launches
- ✅ ACA-listed or similar third-party route where the managing
     entity also confirms the route formally
- ✅ Corps of Engineers or other federal paddling trail with
     published documentation

**When NOT to create:**
- ❌ An informal paddling description on a tourism site with no
     managing entity and no documented access points
- ❌ A river segment referenced only as part of a scenic corridor
     with no published paddling route identity
- ❌ A route with only one confirmed Access Point (see §3.2 — flag
     for review instead)

**Field mapping:**
- entity_type: Trail
- use_type_raw: capture raw value; maps to "Paddling" in normalization
- trail_surface_type_raw: "Water" (standard for water trails)
- trail_origin_type_raw: capture as documented
- status_raw: as published
- counties: all counties the route spans
- governance_raw: managing entity name

---

## 2.3 Trail Segment

**Definition:** A distinct section of a named water Trail with
meaningfully different characteristics, management, or access
from adjacent sections.

**When to create Trail Segments:**

Trail Segment boundaries are triggered by any of the following:

| Trigger | Description |
|---------|-------------|
| Management boundary change | Different managing entity for this section, including county line when management also changes |
| Physical interruption | Dam or other obstruction requiring a Hazard Portage AP; the segments above and below are distinct |
| Significant difficulty change | Flatwater transitioning to moving water or whitewater (class change); meaningfully different experience for paddlers |
| Seasonal navigability difference | A section navigable only at certain water levels or seasons while adjacent sections are year-round |

**When NOT to create Trail Segments:**
- ❌ Merely to document distance between access points — Access Points
     alone capture that structure
- ❌ For minor character variation without a clear trigger above
- ❌ Speculatively — only create a Segment when a trigger is documented

**Relationship to the Trail entity:**
- The Trail entity holds the published name, identity, counties, and
  managing entity at the network level.
- Trail Segments are child records linked to the parent Trail.
- The Trail entity must exist before Segments are created.

**Multi-county water trails:**
When a named water trail crosses county lines with different managing
entities on each side, the correct model is:
- One Trail entity (the published named route) spanning both counties
- One Trail Segment per managed section
- The Trail entity is canonically held at the primary managing entity's
  county; the adjacent county's run creates its Segment and links it
  to the held Trail entity at resolution

See §8 (Multi-County Handling) for the full cross-county procedure.

**GPS for Segments:**
Capture start and end reference point GPS coordinates for each Segment
during discovery. Pipeline derives the LineString geometry. See §6.3.

---

## 2.4 Trail Network

**Definition:** A coordinating identity formally organizing multiple
named water trails under one umbrella.

**When to create:**
- ✅ ODNR publishes a named blueway or water trail system that
     explicitly groups multiple named paddling routes
- ✅ A regional authority publishes a branded water trail network
     with a distinct coordinating identity
- ✅ Multiple independently named water trails share a published
     system identity (e.g., "XYZ Blueways System" with member trails)

**When NOT to create:**
- ❌ Multiple sections of one named trail (use Trail Segments instead)
- ❌ An informal grouping of paddling routes with no published
     coordinating identity

**Field mapping:**
- entity_type: Trail Network
- network_type: Water Trail Network
- member_trail_ids: resolved IDs of member Trail entities

---

## 2.5 Access Points

Water trails require Access Points more consistently than land trails.
Every public launch, take-out, and mandatory portage is a candidate
Access Point record.

Two Access Point types apply to water trails:

**Watercraft Access Point:**
A public location where paddlers can launch or take out watercraft.
Includes maintained boat ramps, gravel bars with legal public access,
canoe/kayak launches, and formal take-out platforms.

**Hazard Portage:**
A mandatory carry around a dam, low-head dam, weir, strainer hazard,
or other obstruction that makes the waterway unnavigable or dangerous.
Not a recreational choice — a required safety carry.

See §7 for full Access Point rules including the two-record rule and
address requirements.

---

## 2.6 Co-Existence Rule

A Water Site and a Trail entity can and often do reference the same
physical waterway. They are independent entities assessed independently.

**Example:** The Little Miami River may produce:
- A Water Site (State Scenic River designation, entity_type=Site,
  category=Water Site)
- A Trail (the published Little Miami Scenic Trail paddling route,
  entity_type=Trail)
- Multiple Access Points (boat launches along the route)
- A Trail Segment per managed county section

None of these entities is redundant. Each serves a distinct purpose
in the entity model. Do not suppress one because another exists.

------------------------------------------------------------
# 3. QUALIFICATION THRESHOLD FOR TRAIL ENTITIES

## 3.1 Full Qualification

A paddling route qualifies as a Trail entity when ALL of the
following are met:

1. **Published formal name** — the route has a distinct name
   published by a managing entity (government agency, park district,
   federal agency). The name must be attributable to the managing
   entity, not only to a third-party aggregator.

2. **At least two documented Access Points** — two or more public
   launch or take-out locations are documented by an authoritative
   source (managing entity website, ODNR map, official paddling guide).
   Both must be within the county under discovery OR explicitly
   documented as part of the named route.

3. **Identifiable managing entity** — a government agency, park
   authority, or formally organized conservation body takes
   responsibility for the route. Informal groups, tourism boards,
   and paddling clubs alone do not satisfy this criterion, though
   they may supplement a qualifying managing entity.

When all three criteria are met: create Trail entity, Trail Segments
(if triggers apply), and Access Point records.

---

## 3.2 Near-Miss: WATER_TRAIL_REVIEW Flag

When a paddling route does not fully qualify but shows meaningful
evidence of a named route, retain the record and flag it:

| Condition | Flag | Action |
|-----------|------|--------|
| Named by managing entity but only one confirmed AP | `WATER_TRAIL_REVIEW` | Create Trail record; note missing second AP in identity_notes_raw |
| Named by third party only (ACA, tourism board) with no managing entity confirmation | `WATER_TRAIL_REVIEW` | Create Trail record; note unconfirmed managing entity in identity_notes_raw |
| Managing entity references a route informally with no published map or AP documentation | `WATER_TRAIL_REVIEW` | Create Trail record; note what is missing |
| Route exists in ACA or similar database but no Ohio managing entity can be identified | `WATER_TRAIL_REVIEW` | Create Trail record with third-party source; note for manual verification |

**Staging format:**
```yaml
identity_notes_raw: "WATER_TRAIL_REVIEW: [specific reason for flag —
  e.g., only one confirmed access point; second AP unverified]"
```

Near-miss records enter the standard pipeline and are held for
human review at the Stage 5.5 Human Review Gate before DB upsert.

---

## 3.3 Below Threshold — No Trail Entity

Do not create a Trail entity when:
- No managing entity has published a distinct named route
- Access points are entirely undocumented
- The "route" is only described as "you can paddle this river" with
  no formal identity

Document the negative finding in discovery metadata.

------------------------------------------------------------
# 4. DISCOVERY SOURCES

Work through sources in priority order. Higher-authority sources
override lower-authority sources on field values.

## 4.1 Tier 1 — Primary Authoritative Sources

**ODNR Water Trails Program**
- URL: ohiodnr.gov (search "water trails" or "paddling trails")
- Coverage: ODNR-designated water trails statewide
- Data: named routes, managing entities, access point maps, lengths
- Authority: highest for ODNR-managed or designated routes

**Ohio EPA Scenic Rivers Program**
- URL: epa.ohio.gov/divisions-and-offices/surface-water/scenic-rivers
- Coverage: state-designated scenic rivers
- Data: designated river reaches, designation dates, managing contacts
- Authority: highest for Water Site scenic river designation

**National Wild and Scenic Rivers (NPS / USFS)**
- URL: rivers.gov / nps.gov
- Coverage: federally designated wild and scenic rivers
- Data: designated segments, managing agencies
- Authority: highest for federal designation attribute

---

## 4.2 Tier 2 — Agency and District Sources

**County Park District websites**
- Check each county park district's paddling or water trail section
- Look for: published maps, named routes, launch/take-out lists

**Corps of Engineers recreation guides**
- Applicable for rivers with Corps impoundments, reservoirs, and
  managed recreation areas
- URL: usace.army.mil or district-specific recreation pages
- Data: boat launches, paddling routes, access points with GPS

**MORPC Parks & Open Space GIS layer** (15-county coverage)
- Cross-reference for Access Point GPS verification in covered counties
- See `na_gps_acquisition_v5.x.md` §5.5 for county coverage and
  matching protocol

**Ohio Water Resources Council / Ohio DNR Division of Watercraft**
- Source for boat launch registry data
- Useful for Access Point GPS and address verification

---

## 4.3 Tier 3 — Supplemental Sources

**American Canoe Association (ACA) Trail Finder**
- URL: americancanoe.org
- Use: identify candidate routes; verify against managing entity source
- Authority: supplemental only; ACA listing alone does not satisfy
  managing entity criterion in §3.1

**American Whitewater**
- URL: americanwhitewater.org
- Use: difficulty ratings, hazard locations, portage documentation
- Authority: supplemental; useful for Hazard Portage identification

**County tourism offices and paddling guides**
- Use: lead generation for named routes
- Authority: supplemental; require managing entity confirmation

**Local paddling clubs**
- Use: informal knowledge, hazard portage locations
- Authority: supplemental only

---

## 4.4 Pre-Discovery Checklist

Before beginning water trail discovery in any county:

- [ ] Search ODNR water trails for routes that include this county
- [ ] Search Ohio EPA scenic rivers list for designated reaches in
      this county
- [ ] Check county park district website for paddling section
- [ ] Check NPS/USFS for any federal wild and scenic designations
- [ ] Note any rivers/waterways previously identified in other tiers
      (Tier 1–4) that may have Water Site or water trail significance

Record the checklist outcome in discovery metadata even if all results
are null.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

## 5.1 Economy-of-Scale GPS Capture

When accessing an authoritative source that includes a map, GPS
coordinates, or spatial data (ODNR water trail map, county park
paddling map, Corps recreation guide), capture coordinates and
addresses for ALL entities derivable from that source in a single pass:

1. Trail entity representative point GPS (§6.2)
2. Trail Segment start/end reference points (§6.3)
3. All Access Point GPS coordinates (§6.4)
4. All Access Point street addresses (§6.4)

Do not return to the same authoritative source separately for each
entity type. One pass captures all spatial data for all entities.
Log the source in each entity's `source_map`.

---

## 5.2 Workflow Steps

**Step 1 — Complete pre-discovery checklist (§4.4)**
Before opening any source, confirm what waterways are present in
the county and which may produce entities.

**Step 2 — Visit highest-authority sources first**
Start with ODNR water trails and Ohio EPA scenic rivers. Document
what is found or confirmed null for each source.

**Step 3 — For each candidate waterway or route:**

a. Determine entity types independently (§2):
   - Does this waterway have formal designation significance? → Water Site
   - Does a named paddling route meet the qualification threshold? → Trail
   - Are there distinct managed segments? → Trail Segments
   - Is there a coordinating network identity? → Trail Network
   - What Access Points are documented? → Access Points

b. Apply the qualification threshold (§3) to any Trail candidate.
   Full qualification → Trail entity. Near-miss → WATER_TRAIL_REVIEW.
   Below threshold → no Trail entity; document negative finding.

c. **While on the authoritative source page with spatial data:**
   Execute economy-of-scale GPS capture (§5.1) for all entities
   derived from this source. Do not move to the next source until
   GPS and address capture is complete for all entities from this one.

d. Stage records for all confirmed entities.

**Step 4 — Supplement with Tier 2 and Tier 3 sources**
Check county park district, Corps of Engineers, and ACA for
additional routes or Access Points not found in Tier 1 sources.
Apply the same workflow (Step 3) for each source.

**Step 5 — Document all negative findings**
For each source consulted that yielded no entities, record a null
result in discovery metadata. Silence is not a null.

---

## 5.3 Null Documentation Format

When a source yields no entities:
```yaml
water_trail_discovery_null:
  source: "ODNR Water Trails — [county name]"
  checked: "[date]"
  result: "No ODNR-designated water trails found in county"
  notes: "[any relevant context, e.g., county has no navigable rivers]"
```

------------------------------------------------------------
# 6. GPS AND ADDRESS RULES

## 6.1 General Principle

- **Water trail entity (Trail):** GPS for a representative point; no
  street address for the trail body itself. A street address for a
  linear river corridor is not meaningful and should not be recorded.
- **Trail Segments:** Capture start and end reference point GPS during
  discovery. The pipeline derives LineString geometry from these.
- **Access Points:** GPS required. Street address required (strongly
  preferred). Both must be captured if available.

Capture all spatial data for all entities in one pass while on an
authoritative source with a map (§5.1).

---

## 6.2 Trail Entity GPS

- **GPS point:** The primary put-in / primary launch location is the
  preferred representative point for the Trail entity. If no single
  primary launch is designated, use the upstream terminus.
- **Plus Code:** Derived from the representative GPS point.
- **Street address:** Do NOT record a street address for the Trail
  entity itself. The river body has no street address.
- **Accuracy:** GPS to 5 decimal places if available from authoritative
  source. Accept 4 decimal places from maps. Do not estimate.

---

## 6.3 Trail Segment GPS

- **Capture during discovery:** GPS coordinates for the start point
  and end point of each Segment.
- **Field names in staging:** `segment_start_lat_raw`,
  `segment_start_lon_raw`, `segment_end_lat_raw`, `segment_end_lon_raw`
- **Pipeline derives geometry:** The normalization pipeline converts
  start/end points to a LineString for the Segment geometry field.
  Do not attempt to capture the full river path geometry during
  discovery.
- **If one end is a Hazard Portage:** The portage location is the
  Segment boundary point. Capture the Hazard Portage AP GPS first
  (§6.4), then use those coordinates as the adjacent Segment endpoint.

---

## 6.4 Access Point GPS and Address

**GPS:**
- Required for all water trail Access Points.
- GPS to the physical launch/take-out point (ramp, bank access, or
  portage start), not to the parking lot centroid.
- If only parking lot GPS is available, accept it and note in
  identity_notes_raw.

**Street address — by AP type:**

Address expectations differ by AP type and access situation. Do not
apply a single rule uniformly.

**Watercraft Access Points:**
- Street address strongly expected. A public boat launch, canoe put-in,
  or take-out point almost always has road access and a parking area
  with a findable address.
- Search for the address before concluding it is unavailable.
- If no address is findable after a reasonable search → flag
  `AP_ADDRESS_MISSING` in identity_notes_raw; record the nearest
  cross-street, road name, or landmark in notes_raw.
- A missing address on a Watercraft Access Point is a data quality gap
  that should prompt a second look.

**Hazard Portages:**
- Street address sought but not required. Many portages are at rural
  dams, remote river banks, or stretches of river accessible only from
  the water. No address is the expected and correct result in these cases.
- If road access is evident (urban dam, documented parking area, roadside
  pull-off) → capture the address as you would for a Watercraft Access
  Point.
- If no road access is documented or apparent → leave address blank;
  record the nature of access in notes_raw (e.g., "portage accessed from
  river only; no road access documented"). Do not flag as
  `AP_ADDRESS_MISSING` — a blank address for an inaccessible portage is
  correct data, not a gap.
- If road access is possible but unverified → note "address unverified;
  possible road access via [nearest road]" in notes_raw and flag
  `AP_ADDRESS_UNVERIFIED` in identity_notes_raw for follow-up.

**Summary table:**

| AP Type | Address Expected? | No Address Found |
|---------|------------------|-----------------|
| Watercraft Access | Strongly yes | Flag `AP_ADDRESS_MISSING`; note nearest landmark |
| Hazard Portage — road access evident | Yes | Flag `AP_ADDRESS_MISSING` |
| Hazard Portage — remote / river-access only | No | Leave blank; note in notes_raw |
| Hazard Portage — access uncertain | Uncertain | Flag `AP_ADDRESS_UNVERIFIED`; note nearest road |

------------------------------------------------------------
# 7. ACCESS POINT RULES

## 7.1 Watercraft Access Point

**Definition:** A public location where paddlers can legally launch
or retrieve watercraft. Includes maintained boat ramps, gravel bar
accesses with legal public access, canoe/kayak launch platforms,
and designated take-out points.

**Field mapping:**
- ap_type_raw: "Watercraft Access" (or raw value from source)
- status_raw: as documented
- street address: required (see §6.4)
- GPS: required (physical launch point)
- features_raw: "Boat Ramp" / "Parking Area" / "Restrooms" etc.
  as documented

**Naming convention:**
Name the AP after the launch location, not the river.
- ✅ "Riverside Park Canoe Launch"
- ✅ "State Route 65 Boat Ramp"
- ❌ "Blanchard River Access" — too generic; name the physical location

---

## 7.2 Hazard Portage

**Definition:** A mandatory carry around a dam, low-head dam, weir,
significant hydraulic hazard, or strainer that makes the waterway
unnavigable or dangerous. The portage is not a recreational choice —
it is required for paddler safety.

**When to create a Hazard Portage AP:**
- ✅ A dam or low-head dam is present on the water trail route
- ✅ A hazard is documented by managing entity, ODNR, or American
     Whitewater as a mandatory portage
- ✅ The portage has a carry path documented or discernible from
     source material

**When NOT to create:**
- ❌ A difficult rapid that experienced paddlers may choose to run
     (not a mandatory portage)
- ❌ A seasonal hazard that is not present at normal water levels

**Field mapping:**
- ap_type_raw: "Hazard Portage"
- notes_raw: nature of the hazard (dam, low-head dam, strainer, etc.),
  length of portage if documented, safety notes from authoritative source
- GPS: portage start (river bank above hazard, where paddlers exit)
- street address: capture if road access is evident or documented;
  leave blank if portage is remote or river-access only (see §6.4);
  note access situation in notes_raw either way

**Hazard Portage as Segment boundary:**
A Hazard Portage AP marks the boundary between two Trail Segments
(the navigable section above the hazard and the section below).
Create the Segment boundary at the portage GPS point.

---

## 7.3 Two-Record Rule (IMP-044)

When a boat launch or take-out location is co-located with a Hazard
Portage, create TWO separate AP records:

1. **Watercraft Access Point** — for the recreational launch/take-out
   function
2. **Hazard Portage** — for the mandatory portage function

Do not combine these into one record. The ap_type field is single-value.
The two records share GPS coordinates and address but have distinct
ap_type values, distinct names, and distinct notes.

**Example:**
- "Defiance Dam Portage" (ap_type: Hazard Portage) — mandatory carry
- "Defiance Riverside Launch" (ap_type: Watercraft Access) — recreational
  launch available after the portage at the same location

---

## 7.4 Access Point Count and Trail Qualification

Access Points documented during discovery count toward the §3.1
qualification threshold. The minimum of two Access Points means
two distinct public launch or take-out locations. Hazard Portage
APs do not count toward the qualification threshold — they are not
public access points for launching or retrieving watercraft.

------------------------------------------------------------
# 8. MULTI-COUNTY HANDLING

## 8.1 Core Rule

A named water trail spanning multiple counties is **one Trail entity**,
consistent with the multi-county rule for all Trail entities.

- The `counties` field lists all counties the route spans, alphabetized,
  semicolon-delimited.
- The canonical county is the primary managing entity's county.
- The Trail entity is held at the primary managing county if the
  adjacent county has not yet been discovered. It is released at
  cross-county resolution when both counties have been run.

---

## 8.2 Trail Segments Across County Lines

When a named water trail has different managing entities in different
counties:

- Create one Trail entity (held at primary managing county)
- Create one Trail Segment per distinct managed section
- Each Segment is linked to the Trail entity and carries the managing
  entity for that section in its governance field
- The discoverer for each county creates that county's Segment during
  their county run and stages it against the Trail entity ID (which
  may be a held entity ID if the adjacent county has not yet run)

---

## 8.3 When Both Counties Have Discovered the Same Named Trail

If County A and County B both discover and stage records for the same
named water trail independently (before cross-county resolution runs):

- Both records enter the resolution queue
- Resolution Engine identifies the duplicate via name + counties overlap
- The primary managing entity's record becomes canonical
- The secondary record's segment data is merged into the canonical Trail
- Log the merge in resolution_provenance

This is standard cross-county trail resolution — no water-specific
exception.

---

## 8.4 Segment Discovery by County

**Discovering county's responsibility:**
- Create or identify the Trail entity (held or resolved)
- Create the Trail Segment for their managed section
- Document all Access Points within their county boundary
- If the trail extends beyond their county: note in identity_notes_raw
  and record the out-of-county portion as a cross-county reference

**Do not:**
- Create Access Point records for launches in another county based
  on source material — those belong to that county's discovery run
- Attempt to resolve cross-county entity IDs during discovery — stage
  with the raw trail name and let Resolution handle it

------------------------------------------------------------
# 9. FIELD MAPPING REFERENCE

## 9.1 Water Trail — Trail Entity

| Field | Value / Guidance |
|-------|-----------------|
| entity_type | Trail |
| use_type_raw | Raw value from source; normalizes to "Paddling" |
| trail_surface_type_raw | "Water" |
| trail_origin_type_raw | As documented (natural, developed, etc.) |
| difficulty_raw | If documented (Class I, II, etc.) |
| length_mi_raw | Published route length; do not compute |
| counties | All counties, alphabetized, semicolon-delimited |
| governance_raw | Managing entity name |
| gps_lat_raw | Representative point (primary put-in) |
| gps_lon_raw | Representative point (primary put-in) |
| url_primary_raw | Managing entity page for this route |
| identity_notes_raw | WATER_TRAIL_REVIEW flag if applicable |

---

## 9.2 Water Site Entity

| Field | Value / Guidance |
|-------|-----------------|
| entity_type | Site |
| category_raw | "Water Site" |
| subtype_raw | River / Lake / Reservoir / Canal |
| designation_raw | State Scenic River / National Wild and Scenic River / etc. |
| governance_raw | Managing entity or designating agency |
| status_raw | Active (if designation is current) |
| notes_raw | Designation source, reach description, protection notes |

---

## 9.3 Hazard Portage Access Point

| Field | Value / Guidance |
|-------|-----------------|
| entity_type | Access Point |
| ap_type_raw | "Hazard Portage" |
| gps_lat_raw | Portage start (river bank above hazard) |
| gps_lon_raw | Portage start |
| address_raw | Road access address if evident; blank if remote/river-access only; see §6.4 for flag rules |
| notes_raw | Nature of hazard, portage length, safety notes |

---

## 9.4 Watercraft Access Point

| Field | Value / Guidance |
|-------|-----------------|
| entity_type | Access Point |
| ap_type_raw | "Watercraft Access" |
| gps_lat_raw | Physical launch point |
| gps_lon_raw | Physical launch point |
| address_raw | Parking area or road access address; required |
| features_raw | Boat Ramp / Parking Area / Restrooms / etc. |

------------------------------------------------------------
# 10. CROSS-REFERENCES

This sub-procedure integrates with:

- **`na_gps_acquisition_v5.x.md`** — GPS acquisition mechanics,
  Nominatim fallback rules, MORPC layer (15-county coverage)
- **`na_access_point_vocabulary_v5.x.md`** — Authoritative ap_type
  vocabulary including Watercraft Access and Hazard Portage definitions
- **`na_access_point_normalization_v5.x.md`** — AP normalization rules
  including compound type rule (IMP-084) and empty string enforcement
- **`na_trail_normalization_v5.x.md`** — Trail normalization including
  use_type enforcement (§9.1 read gate)
- **`na_trail_network_vocabulary_v5.x.md`** — Water Trail Network as
  a network_type controlled value
- **`na_resolution_rules_v5.x.md`** — Cross-county entity resolution
  and canonical entity assignment
- **`na_trail_network_discovery_subproc_v5.x.md`** — Trail Network
  discovery when multiple named water trails form a coordinating system

------------------------------------------------------------
# 11. ANTI-PATTERNS

These are common errors to avoid during water trail discovery:

| Anti-Pattern | Correct Approach |
|-------------|-----------------|
| Concluding null for water trail entities after finding no paddling trails, without checking for Water Site designations | Assess Water Site eligibility independently of Trail eligibility (§2.6) |
| Creating a Trail entity for a river that is merely navigable, with no published named route | Apply §3 qualification threshold; below threshold → no Trail entity |
| Omitting Access Point records because "it's just a river bank" | Every public legal launch/take-out is a candidate Watercraft Access Point |
| Omitting a Hazard Portage because the dam is not on the named trail | If the dam is on a water trail route, the portage must be documented |
| Recording a street address for the Trail entity (the river body) | Street address applies to Access Points only; Trail entity uses GPS only |
| Leaving a Watercraft Access Point without a street address without flagging | Flag AP_ADDRESS_MISSING; record nearest landmark; these almost always have road access |
| Flagging a remote Hazard Portage as AP_ADDRESS_MISSING when it has no road access | A blank address is correct for river-access-only portages; note access situation in notes_raw instead (see §6.4) |
| Creating one combined AP record for a co-located launch and portage | Apply two-record rule (§7.3); create two separate AP records |
| Treating a third-party route listing as a qualifying managing entity | Third-party sources require managing entity confirmation for full qualification; flag WATER_TRAIL_REVIEW without it |
| Creating separate Trail entities for each county section of one named route | One Trail entity spanning all counties; use Trail Segments for county sections (§8) |

------------------------------------------------------------
# END OF WATER TRAIL DISCOVERY SUB-PROCEDURE v5.1
