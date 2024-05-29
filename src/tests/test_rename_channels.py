import unittest
import pandas as pd
import yaml
from pathlib import Path
import pickle

class TestRenameChannels(unittest.TestCase):

    def setUp(self):
        # Load rename mapping from YAML file
        with open('intermidiate_files/rename_map.yaml', 'r') as file:
            self.rename_map = yaml.safe_load(file)

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

    def test_existing_column_name(self):
        # Check if the rename map is not empty
        if self.rename_map:
            # Check if the column name exists in the DataFrame before renaming
            for old_name in self.rename_map.keys():
                self.assertIn(old_name, self.df.columns, f"Column '{old_name}' does not exist in DataFrame")
        else:
            self.skipTest("Rename map is empty, skipping test")

    def test_new_column_name_not_exists(self):
        # Check if the rename map is not empty
        if self.rename_map:
            # Verify if the new column name does not already exist in the DataFrame
            new_column_names = list(self.rename_map.values())
            for new_name in new_column_names:
                self.assertNotIn(new_name, self.df.columns, f"Column '{new_name}' already exists in DataFrame")
        else:
            self.skipTest("Rename map is empty, skipping test")

    def test_new_column_name_length(self):
        # Check if the rename map is not empty
        if self.rename_map:
            # Ensure that the new column name does not exceed 20 characters
            new_column_names = list(self.rename_map.values())
            for new_name in new_column_names:
                self.assertLessEqual(len(new_name), 20, f"Length of column name '{new_name}' exceeds 20 characters")
        else:
            self.skipTest("Rename map is empty, skipping test")

if __name__ == '__main__':
    unittest.main()
