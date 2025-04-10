from sqlalchemy import Constraint, String, Integer, Float, BINARY ,JSON, BOOLEAN, ForeignKey, Column
from app.database import Base


class Nomenclature(Base):  
    """[Модель таблицы nomenclatures]"""
    __tablename__ = "nomenclatures"
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    short_name = Column(String(128), nullable = False)
    full_name = Column(String(256), nullable = False)
    description = Column(String(512), nullable = True)
    expiration_date = Column(Integer(), nullable = False)
    measurement = Column(String(32), nullable = False)
    weight = Column(Float(3), nullable = False)
    multiplicity = Column(Float(3), nullable = False)
    is_deleted = Column(BOOLEAN, default=False)    
    is_discount = Column(BOOLEAN, default=False)    
    is_new = Column(BOOLEAN, default=False)
    date_create = Column(String(16), nullable=False)   
    # brand_guid = Column(ForeignKey("brands.guid"), nullable = True)
    brand_guid = Column(String(36), nullable = True)
    # nomenclature_group = Column(ForeignKey("groups.guid"), nullable =True)
    nomenclature_group = Column(String(36), nullable =True)