from common.generic_repository.generic_repo import Repository
from common.database_connection.base import async_session

from models.dao_table.dao import SchedulePayment
from models.dto_table.dto import SchedulePaymentModel, SchedulePaymentIdModel

from dateutil.parser import parse


async def add_schedule(schedule_data: SchedulePaymentModel) -> None:
    async with async_session() as session:
        schedule_repository = Repository[SchedulePayment](SchedulePayment, session)

        await schedule_repository.add(schedule_data)


async def set_paid(schedule_id):
    async with async_session() as session:
        schedule_repository = Repository[SchedulePayment](SchedulePayment, session)

        await schedule_repository.update_val(schedule_id, "payment_status", "Paid")


async def update_payment_sum(schedule_id: int,
                            principal_payment: float, 
                            interest_payment: float,
                            prev_payment_sum: float,
                            payment_sum: float):

    async with async_session() as session:
        schedule_repository = Repository[SchedulePayment](SchedulePayment, session)

        await schedule_repository.update_val(
            schedule_id, 
            "payment_sum", 
            min(principal_payment + interest_payment, prev_payment_sum + payment_sum)
        )


async def add_payment(agreement_id: int, payment_date: str, payment_sum: int):
    async with async_session() as session:
        schedule_repository = Repository[SchedulePayment](SchedulePayment, session)
        
        schedules = await schedule_repository.get_by_value("agreement_id", agreement_id)
        
    datetime_format_payment_date = parse(payment_date)

    dto_models = list()

    for schedule in schedules:
        dto_schedule = SchedulePaymentIdModel.to_dto(schedule)

        dto_schedule.payment_date = dto_schedule.payment_date.timestamp() - datetime_format_payment_date.timestamp()

        if dto_schedule.payment_date > 0:
            dto_models.append(dto_schedule)

    dto_models.sort(key=lambda x: x.payment_date)

    if len(dto_models) == 0:
        return

    save_model = dto_models[0]

    prev_payment_sum = save_model.payment_sum

    current_payment_sum = save_model.principal_payment + save_model.interest_payment - prev_payment_sum - payment_sum

    await update_payment_sum(save_model.id_schedule, save_model.principal_payment, save_model.interest_payment, prev_payment_sum, payment_sum)

    if current_payment_sum < 0.0000001:
        await set_paid(save_model.id_schedule)

    if current_payment_sum < 0:
        for schedule_index in range(1, len(dto_models)):
            next_schedule = dto_models[schedule_index]

            await update_payment_sum(next_schedule.id_schedule, next_schedule.principal_payment, next_schedule.interest_payment, next_schedule.payment_sum, -current_payment_sum)

            current_payment_sum = next_schedule.principal_payment + next_schedule.interest_payment - next_schedule.payment_sum + current_payment_sum

            if current_payment_sum < 0.0000001:
                await set_paid(next_schedule.id_schedule)
                if schedule_index == len(dto_models) - 1:
                    return True

            if current_payment_sum > 0:
                break
    
    return False


async def get_future_payments():
    async with async_session() as session:
        schedule_repository = Repository[SchedulePayment](SchedulePayment, session)

        future_payments = await schedule_repository.get_by_value("payment_status", "Future")

    return future_payments


async def set_overdue(schedule_id):
    async with async_session() as session:
        schedule_repository = Repository[SchedulePayment](SchedulePayment, session)

        await schedule_repository.update_val(schedule_id, "payment_status", "Overdue")
