from fastapi import FastAPI
from starlette.responses import RedirectResponse
from crud import invoice_router

# Create app object
app = FastAPI()

# Redirect root to /docs
@app.get("/", include_in_schema=False) # include_in_schema=False to hide the route from the documentation
async def redirect_to_docs():
    return RedirectResponse(url='/docs') # redirect to /docs route instead of /

# Register your router
app.include_router(invoice_router)
