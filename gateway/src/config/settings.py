from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    ORIGINATION_HOST: str = os.environ['ORIGINATION_HOST']
    ORIGINATION_PORT: int = int(os.environ['ORIGINATION_PORT'])
    PRODUCT_ENGINE_HOST: str = os.environ['PRODUCT_ENGINE_HOST']
    PRODUCT_ENGINE_PORT: int = int(os.environ['PRODUCT_ENGINE_PORT'])


settings = Settings()
