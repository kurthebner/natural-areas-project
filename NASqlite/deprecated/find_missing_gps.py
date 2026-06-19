"""
Script to find missing GPS coordinates and prepare for web search.
"""

import pandas as pd
from pathlib import Path

file_path = "Montgomery cursor_fixed.xlsx"
df = pd.read_excel(file_path)

missing_gps = df[df['GPS Coordinates'].isna() | (df['GPS Coordinates'] == '')]
print(f'Rows missing GPS: {len(missing_gps)}')
print('\nFirst 30 rows missing GPS:')
print('=' * 100)

for idx, row in missing_gps.head(30).iterrows():
    name = row.get('Name', 'N/A')
    address = row.get('Address', 'N/A')
    location = row.get('Location', 'N/A')
    county = row.get('County', 'N/A')
    print(f"\nRow {idx+2}: {name}")
    print(f"  Address: {address}")
    print(f"  Location: {location}")
    print(f"  County: {county}")
