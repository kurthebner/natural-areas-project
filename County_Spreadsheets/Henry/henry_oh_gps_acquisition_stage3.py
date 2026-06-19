#!/usr/bin/env python3
"""
henry_oh_gps_acquisition_stage3.py — Stage 3 GPS Acquisition
Henry County, Ohio | Run ID: henry_oh_2026_04_20
IMP-081: Nominatim fallback protocol + county bounding box check

Processes 12 held entities, attempts GPS acquisition in priority order:
  1. Known address → Nominatim structured geocode (HIGH confidence)
  2. Name + city, Ohio → Nominatim (MED confidence if passes bbox)
  3. Name + county, Ohio → Nominatim (MED confidence if passes bbox)
  4. LOW confidence centroid if rural area without an exact match
  5. NONE if linear/dispersed feature or all queries fail

Outputs:
  henry_oh_gps_results.yaml   — per-entity GPS decisions
  henry_oh_gps_report.md      — human-readable summary
"""

import time, re, json, logging, pathlib, yaml
import urllib.request, urllib.parse

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

# ─── Constants ───────────────────────────────────────────────────────────────
RUN_ID = "henry_oh_2026_04_20"
COUNTY = "Henry"
STATE  = "Ohio"
COUNTY_CENTROID = (41.30, -84.08)   # Henry County, OH centroid
BBOX_BUFFER = 0.35                   # ±0.35° ≈ 25-30 miles (IMP-081)

NOMINATIM_URL  = "https://nominatim.openstreetmap.org/search"
USER_AGENT     = "NaturalAreasProject/5.0 (henry_county_gps_acquisition; contact=pipeline@naturalareasprojec.org)"
REQUEST_DELAY  = 1.5                 # seconds between Nominatim calls (policy)

# ─── Known address data (from discovery sessions) ────────────────────────────
# Populated from T2, T7, T8 session discoveries and session log knowledge
KNOWN_ADDRESSES = {
    "HEN_S_004": {
        "name":    "Dr. John Bloomfield Home & Carriage House Museum",
        "address": "229 W Clinton St, Napoleon, OH 43545",
        "city":    "Napoleon",
    },
    "HEN_S_011": {
        "name":    "Henry County Fairgrounds",
        "address": "821 S Perry St, Napoleon, OH 43545",
        "city":    "Napoleon",
    },
    "HEN_S_012": {
        "name":    "Henry County Historical Society Fairgrounds Historic Complex",
        "address": "821 S Perry St, Napoleon, OH 43545",   # co-located at fairgrounds
        "city":    "Napoleon",
    },
    "HEN_S_018": {
        "name":    "Mary Jane Thurston State Park",
        "address": "1466 State Route 65, McClure, OH 43534",
        "city":    "McClure",
    },
    "HEN_S_009": {
        "name":    "Hamler Community Park",
        "address": None,               # SR 109 north edge of Hamler — no street number
        "city":    "Hamler",
    },
    "HEN_S_017": {
        "name":    "Liberty Center Firemen's Park",
        "address": None,
        "city":    "Liberty Center",
    },
    "HEN_S_006": {
        "name":    "Florida Wildlife Area",
        "address": None,
        "city":    "Florida",          # village of Florida, Henry County
    },
    "HEN_S_023": {
        "name":    "North Turkeyfoot Wildlife Area",
        "address": None,
        "city":    None,
    },
    "HEN_S_013": {
        "name":    "Henry County Wildlife Area 1",
        "address": None,
        "city":    None,
    },
    "HEN_S_014": {
        "name":    "Henry County Wildlife Area 2",
        "address": None,
        "city":    None,
    },
    "HEN_S_015": {
        "name":    "Henry County Wildlife Area 3",
        "address": None,
        "city":    None,
    },
    "HEN_S_019": {
        "name":    "Maumee State Scenic River",
        "address": None,
        "city":    None,
        "_linear": True,               # linear feature — special handling
    },
}

# ─── Entities that are expected to be NONE (no acquirable GPS) ───────────────
# Maumee State Scenic River is a linear feature spanning multiple counties;
# no meaningful single GPS point exists. Confidence = NONE.
LINEAR_FEATURES = {"HEN_S_019"}

# ─── ODNR Wildlife Areas — check ODNR GIS/web for location hints ─────────────
# Henry County Wildlife Area 1/2/3 are ODNR Division of Wildlife parcels.
# No addresses in discovery. Strategy:
#   - Try "Henry County Wildlife Area, Henry County, Ohio" to find any of them
#   - If found and passes bbox: assign MED confidence; note which parcel uncertain
# North Turkeyfoot WA: try "North Turkeyfoot Wildlife Area, Ohio"
# Florida WA: try "Florida Wildlife Area, Henry County, Ohio"


def within_county_bounds(lat: float, lon: float) -> bool:
    """IMP-081 county bounding box check."""
    clat, clon = COUNTY_CENTROID
    return abs(lat - clat) <= BBOX_BUFFER and abs(lon - clon) <= BBOX_BUFFER


def nominatim_query(q: str, attempt: str) -> dict | None:
    """Run a single Nominatim free-text query. Returns first result or None."""
    params = urllib.parse.urlencode({
        "q": q,
        "format": "json",
        "limit": 1,
        "countrycodes": "us",
    })
    url = f"{NOMINATIM_URL}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            results = json.loads(resp.read().decode())
    except Exception as ex:
        logger.warning(f"  [{attempt}] Nominatim error: {ex}")
        return None

    time.sleep(REQUEST_DELAY)

    if not results:
        logger.info(f"  [{attempt}] No results for: {q!r}")
        return None

    r = results[0]
    lat, lon = float(r["lat"]), float(r["lon"])
    logger.info(f"  [{attempt}] Got ({lat:.6f}, {lon:.6f}) — {r.get('display_name','')[:80]}")
    return {"lat": lat, "lon": lon, "display_name": r.get("display_name", ""), "query": q}


def acquire_gps(eid: str, info: dict) -> dict:
    """
    Attempt GPS acquisition for one entity. Returns a result dict with:
      gps_lat, gps_lon, confidence, method, notes
    """
    name   = info["name"]
    addr   = info.get("address")
    city   = info.get("city")
    linear = info.get("_linear", False)

    logger.info(f"\n{'='*60}")
    logger.info(f"{eid} — {name}")

    # Linear features: NONE confidence
    if linear or eid in LINEAR_FEATURES:
        logger.info("  → Linear/dispersed feature — NONE confidence assigned")
        return {
            "gps_lat":    None,
            "gps_lon":    None,
            "confidence": "NONE",
            "method":     "linear_feature",
            "notes":      "Linear feature spanning multiple counties; no single GPS point appropriate.",
        }

    result = None

    # ── Attempt 1: Full street address ───────────────────────────────────────
    if addr:
        logger.info(f"  [Attempt 1] Address: {addr!r}")
        result = nominatim_query(addr, "Attempt 1: address")
        if result and within_county_bounds(result["lat"], result["lon"]):
            return {
                "gps_lat":    round(result["lat"], 6),
                "gps_lon":    round(result["lon"], 6),
                "confidence": "HIGH",
                "method":     f"Nominatim address query: {addr!r}",
                "notes":      result["display_name"][:120],
            }
        elif result:
            logger.warning(f"  [Attempt 1] Result outside county bbox — rejected")
            result = None

    # ── Attempt 2: Name + city, Ohio ─────────────────────────────────────────
    if city:
        q2 = f"{name}, {city}, Ohio"
        logger.info(f"  [Attempt 2] Name+city: {q2!r}")
        result = nominatim_query(q2, "Attempt 2: name+city")
        if result and within_county_bounds(result["lat"], result["lon"]):
            conf = "HIGH" if addr else "MED"  # HIGH if we had an address that matched too
            return {
                "gps_lat":    round(result["lat"], 6),
                "gps_lon":    round(result["lon"], 6),
                "confidence": conf,
                "method":     f"Nominatim query: {q2!r}",
                "notes":      result["display_name"][:120],
            }
        elif result:
            logger.warning(f"  [Attempt 2] Result outside county bbox — rejected")
            result = None

    # ── Attempt 3: Name + county, Ohio ───────────────────────────────────────
    q3 = f"{name}, Henry County, Ohio"
    logger.info(f"  [Attempt 3] Name+county: {q3!r}")
    result = nominatim_query(q3, "Attempt 3: name+county")
    if result and within_county_bounds(result["lat"], result["lon"]):
        return {
            "gps_lat":    round(result["lat"], 6),
            "gps_lon":    round(result["lon"], 6),
            "confidence": "MED",
            "method":     f"Nominatim query: {q3!r}",
            "notes":      result["display_name"][:120],
        }
    elif result:
        logger.warning(f"  [Attempt 3] Result outside county bbox — rejected")

    # ── Attempt 4: Simplified name + Ohio ────────────────────────────────────
    # Strip "Henry County" prefix if present to avoid confusion
    simplified = re.sub(r'^Henry County\s+', '', name)
    if simplified != name:
        q4 = f"{simplified}, Ohio"
        logger.info(f"  [Attempt 4] Simplified name: {q4!r}")
        result = nominatim_query(q4, "Attempt 4: simplified")
        if result and within_county_bounds(result["lat"], result["lon"]):
            return {
                "gps_lat":    round(result["lat"], 6),
                "gps_lon":    round(result["lon"], 6),
                "confidence": "MED",
                "method":     f"Nominatim query: {q4!r}",
                "notes":      result["display_name"][:120],
            }
        elif result:
            logger.warning(f"  [Attempt 4] Result outside county bbox — rejected")

    # ── Attempt 5: City centroid (LOW) ───────────────────────────────────────
    if city:
        q5 = f"{city}, Henry County, Ohio"
        logger.info(f"  [Attempt 5 — LOW fallback] City centroid: {q5!r}")
        result = nominatim_query(q5, "Attempt 5: city centroid")
        if result and within_county_bounds(result["lat"], result["lon"]):
            return {
                "gps_lat":    round(result["lat"], 6),
                "gps_lon":    round(result["lon"], 6),
                "confidence": "LOW",
                "method":     f"LOW: city centroid fallback — {q5!r}",
                "notes":      f"No exact park match; using {city} centroid. {result['display_name'][:80]}",
            }

    # ── No GPS acquired ───────────────────────────────────────────────────────
    logger.info(f"  → All attempts failed — NONE")
    return {
        "gps_lat":    None,
        "gps_lon":    None,
        "confidence": "NONE",
        "method":     "all_queries_failed",
        "notes":      "No Nominatim result within county bounds for any query format.",
    }


def main():
    out_dir = pathlib.Path("/sessions/trusting-sweet-gates/mnt/outputs")
    ws_dir  = pathlib.Path("/sessions/trusting-sweet-gates/mnt/Natural Areas Project v5")

    results = {}
    for eid in sorted(KNOWN_ADDRESSES.keys()):
        info = KNOWN_ADDRESSES[eid]
        r = acquire_gps(eid, info)
        results[eid] = {"name": info["name"], **r}

    # ── Write YAML results ────────────────────────────────────────────────────
    out_yaml = {
        "run_id":  RUN_ID,
        "county":  COUNTY,
        "state":   STATE,
        "stage":   3,
        "results": results,
    }
    yaml_path = ws_dir / "henry_oh_gps_results.yaml"
    yaml_path.write_text(yaml.dump(out_yaml, allow_unicode=True, sort_keys=False))
    logger.info(f"\nResults written → {yaml_path}")

    # ── Write Markdown report ─────────────────────────────────────────────────
    lines = [
        "# Henry County, OH — Stage 3 GPS Acquisition Report",
        f"**Run ID:** {RUN_ID}  ",
        "**Date:** 2026-04-26  ",
        "",
        "| ID | Name | GPS Lat | GPS Lon | Confidence | Method |",
        "|---|---|---|---|---|---|",
    ]
    counts = {"HIGH": 0, "MED": 0, "LOW": 0, "NONE": 0}
    for eid, r in sorted(results.items()):
        lat = f"{r['gps_lat']:.6f}" if r["gps_lat"] else "—"
        lon = f"{r['gps_lon']:.6f}" if r["gps_lon"] else "—"
        conf = r["confidence"]
        counts[conf] = counts.get(conf, 0) + 1
        lines.append(f"| {eid} | {r['name']} | {lat} | {lon} | {conf} | {r['method'][:60]} |")

    lines += [
        "",
        "## Summary",
        "",
        f"| HIGH | MED | LOW | NONE |",
        f"|------|-----|-----|------|",
        f"| {counts['HIGH']} | {counts['MED']} | {counts['LOW']} | {counts['NONE']} |",
        "",
        "## Notes",
        "",
    ]
    for eid, r in sorted(results.items()):
        if r["notes"]:
            lines.append(f"- **{eid}** ({r['name']}): {r['notes']}")

    report_path = ws_dir / "henry_oh_gps_report.md"
    report_path.write_text("\n".join(lines))
    logger.info(f"Report written → {report_path}")

    # ── Summary ───────────────────────────────────────────────────────────────
    acquired = sum(1 for r in results.values() if r["gps_lat"] is not None)
    logger.info(f"\n{'='*60}")
    logger.info(f"GPS Acquisition complete: {acquired}/12 acquired")
    for conf, n in counts.items():
        logger.info(f"  {conf}: {n}")


if __name__ == "__main__":
    main()
