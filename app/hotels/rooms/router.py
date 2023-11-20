from fastapi import APIRouter, Depends



router = APIRouter(
    prefix="/rooms",
    tags=["Комнаты"],
)

@router.get("")
async def get_rooms():
    pass