from app.database   import async_session_maker
from .models        import Basket
from sqlalchemy     import select, insert, delete, update
from fastapi        import HTTPException, status

class BasketDAO:
    
    @classmethod
    async def product_creation(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = insert(Basket).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def checking_availability_of_goods_in_basket(cls, user_guid: str,
                                                       contract_guid: str,
                                                       product_guid: str):
        async with async_session_maker() as session:
            try:
                query = select(Basket).filter_by(user_guid = user_guid, 
                                              contract_guid = contract_guid,
                                              product_guid = product_guid)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_all_product_user_by_contract_guid(cls, user_guid: str, contract_guid: str) -> list:
        async with async_session_maker() as session:
            try:
                query = select(Basket).filter_by(user_guid = user_guid, contract_guid = contract_guid)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))

    @classmethod
    async def deleted_product_from_basket(cls, user_guid: str, contract_guid: str, product_guid: str) -> None:
        async with async_session_maker() as session:
            try:
                query = delete(Basket).filter_by(user_guid = user_guid, 
                                                 contract_guid = contract_guid,
                                                 product_guid = product_guid)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args)) 
            
    @classmethod
    async def deleted_products_from_basket(cls, user_guid: str, contract_guid: str) -> None:
        async with async_session_maker() as session:
            try:
                query = delete(Basket).filter_by(user_guid = user_guid, 
                                                 contract_guid = contract_guid)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args)) 

    @classmethod
    async def update_product_details(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = update(Basket).filter_by(user_guid = kwargs["user_guid"], 
                                                contract_guid = kwargs["contract_guid"],
                                                product_guid = kwargs["product_guid"]).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))