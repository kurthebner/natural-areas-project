# NATURAL AREAS PROJECT
# AUDIT & LOGGING MODULE v5.0
Authoritative, deterministic, system-wide framework for recording, storing, and
surfacing all decisions, sources, conflicts, formatting transformations,
normalization actions, county list behaviors, and delimiter-integrity checks
made during the Natural Areas processing pipeline for **all six entity types**.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v5.0.

------------------------------------------------------------
# CHANGES FROM v4.0

- Field-level references updated for v5.0 schema (municipality, township, features, difficulty, accessibility, maps, gps_lat/gps_lon split)
- `role` and `access_level` removed from normalization log — fields deleted from Access Point schema
- **Discovery = Collection** principle reinforced in discovery logging — discovery log must never record normalization decisions
- Run metadata updated to reference v5.0 modules
- Multi-state reference simplified — county list is standard; state list applies only when entities cross state lines
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- What must be logged during each processing run
- How logs are structured
- How conflicts and ambiguities are surfaced
- How normalization and formatting transformations are recorded
- How multi-county list behavior is documented
- How delimiter-integrity checks are logged
- How module versions are recorded
- How audit trails ensure reproducibility and transparency

This module ensures:

- Every decision is traceable
- Every data source is documented
- No silent corrections occur
- No silent formatting drift occurs
- All conflicts are visible
- All delimiter-integrity issues are surfaced
- All identity-anchor validations are logged
- The entire pipeline is reproducible at any time

------------------------------------------------------------
# 2. SCOPE OF LOGGING

Logging applies to **all six entity types**:

- Site
- Access Point
- Trail
- Trail Segment
- Trail Network
- Site Network

Logging must cover all actions taken during:

- Baseline loading
- Discovery
- Resolution
- Normalization
- TSV output generation
- TSV delimiter-integrity validation

Logging applies to:

- Every entity
- Every field
- Every conflict
- Every correction
- Every unverifiable claim
- Every formatting correction
- Every delimiter-integrity anomaly
- Every county list normalization
- Every Derived Label construction
- Every identity-anchor validation
- Every parent-entity validation
- Every GIS-derived field assignment (township, municipality)

------------------------------------------------------------
# 3. LOG STRUCTURE

Each processing run produces a structured log with the following sections.

------------------------------------------------------------
## 3.1 Run Metadata

- County processed
- Timestamp (start and end)
- discovery_run_id (unique identifier for the discovery session)
- Module versions used:
  - All six Schema Modules v5.0
  - All six Vocabulary Modules v5.0
  - All six Normalization Modules v5.0
  - All six TSV Output Specifications v5.0
  - TSV Integrity Check Module v5.0
  - Discovery Protocol Module v5.0
  - Discovery Output Specification v5.0
  - Discovery Metadata Specification v5.0
  - Resolution Engine v5.0
  - Normalization Engine v5.0
  - Entity Upsert Engine v5.0
  - Audit & Logging Module v5.0
  - County Baseline Module v5.0
  - Child Site Rules Module v5.0

------------------------------------------------------------
## 3.2 Discovery Log

For each entity discovered:

- Entity name (raw)
- Entity type (raw)
- Tier discovered in
- All source URLs consulted
- All GIS layers consulted
- Extraction method (enumerative / recursive / baseline)
- parent_url (if recursive)
- discovery_run_id
- Raw county list
- Raw field values (preserved exactly)
- Uncertainty flags
- Conflict flags (raw — not resolved)

**Discovery logging must never record normalization decisions.**
Discovery = Collection. Any decision about value selection, vocabulary assignment,
or field correction belongs in the Normalization Log.

------------------------------------------------------------
## 3.3 Source Log

For each entity:

- All URLs consulted
- All GIS layers consulted
- All authoritative documents consulted
- All secondary sources consulted
- Notes on source reliability (if applicable)

------------------------------------------------------------
## 3.4 Conflict Log

For each conflict:

- Entity type
- Field name
- Conflicting values
- Sources of each conflicting value
- Resolution applied (or flagged for review)
- Module responsible

------------------------------------------------------------
## 3.5 Correction Log

For each correction:

- Entity type
- Field name
- Original value
- Corrected value
- Reason for correction
- Source supporting correction
- Module responsible

------------------------------------------------------------
## 3.6 Unverifiable Claims Log

For each unverifiable claim:

- Entity type
- Field name
- Claimed value
- Source of claim
- Reason unverifiable
- Action taken (blanked, flagged, or deferred)

------------------------------------------------------------
## 3.7 Exclusion Log

For each excluded entity:

- Name
- Entity type
- Reason for exclusion
- Module rule invoked
- Supporting sources

------------------------------------------------------------
## 3.8 Multi-Entity Split Log

For each split:

- Parent entity
- Child entities created
- Reason for split
- Rules invoked

(Applies to Sites and Networks; never to Access Points or Trail Segments.)

------------------------------------------------------------
## 3.9 Normalization Log

For each entity:

- All fields normalized
- Any fields left blank (with reason)
- Any formatting corrections
- Controlled vocabulary assignments
- Derived Label construction details
- Identity-anchor validation
- Parent-entity validation
- **County list normalization:**
  - Final semicolon-delimited list
  - Alphabetical ordering confirmed
  - Duplicate removal (if any)
  - Source of county assignments
  - Any unverifiable county claims
- URL normalization
- GPS normalization (gps_lat / gps_lon split from gps_raw)
- **GIS-derived field assignments:**
  - Township (assigned via GIS spatial lookup)
  - Municipality (assigned via GIS spatial lookup)
- Features normalization (semicolon-delimited list from features_raw)
- Difficulty normalization (vocabulary assignment from difficulty_raw)
- Accessibility normalization (vocabulary assignment from accessibility_raw)
- Maps normalization (semicolon-delimited URL list from maps_raw)
- Management normalization (free-text, rule-governed)
- Ownership normalization (free-text, rule-governed)

------------------------------------------------------------
## 3.10 Delimiter-Integrity Log

For each TSV row:

- Entity type
- Expected delimiter count
- Actual delimiter count
- Whether the row passed delimiter-integrity validation
- Any anomalies:
  - Missing delimiters
  - Extra delimiters
  - Spaces between delimiters
  - Collapsed blank fields
  - Misaligned fields
  - Misaligned Derived Label
  - Misaligned identity anchor
  - Misaligned parent entity
  - Misaligned GPS fields
  - Misaligned Features field
  - Misaligned Difficulty or Accessibility field

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
Ensures reproducibility across sessions and counties.

## 4.8 Blank Fields Must Be True Blanks
No placeholders or invisible characters.

## 4.9 Delimiter Count Must Be Validated
Entity-specific delimiter counts must be enforced.

## 4.10 Multi-County Behavior Must Be Logged
For all six entities:
- Semicolon-delimited county list
- Alphabetical ordering
- Duplicate detection
- Source of county assignments

## 4.11 Identity Anchors Must Be Validated
For all six entity types.

## 4.12 GIS-Derived Fields Must Be Logged
Every assignment of `township` and `municipality` via GIS spatial lookup
must be logged, including the GIS layer used and the spatial relationship confirmed.

## 4.13 Discovery Log Must Not Contain Normalization Decisions
Discovery logging records only what was collected. If a value was chosen
between conflicting sources, that decision belongs in the Normalization Log.

## 4.14 Developer Preview TSVs
Developer-requested TSV previews are not logged as official outputs.

------------------------------------------------------------
# 5. USER-VISIBLE SURFACING

At the end of each run, the system must surface:

- Summary of conflicts requiring review
- Summary of unverifiable claims
- Summary of exclusions
- Summary of multi-entity splits
- Summary of baseline anomalies
- Summary of normalization failures
- Summary of delimiter-integrity anomalies
- Summary of county list anomalies
- Summary of GIS-derived field assignments (township, municipality)

Summaries must be concise but complete.

------------------------------------------------------------
# 6. STORAGE & RETENTION

## 6.1 Logs stored per county per run
## 6.2 Logs retrievable for comparison across runs
## 6.3 Logs include module version numbers and discovery_run_id
## 6.4 Logs never overwrite previous logs unless explicitly instructed

------------------------------------------------------------
# 7. AUDIT TRAIL REQUIREMENTS

A valid audit trail must allow the user to:

- Reconstruct every decision
- Trace every field to its source
- Identify every conflict and resolution
- Verify no invented data was introduced
- Confirm correct module ordering
- Confirm all delimiter-integrity checks passed
- Confirm all six entity types were processed correctly
- Confirm county list normalization was correct
- Confirm Derived Labels and identity anchors were correct
- Confirm parent-entity relationships were validated correctly
- Confirm GIS-derived township and municipality assignments were correct
- Confirm difficulty and accessibility came from authoritative sources only (not inferred)

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

It produces the final audit output of Stage 7.

------------------------------------------------------------
# 9. MODULE DEPENDENCIES

This module depends on:

- All six Schema Modules v5.0
- All six Vocabulary Modules v5.0
- All six Normalization Modules v5.0
- All six TSV Output Specifications v5.0
- TSV Integrity Check Module v5.0
- Discovery Protocol Module v5.0
- Discovery Output Specification v5.0
- Discovery Metadata Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Upsert Engine v5.0
- County Baseline Module v5.0

------------------------------------------------------------
# END OF AUDIT & LOGGING MODULE v5.0
