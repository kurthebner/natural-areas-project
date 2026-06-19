import pandas as pd
import os

# Load only the "Ohio" sheet
df = pd.read_excel("Natural Areas.xlsx", sheet_name="Ohio")

# Normalize county column
df['County'] = df['County'].fillna('').astype(str).str.strip()

# Create output folder
output_dir = "County_Spreadsheets"
os.makedirs(output_dir, exist_ok=True)

# Initialize containers
single_county = {}
multi_county = []
no_county = []

# Process each row
for _, row in df.iterrows():
    counties = [c.strip() for c in row['County'].split(',') if c.strip()]
    
    if not counties:
        no_county.append(row)
    elif len(counties) > 1:
        multi_county.append(row)
    else:
        county = counties[0]
        if county not in single_county:
            single_county[county] = []
        single_county[county].append(row)

# Write single-county spreadsheets
for county, rows in single_county.items():
    county_df = pd.DataFrame(rows)
# Sanitize county name for filename
    safe_county = "".join(c for c in county if c not in r'\/:*?"<>|')
    county_df.to_excel(os.path.join(output_dir, f"{safe_county}.xlsx"), index=False)

# Write multi-county spreadsheet
multi_df = pd.DataFrame(multi_county)
multi_df.to_excel(os.path.join(output_dir, "MULTI_COUNTY.xlsx"), index=False)

# Write no-county spreadsheet
no_df = pd.DataFrame(no_county)
no_df.to_excel(os.path.join(output_dir, "NO_COUNTY.xlsx"), index=False)