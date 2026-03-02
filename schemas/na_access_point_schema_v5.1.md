# NATURAL AREAS PROJECT
# ACCESS POINT SCHEMA MODULE v5.1
(Authoritative Schema for Normalized Access Point Entities)

This module contains no controlled vocabularies.
All vocabularies are defined in the **Access Point Vocabulary Module v5.x**.

This module is authoritative for the structure and semantics of
**Access Point** entities.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Derived Label removed**: No longer computed or stored — presentation-layer
  concern only; consistent with Site entity architectural decision
- **Map URL removed**: Map URLs now captured in urls_raw at discovery stage
  and included in url at normalized stage (semicolon-delimited)
- **identity_notes added**: Separate normalized field for identity
  clarifications, distinct from notes
- **GPS split at discovery stage**: gps_raw replaced by gps_lat_raw +
  gps_lon_raw at discovery; normalized fields gps_lat + gps_lon unchanged
- **GPS Hold Workflow retired**: GPS acquisition now handled by GPS
  Acquisition Module (Stage 3 of pipeline), consistent with all entities
- **Field count updated**: 16 fields (was 17)
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `access_level` removed — redundant with Access Point Type and Status
- `role` removed — not needed
- `gps_primary` replaced by `gps_lat` and `gps_lon` (numeric, WGS84)
- `features` added (semicolon-delimited facilities and amenities)
- `source_primary` removed — provenance tracked via provenance tables
- `municipality` and `township` retained — GIS-derived only, never
  collected during discovery

------------------------------------------------------------
# 1. PURPOSE

An **Access Point** is a visitor-facing, navigational entry location
associated with one or more parent entities. Access Points provide the
coordinates, jurisdictional context, and practical details needed to reach
a Site, Trail, or Trail Segment.

Access Points are a distinct entity type and do not modify the schemas of
Sites, Trails, Trail Segments, Site Networks, or Trail Networks.

This schema is authoritative for **Access Point structure**.

------------------------------------------------------------
# 2. ACCESS POINT FIELDS (16 FIELDS, AUTHORITATIVE ORDER)

1.  **Access Point Name**
2.  **Access Point Type**
3.  **Status**
4.  **Identity Parent Entity Type**
5.  **Identity Parent Entity ID**
6.  **County**
7.  **Township**
8.  **Municipality**
9.  **Address**
10. **GPS Latitude**
11. **GPS Longitude**
12. **Plus Code**
13. **Features**
14. **Identity Notes**
15. **Notes**
16. **URL**
17. **Access Point ID**

Parent relationships beyond the identity parent are stored in
`access_point_parents`.

------------------------------------------------------------
# 3. FIELD-BY-FIELD RULES

## 3.1 Access Point Name
- Must be a human-readable name.
- Must be unique within the set of parent entities.
- Use authoritative names when available.
- If unnamed but clearly identifiable, normalization may construct a name
  using the normalization contract rules (e.g., primary parent name + type).
- Must not be invented beyond these rules.

## 3.2 Access Point Type
- Must match a value from the Access Point Type vocabulary.
- Must describe a visitor-facing navigational entry node.
- Must not describe internal features or amenities.
- Must not be inferred solely from amenities.

## 3.3 Status
- Optional.
- Must match a value from the Access Point Status vocabulary.
- Must describe the Access Point itself, not the parent entity.
- Allowed values: Active, Closed, Seasonal, Restricted.
- Leave blank if ambiguous or unverifiable.

## 3.4 Identity Parent Entity Type
- Required.
- Must be one of: Site, Trail, Trail Segment.
- Represents the single identity-defining parent for the Access Point.
- Must not be inferred from proximity alone.

## 3.5 Identity Parent Entity ID
- Required.
- Must reference a normalized entity in the Entity Graph.
- Must be consistent with `access_point_parents` entries.

## 3.6 County
- Required.
- Must represent the single county in which the Access Point physically
  resides.
- Must not include the word "County."
- Must not be a semicolon-delimited list — Access Points are point
  locations.
- Must not be inferred solely from parent entities.

## 3.7 Township
- Optional.
- Populated via GIS spatial lookup during normalization.
- Not collected during web discovery.
- Must represent the civil township in which the Access Point resides.
- Blank if unverifiable.

## 3.8 Municipality
- Optional.
- Populated via GIS spatial lookup during normalization.
- Not collected during web discovery.
- Must represent the municipality in which the Access Point resides.
- Blank if unverifiable or outside any municipality.

## 3.9 Address
- Optional.
- Must be an authoritative or defensible address or road description.
- No invented street numbers.
- Allowed fallback patterns when supported by mapping:
  - "Forest Road ###"
  - "Township Road ###"
  - "County Road ###"
  - Generic labels such as "Park Entrance Drive" when supported by
    authoritative mapping.
- Must never be USPS-normalized.
- Blank if no authoritative or defensible designation exists.

## 3.10 GPS Latitude
- Type: numeric (decimal degrees, WGS84).
- Sourced from gps_lat_raw at discovery stage.
- May be blank during discovery; required before inclusion in statewide
  database.
- Must represent the physical location of the Access Point.
- Must never be inferred.
- Must be present if GPS Longitude is present.
- If blank after normalization, entity is routed to GPS Acquisition
  Module (Stage 3) for resolution.

## 3.11 GPS Longitude
- Type: numeric (decimal degrees, WGS84).
- Sourced from gps_lon_raw at discovery stage.
- May be blank during discovery; required before inclusion in statewide
  database.
- Must represent the physical location of the Access Point.
- Must never be inferred.
- Must be present if GPS Latitude is present.

## 3.12 Plus Code
- Derived from accepted gps_lat and gps_lon values.
- Required once GPS is present.
- Blank if GPS is blank.

## 3.13 Features
- Optional.
- Semicolon-delimited flat list of documented facilities and amenities
  present at the access point.
- Must match Features vocabulary values.
- Metadata may appear in parentheses: "parking (50 spaces, 4 ADA)"
- Must not include features of the parent entity.
- Must not be inferred.

## 3.14 Identity Notes
- Optional free-text field for identity clarifications.
- Use for: disambiguation notes, access point type uncertainty, parent
  entity assignment notes, flag rationale.
- Must not duplicate Notes content.
- Must not include operational or contextual notes (those go in Notes).

## 3.15 Notes
- Optional.
- Short, factual, non-invented operational details specific to this
  access point.
- Captures entrance-specific details: gate hours, seasonal conditions,
  parking constraints, surface/grade issues, fees, signage/visibility.
- Must not include features (use Features field).
- Must not duplicate parent entity information.
- Must remain strictly operational and non-narrative.

## 3.16 URL
- Optional.
- Full https:// URLs only.
- Semicolon-delimit if multiple authoritative URLs exist, including
  any map URLs (authoritative maps, GIS viewers, PDF maps).
- Must reference authoritative sources.

## 3.17 Access Point ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- Must be a valid integer matching the entity's access_point_id.
- Enables joins to the access_point_parents relationship table.

------------------------------------------------------------
# 4. IDENTITY RULES

An Access Point is valid only if:

- It corresponds to a real, physical entrance that can be mapped.
- It is discoverable in at least one authoritative or defensible source.
- It has at least one parent entity (Site, Trail, or Trail Segment)
  recorded in `access_point_parents`.
- It is visitor-facing: a visitor would reasonably use it to begin access.
- It does not duplicate another Access Point at the same location with the
  same parent set and type.

Special rule for Sites that are navigational endpoints:
- Sites that are themselves the navigational destination do not require
  Access Points unless they have distinct, visitor-facing entrances
  separate from the Site itself.

If any identity condition fails, the Access Point must not be created.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Identity vs. Association

Identity is defined by the combination of:
- Identity Parent
- Location (GPS)
- Access Point Type

## 5.2 Parent Storage

All parent relationships stored in `access_point_parents`:
- `access_point_id`
- `parent_entity_type` (Site, Trail, Trail Segment)
- `parent_entity_id`

Identity parent must be one of these rows.
Additional parents stored as additional rows in same table.

------------------------------------------------------------
# 6. DISCOVERY PHASE NOTE

The following fields are not collected during web discovery:

- `gps_lat`, `gps_lon` — converted from gps_lat_raw + gps_lon_raw by
  Normalization Engine; if blank, resolved by GPS Acquisition Module
- `plus_code` — computed from GPS
- `municipality` — GIS spatial lookup
- `township` — GIS spatial lookup

GPS is required before Access Point is included in the statewide database.
Access Points without GPS after normalization are passed to the GPS
Acquisition Module (Stage 3 of the pipeline) for resolution, consistent
with all other entity types.

------------------------------------------------------------
# 7. MODULE DEPENDENCIES

This module depends on:

- Access Point Vocabulary Module v5.x
- Access Point Normalization Contract v5.x
- Entity Graph Schema v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- GPS Acquisition Module v5.x
- Discovery Protocol Module v5.x
- TSV Output Specification (Access Points) v5.x

------------------------------------------------------------
# END OF ACCESS POINT SCHEMA MODULE v5.1
