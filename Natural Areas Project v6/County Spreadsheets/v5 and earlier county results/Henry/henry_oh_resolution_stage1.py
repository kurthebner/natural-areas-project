"""
Henry County, OH — Stage 1 Resolution Engine
Natural Areas Project v5.x Pipeline

Executes all 5 phases of the Resolution Engine v5.5 against henry_oh_raw_discovery.yaml.
Produces henry_oh_resolved_entities.yaml and a resolution report.

Rules: na_resolution_engine_v5.5.md + na_resolution_rules_v5.3.md
"""

import yaml
import pathlib
import re
import difflib
import uuid
from collections import defaultdict
from datetime import datetime

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────────────────────────────────────

RUN_ID = "henry_oh_2026_04_20"
PREFIX = "HEN"
COUNTY_PRIMARY_CANONICAL = "Henry County, OH"
RUN_DATE = "2026-04-21"

# Merge thresholds (per entity type, keyed by entity_type)
MERGE_THRESHOLD = {
    "Site": 80,
    "Trail": 80,
    "Trail Segment": 80,
    "Trail Network": 80,
    "Site Network": 80,
    "Access Point": 80,
}
REVIEW_THRESHOLD = {
    "Site": 50,
    "Trail": 50,
    "Trail Segment": 50,
    "Trail Network": 50,
    "Site Network": 50,
    "Access Point": 50,
}

# GPS proximity bucket: round to 3 decimal places
GPS_BUCKET_PRECISION = 3

# Hard separation: Sites (and APs) with GPS coordinates more than this many
# degrees apart are definitively distinct entities (§10.5 — identity anchor
# contradiction discovered post-scoring). ~0.01° ≈ 1 km in Ohio.
GPS_HARD_SEP_DEG = 0.01

INPUT_PATH = pathlib.Path(
    "/sessions/trusting-sweet-gates/mnt/Natural Areas Project v5/henry_oh_raw_discovery.yaml"
)
OUTPUT_PATH = pathlib.Path(
    "/sessions/trusting-sweet-gates/mnt/Natural Areas Project v5/henry_oh_resolved_entities.yaml"
)
REPORT_PATH = pathlib.Path(
    "/sessions/trusting-sweet-gates/mnt/Natural Areas Project v5/henry_oh_resolution_report.md"
)

# ──────────────────────────────────────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────────────────────────────────────

def normalize_county(raw: str) -> str:
    """Strip state suffix and 'County' suffix for comparison only."""
    if not raw:
        return ""
    s = raw.strip()
    # Remove state suffix
    s = re.sub(r",?\s*(Ohio|OH)\s*$", "", s, flags=re.IGNORECASE).strip()
    # Remove 'County' suffix
    s = re.sub(r"\s+County\s*$", "", s, flags=re.IGNORECASE).strip()
    return s.lower()


def counties_normalized(counties_raw: list) -> set:
    """Return a set of normalized county tokens from a counties_raw list."""
    result = set()
    for c in (counties_raw or []):
        result.add(normalize_county(c))
    return result


def fuzzy_name_score(a: str, b: str) -> float:
    """Return 0-1 fuzzy name similarity (matching-only, not for output)."""
    if not a or not b:
        return 0.0
    a_norm = re.sub(r"[^\w\s]", "", a.lower()).strip()
    b_norm = re.sub(r"[^\w\s]", "", b.lower()).strip()
    # Use SequenceMatcher + token sort ratio
    seq = difflib.SequenceMatcher(None, a_norm, b_norm).ratio()
    # Token sort: sort tokens, join, compare
    a_tokens = " ".join(sorted(a_norm.split()))
    b_tokens = " ".join(sorted(b_norm.split()))
    tok = difflib.SequenceMatcher(None, a_tokens, b_tokens).ratio()
    return max(seq, tok)


def counties_overlap(ca: list, cb: list) -> bool:
    """True if any normalized county appears in both lists."""
    return bool(counties_normalized(ca) & counties_normalized(cb))


def gps_bucket(lat, lon):
    """Return GPS proximity bucket tuple or None if GPS missing."""
    try:
        return (round(float(lat), GPS_BUCKET_PRECISION),
                round(float(lon), GPS_BUCKET_PRECISION))
    except (TypeError, ValueError):
        return None


# ──────────────────────────────────────────────────────────────────────────────
# PHASE 1 — GROUPING
# ──────────────────────────────────────────────────────────────────────────────

def phase1_grouping(records: list) -> dict:
    """
    Partition records into groups keyed by (entity_type, county_primary_normalized).
    Multi-county records are added to ALL relevant county groups.
    Records with county_primary=None use counties_raw to derive membership.
    Returns: dict[(entity_type, county_key)] → [list of record indices]
    """
    groups = defaultdict(list)

    for idx, rec in enumerate(records):
        et = rec["entity_type"]
        cp_raw = rec.get("county_primary") or ""
        counties_raw = rec.get("counties_raw") or []

        # Determine which county groups this record belongs to
        group_counties = set()

        if cp_raw:
            group_counties.add(normalize_county(cp_raw))

        # For multi-county records, also add all other counties in counties_raw
        for c in counties_raw:
            group_counties.add(normalize_county(c))

        # Fallback: if still empty, use a placeholder
        if not group_counties:
            group_counties.add("unknown")

        for county_key in group_counties:
            groups[(et, county_key)].append(idx)

    return dict(groups)


# ──────────────────────────────────────────────────────────────────────────────
# PHASE 2 — IDENTITY MATCHING (Anchors + Similarity Scoring)
# ──────────────────────────────────────────────────────────────────────────────

ANCHOR_NAME_THRESHOLD = 0.40  # minimum fuzzy name score for anchor to pass

def anchor_site(ra, rb) -> bool:
    """Site identity anchor: fuzzy name match + county overlap."""
    name_score = fuzzy_name_score(ra.get("name_raw", ""), rb.get("name_raw", ""))
    if name_score < ANCHOR_NAME_THRESHOLD:
        return False
    return counties_overlap(ra.get("counties_raw", []), rb.get("counties_raw", []))


def anchor_trail(ra, rb) -> bool:
    """Trail identity anchor: fuzzy name match + county overlap."""
    name_score = fuzzy_name_score(ra.get("name_raw", ""), rb.get("name_raw", ""))
    if name_score < ANCHOR_NAME_THRESHOLD:
        return False
    return counties_overlap(ra.get("counties_raw", []), rb.get("counties_raw", []))


def anchor_trail_segment(ra, rb) -> bool:
    """
    Trail Segment anchor: parent trail must match; if both have segment names, fuzzy match.
    Parent trail is matched via name in identity_notes_raw or parent_trail_name_raw.
    """
    pa = (ra.get("parent_trail_name_raw") or
          _extract_parent_trail_from_notes(ra.get("identity_notes_raw", "") or ""))
    pb = (rb.get("parent_trail_name_raw") or
          _extract_parent_trail_from_notes(rb.get("identity_notes_raw", "") or ""))
    if pa and pb:
        if fuzzy_name_score(pa, pb) < ANCHOR_NAME_THRESHOLD:
            return False
    # If both have segment names, check them
    na = ra.get("name_raw", "")
    nb = rb.get("name_raw", "")
    if na and nb:
        return fuzzy_name_score(na, nb) >= ANCHOR_NAME_THRESHOLD
    return True


def anchor_access_point(ra, rb) -> bool:
    """
    Access Point anchor: identity_parent_entity_id match + GPS proximity bucket.
    Parent identity is extracted from identity_notes_raw if formal field is blank.
    """
    pa = (ra.get("identity_parent_entity_id_raw") or
          _extract_ap_parent_from_notes(ra.get("identity_notes_raw", "") or ""))
    pb = (rb.get("identity_parent_entity_id_raw") or
          _extract_ap_parent_from_notes(rb.get("identity_notes_raw", "") or ""))

    # Parent must match (fuzzy)
    if pa and pb:
        if fuzzy_name_score(pa, pb) < ANCHOR_NAME_THRESHOLD:
            return False
    elif pa or pb:
        # One has parent, one doesn't — anchor fails
        return False

    # GPS proximity bucket must match
    ba = gps_bucket(ra.get("gps_lat_raw"), ra.get("gps_lon_raw"))
    bb = gps_bucket(rb.get("gps_lat_raw"), rb.get("gps_lon_raw"))
    if ba is None or bb is None:
        return False  # Can't determine proximity without GPS
    return ba == bb


def _extract_parent_trail_from_notes(notes: str) -> str:
    """Extract parent trail name from identity_notes_raw free text."""
    m = re.search(r"[Pp]arent.*?[Tt]rail[:\s]+([^\.\n;]+)", notes)
    if m:
        return m.group(1).strip()
    # Also try "Parent: X"
    m = re.search(r"[Pp]arent:\s+([^\.\n;]+)", notes)
    if m:
        return m.group(1).strip()
    return ""


def _extract_ap_parent_from_notes(notes: str) -> str:
    """Extract parent site/trail name from AP identity_notes_raw."""
    m = re.search(r"[Pp]arent site:\s+([^\.\n;(]+)", notes)
    if m:
        return m.group(1).strip()
    m = re.search(r"[Pp]arent trail:\s+([^\.\n;/]+)", notes)
    if m:
        return m.group(1).strip()
    m = re.search(r"[Cc]hild access point of\s+([^\.\n;]+)\.", notes)
    if m:
        return m.group(1).strip()
    return ""


def _extract_ap_parent_from_name(ap_name: str, trail_names: list) -> str:
    """
    For APs whose name begins with a known trail name (e.g. 'Wabash Cannonball
    Trail Liberty Center Depot Trailhead'), extract the trail as parent.
    """
    if not ap_name:
        return ""
    for tname in sorted(trail_names, key=len, reverse=True):
        if ap_name.lower().startswith(tname.lower()):
            return tname
    return ""


def _extract_parent_from_segment_name(seg_name: str) -> str:
    """
    M&E Canal Towpath segments follow the pattern:
    'Segment Name — Parent Trail Name'
    Extract the parent trail from the em-dash separator.
    """
    if " — " in seg_name:
        return seg_name.split(" — ", 1)[1].strip()
    return ""


def score_site(ra, rb) -> float:
    """Site identity signature: name 40, org 35, county 10, location 10, URL 5."""
    score = 0.0
    # Name (40)
    score += 40 * fuzzy_name_score(ra.get("name_raw", ""), rb.get("name_raw", ""))
    # Organizational (35): governance + ownership
    gov_a = (ra.get("governance_raw") or "") + " " + (ra.get("ownership_raw") or "")
    gov_b = (rb.get("governance_raw") or "") + " " + (rb.get("ownership_raw") or "")
    score += 35 * fuzzy_name_score(gov_a.strip(), gov_b.strip())
    # County overlap (10)
    ca = counties_normalized(ra.get("counties_raw", []))
    cb = counties_normalized(rb.get("counties_raw", []))
    if ca and cb:
        overlap = len(ca & cb) / max(len(ca | cb), 1)
        score += 10 * overlap
    # Location (10)
    la = ra.get("location_raw") or ""
    lb = rb.get("location_raw") or ""
    if la and lb:
        score += 10 * fuzzy_name_score(la[:60], lb[:60])
    # URL (5)
    ua = set(ra.get("urls_raw") or [])
    ub = set(rb.get("urls_raw") or [])
    if ua and ub and ua & ub:
        score += 5
    return score


def score_trail(ra, rb) -> float:
    """Trail identity signature: name 40, use 15, length 15, gov 10, county 10, surface 5, URL 5."""
    score = 0.0
    score += 40 * fuzzy_name_score(ra.get("name_raw", ""), rb.get("name_raw", ""))
    # Use type (15)
    ua = ra.get("trail_use_type_raw") or ""
    ub = rb.get("trail_use_type_raw") or ""
    if ua and ub:
        score += 15 * fuzzy_name_score(ua, ub)
    # Length (15) — skip if blank
    la = ra.get("total_length_miles_raw")
    lb = rb.get("total_length_miles_raw")
    if la and lb:
        try:
            la_f, lb_f = float(la), float(lb)
            diff = abs(la_f - lb_f) / max(la_f, lb_f, 0.001)
            score += 15 * max(0, 1 - diff)
        except (ValueError, TypeError):
            pass
    # Governance (10)
    score += 10 * fuzzy_name_score(
        ra.get("governance_raw") or "", rb.get("governance_raw") or "")
    # County overlap (10)
    ca = counties_normalized(ra.get("counties_raw", []))
    cb = counties_normalized(rb.get("counties_raw", []))
    if ca and cb:
        overlap = len(ca & cb) / max(len(ca | cb), 1)
        score += 10 * overlap
    # Surface (5)
    sa = ra.get("trail_surface_type_raw") or ""
    sb = rb.get("trail_surface_type_raw") or ""
    if sa and sb:
        score += 5 * fuzzy_name_score(sa, sb)
    # URL (5)
    ua = set(ra.get("urls_raw") or [])
    ub = set(rb.get("urls_raw") or [])
    if ua and ub and ua & ub:
        score += 5
    return score


def score_trail_segment(ra, rb) -> float:
    """Trail Segment signature: seg name 50, length 20, surface 15, county 10, seg type 5."""
    score = 0.0
    score += 50 * fuzzy_name_score(ra.get("name_raw", ""), rb.get("name_raw", ""))
    la = ra.get("segment_length_miles_raw")
    lb = rb.get("segment_length_miles_raw")
    if la and lb:
        try:
            la_f, lb_f = float(la), float(lb)
            diff = abs(la_f - lb_f) / max(la_f, lb_f, 0.001)
            score += 20 * max(0, 1 - diff)
        except (ValueError, TypeError):
            pass
    sa = ra.get("surface_type_raw") or ""
    sb = rb.get("surface_type_raw") or ""
    if sa and sb:
        score += 15 * fuzzy_name_score(sa, sb)
    ca = counties_normalized(ra.get("counties_raw", []))
    cb = counties_normalized(rb.get("counties_raw", []))
    if ca and cb:
        overlap = len(ca & cb) / max(len(ca | cb), 1)
        score += 10 * overlap
    ta = ra.get("segment_type_raw") or ""
    tb = rb.get("segment_type_raw") or ""
    if ta and tb:
        score += 5 * fuzzy_name_score(ta, tb)
    return score


def score_access_point(ra, rb) -> float:
    """AP signature: parent 40, GPS 30, type 20, name 10."""
    score = 0.0
    pa = _extract_ap_parent_from_notes(ra.get("identity_notes_raw", "") or "")
    pb = _extract_ap_parent_from_notes(rb.get("identity_notes_raw", "") or "")
    if pa and pb:
        score += 40 * fuzzy_name_score(pa, pb)
    ba = gps_bucket(ra.get("gps_lat_raw"), ra.get("gps_lon_raw"))
    bb = gps_bucket(rb.get("gps_lat_raw"), rb.get("gps_lon_raw"))
    if ba and bb and ba == bb:
        score += 30
    ta = ra.get("access_point_type_raw") or ""
    tb = rb.get("access_point_type_raw") or ""
    if ta and tb:
        score += 20 * fuzzy_name_score(ta, tb)
    score += 10 * fuzzy_name_score(ra.get("name_raw", ""), rb.get("name_raw", ""))
    return score


ANCHOR_FN = {
    "Site": anchor_site,
    "Trail": anchor_trail,
    "Trail Segment": anchor_trail_segment,
    "Access Point": anchor_access_point,
}

SCORE_FN = {
    "Site": score_site,
    "Trail": score_trail,
    "Trail Segment": score_trail_segment,
    "Access Point": score_access_point,
}


def phase2_identity_matching(records: list, groups: dict) -> dict:
    """
    Compute pairwise similarity matrices for each group.
    Returns: dict[(entity_type, county_key)] → dict[(i, j)] → score or None
    """
    matrices = {}

    for group_key, idxs in groups.items():
        et = group_key[0]
        anchor_fn = ANCHOR_FN.get(et)
        score_fn = SCORE_FN.get(et)
        if not anchor_fn or len(idxs) < 2:
            matrices[group_key] = {}
            continue

        matrix = {}
        for ii in range(len(idxs)):
            for jj in range(ii + 1, len(idxs)):
                i, j = idxs[ii], idxs[jj]
                ra, rb = records[i], records[j]
                if anchor_fn(ra, rb):
                    s = score_fn(ra, rb)
                    matrix[(i, j)] = round(s, 1)
                else:
                    matrix[(i, j)] = None  # anchor failed
        matrices[group_key] = matrix

    return matrices


# ──────────────────────────────────────────────────────────────────────────────
# PHASE 3 — MERGE DECISIONS
# ──────────────────────────────────────────────────────────────────────────────

def hard_separate(ra: dict, rb: dict) -> str | None:
    """
    Apply §10.5 hard separation conditions.
    Returns a string reason if the pair must remain separate, or None if no
    hard separation condition is triggered.
    Checked BEFORE applying merge threshold.
    """
    et = ra.get("entity_type")

    # ── GPS hard separation (Sites and Access Points) ──────────────────────
    # When both records have GPS that differ by more than GPS_HARD_SEP_DEG in
    # either axis, they are definitively at different physical locations and
    # cannot be the same entity.
    if et in ("Site", "Access Point"):
        lat_a = ra.get("gps_lat_raw")
        lon_a = ra.get("gps_lon_raw")
        lat_b = rb.get("gps_lat_raw")
        lon_b = rb.get("gps_lon_raw")
        if lat_a and lon_a and lat_b and lon_b:
            try:
                dlat = abs(float(lat_a) - float(lat_b))
                dlon = abs(float(lon_a) - float(lon_b))
                if dlat > GPS_HARD_SEP_DEG or dlon > GPS_HARD_SEP_DEG:
                    return (f"GPS hard separation: lat_diff={dlat:.4f}, "
                            f"lon_diff={dlon:.4f} > {GPS_HARD_SEP_DEG}")
            except (ValueError, TypeError):
                pass

    # ── Numbered-name hard separation ──────────────────────────────────────
    # Records whose names are identical except for a trailing number are
    # definitively distinct entities (e.g., "Wildlife Area 1" vs "Wildlife
    # Area 2").
    name_a = (ra.get("name_raw") or "").strip()
    name_b = (rb.get("name_raw") or "").strip()
    if name_a and name_b and name_a != name_b:
        stem_a = re.sub(r'\s+\d+$', '', name_a)
        stem_b = re.sub(r'\s+\d+$', '', name_b)
        num_a = re.search(r'\d+$', name_a)
        num_b = re.search(r'\d+$', name_b)
        if (stem_a == stem_b and stem_a != name_a and stem_b != name_b
                and num_a and num_b and num_a.group() != num_b.group()):
            return (f"Numbered-name hard separation: '{name_a}' vs '{name_b}' — "
                    f"same stem '{stem_a}', different ordinal")

    return None


def phase3_merge_decisions(records: list, groups: dict, matrices: dict):
    """
    Convert similarity scores into merge clusters and review sets.
    Returns:
      - merge_clusters: list of frozensets of record indices
      - review_sets: list of dicts
      - singletons: list of record indices with no merge or review pair
    """
    # Build adjacency: index → set of indices it merges with
    merge_graph = defaultdict(set)
    review_sets = []
    scored_pairs = set()

    for group_key, idxs in groups.items():
        et = group_key[0]
        merge_thresh = MERGE_THRESHOLD[et]
        review_thresh = REVIEW_THRESHOLD[et]
        matrix = matrices.get(group_key, {})

        for (i, j), score in matrix.items():
            if score is None:
                continue  # anchor failed
            pair_key = (min(i, j), max(i, j))
            if pair_key in scored_pairs:
                continue
            scored_pairs.add(pair_key)

            ra, rb = records[i], records[j]

            # Apply §10.5 hard separation conditions BEFORE threshold
            hs_reason = hard_separate(ra, rb)
            if hs_reason:
                # Hard separation overrides score — emit as REVIEW if score
                # was above review threshold (human may still want visibility)
                if score >= review_thresh:
                    review_sets.append({
                        "record_ids": [i, j],
                        "record_names": [ra.get("name_raw"), rb.get("name_raw")],
                        "entity_type": et,
                        "similarity_score": score,
                        "group_key": f"{group_key[0]}|{group_key[1]}",
                        "anchor_pass": True,
                        "merge_threshold": merge_thresh,
                        "review_threshold": review_thresh,
                        "hard_separation": True,
                        "hard_separation_reason": hs_reason,
                        "note": f"HARD SEPARATED (§10.5): {hs_reason}",
                    })
                continue  # skip merge graph

            if score >= merge_thresh:
                merge_graph[i].add(j)
                merge_graph[j].add(i)
            elif score >= review_thresh:
                review_sets.append({
                    "record_ids": [i, j],
                    "record_names": [ra.get("name_raw"), rb.get("name_raw")],
                    "entity_type": et,
                    "similarity_score": score,
                    "group_key": f"{group_key[0]}|{group_key[1]}",
                    "anchor_pass": True,
                    "merge_threshold": merge_thresh,
                    "review_threshold": review_thresh,
                    "note": "Score between REVIEW and MERGE threshold — requires human review",
                })

    # Connected components = merge clusters
    seen = set()
    merge_clusters = []
    for start in merge_graph:
        if start in seen:
            continue
        component = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            component.add(node)
            stack.extend(merge_graph[node] - seen)
        merge_clusters.append(frozenset(component))

    # All indices that appear in a merge cluster
    clustered = set()
    for c in merge_clusters:
        clustered.update(c)

    # Singletons: indices not in any merge cluster
    all_idxs = set(range(len(records)))
    singletons = sorted(all_idxs - clustered)

    return merge_clusters, review_sets, singletons


# ──────────────────────────────────────────────────────────────────────────────
# PHASE 4 — FIELD-LEVEL MERGING
# ──────────────────────────────────────────────────────────────────────────────

def _choose_or_conflict(field_name: str, values_with_sources: list) -> tuple:
    """
    Returns (chosen_value, conflict_entry_or_None).
    If all agree → chosen. If disagree → conflict recorded.
    Values: list of (value, record_idx, tier)
    """
    distinct = {}
    for val, ridx, tier in values_with_sources:
        if val is not None and str(val).strip():
            k = str(val).strip().lower()
            if k not in distinct:
                distinct[k] = (val, ridx, tier)

    if len(distinct) == 0:
        return None, None
    if len(distinct) == 1:
        return list(distinct.values())[0][0], None
    # Conflict — sort by tier (lower = higher authority), choose lowest tier
    sorted_vals = sorted(distinct.values(), key=lambda x: x[2] if x[2] else 999)
    conflict = {
        "field": field_name,
        "values": [{"value": v, "record_idx": r, "tier": t}
                   for v, r, t in distinct.values()],
        "note": "choose_or_conflict: multiple distinct values; tier-preferred value shown in identity_block"
    }
    return sorted_vals[0][0], conflict


def _union(field_name: str, lists_with_sources: list) -> list:
    """Combine all distinct values from multiple lists."""
    seen = set()
    result = []
    for lst, _, _ in lists_with_sources:
        if not lst:
            continue
        for item in (lst if isinstance(lst, list) else [lst]):
            k = str(item).strip().lower()
            if k not in seen:
                seen.add(k)
                result.append(item)
    return result


def phase4_merge_fields(records: list, cluster: frozenset) -> dict:
    """
    Merge all fields for a cluster using the v5.5 field strategies.
    Returns a merged entity dict with all blocks.
    """
    cluster_records = [(records[i], i) for i in sorted(cluster)]
    conflicts = []

    def vals(field):
        return [(r.get(field), i, r.get("discovery_tier", 99))
                for r, i in cluster_records]

    # ── Identity block ──
    name_raw, conf = _choose_or_conflict("name_raw", vals("name_raw"))
    if conf:
        conflicts.append(conf)

    counties_raw = _union("counties_raw",
                          [(r.get("counties_raw"), i, r.get("discovery_tier", 99))
                           for r, i in cluster_records])

    urls_raw = _union("urls_raw",
                      [(r.get("urls_raw"), i, r.get("discovery_tier", 99))
                       for r, i in cluster_records])

    location_raw, conf = _choose_or_conflict("location_raw", vals("location_raw"))
    if conf:
        conflicts.append(conf)

    # ── Organizational block ──
    ownership_raw, conf = _choose_or_conflict("ownership_raw", vals("ownership_raw"))
    if conf:
        conflicts.append(conf)

    governance_raw, conf = _choose_or_conflict("governance_raw", vals("governance_raw"))
    if conf:
        conflicts.append(conf)

    partner_agencies_raw = _union("partner_agencies_raw",
                                  [(r.get("partner_agencies_raw"), i, r.get("discovery_tier", 99))
                                   for r, i in cluster_records])

    coordination_raw = _union("coordination_raw",
                              [(r.get("coordination_raw"), i, r.get("discovery_tier", 99))
                               for r, i in cluster_records])

    # ── Entity-type specific payload ──
    et = cluster_records[0][0]["entity_type"]
    payload = {}

    if et in ("Trail", "Trail Segment"):
        for field in ["trail_use_type_raw", "trail_surface_type_raw",
                      "trail_origin_type_raw", "surface_type_raw",
                      "segment_type_raw", "difficulty_raw", "accessibility_raw"]:
            v, conf = _choose_or_conflict(field, vals(field))
            payload[field] = v
            if conf:
                conflicts.append(conf)

        # Quantitative — conflict strategy
        for field in ["total_length_miles_raw", "segment_length_miles_raw"]:
            all_vals = [v for v, _, _ in vals(field) if v is not None]
            if len(set(str(x) for x in all_vals)) > 1:
                conflicts.append({
                    "field": field,
                    "values": [{"value": v, "record_idx": i, "tier": t}
                               for v, i, t in vals(field) if v is not None],
                    "note": "conflict: quantitative field with multiple values"
                })
                payload[field] = all_vals  # preserve all
            elif all_vals:
                payload[field] = all_vals[0]
            else:
                payload[field] = None

    if et == "Access Point":
        # GPS — conflict strategy
        lats = [(v, i, t) for v, i, t in vals("gps_lat_raw") if v is not None]
        lons = [(v, i, t) for v, i, t in vals("gps_lon_raw") if v is not None]
        if len(set(str(x[0]) for x in lats)) > 1:
            conflicts.append({"field": "gps_lat_raw",
                               "values": [{"value": v, "record_idx": i, "tier": t}
                                          for v, i, t in lats],
                               "note": "conflict"})
        payload["gps_lat_raw"] = lats[0][0] if lats else None
        if len(set(str(x[0]) for x in lons)) > 1:
            conflicts.append({"field": "gps_lon_raw",
                               "values": [{"value": v, "record_idx": i, "tier": t}
                                          for v, i, t in lons],
                               "note": "conflict"})
        payload["gps_lon_raw"] = lons[0][0] if lons else None

        v, conf = _choose_or_conflict("access_point_type_raw", vals("access_point_type_raw"))
        payload["access_point_type_raw"] = v
        if conf:
            conflicts.append(conf)

    if et == "Site":
        # Carry through site-specific fields
        for field in ["description_raw", "features_raw", "acres_raw",
                      "category_raw", "status_raw"]:
            v, conf = _choose_or_conflict(field, vals(field))
            payload[field] = v
            if conf:
                conflicts.append(conf)
        # GPS for sites
        lats = [(v, i, t) for v, i, t in vals("gps_lat_raw") if v is not None]
        lons = [(v, i, t) for v, i, t in vals("gps_lon_raw") if v is not None]
        if len(set(str(x[0]) for x in lats)) > 1:
            conflicts.append({"field": "gps_lat_raw",
                               "values": [{"value": v, "record_idx": i, "tier": t}
                                          for v, i, t in lats],
                               "note": "conflict"})
        payload["gps_lat_raw"] = lats[0][0] if lats else None
        if len(set(str(x[0]) for x in lons)) > 1:
            conflicts.append({"field": "gps_lon_raw",
                               "values": [{"value": v, "record_idx": i, "tier": t}
                                          for v, i, t in lons],
                               "note": "conflict"})
        payload["gps_lon_raw"] = lons[0][0] if lons else None

    # ── Parent fields (parent_resolution strategy) ──
    parent_raw = {
        "parent_site_id_raw": _union("parent_site_id_raw",
                                     [(r.get("parent_site_id_raw"), i, r.get("discovery_tier", 99))
                                      for r, i in cluster_records]),
        "parent_trail_id_raw": _union("parent_trail_id_raw",
                                      [(r.get("parent_trail_id_raw"), i, r.get("discovery_tier", 99))
                                       for r, i in cluster_records]),
        "identity_notes_raw": "\n---\n".join(
            [r.get("identity_notes_raw", "") or ""
             for r, _ in cluster_records if r.get("identity_notes_raw")]
        ) or None,
    }

    # ── Metadata block ──
    baseline_ids = [r.get("baseline_id") for r, _ in cluster_records if r.get("baseline_id")]
    discovery_tiers = sorted(set(r.get("discovery_tier") for r, _ in cluster_records
                                  if r.get("discovery_tier")))

    metadata_block = {
        "seeded_from_baseline": any(r.get("seeded_from_baseline") for r, _ in cluster_records),
        "baseline_ids": baseline_ids,
        "discovery_tiers": discovery_tiers,
        "source_record_indices": sorted(cluster),
        "conflict_count": len(conflicts),
        "conflicts": conflicts if conflicts else [],
        "gis_verify_county": any(
            "GIS_VERIFY_COUNTY" in (r.get("identity_notes_raw") or "")
            for r, _ in cluster_records
        ),
    }

    return {
        "entity_type": et,
        "source_records": sorted(cluster),
        "identity_block": {
            "name_raw": name_raw,
            "counties_raw": counties_raw,
            "urls_raw": urls_raw,
            "location_raw": location_raw,
        },
        "organizational_block": {
            "ownership_raw": ownership_raw,
            "governance_raw": governance_raw,
            "partner_agencies_raw": partner_agencies_raw,
            "coordination_raw": coordination_raw,
        },
        "parent_block": parent_raw,
        "metadata_block": metadata_block,
        "payload": payload,
        "resolution_provenance": {
            "merge_cluster_size": len(cluster),
            "merge_threshold_used": MERGE_THRESHOLD[et],
            "review_threshold_used": REVIEW_THRESHOLD[et],
            "cross_tier_trail": False,
        }
    }


def phase4_singleton(record: dict, idx: int) -> dict:
    """Wrap a singleton record as a Resolved Entity."""
    et = record["entity_type"]
    payload = {}

    if et == "Site":
        for field in ["description_raw", "features_raw", "acres_raw",
                      "category_raw", "status_raw", "gps_lat_raw", "gps_lon_raw"]:
            payload[field] = record.get(field)

    if et in ("Trail", "Trail Segment"):
        for field in ["trail_use_type_raw", "trail_surface_type_raw",
                      "trail_origin_type_raw", "surface_type_raw", "segment_type_raw",
                      "difficulty_raw", "accessibility_raw",
                      "total_length_miles_raw", "segment_length_miles_raw"]:
            payload[field] = record.get(field)

    if et == "Access Point":
        for field in ["gps_lat_raw", "gps_lon_raw", "access_point_type_raw",
                      "description_raw", "features_raw"]:
            payload[field] = record.get(field)

    return {
        "entity_type": et,
        "source_records": [idx],
        "identity_block": {
            "name_raw": record.get("name_raw"),
            "counties_raw": record.get("counties_raw") or [],
            "urls_raw": record.get("urls_raw") or [],
            "location_raw": record.get("location_raw"),
        },
        "organizational_block": {
            "ownership_raw": record.get("ownership_raw"),
            "governance_raw": record.get("governance_raw"),
            "partner_agencies_raw": record.get("partner_agencies_raw") or [],
            "coordination_raw": record.get("coordination_raw") or [],
        },
        "parent_block": {
            "parent_site_id_raw": record.get("parent_site_id_raw") or [],
            "parent_trail_id_raw": record.get("parent_trail_id_raw") or [],
            "identity_notes_raw": record.get("identity_notes_raw"),
        },
        "metadata_block": {
            "seeded_from_baseline": record.get("seeded_from_baseline", False),
            "baseline_ids": [record["baseline_id"]] if record.get("baseline_id") else [],
            "discovery_tiers": [record.get("discovery_tier")],
            "source_record_indices": [idx],
            "conflict_count": 0,
            "conflicts": [],
            "gis_verify_county": "GIS_VERIFY_COUNTY" in (record.get("identity_notes_raw") or ""),
        },
        "payload": payload,
        "resolution_provenance": {
            "merge_cluster_size": 1,
            "merge_threshold_used": MERGE_THRESHOLD[et],
            "review_threshold_used": REVIEW_THRESHOLD[et],
            "cross_tier_trail": False,
        }
    }


# ──────────────────────────────────────────────────────────────────────────────
# PHASE 5 — PARENT RESOLUTION AND ID ASSIGNMENT
# ──────────────────────────────────────────────────────────────────────────────

# Entity type → short code for ID
ET_CODE = {
    "Site": "S",
    "Trail": "T",
    "Trail Segment": "TS",
    "Trail Network": "TN",
    "Site Network": "SN",
    "Access Point": "AP",
}


def assign_resolved_ids(entities: list) -> list:
    """Assign stable resolved_entity_id to each entity, sorted by type then name."""
    counters = defaultdict(int)
    for ent in entities:
        et = ent["entity_type"]
        code = ET_CODE.get(et, "X")
        counters[code] += 1
        ent["resolved_entity_id"] = f"{PREFIX}_{code}_{counters[code]:03d}"
    return entities


def phase5_parent_resolution(entities: list, records: list) -> list:
    """
    Resolve parent names to resolved_entity_ids.
    Uses identity notes to extract parent names, then fuzzy-matches against
    resolved entity names.
    """
    # Build lookup: normalized name → resolved_entity_id (for Sites and Trails)
    name_to_eid = {}
    for ent in entities:
        name = ent["identity_block"].get("name_raw") or ""
        if name:
            name_to_eid[name.strip().lower()] = ent["resolved_entity_id"]

    def fuzzy_lookup(target_name: str, et_filter: str = None) -> str:
        """Find best matching resolved entity ID for a parent name."""
        if not target_name:
            return None
        target_norm = target_name.strip().lower()
        best_score = 0
        best_eid = None
        for name, eid in name_to_eid.items():
            # Filter by entity type if specified
            if et_filter:
                ent = next((e for e in entities if e["resolved_entity_id"] == eid), None)
                if ent and ent["entity_type"] != et_filter:
                    continue
            score = fuzzy_name_score(target_norm, name)
            if score > best_score:
                best_score = score
                best_eid = eid
        if best_score >= 0.6:  # minimum confidence for parent resolution
            return best_eid
        return None

    # Build list of known trail names for AP name-based parent extraction
    trail_names = [
        e["identity_block"]["name_raw"] for e in entities
        if e["entity_type"] == "Trail" and e["identity_block"].get("name_raw")
    ]

    for ent in entities:
        et = ent["entity_type"]
        notes = ent["parent_block"].get("identity_notes_raw") or ""
        ap_name = ent["identity_block"].get("name_raw") or ""
        seg_name = ap_name  # same field for Trail Segments
        parent_ids_resolved = {}
        parent_conflicts = []

        if et == "Access Point":
            # Try notes-based extraction first
            parent_name = _extract_ap_parent_from_notes(notes)
            # Fallback: extract from AP name (e.g. "Wabash Cannonball Trail ... Trailhead")
            if not parent_name:
                parent_name = _extract_ap_parent_from_name(ap_name, trail_names)
            if parent_name:
                # Try Trail first (most APs on linear trails), then Site
                for etype in ["Trail", "Trail Segment", "Site"]:
                    eid = fuzzy_lookup(parent_name, etype)
                    if eid:
                        parent_ids_resolved["parent_entity_id"] = eid
                        parent_ids_resolved["parent_entity_type"] = etype
                        break
                if "parent_entity_id" not in parent_ids_resolved:
                    parent_conflicts.append({
                        "note": f"Could not resolve parent '{parent_name}' to any entity"
                    })

        elif et == "Trail Segment":
            # Try multiple extraction strategies:
            # 1. Explicit "Parent: X" or "Parent trail: X" in notes
            parent_name = _extract_parent_trail_from_notes(notes)
            if not parent_name:
                parent_name = _extract_ap_parent_from_notes(notes)
            # 2. Em-dash convention in segment name: "Leg Name — Parent Trail"
            if not parent_name:
                parent_name = _extract_parent_from_segment_name(seg_name)
            if parent_name:
                # Strip any trailing qualifier text like " (Henry County section ~6 miles)"
                parent_name = re.sub(r"\s*/.*$", "", parent_name).strip()
                eid = fuzzy_lookup(parent_name, "Trail")
                if eid:
                    parent_ids_resolved["parent_trail_id"] = eid
                else:
                    parent_conflicts.append({
                        "note": f"Could not resolve parent trail '{parent_name}' to any Trail entity"
                    })

        elif et == "Trail":
            # Check if identity notes mention a parent site (for MJTSP internal trails)
            m = re.search(r"[Pp]arent site:\s+([^\.\n;(]+)", notes)
            if m:
                parent_site_name = m.group(1).strip()
                # Remove qualifying text after " (this run" etc.
                parent_site_name = re.sub(r"\s*\(.*$", "", parent_site_name).strip()
                eid = fuzzy_lookup(parent_site_name, "Site")
                if eid:
                    parent_ids_resolved["parent_site_id"] = eid

        ent["parent_block"]["resolved_parent_ids"] = parent_ids_resolved
        if parent_conflicts:
            ent["parent_block"]["parent_resolution_conflicts"] = parent_conflicts

    return entities


# ──────────────────────────────────────────────────────────────────────────────
# MAIN PIPELINE
# ──────────────────────────────────────────────────────────────────────────────

def run_resolution():
    print("=" * 70)
    print("HENRY COUNTY, OH — STAGE 1 RESOLUTION ENGINE v5.5")
    print(f"Run ID: {RUN_ID}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    # Load raw records
    data = yaml.safe_load(INPUT_PATH.read_text())
    records = data["records"]
    print(f"\nLoaded {len(records)} raw records from {INPUT_PATH.name}")

    # ── PHASE 1 ──────────────────────────────────────────────────────────────
    print("\n── PHASE 1: GROUPING ──")
    groups = phase1_grouping(records)
    print(f"Groups formed: {len(groups)}")
    for gk, idxs in sorted(groups.items()):
        print(f"  {gk[0]:14s} | {gk[1]:25s} | {len(idxs)} records")

    # ── PHASE 2 ──────────────────────────────────────────────────────────────
    print("\n── PHASE 2: IDENTITY MATCHING ──")
    matrices = phase2_identity_matching(records, groups)
    total_pairs = sum(len(m) for m in matrices.values())
    scored_pairs = sum(1 for m in matrices.values()
                        for s in m.values() if s is not None)
    anchor_failures = total_pairs - scored_pairs
    print(f"Total pairs evaluated: {total_pairs}")
    print(f"Anchor passes (scored): {scored_pairs}")
    print(f"Anchor failures: {anchor_failures}")

    # Print scored pairs above 0
    print("\nScored pairs (score > 0):")
    for gk, matrix in matrices.items():
        for (i, j), score in matrix.items():
            if score is not None and score > 0:
                print(f"  [{i+1:02d}] {records[i].get('name_raw','')[:35]:<35s} vs "
                      f"[{j+1:02d}] {records[j].get('name_raw','')[:35]:<35s} "
                      f"→ {score:.1f}")

    # ── PHASE 3 ──────────────────────────────────────────────────────────────
    print("\n── PHASE 3: MERGE DECISIONS ──")
    merge_clusters, review_sets, singletons = phase3_merge_decisions(
        records, groups, matrices)
    print(f"Merge clusters: {len(merge_clusters)}")
    print(f"Review sets: {len(review_sets)}")
    print(f"Singletons: {len(singletons)}")
    for rs in review_sets:
        print(f"  REVIEW: {rs['record_names']} | score={rs['similarity_score']}")

    # ── PHASE 4 ──────────────────────────────────────────────────────────────
    print("\n── PHASE 4: FIELD-LEVEL MERGING ──")
    entities = []

    # Process merge clusters first
    for cluster in merge_clusters:
        ent = phase4_merge_fields(records, cluster)
        entities.append(ent)
        print(f"  MERGED cluster: {[records[i].get('name_raw','?') for i in sorted(cluster)]}")

    # Process singletons
    for idx in singletons:
        ent = phase4_singleton(records[idx], idx)
        entities.append(ent)

    print(f"\nResolved entities: {len(entities)}")

    # ── PHASE 4.5: Cross-Tier Trail Detection (§11.8) ──────────────────────
    print("\n── PHASE 4.5: CROSS-TIER TRAIL CHECK (§11.8) ──")
    cross_tier_found = False
    for ent in entities:
        if ent["entity_type"] == "Trail":
            tiers = ent["metadata_block"]["discovery_tiers"]
            notes = ent["parent_block"].get("identity_notes_raw") or ""
            if len(tiers) > 1 and "Cross-tier trail" in notes:
                ent["resolution_provenance"]["cross_tier_trail"] = True
                cross_tier_found = True
                print(f"  CROSS-TIER TRAIL: {ent['identity_block']['name_raw']} — tiers {tiers}")
    if not cross_tier_found:
        print("  No cross-tier Trail clusters found (§11.8 criteria not met)")

    # ── PHASE 5 ──────────────────────────────────────────────────────────────
    print("\n── PHASE 5: PARENT RESOLUTION & ID ASSIGNMENT ──")

    # Sort entities by type then name for stable ID assignment
    type_order = ["Site", "Trail", "Trail Segment", "Trail Network",
                  "Site Network", "Access Point"]
    entities.sort(key=lambda e: (
        type_order.index(e["entity_type"]) if e["entity_type"] in type_order else 99,
        e["identity_block"].get("name_raw") or ""
    ))

    # Assign IDs
    entities = assign_resolved_ids(entities)
    entities = phase5_parent_resolution(entities, records)

    print("\nID assignments:")
    for ent in entities:
        pid = ent["parent_block"].get("resolved_parent_ids", {})
        print(f"  {ent['resolved_entity_id']:12s} | {ent['entity_type']:14s} | "
              f"{ent['identity_block']['name_raw'][:45]:<45s} | parent={pid}")

    # ── OUTPUT ───────────────────────────────────────────────────────────────

    # Build final output structure
    output = {
        "run_id": RUN_ID,
        "county": "Henry County",
        "state": "Ohio",
        "resolution_date": datetime.now().strftime("%Y-%m-%d"),
        "records_input": len(records),
        "entities_resolved": len(entities),
        "merge_clusters_formed": len(merge_clusters),
        "singletons": len(singletons),
        "review_sets": review_sets,
        "resolved_entities": entities,
    }

    OUTPUT_PATH.write_text(
        yaml.dump(output, allow_unicode=True, sort_keys=False, default_flow_style=False)
    )
    print(f"\nWrote resolved entities to: {OUTPUT_PATH.name}")

    # ── SUMMARY TABLE ────────────────────────────────────────────────────────
    from collections import Counter
    et_counts = Counter(e["entity_type"] for e in entities)
    print("\n── RESOLUTION SUMMARY ──")
    print(f"{'Entity Type':<18} {'Count':>5}")
    print("-" * 25)
    for et in type_order:
        if et_counts[et]:
            print(f"{et:<18} {et_counts[et]:>5}")
    print(f"{'TOTAL':<18} {len(entities):>5}")
    print(f"\nReview sets requiring attention: {len(review_sets)}")

    # Build report
    report_lines = [
        f"# Henry County, OH — Stage 1 Resolution Report",
        f"**Run ID:** `{RUN_ID}`",
        f"**Resolution Date:** {datetime.now().strftime('%Y-%m-%d')}",
        f"**Records Input:** {len(records)}",
        f"**Entities Resolved:** {len(entities)}",
        f"**Merge Clusters Formed:** {len(merge_clusters)}",
        f"**Singletons:** {len(singletons)}",
        f"**Review Sets:** {len(review_sets)}",
        "",
        "## Entity Counts",
        "",
        "| Entity Type | Count |",
        "|-------------|-------|",
    ]
    for et in type_order:
        if et_counts[et]:
            report_lines.append(f"| {et} | {et_counts[et]} |")
    report_lines.append(f"| **TOTAL** | **{len(entities)}** |")
    report_lines.extend(["", "## ID Assignments", ""])
    for ent in entities:
        pid = ent["parent_block"].get("resolved_parent_ids", {})
        pid_str = str(pid) if pid else "—"
        report_lines.append(
            f"- `{ent['resolved_entity_id']}` — {ent['entity_type']} — "
            f"**{ent['identity_block']['name_raw']}** — parent: {pid_str}"
        )
    if review_sets:
        report_lines.extend(["", "## Review Sets", ""])
        for rs in review_sets:
            report_lines.append(
                f"- **{rs['entity_type']}** score={rs['similarity_score']}: "
                f"{rs['record_names']} — {rs['note']}"
            )
    if merge_clusters:
        report_lines.extend(["", "## Merge Clusters", ""])
        for cluster in merge_clusters:
            names = [records[i].get("name_raw", "?") for i in sorted(cluster)]
            report_lines.append(f"- Merged: {names}")

    REPORT_PATH.write_text("\n".join(report_lines))
    print(f"Wrote resolution report to: {REPORT_PATH.name}")

    return len(entities), len(review_sets), len(merge_clusters)


if __name__ == "__main__":
    run_resolution()
