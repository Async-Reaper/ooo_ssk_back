from pydantic import BaseModel, Field
from ..picture.schemas import PictureOutput
from config import GUID


class BrandInput(BaseModel):
    guid: str = Field(GUID, description="Уникальный GUID бренда", max_length=36, min_length=36)
    fullname: str = Field(..., description="Полное наименование бренда", max_length=256)
    is_deleted: bool = Field(False, description="Признак того что контранкт был помечен на удаление")

class BrandOutput(BaseModel):
    guid: str = Field(GUID, description="Уникальный GUID бренда", max_length=36, min_length=36)
    fullname: str = Field(..., description="Полное наименование бренда", max_length=256)
    is_deleted: bool = Field(False, description="Признак того что контранкт был помечен на удаление")
    pictures: None | list[PictureOutput] = Field(None, description="Изображения бренда")

class BrandsGet(BaseModel):
    total_count_brands: int = Field(..., description="Общее количество брендов")
    brands: list[BrandOutput] = Field(..., description="Список доступных брендов")