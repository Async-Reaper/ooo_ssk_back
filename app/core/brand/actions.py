from app.database   import async_session_maker
from .models        import Brands
from sqlalchemy     import select, insert, delete, update
from fastapi        import HTTPException, status

class BrandDAO:
    
    @classmethod
    async def brand_creation(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = insert(Brands).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def serch_brand_by_guid(cls, guid) -> None:
        async with async_session_maker() as session:
            try:
                query = select(Brands).filter_by(guid = guid)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_all_brands(cls) -> list:
        async with async_session_maker() as session:
            try:
                query = select(Brands).filter_by(is_deleted = False)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def update_brand_by_guid(cls, **kwargs) -> list:
        async with async_session_maker() as session:
            try:
                query = update(Brands).filter_by(guid = kwargs["guid"]).values(kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
    
    @classmethod
    async def deleted_brand(cls, brand_guid: str) -> None:
        async with async_session_maker() as session:
            try:
                query = delete(Brands).filter_by(guid = brand_guid)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))