from app.database   import async_session_maker
from .models        import Favorites, FavoritesSeller
from sqlalchemy     import select, insert, delete, update, literal, String, type_coerce
from sqlalchemy.dialects.postgresql import JSONB
from fastapi        import HTTPException, status
from ..nomenclature.models import Nomenclature
from ..picture.models import Picture

class FavoriteDAO:
    
    @classmethod
    async def favorite_creation(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = insert(Favorites).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
            try:
                query = insert(FavoritesSeller).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_favorites_by_user(cls, user_guid: str) -> list:
        async with async_session_maker() as session:
            try:
                query = select(Favorites).filter_by(user_guid = user_guid)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))

    @classmethod
    async def get_favorites(cls, user_guid: str, contractGuid: str) -> list:
        async with async_session_maker() as session:
            try:
                query = select(Favorites.__table__.c.product_guid,
                               Nomenclature.__table__,
                               Picture.__table__).select_from(
                                Nomenclature.__table__.join(Favorites.__table__, Nomenclature.__table__.c.guid == Favorites.__table__.c.product_guid)\
                                .outerjoin(Picture.__table__, Picture.__table__.c.guid_object == Favorites.__table__.c.product_guid))\
                .filter(Favorites.__table__.c.user_guid == user_guid, Favorites.__table__.c.currentTradePoint == contractGuid)
            
                result = await session.execute(query)
                return {"classObject": result,
                        "requestResult": result.fetchall(),
                        "requestMapping": result.mappings().all()}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))

            
    @classmethod
    async def delete_favorite(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                print(kwargs)
                query = delete(Favorites).filter_by(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def delete_favorite_seller(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                print(kwargs)
                query = delete(FavoritesSeller).filter_by(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))