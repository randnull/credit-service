from fastapi import FastAPI
from contextlib import asynccontextmanager

from controllers.product_controllers import product_router
from controllers.agreement_controllers import agreement_router
from controllers.schedule_controller import schedule_router
from controllers.datetime_controller import datetime_router

from jobs.job import start_scheduler, stop_scheduler

from kafka.kafka_producer import kafka_producer
from kafka.kafka_consumer import scoring_consumer, payment_consumer

import asyncio


tags = [
    {
        "name": "product",
        "description": "Operations with products"
    },
    {
        "name": "agreement",
        "description": "Operations with agreement"
    },
    {
        "name": "schedule",
        "description": "Operations with schedule"
    }
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await kafka_producer.create_producer()

    await scoring_consumer.create_consumer()

    await payment_consumer.create_consumer()

    asyncio.create_task(scoring_consumer.consume())

    asyncio.create_task(payment_consumer.consume())

    await start_scheduler()
    yield
    await scoring_consumer.stop()

    await payment_consumer.stop()
    
    await kafka_producer.stop_producer()

    await stop_scheduler()


app = FastAPI(openapi_tags=tags, lifespan=lifespan) 

app.include_router(product_router)
app.include_router(agreement_router)
app.include_router(schedule_router)
app.include_router(datetime_router)
