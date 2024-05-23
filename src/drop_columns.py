import pickle

import os  # Added import statement for os module
def drop_columns(df, drop_file_path):
    """
    Drops columns specified in a text file from the DataFrame.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame.
    drop_file_path (str): Path to the text file containing column names to drop.
    
    Returns:
    pd.DataFrame: DataFrame with specified columns dropped.
    """
    # Check if the drop file is not null
    if os.path.exists(drop_file_path) and os.path.getsize(drop_file_path) > 0:
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
    
    # Process each input DataFrame in the directory
    for file_name in os.listdir(args.input_dir):
        if file_name.endswith(".pkl"):
            input_file_path = os.path.join(args.input_dir, file_name)
            # Load DataFrame from pickle file
            with open(input_file_path, 'rb') as f:
                df = pickle.load(f)
            # Drop specified columns
            df = drop_columns(df, args.drop_file)
            # Save the result as a pickle file
            output_file_path = os.path.join(args.output_dir, file_name)
            with open(output_file_path, 'wb') as f:
                pickle.dump(df, f)
