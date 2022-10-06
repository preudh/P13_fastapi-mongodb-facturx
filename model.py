# import statement
from bson import binary, ObjectId
from pydantic import BaseModel, Field


class Invoice(BaseModel):
    file: binary.Binary = Field(..., alias = "file")
    file_name: str = Field(..., alias = "file_name")  # alias is the name of the field in the database

    class Config:
        allow_population_by_field_name = True  # used to allow the use of field names in the database
        arbitrary_types_allowed = True  # used to allow the use of binary data type
        json_encoders = {ObjectId: str}  # used to encode the ObjectId to string

# class InvoiceUpdate(BaseModel):
#     file: binary.Binary = Field(..., alias = "file")
#     file_name: str = Field(..., alias = "file_name")
