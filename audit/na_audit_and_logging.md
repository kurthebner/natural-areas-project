# NATURAL AREAS PROJECT — AUDIT & LOGGING MODULE v3.1
A deterministic, system‑wide framework for recording, storing, and surfacing all
decisions, sources, conflicts, formatting transformations, normalization actions,
multi‑county expansions, and delimiter‑integrity checks made during the Natural
Areas processing pipeline for **all seven entity types**.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- What must be logged during each processing run
- How logs are structured
- How conflicts and ambiguities are surfaced
- How normalization and formatting transformations are recorded
- How multi‑county expansions are documented
- How delimiter‑integrity checks are logged
- How module versions are recorded
- How audit trails ensure reproducibility and transparency

This module ensures:

- Every decision is traceable
- Every data source is documented
- No silent corrections occur
- No silent formatting drift occurs
- All conflicts are visible
- All delimiter‑integrity issues are surfaced
- The entire pipeline is reproducible at any time

------------------------------------------------------------
# 2. SCOPE OF LOGGING

Logging applies to **all seven entity types**:

- Site
- Sub‑Site
- Access Point
- Trail
- Trail Segment
- Trail Network
- Site Network

Copilot must log all actions taken during:

- Baseline loading
- Discovery (all seven entities)
- Resolution (all seven entities)
- Normalization (all seven entities)
- TSV output generation (all seven entities)
- TSV delimiter‑integrity validation (all seven entities)

Logging applies to:

- Every entity
- Every field
- Every conflict
- Every correction
- Every unverifiable claim
- Every formatting correction
- Every delimiter‑integrity anomaly
- Every multi‑county expansion
- Every Derived Label construction
- Every integrity‑anchor validation

------------------------------------------------------------
# 3. LOG STRUCTURE

Each processing run produces a structured log with the following sections.

------------------------------------------------------------
## 3.1 Run Metadata

- County name (or multi‑county batch)
- Timestamp (start and end)
- Module versions used:
  - All seven Schema Modules v3.1
  - All seven Vocabulary Modules v3.1
  - All seven Normalization Contracts v3.1
  - All seven TSV Output Specifications v3.1
  - TSV Integrity Check Module v3.1
  - Discovery Protocol Module v3.1
  - Discovery Output Specification v3.1
  - Resolution Module v3.1
  - Processing / Orchestration Module v3.1
  - Audit & Logging Module v3.1
  - County Baseline Module

------------------------------------------------------------
## 3.2 Source Log

For each entity:

- All URLs consulted
- All GIS layers consulted
- All authoritative documents consulted
- All secondary sources consulted
- Notes on source reliability (if applicable)

------------------------------------------------------------
## 3.3 Conflict Log

For each conflict:

- Entity type
- Field name
- Conflicting values
- Sources of each conflicting value
- Resolution applied (or flagged for user review)
- Module responsible for resolution

------------------------------------------------------------
## 3.4 Correction Log

For each correction:

- Entity type
- Field name
- Original value
- Corrected value
- Reason for correction
- Source supporting correction
- Module responsible

------------------------------------------------------------
## 3.5 Unverifiable Claims Log

For each unverifiable claim:

- Entity type
- Field name
- Claimed value
- Source of claim
- Reason unverifiable
- Action taken (blanked, flagged, or deferred)

------------------------------------------------------------
## 3.6 Exclusion Log

For each excluded entity:

- Name
- Entity type
- Reason for exclusion
- Module rule invoked
- Supporting sources

------------------------------------------------------------
## 3.7 Multi‑Entity Split Log

For each split:

- Parent entity
- Child entities created
- Reason for split
- Rules invoked

(Applies to Sites, Trails, and Networks; never to Access Points.)

------------------------------------------------------------
## 3.8 Normalization Log

For each entity:

- All fields normalized
- Any fields left blank (with reason)
- Any formatting corrections
- Controlled vocabulary assignments
- Derived Label construction details
- Integrity‑anchor validation
- Multi‑county expansion details
- Parent/child relationship validation
- URL normalization
- GPS normalization
- Plus Code normalization

------------------------------------------------------------
## 3.9 Delimiter‑Integrity Log

For each TSV row:

- Expected delimiter count (entity‑specific)
- Actual delimiter count
- Whether the row passed delimiter‑integrity validation
- Any anomalies:
  - Missing delimiters
  - Extra delimiters
  - Spaces between delimiters
  - Collapsed blank fields
  - Misaligned fields
  - Misaligned Derived Label
  - Misaligned integrity anchor
  - Misaligned parent entity

### Corrective Action
- Whether the row was corrected
- Whether the row was rejected
- Whether the pipeline halted

------------------------------------------------------------
# 4. LOGGING RULES

## 4.1 No Silent Corrections
Every correction must appear in the Correction Log.

## 4.2 No Silent Exclusions
Every exclusion must appear in the Exclusion Log.

## 4.3 No Silent Assumptions
If a field cannot be verified, it must be logged as unverifiable.

## 4.4 No Invented Data
Missing data must remain blank and be logged.

## 4.5 All Sources Must Be Recorded
Even if they yield no useful information.

## 4.6 All Conflicts Must Be Surfaced
Never resolved silently.

## 4.7 All Module Versions Must Be Recorded
Ensures reproducibility.

## 4.8 Blank Fields Must Be True Blanks
No placeholders or invisible characters.

## 4.9 Delimiter Count Must Be Validated
Entity‑specific delimiter counts must be enforced.

## 4.10 Multi‑County Expansion Must Be Logged
Including:
- Counties emitted
- Order of rows
- Any unverifiable county assignments

## 4.11 Integrity Anchors Must Be Validated
For Trails, Trail Segments, Trail Networks, Site Networks, Sub‑Sites.

------------------------------------------------------------
# 5. USER‑VISIBLE SURFACING

At the end of each run, Copilot must surface:

- Summary of conflicts requiring review
- Summary of unverifiable claims
- Summary of exclusions
- Summary of multi‑entity splits
- Summary of baseline anomalies
- Summary of normalization failures
- Summary of delimiter‑integrity anomalies
- Summary of multi‑county expansion anomalies

Summaries must be concise but complete.

------------------------------------------------------------
# 6. STORAGE & RETENTION

## 6.1 Logs stored per county per run  
## 6.2 Logs retrievable for comparison across runs  
## 6.3 Logs include module version numbers  
## 6.4 Logs never overwrite previous logs unless explicitly instructed  

------------------------------------------------------------
# 7. AUDIT TRAIL REQUIREMENTS

A valid audit trail must allow the user to:

- Reconstruct every decision
- Trace every field to its source
- Identify every conflict and resolution
- Verify no invented data was introduced
- Confirm correct module ordering
- Confirm all delimiter‑integrity checks passed
- Confirm all seven entity types were processed correctly
- Confirm multi‑county expansion was correct
- Confirm Derived Labels and integrity anchors were correct

------------------------------------------------------------
# 8. PIPELINE INTEGRATION

This module is invoked automatically during:

- Stage 1: Baseline Loading
- Stage 2: Discovery
- Stage 3: Resolution
- Stage 4: Normalization
- Stage 5: TSV Output
- Stage 6: TSV Integrity Check
- Stage 7: Finalization

It produces the final output of Stage 7.

------------------------------------------------------------
# 9. MODULE DEPENDENCIES

This module depends on:

- All seven Schema Modules v3.1
- All seven Vocabulary Modules v3.1
- All seven Normalization Contracts v3.1
- All seven TSV Output Specifications v3.1
- TSV Integrity Check Module v3.1
- Discovery Protocol Module v3.1
- Resolution Module v3.1
- Processing / Orchestration Module v3.1

------------------------------------------------------------
# END OF AUDIT & LOGGING MODULE v3.1