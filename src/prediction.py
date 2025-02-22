import numpy as np
import pandas as pd

# Charger les valeurs min/max pour la dé-normalisation
df = pd.read_csv("data/data_normalized.csv")
km_min, km_max = df["km"].min(), df["km"].max()
price_min, price_max = df["price"].min(), df["price"].max()

def predict_price(km):
    """Prédit le prix d'une voiture en fonction du kilométrage donné en entrée."""
    # Charger les paramètres optimisés (entraînés sur des données normalisées)
    theta_0, theta_1 = np.load("model.npy")

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

