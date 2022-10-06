# import statements
import bson
from fastapi import APIRouter, UploadFile, Response, File
from starlette.responses import FileResponse
from database import collection
from bson import ObjectId
import os


invoice_router = APIRouter()


# getting all invoices ok
@invoice_router.get('/invoices')
async def get_all_invoices_id_and_file_name():
    list_inv = []  # create an empty list
    cursor = collection.find({})  # find all documents in the collection
    async for document in cursor:  # loop through the documents
        # append only the file name and the id to the list
        list_inv.append({"id": str(document["_id"]), "file_name": document["file_name"]})
    return list_inv  # return the list of invoices


# getting a specific invoice ok
@invoice_router.get('/invoices/{invoiceId}')
async def find_invoice_by_id(invoiceId):
    invoiceId = await collection.find_one({"_id": ObjectId(invoiceId)})
    found_invoice = invoiceId["file"]  # this is the file that we want to download
    found_invoice = bson.binary.Binary(found_invoice)  # convert the file to binary
    print(os.getcwd())
    if found_invoice:
        with open("./pdf_extract/found_invoice.pdf", "wb") as file:  # open the file in write binary mode
            found_invoice.pdf = file.write(found_invoice)
            # file_path used to write the file
            file_path_pdf = "./pdf_extract/found_invoice.pdf"
            return FileResponse(path = file_path_pdf, filename = file.name,
                                media_type = "application/pdf")  # return the file
    else:  # if the file is not found
        return Response(content = "File not found", media_type = "text/plain")  # return a text response


# creating invoice in DB ok but 422 validation error
@invoice_router.post('/invoices')
async def create_invoice(file: UploadFile = File(...)):
    # convert the file to binaryfile
    binaryfile = bson.Binary(file.file.read())
    # insert the binaryfile into the database and the collection invoices
    await collection.insert_one({"file_name": file.filename, "file": binaryfile, })
    # remove error 422
    return Response(content = "File uploaded successfully", media_type = "text/plain")


# update invoice in DB  ok but 422 validation error
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


# Delete invoice ok but 422 validation error
@invoice_router.delete('/invoices/{invoiceId}')
async def delete_invoice(invoiceId):
    # finds the student deletes it and also returns the same student object
    await collection.delete_one({"_id": ObjectId(invoiceId)})
    # return invoiceEntity(await collection.find_one_and_delete({"_id": ObjectId(invoiceId)}))
    return {"message": "File deleted successfully"}
