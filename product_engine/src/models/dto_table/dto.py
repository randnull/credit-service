from pydantic import BaseModel
import datetime

class ProductModel(BaseModel):
    code: str
    title: str
    min_term: int
    max_term: int
    min_principal: int
    max_principal: int
    min_interest: int
    max_interest: int
    min_origination: int
    max_origination: int

    @classmethod
    def to_dto(cls, product_dao):
        return ProductModel(
            code=product_dao.code,
            title=product_dao.title,
            min_term=product_dao.min_term,
            max_term=product_dao.max_term,
            min_principal=product_dao.min_principal,
            max_principal=product_dao.max_principal,
            min_interest=product_dao.min_interest,
            max_interest=product_dao.max_interest,
            min_origination=product_dao.min_origination,
            max_origination=product_dao.max_origination
        )


class AgreementModel(BaseModel):
    product_code: str
    client_id: int
    principal: int
    term: int
    origination: int
    interest: int
    create_datetime: datetime.datetime
    status: str

    @classmethod
    def to_dto_from_request(cls, request, id_client, origination_value):
        return AgreementModel(
            product_code=request.product_code,
            client_id=id_client,
            principal=request.disbursment_amount + origination_value,
            term=request.term,
            origination=origination_value,
            interest=request.interest,
            create_datetime=datetime.datetime.now(),
            status="New"
        )

    @classmethod
    def to_dto(cls, agreement_dao):
        return AgreementModel(
            product_code=agreement_dao.product_code,
            client_id=agreement_dao.client_id,
            principal=agreement_dao.principal,
            term=agreement_dao.term,
            origination=agreement_dao.origination,
            interest=agreement_dao.interest,
            create_datetime=agreement_dao.create_datetime,
            status=agreement_dao.status
        )


class AgreementIdModel(BaseModel):
    id_agreement: int
    product_code: str
    client_id: int
    principal: int
    term: int
    origination: int
    interest: int
    create_datetime: datetime.datetime
    status: str

    @classmethod
    def to_dto(cls, agreement_dao):
        return AgreementIdModel(
            id_agreement=agreement_dao.id_agreement,
            product_code=agreement_dao.product_code,
            client_id=agreement_dao.client_id,
            principal=agreement_dao.principal,
            term=agreement_dao.term,
            origination=agreement_dao.origination,
            interest=agreement_dao.interest,
            create_datetime=agreement_dao.create_datetime,
            status=agreement_dao.status
        )


class SchedulePaymentModel(BaseModel):
    agreement_id: int
    payment_date: datetime.datetime
    principal_payment: float
    interest_payment: float
    payment_sum: float
    payment_number: int
    payment_status: str

    @classmethod
    def to_dto(cls, schedule_dao):
        return SchedulePaymentModel(
            agreement_id=schedule_dao.agreement_id,
            payment_date=schedule_dao.payment_date,
            principal_payment=schedule_dao.principal_payment,
            interest_payment=schedule_dao.interest_payment,
            payment_sum=schedule_dao.payment_sum,
            payment_number=schedule_dao.payment_number,
            payment_status=schedule_dao.payment_status
        )


class SchedulePaymentIdModel(BaseModel):
    id_schedule: int
    agreement_id: int
    payment_date: datetime.datetime
    principal_payment: float
    interest_payment: float
    payment_sum: float
    payment_number: int
    payment_status: str

    @classmethod
    def to_dto(cls, schedule_dao):
        return SchedulePaymentIdModel(
            id_schedule=schedule_dao.id_schedule,
            agreement_id=schedule_dao.agreement_id,
            payment_date=schedule_dao.payment_date,
            principal_payment=schedule_dao.principal_payment,
            interest_payment=schedule_dao.interest_payment,
            payment_sum=schedule_dao.payment_sum,
            payment_number=schedule_dao.payment_number,
            payment_status=schedule_dao.payment_status
        )


class ClientModel(BaseModel):
    first_name: str
    second_name: str
    third_name: str
    birthday: str
    phone_number: str
    client_email: str
    passport_data: str
    salary: int
    
    @classmethod
    def to_dto_from_request(cls, request):
        return ClientModel(
            first_name=request.first_name,
            second_name=request.second_name,
            third_name=request.third_name,
            birthday=request.birthday,
            phone_number=request.phone_number,
            client_email=request.client_email,
            passport_data=request.passport_data,
            salary=request.salary
        )


class DatetimeModel(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int
