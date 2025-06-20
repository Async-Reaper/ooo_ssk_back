from pydantic import BaseModel, Field
from config import GUID, DATE, DATE_TWO
from ..picture.schemas import PictureOutput


class NomenclatureInput(BaseModel):
    guid: str = Field(GUID, descriptio="Уникальный идентификатор товара")
    short_name: str = Field(..., description="Упрощенное наименование товара")
    nomenclature_group: str = Field(GUID, description="Группа товара")
    full_name: str = Field(..., description="Полное наименование товара ")
    description: str = Field(..., description="Описание товара")
    expiration_date: int = Field(30, description="Срок годности товара(в днях)")
    measurement: str = Field(..., description="Единица измерения товара")
    weight: float = Field(0.01, description="Вес товара")
    multiplicity: float = Field(0.01, description="Множитель цены товара(не точно)")
    is_deleted: bool = Field(False, description="Пометка удаления товара")
    is_discount: bool = Field(False, description="Идет скидка на товар(да/нет)")
    is_new: bool = Field(False, description="Новый товара(да/нет)")
    date_create: str = Field(DATE_TWO, description="Дата создания товара")
    brand_guid: str = Field(GUID, description="Уникальный идентификатор бренда")

class NomenclatureOutput(BaseModel):
    guid: str = Field(GUID, descriptio="Уникальный идентификатор товара")
    short_name: str = Field(..., description="Упрощенное наименование товара")
    nomenclature_group: str = Field(GUID, description="Группа товара")
    full_name: str = Field(..., description="Полное наименование товара ")
    description: str = Field(..., description="Описание товара")
    expiration_date: int = Field(30, description="Срок годности товара(в днях)")
    measurement: str = Field(..., description="Единица измерения товара")
    weight: float = Field(0.01, description="Вес товара")
    multiplicity: float = Field(0.01, description="Множитель цены товара(не точно)")
    is_deleted: bool = Field(False, description="Пометка удаления товара")
    is_discount: bool = Field(False, description="Идет скидка на товар(да/нет)")
    is_new: bool = Field(False, description="Новый товара(да/нет)")
    date_create: str = Field(DATE_TWO, description="Дата создания товара")
    brand_guid: str = Field(GUID, description="Уникальный идентификатор бренда")
    additional_information: dict | None = Field(None, description="Дополнительная информация продукта")
    pictures: None | list[PictureOutput] = Field([], description="Изображения товара")

class NomenclatureGet(BaseModel):
    total_count_products: int = Field(1, description="Общее количество товаров")
    count_products: int = Field(1, description="Количество найденных товаров")
    products: list[NomenclatureOutput] = Field(..., description="Список товаров")

class NomenclatureListInput(BaseModel):
    nomenclatures: list = Field([GUID], description="Список номенклатур")

class NomenclatureListOutput(BaseModel):
    guid: str = Field(GUID, description="Гуид товара")
    short_name: str = Field(..., description="Упрощенное наименование товара")
    expiration_date: int = Field(..., description="Срок годности товара(в днях)")
    measurement: str = Field(..., description="Единица измерения товара")
