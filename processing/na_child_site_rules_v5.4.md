# NATURAL AREAS PROJECT
# CHILD SITE RULES MODULE v5.4
Authoritative Ontological Rules for Parent–Child Site Relationships

------------------------------------------------------------
# 1. PURPOSE

Child Sites represent named, identity‑bearing internal land units contained within a parent Site.  
A child Site is a **Site** with a populated `parent_site_id`, using the same schema as all Sites.

This module defines:

- Ontological rules  
- Identity rules  
- Evidence requirements  
- Prohibited cases  
- Boundary rules  
- County inheritance rules  
- Multi‑level hierarchy rules  
- Circularity rules  
- Discovery rules  
- Normalization‑phase validation rules  

This module contains **no schema** and **no vocabularies**.  
All fields are defined in the Site Schema Module v5.x.

------------------------------------------------------------
# 2. IDENTITY RULES

A Site may be assigned a Parent Site only if all of the following are true:

- The child has a documented, stable, name‑based identity.  
- The child exists within the spatial, cultural, historical, or administrative scope of the parent.  
- The relationship is explicitly documented in authoritative sources.  
- The child is not a feature, amenity, trail, or administrative zone.  
- The child is not a standalone Site in authoritative sources.  
- The relationship is not inferred from layout or proximity.  

------------------------------------------------------------
# 3. EVIDENCE REQUIREMENTS

Acceptable evidence:

- Official maps  
- Government GIS layers  
- Management plans  
- Signage  
- Published materials  
- Historical documentation  

Unacceptable evidence:

- User‑generated content  
- Informal names  
- Temporary labels  
- Amenities lists  
- Inferred relationships  

------------------------------------------------------------
# 4. PROHIBITED CASES

A Site must not be assigned a Parent Site if:

- The name refers to a feature (playground, shelter, parking lot)  
- The name refers to a temporary condition  
- The name refers to a habitat type  
- The name refers to a trail or segment  
- The name refers to an administrative zone  
- The name is not identity‑bearing  
- The name is undocumented  
- The name is a building or facility unless explicitly identity‑bearing  

------------------------------------------------------------
# 5. BOUNDARY RULES

Child Sites may be spatially, conceptually, or administratively contained within the parent.

A child Site must not:

- Span counties independently of the parent without documentation  
- Contradict the parent’s documented boundaries  
- Represent a larger area than the parent  
- Exist in a different state than the parent  

------------------------------------------------------------
# 6. COUNTY INHERITANCE RULES

County rules apply to **normalized** county sets (`counties`), not raw values.

- A child Site’s counties must be a **subset** of the parent’s counties unless explicitly documented otherwise.  
- Documented exceptions must trigger a Parent–Child Boundary Review.  
- A child Site must not list counties not documented for the parent without explicit evidence.  
- A child Site is not required to inherit all parent counties; it reflects its own documented footprint.

------------------------------------------------------------
# 7. MULTI‑LEVEL HIERARCHY RULES

Multi‑level hierarchies are allowed only when explicitly documented.

Each level must independently satisfy all identity rules.

No inferred intermediate levels.

------------------------------------------------------------
# 8. CIRCULARITY RULES

Circular parentage is prohibited:

- A → B → A  
- A → B → C → A  

Normalization must detect and reject cycles.

------------------------------------------------------------
# 9. DISCOVERY RULES

Discovery must:

- Create independent raw records for identity‑bearing internal units  
- Never assign `parent_site_id`  
- Note suspected parent relationships in `identity_notes_raw`  
- Reject undocumented names  
- Flag ambiguous cases for normalization review  

Discovery must not:

- Infer parent relationships  
- Suppress internal units  
- Assign parent IDs  
- Treat features as child Sites  

------------------------------------------------------------
# 10. NORMALIZATION RULES

Normalization must:

- Validate that the parent exists as a normalized Site  
- Validate that the child meets all identity rules  
- Validate that the relationship is explicitly documented  
- Validate that no circularity is introduced  
- Validate county subset rules  
- Validate state consistency  
- Apply Child Site Rules before upsert  
- Reject invented or inferred relationships  

Normalization must not:

- Infer parent relationships  
- Override Resolution identity decisions  
- Modify lineage metadata  

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v5.x  
- Site Vocabulary Module v5.x  
- Discovery Output Specification v5.x  
- Metadata Specification v5.x  
- Resolution Engine v5.x  
- Normalization Engine v5.x  
- Entity Graph Schema v5.x  
- Processing Orchestration Module v5.x  

------------------------------------------------------------
# END OF CHILD SITE RULES MODULE v5.4