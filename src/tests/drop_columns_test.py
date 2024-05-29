import unittest
import pandas as pd
import yaml
from pathlib import Path
import pickle



class TestdropChannels(unittest.TestCase):

    def setUp(self):
        # Load rename mapping from YAML file
        with open('intermidiate_files/rename_map.yaml', 'r') as file:
            self.rename_map = yaml.safe_load(file)

        # Read column name from the text file
        with open('intermidiate_files/drop_file.txt', 'r') as column_file:
            self.column_name = column_file.read().strip()

        # Create DataFrames from files in the out directory
        self.df = self.load_dataframes_from_files()

    def load_dataframes_from_files(self):
        dataframes = []
        out_dir = Path('out')
        for file_path in out_dir.glob('*.pkl'):
            with open(file_path, 'rb') as f:
                df = pickle.load(f)
                dataframes.append(df)
        return pd.concat(dataframes, ignore_index=True)

    def test_column_existence(self):
        # Check if the column name exists
        if self.column_name:
            # Check if the column exists in the DataFrame
            self.assertTrue(self.column_name in self.df.columns, f"Column '{self.column_name}' does not exist in the DataFrame")
        else:
            # If column name is empty, pass the test
            self.assertTrue(True, "Column name is empty, test skipped")

if __name__ == '__main__':
    unittest.main()
