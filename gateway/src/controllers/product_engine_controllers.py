from fastapi import APIRouter
from fastapi.responses import JSONResponse

import requests

from config.settings import settings

from common.shared_models.dto_models.request_model import RequestModel


pe_router = APIRouter()


@pe_router.get("/product", tags=["product_engine"])
async def get_products():
   '''
   Get all products
   '''
   try:
      answer = requests.get(f"http://{settings.PRODUCT_ENGINE_HOST}:{settings.PRODUCT_ENGINE_PORT}/product")
      answer_content = answer.json()
      return JSONResponse(content={"message": answer_content}, status_code=answer.status_code)
   except:
      return JSONResponse(content={"message": "Servise not available"}, status_code=503)

@pe_router.get("/product/{product_code}", tags=["product_engine"])
async def get_product_by_code(product_code: str):
   '''
   Get product by code
   '''
   try:
      answer = requests.get(f"http://{settings.PRODUCT_ENGINE_HOST}:{settings.PRODUCT_ENGINE_PORT}/product/{product_code}")
      answer_content = answer.json()
      return JSONResponse(content={"message": answer_content}, status_code=answer.status_code)
   except:
      return JSONResponse(content={"message": "Servise not available"}, status_code=503)

@pe_router.post("/agreement", tags=["product_engine"])
async def add_agreement(request: RequestModel):
   '''
   Add new agreement
   '''
   try:
      answer = requests.post(f"http://{settings.PRODUCT_ENGINE_HOST}:{settings.PRODUCT_ENGINE_PORT}/agreement", json=request.dict())
      answer_content = answer.json()
      return JSONResponse(content={"message": answer_content}, status_code=answer.status_code)
   except:
      return JSONResponse(content={"message": "Servise not available"}, status_code=503)


@pe_router.get("/schedule/{agreement_id}", tags=["schedule"])
async def get_schedule(agreement_id: int):
   '''
   Get schedule by agreement_id
   '''
   try:
      answer = requests.get(f"http://{settings.PRODUCT_ENGINE_HOST}:{settings.PRODUCT_ENGINE_PORT}/schedule/{agreement_id}")
      answer_content = answer.json()
      return answer_content
   except:
      return JSONResponse(content={"message": "Servise not available"}, status_code=503)


@pe_router.get("/agreements/client/{client_id}", tags=["product_engine"])
async def get_agreements(client_id: int):
   '''
   Get agrements by clint_id
   '''
   try:
      answer = requests.get(f"http://{settings.PRODUCT_ENGINE_HOST}:{settings.PRODUCT_ENGINE_PORT}/agreement/client/{client_id}")
      answer_content = answer.json()
      return answer_content
   except:
      return JSONResponse(content={"message": "Servise not available"}, status_code=503)
