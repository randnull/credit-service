from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from common.errors.errors import *

from models.dto_table.dto import ApplicationRequestModel
from typing import Annotated
from services.application_service import ApplicationService


application_router = APIRouter(prefix="/application", tags=["origination"])

ApplicationServiceRepo = Annotated[ApplicationService, Depends(ApplicationService)]


@application_router.post("/")
async def add_application(application_request: ApplicationRequestModel, application_service: ApplicationServiceRepo):
    '''
    Add new application
    '''

    answer = await application_service.add_application(application_request)
    
    return JSONResponse(content={"application_id": f"{answer['id']}", "status": f"{answer['status']}"}, status_code=answer['code'])


@application_router.post("/{agreement_id}/close")
async def close_application(agreement_id: int, application_service: ApplicationServiceRepo):
    '''
    Close application
    '''

    try:
        status = await application_service.close_application(agreement_id)
    except ApplicationNotFound:
        return JSONResponse(content={"message": "Not Found"}, status_code=404)
    except TryCloseWhileFuture:
        return JSONResponse(content={"message": "Your credit was already active and you have future payments"}, status_code=403)
    except ServerCloseError:
        return JSONResponse(content={"message": "Error with closing credit"}, status_code=500)
    
    return JSONResponse(content={"message": "Application was succefully closed!"}, status_code=200)
