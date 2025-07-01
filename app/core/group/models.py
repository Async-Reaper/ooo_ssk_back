from sqlalchemy import String, BOOLEAN, Column, Integer
from app.database import Base

class Groups(Base): 
    """[Модель таблицы groups]"""
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    guid        = Column(String)
    fullname    = Column(String(256),   nullable        = False)
    parent_guid = Column(String(64),    nullable        = True)
    # image    = Column(String(256),   nullable        = False)
    is_deleted  = Column(BOOLEAN,       nullable        = False)