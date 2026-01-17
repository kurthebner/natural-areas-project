# NATURAL AREAS PROJECT — TRAIL DISCOVERY SUB‑PROCEDURE v1
Authoritative, versioned sub‑procedure for discovering Trails in the statewide
Natural Areas & Trails system.

This module defines:
- The Trail discovery workflow
- Required sources
- Identity rules for Trail candidates
- Tier‑specific discovery expectations
- Output requirements
- Integration points

This module contains no controlled vocabularies.
All vocabularies are defined in the Trail Vocabulary Module v1.

------------------------------------------------------------
# 1. PURPOSE
The Trail Discovery Sub‑Procedure v1 provides the authoritative, deterministic
workflow for discovering Trails across all eight discovery tiers.

A Trail is:
- An identity‑bearing linear corridor
- Documented in authoritative sources
- Distinct from its Trail Segments
- Distinct from Trail Networks
- Distinct from Sites and Sub‑Sites

This sub‑procedure ensures:
- Consistent identification of Trails
- Prevention of misclassification as Sites or Trail Networks
- Proper metadata capture
- Clean integration with Trail Segment and Trail Network discovery

This module is authoritative for Trail discovery.

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

Each tier must surface Trail candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES
Each tier must check the following for Trail references:

- Official agency websites
- GIS systems and interactive trail maps
- Trail brochures and downloadable maps
- Park district trail pages
- Statewide trail inventories
- Federal trail inventories
- Regional greenway or bikeway plans
- Trail signage programs
- Trailhead kiosks (digitally documented)
- Planning documents (master plans, corridor plans)
- Multi‑trail system documents (for individual trail extraction)

All sources must be logged in Discovery Metadata.

------------------------------------------------------------
# 4. IDENTITY RULES FOR TRAIL CANDIDATES
A Trail candidate is valid only if:

1. It is explicitly documented as a named linear corridor.  
2. It has a stable, identity‑bearing name.  
3. It is not merely a segment of a larger Trail.  
4. It is not a Trail Network (umbrella over multiple Trails).  
5. It is not a Site or Sub‑Site.  
6. It is not an Access Point or amenity.  
7. It is not a temporary or unnamed connector.  

If any of these conditions fail, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

## 5.1 Step 1 — Identify Named Trails
Search all required sources for:
- Named trails
- Named loops
- Named linear corridors
- Named bikeways or greenways
- Named water trails
- Named equestrian trails
- Named multi‑use trails

Record each appearance as a raw candidate.

## 5.2 Step 2 — Verify Identity‑Bearing Name
A Trail must have:
- A documented, stable name
- Not a temporary project name
- Not a marketing slogan
- Not a generic label (e.g., “Main Trail,” “Loop Trail”) unless officially used

If ambiguous, flag for review.

## 5.3 Step 3 — Confirm Trail‑Level Identity
The candidate must:
- Represent a full linear corridor
- Not be a single segment
- Not be a cluster of segments
- Not be a Trail Network

If unclear, flag for review.

## 5.4 Step 4 — Extract Required Metadata
For each candidate, extract:
- Trail name
- Alternate names
- Trail type
- Total length (if documented)
- Counties traversed
- Managing agency (primary)
- Managing agencies (secondary)
- Status
- Description
- URL
- Map link
- Notes
- Source tier
- Source dataset
- Discovery confidence

## 5.5 Step 5 — Log Trail Segments (Non‑Authoritative)
Record any documented segments, but do not create segment entities here.
Segment creation occurs in the Trail Segment Discovery Sub‑Procedure v1.

## 5.6 Step 6 — Log Trail Network Membership (Non‑Authoritative)
Record any Trail Networks the Trail is part of.
Membership becomes authoritative during normalization.

## 5.7 Step 7 — Emit Raw Candidate Record
Produce a Raw Candidate Trail Record following the Trail Schema Module v1.

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

## 6.1 Federal Tier
Must surface:
- National Scenic Trails
- National Historic Trails
- National Recreation Trails
- Federally documented water trails

## 6.2 State Tier
Must surface:
- State‑designated trails
- Statewide trail corridors
- State water trails
- State greenway or bikeway systems (individual trails)

## 6.3 Park District Tier
Must surface:
- All named trails within district boundaries
- All named loops
- All named multi‑use trails

## 6.4 County Tier
May surface:
- Countywide bikeways
- Countywide greenways
- County‑managed trail corridors

## 6.5 Township & Municipal Tiers
May surface:
- Local named trails
- Local greenways
- Local bikeways

## 6.6 Land Trust & Conservancy Tier
May surface:
- Named trails within preserves
- Named loops
- Named access corridors

## 6.7 Private & Organization‑Based Tier
May surface:
- Privately managed named trails
- Campus‑scale trail systems (individual trails)

------------------------------------------------------------
# 7. CONSOLIDATION RULES
During consolidation:
- Merge identical Trail names across tiers.
- Preserve all conflicting metadata.
- Do not merge Trails with different documented names.
- Align Trail Segments with their parent Trails.
- Align Trails with Trail Networks when documented.
- Maintain all source references.

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS
Each Trail candidate must output:

- All fields required by the Trail Schema Module v1
- Discovery Metadata
- Source references
- Non‑authoritative segment references
- Non‑authoritative network membership references
- Confidence and verification placeholders

Output must conform to:
- Discovery Metadata Specification v1.0
- TSV Output Specification v2.0
- Normalization Contract v2.0

------------------------------------------------------------
# 9. INTEGRATION POINTS
This module integrates with:
- Discovery Protocol Module v3.1
- Trail Schema Module v1
- Trail Vocabulary Module v1
- Trail Segment Discovery Sub‑Procedure v1
- Trail Network Discovery Sub‑Procedure v1
- Site Network Discovery Sub‑Procedure v1
- Normalization and Resolution Modules
- TSV Output Specifications
- Audit & Logging Module v1.1

------------------------------------------------------------
# END OF TRAIL DISCOVERY SUB‑PROCEDURE v1