# import statements
import bson # used to convert the file to binary
from fastapi import UploadFile, File # used to upload
from database import collection # used to connect to the database
from fastapi import APIRouter, HTTPException # used to create a router
from fastapi.responses import StreamingResponse # used to stream the file
from starlette.responses import Response # used to send a response
from io import BytesIO # used to create a file in memory
from bson import ObjectId # used to convert the id to string

# Allow to group routes
invoice_router = APIRouter()


# getting all invoices id and file name ok
# Ask the collection MongoDB for all the documents and return a list of dictionaries with the id and file_name of each invoice
@invoice_router.get('/invoices')
async def get_all_invoices_id_and_file_name():
    list_inv = []  # create an empty list
    cursor = collection.find({})  # find all documents in the collection
    async for document in cursor:  # loop through the documents
        # append only the file name and the id to the list
        list_inv.append({"id": str(document["_id"]), "file_name": document["file_name"]})
    return list_inv  # return the list of invoices

# getting a specific invoice by id
# Find a specific document in the collection MongoDB
# Write the file in the ram then return the file as a FileResponse allowing the user to download the file
@invoice_router.get('/invoices/{invoiceId}', response_class = StreamingResponse)
async def find_invoice_by_id(invoiceId: str):
    invoice_record = await collection.find_one({"_id": ObjectId(invoiceId)})

    if not invoice_record:
        raise HTTPException(status_code = 404, detail = "Invoice not found") # 404 Not Found

    found_invoice = invoice_record.get("file") # this is the file that we want to download

    if not found_invoice: # if the file is not found
        raise HTTPException(status_code = 404, detail = "Invoice file not found") # 404 Not Found


    pdf_in_memory = BytesIO(found_invoice)  # create a file in memory
    pdf_in_memory.seek(0)  # move the cursor to the beginning of the file

    headers = {
        'Content-Disposition': 'attachment; filename="invoice.pdf"'
    } # Force the browser to download the file

    return StreamingResponse(pdf_in_memory, media_type = 'application/pdf', headers = headers) # return the file


# Define a route for creating a new invoice. Read the file and convert it to binary then insert in the collection MongoDB
# Then send success message
@invoice_router.post('/invoices')
async def create_invoice(file: UploadFile = File(...)):
    # convert the file to binaryfile
    binaryfile = bson.Binary(file.file.read())
    # insert the binaryfile into the database and the collection invoices
    await collection.insert_one({"file_name": file.filename, "file": binaryfile, })
    # remove error 422
    return Response(content = "File uploaded successfully", media_type = "text/plain")


# Define a route to update an existing invoice in DB with its ID  ok but 422 validation error
@invoice_router.put('/invoices/{invoiceId}')
async def update_invoice(invoiceId, file: UploadFile = File(...)):
    # convert the file to binaryfile
    binaryfile = bson.Binary(file.file.read())  # convert the file to binary
    # reload the invoice with file and filename
    await collection.update_one(
        {"_id": ObjectId(invoiceId)},  # find the invoice with matching id
        {"$set": {"file_name": file.filename, "file": binaryfile}}  #
    )
    return Response(content = "File updated successfully", media_type = "text/plain")


# Delete invoice by using its ID ok but 422 validation error
# send success message
@invoice_router.delete('/invoices/{invoiceId}')
async def delete_invoice(invoiceId):
    # finds the student deletes it and also returns the same student object
    await collection.delete_one({"_id": ObjectId(invoiceId)})
    # return invoiceEntity(await collection.find_one_and_delete({"_id": ObjectId(invoiceId)}))
    return {"message": "File deleted successfully"}





