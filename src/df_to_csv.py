import os
import pandas as pd
import pickle

def convert_to_csv(input_dir, output_dir):
    """
    Converts DataFrame pickle files from input_dir to CSV files in output_dir.

    Parameters:
    input_dir (str): Path to the directory containing input DataFrame pickle files.
    output_dir (str): Path to the directory to save the output CSV files.
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Loop through each pickle file in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pkl"):
            input_file_path = os.path.join(input_dir, file_name)
            output_file_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + ".csv")

            # Read DataFrame from pickle file
            df = pd.read_pickle(input_file_path)

            # Save the DataFrame as CSV
            df.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert DataFrame pickle files to CSV files")
    parser.add_argument("input_dir", type=str, help="./cml-pipeline-dvc/out")
    parser.add_argument("output_dir", type=str, help="./csv_out")

    args = parser.parse_args()
    
    # Call convert_to_csv function
    convert_to_csv(args.input_dir, args.output_dir)
