from pydantic import BaseModel, Field
from enum import Enum

from config import GUID

class RepresentativeDataInput(BaseModel):
    user_guid: str = Field(GUID, description="Пользовательский GUID", min_length=36, max_length=36)
    document_guid: str = Field(GUID, description="GUID документа", min_length=36, max_length=36)
    document_data: dict = Field(..., description="Данные для документа")
