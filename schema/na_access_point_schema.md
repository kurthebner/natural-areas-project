# NATURAL AREAS PROJECT — ACCESS POINT SCHEMA MODULE v1
Authoritative, versioned schema for Access Points in the statewide Natural Areas & Trails system.

This module defines:
- The Access Point entity type
- The 10 Access Point fields
- Field‑level rules
- Dependencies on the Access Point Vocabulary Module v1

This module contains no controlled vocabularies.  
All vocabularies are defined in the Access Point Vocabulary Module v1.

---

# 1. PURPOSE
Access Points represent visitor‑facing, navigational entry locations associated with a Site.  
They provide the coordinates, road names, and practical details needed to reach a Site in the real world.

Access Points are a distinct entity type and do not modify the 25‑field Site Schema.

---

# 2. ACCESS POINT FIELDS (10 FIELDS, AUTHORITATIVE ORDER)

1. **Access Point Name**  
2. **Access Point Type**  
3. **Parent Site**  
4. **GPS Coordinates**  
5. **Plus Code**  
6. **Road Name**  
7. **Access Notes**  
8. **URL**  
9. **Status**  
10. **Derived Label** (computed, not stored)

This order is absolute and must never change.

---

# 3. FIELD RULES

## 3.1 Access Point Name
- Must be a human‑readable name.  
- Must be unique within the parent site.  
- Use authoritative names when available.  
- If unnamed but clearly identifiable, construct a name using:  
  **Parent Site + " — " + Access Point Type**  
- Do not invent names beyond this construction rule.

---

## 3.2 Access Point Type
- Must match a value from the **Access Point Vocabulary Module v1**.  
- Must describe a visitor‑facing navigational entry node.  
- Must not describe internal features or amenities.

---

## 3.3 Parent Site
- Must match the exact **Name** field of a normalized Site.  
- Defines the one‑to‑many relationship between Sites and Access Points.  
- A Site may have many Access Points; an Access Point has exactly one parent.

---

## 3.4 GPS Coordinates
- Decimal degrees, WGS84.  
- Required.  
- Must be authoritative.  
- Must represent the physical location of the access point.

---

## 3.5 Plus Code
- Derived from accepted GPS coordinates.  
- Required.  
- Must be blank if GPS is blank.

---

## 3.6 Road Name
- Must be an authoritative, published road name.  
- No invented street numbers.  
- No reverse‑geocoded approximations.  
- Blank if not authoritative.

---

## 3.7 Access Notes
- Short, factual, non‑invented details relevant to reaching or using the access point.  
- Must not include features, amenities, or ecological descriptions.  
- Must not duplicate information from the parent Site.

---

## 3.8 URL
- Optional.  
- Must be a full `https://` URL.  
- Semicolon‑delimit multiple URLs.  
- Must reference authoritative sources only.

---

## 3.9 Status
- Must match a value from the **Access Point Vocabulary Module v1**.  
- Must describe the access point itself, not the parent site.

---

## 3.10 Derived Label
- Computed, not stored.  
- Formula: **Access Point Type + " Access Point"**  
- Must match the Access Point Type exactly.  
- No parentheses or punctuation.

---

# 4. IDENTITY RULES
An Access Point is valid only if:
- It is mappable.  
- It is discoverable in authoritative sources.  
- It is tied to a parent Site.  
- It represents a visitor‑facing navigational entry location.

If any of these conditions fail, the Access Point must not be created.

---

# 5. MODULE DEPENDENCIES
This module depends on:

- **Access Point Vocabulary Module v1**  
  (for Access Point Type and Access Point Status)

All other modules (Normalization, TSV Output, Discovery, Resolution, Orchestration) must reference this schema.

---

# END OF ACCESS POINT SCHEMA MODULE v1