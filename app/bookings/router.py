from fastapi import APIRouter
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking


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
