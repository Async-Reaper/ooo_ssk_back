from app.database   import async_session_maker
from .models        import Picture
from sqlalchemy     import select, insert, delete, update, func
from fastapi        import HTTPException, status
from aiohttp                import ClientSession
from config import PATH_IMAGE
from base64 import b64decode
from pathlib import Path
import os
import json



class PictureDAO:
    
    @classmethod
    async def picture_creation(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = insert(Picture).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_object_by_object(cls, guid_object) -> list:
        async with async_session_maker() as session:
            try:
                query = select(Picture).filter_by(guid_object = guid_object)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
    
    @classmethod
    async def serch_picture_py_name(cls, namePic:str, typePic:str) -> list:
        async with async_session_maker() as session:
            try:
                query = select(Picture).filter(Picture.file_name == namePic, 
                                               Picture.picture_type == typePic)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def update_picture_by_name(cls, namePic:str, typePic:str,  **kwargs) -> list:
        async with async_session_maker() as session:
            try:
                query = update(Picture).filter(Picture.file_name == namePic, 
                                                Picture.picture_type == typePic).values(kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))

            
class PictureManager:

    @classmethod
    async def image_decoding_and_recording(cls, picture_data: dict) -> None:
        file_path = f"{PATH_IMAGE}{picture_data.picture_category.value}/{picture_data.guid_object}"
        try:
            Path(file_path).mkdir(parents=True, exist_ok=True)

            decoded_image = b64decode(picture_data.binary_image)
            
            with open(f"{file_path}/{picture_data.file_name}.{picture_data.picture_type.value}", "wb") as file:
                file.write(decoded_image)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e.args))