# IMP-082 — ODNR Division of Wildlife GIS Parcel Protocol
**Added:** 2026-04-27 (Henry County, OH run)  
**Applies to:** Ohio counties with ODNR Division of Wildlife lands

---

## Purpose

For Ohio ODNR DOW lands (Wildlife Areas, Fishing Access areas, etc.) that fail Nominatim or have no street address, query the official DOW parcel boundary GIS layer before assigning LOW or NONE confidence GPS. This endpoint is publicly accessible and returns exact polygon geometries — far more accurate than any geocoder fallback.

## Endpoint

```
https://gis.ohiodnr.gov/arcgis/rest/services/DOW_Services/Roads_ParkingAreas/FeatureServer/28
```

**Layer 28 = `DNR_Lands_repl`** — DOW parcel polygons (boundaries, not points)  
Always request `outSR=4326` to get WGS84 output.

## Query by County FIPS

```
GET /28/query?where=CNTY_FIPS='069'
  &outFields=ALT_NAME,PROP_TYPE,SUM_CALC_ACRES,CNTY_FIPS,Name_Label
  &returnGeometry=true&outSR=4326&geometryPrecision=6&f=json
```

To filter to Wildlife Areas only: `where=CNTY_FIPS='069'+AND+PROP_TYPE='WA'`

**Ohio county FIPS (3-digit, zero-padded):**

| County | FIPS | County | FIPS |
|--------|------|--------|------|
| Allen | 003 | Fulton | 051 |
| Defiance | 039 | Henry | 069 |
| Hancock | 063 | Lucas | 095 |
| Hardin | 065 | Paulding | 125 |
| Mercer | 107 | Putnam | 137 |
| Van Wert | 161 | Williams | 171 |
| Wood | 173 | Wyandot | 175 |

Full FIPS list: https://www.census.gov/library/reference/code-lists/ansi/ansi-codes-for-states.html (Ohio state FIPS = 39; county codes appended)

## PROP_TYPE Values

| Value | Meaning |
|-------|---------|
| `WA` | Wildlife Area |
| `FISH ACCESS` | Fishing Access |
| `SR AREA` | Scenic River Area (linear feature — no useful single GPS) |
| `PARK` | State park parcels (usually managed by ODNR Parks, not DOW) |

## Centroid Computation

Use the **largest ring's shoelace centroid** — not bbox center. Multi-ring polygons (common for non-contiguous parcels) require area-weighting to pick the main parcel.

```python
def ring_centroid(ring):
    """Signed-area centroid via shoelace formula."""
    n = len(ring)
    area = cx = cy = 0.0
    for i in range(n):
        x0, y0 = ring[i]
        x1, y1 = ring[(i + 1) % n]
        cross = x0 * y1 - x1 * y0
        area += cross
        cx += (x0 + x1) * cross
        cy += (y0 + y1) * cross
    area /= 2.0
    if abs(area) < 1e-12:
        return sum(p[0] for p in ring)/n, sum(p[1] for p in ring)/n
    return cx / (6.0 * area), cy / (6.0 * area)

def polygon_centroid(rings):
    """Centroid of the largest ring in a multi-ring polygon."""
    def ring_area(r):
        n = len(r); a = 0.0
        for i in range(n):
            x0, y0 = r[i]; x1, y1 = r[(i + 1) % n]
            a += x0 * y1 - x1 * y0
        return abs(a) / 2.0
    biggest = rings[max(range(len(rings)), key=lambda i: ring_area(rings[i]))]
    return ring_centroid(biggest)

# Usage:
lon, lat = polygon_centroid(feature["geometry"]["rings"])
lat_r, lon_r = round(lat, 6), round(lon, 6)
```

## Confidence Level

**HIGH** — This is the authoritative geometry from the managing state agency's GIS. Use GPS confidence = HIGH and record the method as:

```
GPS: HIGH — ODNR GIS polygon centroid (DOW_Services/Roads_ParkingAreas layer 28, queried YYYY-MM-DD)
```

## Other Public Layers in the DOW_Services Folder

`https://gis.ohiodnr.gov/arcgis/rest/services/DOW_Services`

| Service | Layer(s) | Contents | Use |
|---------|----------|----------|-----|
| `Roads_ParkingAreas` | 26 | Roads on DOW land | Confirm access |
| `Roads_ParkingAreas` | 28 | DNR_Lands_repl (parcels) | **Primary GPS source** |
| `Roads_ParkingAreas` | 29 | Parking_Areas | GPS for Access Points |
| `DOW_Facilities/MapServer` | 0 | Marinas | AP GPS |
| `DOW_Facilities/MapServer` | 1 | Boat launch ramps | AP GPS |
| `DOW_Facilities/MapServer` | 2 | Fishing Access | AP GPS |
| `DOW_Facilities/MapServer` | 9 | Park Office | Site GPS (urban/staffed WAs) |
| `DOW_Facilities/MapServer` | 14 | Campgrounds | Feature verification |
| `Dog_Training_Areas` | — | Dog training area polygons | Discovery supplement |
| `ControlledHunt_Pub` | — | Controlled hunt unit boundaries | Discovery supplement |

**Querying DOW_Facilities by county bbox:**
```
/DOW_Facilities/MapServer/{layer}/query
  ?where=1=1
  &geometry={"xmin":-84.25,"ymin":41.18,"xmax":-83.90,"ymax":41.42}
  &geometryType=esriGeometryEnvelope&inSR=4326
  &outFields=*&returnGeometry=true&outSR=4326&f=json
```

**Do NOT attempt:** `gis.ohiodnr.gov/arcgis/rest/services/oinp/PublicLands` — requires ODNR login, redirects to sign-in page.

## When to Use

Run IMP-082 **in the GPS Acquisition script**, not as a post-pipeline patch:
1. Build the `KNOWN_ADDRESSES` dict during discovery (T2 session), flag ODNR DOW entities
2. In Stage 3, for any entity flagged as ODNR DOW with no street address: query layer 28 by entity name pattern before falling back to Nominatim city-centroid
3. If parcel found and centroid passes county bbox check: assign HIGH confidence and proceed to normalize

## DB Schema Notes (verified 2026-04-27)

The `sites` table does **not** have an `identity_notes` column. Route GPS provenance notes into the `notes` field instead. The `run_metadata` table does **not** have an `updated_at` column. Exact column lists:

**sites:** `site_id, name, category, subtype, designation, status, ownership, governance, partner_agencies, coordination, description, location, acres, counties, municipality, township, gps_lat, gps_lon, plus_code, features, notes, url_primary, urls, parent_site_id, created_at, updated_at, features_raw`

**run_metadata:** `run_id, county, state, run_date, records_input, normalized, held, rejected, notes, created_at`

**DB location:** `{BASE}/NASqlite/natural_areas_v5.db` (not `{BASE}/natural_areas_v5.db` — the root-level .db file is a stale empty placeholder)

