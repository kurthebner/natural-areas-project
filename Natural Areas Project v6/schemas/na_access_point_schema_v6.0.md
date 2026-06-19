# NATURAL AREAS PROJECT
# ACCESS POINT SCHEMA MODULE v6.0
(Authoritative Structure, Semantic Rules, and Validation Requirements for Access Point Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Access Point Vocabulary Module v6.x**.

This module is authoritative for the structure and semantics of **Access Point** entities.

------------------------------------------------------------
# CHANGES FROM v5.2 → v6.0

- **Identity Parent Entity Type updated** (§3.4): Allowed values changed from
  "Site, Trail, Trail Segment" to "Site, Trailthing". Trail and Trail Segment
  are unified into the Trailthing entity type in v6.x; Access Points referencing
  trail-related parent entities now reference a Trailthing record.

- **Two new fields added** (IMP-013):
  - `last_verified_date` — date the record was last confirmed accurate
  - `field_verified` — boolean; default false; set true on physical visit
  - Field count: 17 → 19

- **Notes field scope tightened** (IMP-014): Notes is a customer-facing field;
  pipeline provenance artifacts must not appear here (§3.15).

- **Field-by-field rules expanded**: v5.2 rules were minimal. v6.0 provides
  explicit guidance consistent with the v6 schema style across all entity types.

- **`access_notes` not added to Access Points**: The v5 Notes field for Access
  Points was already correctly scoped to operational access detail (gate hours,
  seasonal conditions, restrictions, fees). No separate access_notes field is
  needed. The Notes field guidance in this version formalizes and tightens
  that existing scope.

------------------------------------------------------------
# 1. PURPOSE

An **Access Point** is a visitor-facing, navigational entry location associated
with one or more parent entities. Access Points provide the coordinates,
jurisdictional context, and practical details needed to reach a Site or
Trailthing.

Access Points are a distinct entity type and do not modify the schemas of
Sites, Trailthings, Site Networks, or any other entity type.

Examples:
- A named trailhead with a parking lot and kiosk
- A boat ramp providing river access for paddlers
- A hazard portage point at a dam on a water trail
- A pedestrian park entrance gate
- A roadside pull-off serving as the only access to a nature preserve
- A horse trailer parking area with bridle trail access

An Access Point is distinct from:
- A Site Feature — Features describe internal components of a site; an Access
  Point is a discrete navigational entry location, often with its own GPS
  coordinate and name
- A child Site — child Sites are bounded land units; Access Points are entry
  nodes that may have no land area of their own

This schema is authoritative for **Access Point structure**.

------------------------------------------------------------
# 2. ACCESS POINT FIELDS (19 FIELDS, AUTHORITATIVE ORDER)

**Identity**
1.  Access Point Name
2.  Access Point Type
3.  Status

**Parent Relationship**
4.  Identity Parent Entity Type
5.  Identity Parent Entity ID

**Geography**
6.  County
7.  Township
8.  Municipality
9.  Address
10. GPS Latitude
11. GPS Longitude
12. Plus Code

**Character**
13. Features

**Documentation**
14. Identity Notes
15. Notes
16. URL

**Verification**
17. Last Verified Date
18. Field Verified

**ID**
19. Access Point ID

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Access Point Name
- Must be a human-readable name.
- Use the authoritative name when the managing agency has named the access
  point (e.g., "Griggs Reservoir Trailhead," "South Parking Area").
- If unnamed in authoritative sources, the normalization contract may
  construct a name using: [primary parent entity name] + [ap_type] (e.g.,
  "Pickerel Creek Wildlife Area Boat Ramp"). Must not be invented beyond
  these construction rules.
- Must be unique within the set of parent entities sharing the same location.

## 3.2 Access Point Type
- Must match a value from the Access Point Vocabulary Module v6.x.
- Describes the visitor-facing function of the access point.
- Must not describe internal site features or amenities.
- Must not be inferred solely from nearby amenities.
- Single value only — compound types (e.g., "Trailhead/Parking") are never
  valid. See §4.3 and the Vocabulary Module for compound type handling.

## 3.3 Status
- Optional.
- Must match a value from the Access Point Vocabulary Module v6.x.
- Must describe the status of the Access Point itself — not the parent entity.
- Leave blank if the access point is clearly active and no other status is
  documented.

## 3.4 Identity Parent Entity Type
- Required.
- Must be one of: **Site**, **Trailthing**.
- Represents the single identity-defining parent for this Access Point.
- "Trailthing" replaces the v5 values of "Trail" and "Trail Segment" — both
  are now Trailthing entities in v6.x.
- Must not be inferred from proximity alone.
- Must not be a Site Network — Site Networks do not serve as identity parents
  for Access Points.

## 3.5 Identity Parent Entity ID
- Required.
- Must reference a normalized entity in the project database.
- Format: OH-{COUNTY}-{TYPE}-{SEQ} (Site: OH-{COUNTY}-S-{SEQ},
  Trailthing: OH-{COUNTY}-TT-{SEQ}).
- Must be consistent with entries in the `access_point_parents` relationship
  table.

## 3.6 County
- Required.
- The single county in which the Access Point physically resides.
- Must not include the word "County."
- Must not be a semicolon-delimited list — Access Points are point locations
  in one county.
- Must not be inferred solely from parent entity counties — an AP at a
  county-line trailhead is in one county; determine which.

## 3.7 Township
- Optional.
- GIS-derived only — do not populate during discovery.
- The civil township in which the Access Point resides.
- Populated by the GIS pipeline via point-in-polygon lookup.
- Blank for access points within incorporated municipalities.

## 3.8 Municipality
- Optional.
- GIS-derived only — do not populate during discovery.
- The incorporated municipality in which the Access Point resides.
- Populated by the GIS pipeline.
- Blank for access points in unincorporated township territory.

## 3.9 Address
- Optional.
- An authoritative or defensible address or road description for
  navigation to the access point.
- Must not include invented street numbers.
- Allowed fallback patterns when supported by authoritative mapping:
  - "County Road ###"
  - "Township Road ###"
  - "Forest Road ###"
  - Generic labels such as "Park Entrance Drive" when supported by
    authoritative mapping
- Must never be USPS-normalized.
- Blank if no authoritative or defensible designation exists.

## 3.10 GPS Latitude
- Numeric (decimal degrees, WGS84, north positive).
- Optional during discovery; required before inclusion in statewide database.
- Must represent the physical location of the Access Point itself — the entry
  node — not the parent entity's centroid.
- Must never be inferred, estimated, or taken from the parent entity.
- Sourced from `gps_lat_raw` at discovery stage.
- If blank after normalization, the entity is routed to the GPS Acquisition
  Module for resolution.
- Must be present if GPS Longitude is present.

## 3.11 GPS Longitude
- Numeric (decimal degrees, WGS84, west negative for Ohio).
- Same sourcing and rules as GPS Latitude.
- Must be present if GPS Latitude is present.

## 3.12 Plus Code
- Derived from GPS Latitude and GPS Longitude — never entered manually.
- Populated by the pipeline utility (`na_plus_code.py`).
- Required once GPS is present; blank until GPS is populated.

## 3.13 Features
- Optional.
- Semicolon-delimited list of documented facilities and amenities present
  at the access point.
- Must match values from the Access Point Vocabulary Module v6.x.
- Metadata may appear in parentheses: "Parking Area (50 spaces, 4 ADA)"
- Must not include features of the parent entity — only features physically
  present at this access point.
- Must not be inferred.
- Examples: Parking Area, Restrooms, Kiosk, Picnic Table, Boat Ramp,
  Vault Toilet, Information Board, Bike Rack.

## 3.14 Identity Notes
- Optional free-text field for identity clarifications.
- Use for: access point type uncertainty, parent entity assignment uncertainty,
  disambiguation notes, flag rationale, co-location notes (e.g., when a
  recreational access point shares a physical location with a Hazard Portage).
- Must not duplicate Notes content.
- Must not include operational details (those go in Notes).

## 3.15 Notes
- Optional.
- Short, factual, operational details specific to this access point.
- **Correct scope:** gate hours, seasonal access conditions, parking
  constraints, surface or grade issues, fees, signage visibility, permit
  requirements, safety warnings (especially for Hazard Portage records).
- **Always populate Notes for Hazard Portage records** with: hazard type and
  name (e.g., "Griggs Dam — low-head dam, mandatory portage on river left"),
  carry distance and difficulty if documented, re-entry point location if
  documented, and any safety warnings.
- **Customer-facing field — no provenance artifacts.** Pipeline source
  references, IMP numbers, batch load notes, GPS acquisition sources, and
  similar process or provenance content must not appear here. Notes must be
  readable by someone who knows nothing about the pipeline.
- Must not include Features (those go in the Features field).
- Must not duplicate parent entity information.

## 3.16 URL
- Optional.
- Full https:// URLs only.
- Semicolon-delimit if multiple authoritative URLs exist, including any
  map URLs (authoritative maps, GIS viewers, PDF maps, trailhead guides).
- Must reference authoritative sources.
- Tracking parameters must be removed.

## 3.17 Last Verified Date
- Optional.
- **New in v6.0** (IMP-013).
- DATE field (YYYY-MM-DD).
- Records the date the access point record was last confirmed accurate.
- Particularly important for Access Points: GPS coordinates, parking
  availability, and seasonal conditions change more frequently than most
  entity fields.
- Populate at discovery time; update during any subsequent verification pass.

## 3.18 Field Verified
- Boolean, default false.
- **New in v6.0** (IMP-013).
- Set to true when the user has physically visited this access point and
  confirmed its existence, location, and general character.
- Field verification of an Access Point is distinct from field verification
  of its parent entity — a Site may be field-verified while individual
  trailheads within it have not been.
- Never set to true based on web review or map review alone.
- Enables visit planning queries: `WHERE field_verified = false` identifies
  access points that have never been physically confirmed.

## 3.19 Access Point ID
- TEXT, required for referential integrity and downstream processing.
- Format: OH-{COUNTY}-AP-{SEQ} (e.g., OH-OTT-AP-001).
- Assigned by the Upsert Engine — not populated during discovery.
- Enables joins to the `access_point_parents` relationship table.

------------------------------------------------------------
# 4. IDENTITY RULES

## 4.1 The Standard

An Access Point record is created when **all of the following are true**:

1. It corresponds to a real, physical entry location that can be mapped
   to a GPS coordinate.
2. It is discoverable in at least one authoritative or defensible source.
3. It has at least one parent entity (Site or Trailthing) recorded in
   `access_point_parents`.
4. It is visitor-facing: a visitor would reasonably use it to begin access
   to the parent entity.
5. It does not duplicate another Access Point at the same location with the
   same parent set and type.

If any condition fails, the Access Point must not be created.

## 4.2 The Site-as-Destination Rule

Sites that are themselves the navigational destination do not require Access
Points unless they have distinct, visitor-facing entry locations separate from
the site itself. A cemetery, small preserve, or roadside natural area that a
visitor simply parks near and walks into does not need a separate Access Point
record — the Site record's GPS is sufficient.

Access Points are warranted when: there are multiple distinct entry locations
to a site, a named trailhead with documented facilities exists, the entry
involves specific navigation (boat ramp, parking area, trail access), or the
site has access conditions that warrant a separate entry record.

## 4.3 Compound Type Handling

`ap_type` is a single-value field. When an access point serves two functions:
- **Trailhead + Parking Area**: `ap_type = "Trailhead"`. Represent parking
  in the Features field as "Parking Area" (with count if documented).
- **Parking Area + incidental trail access**: `ap_type = "Parking Area"`.
  Add "Trailhead" to Features only if the source explicitly designates it.
- **Other compound cases**: assign the primary function as `ap_type`; represent
  secondary function in Features if applicable.

## 4.4 Hazard Portage Identity

Hazard Portage is the one ap_type where inference from physical context is
permitted. A documented dam or low-head weir on an active water trail with a
mandatory carry qualifies as a Hazard Portage even if the source does not use
the word "portage." See Vocabulary Module §2.2 for full criteria.

When a recreational access point and a Hazard Portage share the same physical
location (e.g., a park boat ramp just above a dam), create two separate Access
Point records — one for the recreational access and one for the portage — and
note the co-location in `identity_notes` on both records.

## 4.5 AP-to-Site Reclassification (IMP-114)

Any Access Point record with `acres_raw` populated, `description_raw` present,
and governance distinct from the parent trail is a candidate for reclassification
as a Site entity. Surface these during Stage 5.5 Human Review for manual
evaluation. See Access Point Normalization Contract v6.x.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Parent Storage

All parent relationships are stored in the `access_point_parents` table:
- `access_point_id` (FK to access_points)
- `parent_entity_type` (Site, Trailthing)
- `parent_entity_id`

The Identity Parent (§3.4, §3.5) must be one of these rows.
Additional parents (e.g., an AP serving both a Site and a Trailthing) are
stored as additional rows in the same table.

## 5.2 Identity Defined By

Identity is defined by the combination of:
- Identity Parent Entity (type + ID)
- GPS location
- Access Point Type

Two access points at the same location with the same parent and type are
duplicates — the second must not be created.

------------------------------------------------------------
# 6. DISCOVERY GUIDANCE

## 6.1 What to Capture

- Access point name — exactly as documented; construct per §3.1 if unnamed
- Access point type — from source documentation; verbatim in `ap_type_raw`
- Identity parent — which Site or Trailthing this AP belongs to
- GPS — only if explicitly stated in source; never estimated
- Address — authoritative road description
- Features — amenity list at the access point specifically
- Notes — gate hours, seasonal conditions, fees, restrictions, safety warnings
- URL — authoritative source page or map

## 6.2 What NOT to Populate During Discovery

- `township` — GIS-derived; always blank at discovery
- `municipality` — GIS-derived; always blank at discovery
- `plus_code` — computed from GPS; blank until pipeline run
- `access_point_id` — assigned by Upsert Engine

## 6.3 Raw Discovery Record Fields

```
ap_name_raw:
ap_type_raw:
status_raw:
identity_parent_entity_type:
identity_parent_entity_id:
county:
address_raw:
gps_lat_raw:
gps_lon_raw:
features_raw:
identity_notes_raw:
notes_raw:
urls_raw: []
last_verified_date:
field_verified:
discovery_tier:
```

## 6.4 Entity Type Sequence Within Tiers

Access Points are processed last within each discovery tier:

**Sites → Trailthings → Site Networks → Access Points**

------------------------------------------------------------
# 7. MODULE DEPENDENCIES

This module depends on:

- Access Point Vocabulary Module v6.x
- Access Point Normalization Contract v6.x *(pending)*
- Access Point TSV Output Specification v6.x *(pending — use v5.x spec;
  note two new fields not yet in TSV spec)*
- Site Discovery Sub-Procedure v6.x *(pending)*
- Resolution Engine v6.x *(or v5.x)*
- Normalization Engine v6.x *(or v5.x)*
- GPS Acquisition Module v6.x *(or v5.x)*
- Site Schema Module v6.0 *(for Site parent references)*
- Trailthing Schema Module v6.0 *(for Trailthing parent references)*

------------------------------------------------------------
# END OF ACCESS POINT SCHEMA MODULE v6.0
