from fastapi import APIRouter, Body, HTTPException, Response, status, Path, Request, Query
from ..nomenclature.actions import NomenclatureDAO

from .schemas import *
from .actions import *

dao_router = APIRouter(
    prefix="/api/dao",
    tags=["DAO"]
)

@dao_router.get("/get_orders_headers/{orderGuid}", response_model=OrderHead)
async def get_orders_headers(orderGuid: str = Path(..., description="GUID документа", min_length=36, max_length=36)):
    return await Dao.get_order_header(orderGuid = orderGuid)

@dao_router.get("/get_orders_table/{orderGuid}", )
async def get_orders_table(orderGuid: str = Path(..., description="GUID документа", min_length=36, max_length=36)):
    products = await Dao.get_order_table(orderGuid = orderGuid)
    # for product in products: 
    #     product["additional_information"] = {
    #        "remains": product.amount
    #     }

    return {
        "total_count_products": len(products),
        "products": products
    }

@dao_router.get("/get_history_product/{productGuid}/{contractGuid}")
async def get_history_product(productGuid: str = Path(..., description="GUID товара", min_length=36, max_length=36),
                              contractGuid: str = Path(..., description="GUID договора", min_length=36, max_length=36)):
    return await Dao.get_history_product(productGuid=productGuid, contractGuid=contractGuid)

@dao_router.get("/get_history_product/{startDate}/{endDate}/{contractGuid}")
async def get_history_product(startDate: str = Path(..., description="Стартовая дата поиска. Формат — [00010101]", max_length=16),
                              endDate: str = Path(..., description="Конечная дата поиска. Формат — [00010101]", max_length=16),
                              contractGuid: str = Path(..., description="GUID договора", min_length=36, max_length=36)):
    return await Dao.get_history_by_date(startDate=startDate, endDate=endDate, contractGuid=contractGuid)

# @dao_router.post("/create_order", response_model=OrderCreateOutput)
@dao_router.post("/create_order")
async def create_order(order_data: OrderCreateBody, response: Response):
    return await Dao.build_order(**order_data.model_dump())

@dao_router.post("/approve_order", response_model=OrderCreateOutput)
async def approve_order(order_data: ApproveCreateBody, response: Response):
    return await Dao.approve_order(**order_data.model_dump())

@dao_router.get("get_receive_accounts_receivable/{contractGuid}", response_model=ReceivableOutput)
async def get_receive_accounts_receivable(contractGuid: str = Path(..., description="GUID договора")):
    return await Dao.get_receive_accounts_receivable(contractGuid)