from fastapi import APIRouter, Body, HTTPException, Response, status, Path, Request, Query
from ..utils.utils import convert_str_to_type, nomenclature_data_distribution_manager, add_objects_with_pictures
from ..contract.actions import ContractDAO
from ..contract.schemas import ContractInput
from ..utils.utils import add_objects_with_more_info

from .schemas import *
from .actions import *

favorite_router = APIRouter(
    prefix="/api",
    tags=["favorite"]
)

@favorite_router.post("/create_favorite")
async def create_favorite(product_data: FavoriteInput = Body(..., description="Данные для карточки товара")):
    await FavoriteDAO.favorite_creation(**product_data.model_dump())

@favorite_router.get("/get_favorites_by_user/{userGuid}", response_model=list[FavoriteInput])
async def get_favorites_by_user(userGuid: str = Path(..., description="GUID пользователя")):
    return await FavoriteDAO.get_favorites_by_user(user_guid=userGuid)

@favorite_router.get("/get_favorites/{userGuid}/{contractGuid}")
async def get_favorites(userGuid: str = Path(..., description="GUID пользователя"),
                                contractGuid: str = Path(..., description="GUID договора")):
    result= await FavoriteDAO.get_favorites(user_guid=userGuid, contractGuid=contractGuid)
    return [element._mapping for element in result["requestResult"]]


# @favorite_router.get("/get_favorites_by_representativeGuid/{representativeGuid}", response_model=list[FavoriteInput])
@favorite_router.get("/get_favorites_by_representativeGuid/{representativeGuid}")
async def get_favorites_by_user(representativeGuid: str = Path(..., description="GUID представитель")):
    result = await ContractDAO.get_contract_representative_guid(representativeGuid)
    table_result = []
    for _ in result:
        table_result.append(
            {
                "user_name": _.counterparty_name,
                "user_guid": _.user_guid,
                "product_guid": _.product_guid,
                "product_title": _.full_name,
                "picture_path": _.path,
                "nomenclature_data": _._mapping
            }
        )
    return table_result


@favorite_router.delete("/deleted_favotite_by_guid")
async def deleted_favotite_by_guid(product_guid: FavoriteInput = Body(..., description="Данные для карточки товара")):
    await FavoriteDAO.delete_favorite(**product_guid.model_dump())

