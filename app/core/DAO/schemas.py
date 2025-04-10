from pydantic import BaseModel, Field
from config import GUID, DATE_TWO, DATE_THREE
from ..nomenclature.schemas import NomenclatureOutput

class OrderHead(BaseModel):
    documentGUID: str = Field(GUID, description="GUID документа", min_length=36, max_length=36)
    number: str = Field("ОС000000000", description="Номер документа")
    date: str = Field(DATE_TWO, description="Дата создания документа")
    dateShipment: str = Field(DATE_TWO, description="[!..Уточник..!]")
    contractName: str = Field(..., description="Название договора")
    contractGUID: str = Field(GUID, description="GUID договора", min_length=36, max_length=36)
    approved: bool = Field(..., description="Статус утверждения документа")
    products_count: int = Field(..., description="Количество товаров")
    amount: float = Field(0.01, description="Сумма документа")
    comment: str = Field(..., description="Комментарий заказа", max_length=256)

class OrderTable(BaseModel):
    product_guid: str = Field(GUID, description="GUID товра ![..заменить productID на productGUID..]!")
    # other_data: NomenclatureOutput = Field(..., description="Дополнительная информация")
    count: float = Field(0.01, description="Количестко товара")
    price: float = Field(0.01, description="Цена товара")
    amount: float = Field(0.01, description="Сумма")


class OrderTableOutbut(BaseModel):
    total_count_products: int = Field(..., description="Количество товаров")
    products: list[OrderTable] | None = Field(..., description="Список товаров")
class ProductItem(BaseModel):
    product_guid: str = Field(GUID, description="GUID товара")
    count: float = Field(1.00, description="Количество товара")

class OrderCreateHeader(BaseModel):
    contractGUID: str = Field(GUID, description="GUID контракта", min_length=36, max_length=36)
    dateshipment: str = Field(DATE_THREE, description="Дата создания документа")
    userGUID: str = Field(GUID, description="GUID пользователя")
    comment: str = Field(..., description="Комментарий заказа")

class ApproveCreateHeader(BaseModel):
    documentGUID: str = Field(GUID, description="GUID контракта", min_length=36, max_length=36)
    dateshipment: str = Field(DATE_THREE, description="Дата создания документа")
    userGUID: str = Field(GUID, description="GUID пользователя")
    comment: str = Field(..., description="Комментарий заказа", max_length=256)

class OrderCreateBody(BaseModel):
    header: OrderCreateHeader = Field(..., description="Заголовки")
    products: list[ProductItem] = Field(..., description="Данные товаров")

class ApproveCreateBody(BaseModel):
    header: ApproveCreateHeader = Field(..., description="Заголовки")
    products: list[ProductItem] = Field(..., description="Данные товаров")

class ProductItemOutput(BaseModel):
    product_guid: str = Field(GUID, description="GUID товара")
    message: str = Field(..., description="Детали")

class OrderCreateOutput(BaseModel):
    message: str = Field(..., description="Результат выполнения команды")
    error: bool = Field(False, description="Признак наличия ошибки")
    detail: list[ProductItemOutput] | None = Field(None, description="Фиктивные товары")

class OrderHeadOutput(BaseModel):
    total_count_products: int = Field(..., description="Общее документов товаров")
    products: list[OrderTable] = Field(..., description="Список товаров")
    

class ReceivableItemOutput(BaseModel):
    documentGUID: str = Field(GUID, description="Пользовательский GUID")
    date: str = Field(DATE_TWO, description="Дата задолжности")
    number: str = Field(..., description="Номер документа")
    amount: float = Field(0.01, description=".?.")
    amountDebt: float = Field(0.01, description=".?.")
    daysNotPaid: float = Field(0.01, description="Количество дней просрочки")
    

class ReceivableOutput(BaseModel):
    totalDebts: float
    totalCount: int
    debts: list[ReceivableItemOutput] | list[None]
