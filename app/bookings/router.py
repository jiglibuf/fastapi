from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix='/bookings',
    tags=["Бронирования"],
)


@router.get('')
async def get_bookings() -> list[SBooking]:
    return await BookingDAO.find_all()
     
@router.get('/test')
async def get_bookings() -> SBooking:
    return await BookingDAO.find_one_or_none(room_id = 7)
@router.get('/test1')
async def get_bookings(user: Users = Depends(get_current_user)): #-> list[SBooking]:
    return await BookingDAO.find_all(user_id = user.id)