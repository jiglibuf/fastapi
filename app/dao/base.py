#Data access object (работаем с бд)
from app.database import async_session_maker
from sqlalchemy import select


class BaseDAO: # Базовый класс для других моделей (описаны стандартные запросы к бд, например выбор всех строк из таблицы X)
    model = None

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()