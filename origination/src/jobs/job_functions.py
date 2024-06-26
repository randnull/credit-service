from config.settings import settings

from functions.application_functions import get_all_new_status, update_status, get_all_with_status

from kafka.kafka_producer import kafka_producer
from common.kafka.producer import Producer


async def job_scoring():
    application_new_status = await get_all_new_status()

    for application in application_new_status:
        data_to_scoring = {
            "client_id": application.client_id,
            "agreement_id": application.agreement_id
        }

        async with kafka_producer.producer_session() as producer:
            await Producer.send_to_kafka(producer, data_to_scoring, settings.KAFKA_SCORING_PRODUCER_TOPIC)

        await update_status(application.agreement_id, "Scoring")


async def job_check_approved():
    application_approved_status = await get_all_with_status("Approved")

    for application in application_approved_status:
        data_to_payment = {
            "client_id": application.client_id,
            "principal": application.principal
        }

        async with kafka_producer.producer_session() as producer:
            await Producer.send_to_kafka(producer, data_to_payment, settings.KAFKA_PAYMENT_OPERATIONS_TOPIC)

        await update_status(application.agreement_id, "Closed")
