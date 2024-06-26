from pydantic import BaseModel


class RequestModel(BaseModel):
    product_code: str
    first_name: str
    second_name: str
    third_name: str
    birthday: str
    passport_data: str
    client_email: str
    phone_number: str
    salary: int
    term: int
    interest: int
    disbursment_amount: int
