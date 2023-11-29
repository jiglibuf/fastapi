
# fastapi
Прохожу курс по fastapi
Используемые команды для других машин после клонирования репозитория:
1)python -m venv venv
2)venv\Scripts\activate
3)pip install -r requirements.txt

Для обновления библиотек pip freeze > requirements.txt

Для запуска сервера: uvicorn app.main:app --reload

Для выхода из витруального окружения deactivate
  Для создания:
  alembic init migrations
  изменить script_location если перенес папку migrations ниже (обычно папка app)
  
  Для изменения дб:
Alembic:
1)alembic revision --autogenerate -m "Название миграции"
2)alembic upgrade head (Залить все миграции)
3)alembic downgrade -1 (Откатиться на миграцию назад)
