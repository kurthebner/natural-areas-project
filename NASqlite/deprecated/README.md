# Natural Areas & Trails SQLite Database

A SQLite database implementation of the Natural Areas & Trails Data Dictionary (Fields 1-21), designed for cataloging parks, preserves, natural areas, trail systems, trail segments, and trail access infrastructure.

## Setup

1. Initialize the database:
   ```bash
   python database.py
   ```

This will create a `natural_areas.db` file in the current directory with the complete 21-field schema.

## Database Schema

The database includes a `natural_areas` table with all 21 fields from the data dictionary:

1. **name** - Official name (required)
2. **type** - Governance-aligned classification (controlled vocabulary)
3. **description** - Concise summary (1-3 sentences)
4. **status** - Active, Seasonal, Access Permit Required, No Public Entry, Under Development, Proposed, Abandoned, Closed
5. **ownership** - Legal owner
6. **management** - Managing entity/entities (semicolon-delimited)
7. **coordination** - Coordinating entities (semicolon-delimited)
8. **address** - Street address
9. **acres** - Total acreage (numeric)
10. **location** - Municipality/township (semicolon-delimited)
11. **county** - County/counties (semicolon-delimited, alphabetical)
12. **gps_coordinates** - Decimal degrees format: "lat,lon"
13. **plus_code** - Google Open Location Code
14. **trail_role** - Trail System, Trail Segment, Trail, Connector Trail/Spur, Trailhead, Trail Access Point, Bikeway Access Point, Bikeway Spur, Greenway Corridor, None
15. **parent_trail_name** - Parent trail system name
16. **trail_segment_type** - Connector, Crossing, Loop, Linear, Access Segment, None
17. **trail_access_type** - Trailhead, Access Point, Connector, Crossing, None
18. **trail_length_miles** - Length in miles (numeric)
19. **features** - Semicolon-delimited list from controlled vocabulary
20. **notes** - Additional context and clarifications
21. **url** - Authoritative URLs (semicolon-delimited)

Plus metadata fields:
- **id** - Primary key (auto-increment)
- **created_at** - Timestamp of creation
- **updated_at** - Timestamp of last update

## Usage

### Python Example

```python
from database import get_connection

# Get a connection
conn = get_connection()
cursor = conn.cursor()

# Insert data
cursor.execute("""
    INSERT INTO natural_areas (
        name, type, description, status, ownership, acres, county, location
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "Example State Park",
    "State Park",
    "A protected forest area with high-quality riparian habitat.",
    "Active",
    "Ohio Department of Natural Resources",
    150.5,
    "Franklin",
    "Columbus"
))

conn.commit()

# Query data
cursor.execute("SELECT name, type, county FROM natural_areas WHERE status = ?", ("Active",))
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
```

### Using SQLite Command Line

You can also interact with the database using the SQLite command-line tool:

```bash
sqlite3 natural_areas.db
```

Then run SQL commands:
```sql
.tables
.schema natural_areas
SELECT name, type, county FROM natural_areas;
```

## Data Dictionary

For complete field definitions, rules, and controlled vocabularies, see the `natural-areas-project.md` file in the parent directory.
