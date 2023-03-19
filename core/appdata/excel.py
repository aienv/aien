import pandas as pd
import json
import os
import glob

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
USERSS_FILE = os.path.join(APP_ROOT, '', 'user.json')
FIRM_FILE = os.path.join(APP_ROOT, '', 'firm.json')

def strip_appdata(path):
    return path.replace('\\appdata', '')

APP_ROOT = strip_appdata(APP_ROOT)

################################
# Firm data
################################

FIRM_XLSX = os.path.join(APP_ROOT, 'static', 'firms.xlsx')

def fhandle():
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
    
################################
# User data
################################


USERSS_XLSX = os.path.join(APP_ROOT, 'static', 'users.xlsx')


def uhandle():
    with open(USERSS_FILE) as f:
        data = json.load(f)
         
    # Load the Excel data into a DataFrame
    df_excel = pd.read_excel(USERSS_XLSX )

    # Convert the JSON data to a DataFrame
    df_json = pd.json_normalize(data, 'users')

    # Merge the Excel and JSON data
    df_merged = pd.concat([df_excel, df_json])

    # Save the merged data to the Excel file
    # Delete the old file if it exists
    if os.path.isfile(USERSS_XLSX):
        os.remove(USERSS_XLSX)

    # Save the merged data to a new Excel file with the same name
    df_merged.to_excel(USERSS_XLSX, index=False)
