import numpy as np
import pandas as pd
import os

# Génère le chemin absolu basé sur l’emplacement du script
file_path = os.path.abspath(os.path.join(os.getcwd(), "data", "data_normalized.csv"))
df = pd.read_csv(file_path)
km_min, km_max = df["km"].min(), df["km"].max()
price_min, price_max = df["price"].min(), df["price"].max()

def predict_price(km):
    """Prédit le prix d'une voiture en fonction du kilométrage donné en entrée."""
    # Charger les paramètres optimisés (entraînés sur des données normalisées)
    theta_0, theta_1 = np.load("data/model.npy")

    # Normaliser le kilométrage
    km_norm = (km - km_min) / (km_max - km_min)

    # Calculer le prix normalisé
    price_norm = theta_0 + theta_1 * km_norm

    # Dé-normaliser le prix pour obtenir un montant en euros
    price = price_norm * (price_max - price_min) + price_min

    return price

if __name__ == "__main__":
    km_input = float(input("Entrez un kilométrage : "))
    price_predicted = predict_price(km_input)
    print(f"Prix estimé : {price_predicted:.2f} €")

