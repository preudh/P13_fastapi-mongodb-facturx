# import statement
from bson import binary, ObjectId # used to convert the file to binary
from pydantic import BaseModel, Field # used to create a model


class Invoice(BaseModel): # create a model for the invoice
    file: binary.Binary = Field(..., alias = "file") # alias is the name of the field in the database
    file_name: str = Field(..., alias = "file_name")  # alias is the name of the field in the database

    class Config: # used to configure the model
        allow_population_by_field_name = True  # used to allow the use of field names in the database
        arbitrary_types_allowed = True  # used to allow the use of binary data type
        json_encoders = {ObjectId: str}  # used to encode the ObjectId to string

