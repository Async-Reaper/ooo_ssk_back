from pydantic import BaseModel, Field
from config import PHONE, GUID

class ContractInput(BaseModel):
    guid: str = Field(GUID, description="GUID договора", min_length=36, max_length=36)
    fullname: str = Field(..., description="Полное наименование договора", max_length=256)
    counterparty_guid: str = Field(GUID, description="GUID контрагента", min_length=36, max_length=36)
    counterparty_name: str = Field(..., description="Полное наименование контрагента", max_length=256)
    organization_guid: str = Field(GUID, description="GUID организации", min_length=36, max_length=36)
    organization_name: str = Field(..., description="Название организации", max_length=256)
    representative_guid: str = Field(GUID, description="GUID торгового представителя", min_length=36, max_length=36)
    representative_name: str = Field(..., description="Имя торгового представителя", max_length=128)
    representative_phone: str = Field(PHONE, description="Контактный номер телефона", max_length=16)
    is_deleted: bool = Field(False, description="Признак того что контранкт был помечен на удаление")
    see_only_your_matrix: bool = Field(False, description="Признак просмотра всей матрицы товаров")


# class ContractOutput(BaseModel):
    # total_count_contracts: int = Field(..., description="Общее количество договоров")
    # contracts: list[ContractInput] = Field(..., description="Список доступных договоров")