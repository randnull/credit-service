from pydantic import BaseModel
import datetime


class ApplicationModel(BaseModel):
    client_id: int
    principal: int
    agreement_id: int
    product_code: str
    create_datetime: datetime.datetime
    status: str

    @classmethod
    def to_dto(cls, application_dao):
        return ApplicationModel(
            client_id=application_dao.client_id,
            principal=application_dao.principal,
            agreement_id=application_dao.agreement_id,
            product_code=application_dao.product_code,
            create_datetime=application_dao.create_datetime,
            status=application_dao.status
        )

    @classmethod
    def to_dto_from_request(cls, application_request_dto):
        return ApplicationModel(
            client_id=application_request_dto.client_id,
            principal=application_request_dto.principal,
            agreement_id=application_request_dto.agreement_id,
            product_code=application_request_dto.product_code,
            create_datetime=datetime.datetime.now(),
            status="New"
        )
    
    

class ApplicationRequestModel(BaseModel):
    client_id: int
    principal: int
    agreement_id: int
    product_code: str
