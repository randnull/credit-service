import json

from functions.application_functions import create_application, update_status, check_if_closed

from models.dto_table.dto import ApplicationRequestModel


async def create_new_application(msg):
    data = json.loads(msg.value.decode('utf-8'))

    new_application = ApplicationRequestModel(
        client_id=data["client_id"],
        principal=data["principal"],
        agreement_id=data["agreement_id"],
        product_code=data["product_code"]
    )

    await create_application(new_application)


async def get_scoring_result(msg):
    data = json.loads(msg.value.decode('utf-8'))

    agreement_id = data["agreement_id"]
    bool_scoring_result = data["result"]

    if bool_scoring_result:
        is_closed = await check_if_closed(agreement_id)

        if not is_closed:
            await update_status(agreement_id, "Approved")
    else:
        await update_status(agreement_id, "Closed")
