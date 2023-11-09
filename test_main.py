# test_main.py
from motor.motor_asyncio import AsyncIOMotorClient
import pytest
from unittest.mock import AsyncMock, patch
from httpx import AsyncClient
from starlette.testclient import TestClient
from main import app  # Replace this with the actual import of your FastAPI application
from bson import ObjectId
from crud import invoice_router  # Make sure to correctly import the router
from fastapi import UploadFile
from io import BytesIO

# Hard-coded test database settings
TEST_MONGODB_URI = 'mongodb://localhost:27017/'
TEST_MONGODB_DB = 'test_db'
TEST_MONGODB_COLLECTION = 'test_invoice'

@pytest.fixture(scope='function')
async def test_db():
    # Initialize connection to the test database
    client = AsyncIOMotorClient(TEST_MONGODB_URI)
    test_db = client[TEST_MONGODB_DB]
    test_collection = test_db[TEST_MONGODB_COLLECTION]

    # Preparation if necessary
    # await test_collection.insert_one({'_id': ObjectId(), 'data': 'test'})

    yield test_collection  # Yield the test collection to the test function

    # Cleanup: drop the test collection after each test
    await test_db.drop_collection(TEST_MONGODB_COLLECTION)
    client.close()  # Close the database client

# Use the 'test_db' fixture in test functions
@pytest.mark.asyncio
async def test_get_all_invoices_id_and_file_name(test_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/invoices")  # Send a GET request to /invoices
        assert response.status_code == 200  # Check that the response status code is 200
        assert isinstance(response.json(), list)  # Check that the response is a list

# Create a TestClient instance for your FastAPI application
client = TestClient(app)

# Configure your FastAPI application's routes to use the TestClient
app.include_router(invoice_router)

# Use the patch decorator to mock the MongoDB collection
@pytest.fixture(scope="function")
def mock_collection():
    with patch("crud.collection", new_callable=AsyncMock) as mock:
        yield mock

@pytest.mark.asyncio
async def test_find_invoice_by_id(mock_collection):
    # Prepare an ObjectId for the test
    invoice_id = ObjectId()

    # Prepare the mock's behavior
    mock_collection.find_one.return_value = {
        "_id": invoice_id,
        "file_name": "invoice.pdf",
        "file": b"PDF content"
    }

    # Make the request to the FastAPI endpoint
    response = client.get(f"/invoices/{invoice_id}")

    # Assertions to test the request result
    assert response.status_code == 200
    assert response.content == b"PDF content"

# Continue with the rest of the test functions for create, update, and delete.
# Replace "crud.collection" with the path to your actual collection in the application code.

@pytest.mark.asyncio
async def test_create_invoice(mock_collection):
    # Mock the uploaded file
    file_data = b"PDF content"
    file_name = "test_invoice.pdf"
    content_type = "application/pdf"
    upload_file = UploadFile(filename=file_name, content_type=content_type)
    upload_file.file = BytesIO(file_data)

    # Configure the mock's behavior
    mock_collection.insert_one.return_value.inserted_id = ObjectId()

    # Make the request to the FastAPI endpoint
    response = client.post(
        "/invoices",
        files={"file": (file_name, file_data, content_type)}
    )

    # Assertions to test the request result
    assert response.status_code == 200
    mock_collection.insert_one.assert_called_once()

@pytest.mark.asyncio
async def test_update_invoice(mock_collection):
    # Mock the uploaded file
    file_data = b"Updated PDF content"
    file_name = "updated_test_invoice.pdf"
    content_type = "application/pdf"
    upload_file = UploadFile(filename=file_name, content_type=content_type)
    upload_file.file = BytesIO(file_data)

    # Prepare an ObjectId for the test
    invoice_id = ObjectId()

    # Configure the mock's behavior
    mock_collection.update_one.return_value.modified_count = 1

    # Make the request to the FastAPI endpoint
    response = client.put(
        f"/invoices/{invoice_id}",
        files={"file": (file_name, file_data, content_type)}
    )

    # Assertions to test the request result
    assert response.status_code == 200
    mock_collection.update_one.assert_called_once()

@pytest.mark.asyncio
async def test_delete_invoice(mock_collection):
    # Prepare an ObjectId for the test
    invoice_id = ObjectId()

    # Configure the mock's behavior
    mock_collection.delete_one.return_value.deleted_count = 1
    # Make the request to the FastAPI endpoint


    response = client.delete(f"/invoices/{invoice_id}")

    # Assertions to test the request result
    assert response.status_code == 200
    mock_collection.delete_one.assert_called_once()


# In the 3 latest tests, the database operations are mocked, which means that no real MongoDB database is required for
# the tests to run. The `AsyncMock` is used to simulate the behavior of the `collection` object, and assertions are made
# based on the expected outcomes of API calls. This allows you to test the API's logic and response without needing an
# actual database, which is a common practice for unit testing.
