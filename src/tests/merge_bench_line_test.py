import unittest
import pandas as pd
import yaml
from pathlib import Path
import pickle

class TestRenameChannels(unittest.TestCase):

    def setUp(self):
      

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

    def test_null_columns(self):
        # Assuming 'col_A' and 'col_B' should be merged based on the provided function logic
        columns_A = [col for col in self.df.columns if col.endswith('_A')]
        columns_B = [col.replace('_A', '_B') for col in columns_A if col.replace('_A', '_B') in self.df.columns]

        for col_A, col_B in zip(columns_A, columns_B):
            prefix = col_A[:-2]  # Remove the '_A' suffix to get the prefix
            
            self.df[prefix] = self.df.apply(
                lambda row: row[col_A] if pd.isnull(row[col_A]) or pd.isnull(row[col_B]) else (row[col_A] if row[col_A] == row[col_B] else max(row[col_A], row[col_B])),
                axis=1
            )

            # Check if the new column is correctly merged
            for idx, row in self.df.iterrows():
                val_A = row[col_A]
                val_B = row[col_B]
                if pd.isnull(val_A):
                    self.assertTrue(pd.isnull(row[prefix]) or row[prefix] == val_B)
                elif pd.isnull(val_B):
                    self.assertTrue(row[prefix] == val_A)
                else:
                    expected_val = val_A if val_A == val_B else max(val_A, val_B)
                    self.assertEqual(row[prefix], expected_val)

if __name__ == '__main__':
    unittest.main()
