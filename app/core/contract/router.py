from fastapi import APIRouter, Body, Path, HTTPException, Response, Request, status, Depends
from fastapi import Request, Response
from .schemas import *
from .actions import *

router_contract = APIRouter(
    tags=["contract"],
    prefix="/api"
)

@router_contract.post("/contract/creating_contract")
async def creating_contract(contract_data: ContractInput):
    result = await ContractDAO.get_contract_by_create(contract_data.guid)
    if not result:
        await ContractDAO.creating_contract(**contract_data.model_dump())
        return None
    await ContractDAO.update_contract(**contract_data.model_dump())
    
@router_contract.get("/contract/get_contract/{userGuid}", response_model=list[ContractInput])
async def get_contract(userGuid: str = Path(..., description="GUID пользователя",
                                                     min_length=36,
                                                     max_length=36)):
    return await ContractDAO.get_contract(userGuid)

@router_contract.get("/contract/get_contract_by_representativeGuid/{representativeGuid}", response_model=list[ContractInput])
async def get_contract(representativeGuid: str = Path(..., description="GUID Представителя",
                                                     min_length=36,
                                                     max_length=36)):
    return await ContractDAO.get_contract_representative_guid(representativeGuid)

@router_contract.delete("/contract/deleting_contract/{contract_guid}")
async def deleting_contract(contract_guid: str = Path(..., description="GUID договора", 
                                                       min_length=36,
                                                       max_length=36)):
    await ContractDAO.deleting_contract(contract_guid=contract_guid)


