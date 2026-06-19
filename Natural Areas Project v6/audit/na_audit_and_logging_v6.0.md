# NATURAL AREAS PROJECT
# AUDIT & LOGGING MODULE v6.0
Authoritative, deterministic, system-wide framework for recording, storing, and
surfacing all decisions, sources, conflicts, formatting transformations,
normalization actions, county list behaviors, delimiter-integrity checks, and
document collection activity made during the Natural Areas processing pipeline
for **all four entity types**.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v6.x.

This module supersedes Audit & Logging Module v5.1.

------------------------------------------------------------
# CHANGES FROM v5.1 → v6.0

- **Entity types reduced from six to four**: Trail, Trail Segment, and Trail
  Network are unified into the Trailthing entity type. All references to Trail,
  Trail Segment, and Trail Network updated. §2 Scope, §4.10, §4.11, §7, §9
  updated accordingly.

- **Derived Label removed throughout**: Derived Label was retired in v5.x but
  still appeared in v5.1 §3.9 Normalization Log and §3.10 Delimiter-Integrity
  Log. All references removed.

- **Document Collection Log added (§3.11)**: The Document Collection System
  (Discovery Orchestration Module v6.0 §4) requires logging of all downloaded
  source documents. §3.11 defines the document collection log structure. §3.2
  Discovery Log updated with cross-reference. §2 Scope updated.

- **Normalization Log (§3.9) updated**: Derived Label removed. New v6.0 field
  entries added: habitat_type (open vocabulary — no mapping), access_notes
  (free-text), last_verified_date (DATE validation), field_verified (boolean
  validation), source_term_raw (verbatim pass-through, warn if blank), cross-entity
  reference pairing validation (ID / Name pairs).

- **Delimiter-Integrity Log (§3.10) updated**: Field counts updated to v6.0
  values (Site 30, Trailthing 30, Site Network 17, Access Point 19 delimiters).
  Derived Label misalignment condition removed. Cross-entity reference pairing
  anomaly added. source_term blank warning added for Trailthings.

- **Run Metadata (§3.1) updated**: Module list updated to v6.0 (four schemas,
  four vocabularies, four normalization contracts, four TSV specs, v6.0 integrity
  check, resolution engine, normalization engine).

- **IMP-018 — Visit Planning Query Template added (§10)**: Standard queries for
  reviewing held entities with GPS and field verification status to plan field
  verification passes.

- **All v5.1 rules carried forward**: no silent corrections, no silent exclusions,
  no invented data, all sources recorded, all conflicts surfaced, module versions
  recorded, GIS-derived field logging, multi-county logging.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- What must be logged during each processing run
- How logs are structured
- How conflicts and ambiguities are surfaced
- How normalization and formatting transformations are recorded
- How document collection activity is recorded
- How multi-county list behavior is documented
- How delimiter-integrity checks are logged
- How module versions are recorded
- How audit trails ensure reproducibility and transparency
- Standard queries for visit planning (§10)

This module ensures:

- Every decision is traceable
- Every data source is documented
- No silent corrections occur
- No silent formatting drift occurs
- All conflicts are visible
- All delimiter-integrity issues are surfaced
- All identity-anchor validations are logged
- All downloaded source documents are logged
- The entire pipeline is reproducible at any time

------------------------------------------------------------
# 2. SCOPE OF LOGGING

Logging applies to **all four entity types**:

- Site
- Trailthing
- Site Network
- Access Point

Logging must cover all actions taken during:

- Baseline loading
- Discovery (including document collection)
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
- Every identity-anchor validation
- Every parent-entity validation
- Every cross-entity reference pairing validation (ID / Name pairs)
- Every GIS-derived field assignment (township, municipality)
- Every document downloaded during discovery (§3.11)

------------------------------------------------------------
# 3. LOG STRUCTURE

Each processing run produces a structured log with the following sections.

------------------------------------------------------------
## 3.1 Run Metadata

- County processed
- Timestamp (start and end)
- discovery_run_id (unique identifier for the discovery session)
- Module versions used:
  - Site Schema Module v6.0
  - Trailthing Schema Module v6.0
  - Site Network Schema Module v6.0
  - Access Point Schema Module v6.0
  - Site Vocabulary Module v6.0
  - Trailthing Vocabulary Module v6.0
  - Site Network Vocabulary Module v6.0
  - Access Point Vocabulary Module v6.0
  - Site Normalization Contract v6.0
  - Trailthing Normalization Contract v6.0
  - Site Network Normalization Contract v6.0
  - Access Point Normalization Contract v6.0
  - Site TSV Output Specification v6.0
  - Trailthing TSV Output Specification v6.0
  - Site Network TSV Output Specification v6.0
  - Access Point TSV Output Specification v6.0
  - TSV Integrity Check Module v6.0
  - Discovery Orchestration Module v6.0
  - Resolution Engine v6.0
  - Normalization Engine v6.0
  - Entity Upsert Engine v6.x *(or v5.x)*
  - Audit & Logging Module v6.0
  - County Baseline Module v6.x *(or v5.x)*

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

For documents downloaded during discovery, see **§3.11 Document Collection Log**.

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

(Applies to Sites and Site Networks; never to Access Points or Trailthings.)

------------------------------------------------------------
## 3.9 Normalization Log

For each entity:

- All fields normalized
- Any fields left blank (with reason)
- Any formatting corrections
- Controlled vocabulary assignments
- Identity-anchor validation
- Parent-entity validation
- Cross-entity reference pairing validation:
  - Each ID / Name field pair checked (both blank together or both populated together)
  - Any mismatch logged as a pairing anomaly
  - For Site Network member lists: count of member_site_ids vs. member_site_names

**County list normalization:**
- Final semicolon-delimited list
- Alphabetical ordering confirmed
- Duplicate removal (if any)
- Source of county assignments
- Any unverifiable county claims

**GPS and spatial fields:**
- GPS validation → numeric gps_lat, gps_lon (from gps_lat_raw / gps_lon_raw)
- plus_code derivation
- Township (assigned via GIS spatial lookup — log layer and spatial relationship)
- Municipality (assigned via GIS spatial lookup — log layer and spatial relationship)

**Features normalization** (Sites, Access Points):
- Semicolon-delimited list from features_raw
- Activity detection step results (IMP-049)
- Operational content stripping results (IMP-050)
- Named entity detection results (IMP-051)
- Vocabulary mapping results
- Unmapped token log entries (IMP-116 — for Stage 5 vocabulary expansion candidates)

**Description normalization** (Sites):
- Redundancy detection result (IMP-052)
- Formula description detection result (IMP-059)
- Acreage source documented (IMP-060)

**Notes normalization** (all entity types):
- Pipeline metadata stripping result (IMP-053)
- Content retained vs. stripped

**Trailthing-specific normalizations:**
- source_term_raw pass-through (log verbatim value; WARN if blank)
- source_hierarchy_context_raw pass-through
- use_type, surface_type, origin_type, org_type, status, difficulty vocabulary
  assignments or null-and-log decisions
- parent_id, site_parent_id, parent_site_network_id resolution outcomes

**New v6.0 field normalizations (Sites, Access Points):**
- habitat_type: open vocabulary — log value as passed through; no mapping applied
- access_notes: free-text — log value as passed through
- last_verified_date: log DATE format validation result (valid / reformatted / absent)
- field_verified: log boolean validation result (valid / defaulted / anomaly)

------------------------------------------------------------
## 3.10 Delimiter-Integrity Log

For each TSV row:

- Entity type
- Expected delimiter count:
  - Site: 30
  - Trailthing: 31
  - Site Network: 17
  - Access Point: 19
- Actual delimiter count
- Whether the row passed delimiter-integrity validation
- Any anomalies:
  - Missing or extra delimiters
  - Spaces between delimiters
  - Collapsed blank fields
  - Misaligned fields
  - Misaligned identity anchor
  - Misaligned parent entity
  - Misaligned GPS fields
  - Misaligned Features field
  - **Cross-entity reference pairing anomaly** (ID field blank / Name field populated, or vice versa)
  - **source_term blank warning** (Trailthings only — discovery gap indicator)
  - **member_site_ids / member_site_names count mismatch** (Site Networks)
  - Misaligned last_verified_date or field_verified
  - Non-DATE content in last_verified_date
  - Non-boolean content in field_verified

### Corrective Action

- Whether the row was corrected
- Whether the row was rejected
- Whether the pipeline halted

------------------------------------------------------------
## 3.11 Document Collection Log

The Document Collection System (Discovery Orchestration Module v6.0 §4) downloads
qualifying source documents during discovery and records them in the county's
`source_documents/{county}_document_log.yaml`. This log section provides an audit
summary of document collection activity for the run.

For each run, record:

- Total documents downloaded during this run
- Total documents in the county document log (cumulative)
- Any download failures (URL, error, tier, date attempted)
- Any documents logged as URL-only (interactive GIS viewers, REST endpoints)
- document_log.yaml location (relative path from county folder)
- source_documents/ folder location

For each downloaded document, the document log entry (in `{county}_document_log.yaml`)
serves as the primary record. The audit log references it by count and flags exceptions.

**Document log entry fields** (per Discovery Orchestration Module v6.0 §4):
- local_file (relative path from source_documents/ folder, or blank for URL-only)
- url
- document_type (vocabulary: PDF Map, Brochure, Recreation Guide, Master Plan,
  Management Plan, GPX, KML, GIS Export, Interactive Viewer, ArcGIS Endpoint,
  Kiosk Documentation, Other)
- date_accessed (YYYY-MM-DD)
- title
- description
- tier (1–8)
- entities (optional free-text — informal annotation of which entities the document
  covers)

**Logging rule**: If the pipeline run discovers documents not yet in the
`{county}_document_log.yaml`, the failure to log them at discovery time is a
process failure (not a pipeline error). Log the gap here and flag for manual addition
to the document log before the next county run resumes.

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
Entity-specific delimiter counts must be enforced per §3.10.

## 4.10 Multi-County Behavior Must Be Logged
For all four entities:
- Semicolon-delimited county list
- Alphabetical ordering
- Duplicate detection
- Source of county assignments

## 4.11 Identity Anchors Must Be Validated
For all four entity types.

## 4.12 GIS-Derived and GPS-Derived Fields Must Be Logged
Every assignment of `township` and `municipality` via GIS spatial lookup must be
logged, including the GIS layer used and the spatial relationship confirmed. Every
derivation of `plus_code` from validated GPS coordinates must be logged.

## 4.13 Discovery Log Must Not Contain Normalization Decisions
Discovery logging records only what was collected. If a value was chosen between
conflicting sources, that decision belongs in the Normalization Log.

## 4.14 Developer Preview TSVs
Developer-requested TSV previews are not logged as official outputs.

## 4.15 Document Collection Must Be Logged
Every document downloaded during discovery must be logged in the county's
`{county}_document_log.yaml`. Download failures must also be logged. See §3.11.

## 4.16 Cross-Entity Reference Pairings Must Be Validated and Logged
Every ID / Name field pair must be checked. Mismatches are logged as anomalies.
See §3.9 and §3.10.

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
- Summary of vocabulary expansion candidates (unmapped tokens from IMP-116)
- Summary of document collection activity (documents downloaded, failures, URL-only)
- Summary of cross-entity reference pairing anomalies

Summaries must be concise but complete.

------------------------------------------------------------
# 6. STORAGE & RETENTION

## 6.1 Logs stored per county per run
## 6.2 Logs retrievable for comparison across runs
## 6.3 Logs include module version numbers and discovery_run_id
## 6.4 Logs never overwrite previous logs unless explicitly instructed
## 6.5 Document log ({county}_document_log.yaml) is a cumulative county artifact
  — it is not reset per run; it accumulates across all runs for the county

------------------------------------------------------------
# 7. AUDIT TRAIL REQUIREMENTS

A valid audit trail must allow the user to:

- Reconstruct every decision
- Trace every field to its source
- Identify every conflict and resolution
- Verify no invented data was introduced
- Confirm correct module ordering
- Confirm all delimiter-integrity checks passed
- Confirm all four entity types were processed correctly
- Confirm county list normalization was correct
- Confirm identity anchors were correct
- Confirm parent-entity relationships were validated correctly
- Confirm cross-entity ID / Name pairs are consistent
- Confirm GIS-derived township and municipality assignments were correct
- Confirm difficulty and accessibility came from authoritative sources only (not inferred)
- Confirm source_term_raw was captured for all Trailthings (WARN if absent)
- Confirm document collection log is complete for the county

------------------------------------------------------------
# 8. PIPELINE INTEGRATION

This module is invoked automatically during:

- Stage 1: Baseline Loading
- Stage 2: Discovery (including document collection logging)
- Stage 3: Resolution
- Stage 4: Normalization
- Stage 5: TSV Output
- Stage 6: TSV Integrity Check
- Stage 7: Finalization

It produces the final audit output of Stage 7.

------------------------------------------------------------
# 9. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v6.0
- Trailthing Schema Module v6.0
- Site Network Schema Module v6.0
- Access Point Schema Module v6.0
- Site Vocabulary Module v6.0
- Trailthing Vocabulary Module v6.0
- Site Network Vocabulary Module v6.0
- Access Point Vocabulary Module v6.0
- Site Normalization Contract v6.0
- Trailthing Normalization Contract v6.0
- Site Network Normalization Contract v6.0
- Access Point Normalization Contract v6.0
- Site TSV Output Specification v6.0
- Trailthing TSV Output Specification v6.0
- Site Network TSV Output Specification v6.0
- Access Point TSV Output Specification v6.0
- TSV Integrity Check Module v6.0
- Discovery Orchestration Module v6.0 *(document collection rules, §4)*
- Resolution Engine v6.0
- Normalization Engine v6.0
- Entity Upsert Engine v6.x *(or v5.x)*
- County Baseline Module v6.x *(or v5.x)*

------------------------------------------------------------
# 10. VISIT PLANNING QUERY TEMPLATE (IMP-018)

This section provides standard queries for reviewing entities by verification status
and GPS availability, supporting efficient planning of field verification passes.

These queries run against the live SQLite database (`natural_areas_v5.db`) and apply
to the normalized entity tables.

## 10.1 Sites Needing Field Verification

Returns all active Sites that have GPS coordinates but have never been field-verified.
Useful for planning a county visit pass.

```sql
SELECT
    site_id,
    name,
    category,
    subtype,
    governance,
    counties,
    municipality,
    township,
    gps_lat,
    gps_lon,
    plus_code,
    last_verified_date,
    field_verified
FROM sites
WHERE field_verified = 0
  AND gps_lat IS NOT NULL
  AND gps_lon IS NOT NULL
  AND status = 'Active'
ORDER BY counties, township, municipality, name;
```

## 10.2 Sites with No GPS (GPS Missing)

Returns Sites held for missing GPS — candidates for field GPS acquisition.

```sql
SELECT
    entity_id,
    entity_type,
    hold_reason,
    hold_detail,
    counties,
    name
FROM held_entities
WHERE entity_type = 'Site'
  AND hold_reason = 'gps_missing'
ORDER BY counties, name;
```

## 10.3 Sites Not Verified Since a Target Date

Returns Sites where last_verified_date is older than a specified cutoff, or is null.
Replace '2025-01-01' with the desired staleness threshold.

```sql
SELECT
    site_id,
    name,
    category,
    governance,
    counties,
    gps_lat,
    gps_lon,
    last_verified_date,
    field_verified
FROM sites
WHERE (last_verified_date < '2025-01-01'
       OR last_verified_date IS NULL)
  AND status = 'Active'
  AND gps_lat IS NOT NULL
ORDER BY last_verified_date ASC NULLS FIRST, counties, name;
```

## 10.4 Access Points Needing Field Verification

Returns Access Points that have GPS but have never been field-verified.

```sql
SELECT
    ap.access_point_id,
    ap.access_point_name,
    ap.access_point_type,
    ap.county,
    ap.township,
    ap.municipality,
    ap.gps_lat,
    ap.gps_lon,
    ap.last_verified_date,
    ap.field_verified
FROM access_points ap
WHERE ap.field_verified = 0
  AND ap.gps_lat IS NOT NULL
  AND ap.gps_lon IS NOT NULL
ORDER BY ap.county, ap.township, ap.municipality, ap.access_point_name;
```

## 10.5 Entities with RECLASSIFICATION_CANDIDATE Flag

Returns Access Points flagged during discovery or normalization as candidates for
reclassification as Sites (IMP-114). These require manual review before the next run.

```sql
SELECT
    access_point_id,
    access_point_name,
    access_point_type,
    county,
    identity_notes,
    gps_lat,
    gps_lon
FROM access_points
WHERE identity_notes LIKE '%RECLASSIFICATION_CANDIDATE%'
ORDER BY county, access_point_name;
```

## 10.6 Combined Field Visit Priority List

Returns Sites and Access Points in a county, sorted by geographic proximity
(municipality/township), to support planning an efficient field visit route.
Replace 'Wood' with the target county.

```sql
SELECT
    'Site' AS entity_type,
    site_id AS entity_id,
    name,
    category AS subtype_or_type,
    township,
    municipality,
    gps_lat,
    gps_lon,
    plus_code,
    last_verified_date,
    CAST(field_verified AS TEXT) AS field_verified
FROM sites
WHERE counties LIKE '%Wood%'
  AND status = 'Active'
  AND gps_lat IS NOT NULL

UNION ALL

SELECT
    'Access Point' AS entity_type,
    CAST(access_point_id AS TEXT) AS entity_id,
    access_point_name AS name,
    access_point_type AS subtype_or_type,
    township,
    municipality,
    gps_lat,
    gps_lon,
    plus_code,
    last_verified_date,
    CAST(field_verified AS TEXT) AS field_verified
FROM access_points
WHERE county = 'Wood'
  AND gps_lat IS NOT NULL

ORDER BY municipality NULLS LAST, township NULLS LAST, name;
```

**Usage note**: The `field_verified` column in the Sites and Access Points tables
uses boolean storage (0/1 in SQLite). The CAST in the query above renders it as
text "0"/"1" for readability. Adjust as needed for the reporting context.

------------------------------------------------------------
# END OF AUDIT & LOGGING MODULE v6.0
