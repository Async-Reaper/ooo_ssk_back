from sqlalchemy import String, Integer, JSON, BOOLEAN, ForeignKey, Column
from app.database import Base


class RepresentativeData(Base): 
    """[Модель таблицы representative_data]"""

    __tablename__ = "representative_data"
    
    id= Column(Integer, primary_key= True)
    user_guid= Column(String(36), nullable=False)
    document_guid= Column(String(36), nullable=False)
    document_data= Column(JSON, nullable=True)

