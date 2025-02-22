import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Visualisation des données brutes
def plot_raw_data(df):
    """Affiche les histogrammes du kilométrage et du prix avant normalisation."""
    plt.figure(figsize=(12, 5))    
    # Histogramme du kilométrage
    plt.subplot(1, 2, 1) # 1 ligne, 2 colonnes, 1ère figure
    sns.histplot(df["km"], bins = 20, kde=True, color="blue")
    plt.xlabel("Kilométrage (km)")
    plt.ylabel("Nombre de voitures")
    plt.title("Distribution du kilométrage (Données brutes)")    
    # Histogramme du prix
    plt.subplot(1, 2, 2) # 1 ligne, 2 colonnes, 2ème figure
    sns.histplot(df["price"], bins = 20, kde=True, color="green")
    plt.xlabel("Prix (€)")
    plt.ylabel("Nombre de voitures")
    plt.title("Distribution du prix (Données brutes)")
    plt.show()
    
    # Nuage de points
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="km", y="price", data=df, alpha=0.5, color="red")
    plt.xlabel("Kilométrage (km)")
    plt.ylabel("Prix (€)")
    plt.title("Relation entre Kilométrage et Prix (Données brutes)")
    plt.show()

# Visualisation des données normalisées
def plot_normalized_data(df):
    """"Affiche les distributions des données après normalisation."""
    plt.figure(figsize=(12, 5))
    # Histogramme du kilométrage normalisé
    plt.subplot(1, 2, 1) # 1 ligne, 2 colonnes, 1ère figure
    sns.histplot(df["km_norm"], bins = 20, kde=True, color="blue")
    plt.xlabel("Kilométrage normalisé")
    plt.ylabel("Nombre de voitures")
    plt.title("Distribution du kilométrage normalisé")
    # Histogramme du prix normalisé
    plt.subplot(1, 2, 2) # 1 ligne, 2 colonnes, 2ème figure
    sns.histplot(df["price_norm"], bins = 20, kde=True, color="green")
    plt.xlabel("Prix normalisé")
    plt.ylabel("Nombre de voitures")
    plt.title("Distribution du prix normalisé")
    plt.show()
    
    # Nuage de points
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="km_norm", y="price_norm", data=df, alpha=0.5, color="red")
    plt.xlabel("Kilométrage normalisé")
    plt.ylabel("Prix normalisé")
    plt.title("Relation entre Kilométrage et Prix normalisés")
    plt.show()


def plot_cost_history(cost_history):
    """Affiche l'évolution du coût en fonction du nombre d'itérations."""
    plt.figure(figsize=(8 , 6)) # taille de la figure
    plt.plot(range(len(cost_history)), cost_history, 'b-', linewidth=2)
    plt.xlabel("Nombre d'itérations") # Axe des abscisses
    plt.ylabel("Coût J(θ)") # Axe des ordonnées
    plt.title("Evolution du coût en fonction des itérations")
    plt.grid(True) # Affichage de la grille
    plt.show()
    
# Visualisation de la régression linéaire
def plot_regression_line(df, theta_0, theta_1):
    """Affiche la droite de régression linéaire sur les données normalisées."""
    # Affichage des données normalisées
    plt.figure(figsize=(8, 6))
    # Nuage de points des données
    sns.scatterplot(x=df["km_norm"], y=df["price_norm"], alpha=0.5, label="Données") # alpha=0.5 pour la transparence
    # Droite de régression linéaire
    X_range = np.linspace(0, 1, 100) # Génère 100 valeurs entre 0 et 1
    y_pred = theta_0 + theta_1 * X_range
    plt.plot(X_range, y_pred, color="red", label="Régression linéaire")
    plt.xlabel("Kilométrage normalisé")
    plt.ylabel("Prix normalisé")
    plt.title("Régression linéaire après entraînement")
    plt.legend() # Affiche la légende
    plt.show()

    
    