from pydantic import BaseModel
#схема ответа 
class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int 


class SHotelWithRoomsLeft(SHotels):
    # hotel: SHotels
    rooms_left: int