from common.kafka.consumer import Consumer
from config.settings import settings

from kafka.kafka_functions import scoring_client


BOOTSTRAP_SERVER = f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}'
ORIGINATION_TOPIC = settings.KAFKA_CONSUMER_TOPIC
GROUP_ID = settings.KAFKA_GROUP_ID


origination_consumer = Consumer(ORIGINATION_TOPIC, BOOTSTRAP_SERVER, GROUP_ID, scoring_client)
