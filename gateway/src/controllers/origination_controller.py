from fastapi import APIRouter
from fastapi.responses import JSONResponse

import requests

import httpx

from config.settings import settings


origination_router = APIRouter()


@origination_router.post("/application/{agreement_id}/close", tags=["origination"])
async def close_application(agreement_id: int):
   '''
   Close application
   '''
   link = f"http://{settings.ORIGINATION_HOST}:{settings.ORIGINATION_PORT}/application/{agreement_id}/close"
   
   async with httpx.AsyncClient(follow_redirects=True) as client:
      try:
         answer = await client.post(link)
         answer_content = answer.json()
         return JSONResponse(content={"message": answer_content}, status_code=answer.status_code)
      except httpx.RequestError:
         return JSONResponse(content={"message": "Service not available"}, status_code=503)
