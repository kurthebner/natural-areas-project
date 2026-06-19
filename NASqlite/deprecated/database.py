"""
SQLite Database Manager for Natural Areas & Trails
Based on the Natural Areas & Trails Data Dictionary (Fields 1-21)
"""
import sqlite3
import os
from pathlib import Path

# Database file path
DB_PATH = Path(__file__).parent / "natural_areas.db"

def get_connection():
    """Get a database connection."""
    return sqlite3.connect(DB_PATH)

def init_database():
    """Initialize the database with the full 21-field schema."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create the natural_areas table with all 21 fields from the data dictionary
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS natural_areas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            -- Field 1: Name
            name TEXT NOT NULL,
            -- Field 2: Type (governance-aligned classification)
            type TEXT,
            -- Field 3: Description
            description TEXT,
            -- Field 4: Status
            status TEXT,
            -- Field 5: Ownership
            ownership TEXT,
            -- Field 6: Management (semicolon-delimited)
            management TEXT,
            -- Field 7: Coordination (semicolon-delimited)
            coordination TEXT,
            -- Field 8: Address
            address TEXT,
            -- Field 9: Acres (numeric)
            acres REAL,
            -- Field 10: Location (municipality/township, semicolon-delimited)
            location TEXT,
            -- Field 11: County (semicolon-delimited, alphabetical)
            county TEXT,
            -- Field 12: GPS Coordinates (format: "lat,lon")
            gps_coordinates TEXT,
            -- Field 13: Plus Code
            plus_code TEXT,
            -- Field 14: Trail Role
            trail_role TEXT,
            -- Field 15: Parent Trail Name
            parent_trail_name TEXT,
            -- Field 16: Trail Segment Type
            trail_segment_type TEXT,
            -- Field 17: Trail Access Type
            trail_access_type TEXT,
            -- Field 18: Trail Length (Miles)
            trail_length_miles REAL,
            -- Field 19: Features (semicolon-delimited)
            features TEXT,
            -- Field 20: Notes
            notes TEXT,
            -- Field 21: URL (semicolon-delimited)
            url TEXT,
            -- Metadata
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create indexes for common queries
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_name ON natural_areas(name)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_type ON natural_areas(type)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_status ON natural_areas(status)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_county ON natural_areas(county)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_trail_role ON natural_areas(trail_role)
    """)
    
    conn.commit()
    conn.close()
    print(f"Database initialized at: {DB_PATH}")
    print("Schema includes all 21 fields from the Natural Areas & Trails Data Dictionary")

def reset_database():
    """Reset the database (drop all tables)."""
    if DB_PATH.exists():
        os.remove(DB_PATH)
        print("Database file removed.")
    init_database()
    print("Database reset complete.")

if __name__ == "__main__":
    init_database()
