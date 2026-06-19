#!/usr/bin/env python3
"""
Natural Areas Project — Wayne County, Ohio
Self-Contained Upsert Script
Generated: 2026-03-08 | Schema: v5.2 (Sites) / v5.1 (all others)

USAGE:
    python wayne_oh_upsert.py [--db PATH] [--dry-run] [--reset-county]

OPTIONS:
    --db PATH         Path to the SQLite database file
                      Default: ./natural_areas.db
    --dry-run         Print all SQL without executing
    --reset-county    DELETE all existing Wayne County records before upserting
                      (use when re-running to replace a prior Wayne County run)

WHAT THIS SCRIPT DOES:
    1. Creates schema (all 6 entity tables + relationship + provenance tables)
       if they don't already exist — safe to run against an existing database.
    2. Upserts 73 normalized Wayne County records across:
         Sites (44), Access Points (17), Trails (11), Trail Networks (1)
         Trail Segments (0), Site Networks (0)
    3. Writes 6 held records to the held_entities table.
    4. Appends a run metadata record.

HELD (NOT UPSERTED TO MAIN TABLES):
    T2-004  Killbuck Marsh WA         multi_county (Holmes not yet processed)
    T2-007  Killbuck Marsh Obs. Trail identity_uncertain
    T2-012  Funk Bottoms WA           multi_county (Ashland not yet processed)
    T5-002  Chippewa Twp trails       identity_uncertain
    T7-002  Sippo Valley Trail        multi_county (Stark not yet processed)
    T7-004  Holmes County Trail       multi_county (Holmes not yet processed)
"""

import sqlite3
import sys
import argparse
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

DEFAULT_DB = "./natural_areas.db"
COUNTY = "Wayne"
STATE = "Ohio"
RUN_ID = "wayne_oh_2026_03_08"
RUN_DATE = "2026-03-08"

# ---------------------------------------------------------------------------
# SCHEMA CREATION
# ---------------------------------------------------------------------------

SCHEMA_SQL = """

-- ============================================================
-- CORE ENTITY TABLES
-- ============================================================

CREATE TABLE IF NOT EXISTS sites (
    site_id         TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    category        TEXT,
    subtype         TEXT,
    designation     TEXT,
    status          TEXT,
    ownership       TEXT,
    governance      TEXT,
    partner_agencies TEXT,
    coordination    TEXT,
    description     TEXT,
    location        TEXT,
    acres           REAL,
    counties        TEXT,
    municipality    TEXT,
    township        TEXT,
    gps_lat         REAL,
    gps_lon         REAL,
    plus_code       TEXT,
    features        TEXT,
    notes           TEXT,
    url_primary     TEXT,
    urls            TEXT,
    parent_site_id  TEXT,
    created_at      TEXT,
    updated_at      TEXT
);

CREATE TABLE IF NOT EXISTS trails (
    trail_id            TEXT PRIMARY KEY,
    name                TEXT NOT NULL,
    alternate_names     TEXT,
    use_type            TEXT,
    surface_type        TEXT,
    origin_type         TEXT,
    length_mi           REAL,
    counties            TEXT,
    governance          TEXT,
    partner_agencies    TEXT,
    status              TEXT,
    difficulty          TEXT,
    accessibility       TEXT,
    description         TEXT,
    trail_history       TEXT,
    identity_notes      TEXT,
    notes               TEXT,
    url_primary         TEXT,
    maps                TEXT,
    created_at          TEXT,
    updated_at          TEXT
);

CREATE TABLE IF NOT EXISTS trail_segments (
    segment_id      TEXT PRIMARY KEY,
    parent_trail_id TEXT,
    name            TEXT,
    counties        TEXT,
    governance      TEXT,
    length_mi       REAL,
    surface_type    TEXT,
    segment_type    TEXT,
    status          TEXT,
    difficulty      TEXT,
    accessibility   TEXT,
    description     TEXT,
    identity_notes  TEXT,
    notes           TEXT,
    url_primary     TEXT,
    maps            TEXT,
    geometry        TEXT,
    created_at      TEXT,
    updated_at      TEXT
);

CREATE TABLE IF NOT EXISTS trail_networks (
    network_id          TEXT PRIMARY KEY,
    name                TEXT NOT NULL,
    network_type        TEXT,
    status              TEXT,
    ownership           TEXT,
    governance          TEXT,
    partner_agencies    TEXT,
    counties            TEXT,
    states_included     TEXT,
    length_mi           REAL,
    member_trail_count  INTEGER,
    member_trail_ids    TEXT,
    description         TEXT,
    identity_notes      TEXT,
    notes               TEXT,
    url_primary         TEXT,
    maps                TEXT,
    created_at          TEXT,
    updated_at          TEXT
);

CREATE TABLE IF NOT EXISTS site_networks (
    network_id      TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    network_type    TEXT,
    status          TEXT,
    ownership       TEXT,
    governance      TEXT,
    partner_agencies TEXT,
    counties        TEXT,
    states_included TEXT,
    member_count    INTEGER,
    member_site_ids TEXT,
    description     TEXT,
    identity_notes  TEXT,
    notes           TEXT,
    url_primary     TEXT,
    created_at      TEXT,
    updated_at      TEXT
);

CREATE TABLE IF NOT EXISTS access_points (
    access_point_id     TEXT PRIMARY KEY,
    name                TEXT NOT NULL,
    ap_type             TEXT,
    status              TEXT,
    parent_entity_type  TEXT,
    parent_entity_id    TEXT,
    county              TEXT,
    township            TEXT,
    municipality        TEXT,
    address             TEXT,
    gps_lat             REAL,
    gps_lon             REAL,
    plus_code           TEXT,
    features            TEXT,
    identity_notes      TEXT,
    notes               TEXT,
    url_primary         TEXT,
    created_at          TEXT,
    updated_at          TEXT
);

-- ============================================================
-- RELATIONSHIP TABLES
-- ============================================================

CREATE TABLE IF NOT EXISTS site_parent (
    site_id         TEXT NOT NULL,
    parent_site_id  TEXT NOT NULL,
    PRIMARY KEY (site_id, parent_site_id)
);

CREATE TABLE IF NOT EXISTS trail_to_segment (
    trail_id        TEXT NOT NULL,
    segment_id      TEXT NOT NULL,
    PRIMARY KEY (trail_id, segment_id)
);

CREATE TABLE IF NOT EXISTS trail_network_members (
    network_id      TEXT NOT NULL,
    trail_id        TEXT NOT NULL,
    PRIMARY KEY (network_id, trail_id)
);

CREATE TABLE IF NOT EXISTS site_network_members (
    network_id      TEXT NOT NULL,
    site_id         TEXT NOT NULL,
    PRIMARY KEY (network_id, site_id)
);

CREATE TABLE IF NOT EXISTS access_point_parents (
    access_point_id     TEXT NOT NULL,
    parent_entity_type  TEXT NOT NULL,
    parent_entity_id    TEXT NOT NULL,
    PRIMARY KEY (access_point_id, parent_entity_type, parent_entity_id)
);

-- ============================================================
-- OPERATIONAL TABLES
-- ============================================================

CREATE TABLE IF NOT EXISTS entity_conflicts (
    conflict_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    field           TEXT NOT NULL,
    value_a         TEXT,
    value_b         TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS entity_uncertainty (
    uncertainty_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    field           TEXT,
    uncertainty_note TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS entity_geometry (
    geometry_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    geometry_type   TEXT,
    geometry_wkt    TEXT,
    source          TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS held_entities (
    held_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    record_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    name            TEXT NOT NULL,
    county          TEXT,
    hold_reason     TEXT,
    hold_detail     TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS manual_review_queue (
    review_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    record_id       TEXT,
    entity_type     TEXT,
    name            TEXT,
    issue           TEXT,
    run_id          TEXT,
    created_at      TEXT
);

-- ============================================================
-- PROVENANCE TABLES
-- ============================================================

CREATE TABLE IF NOT EXISTS run_metadata (
    run_id          TEXT PRIMARY KEY,
    county          TEXT,
    state           TEXT,
    run_date        TEXT,
    records_input   INTEGER,
    normalized      INTEGER,
    held            INTEGER,
    rejected        INTEGER,
    notes           TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS discovery_provenance (
    prov_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT,
    entity_type     TEXT,
    county          TEXT,
    discovery_tier  INTEGER,
    source_notes    TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS resolution_provenance (
    prov_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT,
    entity_type     TEXT,
    county          TEXT,
    resolution_run  TEXT,
    notes           TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS normalization_provenance (
    prov_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT,
    entity_type     TEXT,
    county          TEXT,
    outcome         TEXT,
    hold_reason     TEXT,
    notes           TEXT,
    run_id          TEXT,
    created_at      TEXT
);

"""

# ---------------------------------------------------------------------------
# NORMALIZED DATA — SITES (44 records)
# ---------------------------------------------------------------------------

# Format: (site_id, name, category, subtype, designation, status, ownership,
#          governance, partner_agencies, coordination, description, location,
#          acres, counties, municipality, township, gps_lat, gps_lon,
#          plus_code, features, notes, url_primary, urls, parent_site_id)

SITES = [
    # --- TIER 2: STATE ---
    ("T2-001", "Brown's Lake Bog State Nature Preserve",
     "Nature Preserve", "Bog", "State Nature Preserve", "Open",
     "Ohio Department of Natural Resources (ODNR) — Division of Natural Areas and Preserves",
     "Ohio DNAP", "", "",
     "Designated State Nature Preserve protecting a glacial bog ecosystem with rare sphagnum moss, pitcher plants, sundews, and bog rosemary surrounding Brown's Lake.",
     "Brown Rd, approximately 2 miles west of Shreve, Wayne County, Ohio",
     None, "Wayne", "", "",
     40.682973, -82.067569, "8MGV54GH+JJ",
     "Glacial bog; sphagnum moss; pitcher plants (Sarracenia purpurea); sundews; bog rosemary; rare orchids; Brown's Lake; viewing platform; permit required for access",
     "Access by permit only — contact Ohio DNAP. Wayne County portion only.",
     "https://ohiodnap.gov/site/browns-lake-bog", "", None),

    ("T2-002", "Johnson Woods State Nature Preserve",
     "Nature Preserve", "Old-Growth Forest", "State Nature Preserve", "Open",
     "Ohio Department of Natural Resources (ODNR) — Division of Natural Areas and Preserves",
     "Ohio DNAP", "", "",
     "One of the largest remaining old-growth forests in Ohio, featuring ancient white and red oaks up to 500 years old in a glacially flattened landscape.",
     "13240 Fox Lake Rd, Marshallville, Wayne County, Ohio 44644",
     None, "Wayne", "Marshallville", "",
     40.888626, -81.744192, "8MGWX5M4+GG",
     "Old-growth forest; white oak; red oak; trees 300-500 years old; 1-mile boardwalk trail; interpretive signage; no pets; no bikes; dawn to dusk",
     "One of the finest old-growth forest remnants in the Midwest.",
     "https://ohiodnap.gov/site/johnson-woods", "", None),

    ("T2-003", "Shreve Lake Wildlife Area",
     "Wildlife Area", "Lake/Wetland", None, "Open",
     "Ohio Department of Natural Resources (ODNR) — Division of Wildlife",
     "Ohio Division of Wildlife", "", "",
     "State wildlife area centered on Shreve Lake, managed primarily for waterfowl hunting and fishing, with boat launch and fishing pier access.",
     "Critchfield Rd and Brown Rd, near Shreve, Wayne County, Ohio",
     None, "Wayne", "Shreve", "",
     40.682994, -82.044038, "8MGV55J4+MX",
     "Shreve Lake; waterfowl hunting; fishing; boat launch; fishing pier; open to public hunting and fishing per ODNR regulations",
     "Hunting seasons apply. Check ODNR for current regulations.",
     "https://ohiodnr.gov/go-and-do/hunt-fish/wildlife-areas/shreve-lake-wildlife-area", "", None),

    # --- TIER 3: DISTRICT ---
    ("T3-001", "Barnes Preserve",
     "Nature Preserve", "Woodland/Wetland", None, "Open",
     "Wayne County Park District",
     "Wayne County Park District", "", "Wayne County Park District, 3376 Shreve Rd (Sylvan Rd), Wooster",
     "76-acre preserve featuring mixed woodland and wetland habitats along Killbuck Creek, with two named trail loops and Koehler's Pond.",
     "3396 Sylvan Rd, Wooster, Wayne County, Ohio",
     76.0, "Wayne", "Wooster", "",
     40.781233, -81.896940, "8MGWQ4J3+F6",
     "76 acres; mixed woodland; wetland; Killbuck Creek; Koehler's Pond; two trail loops; interpretive signage; parking; open dawn to dusk",
     "",
     "https://www.waynecountyparkdistrict.org/barnes-preserve",
     "", None),

    ("T3-002", "Koehler's Pond",
     "Natural Feature", "Pond/Wetland", None, "Open",
     "Wayne County Park District",
     "Wayne County Park District (child site within Barnes Preserve)", "", "",
     "Named wetland pond within Barnes Preserve, accessible via Casey's Trails, with an accessible observation deck overlooking the pond and its wildlife.",
     "Within Barnes Preserve, 3396 Sylvan Rd, Wooster, Ohio",
     None, "Wayne", "Wooster", "",
     40.781233, -81.896940, "8MGWQ4J3+F6",
     "Wetland pond; accessible observation deck; turtles; frogs; aquatic life; wildlife hydration source",
     "Flag N-001: routed as Site (named natural feature destination, not access point).",
     "https://www.waynecountyparkdistrict.org/barnes-preserve",
     "", "T3-001"),

    # --- TIER 5: TOWNSHIP ---
    ("T5-001", "Chippewa Township Nature Preserve",
     "Nature Preserve", "Woodland/Riparian", None, "Open",
     "Chippewa Township",
     "Chippewa Township", "Chippewa-Rogues Hollow Historical Society", "Darlene Smith, Chippewa Township office, 330-658-2112",
     "24-25 acre township-owned nature preserve in the Rogues Hollow area, featuring Silver Creek riparian corridor, woodland trails, pavilion, and the Chidester Mill historical museum.",
     "17500 Galehouse Road, Doylestown, Wayne County, Ohio 44230",
     24.5, "Wayne", "Doylestown", "Chippewa Township",
     40.662400, -81.702500, "8MGVXR8H+22",
     "24-25 acres; Silver Creek; riparian corridor; woodland trails; pavilion; picnic area; Chidester Mill replica museum; ~200-year-old sycamore; pond/mill race site; dawn to dusk",
     "Also referenced as 'Chippewa Rogues Hollow Nature Preserve and Historical Park'. GPS approximate — address geocode, no Maps pin.",
     "http://www.chippewatwp.com",
     "", None),

    # --- TIER 6: MUNICIPAL — WOOSTER ---
    ("T6-001", "Wooster Memorial Park",
     "Park", "Natural/Woodland Park", None, "Open",
     "City of Wooster",
     "City of Wooster (Public Properties Maintenance Division)",
     "Friends of Wooster Memorial Park", "City of Wooster Parks Dept, 1151 Mechanicsburg Rd, 330-263-5275",
     "422-acre city natural area featuring primitive woodland, steep ravines, and 11.6 miles of named foot trails. City-designated permanent natural area. Also known as Spangler Park.",
     "5197 Silver Road, Wooster, Ohio; intersection of Silver Road and North Jefferson Road",
     422.0, "Wayne", "Wooster", "",
     40.811007, -82.023044, "8MGVRX8G+CF",
     "422 acres; primitive woodland; steep ravines; Rathburn Run; 11.6 miles foot trails; Spangler Trail 1.5mi; Outer Trail; Old Field Trail 0.5mi; Education Trail 0.9mi; Trillium Trail; Strock Trail 0.4mi; Kenwood Trail 0.8mi; Hartman Trail 0.2mi; Sassafras Trail 0.6mi; ADA-accessible Kenwood Acres section (1 mile); vault toilet; pavilions; spring wildflowers; foot traffic only",
     "Foot traffic only — no bikes, horses, motorized vehicles.",
     "https://www.woosteroh.com/parks/wooster-memorial-park",
     "https://www.friendsofwmp.com/;https://www.woosteroh.com/sites/default/files/WMP-Trail-Map-2-22-2016.pdf",
     None),

    ("T6-005", "Oak Hill Park",
     "Park", "Natural/Woodland Park", None, "Open",
     "City of Wooster", "City of Wooster", "", "",
     "100-acre park with paved accessible trail, prairie restoration area, and woodland habitat.",
     "Wooster, Ohio",
     100.0, "Wayne", "Wooster", "",
     40.836059, -81.955606, "8MGWQ8CF+JP",
     "100 acres; paved trail 1.7mi; prairie restoration; woodland; 2 van-accessible parking spaces; ADA accessible",
     "", "https://www.woosteroh.com/parks", "", None),

    ("T6-007", "Freedlander Park",
     "Park", "Community Park", None, "Open",
     "City of Wooster", "City of Wooster", "", "",
     "Large multi-use park with disc golf, swimming pool, the historic Chalet, and recreation facilities.",
     "Wooster, Ohio",
     None, "Wayne", "Wooster", "",
     40.838412, -81.935627, "8MGWQ9G4+VQ",
     "Disc golf; swimming pool; Chalet; multi-use recreation",
     "", "https://www.woosteroh.com/parks", "", None),

    ("T6-008", "Christmas Run Park",
     "Park", "Community Park", None, "Open",
     "City of Wooster", "City of Wooster", "", "",
     "Wooster park with swimming pool, playground, 7 pavilions, and hiking trails.",
     "Wooster, Ohio",
     None, "Wayne", "Wooster", "",
     40.806486, -81.946700, "8MGWP8HH+VF",
     "Pool; playground; 7 pavilions (reservable); hiking trails",
     "", "https://www.woosteroh.com/parks", "", None),

    ("T6-009", "Grosjean Park",
     "Park", "Natural/Riparian Park", None, "Open",
     "City of Wooster", "City of Wooster", "", "",
     "Rustic park along Apple Creek with trout stocking, accessible education trail, and riparian habitat.",
     "Wooster, Ohio",
     None, "Wayne", "Wooster", "",
     40.792605, -81.928697, "8MGWP6QH+MV",
     "Rustic; Apple Creek; trout-stocked; accessible education trail; riparian habitat",
     "", "https://www.woosteroh.com/parks", "", None),

    ("T6-010", "Walton Woods Park",
     "Park", "Natural/Woodland Park", None, "Open",
     "City of Wooster", "City of Wooster", "", "",
     "Rustic woodland park. Potential wildflower sanctuary — needs field verification.",
     "Wooster, Ohio",
     None, "Wayne", "Wooster", "",
     40.810102, -81.962528, "8MGWP8HG+44",
     "Rustic woodland; potential wildflower sanctuary",
     "", "https://www.woosteroh.com/parks", "", None),

    ("T6-011", "Diller Park",
     "Park", "Natural/Woodland Park", None, "Open",
     "City of Wooster", "City of Wooster", "", "",
     "Rustic Wooster park.",
     "Wooster, Ohio",
     None, "Wayne", "Wooster", "",
     40.814196, -81.938734, "8MGWQ84H+M2",
     "Rustic", "", "https://www.woosteroh.com/parks", "", None),

    ("T6-012", "Gerstenslager Park",
     "Park", "Natural/Woodland Park", None, "Open",
     "City of Wooster", "City of Wooster", "", "",
     "Rustic Wooster park.",
     "Wooster, Ohio",
     None, "Wayne", "Wooster", "",
     40.814625, -81.914602, "8MGWQ94F+3Q",
     "Rustic", "", "https://www.woosteroh.com/parks", "", None),

    ("T6-013", "Stan Miller Park",
     "Park", "Community Park", None, "Open",
     "City of Wooster", "City of Wooster", "", "",
     "Wooster community park.",
     "Wooster, Ohio",
     None, "Wayne", "Wooster", "",
     40.826899, -81.923812, "8MGWQ9HG+C4",
     "", "", "https://www.woosteroh.com/parks", "", None),

    # --- TIER 6: MUNICIPAL — ORRVILLE ---
    ("T6-014", "Orr Park",
     "Park", "Community Park", None, "Open",
     "City of Orrville", "City of Orrville", "", "",
     "Primary community park in Orrville.",
     "Orrville, Wayne County, Ohio",
     None, "Wayne", "Orrville", "",
     40.844610, -81.772450, "8MGWX5P4+GG",
     "", "", "", "", None),

    ("T6-015", "Gailey Park",
     "Park", "Community Park", None, "Open",
     "City of Orrville", "City of Orrville", "", "",
     "Orrville community park.",
     "Orrville, Wayne County, Ohio",
     None, "Wayne", "Orrville", "",
     40.835667, -81.755116, "8MGWX3Q4+WF",
     "", "", "", "", None),

    ("T6-015b", "Orrville Dog Park",
     "Park", "Dog Park", None, "Open",
     "City of Orrville", "City of Orrville", "", "",
     "Off-leash dog park in Orrville.",
     "Orrville, Wayne County, Ohio",
     None, "Wayne", "Orrville", "",
     40.845003, -81.768516, "8MGWX5P4+QC",
     "Off-leash dog area; fenced", "", "", "", None),

    # --- TIER 6: MUNICIPAL — RITTMAN ---
    ("T6-016", "Morton Salt Park",
     "Park", "Community Park", None, "Open",
     "City of Rittman", "City of Rittman", "", "",
     "Rittman community park near Morton Salt facility.",
     "N State St area, Rittman, Wayne County, Ohio",
     None, "Wayne", "Rittman", "",
     40.974809, -81.780212, "8MGWX694+62",
     "", "GPS-APPROXIMATE — no Maps listing; address geocode only.", "", "", None),

    ("T6-017", "Vincent & Rose Tricomi Memorial Park",
     "Park", "Community Park", None, "Open",
     "City of Rittman", "City of Rittman", "", "",
     "Memorial park in Rittman with pond and athletic fields.",
     "E Ohio Ave, Rittman, Wayne County, Ohio",
     None, "Wayne", "Rittman", "",
     40.976360, -81.771330, "8MGWX694+X2",
     "Pond; athletic fields; memorial", "", "", "", None),

    ("T6-018", "Rotary Park Tennis Courts",
     "Park", "Recreation Area", None, "Open",
     "City of Rittman", "City of Rittman", "", "",
     "Rittman park featuring tennis courts at the recreation center complex.",
     "Recreation center area, Rittman, Wayne County, Ohio",
     None, "Wayne", "Rittman", "",
     40.974660, -81.799610, "8MGWX684+4J",
     "Tennis courts; recreation center complex", "", "", "", None),

    ("T6-021", "Martin Fritz Memorial Park",
     "Park", "Community Park", None, "Open",
     "City of Rittman", "City of Rittman", "", "",
     "Rittman memorial park.",
     "Rittman, Wayne County, Ohio",
     None, "Wayne", "Rittman", "",
     40.977685, -81.773434, "8MGWX694+W8",
     "", "", "", "", None),

    ("T6-022", "First Street Ashton Hall Park",
     "Park", "Community Park", None, "Open",
     "City of Rittman", "City of Rittman", "", "",
     "Rittman park on First Street.",
     "Rittman, Wayne County, Ohio",
     None, "Wayne", "Rittman", "",
     40.971419, -81.783235, "8MGWX684+5W",
     "", "", "", "", None),

    ("T6-023", "Central Park",
     "Park", "Community Park", None, "Open",
     "City of Rittman", "City of Rittman", "", "",
     "Central park in Rittman.",
     "Rittman, Wayne County, Ohio",
     None, "Wayne", "Rittman", "",
     40.971054, -81.786664, "8MGWX684+3C",
     "", "", "", "", None),

    ("T6-024", "E.J. Young Grand View Park",
     "Park", "Community Park", None, "Open",
     "City of Rittman", "City of Rittman", "", "",
     "Rittman park. No standalone Maps listing.",
     "Rittman, Wayne County, Ohio",
     None, "Wayne", "Rittman", "",
     40.970631, -81.791067, "8MGWX674+X8",
     "", "GPS-APPROXIMATE — intersection geocode only.", "", "", None),

    ("T6-025", "Washington Street Park",
     "Park", "Community Park", None, "Open",
     "City of Rittman", "City of Rittman", "", "",
     "Rittman park on Washington Street. No standalone Maps listing.",
     "Washington St, Rittman, Wayne County, Ohio",
     None, "Wayne", "Rittman", "",
     40.979680, -81.793922, "8MGWX694+62",
     "", "GPS-APPROXIMATE — intersection geocode only.", "", "", None),

    ("T6-026", "William J. Robertson Nature Preserve",
     "Nature Preserve", "Woodland", None, "Open",
     "City of Rittman", "City of Rittman", "", "",
     "City-owned nature preserve in Rittman.",
     "Rittman, Wayne County, Ohio",
     None, "Wayne", "Rittman", "",
     40.977441, -81.764589, "8MGWX6C4+9V",
     "Woodland; city nature preserve", "",
     "", "", None),

    # --- TIER 6: VILLAGES ---
    ("T6-019", "Apple Creek Park",
     "Park", "Community Park", None, "Open",
     "Village of Apple Creek", "Village of Apple Creek", "", "",
     "Community park in Apple Creek.",
     "Apple Creek, Wayne County, Ohio",
     None, "Wayne", "Apple Creek", "",
     40.750882, -81.830626, "8MGWM4QG+66",
     "", "", "", "", None),

    ("T6-Burbank-001", "Burbank Community Park",
     "Park", "Community Park", None, "Open",
     "Village of Burbank", "Village of Burbank", "", "",
     "Community park in Burbank.",
     "Burbank, Wayne County, Ohio",
     None, "Wayne", "Burbank", "",
     40.988786, -81.996069, "8MGWX4H4+FX",
     "", "", "", "", None),

    ("T6-020", "Creston Community Park",
     "Park", "Community Park", None, "Open",
     "Village of Creston", "Village of Creston", "", "",
     "Primary community park in Creston.",
     "Creston, Wayne County, Ohio",
     None, "Wayne", "Creston", "",
     40.989120, -81.892377, "8MGWX8H3+2X",
     "", "", "", "", None),

    ("T6-020b", "Brooklyn Park",
     "Park", "Community Park", None, "Open",
     "Village of Creston", "Village of Creston", "", "",
     "Secondary park in Creston.",
     "Creston, Wayne County, Ohio",
     None, "Wayne", "Creston", "",
     40.988632, -81.890036, "8MGWX8H3+2F",
     "", "", "", "", None),

    ("T6-D-001", "Memorial Park",
     "Park", "Community Park", None, "Open",
     "Village of Doylestown", "Village of Doylestown", "", "",
     "Primary park in Doylestown. Includes Gene Daniel Community Center.",
     "Doylestown, Wayne County, Ohio",
     None, "Wayne", "Doylestown", "",
     40.975713, -81.695668, "8MGWX7C4+5M",
     "Gene Daniel Community Center; Chippewa Local School District track/stadium; pavilion",
     "", "", "", None),

    ("T6-D-002", "Paridon Park",
     "Park", "Community Park", None, "Open",
     "Village of Doylestown", "Village of Doylestown", "", "",
     "Doylestown community park.",
     "Doylestown, Wayne County, Ohio",
     None, "Wayne", "Doylestown", "",
     40.969172, -81.698788, "8MGWX6C4+VP",
     "", "", "", "", None),

    ("T6-D-003", "Gilcrest Park",
     "Park", "Community Park", None, "Open",
     "Village of Doylestown", "Village of Doylestown", "", "",
     "Doylestown community park.",
     "Doylestown, Wayne County, Ohio",
     None, "Wayne", "Doylestown", "",
     40.977440, -81.699010, "8MGWX7C4+9J",
     "Maintained green field", "", "", "", None),

    ("T6-Fred-001", "Fredericksburg Community Park",
     "Park", "Community Park", None, "Open",
     "Village of Fredericksburg", "Village of Fredericksburg", "", "",
     "Community park in Fredericksburg.",
     "Fredericksburg, Wayne County, Ohio",
     None, "Wayne", "Fredericksburg", "",
     40.678705, -81.869520, "8MGVV5J4+HJ",
     "", "", "", "", None),

    ("T6-M-001", "Robert Brooker Nature Preserve",
     "Nature Preserve", "Woodland", None, "Open",
     "Village of Marshallville", "Village of Marshallville", "", "",
     "Nearly 50-acre village-owned nature preserve in Marshallville featuring oak-to-maple transitional forest with three named trails.",
     "Marshallville, Wayne County, Ohio",
     50.0, "Wayne", "Marshallville", "",
     40.901336, -81.727713, "8MGWV5J5+GG",
     "~50 acres; oak-to-maple transitional forest; stream crossings (bridges); solar field; 3 named trails; bike rack; interpretive sign; no facilities except porta-pots; sunrise to sunset; no bikes/horses/fires/hunting",
     "", "", "", None),

    ("T6-029", "Marshallville Community Park",
     "Park", "Community Park", None, "Open",
     "Village of Marshallville", "Village of Marshallville", "", "",
     "Community park in Marshallville.",
     "Marshallville, Wayne County, Ohio",
     None, "Wayne", "Marshallville", "",
     40.900306, -81.737956, "8MGWV5J3+52",
     "", "", "", "", None),

    ("T6-MtEaton-001", "Mt Eaton Community Park",
     "Park", "Community Park", None, "Open",
     "Village of Mt Eaton", "Village of Mt Eaton", "", "",
     "Community park in Mt Eaton.",
     "Mt Eaton, Wayne County, Ohio",
     None, "Wayne", "Mt Eaton", "",
     40.698537, -81.700587, "8MGVV7J4+5J",
     "", "", "", "", None),

    ("T6-Shreve-001", "Shreve Village Park",
     "Park", "Community Park", None, "Open",
     "Village of Shreve", "Village of Shreve", "", "",
     "Primary village park in Shreve.",
     "Shreve, Wayne County, Ohio",
     None, "Wayne", "Shreve", "",
     40.689010, -82.017811, "8MGVV4J5+9F",
     "", "", "", "", None),

    ("T6-Shreve-002", "Harold Miller Park",
     "Park", "Community Park", None, "Open",
     "Village of Shreve", "Village of Shreve", "", "",
     "Secondary park in Shreve.",
     "Shreve, Wayne County, Ohio",
     None, "Wayne", "Shreve", "",
     40.679412, -82.019446, "8MGVV4J4+GH",
     "", "", "", "", None),

    ("T6-030", "Smithville Village Park",
     "Park", "Community Park", None, "Open",
     "Village of Smithville", "Village of Smithville", "", "",
     "Community park in Smithville.",
     "Smithville, Wayne County, Ohio",
     None, "Wayne", "Smithville", "",
     40.863101, -81.857338, "8MGWV6M4+3G",
     "", "", "", "", None),

    ("T6-031", "Drake Park",
     "Park", "Community Park", None, "Open",
     "Village of West Salem", "Village of West Salem", "", "",
     "Community park in West Salem.",
     "West Salem, Wayne County, Ohio",
     None, "Wayne", "West Salem", "",
     40.967464, -82.117952, "8MGWX3G4+GH",
     "", "", "", "", None),

    # --- TIER 8: PRIVATE ---
    ("T8-001", "Secrest Arboretum",
     "Arboretum", "Research Arboretum", None, "Open",
     "Ohio State University / Ohio Agricultural Research and Development Center (OARDC)",
     "OSU OARDC Wooster Campus", "", "OARDC, 1680 Madison Ave, Wooster, OH 44691",
     "110-acre living plant collection and research arboretum on the OSU OARDC campus, featuring extensive woody plant collections open to the public.",
     "OARDC campus, 1680 Madison Ave, Wooster, Wayne County, Ohio",
     110.0, "Wayne", "Wooster", "",
     40.782984, -81.917203, "8MGWQ4JH+5G",
     "110 acres; living plant collection; research arboretum; woody plant collections; public access; no fee",
     "On OSU/OARDC campus. Open year-round.",
     "https://secrestarboretum.osu.edu", "", None),

    ("T8-002", "Vulture's Knob Mountain Bike Park",
     "Recreation Area", "Mountain Bike Park", None, "Open",
     "Friends of Vultures Knob (501(c)(3)); ownership transferred December 31 2025 — new owner undisclosed",
     "Friends of Vultures Knob (501(c)(3))", "", "",
     "125-acre mountain bike trail park near Wooster, operated as a nonprofit trail system. Ownership transferred December 31, 2025; trail remains operating.",
     "Near Wooster, Wayne County, Ohio",
     125.0, "Wayne", "", "",
     40.850970, -81.980600, "8MGWQ6J5+RF",
     "125 acres; mountain bike trails; nonprofit trail system; operating post-ownership transfer",
     "Ownership transferred Dec 31 2025; new owner undisclosed as of 2026-03-08. Trail operating normally.",
     "https://www.vulturesknob.com", "", None),
]

# ---------------------------------------------------------------------------
# NORMALIZED DATA — TRAILS (11 records)
# ---------------------------------------------------------------------------

# Format: (trail_id, name, alternate_names, use_type, surface_type,
#          origin_type, length_mi, counties, governance, partner_agencies,
#          status, difficulty, accessibility, description, trail_history,
#          identity_notes, notes, url_primary, maps)

TRAILS = [
    ("T2-005", "Brown's Lake Bog Trail",
     "", "Foot", "Natural/Primitive", "State-built",
     None, "Wayne", "Ohio DNAP", "", "Open",
     "Easy", "Permit required",
     "Permit-access foot trail to Brown's Lake Bog State Nature Preserve.",
     "", "Trail to preserve; permit required for access.",
     "", "https://ohiodnap.gov/site/browns-lake-bog", ""),

    ("T2-006", "Johnson Woods Boardwalk Trail",
     "", "Foot", "Boardwalk", "State-built",
     1.0, "Wayne", "Ohio DNAP", "", "Open",
     "Easy", "Boardwalk; ADA accessible",
     "1-mile boardwalk trail through Johnson Woods old-growth forest.",
     "Opened with preserve designation.",
     "", "No bikes. No pets.",
     "https://ohiodnap.gov/site/johnson-woods", ""),

    ("T3-003", "Casey's Trails",
     "", "Foot", "Natural surface", "District-built",
     None, "Wayne", "Wayne County Park District", "", "Open",
     "Easy-Moderate", "Natural surface",
     "Named trail loop system within Barnes Preserve, Wayne County Park District.",
     "", "", "",
     "https://www.waynecountyparkdistrict.org/barnes-preserve", ""),

    ("T6-002", "Wooster Memorial Park Trail System",
     "Spangler Trail System", "Foot", "Natural surface", "City-built",
     11.6, "Wayne", "City of Wooster (Public Properties Maintenance Division)",
     "Friends of Wooster Memorial Park", "Open",
     "Moderate", "1 mile ADA-accessible (Kenwood Acres section)",
     "11.6-mile foot trail system within Wooster Memorial Park featuring multiple named trails through 422 acres of primitive woodland.",
     "Created 1963; expanded through multiple land additions.",
     "Spangler Trail, Outer Trail, Old Field Trail, Education Trail, Trillium Trail, Strock Trail, Kenwood Trail, Hartman Trail, Sassafras Trail, Saddleback Trail, Roller Trail.",
     "Foot traffic only — no bikes, horses, motorized vehicles.",
     "https://www.woosteroh.com/parks/wooster-memorial-park", ""),

    ("T6-006", "Donald and Alice Noble Trail",
     "Noble Trail", "Foot", "Paved asphalt", "City-built",
     1.7, "Wayne", "City of Wooster", "", "Open",
     "Easy", "Paved; ADA accessible; 2 van-accessible parking spaces",
     "1.7-mile paved accessible trail within Oak Hill Park, Wooster.",
     "", "", "",
     "https://www.woosteroh.com/parks", ""),

    ("T6-M-002", "Marshallville Tigers Trail",
     "", "Foot", "Primitive/Rustic", "Village-built",
     0.6, "Wayne", "Village of Marshallville", "", "Open",
     "Easy", "Rustic/primitive",
     "0.6-mile rustic foot trail within Robert Brooker Nature Preserve, Marshallville.",
     "", "Named trail within Robert Brooker Nature Preserve (T6-M-001).",
     "", "", ""),

    ("T6-M-003", "Dwayne Groll Trail",
     "", "Foot", "Gravel/Chip-and-seal", "Village-built",
     0.4, "Wayne", "Village of Marshallville", "", "Open",
     "Easy", "Gravel/chip-and-seal",
     "0.4-mile gravel trail within Robert Brooker Nature Preserve, Marshallville.",
     "", "Named trail within Robert Brooker Nature Preserve (T6-M-001). Honoree: Dwayne Groll.",
     "", "", ""),

    ("T6-027", "Solar Trail",
     "", "Foot", "Chip-and-seal", "Village-built",
     0.1, "Wayne", "Village of Marshallville", "", "Open",
     "Easy", "Chip-and-seal",
     "0.1-mile chip-and-seal trail through solar field area within Robert Brooker Nature Preserve.",
     "", "Named trail within Robert Brooker Nature Preserve (T6-M-001).",
     "", "", ""),

    ("T7-001", "County Line Trail",
     "", "Foot;Bike", "Paved asphalt", "Rail-trail",
     6.7, "Wayne",
     "Rails to Trails of Wayne County", "", "Open",
     "Easy", "Paved; ADA accessible",
     "6.7-mile paved rail-trail between Creston and Rittman along the former Erie Lackawanna railroad corridor. Includes 0.9-mile on-road connector on Atlantic Avenue near Sterling.",
     "Constructed 2010 on former Erie Lackawanna corridor. Sterling Depot (historic B&O freight depot) along route.",
     "Entirely within Wayne County. Parallels active CSX mainline for much of its length. Dogs on leash.",
     "",
     "https://waynecountytrails.org/existing-trails/",
     "https://www.traillink.com/trail/county-line-trail-(oh)/"),

    ("T7-003", "Heartland Trail",
     "", "Foot;Bike", "Paved asphalt", "Rail-trail",
     3.7, "Wayne",
     "Rails to Trails of Wayne County", "", "Open/Partial",
     "Easy", "Paved; ADA accessible",
     "Paved rail-trail in Wayne County with two built sections (3.7 mi total) and a 1.6-mile gap between Orrville and the Marshallville section. Full route Orrville to Clinton projected at 9.4+ miles.",
     "W Market St → Allen Ave section opened 2016 (1.3 mi); Forrer Rd → Marshallville section opened 2019 (2.4 mi). Gap (Allen Ave → Forrer Rd, 1.6 mi) projected 2026.",
     "Allen Ave → Forrer Rd gap NOT YET BUILT as of 2026-03-08; projected 2026. Marshallville → Coal Bank Rd (1.1 mi) and Coal Bank Rd → Warwick Rd (2.1 mi) also projected.",
     "",
     "https://waynecountytrails.org/existing-trails/",
     "https://www.traillink.com/trail-maps/heartland-trail/"),

    ("T8-TR-001", "Vulture's Knob Trail System",
     "", "Mountain Bike", "Natural/Singletrack", "Purpose-built",
     None, "Wayne",
     "Friends of Vultures Knob (501(c)(3))", "", "Open",
     "Varies", "Singletrack mountain bike trails",
     "Mountain bike trail network within Vulture's Knob Mountain Bike Park.",
     "", "",
     "Ownership transferred Dec 31 2025; trail operating normally.",
     "https://www.vulturesknob.com", ""),
]

# ---------------------------------------------------------------------------
# NORMALIZED DATA — TRAIL NETWORKS (1 record)
# ---------------------------------------------------------------------------

TRAIL_NETWORKS = [
    ("T7-TN-001", "Rails to Trails of Wayne County Trail System",
     "Rail-trail Network", "Open",
     "Rails to Trails of Wayne County (501(c)(3) nonprofit)",
     "Rails to Trails of Wayne County", "",
     "Wayne", "Ohio",
     21.0, 2,
     "T7-001;T7-003",
     "Network of paved rail-trails in Wayne County operated by Rails to Trails of Wayne County nonprofit. Currently includes County Line Trail (6.7 mi) and Heartland Trail (3.7 mi built). Network will grow as additional Heartland Trail segments open.",
     "Sippo Valley Trail (T7-002) and Holmes County Trail (T7-004) held — multi-county.",
     "",
     "https://waynecountytrails.org", ""),
]

# ---------------------------------------------------------------------------
# NORMALIZED DATA — ACCESS POINTS (17 records)
# ---------------------------------------------------------------------------

# Format: (ap_id, name, ap_type, status, parent_entity_type,
#          parent_entity_id, county, township, municipality, address,
#          gps_lat, gps_lon, plus_code, features, identity_notes,
#          notes, url_primary)

ACCESS_POINTS = [
    ("T2-008", "Shreve Lake Boat Launch",
     "Boat Launch", "Open",
     "Site", "T2-003",
     "Wayne", "", "Shreve",
     "Township Rd 316, near Brown Rd, Shreve, Ohio",
     40.683140, -82.046120, "8MGV55J4+HX",
     "Boat ramp; vehicle/trailer parking; ODNR-managed",
     "", "",
     "https://ohiodnr.gov/go-and-do/hunt-fish/wildlife-areas/shreve-lake-wildlife-area"),

    ("T2-009", "Shreve Lake Fishing Pier",
     "Fishing Access", "Open",
     "Site", "T2-003",
     "Wayne", "", "Shreve",
     "Township Rd 316, SE corner of Shreve Lake, Ohio",
     40.683140, -82.046120, "8MGV55J4+HX",
     "Fishing pier; ODNR-managed",
     "", "",
     "https://ohiodnr.gov/go-and-do/hunt-fish/wildlife-areas/shreve-lake-wildlife-area"),

    ("T2-010", "Killbuck Marsh — Carrie Lane Parking Area",
     "Parking Area", "Open",
     "Site", "T2-004",
     "Wayne", "", "",
     "End of Carrie Lane, Wayne County",
     40.671349, -81.966247, "8MGVV5J5+RR",
     "Primitive pull-off; unpaved; hunting/wildlife access",
     "", "GPS-APPROXIMATE — primitive pull-off not Maps-indexed; area coordinate used.",
     "https://ohiodnr.gov/wps/portal/gov/odnr/go-and-do/hunt-fish/wildlife-areas/killbuck-marsh"),

    ("T2-011", "Killbuck Marsh — Wright Marsh Parking Area",
     "Parking Area", "Open",
     "Site", "T2-004",
     "Wayne", "", "",
     "OH-226 / Shreve Rd, Wayne County",
     40.671349, -81.966247, "8MGVV5J5+RR",
     "Primitive pull-off; OH-226 roadside; hunting/wildlife access",
     "", "GPS-APPROXIMATE — primitive pull-off not Maps-indexed; area coordinate used.",
     "https://ohiodnr.gov/wps/portal/gov/odnr/go-and-do/hunt-fish/wildlife-areas/killbuck-marsh"),

    ("T3-004", "Barnes Preserve Main Entrance — Romich Pavilion Parking",
     "Trailhead/Parking", "Open",
     "Site", "T3-001",
     "Wayne", "", "Wooster",
     "3396 Sylvan Rd, Wooster, Ohio",
     40.781233, -81.896940, "8MGWQ4J3+F6",
     "Paved parking lot; pavilion; trailhead kiosk",
     "", "",
     "https://www.waynecountyparkdistrict.org/barnes-preserve"),

    ("T5-003", "Chippewa Township Nature Preserve — Galehouse Road Entrance",
     "Trailhead/Parking", "Open",
     "Site", "T5-001",
     "Wayne", "Chippewa Township", "Doylestown",
     "17500 Galehouse Road, Doylestown, Ohio 44230",
     40.662400, -81.702500, "8MGVXR8H+22",
     "Parking; trailhead; pavilion reservation through township office",
     "", "GPS-APPROXIMATE — address geocode.",
     "http://www.chippewatwp.com"),

    ("T6-003", "Wooster Memorial Park — Silver Road Main Entrance",
     "Trailhead/Parking", "Open",
     "Site", "T6-001",
     "Wayne", "", "Wooster",
     "5197 Silver Road, Wooster, Ohio",
     40.813192, -82.027884, "8MGVRX9G+VF",
     "Primary parking lot; trailhead kiosk; vault toilet",
     "", "",
     "https://www.woosteroh.com/parks/wooster-memorial-park"),

    ("T6-004", "Wooster Memorial Park — Kenwood Acres ADA Entrance",
     "Trailhead/Parking", "Open",
     "Site", "T6-001",
     "Wayne", "", "Wooster",
     "Kenwood Acres area, Wooster, Ohio",
     40.811392, -82.020704, "8MGVRX9G+26",
     "ADA-accessible parking; 1-mile ADA trail access; opened 2018",
     "", "",
     "https://www.woosteroh.com/parks/wooster-memorial-park"),

    ("T6-028", "Robert Brooker Nature Preserve — Heartland Trail Trailhead",
     "Trailhead/Parking", "Open",
     "Site", "T6-M-001",
     "Wayne", "", "Marshallville",
     "Euclid St, Marshallville, Ohio",
     40.900680, -81.727749, "8MGWV5J5+GC",
     "Trailhead; bike rack; interpretive sign and map; Heartland Trail connection",
     "", "",
     "https://waynecountytrails.org/existing-trails/"),

    ("T7-AP-001", "County Line Trail — Rittman Trailhead",
     "Trailhead/Parking", "Open",
     "Trail", "T7-001",
     "Wayne", "", "Rittman",
     "Ohio St (near The Depot restaurant), Rittman, Ohio",
     40.971878, -81.776918, "8MGWX694+55",
     "Paved parking lot; trail kiosk; near The Depot restaurant",
     "", "",
     "https://waynecountytrails.org/existing-trails/"),

    ("T7-AP-002", "County Line Trail — Creston Trailhead",
     "Trailhead/Parking", "Open",
     "Trail", "T7-001",
     "Wayne", "", "Creston",
     "Creston, Ohio",
     40.989180, -81.892460, "8MGWX8H3+3X",
     "Parking; trailhead kiosk",
     "", "",
     "https://waynecountytrails.org/existing-trails/"),

    ("T7-AP-003", "County Line Trail — Kauffman Avenue Sterling Access",
     "Trailhead/Parking", "Open",
     "Trail", "T7-001",
     "Wayne", "", "Sterling",
     "Kauffman Ave, Sterling, Ohio",
     40.970757, -81.850588, "8MGWX6M4+XP",
     "Roadside access; on-road connector section nearby",
     "", "",
     "https://waynecountytrails.org/existing-trails/"),

    ("T7-AP-004", "Sippo Valley Trail — Dalton Trailhead",
     "Trailhead/Parking", "Open",
     "Trail", "T7-002",
     "Wayne", "", "Dalton",
     "Village Green Park, Freet St, just south of US 30 Alt./Main St., Dalton, Ohio",
     40.796528, -81.691498, "8MGWQ6P4+8R",
     "Village Green Park; parking; trail start; near US 30 Alt.",
     "", "",
     "https://www.traillink.com/trail-maps/sippo-valley-trail/"),

    ("T7-AP-005", "Heartland Trail — West Market Street Trailhead (Orrville)",
     "Trailhead/Parking", "Open",
     "Trail", "T7-003",
     "Wayne", "", "Orrville",
     "W Market St / N Ella St, Orrville, Ohio",
     40.840690, -81.769863, "8MGWX5P4+FG",
     "Paved parking; western Orrville trailhead; 1.3-mile built section begins here",
     "", "",
     "https://waynecountytrails.org/existing-trails/"),

    ("T7-AP-006", "Holmes County Trail — Fredericksburg Trailhead",
     "Trailhead/Parking", "Open",
     "Trail", "T7-004",
     "Wayne", "", "Fredericksburg",
     "Fredericksburg, Wayne County, Ohio",
     40.675335, -81.873400, "8MGVV5J4+QR",
     "Northern Wayne County trailhead for Holmes County Trail",
     "", "",
     "https://waynecountytrails.org/existing-trails/"),

    ("T8-AP-001", "Secrest Arboretum — Williams Road Entrance",
     "Trailhead/Parking", "Open",
     "Site", "T8-001",
     "Wayne", "", "Wooster",
     "1680 Madison Ave / Williams Rd, Wooster, Ohio (OARDC campus)",
     40.782984, -81.917203, "8MGWQ4JH+5G",
     "Parking; main entrance to arboretum; on OARDC campus",
     "", "",
     "https://secrestarboretum.osu.edu"),

    ("T8-AP-002", "Vulture's Knob — Main Trailhead",
     "Trailhead/Parking", "Open",
     "Site", "T8-002",
     "Wayne", "", "",
     "Near Wooster, Wayne County, Ohio",
     40.850970, -81.980600, "8MGWQ6J5+RF",
     "Main trailhead and parking area for Vulture's Knob Mountain Bike Park",
     "", "",
     "https://www.vulturesknob.com"),
]

# ---------------------------------------------------------------------------
# HELD ENTITIES
# ---------------------------------------------------------------------------

HELD = [
    ("T2-004", "Site", "Killbuck Marsh Wildlife Area", "Wayne",
     "multi_county",
     "Partner county Holmes not yet processed. Will release when Holmes County discovery run completes."),
    ("T2-007", "Trail", "Killbuck Marsh Wildlife Observation Trail", "Wayne",
     "identity_uncertain",
     "Two conflicting length descriptions found (3.7-mile vs walking trail). Trail existence inferred but not confirmed by ODNR trail inventory. Pending field verification."),
    ("T2-012", "Site", "Funk Bottoms Wildlife Area", "Wayne",
     "multi_county",
     "Partner county Ashland not yet processed. Will release when Ashland County discovery run completes."),
    ("T5-002", "Trail", "Chippewa Township Nature Preserve trails", "Wayne",
     "identity_uncertain",
     "Source describes 'several short hiking trails' with no individual trail names given. Trail count and names unconfirmed. Pending field verification."),
    ("T7-002", "Trail", "Sippo Valley Trail", "Wayne",
     "multi_county",
     "Partner county Stark not yet processed. Will release when Stark County discovery run completes."),
    ("T7-004", "Trail", "Holmes County Trail (Fredericksburg / Wayne County section)", "Wayne",
     "multi_county",
     "Partner county Holmes not yet processed. Will release when Holmes County discovery run completes."),
]

# ---------------------------------------------------------------------------
# UPSERT LOGIC
# ---------------------------------------------------------------------------

def upsert_site(cur, s, now):
    cur.execute("""
        INSERT INTO sites (
            site_id, name, category, subtype, designation, status,
            ownership, governance, partner_agencies, coordination,
            description, location, acres, counties, municipality, township,
            gps_lat, gps_lon, plus_code, features, notes,
            url_primary, urls, parent_site_id, created_at, updated_at
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(site_id) DO UPDATE SET
            name=excluded.name, category=excluded.category,
            subtype=excluded.subtype, designation=excluded.designation,
            status=excluded.status, ownership=excluded.ownership,
            governance=excluded.governance, partner_agencies=excluded.partner_agencies,
            coordination=excluded.coordination, description=excluded.description,
            location=excluded.location, acres=excluded.acres,
            counties=excluded.counties, municipality=excluded.municipality,
            township=excluded.township, gps_lat=excluded.gps_lat,
            gps_lon=excluded.gps_lon, plus_code=excluded.plus_code,
            features=excluded.features, notes=excluded.notes,
            url_primary=excluded.url_primary, urls=excluded.urls,
            parent_site_id=excluded.parent_site_id, updated_at=excluded.updated_at
    """, (*s, now, now))


def upsert_trail(cur, t, now):
    cur.execute("""
        INSERT INTO trails (
            trail_id, name, alternate_names, use_type, surface_type,
            origin_type, length_mi, counties, governance, partner_agencies,
            status, difficulty, accessibility, description, trail_history,
            identity_notes, notes, url_primary, maps, created_at, updated_at
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(trail_id) DO UPDATE SET
            name=excluded.name, alternate_names=excluded.alternate_names,
            use_type=excluded.use_type, surface_type=excluded.surface_type,
            origin_type=excluded.origin_type, length_mi=excluded.length_mi,
            counties=excluded.counties, governance=excluded.governance,
            partner_agencies=excluded.partner_agencies, status=excluded.status,
            difficulty=excluded.difficulty, accessibility=excluded.accessibility,
            description=excluded.description, trail_history=excluded.trail_history,
            identity_notes=excluded.identity_notes, notes=excluded.notes,
            url_primary=excluded.url_primary, maps=excluded.maps,
            updated_at=excluded.updated_at
    """, (*t, now, now))


def upsert_trail_network(cur, tn, now):
    cur.execute("""
        INSERT INTO trail_networks (
            network_id, name, network_type, status, ownership, governance,
            partner_agencies, counties, states_included, length_mi,
            member_trail_count, member_trail_ids, description,
            identity_notes, notes, url_primary, maps, created_at, updated_at
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(network_id) DO UPDATE SET
            name=excluded.name, network_type=excluded.network_type,
            status=excluded.status, ownership=excluded.ownership,
            governance=excluded.governance, partner_agencies=excluded.partner_agencies,
            counties=excluded.counties, states_included=excluded.states_included,
            length_mi=excluded.length_mi, member_trail_count=excluded.member_trail_count,
            member_trail_ids=excluded.member_trail_ids, description=excluded.description,
            identity_notes=excluded.identity_notes, notes=excluded.notes,
            url_primary=excluded.url_primary, maps=excluded.maps,
            updated_at=excluded.updated_at
    """, (*tn, now, now))


def upsert_access_point(cur, ap, now):
    cur.execute("""
        INSERT INTO access_points (
            access_point_id, name, ap_type, status, parent_entity_type,
            parent_entity_id, county, township, municipality, address,
            gps_lat, gps_lon, plus_code, features, identity_notes,
            notes, url_primary, created_at, updated_at
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(access_point_id) DO UPDATE SET
            name=excluded.name, ap_type=excluded.ap_type,
            status=excluded.status, parent_entity_type=excluded.parent_entity_type,
            parent_entity_id=excluded.parent_entity_id,
            county=excluded.county, township=excluded.township,
            municipality=excluded.municipality, address=excluded.address,
            gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon,
            plus_code=excluded.plus_code, features=excluded.features,
            identity_notes=excluded.identity_notes, notes=excluded.notes,
            url_primary=excluded.url_primary, updated_at=excluded.updated_at
    """, (*ap, now, now))


# ---------------------------------------------------------------------------
# RELATIONSHIP TABLE POPULATION
# ---------------------------------------------------------------------------

def populate_site_parent(cur, now):
    """Insert site_parent rows for all child sites."""
    count = 0
    for s in SITES:
        site_id, parent_site_id = s[0], s[23]
        if parent_site_id:
            cur.execute("""
                INSERT OR REPLACE INTO site_parent (site_id, parent_site_id)
                VALUES (?, ?)
            """, (site_id, parent_site_id))
            count += 1
    return count


def populate_trail_network_members(cur, now):
    """Insert trail_network_members rows from trail network member_trail_ids."""
    count = 0
    for tn in TRAIL_NETWORKS:
        network_id = tn[0]
        member_ids_str = tn[11]  # member_trail_ids field
        if member_ids_str:
            for trail_id in member_ids_str.split(";"):
                trail_id = trail_id.strip()
                if trail_id:
                    cur.execute("""
                        INSERT OR REPLACE INTO trail_network_members (network_id, trail_id)
                        VALUES (?, ?)
                    """, (network_id, trail_id))
                    count += 1
    return count


def populate_access_point_parents(cur, now):
    """Insert access_point_parents rows for each access point's identity parent."""
    count = 0
    for ap in ACCESS_POINTS:
        ap_id = ap[0]
        parent_entity_type = ap[4]
        parent_entity_id = ap[5]
        cur.execute("""
            INSERT OR REPLACE INTO access_point_parents
                (access_point_id, parent_entity_type, parent_entity_id)
            VALUES (?, ?, ?)
        """, (ap_id, parent_entity_type, parent_entity_id))
        count += 1
    return count


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Wayne County, Ohio — Natural Areas Upsert")
    parser.add_argument("--db", default=DEFAULT_DB, help=f"SQLite DB path (default: {DEFAULT_DB})")
    parser.add_argument("--dry-run", action="store_true", help="Print stats without writing")
    parser.add_argument("--reset-county", action="store_true",
                        help="Delete all existing Wayne County records before upserting")
    args = parser.parse_args()

    print(f"Natural Areas Project — Wayne County, Ohio Upsert")
    print(f"Database: {args.db}")
    print(f"Dry run: {args.dry_run}")
    print()

    if args.dry_run:
        print(f"DRY RUN — records that would be written:")
        print(f"  Sites:          {len(SITES)}")
        print(f"  Trails:         {len(TRAILS)}")
        print(f"  Trail Networks: {len(TRAIL_NETWORKS)}")
        print(f"  Access Points:  {len(ACCESS_POINTS)}")
        print(f"  Held:           {len(HELD)}")
        print(f"  Total:          {len(SITES)+len(TRAILS)+len(TRAIL_NETWORKS)+len(ACCESS_POINTS)} normalized + {len(HELD)} held")
        return

    con = sqlite3.connect(args.db)
    cur = con.cursor()

    # Create schema
    cur.executescript(SCHEMA_SQL)
    print("Schema: OK")

    # Optional county reset
    if args.reset_county:
        tables = ["sites", "trails", "trail_segments", "trail_networks",
                  "site_networks", "access_points"]
        for tbl in tables:
            cur.execute(f"DELETE FROM {tbl} WHERE counties LIKE '%Wayne%' OR county LIKE '%Wayne%'")
        cur.execute("DELETE FROM held_entities WHERE county='Wayne' AND run_id=?", (RUN_ID,))
        print(f"Reset: Wayne County records cleared from all tables.")

    now = datetime.now(timezone.utc).isoformat()

    # Upsert sites
    for s in SITES:
        upsert_site(cur, s, now)
    print(f"Sites:          {len(SITES)} upserted")

    # Upsert trails
    for t in TRAILS:
        upsert_trail(cur, t, now)
    print(f"Trails:         {len(TRAILS)} upserted")

    # Upsert trail networks
    for tn in TRAIL_NETWORKS:
        upsert_trail_network(cur, tn, now)
    print(f"Trail Networks: {len(TRAIL_NETWORKS)} upserted")

    # Upsert access points
    for ap in ACCESS_POINTS:
        upsert_access_point(cur, ap, now)
    print(f"Access Points:  {len(ACCESS_POINTS)} upserted")

    # Populate relationship tables
    n_sp = populate_site_parent(cur, now)
    print(f"site_parent:    {n_sp} rows")
    n_tnm = populate_trail_network_members(cur, now)
    print(f"trail_network_members: {n_tnm} rows")
    n_app = populate_access_point_parents(cur, now)
    print(f"access_point_parents:  {n_app} rows")

    # Write held entities
    for h in HELD:
        cur.execute("""
            INSERT INTO held_entities
                (record_id, entity_type, name, county, hold_reason, hold_detail, run_id, created_at)
            VALUES (?,?,?,?,?,?,?,?)
        """, (*h, RUN_ID, now))
    print(f"Held:           {len(HELD)} written to held_entities table")

    # Write run metadata
    total_norm = len(SITES) + len(TRAILS) + len(TRAIL_NETWORKS) + len(ACCESS_POINTS)
    cur.execute("""
        INSERT OR REPLACE INTO run_metadata
            (run_id, county, state, run_date, records_input, normalized, held, rejected, notes, created_at)
        VALUES (?,?,?,?,?,?,?,?,?,?)
    """, (RUN_ID, COUNTY, STATE, RUN_DATE,
          79, total_norm, len(HELD), 0,
          "Resolution Pass 1 + Normalization complete. 6 held (4 multi-county, 2 identity-uncertain).",
          now))
    print(f"Run metadata:   written (run_id={RUN_ID})")

    # Write discovery provenance
    all_records = (
        [(s[0], "Site", s[13], int(s[0][1])) for s in SITES] +
        [(t[0], "Trail", t[7], int(t[0][1])) for t in TRAILS] +
        [(tn[0], "Trail Network", tn[7], int(tn[0][1])) for tn in TRAIL_NETWORKS] +
        [(ap[0], "Access Point", ap[6], int(ap[0][1])) for ap in ACCESS_POINTS]
    )
    for eid, etype, county, tier in all_records:
        cur.execute("""
            INSERT INTO discovery_provenance
                (entity_id, entity_type, county, discovery_tier, source_notes, run_id, created_at)
            VALUES (?,?,?,?,?,?,?)
        """, (eid, etype, county, tier, f"Wayne County {RUN_DATE} discovery run", RUN_ID, now))

    con.commit()
    con.close()

    print()
    print(f"✓ Upsert complete — {total_norm} records written to {args.db}")
    print(f"  Sites: {len(SITES)} | Trails: {len(TRAILS)} | Networks: {len(TRAIL_NETWORKS)} | Access Points: {len(ACCESS_POINTS)}")
    print(f"  Held: {len(HELD)} | Rejected: 0")
    print()
    print("Held entities (awaiting partner county runs or field verification):")
    for h in HELD:
        print(f"  {h[0]:15s} {h[1]:15s} {h[2][:45]}")
        print(f"             Reason: {h[4]} — {h[5][:60]}")


if __name__ == "__main__":
    main()
