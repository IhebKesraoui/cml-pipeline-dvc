from pathlib import Path
from nptdms import TdmsFile
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import json

# Authenticate using service account credentials
service_account_file = '/home/nanoz-admin/Documents/trypipeline/cml-pipeline-dvc/.dvc/default.json'
credentials = service_account.Credentials.from_service_account_file(
    service_account_file,
    scopes=['https://www.googleapis.com/auth/drive']
)

# Build the Google Drive service
drive_service = build('drive', 'v3', credentials=credentials)

# Define input and output folders
input_folder = Path('./data')
output_folder = Path('./out')

# Create output folder if it doesn't exist
output_folder.mkdir(parents=True, exist_ok=True)

# Get list of tdms files
tdms_rglob = input_folder.rglob('*.tdms')
list_rglob = list(tdms_rglob)
list_rglob.sort(key=lambda i: int(i.name.split('_')[-1].split('.')[0]))

# Specify the destination folder ID in Google Drive
destination_folder_id = '19opW14aCDPxnvOaYmLrP1T8E2ogYA_rL'

# Iterate through each tdms file
for tdms_file in list_rglob:
    # Read tdms file
    tdms_df = TdmsFile.read(tdms_file).as_dataframe()

    # Convert to CSV and save to local disk
    csv_file_path = output_folder / f'{tdms_file.stem}.csv'
    tdms_df.to_csv(csv_file_path)

    # Upload CSV file to Google Drive in the specified folder
    file_metadata = {
        'name': f'{tdms_file.stem}.csv',
        'parents': [destination_folder_id]
    }
    media = MediaFileUpload(csv_file_path, mimetype='text/csv')
    drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

print('Finished')
