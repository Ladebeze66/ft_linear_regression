import pandas as pd # Manipulation des données
from visualization import plot_raw_data

def load_and_process_data(file_path):
    df = pd.read_csv(file_path)
    
    # Nettoyage : Suppression des valeurs manquantes
    df = df.dropna() # méthode de pandas dropna() pour supprimer les valeurs NaN (NotaNumber) manquantes dans le 
    # Normailisation Min-Max
    km_min, km_max = df["km"].min(), df["km"].max()
    price_min, price_max = df["price"].min(), df["price"].max()
    
    df["km_norm"] = (df["km"] - km_min) / (km_max - km_min)
    df["price_norm"] = (df["price"] - price_min) / (price_max - price_min)
    
    df.to_csv("data/data_normalized.csv", index=False)
    print("Données nettoyées et normalisées suvegardées dans 'data/data_normalized.csv' !")
    plot_raw_data(df) # Affichage des données normalisées 
    
    return df, km_min, km_max, price_min, price_max # Retourne les données normalisées et les bornes de normalisation
      

if __name__ == "__main__":
    load_and_process_data("data/data.csv") # Appel de la fonction avec le chemin du fichier de données