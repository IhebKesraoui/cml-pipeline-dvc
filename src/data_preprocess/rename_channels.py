import pandas as pd
import pickle
from pathlib import Path
import yaml

def rename_channels(df, rename_map_path):
    """
    Renames channels in the DataFrame based on a mapping file.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame.
    rename_map_path (str): Path to the YAML file containing channel rename mappings.
    
    Returns:
    pd.DataFrame: DataFrame with renamed channels.
    """
    with open(rename_map_path, 'r') as file:
        rename_map = yaml.safe_load(file)
    
    # Ensure the rename_map is not empty
    if not rename_map:
        print("No rename mappings found. DataFrame returned unchanged.")
        return df
    
    # Use a copy of the DataFrame to avoid modifying the original DataFrame
    df_copy = df.copy()
    
    # Rename columns using the rename_map
    df_copy.rename(columns=rename_map, inplace=True)
    return df_copy

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Rename channels in DataFrames and save as pickles")
    parser.add_argument("input_dir", type=str, help="./cml-pipeline-dvc/src/out")
    parser.add_argument("rename_map", type=str, help="./cml-pipeline-dvc/intermidiate_file/rename_map.yaml")
    parser.add_argument("output_dir", type=str, help="./cml-pipeline-dvc/src/out")

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    rename_map = Path(args.rename_map)
    output_dir = Path(args.output_dir)

    # Ensure the output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process each pickle file in the input directory
    for input_file_path in input_dir.glob("*.pkl"):
        with open(input_file_path, 'rb') as f:
            df = pickle.load(f)
        df_renamed = rename_channels(df, rename_map)
        output_file_path = output_dir / input_file_path.name
        with open(output_file_path, 'wb') as f:
            pickle.dump(df_renamed, f)
