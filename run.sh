#!/bin/bash

echo "Activation de l'environnement virtuel..."

# Vérifier si l'environnement virtuel existe
if [ ! -d "ftlinear" ]; then
    echo "🛠 Création de l'environnement virtuel..."
    python3 -m venv ftlinear
fi

# Détecter si le système est Debian/Ubuntu avec PEP 668 (éviter l'erreur `externally-managed-environment`)
if grep -q "externally-managed" /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null; then
    echo "Système avec gestion des paquets restreinte. Utilisation de '--break-system-packages'."
    PIP_EXTRA="--break-system-packages"
else
    PIP_EXTRA=""
fi

# Activer l'environnement virtuel
source ftlinear/bin/activate

echo "Installation des dépendances..."
pip install --upgrade pip $PIP_EXTRA
pip install -r requirements.txt $PIP_EXTRA

echo "Exécution du programme..."
python main.py
