# RESOLUTION RULES MODULE v5.3  
Authoritative Ontology, Identity, and Classification Rules for All Six Entity Types  
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# 1. PURPOSE

The Resolution Rules Module v5.3 defines the **authoritative ontology and identity framework** for all six entity types in the Natural Areas Project. It establishes:

- What each entity type *is*  
- How identity is recognized  
- How similarity is interpreted  
- How ambiguous cases are resolved  
- How category decisions are made  
- How parent/child relationships are determined  
- How multi‑county identity is handled  
- How conflicts are overridden  

This module is the **single source of truth** for identity and classification logic.  
The Resolution Engine v5.x executes these rules; it does not define them.

------------------------------------------------------------
# 2. SCOPE

This module governs:

- All six entity types:
  - Site  
  - Trail  
  - Trail Segment  
  - Trail Network  
  - Site Network  
  - Access Point  
- All identity-bearing objects discovered in v5.x  
- All baseline (Tier‑0) identity seeds  
- All ambiguous or conflicting cases  
- All parent/child Site relationships  
- All multi‑county identity decisions  
- All category-level decisions for Sites  

This module applies during:

- Resolution (identity detection, merging, conflict detection)  
- Normalization (canonicalization and vocabulary decisions)  
- Entity Upsert (graph integration)  

Discovery must not apply these rules; it collects raw values only.

------------------------------------------------------------
# 3. CROSS‑MODULE ALIGNMENT (v5.x)

This module aligns with:

- **Discovery Protocol v5.x** — raw collection only  
- **Discovery Output Specification v5.x** — authoritative raw field model  
- **Discovery Metadata Specification v5.x** — identity, lineage, provenance, conflict, uncertainty  
- **Resolution Engine v5.x** — executes identity anchors, signatures, and merge logic  
- **Normalization Engine v5.x** — applies vocabulary and canonicalization  
- **Child Site Rules Module v5.x** — governs parent/child Site relationships  
- **TSV Output Specifications v5.x** — formatting only  

All modules reference this one for identity and classification decisions.

------------------------------------------------------------
# 4. CORE IDENTITY PRINCIPLES

### 4.1 Identity First  
Classification is based on **ontological identity**, not amenities, marketing language, or management.

### 4.2 Raw Values Are Authoritative  
Identity is determined from raw discovery values and metadata, not normalized or inferred values.

### 4.3 Governance ≠ Identity  
Ownership, governance, partner agencies, and coordination do not determine entity type or category.

### 4.4 Features Are Not Entities  
Amenities (playgrounds, shelters, overlooks, parking lots) are Features unless explicitly documented as identity-bearing.

### 4.5 Trails Are Not Sites  
A named trail is always a Trail, never a Site.

### 4.6 Access Points Are Never Sites  
Trailheads, parking areas, boat launches, and entrances are Access Points.

### 4.7 Segments Are Not Trails  
Trail Segments are identity-bearing subdivisions of Trails.

### 4.8 Networks Are Not Physical Land Units  
Networks are collections of Trails or Sites, not physical places.

### 4.9 Provenance Always Wins  
When sources conflict, tier precedence and provenance metadata determine authority.

### 4.10 No Inference  
Identity must never be inferred from:
- layout  
- proximity  
- GIS geometry  
- implied relationships  
- marketing language  

### 4.11 Multi‑County Entities Are Single Entities  
No entity may be segmented by county.

------------------------------------------------------------
# 5. IDENTITY ANCHORS (STRICT PREREQUISITES)

Identity anchors define when two records *may* represent the same real‑world entity.  
If anchors fail, similarity scoring is not computed.

Anchors use **raw discovery fields only**.

### 5.1 Site Identity Anchor
- Fuzzy‑normalized `name_raw` match  
- Overlap in `counties_raw`  

### 5.2 Trail Identity Anchor
- Fuzzy‑normalized `name_raw` match  
- Overlap in `counties_raw`  

### 5.3 Trail Segment Identity Anchor
- `parent_trail_id` matches exactly (or raw parent name + county context if unresolved)  
- If both have `segment_name_raw`, fuzzy‑normalized match  

### 5.4 Access Point Identity Anchor
- `identity_parent_entity_id` matches  
- GPS proximity bucket match:  
  - `round(gps_lat_raw, 3)`  
  - `round(gps_lon_raw, 3)`  

### 5.5 Trail Network Identity Anchor
- Fuzzy‑normalized `network_name_raw` match  
- Exact match on `network_type_raw` (case‑folded for matching only)  

### 5.6 Site Network Identity Anchor
- Fuzzy‑normalized `network_name_raw` match  
- Exact match on `network_type_raw`  

------------------------------------------------------------
# 6. IDENTITY SIGNATURES (FUZZY SIMILARITY)

Identity signatures define how similarity is computed (0–100).  
Weights are authoritative and executed by the Resolution Engine v5.x.

### 6.1 Site Identity Signature
- Name similarity — 40  
- Organizational similarity — 35  
- County overlap — 10  
- Location similarity — 10  
- URL overlap — 5  

### 6.2 Trail Identity Signature
- Name similarity — 40  
- Use type match — 15  
- Length similarity — 15  
- Governance match — 10  
- County overlap — 10  
- Surface type match — 5  
- URL overlap — 5  

### 6.3 Trail Segment Identity Signature
- Segment name similarity — 50 (25 if both unnamed)  
- Length similarity — 20  
- Surface type match — 15  
- County overlap — 10  
- Segment type match — 5  

### 6.4 Access Point Identity Signature
- Parent match — 40  
- GPS distance — 30  
- Type match — 20  
- Name similarity — 10  

### 6.5 Trail Network Identity Signature
- Name similarity — 50  
- Network type match — 20  
- Governance match — 15  
- County overlap — 10  
- URL overlap — 5  

### 6.6 Site Network Identity Signature
- Name similarity — 50  
- Network type match — 20  
- Governance match — 15  
- County overlap — 10  
- URL overlap — 5  

------------------------------------------------------------
# 7. ENTITY‑TYPE DEFINITIONS (ONTOLOGICAL)

### 7.1 Site  
A named, bounded, identity-bearing land unit recognized by authoritative sources.

### 7.2 Child Site  
A Site with a `parent_site_id`, governed by the Child Site Rules Module v5.x.

### 7.3 Trail  
A named, linear, identity-bearing route.

### 7.4 Trail Segment  
A named or identity-bearing subdivision of a Trail.

### 7.5 Trail Network  
A documented collection of Trails with a shared identity.

### 7.6 Site Network  
A documented collection of Sites with a shared identity.

------------------------------------------------------------
# 8. CATEGORY RULES FOR SITES

Category decisions apply only to Sites and use vocabulary from the Site Vocabulary Module v5.x.

### 8.1 Categories Must Be Documented  
Category must be explicitly stated or clearly implied by authoritative sources.

### 8.2 Ecology Does Not Determine Category  
Ecological character belongs in Description, not Category.

### 8.3 Category Edge Cases  
- Boardwalk → Feature  
- Natural Play Area → Feature  
- Linear Park → Category: Park (Subtype: Linear Park)  
- Greenway → Category: Greenway Corridor  
- Stormwater Basin (no ecological identity) → Excluded  
- Mitigation Bank → Category: Conservation Area  
- Cemetery with natural area → Category: Cemetery  
- Campground → Category: Camp (if identity-bearing)  
- Water Access Site → Category: Water Access Site  
- NRHP archaeological sites → Category: Archaeological Site or Historic Site  

------------------------------------------------------------
# 9. ACCESS POINT RULES

### 9.1 Access Points Are Visitor-Facing Entrances  
Includes trailheads, parking areas, boat launches, documented entrances.

### 9.2 Access Points Are Never Sites  
Even if large, named, or heavily used.

### 9.3 Access Point Edge Cases  
- Scenic pull-offs → Access Point if documented as entrances  
- Administrative access → Access Point only if documented  
- Trail intersections → Geometry, not entities  

------------------------------------------------------------
# 10. TRAIL & SEGMENT RULES

### 10.1 Trails  
Must be named and identity-bearing.

### 10.2 Trail Segments  
Must be named or identity-bearing subdivisions of Trails.

### 10.3 Connectors and Spurs  
May be Trails or Segments depending on identity.

### 10.4 Loop Trails  
Trails; Segments may have `segment_type = Loop`.

------------------------------------------------------------
# 11. NETWORK RULES

### 11.1 Trail Networks  
Must be explicitly documented as networks.

### 11.2 Site Networks  
Must be explicitly documented as networks.

### 11.3 No Inference  
Networks cannot be inferred from proximity or shared governance.

------------------------------------------------------------
# 12. PARENT/CHILD SITE RULES

### 12.1 Identity Requirements  
Child Sites must be:
- named  
- identity-bearing  
- documented  
- internal to the parent  

### 12.2 Evidence Requirements  
Must be supported by authoritative documentation.

### 12.3 Prohibited Cases  
- Features  
- Temporary labels  
- Habitat types  
- Administrative zones  
- Named buildings (unless identity-bearing)  

### 12.4 Boundary Rules  
Child Site counties must be a subset of the parent unless documented otherwise.

### 12.5 Multi-Level Hierarchies  
Allowed only when explicitly documented.

### 12.6 Circularity  
Prohibited.

------------------------------------------------------------
# 13. MULTI‑COUNTY RULES

### 13.1 Single Entity Rule  
Entities spanning multiple counties must be represented as a single entity.

### 13.2 County Lists  
Must reflect all documented counties.

### 13.3 No Inference  
Counties must not be inferred from GIS or proximity.

------------------------------------------------------------
# 14. CONFLICT OVERRIDE RULES

### 14.1 Tier Precedence  
Tier 1 > Tier 2 > … > Tier 8 > Tier 0.

### 14.2 Category Conflicts  
This module overrides all others.

### 14.3 Entity-Type Conflicts  
This module determines final entity type.

### 14.4 Governance Conflicts  
Normalization Engine resolves unless ambiguous; this module decides ambiguous cases.

### 14.5 Parent/Child Conflicts  
Child Site Rules Module governs; this module resolves edge cases.

### 14.6 Provenance Conflicts  
Resolved using tier precedence, source authority, and discovery path.

------------------------------------------------------------
# 15. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol v5.x  
- Discovery Output Specification v5.x  
- Discovery Metadata Specification v5.x  
- Resolution Engine v5.x  
- Normalization Engine v5.x  
- Child Site Rules Module v5.x  
- Site Schema Module v5.x  
- Vocabulary Modules v5.x  
- Entity Graph Schema v5.x  

------------------------------------------------------------
# END OF RESOLUTION RULES MODULE v5.3