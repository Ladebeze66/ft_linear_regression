def cli_interface(predict_price):
    """Interface en ligne de commande pour entrer un kilométrage et voir le prix estimé."""
    while True:
        user_input = input("Entrez un kilométrage (ou 'q' pour quitter) : ")
        if user_input.lower() == 'q':
            print("Fermeture du programme.")
            break
        try:
            km = float(user_input)
            price = predict_price(km)
            print(f"Prix estimé : {price:.2f} €")
        except ValueError:
            print("Erreur : Veuillez entrer un kilométrage valide.")
