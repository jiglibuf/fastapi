from datetime import date
from pydantic import BaseModel
#схема ответа 
class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

class SBookingsWithRoomData(SBooking):
    image_id:int
    name: str
    description: str
    services: dict