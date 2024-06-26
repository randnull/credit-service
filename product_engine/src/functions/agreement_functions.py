from common.generic_repository.generic_repo import Repository
from common.database_connection.base import async_session
from models.dao_table.dao import Agreement


async def get_all_new_status():
    async with async_session() as session:
        agreement_repository = Repository[Agreement](Agreement, session)
        agreements = await agreement_repository.get_by_value("status", "New")

    return agreements


async def update_status(agreement_id: int, new_status: str) -> None:
    async with async_session() as session:
        agreement_repository = Repository[Agreement](Agreement, session)

        await agreement_repository.update_status(agreement_id, new_status)


async def get_agreement_by_id(agreement_id: int) -> Agreement:
    async with async_session() as session:
        agreement_repository = Repository[Agreement](Agreement, session)

        agreement: Agreement = await agreement_repository.get_by_id(agreement_id)
    
    return agreement
