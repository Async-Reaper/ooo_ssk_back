from fastapi import APIRouter, Body, HTTPException, status, Path
from ..utils.utils import get_element_by_guid
from fastapi.responses import FileResponse
import os
from .schemas import *
from .actions import *

group_router = APIRouter(
    prefix="/api",
    tags=["group"]
)


@group_router.post("/group/create_group", status_code=200, description="Добавдение группы товара")
async def add_picture(nomenclature_group: GroupInput = Body(..., description="...")):
    result = await GroupDAO.get_group_by_guid(nomenclature_group.guid)
    if not result:
        await GroupDAO.group_creation(**nomenclature_group.model_dump())
        return None
    await GroupDAO.group_update(**nomenclature_group.model_dump())
   
@group_router.get("/group/get_group", status_code=200, description="Получение груп товаров")
async def get_picture(): 
    result = await GroupDAO.group_get()

    return result

@group_router.get("/group/get_group/structures", description="Получить группы для структур подчиненных")
async def get_group_by_structures():
    result = await GroupDAO.group_get()

    def get_children(parent_guid):
        return [group for group in result if group.parent_guid == parent_guid]

    structured_result = [
        {
            "object": group,
            "subject": get_children(group.guid)
        }
        for group in result
        if group.parent_guid == "00000000-0000-0000-0000-000000000000" or group.parent_guid == group.guid
    ]

    return structured_result
    # result = await GroupDAO.group_get()
    # fine_groupe = []
    # for element in result:
    #     objects = {
    #         "object": element,
    #         "subject": await get_element_by_guid(result, element.guid)
    #     }
    #     fine_groupe.append(objects)
    # return fine_groupe
