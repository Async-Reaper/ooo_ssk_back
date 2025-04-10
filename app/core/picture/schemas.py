from pydantic import BaseModel, Field
from enum import Enum

from config import GUID, BINARY_IMAGE

class PictureType(Enum):
    JPG = "jpg"
    PNG = "png"
    GIF = "gif"
    JPEG = "jpeg"
    TIF = "tiff"

class PictureCategory(Enum):
    GROUPS = "groups"
    NOMENCLATURE_GROUPS = "nomenclature_groups"
    NOMENCLATURES = "nomenclatures"
    BRANDS = "brands"

class PictureInput(BaseModel):
    guid_object: str = Field(GUID, description="GUID объекта к которому относиться изображение", min_length=36, max_length=36)
    picture_type: PictureType = Field(..., description="Типы поддерживаемых изображений")
    binary_image: str = Field(BINARY_IMAGE, description="Двоичные даные изображения")
    picture_category: PictureCategory = Field(..., description="Категория картинки")
    file_name: str = Field(..., description="Название файла с типом", max_length=128)
    is_deleted: bool = Field(False,  description="Признак того что картинка помечена на удаление")
    is_main: bool = Field(False, description="Признак того что картинка являеться главной")

class PictureOutput(BaseModel):
    guid_object: str = Field(GUID, description="GUID объекта к которому относиться изображение", min_length=36, max_length=36)
    path: str = Field(..., description="Путь до изображения", max_length=256)
    picture_type: PictureType = Field(..., description="Типы поддерживаемых изображений")
    picture_category: PictureCategory = Field(..., description="Категория картинки")
    file_name: str = Field(..., description="Название файла с типом", max_length=128)
    is_deleted: bool = Field(..., description="Признак того что картинка помечена на удаление")
    is_main: bool = Field(..., description="Признак того что картинка являеться главной")
