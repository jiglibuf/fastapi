from datetime import datetime
from jose import jwt, JWTError
from app.users.dao import UsersDAO
from config import settings
from fastapi import Depends, HTTPException, Request, status


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token

async def get_current_user(token:str = Depends(get_token)):

    try: # Декодируем токен
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=1)
    
    expire: str = payload.get("exp") #проверяем закончилось ли время жизни токена
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=2)

    user_id: str = payload.get("sub") # получаем id пользователя из токена
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    user = await UsersDAO.find_one_or_none(id = int(user_id)) # проверяем есть ли пользователь с id = user_id в БД
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user