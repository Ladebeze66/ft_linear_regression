import numpy as np

# Fonction de coût
def compute_cost(theta_0, theta_1, X, y):
    m = len(y)
    predictions = theta_0 + theta_1 * X # calcul des prédictions h(θ)
    errors = predictions - y # Erreur entre prédictions et vrai prix
    cost = (1 / (2 * m)) * np.sum(errors **2) # Somme des erreurs quadratiques
    return cost
