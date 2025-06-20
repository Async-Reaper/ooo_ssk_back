from app.database   import async_session_maker
from .models        import Contract
from sqlalchemy     import select, insert, delete, update, join
from fastapi        import HTTPException, status
from ..favorite.models import FavoritesSeller
from ..nomenclature.models import Nomenclature
from ..picture.models import Picture

class ContractDAO:

    @classmethod
    async def creating_contract(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = insert(Contract).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def update_contract(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = update(Contract).filter_by(guid = kwargs["guid"]).values(kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))

    @classmethod
    async def get_contract(cls, counterparty_guid: str) -> list:
        async with async_session_maker() as session:
            try:
                query = select(Contract).filter_by(counterparty_guid = counterparty_guid, is_deleted = False)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_contract_by_create(cls, guid: str) -> list:
        async with async_session_maker() as session:
            try:
                query = select(Contract).filter_by(guid = guid)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_contract_representative_guid(cls, representativeGuid: str) -> list:
        async with async_session_maker() as session:
            try:
                query = select(
                    Contract.__table__.c.counterparty_name,
                    Contract.__table__.c.guid,
                    FavoritesSeller.__table__.c.user_guid,
                    FavoritesSeller.__table__.c.user_name,
                    FavoritesSeller.__table__.c.product_guid,
                    Nomenclature.__table__,
                ).filter_by(representative_guid = representativeGuid).select_from(
                    # join(Contract.__table__, Favorites.__table__, Contract.__table__.c.counterparty_guid == Favorites.__table__.c.user_guid)
                    Contract.__table__.join(FavoritesSeller.__table__, Contract.__table__.c.counterparty_guid ==FavoritesSeller.__table__.c.user_guid)\
                        .join(Nomenclature.__table__, Nomenclature.__table__.c.guid == FavoritesSeller.__table__.c.product_guid)\
                        ,Nomenclature
                )
                # query = select(Contract).filter_by(representative_guid = representativeGuid)

                result = await session.execute(query)
                return result.fetchall()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_contract_representative_guid_and_counterparty_guid(cls, representativeGuid: str, counterparty_guid: str) -> list:
        async with async_session_maker() as session:
            try:
                query = select(Contract).filter_by(representative_guid = representativeGuid, counterparty_guid = counterparty_guid)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def deleting_contract(cls, contract_guid: str) -> None:
        async with async_session_maker() as session:
            try:
                query = delete(Contract).filter_by(guid = contract_guid)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))