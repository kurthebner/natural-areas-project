---
name: na-pipeline
description: Executes the Natural Areas Project pipeline after discovery — resolution, normalization, GPS acquisition, TSV output, and database upsert. Triggers on resolve, normalize, generate TSV, upsert, pipeline, or post-discovery processing.
---

# Natural Areas Project — Pipeline Skill v5.4

Executes all post-discovery pipeline stages: Resolution → Normalization → GPS Acquisition → TSV Output → Vocabulary Validation → TSV Integrity Check → Database Upsert.

## Pipeline Overview

```
Raw Discovery Records (staging file)
        ↓
Stage 1: Resolution Engine
        ↓
Stage 2: Normalization Engine
        (2a: Read vocabulary modules FIRST)
        (2b: Normalize all fields)
        (2c: Map features_raw → controlled vocab features)
        ↓
Stage 3: GPS Acquisition Module  (for entities with blank GPS)
        ↓
Stage 4: TSV Output  (six files, one per entity type)
        ↓
Stage 4.5: Vocabulary Validation Gate  ← halts on any violation
        ↓
Stage 5: TSV Integrity Check
        ↓
Stage 6: Database Upsert
```

## Stage 1 — Resolution Engine

Transforms raw discovery records into resolved entities by detecting identity, merging duplicates, and preserving conflicts.

**Five phases:**
1. **Grouping** — partition records by `(entity_type, county_primary)`
2. **Identity Matching** — apply anchors and similarity scoring
3. **Merge Decisions** — form clusters above MERGE_THRESHOLD; flag review sets
4. **Field-Level Merging** — merge raw values using deterministic strategies
5. **Parent Resolution** — resolve parent names to IDs; preserve lineage metadata

**Key rules:**
- Resolution is purely mechanical — it does not normalize, infer, or choose between conflicting values
- All raw values are preserved exactly
- Conflicts are recorded, not resolved — Normalization resolves them
- Multi-county records are placed in all relevant county groups
- Resolution does not modify raw metadata

**Field merge strategies:**
- `choose_or_conflict` — name, location, organizational fields
- `union` — counties, URLs, partner agencies
- `conflict` — GPS lat/lon, lengths, acreage
- `metadata_union` — all metadata blocks
- `parent_resolution` — parent_*_raw lists

Reference: `na_resolution_engine_v5.4.md`, `na_resolution_rules_v5.3.md`

## Stage 2 — Normalization Engine

Transforms resolved entities into normalized entities ready for TSV output and database upsert.

### 2a — Read Vocabulary Modules Before Writing Any Normalization Code

Before writing any normalization logic, read the current vocabulary module files:

- `vocabularies/na_site_vocabulary_v5.5.md` — category (18 values), subtype (category-dependent lists), designation, status, and features
- `vocabularies/na_trail_vocabulary_v5.1.md` — use type, surface type, origin type, status, difficulty
- `vocabularies/na_access_point_vocabulary_v5.2.md` — access point type, status

**Code imports**: All controlled vocabulary sets (ALLOWED_CATEGORIES, ALLOWED_SUBTYPES, ALLOWED_FEATURES, etc.) are codified in `utilities/na_vocab_constants.py`. Import from there rather than transcribing values manually into pipeline scripts. Reading the vocabulary markdown files is still required — the constants encode what values are allowed, but the §7.x normalization mapping tables (raw term → canonical value) live only in the markdown and are essential for normalization decisions.

This is not optional research — it is the source of truth for every controlled value the normalization code will assign. The failure mode when you skip this step is that you invent plausible-sounding values ("City Park", "Private Reserve", "Riparian", "Conservancy Preserve") that feel reasonable but are not in the vocabulary and will fail the Stage 4.5 gate. Every controlled field assignment must trace directly to a value found in one of these files.

Pay particular attention to:
- **§7.x normalization mappings in the site vocabulary** — the tables that map raw discovery terms to correct values (e.g., "Community Park" → "Neighborhood Park", "natural feature" → "Natural Area", "Wildlife Area" subtype → "State Wildlife Area"). These mappings exist precisely because discovery captures informal terms that need remapping.
- **Category-specific subtype lists (§3.2)** — subtypes are not global; each category has its own permitted list. A subtype valid for Nature Preserve is not valid for Park. If a raw subtype value is not in the list for that category, null it or apply the normalization mapping — never leave an out-of-vocabulary value in place.
- **IMP-065 subtype inference rules (§7.4)** — deterministic inference is permitted for Nature Preserve, Water Site, Recreation Facility, and Campground when subtype is blank after vocabulary validation.
- **IMP-063 FATAL REJECT rule** — any category value with no valid mapping must halt normalization for that entity, not silently pass through.

### 2b — Key Normalizations

- Schema validation against Schema Modules v5.x
- Vocabulary normalization against Vocabulary Modules v5.x (see 2a above)
- County normalization: semicolon-delimited, alphabetized, "County" suffix stripped
- GPS validation: parse to numeric, validate ranges, round to 6 decimal places
- Plus Code computation from validated GPS — use `from na_plus_code import encode_plus_code` (direct import only; never call `na_plus_code.py` via subprocess — the module's self-test block runs on subprocess execution and pollutes stdout). See GPS Acquisition Module v5.2 §5.6.
- GIS spatial lookup: derive `township` and `municipality` from GPS coordinates
- GPS county check (IMP-067): cross-check `counties` field against county derived from GPS point-in-polygon (TIGER COUSUB, HIGH/MED confidence only); mismatch → `manual_review_queue` with `flag='county_mismatch'`; entity continues to output with existing counties value. See Site Normalization Contract v5.10 §5.17b for full logic and manual review options.
- Integrity anchor dedup check against current run and existing graph entities
- Parent/child validation

### 2c — Features Normalization (Sites)

The `features` TSV column is controlled vocabulary — every semicolon-delimited value must be a term from the site vocabulary §6.2 feature list. Raw discovery text belongs in `features_raw` (a DB-only column) and must never pass through to the TSV `features` column unchanged.

The normalization step for features is a **mapping operation**, not a passthrough:

1. Build a pattern list that maps raw text patterns to canonical vocabulary terms (e.g., `"splash pad"` → `"Spray Park"`, `"ada accessible"` → `"ADA Accessible"`, `"3 pavilions (rentable)"` → `"Pavilion"`, `"hiking trails"` → `"Hiking Trail"`)
2. For each entity, scan `features_raw` against the pattern list
3. Emit only the matched canonical terms as the `features` value
4. Anything in `features_raw` that has no vocabulary match is dropped from `features` — it remains in `features_raw` for reference

The result must be a semicolon-delimited set of exact vocabulary terms, or blank. Never a mix of vocabulary terms and free text.

**Per-entity routing:**
- Sites: category, subtype, designation, features (vocab mapping, see 2c), GPS, Plus Code, GIS, Derived Label
- Trails: use type, surface type, origin type, difficulty, maps URL list, identity notes
- Trail Segments: segment type, surface type, difficulty, geometry, maps URL list, identity notes
- Trail Networks: network type, member trail IDs validation, maps URL list, identity notes
- Site Networks: network type, member site IDs validation, identity notes
- Access Points: type, features (free text — AP vocabulary §1 explicitly has no controlled vocabulary for AP features), GPS (required), Plus Code, GIS, Derived Label, identity notes

**Note**: Derived Label is computed for Sites and Access Points only. It is a human-readable display string derived from name + category + subtype; it is not a controlled vocabulary field.

### Held-Entity Child Rule (IMP-086)

After the held entities list is finalized during normalization, scan all child entities for parent references pointing to a held entity:

**Access Points:** Any access point whose `parent_entity_id` references a held entity is itself held — move it to `held_entities` with `hold_reason = "parent_held"`. The hold detail must reference the parent's `entity_id`.

```python
held_ids = {e["entity_id"] for e in held_entities}
for ap in access_points:
    if ap.get("parent_entity_id") in held_ids:
        held_entities.append({
            "record_id": ap["ap_id"],
            "entity_type": "Access Point",
            "name": ap["name"],
            "hold_reason": "parent_held",
            "hold_detail": f"Parent entity {ap['parent_entity_id']} is held pending cross-county resolution",
            "county": ap["county_primary"],
            "run_id": RUN_ID,
        })
        access_points.remove(ap)
```

**Child Sites:** Any child site whose `parent_site_id` references a held site is itself held — move it to `held_entities` with `hold_reason = "parent_held"`.

**Trail Networks:** `member_trail_ids` referencing held trails remain in the network record (the network is not held). Log as `INFO` — the dangling member reference will resolve when the cross-county run completes. Do not log as `WARNING`.


## Stage 3 — GPS Acquisition Module

For every entity with blank GPS after normalization, attempt GPS acquisition before TSV output.

**Priority order:**
1. Official agency website (most reliable — exact park address)
2. Google Maps / mapping service search by name + municipality + state
3. mypacer.com or trail databases (for trails)
4. Approximate from aerial imagery / map centroid (LOW confidence)
5. Leave blank with `NONE` confidence if unresolvable

**Confidence levels:** `HIGH` (confirmed address/geocode), `MED` (approximate from map), `LOW` (centroid-level), `NONE` (not acquired)

Round all coordinates to 6 decimal places. Validate ranges: lat 24–50, lon -130 to -65 (continental US).

### Nominatim Rural Address Fallback Protocol (IMP-081)

Rural Ohio road addresses (county roads, township roads) frequently fail Nominatim or return suspicious geocodes. Before falling back to LOW confidence, try at least two alternate query formats:

1. **Drop street address** — query as `"[Park Name], [nearest city or village], Ohio"` (e.g., `"Penney Nature Center, Defiance, Ohio"`)
2. **County-anchored query** — query as `"[Park Name], [County Name] County, Ohio"` (e.g., `"Penney Nature Center, Defiance County, Ohio"`)

Accept the first result that passes the county bounding box check (below). Only fall back to LOW confidence if both alternates also fail or are rejected by the bounding box check.

### County-Level Bounding Box Sanity Check (IMP-081)

After any Nominatim geocode, **validate the returned coordinate against the county's approximate bounding box** before accepting it. This catches cases where Nominatim returns a plausible-looking but wrong-county result — a silent failure mode where the coordinate passes range validation (lat 24–50, lon -130 to -65) but is nowhere near the county.

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

Include `COUNTY_CENTROID = (lat, lon)` as a named constant in every county pipeline script, alongside `RUN_ID` and `PREFIX`. The centroid is available from the county's session log header or from the TIGER county centroid data.

### Large-County GPS Timeout Protocol (IMP-083)

Counties with 100+ sites missing GPS at Stage 3 start routinely exceed the 45-second bash execution limit. Nominatim calls alone (e.g., 21 calls × 1.1 s minimum) plus the `add_gis_lookup` pass over all sites can push total execution past 45 s. A timeout mid-GPS-pass commits a **partially GPS-populated entity set** to the database, requiring a SQL repair pass.

**Prevention — pre-seed known GPS values:**

After any successful GPS acquisition run, add the confirmed coordinates to the county script's `GPS_FALLBACKS_TEMPLATE` dict as MED-confidence fallbacks. Pre-seeded values are applied immediately in Stage 3a (fill-forward) and never re-queried via Nominatim:

```python
GPS_FALLBACKS_TEMPLATE = {
    # entity_id: (lat, lon, confidence, method)
    "VNW-S-0042": (40.871234, -84.583210, "MED", "nominatim_confirmed"),
    "VNW-S-0107": (40.912456, -84.601890, "MED", "nominatim_confirmed"),
    # ... add each confirmed result here after the acquisition run
}
```

**Prevention — `--skip-nominatim` flag:**

Once all expected GPS values are pre-seeded, pass `--skip-nominatim` to the county pipeline. Stage 3 will apply fill-forward from `GPS_FALLBACKS_TEMPLATE` and skip the live Nominatim query loop entirely, keeping total Stage 3 execution well under 45 s regardless of county size.

```bash
python van_wert_oh_pipeline.py --skip-nominatim
```

With IMP-082 fixed, `acquire_gps` can be called normally in the `--skip-nominatim` path — the earlier Lucas County workaround of bypassing `acquire_gps` entirely is **not** the pattern for new scripts.

**Recovery — SQL repair path for partial commits:**

If a timeout occurs mid-GPS-pass and a partial commit has already been written to the DB:

1. Identify GPS-null rows in the live DB:
```sql
SELECT site_id, name FROM sites WHERE gps_lat IS NULL AND county = 'Van Wert';
```

2. Apply fallback coordinates via targeted UPDATE for each affected row:
```sql
UPDATE sites SET gps_lat = 40.871234, gps_lon = -84.583210,
    gps_confidence = 'MED', gps_acquisition_method = 'nominatim_confirmed'
WHERE site_id = 'VNW-S-0042';
```

3. Regenerate the sites TSV from the repaired DB (do not re-run the full pipeline — the DB is now the source of truth):
```python
python utilities/export_sites_tsv.py --county "Van Wert" --output van_wert_sites.tsv
```

4. Document in the session log Errors and Fixes table:
```
| GPS timeout mid-pass | Stage 3 bash call timed out at 45 s; N sites partially updated | Applied GPS fallbacks via SQL UPDATE; sites TSV regenerated from DB |
```

## Stage 4 — TSV Output

Write six TSV files, one per entity type. Files with zero entities still get written (header row only).

Sites TSV columns: `name, category, subtype, designation, status, ownership, governance, partner_agencies, coordination, description, location, acres, counties, municipality, township, gps_lat, gps_lon, plus_code, features, notes, url_primary, urls, parent_site_id, created_at, updated_at`

Note: `site_id` and `features_raw` are DB-only — they do not appear in the TSV.

## Stage 4.5 — Vocabulary Validation Gate

**Halts the pipeline on any violation.** Must validate ALL of the following:
- Every `category` value is in the 18-value site vocabulary §2.1 list
- Every `subtype` value is in the permitted list for its category (§3.2)
- Every `designation` value is in the designation vocabulary (§4.x)
- Every `status` value is in the status vocabulary (§7.5)
- **Every `features` value is in the §6.2 allowed features list** ← gap identified Fulton County 2026-04-13: this check was missing and 18 violations passed undetected. Always include this check.

```python
for site in sites:
    for term in site["features"].split(";"):
        term = term.strip()
        if term and term not in ALLOWED_FEATURES:
            raise ValueError(f"Invalid features term: '{term}' on {site['site_id']}")
```

## Stage 5 — TSV Integrity Check

Non-halting; log warnings for review:
- Sites with GPS: report count and names of any missing GPS
- All `parent_site_id` references resolve to a known `site_id` in this run or the DB
- No duplicate entity IDs within run
- Held entities: confirm each HELD_ID has a corresponding held_entities record

## Stage 6 — Database Upsert

### Required DDL Table Groups (IMP-087)

Every generated upsert script must include `CREATE TABLE IF NOT EXISTS` DDL for all three table groups, not just primary entity tables. A missing table group causes schema conformance failure post-upsert.

**Primary entity tables** (already standard):
`sites`, `trails`, `trail_segments`, `trail_networks`, `site_networks`, `access_points`

**Relationship tables** — required in every script:
`site_parent`, `trail_to_segment`, `trail_network_members`, `site_network_members`, `access_point_parents`

**Operational tables** — required in every script:
`held_entities`, `manual_review_queue`, `entity_conflicts`, `entity_uncertainty`, `entity_geometry`

**Provenance tables** — required in every script:
`run_metadata`, `discovery_provenance`, `resolution_provenance`, `normalization_provenance`

Provenance logging must populate these tables during the run — do not defer provenance writes to a post-run step.


Upsert all entities into `natural_areas_v5.db` using `ON CONFLICT DO UPDATE`.

**Correct DB schema column names** — verified against live DB 2026-04-13; use these exactly:

`run_metadata`:
```python
INSERT OR IGNORE INTO run_metadata
  (run_id, county, state, run_date, records_input, normalized, held, notes, created_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
```

`held_entities`:
```python
INSERT OR IGNORE INTO held_entities
  (record_id, entity_type, name, hold_reason, hold_detail, county, run_id, created_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
```

> ⚠️ Do not use `pipeline_version`, `entity_id`, or `entity_name` — these columns do not exist in the live schema.

## Canonical Feature Mapper

Use as the starting point for every county pipeline. Extend with county-specific patterns as needed.

```python
FEATURE_MAP = [
    # hiking / walking
    (r'hiking trail|walking trail|walking path|winding trail|nature trail|loop trail|trail system|interpretive trail|self.guided interpretive', "Hiking Trail"),
    (r'boardwalk',                   "Boardwalk"),
    (r'interpretive trail|self.guided interpretive', "Interpretive Sign"),
    (r'bridle trail|equestrian',     "Bridle Trail"),
    # water
    (r'boat ramp|launch ramp',       "Boat Ramp"),
    (r'boat launch|watercraft|canoe|kayak', "Watercraft Access"),
    (r'fishing pond|fishing lake',   "Fishing Area"),
    (r'fishing pond',                "Pond"),
    (r'swimming beach|swim beach',   "Swimming Beach"),
    (r'swimming pool|city pool',     "Swimming Pool"),
    (r'splash pad|spray pad',        "Spray Park"),
    # picnic / shelter
    (r'pavilion|shelter house|open air pavilion|rentable.*shelter|covered seating', "Pavilion"),
    (r'picnic area|picnic spot|picnic table', "Picnic Area"),
    (r'gazebo',                      "Gazebo"),
    # sports
    (r'baseball|softball',           "Ball Diamond"),
    (r'basketball court',            "Basketball Court"),
    (r'tennis court',                "Tennis Court"),
    (r'pickleball court',            "Pickleball Court"),
    (r'volleyball court|sand volleyball', "Volleyball Court"),
    (r'soccer field|soccer complex', "Soccer Pitch"),
    (r'football field',              "Football Field"),
    (r'disc golf',                   "Disc Golf Course"),
    (r'skate park|skate ramp',       "Skate Park"),
    (r'miniature golf',              "Mini Golf"),
    # recreation
    (r'playground|play equipment',   "Playground"),
    (r'sledding hill',               "Sledding Hill"),
    (r'horseshoe',                   "Horseshoe Pitch"),
    (r'archery',                     "Archery Range"),
    (r'ropes course|high ropes',     "Ropes Course"),
    (r'shooting sports|shooting range', "Shooting Range"),
    (r'dog park',                    "Dog Park"),
    # amenities
    (r'restroom|flush toilet|portable toilet|bathroom', "Restrooms"),
    (r'parking',                     "Parking Lot"),
    (r'kiosk|information kiosk',     "Kiosk"),
    (r'camping|campsite',            "Camping"),
    (r'cabin|camper cabin|yurt',     "Cabin Rentals"),
    (r'ADA.compliant|ADA accessible|wheelchair', "ADA Accessible"),
    # natural
    (r'observation deck',            "Observation Deck"),
    (r'vernal pool',                 "Vernal Pool"),
    (r'hunting area|public hunting', "Hunting Area"),
    (r'wildlife viewing|wildlife.*observation', "Wildlife Observation Area"),
    # historical
    (r'historic.*depot|train depot|caboose|railroad artifact', "Historic Structure"),
    (r'war memorial|memorial statue|monument|WWI|military monument', "Monument"),
    # educational / farm
    (r'nature center|nature lab',    "Nature Center"),
    (r'guided.*tour|wagon tour|tractor.*tour', "Guided Tours"),
    (r'farm store|bison.*store',     "Farm Store"),
    # misc
    (r'pollinator garden',           "Pollinator Garden"),
]
```

**No vocabulary equivalent — leave in `features_raw` only:** Concession Stand, Dump Station, Water Frontage (IMP-038)

## Session Log Updates

Update `{county}_{state}_session_log.md` (see `na_session_log_template_v1.md`) as the pipeline runs:

- **After Stage 2 (Normalization)**: Fill in `records_normalized`, `records_held`, and the held entities table. Record any vocabulary violations or FATAL REJECT events in the Errors and Fixes table.
- **After Stage 3 (GPS Acquisition)**: Fill in `gps_acquired`, `gps_high`, `gps_med`, `gps_low`, `gps_none`. Record any Nominatim failures, bounding box rejections, or timeout events in the Errors and Fixes table.
- **After Stage 4 (TSV Output)**: Note TSV file counts per entity type.
- **After Stage 4.5 (Vocabulary Validation Gate)**: Record any gate halts and the specific violations that triggered them.
- **After Stage 6 (Database Upsert)**: Fill in `records_upserted`. Confirm run_metadata row written. Note any schema errors.
