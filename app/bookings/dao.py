from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.rooms.dao import RoomsDAO
from sqlalchemy import  insert, select, delete, func, and_, or_, join
from app.database import async_session_maker
from app.hotels.rooms.models import Rooms
from datetime import date
from app.database import engine

class BookingDAO(BaseDAO):  
    model = Bookings

    @classmethod
    async def add(
        cls, 
        room_id: int,
        date_from: date,
        date_to: date,
        user_id: int,
        ):# добавление строки в бд
            rooms_left = await RoomsDAO.get_rooms_left_for_room(room_id, date_from, date_to)
            async with async_session_maker() as session:
                if rooms_left > 0:
                    get_price = select(Rooms.price).filter_by(id=room_id)
                    price = await session.execute(get_price)
                    price: int = price.scalar()
                    add_booking = insert(Bookings).values(
                        room_id = room_id,
                        user_id = user_id,
                        date_from = date_from,
                        date_to = date_to,
                        price = price,
                    ).returning(Bookings)
                    new_booking = await session.execute(add_booking)
                    await session.commit()
                    return new_booking.scalar()
                else:
                     return None
                
    @classmethod
    async def get_user_bookings(cls, user_id: int):
        async with async_session_maker () as session:
            
            '''SELECT 
                b.room_id,
                b.user_id,
                b.date_from,
                b.date_to,
                b.price,
                b.total_cost,
                b.total_days,
                r.image_id,
                r.name,
                r.description,
                r.services
            FROM 
                bookings b
            JOIN 
                rooms r ON b.room_id = r.id
            WHERE 
                b.user_id = 5;'''

            query = select(
                Bookings.room_id,
                Bookings.user_id,
                Bookings.date_from,
                Bookings.date_to,
                Bookings.price,
                Bookings.total_cost,
                Bookings.total_days,
                Rooms.image_id,
                Rooms.name,
                Rooms.description,
                Rooms.services
            ).join(
                Rooms, Bookings.room_id == Rooms.id
            ).filter(
                Bookings.user_id == user_id
            )

            result = await session.execute(query)
            return result.mappings().all()
                  
         