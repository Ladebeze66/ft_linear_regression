import tkinter as tk
from tkinter import messagebox

def show_gui(predict_price):
    """Affiche l'interface graphique Tkinter pour entrer un kilométrage et voir le prix estimé."""
    
    def estimate_price():
        try:
            km = float(entry_km.get())  # Récupère la valeur entrée
            price = predict_price(km)  # Prédiction du prix
            label_result.config(text=f"Prix estimé : {price:.2f} €", fg="green")  # Affiche le prix
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un kilométrage valide.")

    root = tk.Tk()
    root.title("Estimation de prix de voiture")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    label_title = tk.Label(frame, text="Estimation de prix de voiture", font=("Arial", 14, "bold"))
    label_title.pack()

    label_km = tk.Label(frame, text="Entrez le kilométrage :")
    label_km.pack()

    entry_km = tk.Entry(frame)
    entry_km.pack()

    btn_estimate = tk.Button(frame, text="Estimer le prix", command=estimate_price)
    btn_estimate.pack()

    label_result = tk.Label(frame, text="", font=("Arial", 12))
    label_result.pack()

    root.mainloop()
