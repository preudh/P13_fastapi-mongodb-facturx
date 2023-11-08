import motor.motor_asyncio  # USE THIS CODE TO CONNECT TO YOUR LOCAL MONGODB

# Used to connect to the database
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')  # Create a connection to the DB_NAME
database = client.local  # local is the name of the database in MongoDB
collection = database.invoice  # invoice is the name of the collection in MongoDB://localhost:27017/")


