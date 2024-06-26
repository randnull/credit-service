from sqlalchemy import Column, Integer, String, DateTime
from common.database_connection.base import Base
import datetime

class Application(Base):
    __tablename__ = "application"

    id_application = Column(Integer, autoincrement=True, primary_key=True, index=True)
    client_id = Column(Integer)
    principal = Column(Integer)
    agreement_id = Column(Integer)
    product_code = Column(String)
    create_datetime = Column(DateTime)
    status = Column(String)

    @classmethod
    def to_dao(cls, application_dto):
        return Application(
            client_id=int(application_dto.client_id),
            principal=int(application_dto.principal),
            agreement_id=int(application_dto.agreement_id),
            product_code=application_dto.product_code,
            create_datetime=application_dto.create_datetime,
            status=application_dto.status
        )
