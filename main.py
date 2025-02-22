import sys
import os

# Ajoute dynamiquement le dossier `src/` au path Python
sys.path.append(os.path.abspath("src"))

from src.training_model import train_model
from src.prediction import predict_price  # ✅ Peut maintenant être importé dès le début
from src.gui import show_gui  # ✅ Import propre et structuré

def main():
    print("📌 Bienvenue dans le modèle de prédiction de prix de voiture !")
    print("🔄 Le modèle va être entraîné...")

    # Entraîner le modèle
    train_model()
    print("✅ Modèle entraîné avec succès !")

    # Lancer l'interface graphique après l'entraînement
    print("🖥️ Lancement de l'interface graphique...")
    show_gui(predict_price)

if __name__ == "__main__":
    main()
