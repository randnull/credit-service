from common.kafka.consumer import Consumer
from config.settings import settings

from kafka.kafka_functions import create_new_application
from kafka.kafka_functions import get_scoring_result


BOOTSTRAP_SERVER = f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}'
AGREEMENT_TOPIC = settings.KAFKA_ORIGINATION_CONSUMER_TOPIC
SCORING_TOPIC = settings.KAFKA_SCORING_CONSUMER_TOPIC
SCORING_GROUP_ID = settings.KAFKA_SCORING_GROUP_ID
AGREEMENT_GROUP_ID = settings.KAFKA_ORIGINATION_GROUP_ID


agreement_consumer = Consumer(AGREEMENT_TOPIC, BOOTSTRAP_SERVER, AGREEMENT_GROUP_ID, create_new_application)

scoring_consumer = Consumer(SCORING_TOPIC, BOOTSTRAP_SERVER, SCORING_GROUP_ID, get_scoring_result)
