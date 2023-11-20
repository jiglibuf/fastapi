from datetime import date
from pydantic import BaseModel
#схема ответа 
class SRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: dict
    quantity: int
    image_id: int

class SRoomsWithTotalCostAndRoomsLeft(SRooms):
    rooms_left: int
    total_cost: float