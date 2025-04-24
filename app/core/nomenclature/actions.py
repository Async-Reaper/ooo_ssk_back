from app.database   import async_session_maker
from .models        import Nomenclature
from .schemas       import NomenclatureListInput
from sqlalchemy     import select, insert, delete, update, func
from fastapi        import HTTPException, status
from aiohttp                import ClientSession

import json
import config 


class NomenclatureDAO:
    
    @classmethod
    async def nomenclature_creation(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = insert(Nomenclature).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_nomenclature_by_guid(cls, product_guid: str) -> dict:
        async with async_session_maker() as session:
            try:
                query = select(Nomenclature).filter_by(guid = product_guid)
                result = await session.execute(query)
                return result.scalars().first()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def update_product(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            try:
                query = update(Nomenclature).filter_by(guid = kwargs["guid"]).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
    
    @classmethod
    async def get_product_by_options_without_title(cls, pages: int, limit: int, counter = False, **kwargs) -> list:
        async with async_session_maker() as session:
            try:
                offset = pages * limit
                if counter:
                    query = select(Nomenclature.guid).filter_by(is_deleted = False, **kwargs)
                else:
                    query = select(Nomenclature).filter_by(is_deleted = False, **kwargs).limit(limit).offset(offset)

                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_product_by_options_with_title(cls, pages: int, limit: int, title: str, counter = False,  **kwargs) -> list:
        async with async_session_maker() as session:
            try:
                offset = pages * limit
                if counter:
                    query = select(Nomenclature.guid).filter_by(is_deleted = False, **kwargs).filter(Nomenclature.full_name.ilike(f"%{title}%"))
                else:
                    query = select(Nomenclature).filter_by(is_deleted = False, **kwargs).filter(Nomenclature.full_name.ilike(f"%{title}%")).limit(limit).offset(pages)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))

    @classmethod
    async def get_count_products(cls) -> int:
        async with async_session_maker() as session:
            try:
                query = select(func.count()).select_from(Nomenclature)
                result = await session.execute(query)
                return result.scalars().one()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            

    @classmethod
    async def get_nomenclatures(cls, listNomenclatures: NomenclatureListInput) -> list:
        async with async_session_maker() as session:
            try:
                query = select(Nomenclature).filter(Nomenclature.__table__.c.guid.in_(listNomenclatures)).filter_by(is_deleted = False)

                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))
            
    @classmethod
    async def get_nomenclatures_matrix(cls, list_nomenclatures: list[str]) -> list[dict]:
        """
        Метод для поиска товаров в базе данных по списку GUID.

        :param list_nomenclatures: Список GUID для поиска.
        :return: Список найденных товаров.
        """
        if not list_nomenclatures:
            # Если список пуст, возвращаем пустой результат
            return []

        async with async_session_maker() as session:
            try:
                # Формируем запрос с фильтрацией по GUID и is_deleted=False
                query = (
                    select(Nomenclature)
                    .filter(Nomenclature.guid.in_(list_nomenclatures))
                    .filter_by(is_deleted=False)
                )

                # Выполняем запрос
                result = await session.execute(query)

                # Преобразуем результат в список словарей (если нужно вернуть JSON-совместимый формат)
                nomenclatures = [
                    {**nomenclature.__dict__, "_sa_instance_state": None}
                    for nomenclature in result.scalars().all()
                ]

                return nomenclatures

            except Exception as e:
                # Логируем ошибку и возвращаем HTTP-ошибку
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Ошибка при выполнении запроса: {str(e)}"
                )
        

class UtilsDAO: 
    @classmethod
    async def get_info_product(cls, productID, contractID):
        async with ClientSession() as session:
            headers = {
                "Authorization": config.API_TOKEN
            }
            data = {
            "productID": productID,
            "contractID": contractID 
            }
            async with session.post(f'{config.URL_1C}/fillProduct/update', headers = headers, json= data) as response:
                result = json.loads(await response.text())
                return result
            
    @classmethod
    async def get_more_info_product(cls, productID, contractID):
        async with ClientSession() as session:
            headers = {
                "Authorization": config.API_TOKEN
            }
            data = {
            "productItems": productID,
            "contractGUID": contractID 
            }
            async with session.post(f'{config.URL_1C}/nomenclatures/currentData', headers = headers, json= data) as response:
                result = json.loads(await response.text())
                return result
    