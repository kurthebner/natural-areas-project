import pandas as pd

df = pd.read_excel('Montgomery cursor_fixed.xlsx')
parks_to_find = ['Englewood', 'Huffman', 'Aullwood', 'Cox', 'Sugarcreek']

print("Searching for parks:")
for park in parks_to_find:
    matches = df[df['Name'].str.contains(park, case=False, na=False)]
    if len(matches) > 0:
        for idx, row in matches.iterrows():
            gps = row.get('GPS Coordinates', '')
            status = 'HAS GPS' if pd.notna(gps) and gps != '' else 'MISSING GPS'
            print(f"  {row['Name']} - {status}")
