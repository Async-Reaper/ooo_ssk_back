from fastapi import APIRouter, Body, Path, HTTPException
from fastapi import FastAPI, Request, Response
from ..utils.utils import add_objects_with_pictures
from .schemas import *
from .actions import *

router_brand = APIRouter(
    tags=["brand"],
    prefix="/api")

@router_brand.post("/brand/creating_brand")
async def creating_brands(brand_data: BrandInput):
    result = await BrandDAO.serch_brand_by_guid(brand_data.guid)
    if not result:
        await BrandDAO.brand_creation(**brand_data.model_dump())
        return None
    await BrandDAO.update_brand_by_guid(**brand_data.model_dump())
    

@router_brand.get("/brand/get_all_brands", response_model=BrandsGet)
async def get_all_brands():
    brands = await BrandDAO.get_all_brands()

    await add_objects_with_pictures(brands)

    return {
        "total_count_brands": len(brands),
        "brands": brands
        }

@router_brand.delete("/brand/deleted_brand/{brand_guid}")
async def deleted_brand(brand_guid: str = Path(..., description="Уникальный GUID бренда",
                                               min_length=36, 
                                               max_length=36)):
    await BrandDAO.deleted_brand(brand_guid)
    