# NATURAL AREAS PROJECT — ACCESS POINT SCHEMA MODULE v3.2.2
Authoritative, versioned schema for **Access Points** in the statewide
Natural Areas & Trails system.

This module defines:
- The Access Point entity type
- The 13 normalized Access Point fields (authoritative order)
- Field‑level rules
- Identity rules
- Relationship rules
- Dependencies on the Access Point Vocabulary Module v3.2.2

This module contains no controlled vocabularies.
All vocabularies are defined in the **Access Point Vocabulary Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

An **Access Point** is a visitor‑facing, navigational entry location associated
with one or more parent entities. Access Points provide the coordinates, road
names, counties, and practical details needed to reach a Site, Trail, or
Trail Segment.

Access Points are a distinct entity type and do not modify the schemas of
Sites, Trails, Trail Segments, Site Networks, or Trail Networks.

This schema:
- Establishes the authoritative Access Point record structure
- Defines field‑level rules
- Ensures consistency across all counties and data sources
- Supports discovery, normalization, resolution, and TSV output

This module is authoritative for **Access Point structure**.

------------------------------------------------------------
# 2. ACCESS POINT FIELDS (13 FIELDS, AUTHORITATIVE ORDER)

1. **Access Point Name**
2. **Access Point Type**
3. **Parent Entities (raw)**
4. **Road Name**
5. **County**
6. **GPS Coordinates**
7. **Plus Code**
8. **Access Notes**
9. **URL**
10. **Map URL**
11. **Network Affiliation**
12. **Status**
13. **Derived Label** *(computed, not stored)*

This order is absolute and must never change.

------------------------------------------------------------
# 3. FIELD‑BY‑FIELD RULES

## 3.1 Access Point Name
- Must be a human‑readable name.
- Must be unique within the **set of parent entities**.
- Use authoritative names when available.
- If unnamed but clearly identifiable, construct:
  **Primary Parent Name + " — " + Access Point Type**
- For multi‑parent APs, the Primary Parent is the first in the ordered list.
- For Sites that *are themselves* the navigational feature (e.g., covered bridges),
  the AP Name may equal the Site name **only if** a distinct visitor‑facing entrance exists.
- Do not invent names beyond these rules.

## 3.2 Access Point Type
- Must match a value from the Access Point Vocabulary Module v3.2.2.
- Must describe a visitor‑facing navigational entry node.
- Must not describe internal features or amenities.

## 3.3 Parent Entities (raw)
- Required.
- Semicolon‑delimited list of one or more parent entities.
- Each parent must match the exact **Name** of a normalized:
  - Site, or
  - Trail, or
  - Trail Segment
- **Ontology clarification:**
  - Access Points may attach directly to **Trails** when no Trail Segments exist.
  - When Segments exist, APs may attach to Trails, Segments, or both.
  - APs must not be invented solely to compensate for missing Segments.
- Ordering:
  1. Sites (alphabetized)
  2. Trails (alphabetized)
  3. Trail Segments (alphabetized)
- Must not include Site Networks or Trail Networks.
- Must not include non‑identity associations.

## 3.4 Road Name
- Must be an authoritative, published road name when available.
- No invented street numbers.
- Allowed fallback patterns (non‑inventive):
  - “Forest Road ###”
  - “Township Road ###”
  - “County Road ###”
  - “USFS Road ###”
- For mapped but unnamed drives, use generic labels such as “Park Entrance Drive”
  only if supported by authoritative mapping.
- Blank if no authoritative or defensible designation exists.

## 3.5 County
- Required.
- Must represent the county in which the Access Point physically resides.
- Semicolon‑delimit if multiple; alphabetical order.
- Must not be inferred solely from parent entities.

## 3.6 GPS Coordinates
- Decimal degrees, WGS84.
- Format: `lat,lon` with no space after comma.
- Must represent the physical location of the Access Point.
- **Lifecycle rule:**
  - **Discovery:** GPS is strongly preferred but may be blank.
  - **Resolution:** GPS must be assigned using authoritative sources.
  - **Normalization/TSV:** GPS is required before inclusion in the statewide database.

## 3.7 Plus Code
- Derived from accepted GPS coordinates.
- Required once GPS is present.
- Blank if GPS is blank.

## 3.8 Access Notes
- Short, factual, non‑invented details relevant to reaching or using the AP.
- Must not include features, amenities, or ecological descriptions.
- Must not duplicate parent entity information.
- **Access Notes capture entrance‑specific operational details**, such as:
  - gates, turnstiles, or access controls
  - directional instructions (“Bicycles must stay left when entering”)
  - seasonal conditions
  - parking constraints
  - surface or grade issues
  - signage or visibility notes
- Must remain strictly operational and non‑narrative.

## 3.9 URL
- Optional.
- Full `https://` URLs only.
- Semicolon‑delimit if multiple.
- Must reference authoritative sources.

## 3.10 Map URL
- Full `https://` URL to an authoritative map or GIS viewer.
- May include PDF maps, static images, or interactive GIS layers.
- Semicolon‑delimit if multiple.
- Blank if none.

## 3.11 Network Affiliation
- Optional.
- Semicolon‑delimited list.
- Represents formal affiliations with larger systems (e.g., Buckeye Trail Network).
- Must not encode hierarchy or ownership.
- Must not duplicate any **Parent Entity Name** string, but may reference
  related networks with similar names.
- Networks listed here are **associations**, not parents.

## 3.12 Status
- Must match a value from the Access Point Vocabulary Module v3.2.2.
- Must describe the Access Point itself.

## 3.13 Derived Label
- Computed, not stored.
- Formula: **Access Point Type + " Access Point"**
- Must match Access Point Type exactly.
- No punctuation or parentheses.

------------------------------------------------------------
# 4. IDENTITY RULES

An Access Point is valid only if:

- **It corresponds to a real, physical entrance** that can be mapped during resolution.
- **It is discoverable** in at least one authoritative or defensible source
  (e.g., agency map, trail association map, county GIS, USFS map, GNIS, documented fieldwork).
- **It has one or more parent entities** (Site, Trail, or Trail Segment).
- **It is visitor‑facing**, meaning a visitor would reasonably use it to begin access.
- **It does not duplicate** another AP at the same location with the same parent set and type.
- **It does not encode non‑identity associations** in the parent field.

### Special rule for Sites that are navigational endpoints
Sites that *are themselves* the navigational destination (e.g., covered bridges,
overlooks, historic structures) **do not require Access Points** unless they have
distinct, visitor‑facing entrances separate from the Site itself.

If any identity condition fails, the Access Point must not be created.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Identity vs. Association
- **Parent Entities (raw)** define identity.
- Networks do **not** define identity and must never appear in Parent Entities.

## 5.2 Network Associations
- Access Points may be associated with:
  - Site Networks
  - Trail Networks
- These associations **must appear only in the Network Affiliation field**.
- Networks must not be treated as parents, containers, or identity‑defining entities.

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- **Access Point Vocabulary Module v3.2.2**
- **Normalization Contract v3.2.2**
- **TSV Output Specification v3.2.2**
- **Resolution Module v3.2.2**
- **Discovery Protocol Module v3.2.2**

------------------------------------------------------------
# END OF ACCESS POINT SCHEMA MODULE v3.2.2