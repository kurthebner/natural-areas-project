# NATURAL AREAS PROJECT
# GPS ACQUISITION MODULE v6.0
Authoritative GPS Collection, Browser-Assisted Lookup, and Verification Layer
Natural Areas Project — v6.x Pipeline

This module supersedes GPS Acquisition Module v5.4.

------------------------------------------------------------
# CHANGES FROM v5.4 → v6.0

- **Single-pass acquisition for all entity types**: The v5 design ran GPS
  acquisition between Resolution Pass 1 and Pass 2 (which existed to re-run AP
  identity matching using GPS proximity). In v6.0, AP identity is based on entity
  ID rather than GPS proximity, so Resolution Pass 2 is eliminated. GPS acquisition
  now runs once, after Resolution, covering all four entity types in a single pass.

- **Browser-assisted acquisition elevated to primary method**: Claude in Chrome
  is a first-class GPS acquisition method — not buried under "manual." It covers
  ArcGIS Experience viewers, Google Maps detail cards, ArcGIS REST endpoints, and
  any web-based GIS tool. It is listed as Method 3 in the ranked acquisition order,
  immediately after authoritative source pages and GIS downloads.

- **Human-assisted acquisition formalized**: When automated methods fail and the
  browser does not surface a coordinate, Claude asks the user for help. The user
  may provide a Google Maps link, a coordinate pair, or a location description.
  This is a recognized acquisition method with its own provenance value.

- **Pipeline stage simplification**: v5 stages 2a/2b/2c/2d are collapsed into a
  single GPS Acquisition stage that covers fill-forward and acquisition together.
  The GPS Gate (hold entities without GPS) follows immediately.

- **Operational scaffolding removed**: v5 §9.4 (timeout/pre-seeding protocol)
  was implementation detail that does not belong in a specification module. Removed.

- **Entity types updated**: Trailthing replaces Trail/Trail Segment/Trail Network.
  GPS is optional for Trailthings (linear entities with no meaningful centroid
  typically use gps_unresolvable).

- **All v5.4 substantive rules carried forward**: MORPC layer protocol (§5.5),
  ODNR Lake Map Resource (§5.9), SORP fallback (§5.9), Nominatim rural address
  protocol (§5.7), county bounding box check (§5.8), fill-forward precedence
  (§3a), gps_unresolvable qualifying criteria (§7), Plus Code utility note (§5.6).

------------------------------------------------------------
# 1. PURPOSE

The GPS Acquisition Module v6.0 provides the authoritative workflow for:

- Acquiring GPS coordinates for entities that lack them
- Using browser-based tools (Claude in Chrome) as a primary acquisition method
- Providing a human-assisted acquisition path when automation fails
- Verifying acquired coordinates against county and parent context
- Recording GPS provenance with acquisition method and confidence level
- Preparing entities for GPS-dependent normalization (Plus Code, GIS lookup)

**GPS enables:**
- Plus Code computation (navigation)
- GIS spatial lookup for township and municipality
- GPS county cross-check (normalization integrity)
- Field visit planning (Audit Module §10)

**GPS is not used for entity identity in v6.0.** Entities are identified by name,
county, and parent relationships — not GPS proximity. This eliminates the need
for a second Resolution pass.

This module is a **collection + verification + provenance** layer. It does not
normalize GPS (that is Normalization's responsibility) or perform identity
matching.

------------------------------------------------------------
# 2. SCOPE

GPS acquisition applies to all four entity types:

- **Sites** — primary target; GPS is required for upsert (GPS Gate applies)
- **Access Points** — primary target; GPS is required for upsert (GPS Gate applies)
- **Trailthings** — optional; most are gps_unresolvable (linear corridors); point
  GPS is recorded when a representative trailhead or centroid is published
- **Site Networks** — optional; generally gps_unresolvable (multi-location);
  only acquire if a single authoritative point is explicitly published

GPS acquisition operates on entities that:
- Have passed the Resolution Engine v6.0
- Lack valid `gps_lat_raw` / `gps_lon_raw` (or have not been checked since last run)

------------------------------------------------------------
# 3. POSITION IN PIPELINE

```
Discovery → Resolution → GPS Acquisition (this module) → Normalization → Upsert
```

**Step 1 — Fill-Forward**: For each entity, check the DB for previously acquired
GPS. If found, carry it forward without re-acquiring. (See §4.)

**Step 2 — Acquisition**: For entities with no DB GPS and no source-stated GPS,
run the acquisition workflow. (See §5.)

**Step 3 — GPS Gate**: After acquisition, entities with no GPS and no
gps_unresolvable flag are routed to `held_entities` with
`hold_reason = "gps_missing"`. (See §8.)

**Step 4 — Normalization**: GPS is validated, Plus Code is computed, township and
municipality are derived via GIS spatial lookup.

------------------------------------------------------------
# 4. GPS FILL-FORWARD (IMP-031)

Before running any acquisition workflow, check the DB for each entity.

## 4.1 Fill-Forward Logic

For each entity entering this module:

1. Query the DB by entity ID.
2. If the DB record has non-blank `gps_lat` and `gps_lon`:
   - Carry forward: `gps_lat`, `gps_lon`, `plus_code`, `township`, `municipality`
   - Record provenance: `acquisition_method: "db_fill_forward"`
   - **Do not re-acquire.** Skip to §8 GPS Gate.
3. If the DB record has blank GPS (or the entity is new):
   - Check `gps_lat_raw` / `gps_lon_raw` in the raw discovery record.
   - If present → pass to Normalization directly (source-stated coordinates are
     authoritative; no acquisition needed).
   - If absent → proceed to §5 acquisition workflow.

## 4.2 Precedence Rules

| Source-stated GPS | DB GPS | Action |
|---|---|---|
| Present | Any | Use source-stated GPS — no acquisition needed |
| Absent | Present | Fill-forward from DB — no acquisition needed |
| Absent | Absent | Run acquisition workflow (§5) |

------------------------------------------------------------
# 5. ACQUISITION WORKFLOW

## 5.1 Ranked Acquisition Methods

Apply the following methods in order, stopping at the first successful acquisition.
Record the method used in GPS provenance (§6).

### Method 1 — Authoritative Source Page
The entity's official web page or a closely related authoritative page explicitly
states coordinates.

- Coordinates may appear as: lat/lon in a data table, embedded in a Google Maps
  link, in a "directions" section, in a GIS viewer URL, or in an API response.
- This is the highest-authority method. Accept without further verification beyond
  numeric range checks.
- Record: `acquisition_method: "authoritative_page"`

### Method 2 — Authoritative GIS Download
An official GIS dataset provides a point or centroid matching the entity.

**For Sites in the 15 MORPC-covered counties** (Franklin, Fairfield, Delaware,
Pickaway, Licking, Madison, Union, Ross, Knox, Fayette, Marion, Morrow, Hocking,
Logan, Perry): use the MORPC Parks & Open Space layer as the primary GIS source
before any other method. See §5.5 for the full MORPC protocol.

**For ODNR DOW fishing lakes and wildlife areas**: use the ODNR Ohio Lake Map
Resource ArcGIS Experience. See §5.9.

**For any Ohio state-owned entity (Tier 2) not resolved above**: use the SORP
parcel dataset as the authoritative fallback. See §5.9.

- Record: `acquisition_method: "authoritative_gis"` (or the specific method
  value per §6 for MORPC/ODNR/SORP sources)

### Method 3 — Browser-Assisted Lookup (Claude in Chrome)

**This is a primary acquisition method**, not a fallback. Claude in Chrome can
navigate web-based GIS tools and Google Maps to find coordinates that cannot be
obtained from static downloads.

**When to use:**
- The entity has an ArcGIS Online viewer, ArcGIS Hub page, or county GIS portal
  but no downloadable dataset
- The official page links to a Google Maps location
- The MORPC layer and other GIS downloads do not cover this entity
- The entity appears on Google Maps with a place card

**How to use:**

**Google Maps detail card:**
Navigate to `maps.google.com`, search for the entity by name and county. Click
into the entity's detail card. The page URL updates to:
`https://www.google.com/maps/place/.../@LAT,LON,ZOOMz/...`
Extract LAT and LON from the `@LAT,LON,ZOOMz` portion of the URL.

**ArcGIS Experience viewer:**
Navigate to the ArcGIS Experience URL. Click the entity's feature on the map.
Most ArcGIS viewers display feature attributes including coordinates, or the URL
updates with the map center. Use the viewer's coordinate display or "Get
Directions" link to extract the coordinate.

**ArcGIS REST endpoint:**
Query the feature layer REST endpoint directly for the entity's attributes.
Many ArcGIS layers return geometry in the JSON response:
`{rings: [...], x: LON, y: LAT}` (for projected coordinates, convert to WGS84)
or `{x: LON, y: LAT, spatialReference: {wkid: 4326}}` (already WGS84).

**County GIS portal or AuditorMap:**
Navigate to the county GIS or auditor parcel viewer, search for the parcel
by owner or name, click the parcel to view attributes. Many Ohio county portals
display centroid coordinates or allow copy of coordinates.

**Confidence level:** Browser-acquired coordinates from Google Maps detail cards
or ArcGIS viewers are typically HIGH confidence when the feature name matches
exactly. Record as `acquisition_method: "browser_lookup"`.

**Note:** Claude should actively use browser access during discovery as well
as GPS acquisition — not just for GPS. Whenever a web-based GIS viewer,
interactive map, or ArcGIS Experience is the only way to access authoritative
data, Claude in Chrome is the right tool.

### Method 4 — Address Geocoding (Nominatim)
Geocode `location_raw` using Nominatim or an equivalent geocoder.

For rural Ohio addresses, follow the fallback protocol in §5.7 (drop street
address → county-anchored query). Always apply the county bounding box check
(§5.8) to the result.

- Record: `acquisition_method: "geocoding"`
- Confidence: typically MEDIUM; LOW for rural fallback results

### Method 5 — OSM / Public Map Lookup
Search OpenStreetMap or a public map service for the entity by name and county.
Accept a point if the name matches and the county bounding box check passes.
Record the OSM relation or node ID as the source reference.

- Record: `acquisition_method: "osm"`
- Confidence: MEDIUM

### Method 6 — Human-Assisted Acquisition
When all automated methods fail, ask the user for help. See §6 for the full
human assist protocol.

- Record: `acquisition_method: "human_assist"`
- Confidence: HIGH when user has confirmed from an authoritative source;
  MEDIUM for map drop or judgment call

**When to use:** After Methods 1–5 have been tried and failed. Do not defer to
human assist before attempting browser lookup — the browser covers most cases
that geocoding misses.

### Method 7 — Declare gps_unresolvable
When GPS genuinely cannot be determined. See §7 for qualifying criteria and
required documentation.

Only declare `gps_unresolvable = true` after Methods 1–6 have been attempted and
failed, OR when the entity is categorically unresolvable (e.g., a long linear
corridor with no meaningful centroid).

------------------------------------------------------------
## 5.2 Single-Pass Execution

GPS acquisition runs as a single pass covering all entity types. There is no
separate pass for Sites vs. Access Points vs. Trailthings.

For each entity in the batch (sorted by entity type: Sites first, then APs,
then Trailthings, then Site Networks):

1. Check fill-forward (§4) — if GPS available from DB or source, done.
2. Apply ranked methods (§5.1) in order until one succeeds.
3. Record provenance (§6).
4. Mark acquisition status.

------------------------------------------------------------
## 5.5 MORPC Parks & Open Space Layer (15 Ohio Counties)

**Covered counties:** Franklin, Fairfield, Delaware, Pickaway, Licking, Madison,
Union, Ross, Knox, Fayette, Marion, Morrow, Hocking, Logan, Perry.

**Layer reference:** ArcGIS Hub Layer ID `d898fa77e91d414f8f296b0511f14fbf_11`

**Proven coverage:** 96.4% GPS match rate for Franklin County.

**Name matching protocol:**
1. Pre-normalize: apply "Parkland" → "Park" suffix conversion before scoring
2. Score using combined token-set ratio + distinctive-word bonus
3. Thresholds: ≥93 = auto-match; 85–92 = review queue; <85 = no match
4. Apply county filter at match time (MORPC covers multiple counties)
5. Maintain a county-specific override file for confirmed matches where scoring fails

**Provenance:**
- `acquisition_method: "morpc_gis"`
- `match_score`: the numeric score

------------------------------------------------------------
## 5.6 Plus Code Utility

Plus Code computation is a Normalization responsibility. If any pipeline script
needs to compute Plus Codes, use the project utility:

```python
from utilities.na_plus_code import encode_plus_code
plus_code = encode_plus_code(lat, lon)
```

**Never call via subprocess** — the module's self-test block runs as `__main__`
and pollutes stdout with test output.

------------------------------------------------------------
## 5.7 Nominatim Rural Address Fallback (IMP-081)

For rural Ohio road addresses that fail Nominatim, try two alternate query formats
before accepting LOW confidence:

1. **Drop street address**: query as `"[Entity Name], [nearest city/village], Ohio"`
2. **County-anchored**: query as `"[Entity Name], [County Name] County, Ohio"`

Accept the first result that passes the county bounding box check (§5.8).

------------------------------------------------------------
## 5.8 County Bounding Box Sanity Check (IMP-081)

After any geocode, validate the returned coordinate against the county's
approximate bounding box. Use ±0.35° (≈25–30 miles in Ohio) around the county
centroid.

```python
def within_county_bounds(lat, lon, county_centroid_lat, county_centroid_lon,
                         buffer_deg=0.35):
    return (abs(lat - county_centroid_lat) <= buffer_deg and
            abs(lon - county_centroid_lon) <= buffer_deg)
```

Reject and log any result that falls outside this bounding box.

------------------------------------------------------------
## 5.9 Ohio State-Owned Property GIS Sources (IMP-132, IMP-133)

### ODNR Ohio Lake Map Resource
**URL:** `https://experience.arcgis.com/experience/2a39044c75b04e68872564b4c6ec0638`

**Use for:** ODNR Division of Wildlife fishing lakes and wildlife area centroids.
Match entity name against `SITE_NAME`; confirm county field matches.

**Provenance:** `acquisition_method: "odnr_lake_map"`

---

### SORP — State-Owned Real Property
**ArcGIS Export Tool:**
`https://experience.arcgis.com/experience/802e2079e2e4448e819cee71e4fefe92/page/State-Owned-Property-Data-Export-Tool`

**Project asset:** `SORP_Parcels_2023.csv` (project root, v5 folder)

**Use for:** Any Ohio Tier 2 entity not resolvable via MORPC, ODNR Lake Map,
OSM, or Nominatim. Last authoritative GPS fallback before gps_unresolvable.
Filter by county and managing agency; match on entity name.

**Provenance:** `acquisition_method: "sorp_gis"`

------------------------------------------------------------
# 6. HUMAN ASSIST PROTOCOL

Human assist is a first-class acquisition method, not a last resort. It is
appropriate whenever automated and browser methods have failed or produced
ambiguous results, or when the entity is obscure enough that no automated source
is likely to have it.

## 6.1 What to Present to the Human

When requesting human assist, provide:

1. Entity name, type, county, and parent entity (if AP)
2. Any candidate coordinates already found (with sources and confidence)
3. The entity's `location_raw` and `urls_raw` for reference
4. A specific question: "Can you find the coordinates for this entity, or confirm/
   reject this candidate?"
5. A brief statement of which methods were tried and why they failed

## 6.2 What the Human Can Do

- Navigate to the entity's official page or Google Maps and extract coordinates
- Drop a pin at the correct location and provide decimal degree coordinates
- Provide a Google Maps share link (Claude extracts lat/lon from the URL)
- Confirm a candidate coordinate as correct
- Reject a candidate coordinate and explain why
- Declare the entity GPS-unresolvable with a documented reason (triggering §7)

## 6.3 Recording Human Assist Results

Record the result as a GPS acquisition event with:
- `acquisition_method`: `"human_assist"`
- `verifier`: `"user"` or a human identifier
- `source_url`: the page or map the human used (if applicable)
- `confidence_level`: `"high"` if user confirmed from an authoritative source;
  `"medium"` if from a map drop or judgment call
- `notes`: brief explanation of what the human did and why

------------------------------------------------------------
# 7. PROVENANCE MODEL

Every GPS acquisition event must produce a provenance record including:

- **acquisition_method**:
  - `"source_stated"` — coordinates in raw discovery record
  - `"db_fill_forward"` — carried forward from prior run
  - `"authoritative_page"` — stated on official page
  - `"authoritative_gis"` — from authoritative GIS dataset
  - `"morpc_gis"` — MORPC Parks & Open Space layer
  - `"odnr_lake_map"` — ODNR Ohio Lake Map Resource
  - `"sorp_gis"` — State-Owned Real Property dataset
  - `"browser_lookup"` — Claude in Chrome (Google Maps, ArcGIS viewer, GIS portal)
  - `"geocoding"` — Nominatim or equivalent geocoder
  - `"osm"` — OpenStreetMap or public map lookup
  - `"human_assist"` — user-provided coordinate or location
  - `"other"`

- **source_url** — the URL of the page, viewer, or endpoint used

- **acquisition_timestamp** — ISO 8601 timestamp

- **confidence_level** — `"high"` | `"medium"` | `"low"`

- **notes** (optional) — free-text for ambiguous or manually adjusted cases

- **accepted** (boolean) — whether this coordinate was accepted

Provenance is immutable once written. New acquisitions append, not overwrite.

------------------------------------------------------------
# 8. GPS UNRESOLVABLE FLAG (IMP-069)

## 7.1 Purpose

`gps_unresolvable = true` allows an entity to proceed past the GPS Gate without
GPS, when GPS genuinely cannot be determined. It is an explicit acknowledgment
that acquisition was attempted and failed for documented reasons.

## 7.2 Qualifying Criteria

`gps_unresolvable = true` may be set **only** when one or more of the following
is true and documented in `notes`:

| Criterion | Example |
|---|---|
| Linear corridor with no meaningful centroid | Long-distance rail trail, river section |
| Multi-parcel distributed holding with disjunct parcels | Land trust in 3 non-adjacent parcels |
| Boundary defined by metes and bounds only | Historic commons described in deed only |
| Offshore or floating entity | Floating wetland restoration platform |
| Coordinate disclosure restricted by agency policy | Some sensitive wildlife sites |

## 7.3 Not Qualifying

The following do NOT qualify for `gps_unresolvable = true`:
- GPS not yet attempted
- GPS lookup failed due to tool or network error
- Address is known but coordinates were not converted
- Uncertainty about which of two candidate coordinates is correct

These entities must be held (`hold_reason = "gps_missing"`) until GPS is properly acquired.

## 7.4 Required Documentation

The entity's `notes` field must contain:
1. A plain-language explanation of why GPS cannot be obtained
2. The date the determination was made
3. A description of what acquisition methods were attempted

Example: `"GPS unresolvable — distributed land trust holding in three non-adjacent
parcels; no single coordinate represents the entity. Attempted: MORPC layer (not
found), county auditor GIS (parcel boundaries only), browser lookup (no place card).
Determined 2026-05-31."`

## 7.5 Pipeline Behavior

- Entities with `gps_unresolvable = true` skip the GPS acquisition workflow.
- They pass the GPS Gate and proceed to TSV Output without GPS coordinates.
- `plus_code`, `township`, and `municipality` will be blank.
- They are **not** written to `held_entities`.
- They are upserted to the DB with null GPS.

------------------------------------------------------------
# 9. GPS GATE

After the acquisition pass, every entity must pass through the GPS Gate before
proceeding to Normalization.

**An entity passes the GPS Gate if:**
- `gps_lat` and `gps_lon` are both non-null, OR
- `gps_unresolvable = true` is set and documented

**An entity fails the GPS Gate if:**
- GPS is null AND `gps_unresolvable` is not set

**On failure:**
- Route to `held_entities` with `hold_reason = "gps_missing"`
- Log: `"Entity [id] held: GPS null and gps_unresolvable not set."`
- Entity will be released when GPS is acquired in a subsequent run

**GPS Gate applies to:** Sites and Access Points
**GPS Gate does not apply to:** Trailthings and Site Networks (gps_unresolvable
is assumed for most; if GPS is present, it flows through normally)

------------------------------------------------------------
# 10. VERIFICATION RULES

Every acquired coordinate must be checked:

**Numeric validity:**
- lat in [-90, 90]
- lon in [-180, 180]

**County consistency:**
- Coordinate must fall within one of the entity's `counties_raw`
- If outside all listed counties: flag `gps_requires_manual_review = true`
- Note: this check is also run by the Normalization Engine's GPS County Check
  (IMP-067); a mismatch here triggers manual review; a mismatch at normalization
  routes to the manual_review_queue

**Duplicate detection:**
- If multiple acquisition methods yield different coordinates:
  - Prefer the highest-authority method
  - Record all candidates in GPS provenance
  - Flag `gps_requires_manual_review = true` if differences are large (>0.01°)

The module may only **accept or flag** — never snap, adjust, or infer corrections.

------------------------------------------------------------
# 11. BROWSER USE IN DISCOVERY (BROADER SCOPE)

The browser-assisted method in §5.1 Method 3 is documented specifically for GPS
acquisition, but browser access (Claude in Chrome) is valuable throughout the
pipeline — not just for GPS.

**Discovery uses for Claude in Chrome:**
- ArcGIS Experience viewers that cannot be accessed via web fetch alone
- Interactive GIS portals (county AuditorMap, ODNR GIS layers)
- JS-rendered park listing pages (FacetWP, infinite scroll — IMP-013)
- Map verification pass for municipalities (§20 of Discovery Protocol)
- Accessing GIS exports from MORPC Hub and similar platforms
- Downloading source documents that require browser interaction

**When to use browser vs. web fetch:**
- Web fetch first: most official websites, ArcGIS REST endpoints with known URLs,
  plain HTML pages
- Browser when: page requires JavaScript rendering, the data is in an interactive
  viewer, JS pagination is present, or the source is a GIS platform that doesn't
  expose a REST API

Claude should proactively use browser access whenever the source material is
more accessible or complete via browser than via web fetch. The goal is
comprehensive discovery, not limiting to text-only sources.

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- Resolution Engine v6.0 (input — resolved entities)
- Normalization Engine v6.0 (downstream consumer — GPS validation, Plus Code,
  GIS lookup)
- Site Schema Module v6.0, Access Point Schema Module v6.0 (field definitions)
- Audit & Logging Module v6.0 (provenance logging)
- `utilities/na_plus_code.py` (Plus Code encoding — §5.6)
- `utilities/na_township_lookup.py` (county centroid reference for bounding box)
- Claude in Chrome (browser-assisted acquisition — §5.1 Method 3)

------------------------------------------------------------
# END OF GPS ACQUISITION MODULE v6.0
