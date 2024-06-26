from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    PRODUCT_ENGINE_HOST: str = os.environ['PRODUCT_ENGINE_HOST']
    PRODUCT_ENGINE_PORT: str = os.environ['PRODUCT_ENGINE_PORT']
    KAFKA_HOST: str = os.environ['KAFKA_HOST']
    KAFKA_PORT: str = os.environ['KAFKA_PORT']
    KAFKA_PRODUCER_TOPIC: str = os.environ['KAFKA_PRODUCER_TOPIC']
    KAFKA_CONSUMER_TOPIC: str = os.environ['KAFKA_CONSUMER_TOPIC']
    KAFKA_GROUP_ID: str = os.environ['KAFKA_GROUP_ID']


settings = Settings()
