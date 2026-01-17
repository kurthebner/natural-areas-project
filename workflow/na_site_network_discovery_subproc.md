# NATURAL AREAS PROJECT — SITE NETWORK DISCOVERY SUB‑PROCEDURE v1
Authoritative, versioned sub‑procedure for discovering Site Networks in the statewide
Natural Areas & Trails system.

This module defines:
- The Site Network discovery workflow
- Required sources
- Identity rules for Site Network candidates
- Tier‑specific discovery expectations
- Output requirements
- Integration points

This module contains no controlled vocabularies.
All vocabularies are defined in the Site Network Vocabulary Module v1.

------------------------------------------------------------
# 1. PURPOSE
The Site Network Discovery Sub‑Procedure v1 provides the authoritative, deterministic
workflow for discovering Site Networks across all eight discovery tiers.

A Site Network is:
- An identity‑bearing umbrella entity
- Composed of multiple Sites
- Documented in authoritative sources
- Distinct from its member Sites

This sub‑procedure ensures:
- Consistent identification of Site Networks
- Prevention of misclassification as Sites or Sub‑Sites
- Proper metadata capture
- Clean integration with normalization and resolution

This module is authoritative for Site Network discovery.

------------------------------------------------------------
# 2. SCOPE
This sub‑procedure applies to all eight discovery tiers:

1. Federal  
2. State  
3. Park District  
4. County  
5. Township  
6. Municipal  
7. Land Trust & Conservancy  
8. Private & Organization‑Based  

Each tier must surface Site Network candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES
Each tier must check the following for Site Network references:

- Official agency websites
- GIS systems and interactive maps
- Planning documents (master plans, corridor plans, heritage plans)
- Stewardship or management plans
- Federal and state designation documents
- National Heritage Area documentation
- Scenic River Corridor documentation
- Historic District documentation
- Watershed or ecological corridor plans
- Partnership announcements
- Multi‑site program pages
- Regional conservation or heritage initiatives

All sources must be logged in Discovery Metadata.

------------------------------------------------------------
# 4. IDENTITY RULES FOR SITE NETWORK CANDIDATES
A Site Network candidate is valid only if:

1. It is explicitly documented as a multi‑site system.  
2. It has a stable, identity‑bearing name.  
3. It is composed of multiple Sites (minimum of two).  
4. It is distinct from its member Sites.  
5. It is not merely a marketing label or informal grouping.  
6. It is not a Trail Network (those belong to the Trail Network entity).  
7. It is not a single Site with multiple Sub‑Sites.  

If any of these conditions fail, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

## 5.1 Step 1 — Identify Named Multi‑Site Systems
Search all required sources for:
- Named corridors
- Heritage areas
- Historic districts
- Scenic river systems
- Watershed networks
- Cultural landscape networks
- Multi‑site conservation programs
- Multi‑site recreation networks

Record each appearance as a raw candidate.

## 5.2 Step 2 — Verify Identity‑Bearing Name
A Site Network must have:
- A documented, stable name
- Not a temporary project name
- Not a marketing slogan

If the name is ambiguous, flag for review.

## 5.3 Step 3 — Confirm Multi‑Site Composition
The candidate must include:
- Two or more Sites
- Documented membership
- Explicit geographic or thematic linkage

Do not infer membership.

## 5.4 Step 4 — Determine Network Type
Assign a Network Type from the Site Network Vocabulary Module v1.
If unclear, leave blank and flag for review.

## 5.5 Step 5 — Extract Required Metadata
For each candidate, extract:
- Network name
- Network type
- Counties included
- States included (if multi‑state)
- Managing agency (primary)
- Managing agencies (secondary)
- URLs
- Map links
- Notes
- Source tier
- Source dataset
- Discovery confidence

## 5.6 Step 6 — Log Member Sites (Non‑Authoritative)
Record all Sites referenced as members.
These are non‑authoritative until normalization.

## 5.7 Step 7 — Emit Raw Candidate Record
Produce a Raw Candidate Site Network Record following the Site Network Schema Module v1.

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

## 6.1 Federal Tier
Must surface:
- National Heritage Areas
- National Scenic River Corridors
- Multi‑state heritage or conservation networks

## 6.2 State Tier
Must surface:
- State Scenic River Corridors
- Statewide heritage or conservation networks
- Multi‑county ecological corridors

## 6.3 Park District Tier
May surface:
- Regional greenway networks
- Multi‑park heritage or conservation initiatives

## 6.4 County Tier
May surface:
- Countywide historic districts
- Countywide conservation corridors
- Watershed‑scale networks

## 6.5 Township & Municipal Tiers
May surface:
- Local historic districts
- Local cultural landscape networks

## 6.6 Land Trust & Conservancy Tier
May surface:
- Multi‑site conservation networks
- Ecological corridors
- Watershed networks

## 6.7 Private & Organization‑Based Tier
May surface:
- Privately managed heritage or conservation networks
- Multi‑site campus‑scale networks

------------------------------------------------------------
# 7. CONSOLIDATION RULES
During consolidation:
- Merge identical Site Network names across tiers.
- Preserve all conflicting metadata.
- Do not merge networks with different documented names.
- Align member Sites with normalized Site records.
- Maintain all source references.

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS
Each Site Network candidate must output:

- All fields required by the Site Network Schema Module v1
- Discovery Metadata
- Source references
- Member Site references (non‑authoritative)
- Confidence and verification placeholders

Output must conform to:
- Discovery Metadata Specification v1.0
- TSV Output Specification v2.0
- Normalization Contract v2.0

------------------------------------------------------------
# 9. INTEGRATION POINTS
This module integrates with:
- Discovery Protocol Module v3.1
- Site Network Schema Module v1
- Site Network Vocabulary Module v1
- Site Discovery Sub‑Procedure v3.1
- Trail Network Discovery Sub‑Procedure v1
- Normalization and Resolution Modules
- TSV Output Specifications
- Audit & Logging Module v1.1

------------------------------------------------------------
# END OF SITE NETWORK DISCOVERY SUB‑PROCEDURE v1