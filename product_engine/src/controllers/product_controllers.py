from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import Annotated

from common.errors.errors import *

from models.dto_table.dto import ProductModel
from services.product_service import ProductService


product_router = APIRouter(prefix="/product", tags=["product"])

ProductServiceBase = Annotated[ProductService, Depends(ProductService)]


@product_router.get("/")
async def get_product(product_service: ProductServiceBase):
    """
    Get all products from table product
    """
    products = await product_service.get_product()
    
    return products


@product_router.get("/{code}")
async def get_product_by_code(code: str, product_service: ProductServiceBase) -> ProductModel:
    """
    Get product from table product with using product_code
    """
    product = await product_service.get_product_by_code(code)
    
    if product is None:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)

    return product


@product_router.post("/")
async def add_product(product: ProductModel, product_service: ProductServiceBase):
    """
    Put product to table product
    """

    try:
        await product_service.add_product(product)
    except ProductAldreadyExist:
        return JSONResponse(content={"message": "Product with this code already found"}, status_code=409)

    return JSONResponse(content={"message": "Product was successful added"}, status_code=200)


@product_router.delete("/{code}")
async def delete_product(code: str, product_service: ProductServiceBase):
    """
    Delete product from table product
    """

    _ = await product_service.delete_product(code)

    return JSONResponse(content={"message": "Product was successful deleted"}, status_code=204)
