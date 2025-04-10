from sqlalchemy import String, Integer, JSON, BOOLEAN, ForeignKey, Column
from app.database import Base


class Picture(Base): 
    """[Модель таблицы pictures]"""

    __tablename__ = "pictures"
    id= Column(Integer, primary_key=True)
    guid_object= Column(String(36), nullable=False)
    picture_type= Column(String(8), nullable=False)
    picture_category= Column(String(32), nullable=False)
    file_name= Column(String(45), nullable=False)
    path= Column(String(256), nullable= False) 
    is_deleted= Column(BOOLEAN, default=False)
    is_main= Column(BOOLEAN, default=False)

