import pandas as pd
import pickle
from pathlib import Path

def merge_bench_line_dvc(input_dir, output_dir):
    """
    Merges specific columns in DataFrame pickle files from input_dir based on criteria and saves the merged DataFrames
    in output_dir.

    Parameters:
    input_dir (str): Path to the directory containing input DataFrame pickle files.
    output_dir (str): Path to the directory to save the output merged DataFrame pickle files.
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for input_file_path in input_dir.glob("*.pkl"):
        output_file_path = output_dir / input_file_path.name

        df = pd.read_pickle(input_file_path)

        # Find all columns that match the pattern *_A and *_B
        columns_A = [col for col in df.columns if col.endswith('_A')]
        columns_B = [col.replace('_A', '_B') for col in columns_A if col.replace('_A', '_B') in df.columns]

        for col_A, col_B in zip(columns_A, columns_B):
            prefix = col_A[:-2]  # Remove the '_A' suffix to get the prefix
            insert_position = df.columns.get_loc(col_A)  # Get the position of the col_A column

            # Check if both columns are empty
            if df[col_A].isnull().all() and df[col_B].isnull().all():
                df[prefix] = None
            else:
                # Create the new column with the merged values
                df[prefix] = df.apply(
                    lambda row: row[col_A] if row[col_A] == row[col_B] else max(row[col_A], row[col_B]),
                    axis=1
                )

            # Move the new column to the position of the original _A column
            cols = list(df.columns)
            cols.insert(insert_position, cols.pop(cols.index(prefix)))
            df = df[cols]

        # Drop the original _A and _B columns
        columns_to_drop = [col for pair in zip(columns_A, columns_B) for col in pair]
        df.drop(columns=columns_to_drop, inplace=True)

        df.to_pickle(output_file_path)

    return output_dir

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Merge specific columns in DataFrames and save as pickles")
    parser.add_argument("input_dir", type=str, help="Path to the input directory containing DataFrame pickles.")
    parser.add_argument("output_dir", type=str, help="Path to the output directory to save merged DataFrame pickles.")

    args = parser.parse_args()
    
    # Call merge_bench_line_dvc function
    merge_bench_line_dvc(args.input_dir, args.output_dir)
