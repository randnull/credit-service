from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    PRODUCT_ENGINE_HOST: str = os.environ['PRODUCT_ENGINE_HOST']
    PRODUCT_ENGINE_PORT: int = int(os.environ['PRODUCT_ENGINE_PORT'])
    SCORING_HOST: str = os.environ['SCORING_HOST']
    SCORING_PORT: int = int(os.environ['SCORING_PORT'])
    SECOND_DELAY_REPEAT_CREATING: int = 20
    SECONDS_DELAY_SCHEDULE: int = int(os.environ['SECONDS_DELAY_SCHEDULE'])
    SECONDS_DELAY_SCHEDULE_APPROVED: int = int(os.environ['SECONDS_DELAY_SCHEDULE_APPROVED'])
    DB_LOGIN: str = os.environ['DB_LOGIN']
    DB_PASSWORD: str = os.environ['DB_PASSWORD']
    DB_HOST: str = os.environ['DB_HOST']
    DB_NAME: str = os.environ['DB_NAME']
    KAFKA_HOST: str = os.environ['KAFKA_HOST']
    KAFKA_PORT: int = int(os.environ['KAFKA_PORT'])
    KAFKA_ORIGINATION_CONSUMER_TOPIC: str = os.environ['KAFKA_ORIGINATION_CONSUMER_TOPIC']
    KAFKA_SCORING_PRODUCER_TOPIC: str = os.environ['KAFKA_SCORING_PRODUCER_TOPIC']
    KAFKA_SCORING_CONSUMER_TOPIC: str = os.environ['KAFKA_SCORING_CONSUMER_TOPIC']
    KAFKA_SCORING_GROUP_ID: str =  os.environ['KAFKA_SCORING_GROUP_ID']
    KAFKA_ORIGINATION_GROUP_ID: str = os.environ['KAFKA_ORIGINATION_GROUP_ID']
    KAFKA_PAYMENT_OPERATIONS_TOPIC: str = os.environ['KAFKA_PAYMENT_OPERATIONS_TOPIC']


settings = Settings()