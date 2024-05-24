# rename_channels.py

import os
import pandas as pd
import pickle

def rename_channels(df, rename_map_path):
    """
    Renames channels in the DataFrame based on a mapping file.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame.
    rename_map_path (str): Path to the text file containing channel rename mappings.
    
    Returns:
    pd.DataFrame: DataFrame with renamed channels.
    """
    rename_map = pd.read_csv(rename_map_path, sep=' ', header=None, names=['existing_name', 'new_name'])
    rename_dict = dict(zip(rename_map['existing_name'], rename_map['new_name']))
    df.rename(columns=rename_dict, inplace=True)
    return df

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Rename channels in DataFrames and save as pickles")
    parser.add_argument("input_dir", type=str, help="./cml-pipeline-dvc/out")
    parser.add_argument("rename_map", type=str, help="./cml-pipeline-dvc/rename_map.txt")
    parser.add_argument("output_dir", type=str, help="./cml-pipeline-dvc/out")

    args = parser.parse_args()

    for file_name in os.listdir(args.input_dir):
        if file_name.endswith(".pkl"):
            input_file_path = os.path.join(args.input_dir, file_name)
            with open(input_file_path, 'rb') as f:
                df = pickle.load(f)
            df = rename_channels(df, args.rename_map)
            output_file_path = os.path.join(args.output_dir, file_name)
            with open(output_file_path, 'wb') as f:
                pickle.dump(df, f)
