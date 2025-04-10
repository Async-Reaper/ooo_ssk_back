from pydantic import BaseModel, Field
from ..picture.schemas import PictureOutput
from config import GUID
from ..nomenclature.schemas import NomenclatureOutput


class BasketInput(BaseModel):
    user_guid:      str = Field(GUID, description="GUID пользователя", max_length=36, min_length=36)
    contract_guid:  str = Field(GUID, description="GUID торговой точки", max_length=36, min_length=36)
    product_guid:   str = Field(GUID, description="GUID товара", min_length=36, max_length=36)
    count: float = Field(0.01, description="Количество товара", min=0.01)

class BasketItem(BaseModel):
    user_guid:      str = Field(GUID, description="GUID пользователя", max_length=36, min_length=36)
    contract_guid:  str = Field(GUID, description="GUID торговой точки", max_length=36, min_length=36)
    product_guid:   str = Field(GUID, description="GUID товара", min_length=36, max_length=36)
    count: float = Field(0.01, description="Количество товара", min=0.01)
    # additional_information: dict | None = Field(None, description="Дополнительная информация продукта")
    other_data: NomenclatureOutput = Field(..., description="Дополнительная информация о товаре")

class BasketOutput(BaseModel):
    total_count_products: int = Field(..., description="Общее количество товаров")
    products: list[BasketItem] = Field(..., description="Список товаров")


