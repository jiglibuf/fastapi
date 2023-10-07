[![Board Status](https://dev.azure.com/Prikolists/d0572886-9111-4e16-abf0-2ce3111347a0/7997d182-10d6-444e-9e00-6d194ce89d7f/_apis/work/boardbadge/f1d14ce4-fc20-4f2c-b3ec-74e0714ca8c0)](https://dev.azure.com/Prikolists/d0572886-9111-4e16-abf0-2ce3111347a0/_boards/board/t/7997d182-10d6-444e-9e00-6d194ce89d7f/Microsoft.RequirementCategory)
# fastapi
Прохожу курс по fastapi
Используемые команды для других машин после клонирования репозитория:
1)python -m venv venv
2)venv\Scripts\activate
3)pip install -r requirements.txt

Для обновления библиотек pip freeze > requirements.txt

Для запуска сервера: uvicorn app.main:app --reload

Для выхода из витруального окружения deactivate

Alembic:
1)alembic revision --autogenerate -m "Название миграции"
2)alembic upgrade head (Залить все миграции)
3)alembic downgrade -1 (Откатиться на миграцию назад)