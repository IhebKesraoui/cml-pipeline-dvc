from pathlib import Path
from nptdms import TdmsFile
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io
import os
import json

# Get service account key JSON from environment variable
service_account_info = json.loads(os.environ['GDRIVE_CREDENTIALS_DATA'])

# Authenticate using service account credentials
credentials = service_account.Credentials.from_service_account_info(
    service_account_info,
    scopes=['https://www.googleapis.com/auth/drive']
)

# Build the Google Drive service
drive_service = build('drive', 'v3', credentials=credentials)

# Define input folder
input_folder = Path('./data')

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

    # Convert to CSV and create in-memory file
    csv_buffer = io.StringIO()
    tdms_df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)  # Move to the beginning of the StringIO buffer

    # Upload CSV file to Google Drive in the specified folder
    file_metadata = {
        'name': f'{tdms_file.stem}.csv',
        'parents': [destination_folder_id]
    }
    media = MediaIoBaseUpload(csv_buffer, mimetype='text/csv')
    drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

print('Finished')
