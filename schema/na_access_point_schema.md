# NATURAL AREAS PROJECT
# ACCESS POINT SCHEMA MODULE v4.0 (REVISED)
(Authoritative Schema for Normalized Access Point Entities)

Authoritative, versioned schema for **Access Points** in the statewide
Natural Areas & Trails system under the v4.0 architecture.

This module defines:

- The Access Point entity type  
- The normalized Access Point fields (authoritative logical order)  
- Field‑level rules  
- Identity and relationship rules  
- Dependencies on the Access Point Vocabulary Module v4.0  
- Integration with the Entity Graph Schema v4.0  

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Access Point Vocabulary Module v4.0**.

This module is authoritative for **Access Point structure**.

------------------------------------------------------------
# 1. PURPOSE

An **Access Point** is a visitor‑facing, navigational entry location associated
with one or more parent entities. Access Points provide the coordinates,
jurisdictional context, and practical details needed to reach a Site, Trail,
or Trail Segment.

Access Points are a distinct entity type and do not modify the schemas of
Sites, Trails, Trail Segments, Site Networks, or Trail Networks.

This schema:

- Establishes the authoritative Access Point record structure for v4.0  
- Defines field‑level rules for normalization and TSV output  
- Aligns with the `access_points` and `access_point_parents` tables in the Entity Graph Schema v4.0  
- Ensures consistency across all counties and data sources  

------------------------------------------------------------
# 2. ACCESS POINT FIELDS (LOGICAL ORDER, v4.0)

The following are the **logical Access Point fields** used by normalization
and TSV output. Some are stored directly in `access_points`, others via
relationship or provenance tables.

1. **Access Point Name**  
2. **Access Point Type**  
3. **Access Level**  
4. **Role** (optional)  
5. **Status** (optional)  
6. **Identity Parent**  
7. **Additional Parents**  
8. **County**  
9. **Township**  
10. **Municipality**  
11. **Address**  
12. **GPS Primary**  
13. **Plus Code**  
14. **Access Notes**  
15. **URL**  
16. **Map URL**  
17. **Derived Label** *(computed, not stored)*  

This logical order is authoritative for normalization and TSV output.

### Core storage fields in `access_points` include:

- `access_point_id` (PK)  
- `name`  
- `access_point_type`  
- `access_level`  
- `role`  
- `status`  
- `identity_parent_entity_type`  
- `identity_parent_entity_id`  
- `county`  
- `township`  
- `municipality`  
- `address`  
- `gps_primary`  
- `plus_code`  
- `notes`  
- `url`  
- `map_url`  
- `source_primary`  
- `created_at`  
- `updated_at`  
- `run_id`  

Parent relationships are stored in `access_point_parents`.

------------------------------------------------------------
# 3. FIELD‑BY‑FIELD RULES

## 3.1 Access Point Name

- Must be a human‑readable name.  
- Must be unique **within the set of parent entities**.  
- Use authoritative names when available.  
- If unnamed but clearly identifiable, normalization may construct a name
  using the normalization contract rules (e.g., primary parent + type).  
- Do not invent names beyond these rules.  

## 3.2 Access Point Type

- Must match a value from the Access Point Type vocabulary.  
- Must describe a visitor‑facing navigational entry node.  
- Must not describe internal features or amenities.  
- Must not be inferred solely from amenities.  

## 3.3 Access Level

- Must match a value from the Access Level vocabulary (if defined).  
- Describes visitor access conditions (e.g., Public, Restricted).  
- Must not be inferred without authoritative support.  
- Leave blank if ambiguous or unverifiable.  

## 3.4 Role (Optional)

- If present, must match the Access Point Role vocabulary (if defined).  
- Used to describe functional roles (e.g., primary, overflow).  
- Leave blank if malformed or unverifiable.  

## 3.5 Status (Optional)

- Must match a value from the Access Point Status vocabulary.  
- Must describe the Access Point itself.  
- Leave blank if ambiguous or unverifiable.  

## 3.6 Identity Parent

**Identity parent must be one of: Site, Trail, or Trail Segment.**

- Represents the **single identity‑defining parent** for the Access Point.  
- Must reference a normalized entity in the Entity Graph.  
- Must be consistent with `access_point_parents` entries.  
- Must not be inferred from proximity alone.  
- If multiple candidates exist and cannot be resolved, identity parent is left
  unset and surfaced to Resolution.  

## 3.7 Additional Parents

- Represents additional parent associations beyond the identity parent.  
- May include:  
  - Sites  
  - Trails  
  - Trail Segments  
- Stored as rows in `access_point_parents`:  
  - `access_point_id`  
  - `parent_entity_type`  
  - `parent_entity_id`  
- Must not contradict the identity parent.  
- Must be supported by authoritative sources.  
- Must not be inferred solely from geometry or convenience.  

## 3.8 County

- Required.  
- Must represent the **single** county in which the Access Point physically resides.  
- Stored as `county` in `access_points`.  
- Must not include the word “County”.  
- Must not be a semicolon‑delimited list.  
- Must not be inferred solely from parent entities.  

## 3.9 Township

- Optional.  
- Must represent the civil township in which the Access Point resides.  
- Must not be invented or guessed.  
- Blank if unverifiable.  

## 3.10 Municipality

- Optional.  
- Must represent the municipality (city, village) in which the Access Point resides.  
- Must not be invented or guessed.  
- Blank if unverifiable.  

## 3.11 Address

- Stored as `address` in `access_points`.  
- Optional.  
- Must be an authoritative or defensible address or road description.  
- No invented street numbers.  
- Allowed fallback patterns (non‑inventive) when supported by mapping:  
  - “Forest Road ###”  
  - “Township Road ###”  
  - “County Road ###”  
  - “USFS Road ###”  
  - Generic labels such as “Park Entrance Drive” when supported by authoritative mapping.  
- Must never be USPS‑normalized.  
- Blank if no authoritative or defensible designation exists.  

## 3.12 GPS Primary

- Stored as `gps_primary` in `access_points`.  
- Decimal degrees, WGS84.  
- Format: `lat,lon` with no space after comma.  
- Must represent the physical location of the Access Point.  
- Must never be inferred.  
- Lifecycle:  
  - Discovery: GPS may be blank.  
  - Resolution: GPS should be assigned using authoritative sources.  
  - Normalization/TSV: GPS is required before inclusion in the statewide database.  

## 3.13 Plus Code

- Stored as `plus_code` in `access_points`.  
- Derived from accepted GPS coordinates.  
- Required once GPS is present.  
- Blank if GPS is blank.  

## 3.14 Access Notes

- Short, factual, non‑invented details relevant to reaching or using the AP.  
- Must not include features, amenities, or ecological descriptions.  
- Must not duplicate parent entity information.  
- Captures entrance‑specific operational details (gates, seasonal conditions,
  parking constraints, surface/grade issues, signage/visibility).  
- Must remain strictly operational and non‑narrative.  

## 3.15 URL

- Optional.  
- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must reference authoritative sources.  

## 3.16 Map URL

- Optional.  
- Full `https://` URL to an authoritative map or GIS viewer.  
- May include PDF maps, static images, or interactive GIS layers.  
- Semicolon‑delimit if multiple.  
- Blank if none.  

## 3.17 Derived Label

- Computed, not stored.  
- Not persisted in `access_points`; computed at TSV output.  
- Derived solely from normalized fields.  
- v4.0 formula:  
  **Access Point Type + " Access Point"**  
- Must not introduce new information.  

------------------------------------------------------------
# 4. IDENTITY RULES

An Access Point is valid only if:

- It corresponds to a real, physical entrance that can be mapped.  
- It is discoverable in at least one authoritative or defensible source.  
- It has at least one parent entity (Site, Trail, or Trail Segment) recorded
  in `access_point_parents`.  
- It is visitor‑facing: a visitor would reasonably use it to begin access.  
- It does not duplicate another AP at the same location with the same parent set
  and type.  
- It does not encode non‑identity associations as parents.  

Special rule for Sites that are navigational endpoints:

- Sites that are themselves the navigational destination do not require Access Points
  unless they have distinct, visitor‑facing entrances separate from the Site itself.  

If any identity condition fails, the Access Point must not be created.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Identity vs. Association

Identity is defined by the combination of:

- Identity Parent  
- Additional Parents (if any)  
- Location (GPS)  
- Access Point Type  

## 5.2 Parent Storage

All parent relationships are stored in `access_point_parents`:

- `access_point_id`  
- `parent_entity_type` (`Site`, `Trail`, `Trail Segment`)  
- `parent_entity_id`  

Identity parent must be one of these rows and must be consistent with
normalization rules.

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- Access Point Vocabulary Module v4.0  
- Access Point Normalization Contract v4.0  
- Entity Graph Schema v4.0  
- Resolution Engine v4.0  
- Normalization Engine v4.0  
- Discovery Protocol Module v4.0  
- Discovery Output Specification v4.0  
- TSV Output Specification (Access Points) v4.0  

------------------------------------------------------------
# END OF ACCESS POINT SCHEMA MODULE v4.0 (REVISED)