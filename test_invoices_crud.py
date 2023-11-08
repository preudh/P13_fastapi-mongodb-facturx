"""
Test the crud.py using the FastAPI test client.
"""
from fastapi import FastAPI # import the FastAPI class
from fastapi.testclient import TestClient # import the TestClient class
from crud import invoice_router
import motor.motor_asyncio  # USE THIS CODE TO CONNECT TO YOUR LOCAL MONGODB


# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')

app = FastAPI() # create an app object


def test_get_all_invoice_id_and_file_name():  # is used to test the get_all_invoice_id_and_file_name function
    with TestClient(app) as client:  # create a test client
        new_invoice = client.post("/invoice/", json={"file_name": "invoice.pdf"}).json()  # create a new invoice
        get_invoice_response = client.get("/invoice/" + new_invoice.get("_id"))  # get the invoice_router
        assert get_invoice_response.status_code == 200  # assert that the response status code is 200
        assert get_invoice_response.json() == new_invoice  # assert that the response json is the same as the new invoice

# test find_invoice_by_id






















# client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017") # create a client


# def test_create_invoice():  # used to test the creation of a new invoice
#
#     response = client.post("/invoice/", json={"invoice_number": "1234", "invoice_date": "2021-01-01", "invoice_amount": 100.00})
#     file = open("./sample_facturx/Facture_FR_BASIC.pdf", "wb")
#     binary_file_example = bson.binary.Binary(file)  # create a binary file_name
#     # post the file_name and the binary file
#     response = client.post("/invoice/", json = {"file": binary_file_example, "file_name": "Facture_FR_BASIC.pdf"})
#     assert response.status_code == 201  # check the status code
#
#     body = response.json()  # get the response body
#     assert body.get("file") == binary_file_example  # check the binary file
#     assert body.get("file_name") == "Facture_FR_BASIC.pdf"  # check the file_name
#     assert "_id" in body  # check the id


# def test_get_all_invoice_id_and_file_name():
#     with TestClient(app) as clients:
#         new_invoice = clients.post("/invoice/", json = {"company": "123456789", "number": "FACTURE-123456789"})
#         get_invoice_response = clients.get("/invoice/") + new_invoice.json().get("_id")
#         assert get_invoice_response.status_code == 200
#         assert get_invoice_response.json() == new_invoice
