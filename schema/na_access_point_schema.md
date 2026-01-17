# NATURAL AREAS PROJECT — ACCESS POINT SCHEMA MODULE v1.2
Authoritative, versioned schema for Access Points in the statewide Natural Areas & Trails system.

This module defines:
- The Access Point entity type  
- The 11 Access Point fields (identity‑bearing)  
- Field‑level rules  
- Identity rules  
- Dependencies on the Access Point Vocabulary Module v1 and the Access Point Association Module v1  

This module contains no controlled vocabularies.  
All vocabularies are defined in the Access Point Vocabulary Module v1.

---

# 1. PURPOSE
Access Points represent visitor‑facing, navigational entry locations associated with a parent entity.  
They provide the coordinates, road names, counties, and practical details needed to reach a Site or Trail Segment in the real world.

Access Points are a distinct entity type and do not modify the schemas of Sites, Sub‑Sites, Trails, Trail Segments, Area Networks, or Trail Networks.

This schema:
- Establishes the Access Point record structure  
- Defines field‑level rules  
- Ensures consistency across all counties and data sources  
- Provides the foundation for normalization, TSV output, discovery, resolution, and association mapping  

This module is authoritative for Access Point structure.

---

# 2. ACCESS POINT FIELDS (11 FIELDS, AUTHORITATIVE ORDER)

1. **Access Point Name**  
2. **Access Point Type**  
3. **Parent Entity**  
4. **Road Name**  
5. **County**  
6. **GPS Coordinates**  
7. **Plus Code**  
8. **Access Notes**  
9. **URL**  
10. **Status**  
11. **Derived Label** (computed, not stored)

This order is absolute and must never change.

---

# 3. FIELD‑BY‑FIELD RULES

---

## 3.1 Access Point Name
- Must be a human‑readable name.  
- Must be unique within the parent entity.  
- Use authoritative names when available.  
- If unnamed but clearly identifiable, construct a name using:  
  **Parent Entity Name + " — " + Access Point Type**  
- Do not invent names beyond this construction rule.

---

## 3.2 Access Point Type
- Must match a value from the **Access Point Vocabulary Module v1**.  
- Must describe a visitor‑facing navigational entry node.  
- Must not describe internal features or amenities.

---

## 3.3 Parent Entity
- An Access Point must have **exactly one** parent.  
- The parent must be one of the following entity types:  
  - **Site**  
  - **Trail Segment**  
- The parent must be the entity that physically contains or governs the Access Point.  
- Parent–child relationships must be explicitly documented in authoritative sources.  
- Secondary relationships (e.g., “also serves Trail X”) must be recorded in the  
  **Access Point Association Module**, not in this field.

---

## 3.4 Road Name
- Must be an authoritative, published road name.  
- No invented street numbers.  
- No reverse‑geocoded approximations.  
- Blank if not authoritative.

---

## 3.5 County
- Required.  
- Must match the official Ohio county list.  
- Must represent the county in which the Access Point physically resides.  
- Semicolon‑delimit if multiple counties are confirmed.  
- Alphabetical order.  
- Must not be inferred from the parent entity.

---

## 3.6 GPS Coordinates
- Decimal degrees, WGS84.  
- Required.  
- Format: `lat,lon` with no space after comma.  
- Must represent the physical location of the Access Point.  
- Must be authoritative.

---

## 3.7 Plus Code
- Derived from accepted GPS coordinates.  
- Required.  
- Must be blank if GPS is blank.

---

## 3.8 Access Notes
- Short, factual, non‑invented details relevant to reaching or using the Access Point.  
- Must not include features, amenities, or ecological descriptions.  
- Must not duplicate information from the parent entity.

---

## 3.9 URL
- Optional.  
- Must be a full `https://` URL.  
- Semicolon‑delimit multiple URLs.  
- Must reference authoritative sources only.

---

## 3.10 Status
- Must match a value from the **Access Point Vocabulary Module v1**.  
- Must describe the Access Point itself, not the parent entity.

---

## 3.11 Derived Label
- Computed, not stored.  
- Formula: **Access Point Type + " Access Point"**  
- Must match the Access Point Type exactly.  
- No parentheses or punctuation.

---

# 4. IDENTITY RULES
An Access Point is valid only if:
- It is mappable.  
- It is discoverable in authoritative sources.  
- It has exactly one parent entity (Site or Trail Segment).  
- It represents a visitor‑facing navigational entry location.  
- It does not duplicate another Access Point at the same location.  
- It does not encode secondary relationships in the parent field.

If any of these conditions fail, the Access Point must not be created.

---

# 5. RELATIONSHIP RULES

### 5.1 Identity vs. Association
- The **Parent Entity** defines identity.  
- All other relationships must be represented in the  
  **Access Point Association Module v1**.  
- Associations do not define identity.

### 5.2 Allowed Secondary Associations
An Access Point may be associated with:
- Sites  
- Sub‑Sites  
- Trails  
- Trail Segments  
- Area Networks  
- Trail Networks  

These associations must not appear in the Access Point Schema.

---

# 6. MODULE DEPENDENCIES
This module depends on:

- **Access Point Vocabulary Module v1**  
  (for Access Point Type and Access Point Status)

- **Access Point Association Module v1**  
  (for secondary relationships)

All other modules (Normalization, TSV Output, Discovery, Resolution, Orchestration) must reference this schema.

---

# END OF ACCESS POINT SCHEMA MODULE v1.2