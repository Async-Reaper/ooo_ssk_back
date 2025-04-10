from fastapi import APIRouter, Body, HTTPException, status, Path
from ..utils.utils import add_objects_with_more_info
import math


from .schemas import *
from .actions import *

basket_router = APIRouter(
    tags=["basket"],
    prefix="/api"
)


@basket_router.post('/basket/add_new_position')
async def add_new_position(product_data: BasketInput):
    product = await BasketDAO.checking_availability_of_goods_in_basket(product_data.user_guid, 
                                                                       product_data.contract_guid,
                                                                       product_data.product_guid)
    if product:
        await BasketDAO.update_product_details(**dict(product_data))
        return None

    await BasketDAO.product_creation(**product_data.model_dump())
    return {
        "countBasket": 1
    }

@basket_router.get("/basket/get_all_product_user_by_contract_guid/{user_guid}/{contract_guid}", response_model=BasketOutput)
async def get_all_product_user_by_contract_guid(user_guid: str = Path(..., description="GUID пользователя",
                                                                      min_length=36,
                                                                      max_length=36),
                                                contract_guid: str = Path(..., description="GUID контракта",
                                                                          min_length=36,
                                                                          max_length=36)):
    result = await BasketDAO.get_all_product_user_by_contract_guid(user_guid, contract_guid)

    await add_objects_with_more_info(result)
    # sumOrder = sum([element.other_data.additional_information["price"] * element.count for element in result])
    return {
        "total_count_products": len(result),
        "products": result,
    }

@basket_router.get("/basket/get_info_basket/{user_guid}/{contract_guid}")
async def get_all_product_user_by_contract_guid(user_guid: str = Path(..., description="GUID пользователя",
                                                                      min_length=36,
                                                                      max_length=36),
                                                contract_guid: str = Path(..., description="GUID контракта",
                                                                          min_length=36,
                                                                          max_length=36)):
    result = await BasketDAO.get_all_product_user_by_contract_guid(user_guid, contract_guid)

    await add_objects_with_more_info(result)
    sumOrder = sum([element.other_data.additional_information["price"] * element.count for element in result])
    return {
        "countProduct": len(result),
        "sumOrder": round(sumOrder, 2) if len(result) != 0 else 0,
    }

@basket_router.delete("/basket/deleted_product_from_basket/{user_guid}/{contract_guid}/{product_guid}")
async def deleted_product_from_basket(user_guid: str = Path(..., description="GUID пользователя",
                                                                      min_length=36,
                                                                      max_length=36),
                                    contract_guid: str = Path(..., description="GUID контракта",
                                                                min_length=36,
                                                                max_length=36),
                                    product_guid: str = Path(..., description="GUID товара",
                                                             min_length=36,
                                                             max_length=36)):
    await BasketDAO.deleted_product_from_basket(user_guid, contract_guid, product_guid)
    return {
        "countBasket": 1
    }


@basket_router.delete("/basket/deleted_products_from_basket/{user_guid}/{contract_guid}")
async def deleted_product_from_basket(user_guid: str = Path(..., description="GUID пользователя",
                                                                      min_length=36,
                                                                      max_length=36),
                                    contract_guid: str = Path(..., description="GUID контракта",
                                                                min_length=36,
                                                                max_length=36)):
    await BasketDAO.deleted_products_from_basket(user_guid, contract_guid)