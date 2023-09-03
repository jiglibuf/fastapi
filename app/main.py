from fastapi import FastAPI,Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class SHotel(BaseModel):#схема ответа на гет запрос
    address: str
    name: str
    stars: int

class HotelsSearchArgs:# схема гет запроса
    def __init__(
        self,
        location: str,
        date_from: date, 
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5)
    ):
        self.location = location        
        self.date_from = date_from        
        self.date_to = date_to        
        self.has_spa = has_spa        
        self.stars = stars        
        

@app.get('/hotels',response_model=list[SHotel])
def get_hotels(
    seatch_args: HotelsSearchArgs = Depends()
):
    return seatch_args

class SBooking(BaseModel): #схема пост запроса
    room_id: int
    date_from: date 
    date_to: date
    cost: float

@app.post('/bookings')
def add_booking(booking:SBooking):
    pass
#ааааааааааа учусь
