from fastapi import FastAPI

from controllers.origination_controller import origination_router
from controllers.product_engine_controllers import pe_router

tags = [
    {
        "name": "product_engine",
        "description": "Operations with product engine"
    },
    {
        "name": "origination",
        "description": "Operations with origination"
    },
    {
        "name": "schedule",
        "description": "Operations with schedule"
    }
]


app = FastAPI(openapi_tags=tags)

app.include_router(origination_router)
app.include_router(pe_router)
