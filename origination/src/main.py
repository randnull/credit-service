from fastapi import FastAPI
from contextlib import asynccontextmanager

import asyncio
from kafka.kafka_producer import kafka_producer
from kafka.kafka_consumer import agreement_consumer, scoring_consumer


from controllers.application_controller import application_router
from jobs.job import start_scheduler, stop_scheduler


tags = [
    {
        "name": "origination",
        "description": "Operations with origination"
    }
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await kafka_producer.create_producer()

    await agreement_consumer.create_consumer()
    await scoring_consumer.create_consumer()
    
    asyncio.create_task(agreement_consumer.consume())
    asyncio.create_task(scoring_consumer.consume())
    
    await start_scheduler()
    
    yield

    await kafka_producer.stop_producer()
    
    await agreement_consumer.stop()
    await scoring_consumer.stop()
    
    await stop_scheduler()


app = FastAPI(openapi_tags=tags, lifespan=lifespan)

app.include_router(application_router)
