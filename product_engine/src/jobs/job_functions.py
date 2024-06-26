import requests

from functions.agreement_functions import get_all_new_status, update_status, get_agreement_by_id
from functions.schedule_functions import get_future_payments, set_overdue

import datetime
from pytz import timezone

from config.settings import settings

from kafka.kafka_producer import kafka_producer
from common.kafka.producer import Producer


async def send_to_origination():
    dao_models = await get_all_new_status()

    request_list = []

    for dao in dao_models:
        data_to_origination = {
            "client_id": dao.client_id, 
            "principal": dao.principal, 
            "agreement_id": dao.id_agreement, 
            "product_code": dao.product_code
        }

        request_list.append(data_to_origination)


    for request_form in request_list:
        async with kafka_producer.producer_session() as producer:
                await Producer.send_to_kafka(producer, request_form, settings.KAFKA_ORIGINATION_PRODUCER_TOPIC)


async def check_overdue():
    if settings.USE_CUSTOM_DATETIME:
        current_datetime = settings.CUSTOM_DATETIME
    else:
        current_datetime = datetime.datetime.now()

    current_datetime = current_datetime.astimezone(timezone('UTC'))

    dao_models = await get_future_payments()

    for dao in dao_models:
        if dao.payment_date.timestamp() < current_datetime.timestamp():
            await set_overdue(dao.id_schedule)

            agreement = await get_agreement_by_id(dao.agreement_id)

            customer_id = agreement.client_id
        
            overdue_data_kafka = {
                "agreement_id": dao.agreement_id,
                "overdue_date": str(dao.payment_date.isoformat()),
                "payment": dao.principal_payment + dao.interest_payment,
                "customer_id": customer_id
            }

            async with kafka_producer.producer_session() as producer:
                await Producer.send_to_kafka(producer, overdue_data_kafka, settings.KAFKA_OVERDUE_TOPIC)
