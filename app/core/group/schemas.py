from pydantic import BaseModel, Field
from ..picture.schemas import PictureOutput
from config import GUID

class GroupInput(BaseModel): 
    guid: str = Field(GUID, description="GUID группы")        
    fullname: str = Field(..., description="Полгое наименование группы")    
    parent_guid: str = Field(GUID, description="GUID подчинённой группы") 
    is_deleted: bool = Field(..., description="Признак того что группа помечена на удаление")  

class GroupPutput(BaseModel): 
    guid: str = Field(GUID, description="GUID группы")        
    fullname: str = Field(..., description="Полгое наименование группы")    
    parent_guid: str = Field(GUID, description="GUID подчинённой группы") 
    is_deleted: bool = Field(..., description="Признак того что группа помечена на удаление") 
    picture: PictureOutput | None = Field(..., description="Изображение группы") 
     