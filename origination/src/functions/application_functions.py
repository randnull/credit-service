from common.database_connection.base import async_session
from common.generic_repository.generic_repo import Repository
from models.dto_table.dto import ApplicationModel, ApplicationRequestModel
from models.dao_table.dao import Application

import httpx

import datetime
from pytz import timezone

from config.settings import settings


async def get_all_new_status():
    async with async_session() as session:
        application_repository = Repository[Application](Application, session)

        result = await application_repository.get_by_value(
            "status", "New"
        )

        dto_results = []

        for dao in result:
            dto_results.append(ApplicationModel.to_dto(dao))

        return dto_results


async def get_all_with_status(status: str):
    async with async_session() as session:
        application_repository = Repository[Application](Application, session)

        result = await application_repository.get_by_value(
            "status", status
        )

        dto_results = []

        for dao in result:
            dto_results.append(ApplicationModel.to_dto(dao))

        return dto_results


async def update_status(agreement_id: int, status: str):
    async with async_session() as session:
        application_repository = Repository[Application](Application, session)
        
        is_id_exist = await application_repository.get_by_value(
            "agreement_id", agreement_id
        )

        if not (is_id_exist is None):
            await application_repository.update_value_not_id(
                "agreement_id", agreement_id, 
                "status", status
            )


async def check_if_closed(agreement_id: int):
    async with async_session() as session:
        application_repository = Repository[Application](Application, session)
        
        is_id_exist = await application_repository.get_one_by_value(
            "agreement_id", agreement_id
        )

    if is_id_exist.status == 'Closed':
        return True
    return False


async def create_application(application_request: ApplicationRequestModel):
    async with async_session() as session:
        application_repository = Repository[Application](Application, session)

        check_for_agreement = await application_repository.get_one_by_value(
            "agreement_id", 
            application_request.agreement_id
        )

        if check_for_agreement is not None:
            return

        application_model = ApplicationModel.to_dto_from_request(application_request)

        check_last_attemp_data = {
            "client_id": application_request.client_id,
            "product_code": application_request.product_code
        }

        req_applications = await application_repository.get_by_values(check_last_attemp_data)

        applications_time = []

        for application in req_applications:
            applications_time.append(int(ApplicationModel.to_dto(application).create_datetime.timestamp()))

        if len(applications_time) != 0:
            applications_time.sort(reverse=True)

            time_creating = application_model.create_datetime

            current_datetime = time_creating.astimezone(timezone('UTC'))

            current_datetime = current_datetime.timestamp()

            if current_datetime - applications_time[0] <= settings.SECOND_DELAY_REPEAT_CREATING:
                application_model.status = "Closed"

                try:
                    async with httpx.AsyncClient() as client:
                        response = await client.post(f"http://{settings.PRODUCT_ENGINE_HOST}:{settings.PRODUCT_ENGINE_PORT}/agreement/{application_request.agreement_id}/close")
                except Exception as ex:
                    print(ex)

        await application_repository.add(application_model)
