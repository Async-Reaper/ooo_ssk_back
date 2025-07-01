from app.database   import async_session_maker
from .models        import Groups
from sqlalchemy     import select, insert, delete, update
from fastapi        import HTTPException, status
from ..picture.models import Picture

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
    async def group_get(cls) -> list:
        async with async_session_maker() as session:
            try:
                query_groups = select(Groups).filter_by(is_deleted=False)
                result_groups = await session.execute(query_groups)
                groups = result_groups.scalars().all()

                # Загружаем все изображения для категории "группа"
                query_pictures = select(Picture).where(Picture.picture_category == "nomenclature_groups")
                result_pictures = await session.execute(query_pictures)
                pictures = result_pictures.scalars().all()

                # Создаём словарь изображений по guid
                picture_map = {pic.guid_object: pic.path for pic in pictures}

                # Добавляем поле image_path к каждой группе
                for group in groups:
                    group.picture = picture_map.get(group.guid)

                return groups
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
            
    @classmethod
    async def get_group_by_guid(cls, guid) -> None:
        async with async_session_maker() as session:
            try:
                query = select(Groups).filter_by(guid = guid)
                result = await session.execute(query)
                return result.scalars().all()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.args))