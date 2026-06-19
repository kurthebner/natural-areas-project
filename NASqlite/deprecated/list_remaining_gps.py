import pandas as pd

df = pd.read_excel('Montgomery cursor_fixed.xlsx')
missing = df[df['GPS Coordinates'].isna() | (df['GPS Coordinates'] == '')]
print(f'Remaining parks missing GPS: {len(missing)}')
print('\nNext 25 parks with addresses:')
print('=' * 100)

count = 0
for idx, row in missing.iterrows():
    address = row.get('Address', '')
    if pd.notna(address) and str(address).strip() != '' and str(address).lower() != 'nan':
        print(f"\n{row['Name']}")
        print(f"  Address: {address}")
        print(f"  Location: {row.get('Location', 'N/A')}")
        count += 1
        if count >= 25:
            break
