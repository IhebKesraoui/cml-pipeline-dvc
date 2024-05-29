import pickle
from pathlib import Path  # Importing Path from pathlib
import os  # Imported os module for the existing os.path operations

def drop_columns(df, drop_file_path):
    """
    Drops columns specified in a text file from the DataFrame.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame.
    drop_file_path (str): Path to the text file containing column names to drop.
    
    Returns:
    pd.DataFrame: DataFrame with specified columns dropped.
    """
    # Using Path object for drop_file_path
    drop_file_path = Path(drop_file_path)

    # Check if the drop file exists and is not empty
    if drop_file_path.exists() and drop_file_path.stat().st_size > 0:
        with open(drop_file_path, 'r') as f:
            columns_to_drop = f.read().splitlines()
        df = df.drop(columns=columns_to_drop, errors='ignore')
    return df

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Drop specified columns from DataFrames and save as pickles")
    parser.add_argument("input_dir", type=str, help="./cml-pipeline-dvc/out")
    parser.add_argument("drop_file", type=str, help="./cml-pipeline-dvc/drop_file.txt")
    parser.add_argument("output_dir", type=str, help="./cml-pipeline-dvc/out")

    args = parser.parse_args()
    
    # Convert input_dir, drop_file, and output_dir to Path objects
    input_dir = Path(args.input_dir)
    drop_file = Path(args.drop_file)
    output_dir = Path(args.output_dir)

    # Ensure the output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process each input DataFrame in the directory
    for input_file_path in input_dir.glob("*.pkl"):
        # Load DataFrame from pickle file
        with open(input_file_path, 'rb') as f:
            df = pickle.load(f)
        # Drop specified columns
        df = drop_columns(df, drop_file)
        # Save the result as a pickle file
        output_file_path = output_dir / input_file_path.name
        with open(output_file_path, 'wb') as f:
            pickle.dump(df, f)
