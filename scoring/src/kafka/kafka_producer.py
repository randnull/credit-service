from common.kafka.producer import Producer
from config.settings import settings


BOOTSTRAP_SERVER = f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}'

kafka_producer = Producer(BOOTSTRAP_SERVER)
