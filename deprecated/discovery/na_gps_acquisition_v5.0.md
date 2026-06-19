# GPS ACQUISITION MODULE v5.0  
Authoritative GPS Collection and Verification Layer  
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# 1. PURPOSE

The GPS Acquisition Module v5.0 provides the authoritative, deterministic workflow for:

- Acquiring GPS coordinates for entities that lack them (primarily Access Points and Sites; optionally Trails).
- Verifying acquired coordinates against authoritative context (county, parent entity, known geometry).
- Recording GPS provenance (how, when, and from where coordinates were obtained).
- Preparing entities for **GPS‑dependent resolution** and **GIS‑dependent normalization**.

This module fills the gap between:

- **Resolution Engine v5.x — Pass 1** (structural resolution without GPS‑dependent identity).
- **Resolution Engine v5.x — Pass 2** (full identity resolution for GPS‑dependent entities).
- **Normalization Engine v5.x** (GPS validation, Plus Code computation, GIS lookup).

The module must not:

- Infer GPS from non‑authoritative sources.
- Normalize or validate GPS (that is Normalization’s responsibility).
- Perform identity matching or merging (that is Resolution’s responsibility).

It is a **collection + verification + provenance** layer only.

------------------------------------------------------------
# 2. SCOPE

The GPS Acquisition Module v5.0 governs:

- **Access Points** — primary target; GPS is required for identity and upsert.
- **Sites** — secondary target; GPS is highly desirable for navigation and GIS.
- **Trails / Trail Segments / Networks** — optional, if point representatives are desired.

It operates only on entities that:

- Have passed **Resolution v5.x Pass 1**.
- Lack valid `gps_lat_raw` / `gps_lon_raw`.
- Are eligible for GPS acquisition according to project policy.

The module does **not**:

- Modify non‑GPS fields.
- Modify metadata blocks other than GPS provenance.
- Change entity identity or parent relationships.
- Perform GIS spatial joins (that is Normalization’s responsibility).

------------------------------------------------------------
# 3. POSITION IN THE PIPELINE

The v5.x pipeline with GPS acquisition:

1. **Discovery v5.x**  
   Raw values + metadata (including `gps_lat_raw` / `gps_lon_raw` when published).

2. **Resolution Engine v5.x — Pass 1**  
   - Full resolution for non‑GPS‑dependent entities.  
   - Structural resolution for Access Points (without GPS anchors).  
   - Produces partially resolved entities, including APs with missing GPS.

3. **GPS Acquisition Module v5.0**  ← **THIS MODULE**  
   - Acquires GPS for APs and Sites (and optionally others).  
   - Records GPS provenance.  
   - Produces updated entities with `gps_lat_raw` / `gps_lon_raw`.

4. **Resolution Engine v5.x — Pass 2 (Access Points only)**  
   - Re‑runs identity matching for Access Points using GPS anchors.  
   - Produces fully resolved Access Points.

5. **Normalization Engine v5.x**  
   - Validates GPS.  
   - Computes Plus Codes.  
   - Performs GIS spatial lookup (township, municipality).  
   - Produces normalized entities.

6. **Entity Upsert Engine v5.x**  
   - Writes normalized entities to the graph and TSVs.

------------------------------------------------------------
# 4. INPUTS AND OUTPUTS

## 4.1 Inputs

The GPS Acquisition Module v5.0 consumes:

- **Partially resolved entities** from Resolution v5.x Pass 1:
  - Access Points with missing or blank `gps_lat_raw` / `gps_lon_raw`.
  - Sites with missing or blank `gps_lat_raw` / `gps_lon_raw`.
  - Optional: Trails / Segments / Networks if configured.

- **Context fields**:
  - `name_raw`
  - `location_raw` (address or description)
  - `counties_raw`
  - `urls_raw` (for authoritative pages and maps)
  - `identity_parent_entity_id` (for Access Points)
  - Parent entity attributes (for AP context checks)

- **External resources** (not part of this module’s spec, but required operationally):
  - Authoritative websites (park districts, agencies, etc.).
  - Authoritative GIS datasets (for visual verification).
  - Geocoding services (if allowed by policy).
  - Internal tools for manual verification.

## 4.2 Outputs

The module produces:

- Updated entities with:
  - `gps_lat_raw` (string or numeric, raw form)
  - `gps_lon_raw` (string or numeric, raw form)
  - Optional `plus_code_raw` (if you choose to precompute here; otherwise leave to Normalization)

- **GPS provenance metadata**, including:
  - acquisition_method
  - source_url (if applicable)
  - acquisition_timestamp
  - verifier (human or automated)
  - confidence_level
  - notes (optional)

- **Flags**:
  - `gps_acquisition_status`:
    - "acquired"
    - "verified"
    - "unresolved"
    - "ambiguous"
  - `gps_requires_manual_review` (boolean)

These outputs are fed into:

- Resolution v5.x Pass 2 (for Access Points).
- Normalization v5.x (for all entities).

------------------------------------------------------------
# 5. ACQUISITION WORKFLOW

## 5.1 Target Selection

The module must first select entities eligible for GPS acquisition:

- **Access Points**:
  - `entity_type == "access_point"`
  - `gps_lat_raw` and/or `gps_lon_raw` is null/blank
  - `identity_parent_entity_id` is present (from Resolution Pass 1)
  - `counties_raw` is present

- **Sites**:
  - `entity_type == "site"`
  - `gps_lat_raw` and/or `gps_lon_raw` is null/blank
  - `counties_raw` is present
  - `location_raw` or `urls_raw` provides enough context

- **Optional others** (if configured):
  - Trails, Segments, Networks with missing GPS, if point representatives are desired.

Entities that do not meet minimum context requirements (e.g., no county, no name) must be flagged as `gps_acquisition_status = "unresolved"` and not processed further.

## 5.2 Acquisition Methods (Ranked)

The module may use multiple acquisition methods, in a ranked order of authority. A typical order:

1. **Authoritative site/trail/AP page**  
   - Directly published coordinates on an official page.
   - Highest authority.

2. **Authoritative map or PDF**  
   - Coordinates embedded in official maps.
   - Requires careful extraction and verification.

3. **Authoritative GIS dataset**  
   - Point or centroid from an official GIS layer.
   - Must match entity name and county.

4. **Address geocoding** (if allowed)  
   - Geocode `location_raw` using a geocoding service.
   - Must be verified against county and parent context.

5. **Manual verification**  
   - Human uses map tools to drop a point at the correct location.
   - Must be explicitly flagged as manually verified.

Each acquired coordinate must record which method was used.

## 5.3 Verification Rules

Every acquired coordinate must be checked against:

- **Numeric validity**:
  - lat in [-90, 90]
  - lon in [-180, 180]

- **County consistency**:
  - The coordinate must fall within one of the entity’s `counties_raw` (using GIS).
  - If it falls outside all listed counties:
    - Flag as `gps_requires_manual_review = true`.
    - Optionally mark `gps_acquisition_status = "ambiguous"`.

- **Parent consistency (Access Points)**:
  - For APs, the coordinate must be spatially plausible relative to the parent entity:
    - Within a reasonable distance of the parent Site or Trail geometry (if available).
    - If the AP is clearly far from its parent:
      - Flag as `gps_requires_manual_review = true`.
      - Optionally mark `gps_acquisition_status = "ambiguous"`.

- **Duplicate detection**:
  - If multiple acquisition methods yield different coordinates:
    - Prefer the highest‑authority method.
    - Record all candidates in GPS provenance.
    - Flag as `gps_requires_manual_review = true` if differences are large.

The module must not:

- Snap coordinates to geometry.
- Adjust coordinates to “fit” counties.
- Infer corrections.

It may only **accept or flag**.

## 5.4 Acceptance Criteria

A coordinate may be accepted when:

- It is numerically valid.
- It lies within at least one of the entity’s `counties_raw` (or within configured tolerance of a county boundary).
- For Access Points, it is spatially plausible relative to the parent entity.
- No higher‑authority conflicting coordinate exists.

When accepted:

- Set `gps_lat_raw` and `gps_lon_raw`.
- Set `gps_acquisition_status = "acquired"` or `"verified"` (depending on process).
- Record full GPS provenance.

If not accepted:

- Leave `gps_lat_raw` / `gps_lon_raw` blank.
- Set `gps_acquisition_status = "unresolved"` or `"ambiguous"`.
- Set `gps_requires_manual_review = true` if human intervention is needed.

------------------------------------------------------------
# 6. PROVENANCE MODEL

Every GPS acquisition event must produce a provenance record attached to the entity’s metadata block (or a dedicated GPS provenance block), including:

- **acquisition_method**:
  - "authoritative_page"
  - "authoritative_map"
  - "authoritative_gis"
  - "geocoding"
  - "manual"
  - "other"

- **source_url** (if applicable):
  - The URL of the page or map used.

- **source_dataset** (if GIS):
  - Name of the GIS layer.

- **acquisition_timestamp**:
  - ISO 8601 timestamp.

- **acquired_lat_raw / acquired_lon_raw**:
  - The raw values obtained.

- **accepted** (boolean):
  - Whether this coordinate was accepted as `gps_lat_raw` / `gps_lon_raw`.

- **confidence_level**:
  - "high" | "medium" | "low"

- **verifier**:
  - "automated" or human identifier.

- **notes** (optional):
  - Free‑text explanation for ambiguous or manually adjusted cases.

Provenance must be:

- Immutable once written (new acquisitions append, not overwrite).
- Fully auditable.
- Available to Normalization and downstream review tools.

------------------------------------------------------------
# 7. ACCESS POINT–SPECIFIC RULES

Access Points are the highest‑priority target for GPS acquisition.

### 7.1 Preconditions

An Access Point is eligible for GPS acquisition if:

- `entity_type == "access_point"`.
- `identity_parent_entity_id` is present (from Resolution Pass 1).
- `counties_raw` is present.
- `gps_lat_raw` / `gps_lon_raw` are blank or missing.

### 7.2 Parent Context

The module may use:

- Parent Site or Trail name.
- Parent geometry (if available).
- Parent county set.

to:

- Narrow search.
- Verify plausibility of coordinates.
- Flag outliers.

### 7.3 Identity Implications

After GPS acquisition:

- Access Points must be re‑submitted to **Resolution v5.x Pass 2**.
- Pass 2 applies the full AP identity anchor:
  - `identity_parent_entity_id`
  - GPS proximity bucket (lat/lon rounded to 3 decimals)

This ensures:

- APs are correctly deduplicated.
- AP identity is spatially grounded.
- AP clusters are correct before Normalization.

------------------------------------------------------------
# 8. INTEGRATION WITH RESOLUTION AND NORMALIZATION

## 8.1 With Resolution v5.x

- **Input**: Partially resolved entities from Pass 1.
- **Output**: Updated entities with GPS for APs and Sites.
- **Next step**:
  - Access Points → Resolution v5.x Pass 2.
  - Sites (and others) → Normalization v5.x.

Resolution must treat GPS‑updated APs as new candidates for identity matching in Pass 2.

## 8.2 With Normalization v5.x

Normalization v5.x is responsible for:

- Validating `gps_lat_raw` / `gps_lon_raw` as numeric `gps_lat` / `gps_lon`.
- Rejecting or warning on invalid coordinates.
- Computing Plus Codes from validated GPS.
- Performing GIS spatial lookup for township and municipality.
- Recording normalization‑time GPS provenance (validation results, errors, etc.).

The GPS Acquisition Module must not:

- Perform numeric validation beyond basic sanity checks.
- Compute final Plus Codes (unless you explicitly choose to precompute `plus_code_raw` as a raw field).
- Perform GIS spatial joins.

------------------------------------------------------------
# 9. ERROR HANDLING AND REVIEW

## 9.1 Non‑Fatal Issues (Warnings)

- Coordinate acquired but outside expected county (within tolerance).
- Multiple candidate coordinates with small differences.
- Geocoding result with low confidence.
- Parent proximity slightly outside expected range.

→ Mark `gps_acquisition_status = "ambiguous"` or `"acquired"` with `confidence_level = "medium"` or `"low"`.  
→ Set `gps_requires_manual_review = true` if human review is recommended.

## 9.2 Fatal Issues (Unresolved)

- No coordinate can be acquired with acceptable confidence.
- All candidate coordinates fail county or parent consistency checks.
- Acquisition methods fail (e.g., no authoritative sources found).

→ Leave GPS blank.  
→ Set `gps_acquisition_status = "unresolved"`.  
→ Optionally add entity to a **GPS Review Queue** for manual work.

## 9.3 Manual Review Queue

For entities requiring manual intervention, the module should emit:

- Entity ID and type.
- Current name, county, parent (if AP).
- All candidate coordinates with provenance.
- Reason for review (e.g., "outside county", "conflicting sources").

Manual reviewers can then:

- Select a coordinate.
- Adjust a coordinate.
- Reject all candidates.

Their decision is recorded as a new GPS acquisition event with `acquisition_method = "manual"`.

------------------------------------------------------------
# 10. VERSIONING

- This module is **GPS Acquisition Module v5.0**.
- Any change to acquisition methods, verification rules, or provenance structure requires v5.1, v5.2, etc.
- Entity‑specific GPS policies (e.g., “Trails get centroids”) may be versioned separately in per‑entity GPS policy documents.

------------------------------------------------------------
# END OF GPS ACQUISITION MODULE v5.0