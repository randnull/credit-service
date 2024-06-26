from fastapi import Depends

import httpx

from config.settings import settings

from common.generic_repository.repo_connection import get_repository

from models.dao_table.dao import Application
from models.dto_table.dto import ApplicationRequestModel, ApplicationModel


from common.errors.errors import *


class ApplicationService:
    def __init__(self, application_repository = Depends(get_repository(Application))) -> None:
        self.__application_repository = application_repository


    async def add_application(self, application_request: ApplicationRequestModel):
        check_for_agreement = await self.__application_repository.get_one_by_value("agreement_id", 
                                                                                   application_request.agreement_id)

        if check_for_agreement is not None:
            return {
                "id": check_for_agreement.id_application, 
                "status": check_for_agreement.status, 
                "code": 200
                }
           
        id = await self.__application_repository.add(application_request)

        req_applications = await self.__application_repository.get_by_values({"client_id": application_request.client_id,
                                                                              "product_code": application_request.product_code})

        applications_time = []

        for application in req_applications:
            applications_time.append(int(ApplicationModel.to_dto(application).create_datetime.timestamp()))

        if len(applications_time) <= 1:
            return {
                "id": id, 
                "status": "New", 
                "code": 200
                }

        applications_time.sort(reverse=True)

        if applications_time[0] - applications_time[1] <= settings.SECOND_DELAY_REPEAT_CREATING:
            await self.__application_repository.update_value(id, "status", "Closed")
            
            return {
                "id": id, 
                "status": "Closed", 
                "code": 409
                }

        return {
            "id": id, 
            "status": "New", 
            "code": 200
            }


    async def close_application(self, agreement_id: int):
            is_id_exist = await self.__application_repository.get_one_by_value("agreement_id", agreement_id)

            if is_id_exist is None:
                raise ApplicationNotFound

            is_all_paid = 'False'

            try:
                async with httpx.AsyncClient() as client:
                    response = await client.get(f"http://{settings.PRODUCT_ENGINE_HOST}:{settings.PRODUCT_ENGINE_PORT}/schedule/paid/{agreement_id}")

                json_resp = response.json()

                is_all_paid = json_resp["result"]

            except Exception as ex:
                print(ex)
                return ServerCloseError

            if is_all_paid == 'False':
                raise TryCloseWhileFuture

            await self.__application_repository.update_value_not_id("agreement_id", agreement_id, "status", "Closed")

            try:
                async with httpx.AsyncClient() as client:
                    response = await client.post(f"http://{settings.PRODUCT_ENGINE_HOST}:{settings.PRODUCT_ENGINE_PORT}/agreement/{agreement_id}/close")
            except Exception as ex:
                print(ex)

            return {"status" : 200}
