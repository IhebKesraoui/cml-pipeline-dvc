from pathlib import Path
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from nptdms import TdmsFile
from google.oauth2 import service_account
import os

# Get service account key JSON from environment variable
service_account_key = os.environ.get('GDRIVE_CREDENTIALS_DATA')

# Authenticate using service account credentials
credentials = service_account.Credentials.from_service_account_info(
    service_account_key,
    scopes=['https://www.googleapis.com/auth/drive']
)

drive = GoogleDrive(credentials)

# Define input and output folders
input_folder = Path('./data')
output_folder = './out'

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
    csv_file_path = Path(output_folder, tdms_file.stem+'.csv')
    tdms_df.to_csv(csv_file_path)

    # Upload CSV file to Google Drive in the specified folder
    csv_file = drive.CreateFile({'title': tdms_file.stem+'.csv',
                                 'parents': [{'id': destination_folder_id}]})
    csv_file.SetContentFile(str(csv_file_path))
    csv_file.Upload()

print('Finished')
