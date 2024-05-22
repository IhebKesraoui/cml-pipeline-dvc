from pathlib import Path

from nptdms import TdmsFile

input_folder = Path('./data')

output_folder = './out'

tdms_rglob = input_folder.rglob('*.tdms')
list_rglob = list(tdms_rglob)
list_rglob.sort(key=lambda i: int(i.name.split('_')[-1].split('.')[0]))
print (input_folder)
for tdms_file in list_rglob:
    tdms_df = TdmsFile.read(tdms_file).as_dataframe()

    csv_file_path = Path(output_folder, tdms_file.stem+'.csv')
    tdms_df.to_csv(csv_file_path)

print('Finidzccccsh\n')
