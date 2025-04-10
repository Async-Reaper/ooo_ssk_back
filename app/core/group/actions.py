from app.database   import async_session_maker
from .models        import Groups
from sqlalchemy     import select, insert, delete, update
from fastapi        import HTTPException, status

class GroupDAO:
    
    @classmethod
    async def group_creation(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = insert(Groups).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def group_update(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = update(Groups).filter_by(guid = kwargs["guid"]).values(kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def group_get(cls) -> None:
        async with async_session_maker() as session:
            try:
                query = select(Groups).filter_by(is_deleted = False)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_group_by_guid(cls, guid) -> None:
        async with async_session_maker() as session:
            try:
                query = select(Groups).filter_by(guid = guid)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))