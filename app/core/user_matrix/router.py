from fastapi import APIRouter,Path
from .schemas import *
from .actions import *


router_representative_data = APIRouter(
    tags=["representative_data"],
    prefix="/api/representative_data"
)

@router_representative_data.post("/create_representative_data")
async def create_representative_data(representative_data: RepresentativeDataInput):

    # representative_data.document_data = json.load(representative_data.document_data) 

    result = await RepresentativeDataDAO.get_representative_data(representative_data.user_guid, representative_data.document_guid)
    if not result:
        resylt = await RepresentativeDataDAO.representative_data_creation(**representative_data.model_dump())
    
    resylt = await RepresentativeDataDAO.update_representative_data(**representative_data.model_dump())

    return representative_data

@router_representative_data.get("/get_representative_data/{user_guid}/{document_guid}")
async def get_representative_data(user_guid: str = Path(..., description="Пользовательский GUID"), 
                     document_guid: str = Path(..., description="GUID документа")):

    return await RepresentativeDataDAO.get_representative_data(user_guid, document_guid)

@router_representative_data.get("/get_all_representative_data/{user_guid}")
async def get_representative_data(user_guid: str = Path(..., description="Пользовательский GUID")):

    return await RepresentativeDataDAO.get_all_representative_data(user_guid)

@router_representative_data.delete("/delete_representative_data/{user_guid}/{document_guid}")
async def delete_representative_data(user_guid: str = Path(..., description="Пользовательский GUID"),
                                  document_guid: str = Path(..., description="GUID документа")):

    return await RepresentativeDataDAO.delete_representative_data(user_guid, document_guid)

    
