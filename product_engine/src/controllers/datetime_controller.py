from fastapi import APIRouter
from fastapi.responses import JSONResponse

from common.errors.errors import *

from config.settings import settings

from datetime import datetime

from models.dto_table.dto import DatetimeModel


datetime_router = APIRouter()

@datetime_router.post("/set_datetime")
async def set_datetime(date_model: DatetimeModel):
    """
    Set custom datetime
    """

    settings.USE_CUSTOM_DATETIME = True

    settings.CUSTOM_DATETIME = datetime(
        date_model.year, 
        date_model.month, 
        date_model.day,
        date_model.hour,
        date_model.minute
        )

    return JSONResponse(content={"Status": "ok"}, status_code=200)


@datetime_router.post("/set_original_datetime")
async def set_original_datetime():
    """
    Set original datetime
    """

    settings.USE_CUSTOM_DATETIME = False
    
    return JSONResponse(content={"Status": "ok"}, status_code=200)
