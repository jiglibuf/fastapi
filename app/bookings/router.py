from datetime import date
from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SBookingsWithRoomData
from app.exceptions import MissedBooking, RoomCannotBeBooked
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


# @router.get("")
# async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
#     return await BookingDAO.find_all(user_id = user.id)
@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)): # -> list[SBookingsWithRoomData] ошибка валидации
    return await BookingDAO.get_user_bookings(user_id = user.id)

@router.post("/")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
    
):
    booking = await BookingDAO.add(room_id, date_from, date_to, user.id)
    if not booking:
        raise RoomCannotBeBooked
    
@router.delete("/{booking_id}")
async def delete_booking(booking_id: int, user: Users = Depends(get_current_user)):
    booking = await BookingDAO.find_one_or_none(id=booking_id, user_id=user.id)
    if not booking:
        raise MissedBooking
    await BookingDAO.delete(id=booking_id, user_id=user.id)
    return {"message": "Бронирование успешно удалено"}


# @router.get('/test')
# async def get_bookings() -> SBooking:
#     return await BookingDAO.find_one_or_none(room_id = 7)
