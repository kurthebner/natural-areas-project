# GPS ACQUISITION MODULE v5.4
Authoritative GPS Collection and Verification Layer
Natural Areas Project — v5.x Pipeline

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- **IMP-132**: Added §5.9 ODNR Ohio Lake Map Resource — named authoritative GIS source for
  ODNR Division of Wildlife fishing lakes and wildlife area centroids (ArcGIS Experience
  `2a39044c75b04e68872564b4c6ec0638`). Updated §5.2 step 3 with pointer to §5.9.
  Added `"odnr_lake_map"` to §6 Provenance Model acquisition_method values.
- **IMP-133**: Added §5.9 SORP (State-Owned Real Property) — cross-agency Ohio state parcel
  dataset as GPS fallback for any Tier 2 entity not resolvable via MORPC, ODNR Lake Map, OSM,
  or Nominatim. Documents ArcGIS Export Tool URL and project CSV asset. Updated §5.2 step 3
  with pointer to §5.9. Added `"sorp_gis"` to §6 Provenance Model acquisition_method values.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- **IMP-069 — GPS Unresolvable Flag**: Added §7 defining the `gps_unresolvable` flag — its
  qualifying criteria, required documentation, and pipeline behavior. This flag allows sites
  with genuinely unresolvable GPS (linear corridors, multi-parcel distributed preserves with
  no centroid, etc.) to proceed past the Stage 3c GPS Gate without holding indefinitely.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **IMP-031 — GPS preservation on pipeline re-run**: Added §3a GPS Fill-Forward,
  which runs before the acquisition workflow on every pipeline execution. Entities
  that already have GPS in the DB from a prior run have their GPS, Plus Code,
  township, and municipality carried forward rather than re-acquired. Only entities
  with no DB GPS proceed to the §5 acquisition workflow. Added "db_fill_forward" as
  a recognized acquisition_method value in §6 Provenance Model. Updated §3 pipeline
  position diagram to show the two-sub-step structure.
- **IMP-048 — `na_plus_code.py` correct import pattern documented**: Added §5.6
  with the mandatory import pattern. Calling the module as a subprocess pollutes
  stdout with self-test output; direct import is required.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- Added §5.5 MORPC Parks & Open Space Layer — designates the MORPC ArcGIS feature layer as the
  primary authoritative GIS source for Sites in the 15 Ohio counties covered by the MORPC
  regional planning area (FRA, FAI, DEL, PIC, LIC, MAD, UNI, ROS, KNO, FAY, MAR, MRW, HOC,
  LOG, PER). Achieved 96.4% GPS coverage for Franklin County without geocoding.
- Updated §5.2 Acquisition Methods to reference §5.5 for covered counties at step 3.
- Added "morpc_gis" as a recognized acquisition_method value in §6 Provenance Model.
- Updated §10 Versioning.

------------------------------------------------------------
# 1. PURPOSE

The GPS Acquisition Module v5.2 provides the authoritative, deterministic workflow for:

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

3. **GPS Acquisition Module v5.4**  ← **THIS MODULE**
   - **Step 3a — Fill-Forward**: reads existing GPS from DB for entities that already have it; carries GPS, Plus Code, township, and municipality forward without re-acquisition.
   - **Step 3b — Acquisition**: acquires GPS for entities with no DB GPS (APs and Sites primarily, optionally others).
   - Records GPS provenance for both fill-forward and newly acquired GPS.
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
# 3a. GPS FILL-FORWARD (IMP-031) ✨ NEW IN v5.2

Before any GPS acquisition workflow runs, the pipeline checks the DB for each entity
being processed. This step ensures that GPS data acquired in a previous pipeline run
is never overwritten by blank values when the pipeline is re-run.

## 3a.1 Purpose

Pipeline re-runs are common — new YAML records are added, normalization rules change,
or TSVs need to be regenerated. Without GPS preservation, every re-run would wipe
GPS coordinates, Plus Codes, and GIS-derived fields (township, municipality) that were
acquired through the MORPC layer, geocoder, or manual lookup in a prior run. This would
require re-running GPS acquisition after every pipeline execution.

GPS fill-forward makes the pipeline safe to re-run without data loss.

## 3a.2 Fill-Forward Logic

For each entity entering Stage 3:

1. Query the DB by entity ID (or by name + county if entity is new and has no ID yet).
2. If the DB record has non-blank `gps_lat` and `gps_lon`:
   - Carry forward: `gps_lat`, `gps_lon`, `plus_code`, `township`, `municipality`.
   - Record provenance: `acquisition_method: "db_fill_forward"` with the original
     acquisition source noted (see §6 Provenance Model).
   - **Do not submit this entity to the §5 acquisition workflow.**
3. If the DB record has blank GPS (or the entity is new with no DB record):
   - Submit to the §5 acquisition workflow as normal.

## 3a.3 Precedence Rules

When both YAML and DB provide GPS, YAML takes precedence:

| YAML GPS | DB GPS | Result |
|---|---|---|
| Present | Any | Use YAML GPS (authoritative source stated coordinates) |
| Blank | Present | Use DB GPS (fill-forward) |
| Blank | Blank | Submit to §5 acquisition |

If YAML GPS is present, the entity bypasses both fill-forward and acquisition —
the source-stated coordinates are authoritative and are validated by Normalization.

## 3a.4 Fields Preserved

The following fields are carried forward from DB when YAML GPS is blank:

- `gps_lat`, `gps_lon` — primary coordinates
- `plus_code` — derived from GPS; do not recompute if GPS unchanged
- `township` — GIS spatial lookup result; do not re-derive if GPS unchanged
- `municipality` — GIS spatial lookup result; do not re-derive if GPS unchanged

`acres` is **not** carried forward by this mechanism — acreage comes from discovery
sources and normalization, not GPS acquisition.

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
   - **For Sites in the 15 MORPC-covered Ohio counties**: use the MORPC Parks & Open Space
     layer as the primary GIS source at this step before attempting any other GIS source or
     geocoding. See §5.5 for the full MORPC protocol.
   - **For ODNR Division of Wildlife fishing lakes and wildlife areas (Ohio)**: use the ODNR
     Ohio Lake Map Resource ArcGIS Experience as a named authoritative GIS source. See §5.9.
   - **For any Ohio state-owned entity (Tier 2) not resolved by division-specific sources,
     MORPC layer, ODNR Lake Map, OSM, or Nominatim**: use the SORP parcel dataset as the
     authoritative fallback GIS source before declaring `gps_unresolvable`. See §5.9.

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

## 5.5 MORPC Parks & Open Space Layer — Primary Source for 15 Ohio Counties ✨ NEW IN v5.1

### Covered Counties

The MORPC (Mid-Ohio Regional Planning Commission) Parks & Open Space ArcGIS feature layer
covers the following 15 Ohio counties. For any county in this list, the MORPC layer is the
**primary GPS source** at acquisition step 3 (Authoritative GIS Dataset) for Sites, before
attempting address geocoding or manual verification:

| County Code | County Name |
|-------------|-------------|
| FRA | Franklin |
| FAI | Fairfield |
| DEL | Delaware |
| PIC | Pickaway |
| LIC | Licking |
| MAD | Madison |
| UNI | Union |
| ROS | Ross |
| KNO | Knox |
| FAY | Fayette |
| MAR | Marion |
| MRW | Morrow |
| HOC | Hocking |
| LOG | Logan |
| PER | Perry |

### Layer Reference

- **ArcGIS Hub Layer ID**: `d898fa77e91d414f8f296b0511f14fbf_11`
- **Acquisition**: Download the full layer (all 15 counties) as a project asset. Do NOT filter
  by county at download time. Apply county filter at match time. Store locally as
  `GIS_Assets/morpc_parks_open_space/morpc_parks_all_counties.csv` (or equivalent).
- **Proven coverage**: 96.4% GPS match rate for Franklin County with name-matching alone,
  no geocoding required.

### Name Matching Protocol

Name matching against MORPC layer records is **score-based** using a combined approach:

1. **Pre-normalization**: Before scoring, apply the "Parkland" → "Park" suffix normalization
   to the entity `name_raw` (see Site Normalization Contract §5.1). MORPC records use
   the "Park" form; CRP discovery records use "Parkland". Failing to normalize before
   scoring will cause avoidable match failures.

2. **Scoring**: Use a combined token-set ratio + distinctive-word bonus score:
   - Token-set ratio (e.g., difflib or similar) for general string similarity.
   - Bonus weight for matching on rare/distinctive words that strongly identify an entity.

3. **Thresholds** (validated against Franklin County):
   - Score ≥ 93: auto-match (no manual review needed).
   - Score 85–92: review queue — examine before accepting or rejecting.
   - Score < 85: no match; proceed to geocoding or manual verification.

4. **County filter at match time**: Only consider MORPC records whose county attribute
   matches the entity's `counties_raw`. This eliminates false positives from identically
   named parks in adjacent MORPC-covered counties.

5. **Manual overrides**: Maintain a county-specific override file (CSV or YAML) mapping
   entity IDs to MORPC feature IDs for cases where automated matching fails but the
   correct MORPC record is known. Overrides take precedence over scored matches.

### Provenance

When a coordinate is acquired from the MORPC layer, record:

- `acquisition_method`: `"morpc_gis"`
- `source_dataset`: `"MORPC Parks & Open Space — ArcGIS Hub d898fa77e91d414f8f296b0511f14fbf_11"`
- `match_score`: the numeric score used to accept the match
- `confidence_level`: `"high"` for score ≥ 93; `"medium"` for score 85–92

### Sites Not in the MORPC Layer

Some legitimate Sites will not appear in the MORPC layer (e.g., newly acquired parcels,
private conservancy lands, very small pocket parks). For these:

- Mark `gps_acquisition_status = "unresolved"` after MORPC lookup fails.
- Proceed to address geocoding (step 4) or manual verification (step 5).
- Do not mark a Site GPS-unresolvable solely because the MORPC layer lacks it.

------------------------------------------------------------
## 5.6 Utility: Plus Code Encoding (`na_plus_code.py`)

Plus Code computation is a Normalization stage responsibility (§8.2), but any pipeline
script that computes Plus Codes must use the project utility correctly.

### Location

```
utilities/na_plus_code.py
```

### Correct Usage — Direct Import Only

```python
import sys
sys.path.insert(0, '/path/to/Natural Areas Project v5/utilities')
from na_plus_code import encode_plus_code

plus_code = encode_plus_code(lat, lon)  # returns a 10-character Plus Code string
```

### ⚠️ PROHIBITED — Subprocess Call

```python
# NEVER do this:
result = subprocess.run(['python3', 'na_plus_code.py', str(lat), str(lon)], ...)
```

**Why:** `na_plus_code.py` contains a self-test block that runs when the module is
executed as `__main__`. Calling it via subprocess prints 7 lines of test output
to stdout, which pollutes batch script results and makes them unparseable.

The self-test is intentional (it verifies the implementation is correct), but it
is triggered only by subprocess-style execution. Direct import bypasses `__main__`
entirely, so no test output is emitted.

### Function Signature

```python
encode_plus_code(lat: float, lon: float) -> str
```

Returns a 10-character Open Location Code (Plus Code), e.g. `86FW8Q2F+WH`.
Input must be WGS84 decimal degrees. Raises `ValueError` for out-of-range inputs.

------------------------------------------------------------
## 5.7 Nominatim Rural Address Fallback Protocol (IMP-081)

Rural Ohio road addresses (county roads, township roads) frequently fail Nominatim or return
suspicious geocodes. Before falling back to LOW confidence, try at least two alternate query
formats:

1. **Drop street address** — query as `"[Park Name], [nearest city or village], Ohio"`
   (e.g., `"Penney Nature Center, Defiance, Ohio"`)
2. **County-anchored query** — query as `"[Park Name], [County Name] County, Ohio"`
   (e.g., `"Penney Nature Center, Defiance County, Ohio"`)

Accept the first result that passes the county bounding box check (§5.8). Only fall back to
LOW confidence if both alternates also fail or are rejected by the bounding box check.

## 5.8 County Bounding Box Sanity Check (IMP-081)

After any Nominatim geocode, **validate the returned coordinate against the county's approximate
bounding box** before accepting it. This catches cases where Nominatim returns a plausible-looking
but wrong-county result — a silent failure mode where the coordinate passes range validation but
is nowhere near the county.

```python
def within_county_bounds(lat, lon, county_centroid_lat, county_centroid_lon, buffer_deg=0.35):
    """±0.35° ≈ 25–30 miles in Ohio — wide enough for any in-county park,
    narrow enough to catch results placed in a neighboring county."""
    return (abs(lat - county_centroid_lat) <= buffer_deg and
            abs(lon - county_centroid_lon) <= buffer_deg)

# Add county centroid to each pipeline script's constants:
# COUNTY_CENTROID = (41.28, -84.38)  # Defiance County, OH example

if not within_county_bounds(result_lat, result_lon, *COUNTY_CENTROID):
    logger.warning(f"Nominatim result ({result_lat}, {result_lon}) outside county bounds — rejecting, trying alternate format")
    result = None  # fall through to next query format or LOW fallback
```

Include `COUNTY_CENTROID = (lat, lon)` as a named constant in every county pipeline script,
alongside `RUN_ID` and `PREFIX`. The centroid is available from the county's session log header
or from the TIGER county centroid data.

------------------------------------------------------------
## 5.9 Ohio State-Owned Property GIS Sources (IMP-132, IMP-133) ✨ NEW IN v5.4

Two Ohio state-maintained GIS sources are available for acquiring GPS coordinates for state
entities (Tier 2) that are not in OSM and not geocodable via Nominatim.

### ODNR Ohio Lake Map Resource

**URL:** `https://experience.arcgis.com/experience/2a39044c75b04e68872564b4c6ec0638`

**Coverage:** All ODNR Division of Wildlife–managed fishing lakes and associated access points
across Ohio.

**Use for:** DOW fishing lakes and wildlife area centroids whose names do not appear in OSM and
whose rural road addresses do not geocode reliably. Match entity name against the layer's
`SITE_NAME` attribute. Confirm the county field matches `counties_raw` before accepting.

**Not a substitute for:** ODNR division-specific listing pages (§3.1–§3.6 in the State Lands
sub-procedure). Use ODNR Ohio Lake Map for GPS acquisition, not entity enumeration.

**Provenance fields:**
- `acquisition_method`: `"odnr_lake_map"`
- `source_dataset`: `"ODNR Ohio Lake Map Resource — ArcGIS Experience 2a39044c75b04e68872564b4c6ec0638"`

---

### SORP — State-Owned Real Property

**ArcGIS Export Tool:**
```
https://experience.arcgis.com/experience/802e2079e2e4448e819cee71e4fefe92/page/State-Owned-Property-Data-Export-Tool
```

**Project asset:** `SORP_Parcels_2023.csv` (project root) — statewide snapshot; filter by county name or FIPS for targeted lookups.

**Coverage:** All Ohio state-owned parcels across all agencies (ODNR, OHC, ODOT, state
universities, and others). Parcel centroid coordinates are acceptable GPS representative points.

**Use for:** Any Ohio Tier 2 entity not resolvable via the MORPC layer (non-MORPC county),
ODNR Ohio Lake Map, OSM, or Nominatim. SORP is the last authoritative GPS fallback before
declaring `gps_unresolvable = true`. Particularly useful for:
- ODNR DOW wildlife areas with no usable street address
- OHC state memorials not indexed in OSM
- ODOT mitigation or scenic parcels with no place name in OSM
- State university holdings not in OSM

**Match protocol:** Filter `SORP_Parcels_2023.csv` by county and managing agency. Match on entity
name (partial matches are acceptable; SORP names are often abbreviated). Cross-check the candidate
parcel against the managing agency's website to confirm it is the correct entity before accepting
the coordinate.

**Provenance fields:**
- `acquisition_method`: `"sorp_gis"`
- `source_dataset`: `"SORP State-Owned Real Property — Ohio DAS/OGrIP 2023 (SORP_Parcels_2023.csv)"`
- Note the SORP data year in provenance; the 2023 CSV is the project's working copy.

------------------------------------------------------------
# 6. PROVENANCE MODEL

Every GPS acquisition event must produce a provenance record attached to the entity’s metadata block (or a dedicated GPS provenance block), including:

- **acquisition_method**:
  - "authoritative_page"
  - "authoritative_map"
  - "authoritative_gis"
  - "morpc_gis" ← MORPC Parks & Open Space layer (15 MORPC-covered Ohio counties; see §5.5)
  - "odnr_lake_map" ← ODNR Ohio Lake Map Resource ArcGIS Experience (DOW fishing lakes and wildlife areas; see §5.9)
  - "sorp_gis" ← State-Owned Real Property parcel dataset (all Ohio state agencies; see §5.9)
  - "geocoding"
  - "manual"
  - "db_fill_forward" ← GPS carried forward from a prior pipeline run (see §3a); original acquisition_method noted alongside
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
# 7. GPS UNRESOLVABLE FLAG (IMP-069)

## 7.1 Purpose

The `gps_unresolvable` flag allows a site entity to proceed through the Stage 3c GPS Gate
without having GPS coordinates, when GPS genuinely cannot be determined for the entity.
It is an explicit acknowledgment that GPS acquisition was attempted and failed for documented
reasons — not a placeholder for “GPS not yet attempted.”

## 7.2 Qualifying Criteria

`gps_unresolvable = true` may be set **only** when one or more of the following is true and
documented in `notes`:

| Criterion | Example | Notes Requirement |
|-----------|---------|-------------------|
| Linear corridor with no meaningful centroid | Long-distance rail trail, river section | Describe the extent and why no centroid applies |
| Multi-parcel distributed preserve with disjunct parcels | Land trust holding in 3 non-adjacent parcels | Describe parcel locations; note that no single coordinate represents the entity |
| Boundary defined by metes and bounds only; no authoritative polygon or point | Historic commons described in deed only | Note the documentation source and boundary description |
| Offshore or floating entity | Floating wetland restoration platform | Describe location context |
| Access controlled / coordinate disclosure restricted by agency policy | Some military reservations, sensitive wildlife sites | Cite the agency policy or restriction |

## 7.3 Not Qualifying

The following do NOT qualify for `gps_unresolvable = true`:

- GPS not yet looked up or attempted
- GPS lookup failed due to tool or network error
- Address is known but coordinates were not converted
- Discovery record was added late and GPS acquisition was skipped
- Uncertainty about which of two candidate coordinates is correct

These are pipeline errors or deferrals, not unresolvable situations. Entities in this state
must be held (`hold_reason = “gps_missing”`) until GPS is properly acquired.

## 7.4 Required Documentation

When `gps_unresolvable = true` is set, the entity's `notes` field must contain:
1. A plain-language explanation of why GPS cannot be obtained.
2. The date the determination was made.
3. A description of what GPS acquisition was attempted.

Example: `”GPS unresolvable — site is a distributed land trust holding in three non-adjacent
parcels; no single coordinate represents the entity. Boundary described by conservation easement
document only. Determined 2026-04-07 after reviewing ODNR GIS and county auditor parcel data.”`

## 7.5 Pipeline Behavior

- Entities with `gps_unresolvable = true` are excluded from the Stage 3b GPS acquisition workflow.
- They pass the Stage 3c GPS Gate and proceed to TSV Output without GPS coordinates.
- `plus_code`, `township`, and `municipality` will be blank for these entities (no GPS → no GIS derivation).
- These entities are **not** written to `held_entities`.
- They are upserted to the DB with null GPS and `gps_unresolvable = true` in their normalization provenance.

## 9.4 Large-County GPS Timeout Protocol (IMP-083)

Counties with 100+ sites missing GPS at Stage 2b routinely exceed the 45-second bash execution
limit. Nominatim calls alone (e.g., 21 calls × 1.1 s minimum) plus the `add_gis_lookup` pass
can push total execution past 45 s. A timeout mid-GPS-pass commits a partially GPS-populated
entity set to the database, requiring a SQL repair pass.

**Prevention — pre-seed known GPS values:**

After any successful GPS acquisition run, add confirmed coordinates to the county script's
`GPS_FALLBACKS_TEMPLATE` dict as MED-confidence fallbacks. Pre-seeded values are applied
immediately in Stage 2a (fill-forward) and never re-queried via Nominatim:

```python
GPS_FALLBACKS_TEMPLATE = {
    # entity_id: (lat, lon, confidence, method)
    "VNW-S-0042": (40.871234, -84.583210, "MED", "nominatim_confirmed"),
    "VNW-S-0107": (40.912456, -84.601890, "MED", "nominatim_confirmed"),
}
```

**Prevention — `--skip-nominatim` flag:**

Once all expected GPS values are pre-seeded, pass `--skip-nominatim` to the county pipeline.
Stage 2b will apply fill-forward from `GPS_FALLBACKS_TEMPLATE` and skip the live Nominatim
query loop entirely. With IMP-082 fixed, `acquire_gps` can be called normally in the
`--skip-nominatim` path — bypassing `acquire_gps` entirely is not the pattern for new scripts.

```bash
python van_wert_oh_pipeline.py --skip-nominatim
```

**Recovery — SQL repair path for partial commits:**

If a timeout occurs mid-GPS-pass and a partial commit has already been written to the DB:

1. Identify GPS-null rows in the live DB:
```sql
SELECT site_id, name FROM sites WHERE gps_lat IS NULL AND county = 'Van Wert';
```

2. Apply fallback coordinates via targeted UPDATE:
```sql
UPDATE sites SET gps_lat = 40.871234, gps_lon = -84.583210,
    gps_confidence = 'MED', gps_acquisition_method = 'nominatim_confirmed'
WHERE site_id = 'VNW-S-0042';
```

3. Regenerate the sites TSV from the repaired DB (do not re-run the full pipeline):
```python
python utilities/export_sites_tsv.py --county "Van Wert" --output van_wert_sites.tsv
```

4. Document in the session log Errors and Fixes table:
```
| GPS timeout mid-pass | Stage 2b timed out at 45 s; N sites partially updated | Applied GPS fallbacks via SQL UPDATE; TSV regenerated from DB |
```

------------------------------------------------------------
# 10. VERSIONING

- This module is **GPS Acquisition Module v5.4**.
- Any change to acquisition methods, verification rules, or provenance structure requires v5.4, v5.5, etc.
- Entity‑specific GPS policies (e.g., “Trails get centroids”) may be versioned separately in per‑entity GPS policy documents.
- County-specific GIS source documentation (e.g., §5.5 MORPC layer) is part of this module; adding a new regional source requires a version increment.
- Utility script usage notes (e.g., §5.6 Plus Code encoding) are part of this module; adding a new utility requires a version increment.

------------------------------------------------------------
# END OF GPS ACQUISITION MODULE v5.4