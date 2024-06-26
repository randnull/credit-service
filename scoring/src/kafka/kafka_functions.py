import json

from kafka.kafka_producer import kafka_producer
from common.kafka.producer import Producer

from functions.scoring_functions import scoring

from config.settings import settings


async def scoring_client(msg):
    data = json.loads(msg.value.decode('utf-8'))

    client_id = data["client_id"]
    agreement_id = data["agreement_id"]

    try:
        scoring_result = await scoring(client_id)

        scoring_response = {
            "result": scoring_result,
            "agreement_id": agreement_id
        }
        
        async with kafka_producer.producer_session() as producer:
            await Producer.send_to_kafka(producer, scoring_response, settings.KAFKA_PRODUCER_TOPIC)
        
    except Exception as ex:
        print(ex)
