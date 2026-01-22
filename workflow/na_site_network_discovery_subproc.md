# NATURAL AREAS PROJECT — SITE NETWORK DISCOVERY SUB‑PROCEDURE v3.2.2
Authoritative, versioned sub‑procedure for discovering **Site Networks** in the
statewide Natural Areas & Trails system.

This module defines:
- The Site Network discovery workflow  
- Required sources  
- Identity rules for Site Network candidates  
- Tier‑specific expectations  
- Output requirements  
- Integration points  

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Site Network Vocabulary Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

The Site Network Discovery Sub‑Procedure v3.2.2 provides the authoritative,
deterministic workflow for discovering **Site Networks** across all eight
discovery tiers.

A Site Network is:
- A **named, identity‑bearing umbrella entity**  
- Composed of multiple Sites  
- Documented in authoritative sources  
- Distinct from its member Sites  

This sub‑procedure ensures:
- Consistent identification of Site Networks  
- Prevention of misclassification as Sites or child Sites  
- Proper metadata capture  
- Clean integration with Trail Network and Site discovery  

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

All sources must be logged in **Discovery Metadata v3.2.2**.

------------------------------------------------------------
# 4. IDENTITY RULES FOR SITE NETWORK CANDIDATES

A Site Network candidate is valid only if:

1. It is explicitly documented as a **multi‑site system**.  
2. It has a **stable, identity‑bearing name**.  
3. It is composed of **two or more Sites**.  
4. It is distinct from its member Sites.  
5. It is not merely a marketing label or informal grouping.  
6. It is not a Trail Network.  
7. It is not a single Site with multiple child Sites.  

If any condition fails, the candidate must not be created.

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

Record each appearance as a **Raw Candidate Record**.

## 5.2 Step 2 — Verify Identity‑Bearing Name
A Site Network must have:
- A documented, stable name  
- Not a temporary project name  
- Not a marketing slogan  

If ambiguous, flag for review in metadata.

## 5.3 Step 3 — Confirm Multi‑Site Composition
The candidate must include:
- Two or more Sites  
- Documented membership  
- Explicit geographic or thematic linkage  

Do not infer membership.

## 5.4 Step 4 — Extract Raw Metadata
Extract only **raw, unnormalized** values:

- network_name_raw  
- alternate_names_raw  
- network_type_raw  
- counties_raw  
- states_raw (if multi‑state)  
- managing_agency_raw  
- secondary_managing_agencies_raw  
- description_raw  
- history_raw  
- url_primary_raw  
- url_all_raw  
- notes_raw  

**Discovery Metadata fields (required):**
- source_confidence_raw  
- verification_status_raw  
- field_confidence_map_raw  
- field_verification_map_raw  

**Source tracking fields:**
- source_datasets  
- source_maps  
- source_gis_layers  

No normalization is permitted.

## 5.5 Step 5 — Log Member Sites (Non‑Authoritative)
Record all Sites referenced as members.  
Membership becomes authoritative during normalization.

## 5.6 Step 6 — Emit Raw Candidate Record
Produce a Raw Candidate Site Network Record conforming to the  
**Discovery Output Specification v3.2.2**.

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
- Apply **Resolution Module v3.2.2** for ambiguous cases.  

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS

Each Site Network candidate must output:

- A **Raw Candidate Record** (unnormalized)  
- Raw values only  
- Complete **Discovery Metadata v3.2.2**  
- Raw member Site references  
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
- **Site Network Schema Module v3.2.2**  
- **Site Network Vocabulary Module v3.2.2**  
- **Site Discovery Sub‑Procedure v3.2.2**  
- **Trail Network Discovery Sub‑Procedure v3.2.2**  
- **Resolution Module v3.2.2**  
- **Normalization Contracts v3.2.2**  
- **TSV Output Specifications v3.2.2**  
- **Audit & Logging Module v3.2.2**  

------------------------------------------------------------
# END OF SITE NETWORK DISCOVERY SUB‑PROCEDURE v3.2.2