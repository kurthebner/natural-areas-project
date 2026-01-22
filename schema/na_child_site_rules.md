# NATURAL AREAS PROJECT — CHILD SITE RULES MODULE v3.2.2
Authoritative, versioned ruleset defining when a Site may legitimately function
as a **child identity‑bearing land unit** within another Site.

This module replaces the former Sub‑Site Schema Module v1.  
Sub‑Sites are no longer a separate entity type.  
A “child Site” is now simply a **Site with a populated Parent Site field**.

This module defines:
- Ontological rules for child Sites  
- Evidence requirements  
- Prohibited cases  
- Boundary rules  
- Validation rules  
- Circularity rules  
- Multi‑level hierarchy rules  
- Discovery and normalization rules  

This module contains **no fields** and defines **no schema**.  
All Site fields are defined in the **Site Schema Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

Child Sites are named, identity‑bearing internal land units contained within a
parent Site. They represent distinct, meaningful places such as:

- Gardens  
- Cemetery sections  
- Historic villages  
- Disc golf courses  
- Named internal areas  
- Documented precincts or zones  
- Identity‑bearing cultural or ecological units  

A child Site:
- Has its own identity  
- Is documented in authoritative sources  
- Exists within the boundaries or conceptual scope of a parent Site  
- Does not rise to the level of a standalone top‑level Site  

This module establishes the **rules** governing when a Site may legitimately have
a Parent Site value.

------------------------------------------------------------
# 2. IDENTITY RULES FOR CHILD SITES

A Site may be assigned a Parent Site only if **all** of the following are true:

1. **Identity‑bearing**  
   The child has a documented, stable, name‑based identity.

2. **Internal to the parent**  
   The child exists within the spatial, cultural, historical, or administrative
   scope of the parent Site.

3. **Documented**  
   The child is explicitly referenced in authoritative sources such as:  
   - Official maps  
   - Management plans  
   - Government GIS layers  
   - Signage  
   - Published materials  
   - Institutional documentation  

4. **Not a feature or amenity**  
   Features (e.g., playgrounds, shelters, parking lots, overlooks) must not be
   represented as child Sites.

5. **Not a Trail or Trail Segment**  
   Trails and Trail Segments are separate entity types.

6. **Not a standalone Site**  
   If the internal unit is recognized as a full Site in authoritative sources,
   it must be represented as a top‑level Site, not a child.

7. **Not inferred**  
   Parent Site relationships must not be inferred from layout, signage, maps
   lacking explicit labels, or assumptions.

If any of these conditions fail, the Site must not be assigned a Parent Site.

------------------------------------------------------------
# 3. EVIDENCE REQUIREMENTS

A child Site must be supported by **explicit** documentation.  
Acceptable evidence includes:

- Official park or preserve maps  
- Government GIS layers  
- Published brochures or guides  
- Signage naming the internal area  
- Management or stewardship plans  
- Historical documentation  

Unacceptable evidence:

- User‑generated content  
- Informal names  
- Temporary labels  
- Amenities lists  
- Marketing language  
- Inferred relationships  

------------------------------------------------------------
# 4. PROHIBITED CASES

A Site must **not** be assigned a Parent Site if:

- The internal name refers to a **feature** (e.g., “Playground,” “Shelter 2”)  
- The internal name refers to a **temporary condition**  
- The internal name refers to a **habitat type**  
- The internal name refers to a **trail or trail segment**  
- The internal name refers to an **administrative zone**  
- The internal name is **not identity‑bearing**  
- The internal name is **not documented**  
- The internal name is a **named building** or **named facility** that should be
  represented as a Feature, not a Site  
- The internal name is a **named garden or grove** that is identity‑bearing
  enough to be a full Site  

------------------------------------------------------------
# 5. BOUNDARY RULES

Child Sites may be:

- Spatially contained within the parent  
- Conceptually contained (e.g., a historic village within a larger park)  
- Administratively contained  

Spatial containment is preferred but **not required** if authoritative sources
define the relationship.

A child Site must not:

- Span counties independently of the parent  
- Contradict the parent’s documented boundaries  
- Represent a larger area than the parent  
- Exist in a different **state** than the parent  

County and state values must match the parent unless authoritative sources
explicitly document otherwise.

------------------------------------------------------------
# 6. MULTI‑LEVEL HIERARCHY RULES

Multi‑level hierarchies are allowed **only when explicitly documented**.

Examples:

- Site → Child Site → Grandchild Site  
- “Park” → “Historic Village” → “Blacksmith District”

Rules:

- Each level must independently satisfy all identity rules  
- No invented intermediate levels  
- No inferred hierarchies  

------------------------------------------------------------
# 7. CIRCULARITY RULES

Circular parentage is prohibited.

Invalid:

- A → B → A  
- A → B → C → A  

The normalization pipeline must detect and reject cycles.

------------------------------------------------------------
# 8. VALIDATION RULES

Before assigning a Parent Site:

1. Validate that the parent exists as a normalized Site.  
2. Validate that the child meets all identity rules.  
3. Validate that the relationship is explicitly documented.  
4. Validate that the child is not a feature, trail, or amenity.  
5. Validate that no circularity is introduced.  
6. Validate that the child does not contradict parent boundaries.  
7. Validate that County and State align with the parent unless explicitly
   documented otherwise.  
8. Validate that the Derived Label will compute correctly under v3.2.2 rules.  

------------------------------------------------------------
# 9. DISCOVERY RULES

During discovery:

- Internal names must be evaluated against this module.  
- Only identity‑bearing internal units may become child Sites.  
- Features must be routed to the Features field.  
- Ambiguous names must be flagged for review.  
- Undocumented names must be rejected.  
- Parent Site relationships must never be inferred.  

Discovery must never infer child Sites.

------------------------------------------------------------
# 10. NORMALIZATION RULES

Normalization must:

- Preserve the Parent Site relationship exactly as documented  
- Reject invented or inferred relationships  
- Ensure that child Sites use the same **26 fields** as all Sites  
- Ensure that County reflects the parent’s counties unless explicitly
  documented otherwise  
- Ensure that State matches the parent unless explicitly documented otherwise  
- Ensure that Derived Label is computed identically for child and parent Sites
  using v3.2.2 rules  

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- **Site Schema Module v3.2.2**  
- **Site Vocabulary Module v3.2.2**  
- **Normalization Contract v3.2.2**  
- **Discovery Protocol Module v3.2.2**  
- **Resolution Module v3.2.2**  

All other modules must reference this ruleset when interpreting the Parent Site field.

------------------------------------------------------------
# END OF CHILD SITE RULES MODULE v3.2.2