from pydantic import BaseModel, EmailStr
#схема ответа 
class SUserAuth(BaseModel):
    email: EmailStr
    password: str