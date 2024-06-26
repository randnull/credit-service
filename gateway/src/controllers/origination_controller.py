from fastapi import APIRouter
from fastapi.responses import JSONResponse

import requests

from config.settings import settings


origination_router = APIRouter()


@origination_router.post("/application/{agreement_id}/close", tags=["origination"])
async def close_application(agreement_id: int):
   '''
   Close application
   '''
   try:
      answer = requests.post(f"http://{settings.ORIGINATION_HOST}:{settings.ORIGINATION_PORT}/application/{agreement_id}/close")
      answer_content = answer.json()
      return JSONResponse(content={"message": answer_content}, status_code=answer.status_code)
   except:
      return JSONResponse(content={"message": "Servise not available"}, status_code=503)
