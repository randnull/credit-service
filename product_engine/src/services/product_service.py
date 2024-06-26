from fastapi import Depends

from common.errors.errors import *

from common.generic_repository.repo_connection import get_repository
from models.dao_table.dao import Product
from models.dto_table.dto import ProductModel


class ProductService:
    def __init__(self, product_repository = Depends(get_repository(Product))):
        self.__product_repository = product_repository

    
    async def get_product(self):
        products = await self.__product_repository.get()

        answer = []

        for product in products:
            answer.append(ProductModel.to_dto(product))

        return answer

    async def get_product_by_code(self, code: str):
        product = await self.__product_repository.get_by_code(code)

        if product is None:
            return None

        answer = ProductModel.to_dto(product)
        return answer


    async def add_product(self, product: ProductModel):
        is_exist = await self.__product_repository.check(product)

        if is_exist:
            raise ProductAldreadyExist

        _ = await self.__product_repository.add(product)


    async def delete_product(self, code: str):
        _ = await self.__product_repository.delete(code)
