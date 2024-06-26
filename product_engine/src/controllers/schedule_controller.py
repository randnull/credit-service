from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from common.errors.errors import *

from typing import Annotated

from services.schedule_service import ScheduleService


schedule_router = APIRouter(prefix="/schedule")

ScheduleServiceBase = Annotated[ScheduleService, Depends(ScheduleService)]


@schedule_router.get("/{agreement_id}", tags=["schedule"])
async def get_schedule(agreement_id: int, schedule_service: ScheduleServiceBase):
    """
    Get schedule by agreement_id
    """
    try:
        schedules = await schedule_service.get_schedule(agreement_id)
    except Exception as ex:
        return JSONResponse(content={"message": "schedule not found"}, status_code=404)

    return schedules

@schedule_router.get("/paid/{agreement_id}", tags=["schedule"])
async def get_schedule(agreement_id: int, schedule_service: ScheduleServiceBase):
    """
    Get schedule by agreement_id
    """

    is_all_paid = False

    try:
        is_all_paid = await schedule_service.check_if_all_paid(agreement_id)
    finally:
        pass

    return JSONResponse(content={"result": f"{is_all_paid}"}, status_code=200)
