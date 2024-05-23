import os
import pandas as pd
from nptdms import TdmsFile
import pickle

def tdms_to_df(tdms_file_path):
    """
    Converts a TDMS file to a pandas DataFrame.
    
    Parameters:
    tdms_file_path (str): Path to the TDMS file.
    
    Returns:
    pd.DataFrame: DataFrame containing the data from the TDMS file.
    """
    tdms_file = TdmsFile.read(tdms_file_path)
    data = {}
    for group in tdms_file.groups():
        for channel in group.channels():
            data[channel.name] = channel[:]
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert TDMS files to DataFrames and save as pickles")
    parser.add_argument("tdms_dir", type=str, help="./cml-pipeline-dvc/data")
    parser.add_argument("output_dir", type=str, help="./cml-pipeline-dvc/out")

    args = parser.parse_args()

    # Process each TDMS file in the directory
    for file_name in os.listdir(args.tdms_dir):
        if file_name.endswith(".tdms"):
            tdms_file_path = os.path.join(args.tdms_dir, file_name)
            # Process TDMS file
            df = tdms_to_df(tdms_file_path)
            # Save the result as a pickle file
            output_file_path = os.path.join(args.output_dir, os.path.splitext(file_name)[0] + ".pkl")
            with open(output_file_path, 'wb') as f:
                pickle.dump(df, f)
