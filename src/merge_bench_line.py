import os
import pandas as pd
import pickle

def merge_bench_line_dvc(input_dir, output_dir):
    """
    Merges specific columns in DataFrame pickle files from input_dir based on criteria and saves the merged DataFrames
    in output_dir.

    Parameters:
    input_dir (str): Path to the directory containing input DataFrame pickle files.
    output_dir (str): Path to the directory to save the output merged DataFrame pickle files.
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Loop through each pickle file in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pkl"):
            input_file_path = os.path.join(input_dir, file_name)
            output_file_path = os.path.join(output_dir, file_name)

            # Read DataFrame from pickle file
            df = pd.read_pickle(input_file_path)

            # Merge columns CO_A, CO_B, HCHO_A, HCHO_B, EtOH_A, EtOH_B based on criteria
            for prefix in ['CO', 'HCHO', 'EtOH']:
                col_A = f"{prefix}_A"
                col_B = f"{prefix}_B"
                if col_A in df.columns and col_B in df.columns:
                    if all(df[col_A] == df[col_B]):
                        # If values do not change in all rows, merge columns without averaging
                        df[f"{prefix}"] = df[col_A]
                    else:
                        # Calculate average and take the max of the two columns
                        df[f"{prefix}"] = df[[col_A, col_B]].mean(axis=1).max()

            # Drop the original columns if they exist
            columns_to_drop = ['CO_A', 'CO_B', 'HCHO_A', 'HCHO_B', 'EtOH_A', 'EtOH_B']
            df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

            # Save the merged DataFrame as pickle
            df.to_pickle(output_file_path)

    return output_dir

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Merge specific columns in DataFrames and save as pickles")
    parser.add_argument("input_dir", type=str, help="./cml-pipeline-dvc/out")
    parser.add_argument("output_dir", type=str, help="./cml-pipeline-dvc/out")

    args = parser.parse_args()
    
    # Call merge_bench_line function
    merge_bench_line_dvc(args.input_dir, args.output_dir)
