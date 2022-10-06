# import statements
# from pymongo import MongoClient
# MongoDB driver
import motor.motor_asyncio  # USE THIS CODE TO CONNECT TO YOUR LOCAL MONGODB

# create BD connection
# connection = MongoClient("mongodb://localhost:27017/")

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')  # Create a connection to the DB_NAME
database = client.local  # local is the name of the database in MongoDB
collection = database.invoice  # invoice is the name of the collection in MongoDB://localhost:27017/")


# async def find_all_invoices():  # response_model = List[Invoice]
#     all_invoices = []  # create an empty list
#     cursor = collection.find({})  # find all documents in the collection
#     async for document in cursor:  # loop through the documents
#         all_invoices.append(Invoice(**document))  # ** is used to unpack the dictionary
#     return all_invoices  # return the list of invoices
