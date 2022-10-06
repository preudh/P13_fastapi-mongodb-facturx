# Import statements
from typing import Any, Callable, Set, TypeVar
from fastapi import FastAPI
from crud import invoice_router

# Create app object
app = FastAPI()

# register your router
app.include_router(invoice_router)
