import pandas as pd
import json
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(APP_ROOT, '', 'user.json')
USER_XLSX = os.path.join(APP_ROOT, '', 'user.xlsx')
################################
# User data
################################
# Load the JSON data
with open(USER_FILE) as f:
    data = json.load(f)
    
# Load the Excel data into a DataFrame
df_excel = pd.read_excel(USER_XLSX)

# Convert the JSON data to a DataFrame
df_json = pd.json_normalize(data, 'users')

# Merge the Excel and JSON data
df_merged = pd.concat([df_excel, df_json])

# Save the merged data to the Excel file
df_merged.to_excel(USER_XLSX, index=False)

################################
# Firm data
################################

FIRM_FILE = os.path.join(APP_ROOT, '', 'firm.json')
FIRM_XLSX = os.path.join(APP_ROOT, '', 'firms.xlsx')

with open(FIRM_FILE) as f:
    data = json.load(f)
    
# Load the Excel data into a DataFrame
df_excel = pd.read_excel(FIRM_XLSX)

# Convert the JSON data to a DataFrame
df_json = pd.json_normalize(data, 'firms')

# Merge the Excel and JSON data
df_merged = pd.concat([df_excel, df_json])

# Save the merged data to the Excel file
df_merged.to_excel(FIRM_XLSX, index=False)