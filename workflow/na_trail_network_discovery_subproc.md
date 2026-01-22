# NATURAL AREAS PROJECT — TRAIL NETWORK DISCOVERY SUB‑PROCEDURE v3.2.2
Authoritative, versioned sub‑procedure for discovering **Trail Networks** in the
statewide Natural Areas & Trails system.

This module defines:
- The Trail Network discovery workflow  
- Required sources  
- Identity rules for Trail Network candidates  
- Tier‑specific expectations  
- Output requirements  
- Integration points  

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Network Vocabulary Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

The Trail Network Discovery Sub‑Procedure v3.2.2 provides the authoritative,
deterministic workflow for discovering **Trail Networks** across all eight
discovery tiers.

A Trail Network is:
- A **named, identity‑bearing umbrella entity**  
- Composed of multiple Trails  
- Documented in authoritative sources  
- Distinct from its member Trails  

This sub‑procedure ensures:
- Consistent identification of Trail Networks  
- Prevention of misclassification as Trails or Sites  
- Proper metadata capture  
- Clean integration with Trail and Site Network discovery  

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

All sources must be logged in **Discovery Metadata v3.2.2**.

------------------------------------------------------------
# 4. IDENTITY RULES FOR TRAIL NETWORK CANDIDATES

A Trail Network candidate is valid only if:

1. It is explicitly documented as a **multi‑trail system**.  
2. It has a **stable, identity‑bearing name**.  
3. It is composed of **two or more Trails**.  
4. It is distinct from its member Trails.  
5. It is not merely a marketing label or informal grouping.  
6. It is not a Site Network.  
7. It is not a single Trail with multiple Segments.  

If any condition fails, the candidate must not be created.

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

Record each appearance as a **Raw Candidate Record**.

## 5.2 Step 2 — Verify Identity‑Bearing Name
A Trail Network must have:
- A documented, stable name  
- Not a temporary project name  
- Not a marketing slogan  

If ambiguous, flag for review in metadata.

## 5.3 Step 3 — Confirm Multi‑Trail Composition
The candidate must include:
- Two or more Trails  
- Documented membership  
- Explicit geographic or thematic linkage  

Do not infer membership.

## 5.4 Step 4 — Extract Raw Metadata
Extract only **raw, unnormalized** values:

- network_name_raw  
- network_type_raw  
- counties_raw  
- states_raw (if multi‑state)  
- managing_agency_raw  
- description_raw  
- url_primary_raw  
- url_all_raw  
- source_datasets  
- source_maps  
- source_gis_layers  
- notes_raw  

No normalization is permitted.

## 5.5 Step 5 — Log Member Trails (Non‑Authoritative)
Record all Trails referenced as members.  
Membership becomes authoritative during normalization.

## 5.6 Step 6 — Emit Raw Candidate Record
Produce a Raw Candidate Trail Network Record conforming to the  
**Discovery Output Specification v3.2.2**.

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
- Apply **Resolution Module v3.2.2** for ambiguous cases.  

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS

Each Trail Network candidate must output:

- A **Raw Candidate Record** (unnormalized)  
- Raw values only  
- Complete **Discovery Metadata v3.2.2**  
- Raw member Trail references  
- No normalized fields  
- No Derived Label  
- No TSV rows (unless developer preview is explicitly requested)  

Output must conform to:
- **Discovery Metadata Specification v3.2.2**  
- **Discovery Output Specification v3.2.2**  
- **Resolution Module v3.2.2**  

------------------------------------------------------------
# 9. INTEGRATION POINTS

This module integrates with:
- **Discovery Protocol Module v3.2.2**  
- **Trail Network Schema Module v3.2.2**  
- **Trail Network Vocabulary Module v3.2.2**  
- **Trail Discovery Sub‑Procedure v3.2.2**  
- **Trail Segment Discovery Sub‑Procedure v3.2.2**  
- **Site Network Discovery Sub‑Procedure v3.2.2**  
- **Resolution Module v3.2.2**  
- **Normalization Contracts v3.2.2**  
- **TSV Output Specifications v3.2.2**  
- **Audit & Logging Module v3.2.2**  

------------------------------------------------------------
# END OF TRAIL NETWORK DISCOVERY SUB‑PROCEDURE v3.2.2