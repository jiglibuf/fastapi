from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.exceptions import NoHotelsInLocation
from app.hotels.models import Hotels
from sqlalchemy import  insert, select, delete, func, and_, or_
from app.database import async_session_maker
from app.bookings.dao import BookingDAO
from datetime import date
from app.hotels.rooms.dao import RoomsDAO

from app.hotels.rooms.models import Rooms

class HotelsDAO(BaseDAO):
    model = Hotels
    
    @classmethod
    async def get_hotels_by_location(cls, location:str): # получаем список отелей по location
            async with async_session_maker() as session:
                hotels_by_location = select(cls.model).where(cls.model.location.ilike(f'%{location}%'))
                result = await session.execute(hotels_by_location)
                hotels = result.scalars().all()
                if not hotels:
                     raise NoHotelsInLocation
                return hotels

    @classmethod
    async def get_hotels_data_with_rooms_left(cls, hotels: list[Hotels],date_from: date, date_to: date):# возвращает Отели с их атрибутами + количество оставшихся комнат в отеле
        hotels_with_available_rooms = []

        for hotel in hotels:
            booked_rooms = await RoomsDAO.get_hotel_booked_rooms(hotel.id, date_from, date_to)# Подсчет забронированных номеров
            rooms_left = hotel.rooms_quantity - len(booked_rooms)# Расчет оставшихся(незабронированных) номеров
            # Сбор информации об отеле и оставшихся номерах в словарь
            hotel_data = {
                **hotel.__dict__,
                'rooms_left': rooms_left
            }
            hotels_with_available_rooms.append(hotel_data)
        return hotels_with_available_rooms

    @classmethod
    async def get_hotels_by_location_with_available_rooms(cls, location: str, date_from: date, date_to: date):
        hotels = await cls.get_hotels_by_location(location)
        return await cls.get_hotels_data_with_rooms_left(hotels,date_from,date_to)
    
    @classmethod
    async def get_specific_hotel(cls, id:str): #возвращает отель по id
         return await cls.find_one_or_none(id = id)
        # @classmethod
    # async def get_hotel_by_location(cls, location: str):
    #     async with async_session_maker() as session:
    #         # stmt = select(cls.model).where(cls.model.location.ilike(f'%{location}%'))
    #         hotels_by_location = select(cls.model).where(cls.model.location.ilike(f'%{location}%'))
    #         result = await session.execute(hotels_by_location)
    #         return result.scalars().all()