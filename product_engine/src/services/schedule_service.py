from fastapi import Depends

from common.generic_repository.repo_connection import get_repository
from models.dao_table.dao import SchedulePayment
from models.dto_table.dto import SchedulePaymentModel


class ScheduleService:
    def __init__(self, schedule_repository = Depends(get_repository(SchedulePayment))):
        self.__schedule_repository = schedule_repository

    async def get_schedule(self, agreement_id: int):
        client_schedules = await self.__schedule_repository.get_by_value("agreement_id", agreement_id)

        schedules = []

        for schedule in client_schedules:
            schedules.append(SchedulePaymentModel.to_dto(schedule))

        schedules.sort(key=lambda x: x.payment_number)

        return schedules


    async def check_if_all_paid(self, agreement_id: int) -> bool:
        client_schedules = await self.__schedule_repository.get_by_value("agreement_id", agreement_id)

        for schedule in client_schedules:
            if schedule.payment_status == "Future":
                return False
        return True
