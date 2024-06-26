from pydantic_settings import BaseSettings
import os
from datetime import datetime


class Settings(BaseSettings):
    ORIGINATION_HOST: str = os.environ['ORIGINATION_HOST']
    ORIGINATION_PORT: int = int(os.environ['ORIGINATION_PORT'])
    SECONDS_DELAY_SCHEDULE: int = int(os.environ['SECONDS_DELAY_SCHEDULE'])
    SECONDS_DELAY_SCHEDULE_OVERDUE: int = int(os.environ['SECONDS_DELAY_SCHEDULE_OVERDUE'])
    DB_LOGIN: str = os.environ['DB_LOGIN']
    DB_PASSWORD: str = os.environ['DB_PASSWORD']
    DB_HOST: str = os.environ['DB_HOST']
    DB_NAME: str = os.environ['DB_NAME']
    KAFKA_HOST: str = os.environ['KAFKA_HOST']
    KAFKA_PORT: str = os.environ['KAFKA_PORT']
    KAFKA_ORIGINATION_PRODUCER_TOPIC: str = os.environ['KAFKA_ORIGINATION_PRODUCER_TOPIC']
    KAFKA_SCORING_CONSUMER_TOPIC: str = os.environ['KAFKA_SCORING_CONSUMER_TOPIC']
    KAFKA_SCORING_GROUP_ID: str = os.environ['KAFKA_SCORING_GROUP_ID']
    KAFKA_PAYMENT_CONSUMER_TOPIC: str = os.environ['KAFKA_PAYMENT_CONSUMER_TOPIC']
    KAFKA_PAYMENT_GROUP_ID: str = os.environ['KAFKA_PAYMENT_GROUP_ID']
    KAFKA_OVERDUE_TOPIC: str = os.environ['KAFKA_OVERDUE_TOPIC']
    USE_CUSTOM_DATETIME: bool = False
    CUSTOM_DATETIME: datetime = datetime.now()


settings = Settings()
