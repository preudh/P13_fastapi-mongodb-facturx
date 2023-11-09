# Description: This file contains the code to connect to the MongoDB database.
import motor.motor_asyncio
import os

def get_database_client():
    # Use a different URI if running in a test environment
    # URI is the connection string to connect to MongoDB
    db_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/') # MONGODB_URI is the name of the environment
    # variable and mongodb://localhost:27017/ is the default value
    return motor.motor_asyncio.AsyncIOMotorClient(db_uri)

def get_database(client):
    # Choose the database to use based on an environment variable
    database_name = os.getenv('MONGODB_DB', 'local') # MONGO_DB is the name of the environment variable and local is the
    # default value
    return client[database_name] # MONGODB_DB is the name of the environment variable and local is the default value
    # return client[database_name] with database_name = local or MONGODB_DB

def get_collection(database):
    # Choose the collection to use based on an environment variable
    collection_name = os.getenv('MONGODB_COLLECTION', 'invoice') # MONGODB_COLLECTION is the name of the environment
    # variable and invoice is the default value
    return database[collection_name]

# Create the client, database, and collection using the above functions
client = get_database_client() # USE THIS CODE TO CONNECT TO YOUR LOCAL MONGODB
database = get_database(client) # USE THIS CODE TO CONNECT TO YOUR LOCAL MONGODB
collection = get_collection(database) # USE THIS CODE TO CONNECT TO YOUR LOCAL MONGODB

