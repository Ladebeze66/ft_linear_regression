import numpy as np
import pandas as pd
from data_process import load_and_process_data
from gradient_descent import gradient_descent
from visualization import plot_cost_history, plot_regression_line
from evaluate_model import evaluate_model

def train_model():
    """
    Charge les données, entraîne le modèle et sauvegarde les paramètres optimisés.
    """
    df, _, _, _, _ = load_and_process_data("data/data.csv")
    X = df["km_norm"].values
    y = df["price_norm"].values

    # Paramètres initaux
    theta_0_init = 0
    theta_1_init = 1
    learning_rate = 0.1 # Taux d'apprentissage
    iterations = 10000

    # Exécuter la descente de gradient
    theta_0_opt, theta_1_opt, cost_history = gradient_descent(X, y, theta_0_init, theta_1_init, learning_rate, iterations)

    # Sauvegarder les paramètres optimisés
    np.save("model.npy", [theta_0_opt, theta_1_opt]) # Sauvegarde des paramètres optimisés dans un fichier .npy
    print("Modèle entraîné et paramètres sauvegardés.")
    print(f"Paramètre optimisé θ₀ = {theta_0_opt}")
    print(f"Paramètre optimisé θ₁ = {theta_1_opt}")

    # Affichage du coût
    plot_cost_history(cost_history) # Affichage de l'historique du coût
    # Affichage de la régression linéaire
    plot_regression_line(df, theta_0_opt, theta_1_opt)
    evaluate_model(df, theta_0_opt, theta_1_opt)
    
    return theta_0_opt, theta_1_opt
    
# Exécution directe si appelé en script
if __name__ == "__main__":
    train_model()