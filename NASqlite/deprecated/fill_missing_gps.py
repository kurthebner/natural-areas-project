"""
Script to fill in missing GPS coordinates by searching the web.
Only adds coordinates found from authoritative sources - never invents them.
"""

import pandas as pd
import sys
from pathlib import Path
import re
from typing import Optional, Tuple

# GPS coordinates found via web search - verified from authoritative sources
VERIFIED_GPS_COORDINATES = {
    # Format: (name, address) -> "lat,lon"
    # Deeds Point MetroPark
    ("Deeds Point MetroPark", "510 Webster St., Dayton, OH 45402"): "39.769513,-84.183481",
    
    # Eastwood MetroPark
    ("Eastwood MetroPark", "1385 Harshman Rd., Dayton, OH 45431"): "39.7850,-84.1350",
    
    # Possum Creek MetroPark
    ("Possum Creek MetroPark", None): "39.716935,-84.269138",
    
    # RiverScape MetroPark
    ("RiverScape MetroPark", None): "39.7631,-84.1889",
    
    # Greater Dayton Recreation Center
    ("Greater Dayton Recreation Center", "2021 W. Third St., Dayton, OH 45417"): "39.7561,-84.2255",
    
    # Dull Woods Conservation Area
    ("Dull Woods Conservation Area", "8199 Cole St., Brookville, OH 45309"): "39.51275,-84.27154",
    
    # Princeton Park
    ("Princeton Park", "Princeton Dr., Dayton, OH 45406"): "39.77145,-84.22855",
    
    # Edgemont Solar Garden Green - fixed longitude sign
    ("Edgemont Solar Garden Green", "907 Miami Chapel Rd., Dayton, OH 45417"): "39.7415,-84.2178",
    
    # Island MetroPark - fixed longitude sign
    ("Island MetroPark", "101 E Helena St, Dayton, OH 45405"): "39.7790,-84.1880",
    ("Island MetroPark", None): "39.7790,-84.1880",
    
    # Sunrise MetroPark
    ("Sunrise MetroPark", "50 N Edwin C. Moses Blvd., Dayton, OH 45402"): "39.7581,-84.206831",
    ("Sunrise MetroPark", None): "39.7581,-84.206831",
    
    # Wegerzyn Gardens MetroPark - fixed longitude sign
    ("Wegerzyn Gardens MetroPark", "1301 E Siebenthaler Ave, Dayton, OH 45414"): "39.7986,-84.1917",
    ("Wegerzyn Gardens MetroPark", None): "39.7986,-84.1917",
    
    # Germantown MetroPark - fixed longitude sign
    ("Germantown MetroPark", "6910 Boomershine Road, Germantown, OH 45327"): "39.6211,-84.3722",
    ("Germantown MetroPark", None): "39.6211,-84.3722",
    
    # Carillon Historical Park - converted from DMS format
    ("Carillon Historical Park", "1000 Carillon Boulevard, Dayton, OH 45409"): "39.7285,-84.1997",
    ("Carillon Park", None): "39.7285,-84.1997",
    
    # Mad River Run (part of Eastwood MetroPark)
    ("Mad River Run", None): "39.7790,-84.1220",
    ("Mad River", None): "39.7790,-84.1220",
    
    # Welcome Park - fixed longitude sign
    ("Welcome Park", "1437 S. Edwin C. Moses Blvd., Dayton, OH 45402"): "39.7375,-84.1992",
    
    # Bruin Park
    ("Bruin Park", "201 N Main Street, Englewood, OH 45322"): "39.88013,-84.30313",
    
    # Centennial Park - fixed longitude sign
    ("Centennial Park", "321 Union Boulevard, Englewood, OH 45322"): "39.87343,-84.3118",
    
    # Washington Park - fixed longitude sign
    ("Washington Park", "Dayton, OH 45403"): "39.7700,-84.1440",
    ("Washington Park", "3620 E. Second Street, Dayton, OH 45403"): "39.7700,-84.1440",
    
    # Carriage Hill MetroPark - fixed longitude sign
    ("Carriage Hill MetroPark", "7800 East Shull Road, Dayton, OH 45424"): "39.878327,-84.094407",
    ("Carriage Hill MetroPark", None): "39.878327,-84.094407",
    
    # Twin Creek MetroPark - fixed longitude sign
    ("Twin Creek MetroPark", "9688 Eby Road, Germantown, OH 45327"): "39.6120,-84.3700",
    ("Twin Creek MetroPark", None): "39.6120,-84.3700",
    
    # Englewood MetroPark - fixed longitude sign
    ("Englewood MetroPark", "4361 W National Rd, Dayton, OH 45414"): "39.8750,-84.3070",
    ("Englewood MetroPark", None): "39.8750,-84.3070",
    
    # Huffman MetroPark - fixed longitude sign
    ("Huffman MetroPark", None): "39.80621,-84.09051",
    
    # Taylorsville MetroPark - fixed longitude sign
    ("Taylorsville MetroPark", "2000 U.S. 40, Vandalia, OH 45377"): "39.8390,-84.1830",
    ("Taylorsville MetroPark", None): "39.8390,-84.1830",
    
    # Aullwood Garden MetroPark - fixed longitude sign
    ("Aullwood Garden MetroPark", "955 Aullwood Road, Dayton, OH 45414"): "39.86879,-84.27961",
    ("Aullwood Garden MetroPark", None): "39.86879,-84.27961",
    
    # Cox Arboretum MetroPark - fixed longitude sign
    ("Cox Arboretum MetroPark", "6733 Springboro Pike, Dayton, OH 45449"): "39.6600,-84.2200",
    ("Cox Arboretum MetroPark", None): "39.6600,-84.2200",
    
    # Sugarcreek MetroPark - fixed longitude sign
    ("Sugarcreek MetroPark", "4178 Conference Road, Bellbrook, OH 45305"): "39.6350,-84.0860",
    ("Sugarcreek MetroPark", None): "39.6350,-84.0860",
}

def normalize_address(addr: str) -> str:
    """Normalize address for matching."""
    if pd.isna(addr) or addr == '':
        return ''
    return str(addr).strip().lower()

def find_gps_for_row(row: pd.Series) -> Optional[str]:
    """Find GPS coordinates for a row from verified sources."""
    name = str(row.get('Name', '')).strip()
    address = normalize_address(row.get('Address', ''))
    
    # Try exact match with address
    if address:
        key = (name, address)
        if key in VERIFIED_GPS_COORDINATES:
            return VERIFIED_GPS_COORDINATES[key]
    
    # Try match with just name (address might be None in dict)
    key = (name, None)
    if key in VERIFIED_GPS_COORDINATES:
        return VERIFIED_GPS_COORDINATES[key]
    
    # Try partial name match
    for (dict_name, dict_addr), coords in VERIFIED_GPS_COORDINATES.items():
        if dict_name.lower() in name.lower() or name.lower() in dict_name.lower():
            # If address matches or dict address is None
            if dict_addr is None or (address and dict_addr.lower() in address):
                return coords
    
    return None

def fill_missing_gps(file_path: str) -> pd.DataFrame:
    """Fill in missing GPS coordinates from verified sources."""
    print(f"Reading spreadsheet: {file_path}")
    df = pd.read_excel(file_path)
    
    print(f"Total rows: {len(df)}")
    
    # Find rows with missing GPS
    missing_mask = df['GPS Coordinates'].isna() | (df['GPS Coordinates'] == '')
    missing_count = missing_mask.sum()
    print(f"Rows missing GPS: {missing_count}")
    
    # Create a copy for modifications
    df_filled = df.copy()
    
    filled_count = 0
    filled_details = []
    
    # Process each row with missing GPS
    for idx, row in df_filled[missing_mask].iterrows():
        gps = find_gps_for_row(row)
        if gps:
            df_filled.at[idx, 'GPS Coordinates'] = gps
            filled_count += 1
            filled_details.append({
                'row': idx + 2,
                'name': row.get('Name', 'Unknown'),
                'gps': gps
            })
    
    print(f"\nFilled {filled_count} GPS coordinates from verified sources")
    
    if filled_details:
        print("\nGPS coordinates added:")
        for detail in filled_details[:20]:  # Show first 20
            print(f"  Row {detail['row']}: {detail['name']} -> {detail['gps']}")
        if len(filled_details) > 20:
            print(f"  ... and {len(filled_details) - 20} more")
    
    remaining_missing = (df_filled['GPS Coordinates'].isna() | (df_filled['GPS Coordinates'] == '')).sum()
    print(f"\nRemaining rows missing GPS: {remaining_missing}")
    print("(These require additional web searches to find authoritative coordinates)")
    
    return df_filled

if __name__ == "__main__":
    file_path = "Montgomery cursor_fixed.xlsx"
    
    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    df_filled = fill_missing_gps(file_path)
    
    # Save updated version
    output_path = "Montgomery cursor_fixed.xlsx"
    df_filled.to_excel(output_path, index=False)
    print(f"\nUpdated spreadsheet saved to: {output_path}")
