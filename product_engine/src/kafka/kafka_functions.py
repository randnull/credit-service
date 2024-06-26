import json
import datetime

from functions.schedule_functions import add_schedule, add_payment
from functions.generate_schedule import generate_schedule

from functions.agreement_functions import get_agreement_by_id, update_status

from models.dao_table.dao import Agreement
from models.dto_table.dto import SchedulePaymentModel

from typing import Dict


async def create_schedule(msg):
    data = json.loads(msg.value.decode('utf-8'))

    agreement_id: int = data["agreement_id"]

    if not data["result"]:
        await update_status(agreement_id, "Closed")
        return

    agreement: Agreement = await get_agreement_by_id(agreement_id)

    if agreement.status == 'Closed':
        return

    await update_status(agreement_id, "Active")

    schedules: Dict = generate_schedule(agreement.term, datetime.datetime.now(), agreement.interest, agreement.principal)

    for period in schedules:
        schedule = schedules[period]
            
        schedule_data = SchedulePaymentModel(
            agreement_id=agreement_id,
            payment_date=schedule["payment_date"],
            principal_payment=schedule["principal_payment"],
            interest_payment=schedule["interest_payment"],
            payment_sum=0,
            payment_number=period,
            payment_status="Future"
        )

        await add_schedule(schedule_data)


async def get_payment(msg):
    data = json.loads(msg.value.decode('utf-8'))
    
    date_time: str = data["date"]
    agreement_id: int = int(data["agreement_id"])
    payment: int = int(data["payment"])

    is_all_paid = await add_payment(agreement_id, date_time, payment)

    if is_all_paid:
        await update_status(agreement_id, "Closed")

    #comment
