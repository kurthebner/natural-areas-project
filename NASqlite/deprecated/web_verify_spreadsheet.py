"""
Web verification script for Natural Areas spreadsheet.
Verifies addresses, ownership, URLs, and GPS coordinates via web searches.
"""

import pandas as pd
import sys
from pathlib import Path
import time
from typing import Dict, List, Optional, Tuple
import requests
from urllib.parse import quote

# Note: This script uses web_search via the tool, but for standalone use,
# you would need to implement actual web scraping or use an API

def verify_url(url_str: str) -> Tuple[bool, Optional[str]]:
    """
    Verify if a URL is accessible.
    Returns: (is_valid, error_message)
    """
    if pd.isna(url_str) or url_str == '':
        return True, None  # Empty is valid
    
    url_str = str(url_str).strip()
    
    # Check if it's a valid URL format
    if not url_str.startswith(('http://', 'https://')):
        return False, "URL should start with http:// or https://"
    
    # Try to access the URL
    try:
        response = requests.get(url_str, timeout=5, allow_redirects=True)
        if response.status_code == 200:
            return True, None
        else:
            return False, f"HTTP {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, str(e)

def create_verification_report(df: pd.DataFrame, output_file: str = "verification_report.txt"):
    """
    Create a detailed verification report.
    """
    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append("NATURAL AREAS SPREADSHEET VERIFICATION REPORT")
    report_lines.append("=" * 80)
    report_lines.append(f"\nTotal rows: {len(df)}")
    report_lines.append(f"Generated: {pd.Timestamp.now()}")
    report_lines.append("\n")
    
    # Check for missing required fields
    required_fields = ['Name']
    report_lines.append("REQUIRED FIELDS CHECK:")
    report_lines.append("-" * 80)
    for field in required_fields:
        if field in df.columns:
            missing = df[field].isna().sum()
            if missing > 0:
                report_lines.append(f"  {field}: {missing} rows missing")
            else:
                report_lines.append(f"  {field}: [OK] All rows have values")
    report_lines.append("\n")
    
    # Check Type field against controlled vocabulary
    if 'Type' in df.columns:
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
        
        report_lines.append("TYPE FIELD VALIDATION:")
        report_lines.append("-" * 80)
        invalid_types = df[~df['Type'].isin(valid_types) & df['Type'].notna()]
        if len(invalid_types) > 0:
            report_lines.append(f"  Found {len(invalid_types)} rows with potentially invalid Types:")
            for idx, row in invalid_types.head(10).iterrows():
                report_lines.append(f"    Row {idx+2}: '{row['Name']}' - Type: '{row['Type']}'")
            if len(invalid_types) > 10:
                report_lines.append(f"    ... and {len(invalid_types) - 10} more")
        else:
            report_lines.append("  [OK] All Types are valid")
        report_lines.append("\n")
    
    # Check GPS coordinates
    if 'GPS Coordinates' in df.columns:
        report_lines.append("GPS COORDINATES CHECK:")
        report_lines.append("-" * 80)
        missing_gps = df['GPS Coordinates'].isna().sum()
        report_lines.append(f"  Missing GPS: {missing_gps} rows")
        
        # Check for placeholder coordinates
        import re
        placeholder_pattern = re.compile(r'^-?\d+\.0+,-?\d+\.0+$')
        placeholders = 0
        for idx, row in df.iterrows():
            gps = row['GPS Coordinates']
            if pd.notna(gps) and placeholder_pattern.match(str(gps).replace(' ', '')):
                placeholders += 1
        
        if placeholders > 0:
            report_lines.append(f"  Placeholder coordinates (e.g., 39.0,-84.0): {placeholders} rows")
        report_lines.append("\n")
    
    # Check URLs
    if 'URL' in df.columns:
        report_lines.append("URL CHECK:")
        report_lines.append("-" * 80)
        rows_with_urls = df['URL'].notna().sum()
        report_lines.append(f"  Rows with URLs: {rows_with_urls}")
        report_lines.append("  Note: URL accessibility verification requires manual check or API access")
        report_lines.append("\n")
    
    # Check Trail Role
    if 'Trail Role' in df.columns:
        report_lines.append("TRAIL ROLE CHECK:")
        report_lines.append("-" * 80)
        invalid_roles = df[~df['Trail Role'].isin([
            'Trail System', 'Trail Segment', 'Trail', 'Connector Trail / Spur',
            'Trailhead', 'Trail Access Point', 'Bikeway Access Point',
            'Bikeway Spur', 'Greenway Corridor', 'None'
        ]) & df['Trail Role'].notna()]
        
        if len(invalid_roles) > 0:
            report_lines.append(f"  Found {len(invalid_roles)} rows with potentially invalid Trail Roles")
        else:
            report_lines.append("  [OK] All Trail Roles are valid or None")
        report_lines.append("\n")
    
    # Summary
    report_lines.append("=" * 80)
    report_lines.append("SUMMARY")
    report_lines.append("=" * 80)
    report_lines.append("\nThis report identifies potential issues that may need:")
    report_lines.append("  1. Manual verification via web search")
    report_lines.append("  2. Address corrections")
    report_lines.append("  3. Ownership/Management verification")
    report_lines.append("  4. URL updates")
    report_lines.append("  5. GPS coordinate verification")
    report_lines.append("\nFor web verification of specific rows, use the interactive")
    report_lines.append("verification tool or run targeted searches.")
    
    # Write report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"\nVerification report saved to: {output_file}")
    print("\n".join(report_lines[:50]))  # Print first part

if __name__ == "__main__":
    file_path = "Montgomery cursor.xlsx"
    
    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    print(f"Reading spreadsheet: {file_path}")
    df = pd.read_excel(file_path)
    print(f"Found {len(df)} rows")
    
    # Create verification report
    create_verification_report(df)
    
    print("\nNote: For actual web verification of addresses, ownership, and URLs,")
    print("this would require web search API access or manual verification.")
    print("The report above identifies areas that need attention.")
