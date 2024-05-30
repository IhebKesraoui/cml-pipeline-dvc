import os
import pandas as pd
from nptdms import TdmsFile
import pickle
import argparse
import unittest

def tdms_to_df(tdms_file_path):
    """
    Converts a TDMS file to a pandas DataFrame and returns the DataFrame along with full channel paths.
    
    Parameters:
    tdms_file_path (str): Path to the TDMS file.
    
    Returns:
    tuple: (pd.DataFrame, list) DataFrame containing the data from the TDMS file and a list of full channel paths.
    """
    if not tdms_file_path.endswith(".tdms"):
        raise ValueError(f"{tdms_file_path} n'est pas un fichier TDMS")
    
    if os.path.getsize(tdms_file_path) == 0:
        raise ValueError(f"{tdms_file_path} est vide")
    
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

def main(tdms_dir, output_dir):
    # Process each TDMS file in the directory
    for file_name in os.listdir(tdms_dir):
        tdms_file_path = os.path.join(tdms_dir, file_name)
        if file_name.endswith(".tdms"):
            try:
                # Process TDMS file
                df, full_channel_paths = tdms_to_df(tdms_file_path)
                # Save the result as a pickle file
                output_file_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + ".pkl")
                with open(output_file_path, 'wb') as f:
                    pickle.dump(df, f)
            except ValueError as e:
                print(e)
        else:
            print(f"{file_name} n'est pas un fichier TDMS")
            raise ValueError(f"{file_name} n'est pas un fichier TDMS")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert TDMS files to DataFrames and save as pickles")
    parser.add_argument("tdms_dir", type=str, help="Directory containing TDMS files")
    parser.add_argument("output_dir", type=str, help="Directory to save output pickle files")
    parser.add_argument("--run-tests", action="store_true", help="Run tests on TDMS files")

    args = parser.parse_args()

    if args.run_tests:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        main(args.tdms_dir, args.output_dir)
