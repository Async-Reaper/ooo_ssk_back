from sqlalchemy import String, Integer, Float, ForeignKey, Column
from app.database import Base

class Basket(Base): 
    """[Модель таблицы order_basket]"""
    __tablename__ = "basket"

    id                  = Column(Integer, primary_key=True)
    user_guid           = Column(String(36), nullable= False)
    contract_guid       = Column(String(36), nullable= False)
    product_guid       = Column(String(36), nullable= False)
    count               = Column(Float(3), nullable= False)