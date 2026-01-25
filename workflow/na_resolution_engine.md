# NATURAL AREAS PROJECT  
# RESOLUTION ENGINE v4.0  
(Procedural Identity‑Resolution Engine for All Six Entity Types)

The Resolution Engine v4.0 is the authoritative, deterministic processor that applies  
the **Resolution Module v4.0** rules to transform raw discovery outputs and baseline  
seeds into **Resolved Entity Objects** for all six entity types:

- Site  
- Trail  
- Trail Segment  
- Trail Network  
- Site Network  
- Access Point  

This engine performs identity merging, conflict detection, conflict resolution,  
entity‑type determination, parent/child alignment, network alignment, and  
multi‑county unification.

This module contains no controlled vocabularies.  
All vocabularies are defined in the respective Vocabulary Modules v4.0.

------------------------------------------------------------
# 1. PURPOSE

The Resolution Engine v4.0:

- Applies the Resolution Module v4.0 rules mechanically  
- Produces conflict‑aware, provenance‑preserving **Resolved Entity Objects**  
- Merges multi‑tier representations into single identities  
- Determines final entity type  
- Aligns parent/child relationships  
- Aligns network membership  
- Unifies multi‑county lists  
- Preserves all raw discovery values  
- Surfaces unresolved conflicts  
- Prepares entities for Normalization Engine v4.0  

This engine ensures:

- Deterministic identity resolution  
- Zero improvisation  
- Zero silent assumptions  
- Full provenance preservation  
- Full compatibility with Schema v4.0 and Normalization v4.0  

------------------------------------------------------------
# 2. INPUTS

The Resolution Engine consumes:

## 2.1 Raw Discovery Records v4.0  
For all six entity types, including:

- name_raw  
- category_raw, subtype_raw, designation_raw  
- ownership_raw, management_raw, coordination_raw  
- gps_raw, geometry_raw  
- counties_raw  
- parent_url chain  
- network claims  
- access_level_raw  
- description_raw  
- notes_raw  
- discovery_tier  
- discovered_in_tiers  
- discovery_metadata  

## 2.2 County Baseline v4.0  
- Baseline identity seeds  
- Baseline provenance  
- Baseline naming  

## 2.3 Schema Modules v4.0  
- Field definitions  
- Identity‑anchor definitions  
- Entity‑type definitions  

## 2.4 Vocabulary Modules v4.0  
Used only for validation, never inference.

## 2.5 Resolution Module v4.0  
The authoritative ruleset.

## 2.6 Child Site Rules Module v4.0  
For determining parent/child relationships.

------------------------------------------------------------
# 3. OUTPUTS

The Resolution Engine produces:

- **Resolved Entity Objects v4.0** (six entity types)  
- Conflict metadata  
- Provenance metadata  
- Parent/child alignment  
- Network alignment  
- Multi‑county lists  
- Entity‑type determination  
- Identity anchors  
- Resolution warnings and errors  

These outputs feed directly into the **Normalization Engine v4.0**.

------------------------------------------------------------
# 4. HIGH‑LEVEL WORKFLOW

1. Load raw discovery layer  
2. Group records by candidate identity  
3. Merge multi‑tier representations  
4. Detect conflicts  
5. Apply Resolution Module v4.0 rules  
6. Determine final entity type  
7. Assign identity anchors  
8. Align parent/child relationships  
9. Align network membership  
10. Unify multi‑county lists  
11. Produce Resolved Entity Objects  
12. Emit conflict and provenance metadata  

If any critical step fails → halt and surface error.

------------------------------------------------------------
# 5. PROCEDURAL STEPS (DETAILED)

## 5.1 Grouping (Candidate Identity Clustering)

Group raw records using:

- name_raw  
- parent_url lineage  
- discovery_tier  
- baseline identity  
- geometry proximity (if documented)  
- network membership claims  
- authoritative IDs (if present)  

No inference is permitted.  
Grouping must be deterministic.

---

## 5.2 Multi‑Tier Merge

For each cluster:

- Merge all records from all tiers  
- Preserve all raw values  
- Preserve all conflicts  
- Preserve all provenance  
- Record all discovered_in_tiers  

Tier precedence determines which values are authoritative when conflicts arise.

---

## 5.3 Conflict Detection

Detect conflicts in:

- name  
- category, subtype, designation  
- ownership, management, coordination  
- county list  
- parent/child claims  
- network membership  
- entity‑type claims  
- geometry  
- access level  
- description and notes  

All conflicts must be logged.

---

## 5.4 Entity‑Type Determination

Apply the **Entity‑Type Resolution Rules** from the Resolution Module v4.0:

- Site  
- Child Site  
- Trail  
- Trail Segment  
- Trail Network  
- Site Network  
- Access Point  

If ambiguous → choose the more general identity unless a formal designation dictates otherwise.

---

## 5.5 Identity Anchor Assignment

Assign identity anchors per Schema v4.0:

- Site → name  
- Trail → trail_name  
- Trail Segment → parent_trail + segment_name  
- Trail Network → network_name  
- Site Network → network_name  
- Access Point → access_point_name or location anchor  

Identity anchors must be stable and deterministic.

---

## 5.6 Parent/Child Alignment (Sites Only)

Apply **Child Site Rules Module v4.0**:

- Determine if internal units qualify as child Sites  
- Assign parent_site_id  
- Ensure child Sites do not override parent identity  
- Resolve ambiguous parent claims  
- Surface conflicts  

---

## 5.7 Network Membership Alignment

For Trails and Sites:

- Validate network membership claims  
- Remove inferred memberships  
- Preserve documented memberships only  
- Align with Trail Network and Site Network definitions  

---

## 5.8 Multi‑County Unification

For all six entity types:

- Combine all county claims  
- Remove duplicates  
- Alphabetize  
- Validate against authoritative county list  
- Preserve provenance  
- Surface unverifiable county claims  

No entity may be split across counties.

---

## 5.9 Provenance Preservation

For each resolved entity:

- Record all raw values  
- Record all conflicting values  
- Record tier precedence decisions  
- Record source URLs  
- Record discovery path  
- Record extraction method  
- Record baseline influence  

---

## 5.10 Final Resolved Entity Construction

Construct a **Resolved Entity Object v4.0** with:

- resolved identity key  
- resolved entity_type  
- resolved name  
- resolved parent_site (if any)  
- resolved county list  
- resolved category/subtype/designation (if applicable)  
- resolved ownership/management/coordination  
- resolved network membership  
- resolved geometry (if authoritative)  
- resolved access level (Access Points)  
- conflict metadata  
- provenance metadata  

Emit one object per identity.

------------------------------------------------------------
# 6. ERROR CONDITIONS

Resolution must halt if:

- Entity type cannot be determined  
- Parent/child relationship is contradictory  
- Network membership is contradictory  
- County list cannot be validated  
- Identity anchor cannot be assigned  
- Tier precedence cannot be applied  
- Required raw values are missing  

All errors must be logged.

------------------------------------------------------------
# 7. INTEGRATION POINTS

## 7.1 Normalization Engine v4.0  
Receives Resolved Entity Objects.

## 7.2 Audit & Logging Module v4.0  
Receives:

- conflict logs  
- provenance logs  
- resolution decisions  
- unresolved ambiguities  

## 7.3 Processing Orchestration Module v4.0  
Invokes this engine during Stage 3.

------------------------------------------------------------
# 8. MODULE DEPENDENCIES

This engine depends on:

- Resolution Module v4.0  
- All six Schema Modules v4.0  
- All six Vocabulary Modules v4.0  
- Child Site Rules Module v4.0  
- Discovery Protocol v4.0  
- Discovery Metadata Specification v4.0  
- County Baseline Module v4.0  
- Audit & Logging Module v4.0  

------------------------------------------------------------
# END OF RESOLUTION ENGINE v4.0