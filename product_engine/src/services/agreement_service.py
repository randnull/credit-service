from fastapi import Depends

from common.errors.errors import *

from common.generic_repository.repo_connection import get_repository
from kafka.kafka_producer import get_producer

from common.kafka.producer import Producer

from config.settings import settings

from services.product_service import ProductService
from services.client_service import ClientService

from models.dao_table.dao import Agreement
from models.dto_table.dto import ProductModel, AgreementModel, AgreementIdModel
from common.shared_models.dto_models.request_model import RequestModel

import random


class AgreementService:
    def __init__(self,
                agreement_repository = Depends(get_repository(Agreement)),
                product_service: ProductService = Depends(ProductService),
                client_service: ClientService = Depends(ClientService),
                kafka_producer = Depends(get_producer)):

        self.__agreement_repository = agreement_repository
        self.__product_service = product_service
        self.__client_service = client_service
        self.__kafka_producer = kafka_producer

    
    async def get_all_agreements(self, client_id: int):
        agreements = await self.__agreement_repository.get_by_value("client_id", client_id)
        
        agreements_dto = []

        for agreement in agreements:
            agreements_dto.append(AgreementIdModel.to_dto(agreement))

        return agreements_dto


    async def close_agreement(self, agreement_id: int):
        is_exist = await self.__agreement_repository.get_by_id(agreement_id)

        if is_exist is None:
            raise AgreementNotFound

        await self.__agreement_repository.update_status(agreement_id, "Closed")


    async def put_agreement(self, request: RequestModel):
        req_product = await self.__product_service.get_product_by_code(request.product_code)

        if req_product is None:
            raise ProductNotFound

        product = ProductModel.to_dto(req_product)

        if not (product.min_term <= request.term <= product.max_term):
            raise IncorrectTerm

        if not (product.min_interest <= request.interest <= product.max_interest):
            raise IncorrectInterest
        
        if not (product.min_principal <= request.disbursment_amount <= product.max_principal):
            raise IncorrectPrincipal
        
        id_client = await self.__client_service.get_client_id(request)

        origination_value = random.randint(product.min_origination, product.max_origination)

        new_agreement = AgreementModel.to_dto_from_request(request, id_client, origination_value)

        id_agreement = await self.__agreement_repository.add(new_agreement)

        data_to_origination = {
            "client_id": id_client, 
            "principal": new_agreement.principal, 
            "agreement_id": id_agreement, 
            "product_code": new_agreement.product_code
        }

        await Producer.send_to_kafka(self.__kafka_producer, data_to_origination, settings.KAFKA_ORIGINATION_PRODUCER_TOPIC)

        return id_agreement, id_client
