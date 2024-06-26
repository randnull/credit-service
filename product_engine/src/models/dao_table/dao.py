from sqlalchemy import Column, Integer, String, DateTime, Float
from common.database_connection.base import Base


class Product(Base):
    __tablename__ = "product"

    id_product = Column(Integer, autoincrement=True, primary_key=True, index=True)
    code = Column(String)
    title = Column(String)
    min_term = Column(Integer)
    max_term = Column(Integer)
    min_principal = Column(Integer)
    max_principal = Column(Integer)
    min_interest = Column(Integer)
    max_interest = Column(Integer)
    min_origination = Column(Integer)
    max_origination = Column(Integer)

    @classmethod
    def to_dao(cls, product_dto):
        return Product(
            code=product_dto.code,
            title=product_dto.title,
            min_term=product_dto.min_term,
            max_term=product_dto.max_term,
            min_principal=product_dto.min_principal,
            max_principal=product_dto.max_principal,
            min_interest=product_dto.min_interest,
            max_interest=product_dto.max_interest,
            min_origination=product_dto.min_origination,
            max_origination=product_dto.max_origination
        )


class Agreement(Base):
    __tablename__ = "agreement"

    id_agreement = Column(Integer, autoincrement=True, primary_key=True, index=True)
    product_code = Column(String)
    client_id = Column(Integer)
    principal = Column(Integer)
    term = Column(Integer)
    origination = Column(Integer)
    interest = Column(Float)
    create_datetime = Column(DateTime)
    status = Column(String)

    @classmethod
    def to_dao(cls, agreement_dto):
        return Agreement(
            product_code=agreement_dto.product_code,
            client_id=agreement_dto.client_id,
            principal=agreement_dto.principal,
            term=agreement_dto.term,
            origination=agreement_dto.origination,
            interest=agreement_dto.interest,
            create_datetime=agreement_dto.create_datetime,
            status=agreement_dto.status,
        )


class SchedulePayment(Base):
    __tablename__ = "schedule_payment"

    id_schedule = Column(Integer, autoincrement=True, primary_key=True, index=True)
    agreement_id = Column(Integer)
    payment_date = Column(DateTime)
    principal_payment = Column(Float)
    interest_payment = Column(Float)
    payment_sum = Column(Float)
    payment_number = Column(Integer)
    payment_status = Column(String)

    @classmethod
    def to_dao(cls, schedule_dto):
        return SchedulePayment(
            agreement_id=schedule_dto.agreement_id,
            payment_date=schedule_dto.payment_date,
            principal_payment=schedule_dto.principal_payment,
            interest_payment=schedule_dto.interest_payment,
            payment_sum=schedule_dto.payment_sum,
            payment_number=schedule_dto.payment_number,
            payment_status=schedule_dto.payment_status
        )


class Client(Base):
    __tablename__ = "client"

    id_client = Column(Integer, autoincrement=True, primary_key=True, index=True)
    first_name = Column(String)
    second_name = Column(String)
    third_name = Column(String)
    birthday = Column(String)
    phone_number = Column(String)
    client_email = Column(String)
    passport_data = Column(String)
    salary = Column(Integer)

    @classmethod
    def to_dao(cls, client_dto):
        return Client(
            first_name=client_dto.first_name,
            second_name=client_dto.second_name,
            third_name=client_dto.third_name,
            birthday=client_dto.birthday,
            phone_number=client_dto.phone_number,
            client_email=client_dto.client_email,
            passport_data=client_dto.passport_data,
            salary=client_dto.salary
        )
