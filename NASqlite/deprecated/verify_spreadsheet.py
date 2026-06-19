"""
Verification script for Natural Areas spreadsheet.
Follows the batch-processing protocol from natural-areas-project.md
"""

import pandas as pd
import sys
from pathlib import Path
import re
from typing import Dict, List, Optional, Tuple

def generate_plus_code(lat: float, lon: float) -> str:
    """
    Generate a Plus Code from GPS coordinates.
    This is a simplified version - for production, use the openlocationcode library.
    """
    # For now, we'll leave this as a placeholder that needs proper implementation
    # The actual Plus Code algorithm is complex
    return ""  # Will be filled in if needed

def verify_gps_coordinates(gps_str: str) -> Tuple[Optional[str], bool]:
    """
    Verify GPS coordinates.
    Returns: (normalized_coordinate, is_placeholder)
    """
    if pd.isna(gps_str) or gps_str == '':
        return None, False
    
    gps_str = str(gps_str).strip()
    
    # Check for placeholders like 39.0,-84.0
    if re.match(r'^-?\d+\.0+,-?\d+\.0+$', gps_str):
        return None, True  # Placeholder, remove it
    
    # Normalize format: should be "lat,lon" with no space after comma
    gps_str = gps_str.replace(' ', '')
    
    # Validate format
    try:
        parts = gps_str.split(',')
        if len(parts) == 2:
            lat = float(parts[0])
            lon = float(parts[1])
            # Check if coordinates are reasonable (not placeholders)
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                return f"{lat},{lon}", False
    except (ValueError, IndexError):
        pass
    
    return gps_str, False  # Keep as-is if can't parse

def normalize_type(type_str: str) -> str:
    """
    Validate Type against controlled vocabulary.
    Returns the type if valid, otherwise returns as-is (will flag in report).
    """
    if pd.isna(type_str) or type_str == '':
        return ''
    
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
    
    type_str = str(type_str).strip()
    if type_str in valid_types:
        return type_str
    
    return type_str  # Return as-is, will be flagged

def normalize_trail_role(role_str: str) -> str:
    """Normalize Trail Role field."""
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
    if role_lower in ['no', 'n', 'false', '0']:
        return 'None'
    if role_lower in ['yes', 'y', 'true', '1']:
        return ''  # Invalid - needs specific role
    
    if role_str in valid_roles:
        return role_str
    
    return role_str  # Return as-is

def normalize_county(county_str: str) -> str:
    """Normalize County field - alphabetical, semicolon-delimited, no 'County' suffix."""
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

def verify_spreadsheet(file_path: str) -> pd.DataFrame:
    """
    Verify and normalize spreadsheet data according to batch-processing protocol.
    """
    print(f"Reading spreadsheet: {file_path}")
    df = pd.read_excel(file_path)
    
    print(f"Found {len(df)} rows")
    
    # Create a copy for modifications
    df_verified = df.copy()
    
    # Track issues
    issues = []
    
    # Process each row
    for idx, row in df_verified.iterrows():
        row_issues = []
        
        # 1. Verify GPS Coordinates
        if 'GPS Coordinates' in df_verified.columns:
            gps = row['GPS Coordinates']
            normalized_gps, is_placeholder = verify_gps_coordinates(gps)
            
            if is_placeholder:
                df_verified.at[idx, 'GPS Coordinates'] = ''
                row_issues.append(f"Removed placeholder GPS coordinates")
            elif normalized_gps and normalized_gps != str(gps):
                df_verified.at[idx, 'GPS Coordinates'] = normalized_gps
                row_issues.append(f"Normalized GPS coordinates")
        
        # 2. Generate Plus Codes for valid GPS
        if 'Plus Code' in df_verified.columns and 'GPS Coordinates' in df_verified.columns:
            gps = df_verified.at[idx, 'GPS Coordinates']
            if pd.notna(gps) and gps != '':
                # For now, leave Plus Code generation for manual processing
                # or use openlocationcode library
                pass
        
        # 3. Validate Type
        if 'Type' in df_verified.columns:
            original_type = row['Type']
            normalized_type = normalize_type(original_type)
            if normalized_type != str(original_type):
                # Type might be invalid - flag it
                pass  # Keep original for now, will be checked
        
        # 4. Normalize Trail Role
        if 'Trail Role' in df_verified.columns:
            original_role = row['Trail Role']
            normalized_role = normalize_trail_role(original_role)
            if normalized_role != str(original_role):
                df_verified.at[idx, 'Trail Role'] = normalized_role
                row_issues.append(f"Normalized Trail Role: '{original_role}' -> '{normalized_role}'")
        
        # 5. Normalize County
        if 'County' in df_verified.columns:
            original_county = row['County']
            normalized_county = normalize_county(original_county)
            if normalized_county != str(original_county):
                df_verified.at[idx, 'County'] = normalized_county
                row_issues.append(f"Normalized County: '{original_county}' -> '{normalized_county}'")
        
        if row_issues:
            issues.append({
                'row': idx + 2,  # +2 for header and 0-index
                'name': row.get('Name', 'Unknown'),
                'issues': row_issues
            })
    
    # Print summary
    print(f"\nVerification complete!")
    print(f"Total issues found: {len(issues)}")
    
    if issues:
        print("\nIssues by row:")
        for issue in issues[:20]:  # Show first 20
            print(f"  Row {issue['row']} ({issue['name']}):")
            for i in issue['issues']:
                print(f"    - {i}")
        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more issues")
    
    return df_verified

if __name__ == "__main__":
    file_path = "Montgomery cursor.xlsx"
    
    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    df_verified = verify_spreadsheet(file_path)
    
    # Save verified version
    output_path = "Montgomery cursor_verified.xlsx"
    df_verified.to_excel(output_path, index=False)
    print(f"\nVerified spreadsheet saved to: {output_path}")
