from pydantic import BaseModel, Field
from config import GUID
from enum import Enum

class User(BaseModel):
    login: str = Field(..., description="Логин пользователя")
    password: str = Field(..., description="Пароль пользователя")

class UserRole(Enum):
    Shop = "Shop"
    Seller = "Seller"
    administrator = "admin"

class UserItem(BaseModel):
    userGUID: str= Field(GUID, description="Уникальный ID пользователя")
    role: UserRole = Field(..., description="Роль пользователя")
    exp: int= Field(..., description="Время жизни токена")
    user_info: None | dict
