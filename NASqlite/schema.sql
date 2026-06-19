CREATE TABLE sites (
    site_id TEXT PRIMARY KEY,
    name TEXT, category TEXT, subtype TEXT, designation TEXT, status TEXT,
    ownership TEXT, governance TEXT, partner_agencies TEXT, coordination TEXT,
    description TEXT, location TEXT, acres REAL, counties TEXT, municipality TEXT,
    township TEXT, gps_lat REAL, gps_lon REAL, plus_code TEXT, features TEXT,
    notes TEXT, url_primary TEXT, urls TEXT, parent_site_id TEXT,
    created_at TEXT, updated_at TEXT, features_raw TEXT
);
CREATE TABLE trails (
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
CREATE TABLE trail_segments (
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
CREATE TABLE trail_networks (
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
CREATE TABLE site_networks (
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
, org_type TEXT);
CREATE TABLE access_points (
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
CREATE TABLE site_parent (
    site_id         TEXT NOT NULL,
    parent_site_id  TEXT NOT NULL,
    PRIMARY KEY (site_id, parent_site_id)
);
CREATE TABLE trail_to_segment (
    trail_id        TEXT NOT NULL,
    segment_id      TEXT NOT NULL,
    PRIMARY KEY (trail_id, segment_id)
);
CREATE TABLE trail_network_members (
    network_id      TEXT NOT NULL,
    trail_id        TEXT NOT NULL,
    PRIMARY KEY (network_id, trail_id)
);
CREATE TABLE site_network_members (
    network_id      TEXT NOT NULL,
    site_id         TEXT NOT NULL,
    PRIMARY KEY (network_id, site_id)
);
CREATE TABLE access_point_parents (
    access_point_id     TEXT NOT NULL,
    parent_entity_type  TEXT NOT NULL,
    parent_entity_id    TEXT NOT NULL,
    PRIMARY KEY (access_point_id, parent_entity_type, parent_entity_id)
);
CREATE TABLE entity_conflicts (
    conflict_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    field           TEXT NOT NULL,
    value_a         TEXT,
    value_b         TEXT,
    run_id          TEXT,
    created_at      TEXT
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE entity_uncertainty (
    uncertainty_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    field           TEXT,
    uncertainty_note TEXT,
    run_id          TEXT,
    created_at      TEXT
);
CREATE TABLE entity_geometry (
    geometry_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    geometry_type   TEXT,
    geometry_wkt    TEXT,
    source          TEXT,
    run_id          TEXT,
    created_at      TEXT
);
CREATE TABLE manual_review_queue (
    review_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    record_id       TEXT,
    entity_type     TEXT,
    name            TEXT,
    issue           TEXT,
    run_id          TEXT,
    created_at      TEXT
);
CREATE TABLE run_metadata (
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
CREATE TABLE discovery_provenance (
    prov_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT,
    entity_type     TEXT,
    county          TEXT,
    discovery_tier  INTEGER,
    source_notes    TEXT,
    run_id          TEXT,
    created_at      TEXT
);
CREATE TABLE resolution_provenance (
    prov_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT,
    entity_type     TEXT,
    county          TEXT,
    resolution_run  TEXT,
    notes           TEXT,
    run_id          TEXT,
    created_at      TEXT
);
CREATE TABLE normalization_provenance (
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
CREATE TABLE trail_parents (
    trail_id        TEXT NOT NULL REFERENCES trails(trail_id),
    parent_site_id  TEXT NOT NULL REFERENCES sites(site_id),
    PRIMARY KEY (trail_id, parent_site_id)
);
CREATE TABLE IF NOT EXISTS "held_entities" (
    held_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    record_id   TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    name        TEXT NOT NULL,
    county      TEXT,
    hold_reason TEXT,
    hold_detail TEXT,
    run_id      TEXT,
    created_at  TEXT,
    UNIQUE(record_id)
);
