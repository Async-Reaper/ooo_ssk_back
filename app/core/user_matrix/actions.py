from app.database   import async_session_maker
from .models        import RepresentativeData
from sqlalchemy     import select, insert, delete, update, func
from fastapi        import HTTPException, status
from aiohttp                import ClientSession
from config import PATH_IMAGE
from base64 import b64decode
import os
import json


class RepresentativeDataDAO:
    
    @classmethod
    async def representative_data_creation(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                # kwargs["document_data"] = json.load(kwargs["document_data"])
                query = insert(RepresentativeData).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_representative_data(cls, user_guid:str, document_guid:str,) -> list:
        async with async_session_maker() as session:
            try:
                query = select(RepresentativeData).filter(RepresentativeData.user_guid == user_guid, 
                                                RepresentativeData.document_guid == document_guid)
                result = await session.execute(query)
                return result.scalars().first()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_all_representative_data(cls, user_guid:str) -> list:
        async with async_session_maker() as session:
            try:
                query = select(RepresentativeData).filter(RepresentativeData.user_guid == user_guid)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def update_representative_data(cls, **kwargs) -> list:
        async with async_session_maker() as session:
            try:
                query = update(RepresentativeData).filter(RepresentativeData.user_guid == kwargs["user_guid"], 
                                                RepresentativeData.document_guid == kwargs["document_guid"]).values(kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def delete_representative_data(cls, user_guid, document_guid) -> list:
        async with async_session_maker() as session:
            try:
                query = delete(RepresentativeData).filter(RepresentativeData.user_guid == user_guid, RepresentativeData.document_guid == document_guid)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))