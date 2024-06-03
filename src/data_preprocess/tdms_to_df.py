import os
import pandas as pd
from nptdms import TdmsFile
import pickle

def tdms_to_df(tdms_file_path):
    """
    Converts a TDMS file to a pandas DataFrame and returns the DataFrame along with full channel paths.
    
    Parameters:
    tdms_file_path (str): Path to the TDMS file.
    
    Returns:
    tuple: (pd.DataFrame, list) DataFrame containing the data from the TDMS file and a list of full channel paths.
    """
    tdms_file = TdmsFile.read(tdms_file_path)
    data = {}
    full_channel_paths = []
    for group in tdms_file.groups():
        for channel in group.channels():
            full_channel_path = f"{group.name}/{channel.name}"
            full_channel_paths.append(full_channel_path)
            data[full_channel_path] = channel[:]
    df = pd.DataFrame(data)
    return df, full_channel_paths

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert TDMS files to DataFrames and save as pickles")
    parser.add_argument("tdms_dir", type=str, help="./cml-pipeline-dvc/data")
    parser.add_argument("output_dir", type=str, help="./cml-pipeline-dvc/out")

    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    # Process each TDMS file in the directory
    for file_name in os.listdir(args.tdms_dir):
        if file_name.endswith(".tdms"):
            tdms_file_path = os.path.join(args.tdms_dir, file_name)
            # Process TDMS file
            df, full_channel_paths = tdms_to_df(tdms_file_path)
            # Print full channel paths
            
            # Save the result as a pickle file
            output_file_path = os.path.join(args.output_dir, os.path.splitext(file_name)[0] + ".pkl")
            
            with open(output_file_path, 'wb') as f:
                pickle.dump(df, f)
