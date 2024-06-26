from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from common.errors.errors import *

from common.shared_models.dto_models.request_model import RequestModel
from services.agreement_service import AgreementService

from typing import Annotated


agreement_router = APIRouter(prefix="/agreement")

AgreementServiceBase = Annotated[AgreementService, Depends(AgreementService)]


@agreement_router.post("/{agreement_id}/close", tags=["agreement"])
async def close_agreement(agreement_id: int, agreement_service: AgreementServiceBase):
    """
    Close agreement
    """
    try:
        await agreement_service.close_agreement(agreement_id)
    except AgreementNotFound:
        return JSONResponse(content={"message": "Agreement not found"}, status_code=404)

    return JSONResponse(content={"message": "Agreement was closed"}, status_code=200)


@agreement_router.post("/", tags=["agreement"])
async def put_agreement(request: RequestModel, agreement_service: AgreementServiceBase):
    """
    Put agreement to table agreement
    """
    try:
        id_agreement, id_client = await agreement_service.put_agreement(request)
        return JSONResponse(content={"Agreement_id": f"{id_agreement}", "Client_id": f"{id_client}"}, status_code=200)
    except IncorrectInterest:
        return JSONResponse(content={"message": "interest is incorrect"}, status_code=400)
    except IncorrectTerm:
        return JSONResponse(content={"message": "term is incorrect"}, status_code=400)
    except IncorrectPrincipal:
        return JSONResponse(content={"message": "principal is incorrect"}, status_code=400)
    except ProductNotFound:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    except Exception as ex:
        print(ex)


@agreement_router.get("/client/{client_id}", tags=["agreement"])
async def get_client_agreements(client_id: int, agreement_service: AgreementServiceBase):
    """
    Get all client's agreements 
    """
    agreements = await agreement_service.get_all_agreements(client_id)

    return agreements
