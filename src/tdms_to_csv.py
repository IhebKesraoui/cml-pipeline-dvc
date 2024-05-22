from pathlib import Path

from nptdms import TdmsFile

input_folder = Path('/home/nanoz-admin/Desktop/projects/test remote mini project/data/train')

output_folder = '/home/nanoz-admin/Desktop/projects/last_dvc/out'

tdms_rglob = input_folder.rglob('*.tdms')
list_rglob = list(tdms_rglob)
list_rglob.sort(key=lambda i: int(i.name.split('_')[-1].split('.')[0]))

for tdms_file in list_rglob:
    
    # Read data as dataframe
    tdms_df = TdmsFile.read(tdms_file).as_dataframe()

    # Save extracted data as csv file
    csv_file_path = Path(output_folder, tdms_file.stem+'.csv')
    tdms_df.to_csv(csv_file_path)

print('Finidzsh\n')
