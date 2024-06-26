from fastapi import FastAPI
from fastapi.responses import JSONResponse

from contextlib import asynccontextmanager

import asyncio

from kafka.kafka_producer import kafka_producer
from kafka.kafka_consumer import origination_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):
    await kafka_producer.create_producer()
    await origination_consumer.create_consumer()

    asyncio.create_task(origination_consumer.consume())
    yield
    await kafka_producer.stop_producer()
    await origination_consumer.stop()


app = FastAPI(lifespan=lifespan)


@app.get("/check")
async def check():
    return JSONResponse(content={"message": "ok"}, status_code=200)
