import pandas as pd
import pickle
from pathlib import Path

def convert_to_csv(input_dir, output_dir):
    """
    Converts DataFrame pickle files from input_dir to CSV files in output_dir.

    Parameters:
    input_dir (str): Path to the directory containing input DataFrame pickle files.
    output_dir (str): Path to the directory to save the output CSV files.
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for input_file_path in input_dir.glob("*.pkl"):
        output_file_path = output_dir / (input_file_path.stem + ".csv")

        df = pd.read_pickle(input_file_path)

        df.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="./cml-pipeline-dvc/out")
    parser.add_argument("input_dir", type=str, help="./cml-pipeline-dvc/out")
    parser.add_argument("output_dir", type=str, help="./cml-pipeline-dvc/csv_out")

    args = parser.parse_args()
    
    # Call convert_to_csv function
    convert_to_csv(args.input_dir, args.output_dir)
