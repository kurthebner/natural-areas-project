# NATURAL AREAS PROJECT — ACCESS POINT ASSOCIATION MODULE v3.2
(Secondary, Non‑Identity Relationships for Access Points)

Authoritative, versioned module defining secondary (non‑identity) relationships  
between Access Points and other entity types in the statewide Natural Areas &  
Trails system.

This module defines:
- The Access Point Association entity type  
- The fields and authoritative field order  
- Field‑level rules  
- Allowed association types  
- Identity and validity rules  
- Dependencies on v3.2 schema and vocabulary modules  

This module contains no controlled vocabularies.  
All vocabularies referenced here are defined in their respective v3.2 entity  
vocabulary modules.

------------------------------------------------------------
# 1. PURPOSE

Access Points may serve multiple entities in the real world (e.g., a state park,  
a regional trail, a specific trail segment, a trail network, or a site network).

However, Access Points must have **exactly one identity‑defining parent**:
- A **Site**, or  
- A **Trail Segment**

The Access Point Association Module provides a structured way to record all  
**secondary, non‑identity relationships** between an Access Point and other  
entities.

This module:
- Defines how Access Points may be associated with multiple Trails, Trail  
  Segments, Sites, Trail Networks, and Site Networks  
- Ensures these associations do not affect Access Point identity  
- Provides a normalized structure for discovery, resolution, and TSV output  
- Prevents multi‑parent ambiguity in the core Access Point schema  

This module is authoritative for Access Point associations.

------------------------------------------------------------
# 2. ACCESS POINT ASSOCIATION FIELDS (AUTHORITATIVE ORDER)

1. **Access Point Name**  
2. **Associated Entity Type**  
3. **Associated Entity Name**  
4. **Association Type**  
5. **Notes**  
6. **Source Confidence**  
7. **Verification Status**  
8. **Field Confidence Map**  
9. **Field Verification Map**  

This order is absolute and must never change.

------------------------------------------------------------
# 3. FIELD‑BY‑FIELD RULES

## 3.1 Access Point Name
- Must match the exact **Access Point Name** of a normalized Access Point.  
- Defines the Access Point to which this association applies.  
- Must not reference Access Points that fail identity rules.

## 3.2 Associated Entity Type
Must be one of the **six v3.2 ontology types**:

- **Site**  
- **Trail**  
- **Trail Segment**  
- **Trail Network**  
- **Site Network**  
- **Access Point** *(rare; used only for paired or co‑located APs)*

Rules:
- Must match the entity type of the associated record.  
- Must not include entities outside the Natural Areas ontology.  
- **Sub‑Sites must not appear** (they are Sites with Parent Site populated).

## 3.3 Associated Entity Name
- Must match the exact **Name** field of the associated entity.  
- Must not reference entities that fail identity rules.  
- Must not be inferred, constructed, or normalized.

## 3.4 Association Type

Defines the nature of the relationship between the Access Point and the  
associated entity.

Allowed values:
- **Serves** — the access point provides entry to the entity  
- **Trailhead For** — the access point is a trailhead for a Trail or Trail Segment  
- **Accesses** — the access point provides physical access to the entity  
- **Located Within** — the access point is physically inside the entity  
- **Adjacent To** — the access point is immediately adjacent to the entity  

Rules:
- Must match one of the allowed values.  
- Must reflect authoritative sources.  
- Must not encode identity or governance.

## 3.5 Notes
- Optional free‑text field.  
- Must not include identity‑defining characteristics.  
- Use for clarifications or contextual details.

## 3.6 Source Confidence
Allowed values:
- High  
- Medium  
- Low  

Represents overall confidence in the association.

## 3.7 Verification Status
Allowed values:
- Verified  
- Needs Review  
- Removed  

Represents the current verification state of the association.

## 3.8 Field Confidence Map
- JSON object.  
- Per‑field confidence values.  
- Must follow the structure defined in the v3.2 Normalization Contract.

## 3.9 Field Verification Map
- JSON object.  
- Per‑field verification values.  
- Must follow the structure defined in the v3.2 Normalization Contract.

------------------------------------------------------------
# 4. IDENTITY RULES

An Access Point Association is valid only if:

- The Access Point exists and passes identity rules  
- The associated entity exists and passes identity rules  
- The association is documented in authoritative sources  
- The association does not contradict the Access Point’s primary parent  
- The association does not imply multi‑parent identity  
- The association does not override or duplicate the identity parent relationship  

Invalid associations must not be created.

------------------------------------------------------------
# 5. RELATIONSHIP RULES

## 5.1 Identity vs. Association
- The **Parent** field in the Access Point Schema defines identity.  
- Associations defined here do **not** define identity.  
- An Access Point may have many associations but only one identity parent.

## 5.2 Allowed Associations
An Access Point may be associated with:
- Zero or many Sites  
- Zero or many Trails  
- Zero or many Trail Segments  
- Zero or many Trail Networks  
- Zero or many Site Networks  
- Zero or many Access Points (paired/co‑located only)

## 5.3 Prohibited Associations
- Associations that imply ownership or governance  
- Associations that contradict authoritative sources  
- Associations that duplicate the identity parent relationship  
- Associations that imply multi‑parent identity  

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on the following v3.2 schema modules:

- **Access Point Schema Module v3.2**  
- **Site Schema Module v3.2**  
- **Trail Schema Module v3.2.1**  
- **Trail Segment Schema Module v3.2.2**  
- **Trail Network Schema Module v3.2**  
- **Site Network Schema Module v3.2**  

All other modules (Normalization, TSV Output, Discovery, Resolution,  
Orchestration) must reference this module when handling Access Point associations.

------------------------------------------------------------
# END OF ACCESS POINT ASSOCIATION MODULE v3.2