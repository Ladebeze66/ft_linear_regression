# Utilisation d'une image Python officielle
FROM python:3.12

# Définition du répertoire de travail
WORKDIR /app

# Copier tous les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# COMMANDE PAR défaut : Exécuter "main.py"
CMD ["python", "main.py"]