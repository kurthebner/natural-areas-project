------------------------------------------------------------
-- 1. PRIMARY TABLE: SITES (24-FIELD CORE SCHEMA)
------------------------------------------------------------
CREATE TABLE sites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- Core identity fields
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    subtype TEXT,
    designation TEXT,  -- Only if single; multi handled in join table

    -- Governance
    ownership TEXT,
    -- Management & coordination handled via join tables

    -- Description & status
    description TEXT,
    status TEXT,

    -- Location & geography
    address TEXT,
    acres REAL,
    location TEXT,
    county TEXT NOT NULL,
    gps_lat REAL,
    gps_lon REAL,
    plus_code TEXT,

    -- Trail fields
    trail_role TEXT,
    parent_trail_name TEXT,
    trail_segment_type TEXT,
    trail_access_type TEXT,
    trail_length_miles REAL,

    -- Notes
    notes TEXT,

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_sites_name ON sites(name);
CREATE INDEX idx_sites_category ON sites(category);
CREATE INDEX idx_sites_county ON sites(county);
CREATE INDEX idx_sites_trail_role ON sites(trail_role);
CREATE INDEX idx_sites_plus_code ON sites(plus_code);

------------------------------------------------------------
-- 2. FEATURES (CONTROLLED VOCABULARY)
------------------------------------------------------------
CREATE TABLE features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feature_name TEXT UNIQUE NOT NULL
);

CREATE TABLE site_features (
    site_id INTEGER NOT NULL,
    feature_id INTEGER NOT NULL,
    PRIMARY KEY (site_id, feature_id),
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES features(id) ON DELETE CASCADE
);

------------------------------------------------------------
-- 3. URLS (MULTI-VALUE)
------------------------------------------------------------
CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT UNIQUE NOT NULL
);

CREATE TABLE site_urls (
    site_id INTEGER NOT NULL,
    url_id INTEGER NOT NULL,
    PRIMARY KEY (site_id, url_id),
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    FOREIGN KEY (url_id) REFERENCES urls(id) ON DELETE CASCADE
);

------------------------------------------------------------
-- 4. DESIGNATIONS (MULTI-VALUE)
------------------------------------------------------------
CREATE TABLE designations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    designation_name TEXT UNIQUE NOT NULL
);

CREATE TABLE site_designations (
    site_id INTEGER NOT NULL,
    designation_id INTEGER NOT NULL,
    PRIMARY KEY (site_id, designation_id),
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    FOREIGN KEY (designation_id) REFERENCES designations(id) ON DELETE CASCADE
);

------------------------------------------------------------
-- 5. MANAGEMENT ENTITIES (MULTI-VALUE)
------------------------------------------------------------
CREATE TABLE management_entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_name TEXT UNIQUE NOT NULL
);

CREATE TABLE site_management (
    site_id INTEGER NOT NULL,
    management_id INTEGER NOT NULL,
    PRIMARY KEY (site_id, management_id),
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    FOREIGN KEY (management_id) REFERENCES management_entities(id) ON DELETE CASCADE
);

------------------------------------------------------------
-- 6. COORDINATION ENTITIES (MULTI-VALUE)
------------------------------------------------------------
CREATE TABLE coordination_entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_name TEXT UNIQUE NOT NULL
);

CREATE TABLE site_coordination (
    site_id INTEGER NOT NULL,
    coordination_id INTEGER NOT NULL,
    PRIMARY KEY (site_id, coordination_id),
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    FOREIGN KEY (coordination_id) REFERENCES coordination_entities(id) ON DELETE CASCADE
);

------------------------------------------------------------
-- 7. MULTI-COUNTY SUPPORT (OPTIONAL BUT POWERFUL)
------------------------------------------------------------
CREATE TABLE counties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    county_name TEXT UNIQUE NOT NULL
);

CREATE TABLE site_counties (
    site_id INTEGER NOT NULL,
    county_id INTEGER NOT NULL,
    PRIMARY KEY (site_id, county_id),
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    FOREIGN KEY (county_id) REFERENCES counties(id) ON DELETE CASCADE
);

------------------------------------------------------------
-- 8. AUDIT LOG (ALIGNS WITH AUDIT & LOGGING MODULE)
------------------------------------------------------------
CREATE TABLE audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_id INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    action_type TEXT NOT NULL,  -- e.g., "conflict", "correction", "exclusion"
    field_name TEXT,
    original_value TEXT,
    new_value TEXT,
    source TEXT,
    module TEXT,
    notes TEXT,
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE SET NULL
);

CREATE INDEX idx_audit_site ON audit_log(site_id);
CREATE INDEX idx_audit_action ON audit_log(action_type);

------------------------------------------------------------
-- 9. MODULE VERSIONING (FOR REPRODUCIBILITY)
------------------------------------------------------------
CREATE TABLE module_versions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_name TEXT NOT NULL,
    version TEXT NOT NULL,
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

------------------------------------------------------------
-- 10. PROCESSING RUNS (OPTIONAL BUT IDEAL)
------------------------------------------------------------
CREATE TABLE processing_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    county TEXT NOT NULL,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP,
    baseline_version TEXT,
    discovery_version TEXT,
    resolution_version TEXT,
    normalization_version TEXT,
    orchestration_version TEXT,
    audit_version TEXT
);