from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker


class BookingDAO(BaseDAO):
    model = Bookings