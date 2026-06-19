"""
Comprehensive fix and verification script for Natural Areas spreadsheet.
Fixes common issues and prepares data for web verification.
"""

import pandas as pd
import sys
from pathlib import Path
import re
from typing import Dict, Optional

def fix_type_mappings():
    """Map common invalid types to valid controlled vocabulary types."""
    return {
        'Community Park': 'Municipal Park',
        'Neighborhood Park': 'Municipal Park',
        'Nature Park': 'Municipal Park',
        'City Park': 'Municipal Park',
        'Township Park': 'Township Park',  # This is actually valid
        'County Park': 'County Park',  # This is actually valid
        'State Park': 'State Park',  # This is actually valid
        'National Park': 'National Park',  # This is actually valid
    }

def normalize_type(type_str: str) -> str:
    """Normalize Type field with common mappings."""
    if pd.isna(type_str) or type_str == '':
        return ''
    
    type_str = str(type_str).strip()
    mappings = fix_type_mappings()
    
    # Check if it needs mapping
    if type_str in mappings:
        return mappings[type_str]
    
    # Valid types from the data dictionary
    valid_types = [
        'Arboretum', 'Army Corps of Engineers Property', 'BSA Camp',
        'Bureau of Land Management Lands', 'Canal Corridor', 'Cemetery',
        'City Nature Preserve', 'College Campus Property', 'Conservancy Property',
        'Controversial', 'County Nature Preserve', 'County Park', 'Covered Bridge',
        'Fish Hatchery', 'Fishing Access', 'Flood Control Area', 'Greenway',
        'Historic Site', 'Historical Park', 'Internal Feature', 'Land Trail',
        'Land Trust Preserve', 'Mill', 'Municipal Park', 'Museum',
        'National Forest', 'National Historic Landmark', 'National Historic Site',
        'National Natural Landmark', 'National Park', 'National Recreation Area',
        'National Scenic River', 'National Scenic Trail', 'National Wildlife Refuge',
        'Nonprofit Nature Preserve', 'Park District Conservation Area',
        'Park District Park', 'Private Campground', 'Private Conservation Area',
        'Private Hunting Reserve', 'Private Nature Reserve', 'Private Park',
        'Public School Property', 'Rail Trail', 'Recreation Facility',
        'Reservoir Property', 'Research Forest', 'State Conservation Area',
        'State Fishing Area', 'State Forest', 'State Historical Site',
        'State Memorial', 'State Natural Area', 'State Nature Preserve',
        'State Park', 'State Recreation Area', 'State Scenic River',
        'State Scenic Trail', 'State Wildlife Area', 'Township Nature Preserve',
        'Township Park', 'Tribal Conservation Area', 'Tribal Park',
        'University Natural Area', 'Utility Corridor Recreation Area',
        'Water Authority Land', 'Water Trail'
    ]
    
    if type_str in valid_types:
        return type_str
    
    return type_str  # Return as-is if can't map

def fix_trail_role(role_str: str) -> str:
    """Fix Trail Role field."""
    if pd.isna(role_str) or role_str == '':
        return 'None'
    
    role_str = str(role_str).strip()
    
    valid_roles = [
        'Trail System', 'Trail Segment', 'Trail', 'Connector Trail / Spur',
        'Trailhead', 'Trail Access Point', 'Bikeway Access Point',
        'Bikeway Spur', 'Greenway Corridor', 'None'
    ]
    
    # Handle common variations
    role_lower = role_str.lower()
    if role_lower in ['no', 'n', 'false', '0', 'nan']:
        return 'None'
    
    if role_str in valid_roles:
        return role_str
    
    # Try to map common variations
    role_mappings = {
        'Trail': 'Trail',
        'Trailhead': 'Trailhead',
        'Trail System': 'Trail System',
        'Trail Segment': 'Trail Segment',
    }
    
    for key, value in role_mappings.items():
        if key.lower() in role_lower:
            return value
    
    return 'None'  # Default to None if unclear

def fix_gps_coordinates(gps_str: str) -> Optional[str]:
    """Fix GPS coordinates - remove placeholders, normalize format."""
    if pd.isna(gps_str) or gps_str == '':
        return None
    
    gps_str = str(gps_str).strip()
    
    # Check for placeholders like 39.0,-84.0
    if re.match(r'^-?\d+\.0+,-?\d+\.0+$', gps_str.replace(' ', '')):
        return None  # Remove placeholder
    
    # Normalize format: should be "lat,lon" with no space after comma
    gps_str = gps_str.replace(' ', '')
    
    # Validate format
    try:
        parts = gps_str.split(',')
        if len(parts) == 2:
            lat = float(parts[0])
            lon = float(parts[1])
            # Check if coordinates are reasonable
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                return f"{lat},{lon}"
    except (ValueError, IndexError):
        pass
    
    return gps_str  # Return as-is if can't parse

def normalize_county(county_str: str) -> str:
    """Normalize County field."""
    if pd.isna(county_str) or county_str == '':
        return ''
    
    county_str = str(county_str).strip()
    
    # Split by semicolon
    counties = [c.strip() for c in county_str.split(';') if c.strip()]
    
    # Remove "County" suffix
    counties = [c.replace(' County', '').replace(' county', '').strip() for c in counties]
    
    # Sort alphabetically
    counties.sort()
    
    return '; '.join(counties)

def fix_spreadsheet(file_path: str) -> pd.DataFrame:
    """Fix common issues in the spreadsheet."""
    print(f"Reading spreadsheet: {file_path}")
    df = pd.read_excel(file_path)
    
    print(f"Found {len(df)} rows")
    
    # Create a copy for modifications
    df_fixed = df.copy()
    
    fixes_applied = {
        'type_fixes': 0,
        'trail_role_fixes': 0,
        'gps_fixes': 0,
        'county_fixes': 0,
    }
    
    # Process each row
    for idx, row in df_fixed.iterrows():
        # Fix Type
        if 'Type' in df_fixed.columns:
            original_type = row['Type']
            fixed_type = normalize_type(original_type)
            if fixed_type != str(original_type):
                df_fixed.at[idx, 'Type'] = fixed_type
                fixes_applied['type_fixes'] += 1
        
        # Fix Trail Role
        if 'Trail Role' in df_fixed.columns:
            original_role = row['Trail Role']
            fixed_role = fix_trail_role(original_role)
            if fixed_role != str(original_role):
                df_fixed.at[idx, 'Trail Role'] = fixed_role
                fixes_applied['trail_role_fixes'] += 1
        
        # Fix GPS Coordinates
        if 'GPS Coordinates' in df_fixed.columns:
            original_gps = row['GPS Coordinates']
            fixed_gps = fix_gps_coordinates(original_gps)
            if fixed_gps != original_gps:
                df_fixed.at[idx, 'GPS Coordinates'] = fixed_gps
                if fixed_gps is None:
                    fixes_applied['gps_fixes'] += 1
        
        # Fix County
        if 'County' in df_fixed.columns:
            original_county = row['County']
            fixed_county = normalize_county(original_county)
            if fixed_county != str(original_county):
                df_fixed.at[idx, 'County'] = fixed_county
                fixes_applied['county_fixes'] += 1
    
    # Print summary
    print("\nFixes applied:")
    print(f"  Type fixes: {fixes_applied['type_fixes']}")
    print(f"  Trail Role fixes: {fixes_applied['trail_role_fixes']}")
    print(f"  GPS coordinate fixes: {fixes_applied['gps_fixes']}")
    print(f"  County normalization: {fixes_applied['county_fixes']}")
    
    return df_fixed

if __name__ == "__main__":
    file_path = "Montgomery cursor.xlsx"
    
    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    df_fixed = fix_spreadsheet(file_path)
    
    # Save fixed version
    output_path = "Montgomery cursor_fixed.xlsx"
    df_fixed.to_excel(output_path, index=False)
    print(f"\nFixed spreadsheet saved to: {output_path}")
    print("\nNext steps:")
    print("  1. Review the fixed spreadsheet")
    print("  2. For web verification of addresses, ownership, and URLs,")
    print("     use targeted web searches for specific rows")
    print("  3. The fixed spreadsheet addresses common data quality issues")
