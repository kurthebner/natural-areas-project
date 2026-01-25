# NATURAL AREAS PROJECT  
# CHILD SITE RULES MODULE v4.0  
(Authoritative Ontological Rules for Parent–Child Site Relationships)

This module defines the **v4.0 ruleset** governing when a Site may legitimately function as a **child identity‑bearing land unit** within another Site.  
It replaces the v3.2.2 module and modernizes the logic for the v4.0 identity model, normalization pipeline, and entity graph.

A “child Site” is a **Site with a populated `parent_site_id`**, using the same schema as all Sites.

This module defines:

- Ontological rules for child Sites  
- Identity rules  
- Evidence requirements  
- Prohibited cases  
- Boundary rules  
- County inheritance rules (v4.0)  
- Multi‑level hierarchy rules  
- Circularity rules  
- Validation rules  
- Discovery rules  
- Normalization rules  

This module contains **no fields** and defines **no schema**.  
All Site fields are defined in the **Site Schema Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

Child Sites represent **named, identity‑bearing internal land units** contained within a parent Site.  
They include:

- Historic villages  
- Gardens with documented identity  
- Cemetery sections  
- Named internal areas  
- Documented precincts or zones  
- Identity‑bearing cultural or ecological units  

A child Site:

- Has its own identity  
- Is documented in authoritative sources  
- Exists within the spatial, conceptual, or administrative scope of a parent Site  
- Does not rise to the level of a standalone top‑level Site  

This module establishes the **rules** governing when a Site may legitimately have a Parent Site value.

------------------------------------------------------------
# 2. IDENTITY RULES FOR CHILD SITES

A Site may be assigned a Parent Site only if **all** of the following are true:

### 2.1 Identity‑bearing  
The child has a documented, stable, name‑based identity.

### 2.2 Internal to the parent  
The child exists within the spatial, cultural, historical, or administrative scope of the parent Site.

### 2.3 Documented  
The child is explicitly referenced in authoritative sources such as:

- Official maps  
- Government GIS layers  
- Management plans  
- Signage  
- Published materials  
- Institutional documentation  

### 2.4 Not a feature or amenity  
Features (e.g., playgrounds, shelters, parking lots, overlooks) are usually not represented as child Sites.

### 2.5 Not a Trail or Trail Segment  
Trails and Trail Segments are separate entity types.

### 2.6 Not a standalone Site  
If the internal unit is recognized as a full Site in authoritative sources, it is usually represented as a top‑level Site, not a child.

### 2.7 Not inferred  
Parent Site relationships must not be inferred from layout, signage lacking explicit labels, or assumptions.

If any of these conditions fail, the Site must not be assigned a Parent Site.

------------------------------------------------------------
# 3. EVIDENCE REQUIREMENTS

A child Site must be supported by **explicit** documentation.

### Acceptable evidence:
- Official park or preserve maps  
- Government GIS layers  
- Published brochures or guides  
- Signage naming the internal area  
- Management or stewardship plans  
- Historical documentation  

### Unacceptable evidence:
- User‑generated content  
- Informal names  
- Temporary labels  
- Amenities lists  
- Marketing language  
- Inferred relationships  

------------------------------------------------------------
# 4. PROHIBITED CASES

A Site must **not** be assigned a Parent Site if:

- The internal name refers to a **feature** (e.g., “Playground,” “Shelter 2”), unless that particular feature is named, and is identity-bearing enough to be a full site.  
- The internal name refers to a **temporary condition**  
- The internal name refers to a **habitat type**  
- The internal name refers to a **trail or trail segment**  
- The internal name refers to an **administrative zone**  
- The internal name is **not identity‑bearing**  
- The internal name is **not documented**  
- The internal name is a **named building** or **facility** that should be a Feature. However, some named buildings or facilities may indeed be child sites.  
- The internal name is a **named garden or grove** that is not otherwise a part of a full Site  

------------------------------------------------------------
# 5. BOUNDARY RULES

Child Sites may be:

- Spatially contained within the parent  
- Conceptually contained (e.g., a historic village within a larger park)  
- Administratively contained  

Spatial containment is preferred but **not required** if authoritative sources define the relationship.

A child Site must not:

- Span counties independently of the parent without documentation  
- Contradict the parent’s documented boundaries  
- Represent a larger area than the parent  
- Exist in a different **state** than the parent  

------------------------------------------------------------
# 6. COUNTY INHERITANCE RULES (v4.0)

The following rules govern the relationship between parent and child `county_list` values.

### 6.1 Default Rule — Subset Inheritance  
A child Site’s `county_list` must be a **subset** of the parent Site’s `county_list`, unless authoritative sources explicitly document otherwise.  
Identical sets are valid.

### 6.2 Permitted Variation — Documented Exceptions  
If authoritative sources explicitly document that a child Site occupies a county not listed for the parent, the child Site’s `county_list` must reflect that documentation.  
This must trigger a **Parent–Child Boundary Review**.

### 6.3 Prohibited Case — Undocumented Expansion  
A child Site must not list counties that the parent does not list **unless** supported by authoritative documentation.

### 6.4 No Requirement for Full Inheritance  
A child Site must **not** be required to list all counties of the parent.  
The child Site’s `county_list` must reflect **its actual documented footprint**, not the parent’s.

------------------------------------------------------------
# 7. MULTI‑LEVEL HIERARCHY RULES

Multi‑level hierarchies are allowed **only when explicitly documented**.

Examples:

- Site → Child Site → Grandchild Site  
- “Park” → “Historic Village” → “Blacksmith District”  

Rules:

- Each level must independently satisfy all identity rules  
- No invented intermediate levels  
- No inferred hierarchies  

------------------------------------------------------------
# 8. CIRCULARITY RULES

Circular parentage is prohibited.

Invalid:

- A → B → A  
- A → B → C → A  

The normalization pipeline must detect and reject cycles.

------------------------------------------------------------
# 9. VALIDATION RULES

Before assigning a Parent Site:

1. Validate that the parent exists as a normalized Site.  
2. Validate that the child meets all identity rules.  
3. Validate that the relationship is explicitly documented.  
4. Validate that the child is not a feature, trail, or amenity.  
5. Validate that no circularity is introduced.  
6. Validate that the child does not contradict parent boundaries.  
7. Validate that the child’s `county_list` is a subset of the parent’s unless explicitly documented otherwise.  
8. Validate that State matches the parent unless explicitly documented otherwise.  

------------------------------------------------------------
# 10. DISCOVERY RULES

During discovery:

- Internal names must be evaluated against this module.  
- Only identity‑bearing internal units may become child Sites.  
- Features must be routed to the Features field.  
- Ambiguous names must be flagged for review.  
- Undocumented names must be rejected.  
- Parent Site relationships must never be inferred.  

Discovery must never infer child Sites.

------------------------------------------------------------
# 11. NORMALIZATION RULES

Normalization must:

- Preserve the Parent Site relationship exactly as documented  
- Reject invented or inferred relationships  
- Ensure that child Sites use the same schema as all Sites  
- Ensure that `county_list` follows the v4.0 subset rule  
- Ensure that State matches the parent unless explicitly documented otherwise  
- Ensure that identity anchors and identity signatures remain valid  

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- **Site Schema Module v4.0**  
- **Site Vocabulary Module v4.0**  
- **Discovery Output Specification v4.0**  
- **Resolution Engine v4.0**  
- **Normalization Engine v4.0**  
- **Entity Graph Schema v4.0**  

All other modules must reference this ruleset when interpreting the Parent Site field.

------------------------------------------------------------
# END OF CHILD SITE RULES MODULE v4.0