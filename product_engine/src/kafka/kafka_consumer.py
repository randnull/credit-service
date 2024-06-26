from common.kafka.consumer import Consumer
from config.settings import settings

from kafka.kafka_functions import create_schedule, get_payment

BOOTSTRAP_SERVER = f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}'
SCORING_TOPIC = settings.KAFKA_SCORING_CONSUMER_TOPIC
SCORING_GROUP_ID = settings.KAFKA_SCORING_GROUP_ID
PAYMENT_TOPIC = settings.KAFKA_PAYMENT_CONSUMER_TOPIC
PAYMENT_GROUP_ID = settings.KAFKA_PAYMENT_GROUP_ID


scoring_consumer = Consumer(SCORING_TOPIC, BOOTSTRAP_SERVER, SCORING_GROUP_ID, create_schedule)

payment_consumer = Consumer(PAYMENT_TOPIC, BOOTSTRAP_SERVER, PAYMENT_GROUP_ID, get_payment)
