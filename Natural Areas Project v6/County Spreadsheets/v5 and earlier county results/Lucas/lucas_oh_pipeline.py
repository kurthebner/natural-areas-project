#!/usr/bin/env python3
# =============================================================================
# SUPERSEDED — IMP-091 (2026-05-04)
# This monolithic pipeline script has been replaced by the parameterised model:
#   utilities/na_run_county.py + County_Spreadsheets/{County}/{county}_pipeline_config.json
# Do not use for new county runs. Kept for reference only.
# =============================================================================
"""
lucas_oh_pipeline.py — Lucas County, Ohio — Natural Areas Project Pipeline
RUN_ID: lucas_oh_2026_04_27  |  PREFIX: LUC
Stages 1–6: Resolution → Normalization → GPS → TSV → Vocab Gate → Integrity → DB Upsert
"""

import argparse
import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime, timezone

# ── Path setup ────────────────────────────────────────────────────────────────
THIS_DIR     = Path(__file__).parent                    # County_Spreadsheets/Lucas
PROJECT_ROOT = THIS_DIR.parent.parent                   # Natural Areas Project v5
UTILS_DIR    = PROJECT_ROOT / "utilities"
sys.path.insert(0, str(UTILS_DIR))

from na_pipeline_core import (
    acquire_gps, propagate_gps_to_children, propagate_gps_to_trails,
    propagate_gps_to_aps, add_plus_codes, add_gis_lookup,
    run_vocab_gate, write_all_tsvs, integrity_check,
    upsert_sites, upsert_site_parents, upsert_trails, upsert_trail_parents,
    upsert_access_points, upsert_run_metadata,
)

# ── Run config ────────────────────────────────────────────────────────────────
RUN_ID     = "lucas_oh_2026_04_27"
COUNTY     = "Lucas"
STATE      = "OH"
RUN_DATE   = "2026-04-27"
PREFIX     = "LUC"
NOW        = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
OUTPUT_DIR = str(THIS_DIR)
DEFAULT_DB = str(PROJECT_ROOT / "NASqlite" / "natural_areas_v5.db")
RAW_YAML   = PROJECT_ROOT / "lucas_oh_raw_discovery.yaml"

# Lucas County centroid for Nominatim bbox validation (IMP-081)
COUNTY_CENTROID_LAT = 41.61
COUNTY_CENTROID_LON = -83.63
BBOX_BUFFER = 0.50   # slightly wider — county is elongated E-W along Lake Erie

# ════════════════════════════════════════════════════════════════════════════
#  FEATURE MAP  (canonical mapper for features_raw → controlled vocabulary)
# ════════════════════════════════════════════════════════════════════════════

FEATURE_MAP = [
    # trails / paths
    (r"hiking trail|walking trail|walking path|nature trail|loop trail|trail system"
     r"|interpretive trail|self.guided interpretive|walk.*trail", "Hiking Trail"),
    (r"boardwalk", "Boardwalk"),
    (r"bridle trail|equestrian|horse trail", "Bridle Trail"),
    (r"mountain bike|singletrack", "Mountain Bike Trail"),
    (r"multi.use trail|paved.*trail|hard.surface.*trail|all purpose trail"
     r"|walk/bike|walk.*bike path", "Multi-use Trail"),
    # water access
    (r"boat ramp|launch ramp|4.lane.*launch|boat launch(?! area)", "Boat Ramp"),
    (r"kayak launch|kayak access|kayak cove|kayak concession|canoe|watercraft access"
     r"|paddling access|water trail access", "Watercraft Access"),
    (r"marina", "Marina"),
    (r"fishing pier", "Fishing Area"),
    (r"fishing pond|fishing lake|fishing area|fishing access|fishing spot", "Fishing Area"),
    (r"fishing pond|fishing lake", "Pond"),
    (r"swimming beach|swim beach|swim.*pond", "Swimming Beach"),
    (r"swimming pool|city pool", "Swimming Pool"),
    (r"splash pad|spray pad|spray park", "Spray Park"),
    (r"beach(?!\s*volleyball)", "Beach"),
    # shelters / seating
    (r"pavilion|shelter house|covered shelter|open air pavilion|rentable.*shelter"
     r"|picnic shelter", "Pavilion"),
    (r"picnic area|picnic table|picnic spot", "Picnic Area"),
    (r"gazebo", "Gazebo"),
    (r"amphitheater|amphitheatre", "Amphitheater"),
    # sports
    (r"baseball|softball|ball diamond", "Ball Diamond"),
    (r"basketball court", "Basketball Court"),
    (r"tennis court", "Tennis Court"),
    (r"pickleball", "Pickleball Court"),
    (r"volleyball", "Volleyball Court"),
    (r"soccer field|soccer complex|soccer pitch", "Soccer Pitch"),
    (r"football field", "Football Field"),
    (r"disc golf", "Disc Golf Course"),
    (r"skate park|skate ramp", "Skate Park"),
    (r"mini.*golf|miniature golf", "Mini Golf"),
    # recreation / amenities
    (r"playground|play equipment|climbing structure|nature play", "Playground"),
    (r"sledding hill", "Sledding Hill"),
    (r"horseshoe", "Horseshoe Pitch"),
    (r"archery", "Archery Range"),
    (r"ropes course|high ropes", "Ropes Course"),
    (r"dog park|off.leash", "Dog Park"),
    (r"restroom|flush toilet|portable toilet|bathroom|latrine|pit latrine", "Restrooms"),
    (r"parking(?! area in name)", "Parking Lot"),
    (r"kiosk|information kiosk", "Kiosk"),
    (r"camping|campsite|primitive camp", "Camping"),
    (r"cabin|camper cabin|yurt", "Cabin Rentals"),
    (r"ada.compliant|ada accessible|wheelchair|handicapped|accessible trail", "ADA Accessible"),
    (r"fire ring", "Fire Ring"),
    (r"fitness station|fitness equipment|exercise station|exercise trail", "Fitness Station"),
    # natural features
    (r"observation deck|observation tower|overlook|viewing platform|viewing area", "Observation Deck"),
    (r"bird.*view|wildlife.*view|wildlife.*observation|bird.*watch|birding", "Wildlife Observation Area"),
    (r"vernal pool", "Vernal Pool"),
    (r"prairie restoration|prairie.*restor", "Prairie Restoration"),
    (r"prairie", "Prairie"),
    (r"wetland restoration|wetland.*restor", "Wetland Restoration"),
    (r"wetland", "Wetland"),
    (r"habitat.*restor", "Habitat Restoration Area"),
    (r"interpretive sign|interpretive exhibit|interpretive display"
     r"|interpretive marker", "Interpretive Exhibit"),
    (r"nature center|nature lab|environmental ed", "Nature Center"),
    (r"arboretum", "Arboretum"),
    (r"garden|display garden|flower garden", "Garden"),
    (r"pollinator garden", "Pollinator Garden"),
    (r"community garden", "Community Garden"),
    (r"butterfly|pollinator", "Butterfly or Pollinator Garden"),
    # historic
    (r"historic.*marker|historical marker|historical.*sign", "Historic Marker"),
    (r"historic.*lock|canal lock", "Historic Lock"),
    (r"historic.*canal|canal.*ruin", "Historic Canal Segment"),
    (r"canal structure", "Canal Structure"),
    (r"historic.*structure|renovated.*building", "Historic Structure"),
    # civic / art
    (r"sculpture|public art|artisan village|art installation", "Public Art Installation"),
    (r"fountain", "Fountain"),
    (r"bridge(?!.*bike)", "Bridge"),
    (r"visitor center", "Visitor Center"),
    (r"museum building|museum", "Museum Building"),
]


def map_features(raw: str) -> str:
    """Map raw features text to semicolon-delimited controlled vocabulary terms."""
    if not raw:
        return ""
    text = raw.lower()
    matched, seen = [], set()
    for pattern, term in FEATURE_MAP:
        if term not in seen and re.search(pattern, text):
            matched.append(term)
            seen.add(term)
    return ";".join(matched)


# ════════════════════════════════════════════════════════════════════════════
#  UTILITY HELPERS
# ════════════════════════════════════════════════════════════════════════════

def clean_urls(urls_raw) -> str:
    if not urls_raw:
        return ""
    if isinstance(urls_raw, list):
        return ";".join(u for u in urls_raw if u)
    return str(urls_raw)


def first_url(urls_raw) -> str:
    if not urls_raw:
        return ""
    if isinstance(urls_raw, list):
        return urls_raw[0] if urls_raw else ""
    parts = str(urls_raw).split(";")
    return parts[0].strip() if parts else ""


def clean_counties(counties_raw) -> str:
    if not counties_raw:
        return "Lucas"
    if isinstance(counties_raw, list):
        cleaned = [c.replace(" County", "").strip() for c in counties_raw]
    else:
        cleaned = [c.replace(" County", "").strip()
                   for c in str(counties_raw).split(";")]
    return ";".join(sorted(set(c for c in cleaned if c))) or "Lucas"


def safe_float(val):
    try:
        return round(float(val), 6) if val is not None and str(val).strip() else None
    except Exception:
        return None


def safe_acres(val):
    try:
        s = str(val).strip().replace("~", "").replace("+", "").replace(",", "")
        return float(s) if s else None
    except Exception:
        return None


# ════════════════════════════════════════════════════════════════════════════
#  SITE NORMALIZATION
# ════════════════════════════════════════════════════════════════════════════

def normalize_site_vocab(r: dict):
    """Return (category, subtype, designation, status) for a raw Site record."""
    gov        = r.get("governance_raw", "") or ""
    name       = r.get("name_raw", "") or ""
    notes      = r.get("identity_notes_raw", "") or ""
    name_lower = name.lower()

    # Default
    designation = ""
    status      = "Active"

    # === IMP-068: Name-pattern overrides — checked first ===
    if "arboretum" in name_lower:
        return "Curated Biological Site", "Arboretum", designation, status
    if "botanical garden" in name_lower:
        return "Curated Biological Site", "Botanical Garden", designation, status

    # === Federal ===
    if gov == "U.S. Fish and Wildlife Service":
        return "Wildlife Area", "Federal Wildlife Area", "National Wildlife Refuge", status
    if gov == "U.S. Army Corps of Engineers":
        # Grassy Island — undeveloped island, open space
        return "Open Space", "Urban Open Space", "", status

    # === State ODNR ===
    if gov == "ODNR Division of Natural Areas & Preserves":
        return "Nature Preserve", "State Nature Preserve", "State Nature Preserve", status
    if gov == "ODNR Division of Wildlife":
        return "Wildlife Area", "State Wildlife Area", "State Wildlife Area", status
    if gov == "ODNR Division of Parks & Watercraft":
        return "Park", "", "State Park", status
    if gov == "ODNR-Forest":
        return "Conservation Area", "Forest Management Area", "State Forest", status

    # === Metroparks Toledo ===
    if gov in ("Metroparks Toledo",
               "Metropolitan Park District of the Toledo Area"):
        if "audubon islands" in name_lower:
            return "Nature Preserve", "State Nature Preserve", "State Nature Preserve", status
        if "glass city riverwalk" in name_lower:
            return "Park", "Linear Park", "", status
        if "toledo botanical garden" in name_lower:
            # IMP-068 catches this via 'botanical garden' above, but belt-and-suspenders
            return "Curated Biological Site", "Botanical Garden", "", status
        return "Park", "", "", status

    # === The Nature Conservancy ===
    if gov == "The Nature Conservancy":
        desig = "State Nature Preserve" if "kitty todd" in name_lower else ""
        return "Nature Preserve", "Private Nature Preserve", desig, status

    # === SAJRD ===
    if gov == "Sylvania Area Joint Recreation District":
        if "quarry" in name_lower:
            return "Water Site", "Lake", "", status
        return "Park", "", "", status

    # === Olander Park System ===
    if gov == "Olander Park System":
        if "savanna" in name_lower:
            return "Natural Area", "Savanna", "", status
        if "herr road" in name_lower:
            return "Natural Area", "", "", status
        return "Park", "", "", status

    # === Howard Farms Conservancy District ===
    if gov == "Howard Farms Conservancy District":
        return "Wildlife Area", "Wetland Management Area", "", status

    # === University of Toledo ===
    if gov == "University of Toledo":
        return "Curated Biological Site", "Arboretum", "", status

    # === BSA / Camp Miakonda ===
    if gov == "Erie Shores Council, Boy Scouts of America":
        return "Campground", "Cabin Campground", "", status

    # === Old West End Association ===
    if "old west end" in gov.lower():
        return "Curated Biological Site", "Arboretum", "", status

    # === Owens Corning ===
    if gov == "Owens Corning":
        return "Open Space", "Urban Open Space", "", status

    # === Lucas County ===
    if "lucas county" in gov.lower():
        return "Fishing Area", "", "", status

    # === Ottawa Hills greenspace records ===
    if "greenspace" in name_lower:
        return "Open Space", "Urban Open Space", "", status

    # === Default: municipalities and townships → Park ===
    return "Park", "", "", status


# ════════════════════════════════════════════════════════════════════════════
#  TRAIL NORMALIZATION
# ════════════════════════════════════════════════════════════════════════════

def normalize_trail_vocab(r: dict):
    """Return (use_type, surface_type, origin_type, difficulty) for a Trail record."""
    name       = r.get("name_raw", "") or ""
    name_lower = name.lower()
    notes      = r.get("identity_notes_raw", "") or ""
    notes_low  = notes.lower()
    use_raw    = (r.get("use_type_raw", "") or "").lower()
    surf_raw   = (r.get("surface_raw", "") or "").lower()
    diff_raw   = (r.get("difficulty_raw", "") or "").lower()
    gov        = r.get("governance_raw", "") or ""

    # === Determine surface from raw or notes ===
    def _surf():
        if "boardwalk" in surf_raw or "boardwalk" in name_lower:
            return "Boardwalk"
        if "water trail" in name_lower or "maumee river water trail" == name_lower:
            return "Water"
        if "paved" in surf_raw or "hard-surface" in notes_low:
            return "Paved"
        if "boardwalk" in surf_raw:
            return "Boardwalk"
        if "crushed" in notes_low:
            return "Crushed Stone"
        if "native-material" in notes_low or "natural surface" in notes_low:
            return "Natural Surface"
        if "gravel" in surf_raw or "gravel" in notes_low:
            return "Gravel"
        return "Natural Surface"

    # === Determine use_type ===
    if "boardwalk" in surf_raw or "boardwalk" in name_lower:
        use_type    = "Hiking"
        surface     = "Boardwalk"
        origin      = "Purpose-Built"
    elif "water trail" in name_lower:
        use_type    = "Water"
        surface     = "Water"
        origin      = "Greenway Corridor"
    elif "singletrack" in notes_low or "mountain bike singletrack" in notes_low:
        use_type    = "Mountain Bike"
        surface     = "Natural Surface"
        origin      = "Purpose-Built"
    elif "ski trail" in name_lower or "ski trails" in name_lower:
        use_type    = "Cross Country Ski"
        surface     = "Natural Surface"
        origin      = "Purpose-Built"
    elif "horse trail" in name_lower or "bridle" in name_lower:
        use_type    = "Bridle"
        surface     = "Natural Surface"
        origin      = "Purpose-Built"
    elif "wabash cannonball" in name_lower:
        use_type    = "Multi-Use"
        surface     = "Mixed"
        origin      = "Rail Trail"
    elif "towpath" in name_lower or "canal" in name_lower:
        use_type    = "Multi-Use"
        surface     = "Crushed Stone" if "crushed" in notes_low else _surf()
        origin      = "Canal Towpath"
    elif ("all purpose" in name_lower or "walk/bike" in name_lower
          or ("bike" in name_lower and "all purpose" in name_lower)):
        use_type    = "Multi-Use"
        surface     = "Paved" if ("paved" in surf_raw or "hard-surface" in notes_low) else "Crushed Stone"
        origin      = "Purpose-Built"
    elif ("bicycle trail" in name_lower or "bike trail" in name_lower
          or "bike path" in name_lower or "bike" in name_lower):
        use_type    = "Bicycling"
        surface     = _surf()
        origin      = "Purpose-Built"
    elif "biking" in use_raw and "multi" in use_raw:
        use_type    = "Multi-Use"
        surface     = "Paved" if "paved" in surf_raw else _surf()
        origin      = "Purpose-Built"
    elif "biking" in use_raw:
        use_type    = "Bicycling"
        surface     = "Paved" if "paved" in surf_raw else _surf()
        origin      = "Purpose-Built"
    else:
        use_type    = "Hiking"
        surface     = _surf()
        origin      = "Purpose-Built"

    # Wabash Cannonball Connector follows parent rail trail logic
    if "wabash cannonball trail connector" in name_lower:
        use_type = "Multi-Use"
        surface  = "Paved"
        origin   = "Rail Trail"

    # Anthony Wayne Trail — undeveloped corridor
    if "anthony wayne trail" in name_lower:
        use_type = "Hiking"
        surface  = ""
        origin   = "Greenway Corridor"

    # University/Parks Trail — paved, shared-use
    if "university/parks trail" in name_lower:
        use_type = "Multi-Use"
        surface  = "Paved"
        origin   = "Purpose-Built"

    # Middlegrounds Walk/Bike Path
    if "middlegrounds walk/bike" in name_lower:
        use_type = "Multi-Use"
        surface  = "Paved"
        origin   = "Purpose-Built"

    # === Difficulty ===
    diff_map = {
        "easy": "Easy", "moderate": "Moderate",
        "difficult": "Difficult", "strenuous": "Strenuous", "expert": "Expert",
    }
    difficulty = ""
    for k, v in diff_map.items():
        if k in diff_raw:
            difficulty = v
            break

    return use_type, surface, origin, difficulty


# ════════════════════════════════════════════════════════════════════════════
#  ACCESS POINT NORMALIZATION
# ════════════════════════════════════════════════════════════════════════════

def normalize_ap_type(r: dict) -> str:
    name_lower = (r.get("name_raw", "") or "").lower()
    notes_low  = (r.get("identity_notes_raw", "") or "").lower()
    if "trailhead" in name_lower:
        return "Trailhead"
    if "marina" in name_lower:
        return "Boat Launch"
    if "boat ramp" in name_lower or "launch ramp" in name_lower:
        return "Boat Ramp"
    if "kayak" in name_lower or "paddling" in name_lower or "canoe" in name_lower:
        return "Watercraft Access Point"
    if "fishing" in name_lower and "pier" in name_lower:
        return "Fishing Access"
    if "fishing" in name_lower or "fish" in name_lower:
        return "Fishing Access"
    if "water trail" in name_lower:
        return "Watercraft Access Point"
    if "parking" in name_lower:
        return "Parking Area"
    return "Vehicle Entrance"


# ════════════════════════════════════════════════════════════════════════════
#  STAGE 1 — RESOLUTION
# ════════════════════════════════════════════════════════════════════════════

def load_and_resolve(yaml_path: Path):
    """
    Load raw YAML and apply resolution decisions:
      EXCLUDE: index 6  (Kitty Todd T2 duplicate — T7 canonical at index 334)
      EXCLUDE: index 285 (Chessie Circle Trail T6 — wrong governance, T3 idx 57 canonical)
      EXCLUDE: index 307 (Towpath Trail T6 Site — duplicate of T3 Trail idx 49)
      MERGE:   indices 283+284 → 1 Anthony Wayne Trail (keep 283, absorb 284 URL)
      MERGE:   indices 323+324 → 1 Ottawa Hills Greenspace (same address; keep 323)
      MERGE:   indices 331+332 → 1 Whitehouse Village Park (merge locations; keep 331)
      TRANSFER: index 6 designation "State Nature Preserve" → index 334 (already has it)
    Returns list of resolved raw records with _resolved_index metadata added.
    """
    data    = yaml.safe_load(yaml_path.read_text())
    records = data.get("records", [])

    EXCLUDES = {6, 285, 307}

    # Merge: Anthony Wayne Trail 283+284 → 283
    r283 = records[283]
    r284 = records[284]
    urls_283 = set((r283.get("urls_raw") or []))
    urls_284 = set((r284.get("urls_raw") or []))
    r283["urls_raw"] = sorted(urls_283 | urls_284)
    r283["identity_notes_raw"] = (
        (r283.get("identity_notes_raw") or "") +
        " Merged from two GIS records (indices 283+284); same trail, two GIS address points."
    ).strip()
    EXCLUDES.add(284)

    # Merge: Ottawa Hills Greenspace 323+324 → 323 (identical records, same address)
    EXCLUDES.add(324)

    # Merge: Whitehouse Village Park 331+332 → 331 (merge location notes)
    r331 = records[331]
    r332 = records[332]
    loc331 = r331.get("location_raw", "") or ""
    loc332 = r332.get("location_raw", "") or ""
    if loc332 and loc332 not in loc331:
        r331["location_raw"] = loc331 + "; " + loc332 if loc331 else loc332
    r331["identity_notes_raw"] = (
        (r331.get("identity_notes_raw") or "") +
        " Merged from two GIS address points (indices 331+332) for same park."
    ).strip()
    EXCLUDES.add(332)

    # Index 334: ensure Kitty Todd T7 has State Nature Preserve designation
    # (transferred from excluded index 6 — already noted in discovery)

    resolved = []
    for i, r in enumerate(records):
        if i in EXCLUDES:
            continue
        rc = dict(r)
        rc["_raw_index"] = i
        resolved.append(rc)

    # Partition by entity type
    sites    = [r for r in resolved if r["entity_type"] == "Site"]
    trails   = [r for r in resolved if r["entity_type"] == "Trail"]
    segments = [r for r in resolved if r["entity_type"] == "Trail Segment"]
    networks = [r for r in resolved if r["entity_type"] == "Trail Network"]
    site_nets= [r for r in resolved if r["entity_type"] == "Site Network"]
    aps      = [r for r in resolved if r["entity_type"] == "Access Point"]

    print(f"[Stage 1] Resolution complete.")
    print(f"  Raw records: {len(records)}  |  Excluded: {len(EXCLUDES)}")
    print(f"  Resolved → Sites: {len(sites)}, Trails: {len(trails)}, "
          f"Segments: {len(segments)}, Networks: {len(networks)}, "
          f"Site Networks: {len(site_nets)}, APs: {len(aps)}")

    return sites, trails, segments, networks, site_nets, aps


# ════════════════════════════════════════════════════════════════════════════
#  STAGE 2 — NORMALIZATION
# ════════════════════════════════════════════════════════════════════════════

def normalize_all(raw_sites, raw_trails, raw_segments, raw_networks,
                  raw_site_nets, raw_aps):
    """
    Normalize all entities. Assigns IDs, maps vocabulary fields, maps features.
    Returns (SITES, TRAILS, TRAIL_SEGMENTS, TRAIL_NETWORKS, SITE_NETWORKS, ACCESS_POINTS).
    """

    # ── Assign Site IDs ──────────────────────────────────────────────────────
    SITES = []
    name_to_site_id = {}   # for parent resolution

    for idx, r in enumerate(raw_sites, start=1):
        site_id  = f"{PREFIX}-S-{idx:03d}"
        name     = (r.get("name_raw") or "").strip()
        gov      = r.get("governance_raw", "") or ""
        own      = r.get("ownership_raw", "") or ""
        desc     = r.get("description_raw", "") or ""
        loc      = r.get("location_raw", "") or ""
        feats_r  = r.get("features_raw", "") or ""
        notes    = r.get("identity_notes_raw", "") or ""
        urls     = r.get("urls_raw")
        acres    = safe_acres(r.get("acres_raw"))
        counties = clean_counties(r.get("counties_raw"))
        gps_lat  = safe_float(r.get("gps_lat_raw"))
        gps_lon  = safe_float(r.get("gps_lon_raw"))
        gps_conf = "HIGH" if gps_lat is not None else "NONE"

        category, subtype, designation, status = normalize_site_vocab(r)
        features = map_features(feats_r)

        SITES.append({
            "site_id":          site_id,
            "name":             name,
            "category":         category,
            "subtype":          subtype,
            "designation":      designation,
            "status":           status,
            "ownership":        own,
            "governance":       gov,
            "partner_agencies": r.get("partner_agencies_raw", "") or "",
            "coordination":     r.get("coordination_raw", "") or "",
            "description":      desc,
            "location":         loc,
            "acres":            acres,
            "counties":         counties,
            "municipality":     "",   # GIS-derived in Stage 3
            "township":         "",   # GIS-derived in Stage 3
            "gps_lat":          gps_lat,
            "gps_lon":          gps_lon,
            "gps_confidence":   gps_conf,
            "plus_code":        "",
            "features":         features,
            "features_raw":     feats_r,
            "notes":            notes,
            "url_primary":      first_url(urls),
            "urls":             clean_urls(urls),
            "parent_site_id":   "",   # filled in second pass
            "_name_key":        name.strip().lower(),
            "_raw_index":       r["_raw_index"],
        })
        name_to_site_id[name.strip().lower()] = site_id

    # ── Second pass: fill parent_site_id (child sites within parent parks) ──
    # No explicit parent_site links exist in T6 raw data except Fossil Park note
    # and child sites that share an address with a parent.
    # (GPS propagation handles the rest via propagate_gps_to_children)

    # ── Assign Trail IDs ─────────────────────────────────────────────────────
    TRAILS = []
    for idx, r in enumerate(raw_trails, start=1):
        trail_id = f"{PREFIX}-T-{idx:03d}"
        name     = (r.get("name_raw") or "").strip()
        gov      = r.get("governance_raw", "") or ""
        own      = r.get("ownership_raw", "") or ""
        counties = clean_counties(r.get("counties_raw"))
        urls     = r.get("urls_raw")
        notes    = r.get("identity_notes_raw", "") or ""
        desc     = r.get("description_raw", "") or ""
        length   = r.get("length_raw", "") or ""
        access   = r.get("accessibility_raw", "") or ""

        # Attempt length parsing
        length_mi = None
        if length:
            m = re.search(r"(\d+\.?\d*)\s*mi", str(length).lower())
            if m:
                try:
                    length_mi = round(float(m.group(1)), 2)
                except Exception:
                    pass

        use_type, surface_type, origin_type, difficulty = normalize_trail_vocab(r)

        # Parent site resolution via parent_site_raw
        parent_name = (r.get("parent_site_raw", "") or "").strip().lower()
        parent_site_id = name_to_site_id.get(parent_name, "")

        gps_lat = safe_float(r.get("gps_lat_raw"))
        gps_lon = safe_float(r.get("gps_lon_raw"))

        TRAILS.append({
            "trail_id":         trail_id,
            "name":             name,
            "alternate_names":  "",
            "use_type":         use_type,
            "surface_type":     surface_type,
            "origin_type":      origin_type,
            "length_mi":        length_mi,
            "counties":         counties,
            "governance":       gov,
            "partner_agencies": r.get("partner_agencies_raw", "") or "",
            "status":           "Active",
            "difficulty":       difficulty,
            "accessibility":    access,
            "description":      desc,
            "trail_history":    "",
            "identity_notes":   notes,
            "notes":            "",
            "url_primary":      first_url(urls),
            "maps":             clean_urls(urls),
            "parent_site_id":   parent_site_id,
            "gps_lat":          gps_lat,
            "gps_lon":          gps_lon,
            "gps_confidence":   "HIGH" if gps_lat is not None else "NONE",
            "plus_code":        "",
            "_raw_index":       r["_raw_index"],
        })

    # ── Assign Trail Segment IDs ──────────────────────────────────────────────
    TRAIL_SEGMENTS = []
    for idx, r in enumerate(raw_segments, start=1):
        seg_id   = f"{PREFIX}-TS-{idx:03d}"
        name     = (r.get("name_raw") or "").strip()
        gov      = r.get("governance_raw", "") or ""
        notes    = r.get("identity_notes_raw", "") or ""
        urls     = r.get("urls_raw")
        counties = clean_counties(r.get("counties_raw"))

        # Length from identity notes
        length_mi = None
        m = re.search(r"(\d+)\s*mi(?:le)?", (notes or "").lower())
        if m:
            try:
                length_mi = round(float(m.group(1)), 2)
            except Exception:
                pass

        TRAIL_SEGMENTS.append({
            "trail_segment_id": seg_id,
            "name":             name,
            "counties":         counties,
            "governance":       gov,
            "length_mi":        length_mi,
            "surface_type":     "Mixed",
            "segment_type":     "Named Segment",
            "status":           "Active",
            "difficulty":       "",
            "accessibility":    "",
            "description":      r.get("description_raw", "") or "",
            "identity_notes":   notes,
            "notes":            "",
            "url_primary":      first_url(urls),
            "maps":             clean_urls(urls),
            "geometry":         "",
            "_raw_index":       r["_raw_index"],
        })

    # ── Assign Trail Network IDs ──────────────────────────────────────────────
    TRAIL_NETWORKS = []
    for idx, r in enumerate(raw_networks, start=1):
        net_id = f"{PREFIX}-TN-{idx:03d}"
        TRAIL_NETWORKS.append({
            "trail_network_id": net_id,
            "name":             (r.get("name_raw") or "").strip(),
            "network_type":     "Regional Trail Network",
            "status":           "Active",
            "ownership":        r.get("ownership_raw", "") or "",
            "governance":       r.get("governance_raw", "") or "",
            "partner_agencies": r.get("partner_agencies_raw", "") or "",
            "counties":         clean_counties(r.get("counties_raw")),
            "states_included":  "Ohio",
            "length_mi":        None,
            "member_trail_count": "",
            "member_trail_ids": "",
            "description":      r.get("description_raw", "") or "",
            "identity_notes":   r.get("identity_notes_raw", "") or "",
            "notes":            "",
            "url_primary":      first_url(r.get("urls_raw")),
            "maps":             clean_urls(r.get("urls_raw")),
            "_raw_index":       r["_raw_index"],
        })

    # ── Assign Site Network IDs ───────────────────────────────────────────────
    SITE_NETWORKS = []
    sn_member_names = {
        "metroparks toledo": [
            "Bend View Metropark", "Blue Creek Metropark",
            "Cannonball Prairie Metropark",
            "Fallen Timbers Battlefield & Fort Miamis Metropark",
            "Farnsworth Metropark", "Glass City Metropark", "Glass City Riverwalk",
            "Howard Marsh Metropark", "Manhattan Marsh Preserve Metropark",
            "Middlegrounds Metropark", "Oak Openings Preserve Metropark",
            "Oak Openings Beach Ridge Area", "Pearson Metropark",
            "Providence Metropark", "Secor Metropark", "Side Cut Metropark",
            "Swan Creek Preserve Metropark", "Toledo Botanical Garden Metropark",
            "Westwinds Metropark", "Wildwood Preserve Metropark",
            "Wiregrass Lake Metropark", "Audubon Islands",
            "Brookwood (special use area)",
        ],
        "sylvania area joint recreation district": [
            "Burnham Park", "Centennial Quarry", "Pacesetter Park",
            "Veterans Memorial Park",
        ],
        "olander park system": [
            "Herr Road Property", "Milton Olander Park", "Southview Oak Savanna",
            "Sylvan Prairie Park", "Whetstone Park", "Fossil Park",
        ],
    }

    for idx, r in enumerate(raw_site_nets, start=1):
        sn_id    = f"{PREFIX}-SN-{idx:03d}"
        name     = (r.get("name_raw") or "").strip()
        name_key = name.lower()
        gov      = r.get("governance_raw", "") or ""
        urls     = r.get("urls_raw")

        # Build member_site_ids from name lookup
        member_names = sn_member_names.get(name_key, [])
        member_ids   = [name_to_site_id[n.lower()] for n in member_names
                        if n.lower() in name_to_site_id]

        SITE_NETWORKS.append({
            "site_network_id": sn_id,
            "name":            name,
            "network_type":    "Multi-Site Recreation Network",
            "status":          "Active",
            "ownership":       r.get("ownership_raw", "") or "",
            "governance":      gov,
            "partner_agencies":r.get("partner_agencies_raw", "") or "",
            "counties":        clean_counties(r.get("counties_raw")),
            "states_included": "Ohio",
            "member_count":    len(member_ids),
            "member_site_ids": ";".join(member_ids),
            "description":     r.get("description_raw", "") or "",
            "identity_notes":  r.get("identity_notes_raw", "") or "",
            "notes":           "",
            "url_primary":     first_url(urls),
            "_raw_index":      r["_raw_index"],
        })

    # ── Assign Access Point IDs ───────────────────────────────────────────────
    # Parent site name map for APs (keyed to raw index of AP for precision)
    ap_parent_map = {
        2:   "Cedar Point National Wildlife Refuge",
        22:  "Maumee Bay State Park",
        23:  "Metzger Marsh Wildlife Area",
        24:  "Metzger Marsh Wildlife Area",
        25:  "Magee Marsh Wildlife Area",
        121: "Providence Metropark",
        122: "Farnsworth Metropark",
        123: "Glass City Metropark",
        124: "Glass City Metropark",
        125: "Middlegrounds Metropark",
        126: "Wiregrass Lake Metropark",
        127: "Fallen Timbers Battlefield & Fort Miamis Metropark",
        128: "Bend View Metropark",
        129: "Blue Creek Metropark",
        130: "Cannonball Prairie Metropark",
        131: "Oak Openings Beach Ridge Area",
        132: "Oak Openings Preserve Metropark",
        133: "Oak Openings Preserve Metropark",
        338: "Kitty Todd Nature Preserve",
        339: "Kitty Todd Nature Preserve",
        340: "Kitty Todd Nature Preserve",
    }

    ACCESS_POINTS = []
    for idx, r in enumerate(raw_aps, start=1):
        ap_id    = f"{PREFIX}-AP-{idx:03d}"
        name     = (r.get("name_raw") or "").strip()
        gov      = r.get("governance_raw", "") or ""
        raw_idx  = r["_raw_index"]
        urls     = r.get("urls_raw")
        notes    = r.get("identity_notes_raw", "") or ""
        loc      = r.get("location_raw", "") or ""

        parent_name    = ap_parent_map.get(raw_idx, "")
        parent_site_id = name_to_site_id.get(parent_name.lower(), "")

        ap_type  = normalize_ap_type(r)
        gps_lat  = safe_float(r.get("gps_lat_raw"))
        gps_lon  = safe_float(r.get("gps_lon_raw"))

        ACCESS_POINTS.append({
            "access_point_id":    ap_id,
            "name":               name,
            "ap_type":            ap_type,
            "status":             "Active",
            "parent_entity_type": "Site",
            "parent_entity_id":   parent_site_id,
            "county":             "Lucas",
            "township":           "",
            "municipality":       "",
            "address":            loc,
            "gps_lat":            gps_lat,
            "gps_lon":            gps_lon,
            "gps_confidence":     "HIGH" if gps_lat is not None else "NONE",
            "plus_code":          "",
            "features":           map_features(r.get("features_raw", "") or ""),
            "identity_notes":     notes,
            "notes":              "",
            "url_primary":        first_url(urls),
            "_raw_index":         raw_idx,
        })

    print(f"[Stage 2] Normalization complete.")
    print(f"  Sites: {len(SITES)}, Trails: {len(TRAILS)}, "
          f"Segments: {len(TRAIL_SEGMENTS)}, TrailNets: {len(TRAIL_NETWORKS)}, "
          f"SiteNets: {len(SITE_NETWORKS)}, APs: {len(ACCESS_POINTS)}")

    return SITES, TRAILS, TRAIL_SEGMENTS, TRAIL_NETWORKS, SITE_NETWORKS, ACCESS_POINTS


# ════════════════════════════════════════════════════════════════════════════
#  GPS QUERIES  (Stage 3 — Nominatim queries for sites missing GPS)
# ════════════════════════════════════════════════════════════════════════════

# Built after normalization so we can reference site IDs.
# Queries provided in priority order per IMP-081.
GPS_QUERIES_TEMPLATE = {
    # key = site name (lower), value = Nominatim query string
    "west sister island national wildlife refuge":
        "West Sister Island National Wildlife Refuge, Lake Erie, Ohio",
    "campbell state nature preserve":
        "Campbell State Nature Preserve, Lucas County, Ohio",
    "lanker wildlife area":
        "Lanker Wildlife Area, Grand Rapids, Ohio",
    "van tassel wildlife area":
        "Van Tassel Wildlife Area, Maumee River, Lucas County, Ohio",
    "cooley canal boat ramps":
        "Cooley Canal, Jerusalem Township, Lucas County, Ohio",
    "burnham park":
        "Burnham Park, Sylvania, Ohio",
    "centennial quarry":
        "Centennial Quarry, Sylvania, Ohio",
    "veterans memorial park":
        "Veterans Memorial Park, Sylvania, Ohio",
    "shoreland Park":
        "5470 Patriot Dr, Toledo, Ohio 43611",
    "shoreland park":
        "5470 Patriot Dr, Toledo, Ohio 43611",
    "monclova community park":
        "4335 Albon Road, Monclova, Ohio",
    "keener park":
        "4620 Keener Road, Monclova, Ohio",
    "ottawa wildlife refuge":
        "12581 Lagoon Dr, Lucas County, Ohio",
    # Metroparks sites missing GPS
    "brookwood (special use area)":
        "Brookwood, Swan Creek, Toledo, Ohio",
    "cannonball prairie metropark":
        "Cannonball Prairie Metropark, Lucas County, Ohio",
    "fallen timbers battlefield & fort miamis metropark":
        "Fallen Timbers Battlefield Metropark, Maumee, Ohio",
    "howard marsh metropark":
        "Howard Marsh Metropark, Lucas County, Ohio",
    "manhattan marsh preserve metropark":
        "Manhattan Marsh Preserve Metropark, Toledo, Ohio",
    "oak openings beach ridge area":
        "Oak Openings Beach Ridge Area, Lucas County, Ohio",
    "toledo botanical garden metropark":
        "Toledo Botanical Garden, Toledo, Ohio",
    "audubon islands":
        "Audubon Islands, Maumee River, Maumee, Ohio",
}

# Fallback GPS for all sites that need GPS acquisition.
# Entries confirmed via Nominatim have "MED" confidence; approximate fallbacks have "LOW".
GPS_FALLBACKS_TEMPLATE = {
    # Confirmed via Nominatim (first pipeline run)
    "howard marsh metropark":                      (41.646496, -83.261330),  # Nominatim MED
    "manhattan marsh preserve metropark":          (41.685855, -83.497757),  # Nominatim MED
    "toledo botanical garden metropark":           (41.665605, -83.672688),  # Nominatim MED
    "burnham park":                                (41.718509, -83.709628),  # Nominatim MED
    "centennial quarry":                           (41.720648, -83.744181),  # Nominatim MED
    "monclova community park":                     (41.559228, -83.737437),  # Nominatim MED
    "ottawa wildlife refuge":                      (41.652664, -83.242914),  # Nominatim MED
    # Approximate fallbacks (LOW confidence)
    "west sister island national wildlife refuge": (41.769,    -83.127),     # Lake Erie island
    "campbell state nature preserve":              (41.574,    -83.718),     # SW Lucas
    "van tassel wildlife area":                    (41.579,    -83.734),     # Maumee River area
    "cooley canal boat ramps":                     (41.680,    -83.257),     # Jerusalem Twp, Lake Erie
    "lanker wildlife area":                        (41.436,    -83.858),     # 1 mi NE of Grand Rapids
    "brookwood (special use area)":                (41.598,    -83.727),     # near Swan Creek Preserve
    "cannonball prairie metropark":                (41.537,    -83.760),     # SW Lucas, Swanton Rd
    "fallen timbers battlefield & fort miamis metropark": (41.560, -83.709), # Maumee, OH
    "oak openings beach ridge area":               (41.567,    -83.782),     # Eastmoreland Rd area
    "audubon islands":                             (41.566,    -83.659),     # Maumee River
    "veterans memorial park":                      (41.713,    -83.714),     # central Sylvania
    "shoreland park":                              (41.703,    -83.447),     # 5470 Patriot Dr, E Toledo
    "keener park":                                 (41.560,    -83.739),     # Keener Rd, Monclova
}

# Confidence override for fallbacks (default LOW; Nominatim-confirmed get MED)
GPS_FALLBACK_CONF_OVERRIDE = {
    "howard marsh metropark":             "MED",
    "manhattan marsh preserve metropark": "MED",
    "toledo botanical garden metropark":  "MED",
    "burnham park":                       "MED",
    "centennial quarry":                  "MED",
    "monclova community park":            "MED",
    "ottawa wildlife refuge":             "MED",
}


def build_gps_dicts(SITES, skip_nominatim: bool = False):
    """Build GPS_QUERIES and GPS_FALLBACKS keyed by site_id.

    skip_nominatim=True: omit all Nominatim queries; every missing site uses
    its fallback directly (avoids timeout in constrained environments).
    """
    GPS_QUERIES   = {}
    GPS_FALLBACKS = {}
    GPS_FALLBACK_CONF = {}

    for s in SITES:
        if s.get("gps_lat") is not None:
            continue
        key = s["name"].lower()
        if not skip_nominatim and key in GPS_QUERIES_TEMPLATE:
            GPS_QUERIES[s["site_id"]] = GPS_QUERIES_TEMPLATE[key]
        if key in GPS_FALLBACKS_TEMPLATE:
            GPS_FALLBACKS[s["site_id"]] = GPS_FALLBACKS_TEMPLATE[key]
            conf = GPS_FALLBACK_CONF_OVERRIDE.get(key, "LOW")
            GPS_FALLBACK_CONF[s["site_id"]] = conf

    return GPS_QUERIES, GPS_FALLBACKS, GPS_FALLBACK_CONF


# ════════════════════════════════════════════════════════════════════════════
#  MAIN PIPELINE RUNNER
# ════════════════════════════════════════════════════════════════════════════

def within_county_bounds(lat, lon):
    return (abs(lat - COUNTY_CENTROID_LAT) <= BBOX_BUFFER and
            abs(lon - COUNTY_CENTROID_LON) <= BBOX_BUFFER)


def run_pipeline(db_path: str, dry_run: bool = False, skip_nominatim: bool = False):
    import sqlite3, time

    print("=" * 60)
    print(f"NAP Pipeline  |  {COUNTY} County, {STATE}  |  {RUN_ID}")
    print(f"DB: {db_path}  |  Dry run: {dry_run}")
    print("=" * 60)

    # ── Stages 1 & 2 ─────────────────────────────────────────────────────────
    raw = load_and_resolve(RAW_YAML)
    SITES, TRAILS, TRAIL_SEGMENTS, TRAIL_NETWORKS, SITE_NETWORKS, ACCESS_POINTS = \
        normalize_all(*raw)

    # ── Stage 3: GPS Acquisition ──────────────────────────────────────────────
    print(f"\n[Stage 3] GPS Acquisition")
    if skip_nominatim:
        # Apply fallbacks directly without Nominatim queries.
        # acquire_gps only uses fallbacks when a query is present; bypass it here.
        _, GPS_FALLBACKS, GPS_FALLBACK_CONF = build_gps_dicts(SITES, skip_nominatim=False)
        applied = 0
        for s in SITES:
            if s.get("gps_lat") is None and s["site_id"] in GPS_FALLBACKS:
                lat, lon = GPS_FALLBACKS[s["site_id"]]
                s["gps_lat"] = round(lat, 6)
                s["gps_lon"] = round(lon, 6)
                s["gps_confidence"] = GPS_FALLBACK_CONF.get(s["site_id"], "LOW")
                applied += 1
                print(f"  GPS [{s['site_id']}]: fallback {lat}, {lon} "
                      f"({s['gps_confidence']})")
        print(f"  Applied {applied} fallback GPS coordinates (Nominatim skipped)")
    else:
        GPS_QUERIES, GPS_FALLBACKS, GPS_FALLBACK_CONF = build_gps_dicts(SITES, False)
        acquire_gps(SITES, "site_id", GPS_QUERIES, GPS_FALLBACKS, GPS_FALLBACK_CONF)
    propagate_gps_to_children(SITES)
    propagate_gps_to_trails(TRAILS, SITES)
    propagate_gps_to_aps(ACCESS_POINTS, SITES)
    add_plus_codes(SITES)
    add_plus_codes(TRAILS)
    add_plus_codes(ACCESS_POINTS)
    add_gis_lookup(SITES)
    add_gis_lookup(ACCESS_POINTS)

    gps_ok = sum(1 for s in SITES if s.get("gps_lat") is not None)
    print(f"  GPS acquired/available: {gps_ok}/{len(SITES)} sites")

    # ── Stage 4.5: Vocabulary Validation Gate ─────────────────────────────────
    print(f"\n[Stage 4.5] Vocabulary Validation Gate")
    run_vocab_gate(SITES, TRAILS, ACCESS_POINTS)

    # ── Stage 4: TSV Output ───────────────────────────────────────────────────
    print(f"\n[Stage 4] TSV Output")
    write_all_tsvs(OUTPUT_DIR, PREFIX, NOW,
                   SITES, TRAILS, TRAIL_SEGMENTS,
                   TRAIL_NETWORKS, SITE_NETWORKS, ACCESS_POINTS)

    # ── Stage 5: Integrity Check ──────────────────────────────────────────────
    print(f"\n[Stage 5] Integrity Check")
    warnings = integrity_check(SITES, TRAILS, ACCESS_POINTS)
    if warnings:
        for w in warnings:
            print(f"  WARNING: {w}")
    else:
        print("  No integrity issues found.")

    # ── Stage 6: Database Upsert ──────────────────────────────────────────────
    print(f"\n[Stage 6] Database Upsert")
    normalized = (len(SITES) + len(TRAILS) + len(ACCESS_POINTS) +
                  len(TRAIL_SEGMENTS) + len(TRAIL_NETWORKS) + len(SITE_NETWORKS))
    run_notes = (
        f"Lucas County OH pipeline complete. "
        f"{len(SITES)} Sites, {len(TRAILS)} Trails, {len(TRAIL_SEGMENTS)} Trail Segments, "
        f"{len(TRAIL_NETWORKS)} Trail Networks, {len(SITE_NETWORKS)} Site Networks, "
        f"{len(ACCESS_POINTS)} APs. "
        f"Raw records: 348; excluded 6 (3 duplicates + 3 merges collapsed)."
    )

    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        upsert_sites(cur, SITES, NOW, dry_run)
        upsert_site_parents(cur, SITES, dry_run)
        upsert_trails(cur, TRAILS, NOW, dry_run)
        upsert_trail_parents(cur, TRAILS, dry_run)
        upsert_access_points(cur, ACCESS_POINTS, NOW, dry_run)
        upsert_run_metadata(cur, RUN_ID, COUNTY, STATE, RUN_DATE,
                            348, normalized, 0, run_notes, NOW, dry_run)
        if not dry_run:
            conn.commit()
            print(f"  Committed {len(SITES)} sites, {len(TRAILS)} trails, "
                  f"{len(ACCESS_POINTS)} APs to {os.path.basename(db_path)}")
    except Exception as e:
        conn.rollback()
        print(f"  ERROR during upsert: {e}", file=sys.stderr)
        raise
    finally:
        conn.close()

    # -- Summary
    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE")
    print(f"  Sites:          {len(SITES)}")
    print(f"  Trails:         {len(TRAILS)}")
    print(f"  Trail Segments: {len(TRAIL_SEGMENTS)}")
    print(f"  Trail Networks: {len(TRAIL_NETWORKS)}")
    print(f"  Site Networks:  {len(SITE_NETWORKS)}")
    print(f"  Access Points:  {len(ACCESS_POINTS)}")
    missing_gps = [s["site_id"] for s in SITES if s.get("gps_lat") is None]
    if missing_gps:
        print(f"  Sites still missing GPS ({len(missing_gps)}): {', '.join(missing_gps)}")
    print