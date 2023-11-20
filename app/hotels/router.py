from fastapi import APIRouter, Depends
from app.exceptions import MissedHotel
from app.hotels.dao import HotelsDAO
from app.hotels.models import Hotels
from datetime import date
from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import SRoomsWithTotalCostAndRoomsLeft

from app.hotels.schemas import SHotelWithRoomsLeft, SHotels


router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)

@router.get("/{location}")
async def get_hotels_by_location_with_available_rooms(location: str, date_from: date, date_to: date)-> list[SHotelWithRoomsLeft]:
# async def get_hotels(location: str, date_from: date, date_to: date):
   return await HotelsDAO.get_hotels_by_location_with_available_rooms(location,date_from,date_to)

@router.get("/id/{hotel_id}")
async def get_specific_hotel(hotel_id: int)->SHotels:
    hotel = await HotelsDAO.find_one_or_none(id=hotel_id)
    if not hotel:
        raise MissedHotel
    return hotel

     
@router.get("/id/{hotel_id}/rooms")
async def get_specific_hotel(hotel_id: int, date_from: date, date_to: date):
    hotel = await HotelsDAO.find_one_or_none(id=hotel_id)
    # rooms = await RoomsDAO.get_rooms_left(hotel = hotel, date_from=date_from,date_to=date_to)
    rooms = await RoomsDAO.get_available_rooms_data(hotel = hotel, date_from=date_from,date_to=date_to)
    if not rooms:
        raise MissedHotel
    return rooms