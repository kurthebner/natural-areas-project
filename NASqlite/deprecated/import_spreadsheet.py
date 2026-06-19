"""
Import and normalize spreadsheet data into the Natural Areas database.

This script can import data from:
- Excel files (.xlsx, .xls)
- CSV files (.csv)

It handles:
- Column mapping from spreadsheet to database schema
- Data normalization (splitting semicolon-delimited fields)
- Data type conversion
- Validation
"""

import sqlite3
import pandas as pd
import sys
from pathlib import Path
from database import get_connection, init_database

# Field mapping: spreadsheet column name -> database field name
# Add or modify these mappings based on your spreadsheet column names
COLUMN_MAPPING = {
    # Direct mappings
    'name': 'name',
    'type': 'type',
    'description': 'description',
    'status': 'status',
    'ownership': 'ownership',
    'address': 'address',
    'acres': 'acres',
    'gps_coordinates': 'gps_coordinates',
    'plus_code': 'plus_code',
    'trail_role': 'trail_role',
    'parent_trail_name': 'parent_trail_name',
    'trail_segment_type': 'trail_segment_type',
    'trail_access_type': 'trail_access_type',
    'trail_length_miles': 'trail_length_miles',
    'notes': 'notes',
    
    # Common variations
    'Name': 'name',
    'Type': 'type',
    'Description': 'description',
    'Status': 'status',
    'Ownership': 'ownership',
    'Address': 'address',
    'Acres': 'acres',
    'GPS Coordinates': 'gps_coordinates',
    'GPS': 'gps_coordinates',
    'Coordinates': 'gps_coordinates',
    'Plus Code': 'plus_code',
    'Trail Role': 'trail_role',
    'Parent Trail': 'parent_trail_name',
    'Trail Segment Type': 'trail_segment_type',
    'Trail Access Type': 'trail_access_type',
    'Trail Length': 'trail_length_miles',
    'Length (Miles)': 'trail_length_miles',
    'Notes': 'notes',
    'Management': 'management',
    'Coordination': 'coordination',
    'Location': 'location',
    'County': 'county',
    'Counties': 'county',
    'Features': 'features',
    'URL': 'url',
    'URLs': 'url',
    'Website': 'url',
}

def normalize_semicolon_field(value):
    """Normalize a semicolon-delimited field (remove extra spaces, sort if needed)."""
    if pd.isna(value) or value == '':
        return None
    # Split by semicolon, strip whitespace, filter empty strings
    parts = [part.strip() for part in str(value).split(';') if part.strip()]
    if not parts:
        return None
    return '; '.join(parts)  # Join with '; ' for consistency

def normalize_county(value):
    """Normalize county field (semicolon-delimited, alphabetical)."""
    if pd.isna(value) or value == '':
        return None
    parts = [part.strip() for part in str(value).split(';') if part.strip()]
    if not parts:
        return None
    # Sort alphabetically as per data dictionary
    parts.sort()
    return '; '.join(parts)

def normalize_numeric(value, field_name=''):
    """Convert value to numeric, return None if invalid."""
    if pd.isna(value) or value == '':
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        print(f"Warning: Could not convert {field_name} to numeric: {value}")
        return None

def normalize_gps_coordinates(value):
    """Normalize GPS coordinates to 'lat,lon' format."""
    if pd.isna(value) or value == '':
        return None
    value = str(value).strip()
    # Handle various formats
    # Remove parentheses, brackets, etc.
    value = value.replace('(', '').replace(')', '').replace('[', '').replace(']', '')
    # Split by common delimiters
    for sep in [',', ' ', ';', '\t']:
        if sep in value:
            parts = [p.strip() for p in value.split(sep, 1)]
            if len(parts) == 2:
                try:
                    lat = float(parts[0])
                    lon = float(parts[1])
                    return f"{lat},{lon}"
                except ValueError:
                    pass
    # If already in correct format, return as-is
    if ',' in value:
        return value
    return None

def map_row_to_database(row, column_mapping):
    """Map a spreadsheet row to database fields."""
    db_row = {}
    
    for spreadsheet_col, db_field in column_mapping.items():
        if spreadsheet_col in row.index:
            value = row[spreadsheet_col]
            
            # Handle different field types
            if db_field == 'acres' or db_field == 'trail_length_miles':
                db_row[db_field] = normalize_numeric(value, db_field)
            elif db_field == 'county':
                db_row[db_field] = normalize_county(value)
            elif db_field in ['management', 'coordination', 'location', 'features', 'url']:
                db_row[db_field] = normalize_semicolon_field(value)
            elif db_field == 'gps_coordinates':
                db_row[db_field] = normalize_gps_coordinates(value)
            else:
                # Text fields - convert to string, None if empty
                if pd.isna(value) or value == '':
                    db_row[db_field] = None
                else:
                    db_row[db_field] = str(value).strip()
    
    return db_row

def detect_column_mapping(df):
    """Auto-detect column mapping from dataframe."""
    detected = {}
    spreadsheet_cols = df.columns.tolist()
    
    # First, try exact matches
    for col in spreadsheet_cols:
        col_lower = col.lower().strip()
        # Check direct mapping
        if col in COLUMN_MAPPING:
            detected[col] = COLUMN_MAPPING[col]
        # Check case-insensitive
        elif col_lower in [k.lower() for k in COLUMN_MAPPING.keys()]:
            for key in COLUMN_MAPPING.keys():
                if key.lower() == col_lower:
                    detected[col] = COLUMN_MAPPING[key]
                    break
    
    return detected

def import_spreadsheet(file_path, column_mapping=None, preview=False):
    """
    Import spreadsheet data into the database.
    
    Args:
        file_path: Path to spreadsheet file (.xlsx, .xls, or .csv)
        column_mapping: Optional dict mapping spreadsheet columns to DB fields
        preview: If True, only show what would be imported without actually importing
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return
    
    print(f"Reading spreadsheet: {file_path}")
    
    # Read the spreadsheet
    try:
        if file_path.suffix.lower() == '.csv':
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading spreadsheet: {e}")
        return
    
    print(f"Found {len(df)} rows and {len(df.columns)} columns")
    print(f"\nColumns in spreadsheet:")
    for col in df.columns:
        print(f"  - {col}")
    
    # Detect or use provided column mapping
    if column_mapping is None:
        column_mapping = detect_column_mapping(df)
        print(f"\nAuto-detected column mapping:")
        for spreadsheet_col, db_field in column_mapping.items():
            print(f"  {spreadsheet_col} -> {db_field}")
    else:
        print(f"\nUsing provided column mapping:")
        for spreadsheet_col, db_field in column_mapping.items():
            print(f"  {spreadsheet_col} -> {db_field}")
    
    # Check if name field is mapped (required)
    if 'name' not in column_mapping.values():
        print("\nWarning: 'name' field not mapped. This is required.")
        print("Please provide a column mapping that includes 'name'.")
        return
    
    # Map rows to database format
    db_rows = []
    for idx, row in df.iterrows():
        db_row = map_row_to_database(row, column_mapping)
        if db_row.get('name'):  # Only include rows with a name
            db_rows.append(db_row)
    
    print(f"\nMapped {len(db_rows)} rows to database format")
    
    if preview:
        print("\nPreview of first 3 rows that would be imported:")
        for i, db_row in enumerate(db_rows[:3], 1):
            print(f"\nRow {i}:")
            for key, value in db_row.items():
                if value is not None:
                    print(f"  {key}: {value}")
        return
    
    # Insert into database
    conn = get_connection()
    cursor = conn.cursor()
    
    # Get all database fields
    db_fields = [
        'name', 'type', 'description', 'status', 'ownership', 'management',
        'coordination', 'address', 'acres', 'location', 'county',
        'gps_coordinates', 'plus_code', 'trail_role', 'parent_trail_name',
        'trail_segment_type', 'trail_access_type', 'trail_length_miles',
        'features', 'notes', 'url'
    ]
    
    inserted = 0
    skipped = 0
    
    for db_row in db_rows:
        # Build INSERT statement with only fields that have values
        fields = [f for f in db_fields if f in db_row and db_row[f] is not None]
        if not fields:
            skipped += 1
            continue
        
        placeholders = ', '.join(['?' for _ in fields])
        field_names = ', '.join(fields)
        
        values = [db_row[f] for f in fields]
        
        try:
            cursor.execute(f"""
                INSERT INTO natural_areas ({field_names})
                VALUES ({placeholders})
            """, values)
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"Warning: Skipped row (integrity error): {e}")
            skipped += 1
        except Exception as e:
            print(f"Error inserting row: {e}")
            print(f"  Row data: {db_row}")
            skipped += 1
    
    conn.commit()
    conn.close()
    
    print(f"\nImport complete!")
    print(f"  Inserted: {inserted} rows")
    if skipped > 0:
        print(f"  Skipped: {skipped} rows")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python import_spreadsheet.py <spreadsheet_file> [--preview]")
        print("\nExample:")
        print("  python import_spreadsheet.py data.xlsx")
        print("  python import_spreadsheet.py data.csv --preview")
        sys.exit(1)
    
    file_path = sys.argv[1]
    preview = '--preview' in sys.argv
    
    # Ensure database is initialized
    init_database()
    
    import_spreadsheet(file_path, preview=preview)
