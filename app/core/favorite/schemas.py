from pydantic import BaseModel, Field
from config import GUID, PHONE

class FavoriteInput(BaseModel):
    user_guid: str = Field(GUID, description="GUID пользователя")
    product_guid: str = Field(GUID, description="GUID товара")
    currentTradePoint: str = Field(GUID, description="GUID договора")

class FavoriteOutput(BaseModel):
    representative_guid: str = Field(GUID, description="GUID контрагента")
    representative_name: str = Field(..., description="Имя контрагента")
    representative_phone: str = Field(PHONE, description="Мобильный телефон для связи")

# class FavoriteOutput(BaseModel):
    # total_count_products: int = Field(..., description="Общее количество товаров")
    # products: list[FavoriteInput] | None = Field(None, description="Список товаров")