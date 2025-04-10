from sqlalchemy import String, Integer, JSON, BOOLEAN, ForeignKey, Column
from app.database import Base


class Favorites(Base):  
    """[Модель таблицы favorites]"""
    __tablename__ = "favorites"

    id= Column(Integer(), primary_key=True)
    user_guid= Column(String(36), nullable= False)
    currentTradePoint= Column(String(36), nullable= False)
    product_guid= Column(String(36), nullable= False)

