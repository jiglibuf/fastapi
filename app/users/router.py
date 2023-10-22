from fastapi import APIRouter, HTTPException
from app.users.auth import get_password_hash, verify_password
from app.users.dao import UsersDAO
from app.users.schemas import SUserAuth


router = APIRouter(
    prefix='/auth',
    tags=["Аутентификация"],
)


@router.post('/register',)
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email = user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email = user_data.email, hashed_password = hashed_password)

@router.post('/login',)
async def login_user(user_data: SUserAuth):
        user = await UsersDAO.find_one_or_none(email = user_data.email)
        if not user:
            raise HTTPException(status_code=500)
        if user and verify_password(password, user.hashed_password):  # <-- или даже так
            return user