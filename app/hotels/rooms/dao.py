from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from sqlalchemy import  exists, insert, select, delete, func, and_, or_
from app.database import async_session_maker
from datetime import date


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def get_hotel_rooms(
        cls, 
        hotel:Hotels
        ): #возвращает номера отеля
         async with async_session_maker() as session:
            query = select(cls.model).where(cls.model.hotel_id == hotel.id)
            rooms = await session.execute(query)
            rooms = rooms.scalars().all()
            return rooms

    @classmethod
    async def get_rooms_left_for_room(
    cls, 
    room_id: int, 
    date_from: date, 
    date_to: date):#возвращает количество доступных (незабронированных) номеров для номера на выбранные даты
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                    and_(
                        Bookings.room_id == room_id,
                        or_(
                        and_(
                                Bookings.date_from >= date_from,
                                Bookings.date_to >= date_to,
                            ),
                            and_(
                                Bookings.date_from <= date_from,
                                Bookings.date_to > date_from,
                            )
                    )
                    )
                ).cte('booked_rooms')
            get_rooms_left = select(
                (Rooms.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
                                ).select_from(Rooms).join(
                                    booked_rooms,
                                    booked_rooms.c.room_id == Rooms.id,
                                    isouter=True
                                ).where(Rooms.id == room_id).group_by(Rooms.quantity, booked_rooms.c.room_id)
            # print(get_rooms_left.compile(engine, compile_kwargs = {"literal_binds": True}))
            get_rooms_left = await session.execute(get_rooms_left)
            rooms_left:int = get_rooms_left.scalar()
            return rooms_left
        
    @classmethod
    async def get_hotel_booked_rooms(
        cls, 
        hotel_id:int, 
        date_from: date, 
        date_to: date
        ):# получает все забронированные номера в отеле на выбранные даты
                async with async_session_maker() as session:
                    query = select(Bookings).where(# Подсчет забронированных номеров
                        and_(
                            Bookings.room_id == Rooms.id,
                            Bookings.date_from <= date_to,
                            Bookings.date_to >= date_from,
                            Rooms.hotel_id == hotel_id,
                        )
                    )
                    booked_rooms = await session.execute(query)
                    return booked_rooms.scalars().all()
    @classmethod
    async def get_available_rooms_data(
        cls, 
        hotel: Hotels,
        date_from: date, 
        date_to: date
        ): #rooms: list[Rooms],
        available_rooms = []
        rooms = await cls.get_hotel_rooms(hotel)
        for room in rooms:
            rooms_left = await cls.get_rooms_left_for_room(room.id, date_from, date_to)# Получаем количество забронированных комнат для данной комнаты в заданный период
            if rooms_left == 0:
                continue  # Пропускаем номера, у которых нет свободных номеров
            total_cost = (date_to - date_from).days * room.price
            room_data = {# Сбор информации об отеле и оставшихся номерах в словарь
                **room.__dict__,
                'rooms_left': rooms_left,
                'total_cost': total_cost,
            }
            available_rooms.append(room_data)
        return available_rooms
    
