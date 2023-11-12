from datetime import datetime
from jose import jwt, JWTError
from app.exceptions import IncorrectTokenFormatException, TokenAbsentException,TokenExpiredException, UserIsNotInTokenException
from app.users.dao import UsersDAO
from config import settings
from fastapi import Depends, Request


def get_token(request: Request):
    token = request.cookies.get('booking_access_token') # проверяем есть ли токен
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token:str = Depends(get_token)):

    try: # Декодируем токен
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatException

    expire: str = payload.get("exp") #проверяем закончилось ли время жизни токена
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException

    user_id: str = payload.get("sub") # получаем id пользователя из токена
    if not user_id:
        raise UserIsNotInTokenException
    user = await UsersDAO.find_one_or_none(id = int(user_id)) # проверяем есть ли пользователь с id = user_id в БД
    if not user:
        raise UserIsNotInTokenException

    return user