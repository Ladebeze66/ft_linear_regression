import sys
import os

# Ajoute dynamiquement le dossier `src/` au path Python
sys.path.append(os.path.abspath("src"))

from src.training_model import train_model
from src.prediction import predict_price

# Interface principale en console
def main():
    print(" Bienvenue dans le modèle de prédiction de prix de voiture !")
    print(" Le modèle va être entraîné...")
    
    # Entraîner le modèle
    train_model()

    while True:
        try:
            # Demander un kilométrage
            km = float(input("\nEntrez un kilométrage (ou tapez 'exit' pour quitter) : "))
            
            # Prédire le prix
            price = predict_price(km)
            print(f"Prix estimé : {price:.2f} €")

        except ValueError:
            print("Veuillez entrer un nombre valide ou 'exit' pour quitter.")
        
        # Demander si l'utilisateur veut continuer
        continuer = input("Voulez-vous faire une autre estimation ? (o/n) : ").strip().lower()
        if continuer != "o":
            print("Merci d'avoir utilisé le modèle de prédiction ! À bientôt !")
            break

if __name__ == "__main__":
    main()
