import httpx
import json

from config.settings import settings


async def get_client_information(client_id: int):
    link = f"http://{settings.PRODUCT_ENGINE_HOST}:{settings.PRODUCT_ENGINE_PORT}/agreement/client/{client_id}"

    async with httpx.AsyncClient() as client:
        response = await client.get(link)

        if response.status_code == 200:
            response_data = response.content
            response_data_json = json.loads(response_data.decode('utf-8'))

            return response_data_json


async def scoring(client_id: int):
    agreements = await get_client_information(client_id)

    if agreements is None:
        return True

    count_open_agreements: int = 0

    for agreement in agreements:
        count_open_agreements += (agreement["status"] != "Closed")

    return count_open_agreements == 1
