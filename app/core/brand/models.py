from sqlalchemy import String, BOOLEAN, Column, Integer
from app.database import Base


class Brands(Base): 
    """[Модель таблицы contracts]"""
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    fullname = Column(String(256), nullable = False)
    is_deleted = Column(BOOLEAN, default= False)

