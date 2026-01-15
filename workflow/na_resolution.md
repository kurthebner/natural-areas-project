# NATURAL AREAS PROJECT — RESOLUTION MODULE v1
A deterministic decision framework for resolving ambiguous, borderline, or multi‑identity cases during discovery and normalization of both **Sites** and **Access Points**.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v1 and Access Point Vocabulary Module v1.

This module overrides ambiguity in all other modules.

---

# 1. PURPOSE
The Resolution Module defines how Copilot resolves all ambiguous or borderline cases that arise during:

- Discovery (what counts as a Site or Access Point)  
- Classification (Category, Subtype, Designation, Trail Role, Segment Type, Access Type)  
- Normalization (all Site and Access Point fields)  

This module ensures:

- Zero improvisation  
- Zero silent assumptions  
- Deterministic, repeatable decisions  
- Full alignment with the Schema Modules, Vocabulary Modules, Discovery Protocol, and Normalization Contracts  

---

# 2. GENERAL PRINCIPLES

## 2.1 Identity First
Classification is based on the **ontological identity** of the land unit, not amenities, activities, or marketing language.

## 2.2 Governance ≠ Category
Ownership or management never determines Category.

## 2.3 Ecology Belongs in Description
Ecological character never determines Category or Subtype.  
Ecology informs **Description**, not identity.

## 2.4 Features Are Not Categories
Amenities never determine Category or Subtype.  
If something is an amenity, it belongs in **Features**, not as a Site.

## 2.5 When in Doubt, Choose the More General Category
If a Site could be two things, choose the broader Category unless a formal designation dictates otherwise.

## 2.6 Never Infer Governance
Ownership, Management, and Designation must never be inferred.  
Ambiguity triggers a flag, not a guess.

## 2.7 Multi‑Site Complexes May Be Split
Large parks, forests, or preserves may contain internal identity‑bearing units.  
These become separate Sites when they meet the Internal Parcel Rule.

## 2.8 Access Points Are Never Sites
Trailheads, boat ramps, parking areas, and entrances are **Access Points**, not Sites.

---

# 3. CATEGORY‑LEVEL EDGE CASES (SITES)

These rules determine how ambiguous land units are classified.

## 3.1 Boardwalk
- Not a Site  
- Treated as a **Feature**  

## 3.2 Natural Play Area
- Not a Site  
- Treated as a **Feature**

## 3.3 Paved Path / Multi‑Use Path
- Site only if named and identity‑bearing  
- Category: Trail  
- Subtype determined by identity  
- Trail Role determined by context (Trail vs. Segment)

## 3.4 Linear Park
- Category: Park  
- Subtype: Linear Park  

## 3.5 Greenway
- Category: Greenway Corridor  

## 3.6 Stormwater Green with Ecological Identity
- Category: Natural Area or Conservation Area depending on identity  
- Include even if access is limited  

## 3.7 Stormwater Basin with No Ecological Identity
- Excluded from dataset  

## 3.8 Reservoir Property
- Category: Water Site or Reservoir (depending on identity)  
- Include even if access is limited  

## 3.9 Cemetery with Natural Area
- Category: Cemetery  
- Subtype: Cemetery subtype  
- Ecological identity goes in Description  
- Exclude if no natural features  

## 3.10 Mitigation Bank
- Category: Conservation Area  
- Subtype: Mitigation Bank  
- Include even if access is restricted  

## 3.11 Unnamed Natural Area in GIS
- Category: Natural Area  
- Subtype: As appropriate  
- Name: Use best available GIS label; surface for review  

## 3.12 Internal Natural Areas within Parks
- Category: Natural Area  
- Subtype: As appropriate  
- Parent Site handled via Parent Site field  

## 3.13 Campgrounds
- Category: Camp  
- Include only if natural‑area identity is present  

## 3.14 Water Access Sites
- Category: Water Access Site  
- Trail Role assigned only if part of a trail system  

---

# 4. GOVERNANCE‑LEVEL EDGE CASES

## 4.1 Ownership Unknown
- Leave blank  
- Flag for review  

## 4.2 Management Unknown
- Leave blank  
- Do not assume “same as ownership”  

## 4.3 Joint Management
- Semicolon‑delimited  
- Order does not imply hierarchy  

## 4.4 Private Natural Areas
- Include if designated or publicly referenced  
- Category determined by identity  

## 4.5 Tribal Lands
- Category determined by identity  
- Ownership: Tribal Nation  
- Management: Tribal Nation unless otherwise stated  

---

# 5. TRAIL‑RELATED EDGE CASES (SITES)

## 5.1 Trailhead vs. Trail Access Point
- Trailhead = primary, named, formal access  
- Access Point = secondary or informal access  
- Both are **Access Points**, not Sites  

## 5.2 Bikeway Access Point
- Only when explicitly tied to a bikeway system  

## 5.3 Connector Trail vs. Spur
- Connector Trail = links two trail systems or segments  
- Spur = dead‑end or single‑direction access path  

## 5.4 Loop Trails
- Category: Trail  
- Trail Segment Type: Loop  

## 5.5 Internal Trail Segments
- Category: Trail  
- Subtype: Trail Segment (Internal)  
- Trail Role: Trail Segment  

## 5.6 Greenway Trails
- Category: Trail Corridor  
- Subtype: Greenway Trail  

---

# 6. ECOLOGICAL EDGE CASES (SITES)

## 6.1 Buffer Zones
- Category: Buffer Zone  
- Include only if named or mapped  

## 6.2 Restoration Areas
- Category: Conservation Area  
- Subtype: Restoration Area  

## 6.3 Successional Habitat
- Category: Natural Area  
- Subtype: Successional Habitat  

## 6.4 Floodplain Forest
- Category: Natural Area  
- Subtype: Floodplain Forest  

## 6.5 Wetland Complexes
- Category: Natural Area  
- Subtype: Appropriate wetland subtype  

---

# 7. ACCESS POINT EDGE CASES

## 7.1 Parking Lots
- Always Access Points  
- Never Sites  

## 7.2 Boat Ramps
- Always Access Points  
- Never Sites  

## 7.3 Scenic Pull‑Offs
- Access Points only if they serve as entry locations  
- Otherwise Features  

## 7.4 Internal Amenities
- Shelters, overlooks, playgrounds, restrooms → Features  
- Never Sites  
- Never Access Points unless they function as entrances  

## 7.5 Trail Intersections
- Never Access Points  
- Never Sites  

## 7.6 Administrative Access
- Access Point only if explicitly documented  

---

# 8. INTERNAL PARCEL RULE (SITES)

A Site may only be created for a **named, bounded, physical unit** that carries its own identity.

## Requirements for a Site
A Site must be:

- **Named**  
- **Physical**  
- **Bounded**  
- **Identity‑bearing**  
- **Stable**  

If an object does not meet these criteria, it is a **Feature**, not a Site.

## Valid Internal Parcels
Examples include:

- Named ranger districts  
- Named recreation areas  
- Named natural areas within larger parks  
- Named wilderness or ORV areas  

## Not Valid as Sites
- Individual trailheads  
- Individual overlooks  
- Individual shelters  
- Individual ponds  
- Individual parking lots  
- Individual boat ramps  
- Individual boardwalks  
- Individual playgrounds  
- Unnamed trail segments  

## Hierarchy Rule
- Multi‑site complexes may have a top‑level Site  
- Internal parcels become Sites only if identity‑bearing  
- Relationships are handled via the Parent Site field  

---

# 9. CONFLICT RESOLUTION OVERRIDES

## 9.1 Category Conflicts
Resolution Module overrides Discovery and Normalization.

## 9.2 Governance Conflicts
Normalization rules apply unless ambiguous → then Resolution decides.

## 9.3 Trail Role Conflicts
Resolution Module overrides all other modules.

## 9.4 Ecological Identity Conflicts
Ecology informs Description only; Category never changes based on ecology; some ecological features, when not site-defining, are acceptable in Features.

---

# 10. MODULE DEPENDENCIES
This module depends on:

- **Site Schema Module v1**  
- **Access Point Schema Module v1**  
- **Site Vocabulary Module v1**  
- **Access Point Vocabulary Module v1**  
- **Discovery Protocol v1**  
- **Site Normalization Contract v1**  
- **Access Point Normalization Contract v1**  
- **Processing Orchestration Module v1**  
- **Audit & Logging Module**

---

# END OF RESOLUTION MODULE v1