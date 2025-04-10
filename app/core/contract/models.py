from sqlalchemy import String, Integer, JSON, BOOLEAN, ForeignKey, Column
from app.database import Base


class Contract(Base): 
    """[Модель таблицы contract]"""
    __tablename__ = "contracts"
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    fullname = Column(String(256), nullable = False)
    counterparty_guid = Column(String(36), nullable = False)
    counterparty_name = Column(String(256), nullable = False)
    organization_guid = Column(String(36), nullable = False)
    organization_name = Column(String(256), nullable = False)
    representative_guid = Column(String(36), nullable = False)
    representative_name = Column(String(128), nullable = False)
    representative_phone = Column(String(16), nullable = True)
    is_deleted = Column(BOOLEAN, nullable = False)
    see_only_your_matrix = Column(BOOLEAN, nullable = False)
    
