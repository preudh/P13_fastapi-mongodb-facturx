# Description: Ce fichier contient les paramètres de connexion à la base de données MongoDB.
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir d'un fichier .env situé dans le même répertoire ou à l'emplacement spécifié.
load_dotenv()

# Variable d'environnement pour distinguer l'environnement de développement de la production.
FASTAPI_ENV = os.getenv('FASTAPI_ENV', 'development')

# URI de connexion à MongoDB pour le développement et la production.
LOCAL_MONGODB_URI = 'mongodb://localhost:27017/'
PRODUCTION_MONGODB_URI = os.getenv('MONGODB_URI')  # Doit être défini dans le fichier .env ou dans les variables d'environnement de Heroku.

# Sélection de l'URI en fonction de l'environnement.
MONGODB_URI = PRODUCTION_MONGODB_URI if FASTAPI_ENV == 'production' else LOCAL_MONGODB_URI

# Initialiser le client MongoDB.
client = AsyncIOMotorClient(MONGODB_URI)

# La base de données et la collection peuvent également être paramétrées par des variables d'environnement.
DATABASE_NAME = os.getenv('MONGODB_DB', 'local')
COLLECTION_NAME = os.getenv('MONGODB_COLLECTION', 'invoice')

# Sélectionner la base de données et la collection.
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]
