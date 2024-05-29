import argparse
import pandas as pd
from pathlib import Path
import pickle

def nan_drop(df):
    """
    Drop rows with NaN values from the DataFrame.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame.
    
    Returns:
    pd.DataFrame: DataFrame with rows containing NaN values removed.
    """
    # Supprimer les lignes contenant des valeurs NaN
    return df.dropna(axis=0, how='any')

if __name__ == "__main__":
    # Parser pour les arguments d'entrée
    parser = argparse.ArgumentParser(description="Drop rows with NaN values from DataFrames and save as pickles")
    parser.add_argument("input_dir", type=str, help="./cml-pipeline-dvc/src/out")
    parser.add_argument("output_dir", type=str, help="./cml-pipeline-dvc/src/out")
    args = parser.parse_args()
    
    # Convertir les chemins d'entrée et de sortie en objets Path
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    # Assurer que le répertoire de sortie existe
    output_dir.mkdir(parents=True, exist_ok=True)

    # Parcourir chaque fichier pickle dans le répertoire d'entrée
    for input_file_path in input_dir.glob("*.pkl"):
        # Charger le DataFrame depuis le fichier pickle
        with open(input_file_path, 'rb') as f:
            df = pickle.load(f)
        
        # Appliquer la fonction nan_drop pour supprimer les lignes avec des valeurs NaN
        df_cleaned = nan_drop(df)
        
        # Enregistrer le DataFrame nettoyé dans un fichier pickle dans le répertoire de sortie
        output_file_path = output_dir / input_file_path.name
        with open(output_file_path, 'wb') as f:
            pickle.dump(df_cleaned, f)
