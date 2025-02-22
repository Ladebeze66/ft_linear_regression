import numpy as np

def evaluate_model(df, theta_0, theta_1):
    """Calcule la précision du modèle en utilisant l'erreur quadratique moyenne (MSE) et R²."""
    X = df["km_norm"].values
    y = df["price_norm"].values

    # Prédictions du modèle
    y_pred = theta_0 + theta_1 * X

    # Erreur quadratique moyenne (MSE)
    mse = np.mean((y - y_pred) ** 2)

    # Coefficient de détermination (R²)
    ss_total = np.sum((y - np.mean(y)) ** 2)
    ss_residual = np.sum((y - y_pred) ** 2)
    r2_score = 1 - (ss_residual / ss_total)

    print(f"\nPrécision du modèle :")
    print(f"🔹 Erreur quadratique moyenne (MSE) : {mse:.4f}")
    print(f"🔹 Coefficient de détermination (R²) : {r2_score:.4f} (plus proche de 1 = meilleur)")

    return mse, r2_score
