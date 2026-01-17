# NATURAL AREAS PROJECT — TRAIL NETWORK DISCOVERY SUB‑PROCEDURE v1
Authoritative, versioned sub‑procedure for discovering Trail Networks in the statewide
Natural Areas & Trails system.

This module defines:
- The Trail Network discovery workflow
- Required sources
- Identity rules for Trail Network candidates
- Tier‑specific discovery expectations
- Output requirements
- Integration points

This module contains no controlled vocabularies.
All vocabularies are defined in the Trail Network Vocabulary Module v1.

------------------------------------------------------------
# 1. PURPOSE
The Trail Network Discovery Sub‑Procedure v1 provides the authoritative, deterministic
workflow for discovering Trail Networks across all eight discovery tiers.

A Trail Network is:
- An identity‑bearing umbrella entity
- Composed of multiple Trails
- Documented in authoritative sources
- Distinct from its member Trails

This sub‑procedure ensures:
- Consistent identification of Trail Networks
- Prevention of misclassification as Trails or Sites
- Proper metadata capture
- Clean integration with normalization and resolution

This module is authoritative for Trail Network discovery.

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

Each tier must surface Trail Network candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES
Each tier must check the following for Trail Network references:

- Official agency websites
- GIS systems and interactive trail maps
- Regional trail plans
- Greenway or bikeway master plans
- Statewide trail system documents
- National Trail System documentation
- Multi‑trail corridor plans
- Partnership announcements
- Regional mobility or recreation initiatives
- Multi‑trail branding or signage programs

All sources must be logged in Discovery Metadata.

------------------------------------------------------------
# 4. IDENTITY RULES FOR TRAIL NETWORK CANDIDATES
A Trail Network candidate is valid only if:

1. It is explicitly documented as a multi‑trail system.  
2. It has a stable, identity‑bearing name.  
3. It is composed of multiple Trails (minimum of two).  
4. It is distinct from its member Trails.  
5. It is not merely a marketing label or informal grouping.  
6. It is not a Site Network (those belong to the Site Network entity).  
7. It is not a single Trail with multiple Segments.  

If any of these conditions fail, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

## 5.1 Step 1 — Identify Named Multi‑Trail Systems
Search all required sources for:
- Regional trail networks
- Greenway systems
- Bikeway networks
- Multi‑trail corridors
- Statewide trail systems
- National Trail System components
- Multi‑trail recreation or mobility networks

Record each appearance as a raw candidate.

## 5.2 Step 2 — Verify Identity‑Bearing Name
A Trail Network must have:
- A documented, stable name
- Not a temporary project name
- Not a marketing slogan

If the name is ambiguous, flag for review.

## 5.3 Step 3 — Confirm Multi‑Trail Composition
The candidate must include:
- Two or more Trails
- Documented membership
- Explicit geographic or thematic linkage

Do not infer membership.

## 5.4 Step 4 — Determine Network Type
Assign a Network Type from the Trail Network Vocabulary Module v1.
If unclear, leave blank and flag for review.

## 5.5 Step 5 — Extract Required Metadata
For each candidate, extract:
- Network name
- Network type
- Counties traversed
- States included (if multi‑state)
- Managing agency (primary)
- Managing agencies (secondary)
- URLs
- Map links
- Notes
- Source tier
- Source dataset
- Discovery confidence

## 5.6 Step 6 — Log Member Trails (Non‑Authoritative)
Record all Trails referenced as members.
These are non‑authoritative until normalization.

## 5.7 Step 7 — Emit Raw Candidate Record
Produce a Raw Candidate Trail Network Record following the Trail Network Schema Module v1.

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

## 6.1 Federal Tier
Must surface:
- National Scenic Trails
- National Historic Trails
- National Recreation Trail Networks
- Multi‑state trail systems

## 6.2 State Tier
Must surface:
- Statewide trail systems
- State‑designated greenway networks
- Multi‑county trail corridors

## 6.3 Park District Tier
May surface:
- Regional greenway networks
- Multi‑trail recreation systems

## 6.4 County Tier
May surface:
- Countywide bikeway networks
- Countywide greenway systems

## 6.5 Township & Municipal Tiers
May surface:
- Local trail networks
- Multi‑trail corridor initiatives

## 6.6 Land Trust & Conservancy Tier
May surface:
- Multi‑trail conservation corridors
- Regional trail initiatives

## 6.7 Private & Organization‑Based Tier
May surface:
- Privately managed trail systems
- Campus‑scale multi‑trail networks

------------------------------------------------------------
# 7. CONSOLIDATION RULES
During consolidation:
- Merge identical Trail Network names across tiers.
- Preserve all conflicting metadata.
- Do not merge networks with different documented names.
- Align member Trails with normalized Trail records.
- Maintain all source references.

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS
Each Trail Network candidate must output:

- All fields required by the Trail Network Schema Module v1
- Discovery Metadata
- Source references
- Member Trail references (non‑authoritative)
- Confidence and verification placeholders

Output must conform to:
- Discovery Metadata Specification v1.0
- TSV Output Specification v2.0
- Normalization Contract v2.0

------------------------------------------------------------
# 9. INTEGRATION POINTS
This module integrates with:
- Discovery Protocol Module v3.1
- Trail Network Schema Module v1
- Trail Network Vocabulary Module v1
- Trail Discovery Sub‑Procedure v1
- Site Network Discovery Sub‑Procedure v1
- Normalization and Resolution Modules
- TSV Output Specifications
- Audit & Logging Module v1.1

------------------------------------------------------------
# END OF TRAIL NETWORK DISCOVERY SUB‑PROCEDURE v1