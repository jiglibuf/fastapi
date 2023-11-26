from fastapi import FastAPI,Query, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


from app.users.router import router as router_users
from app.bookings.router import router as router_bookings
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms
from app.pages.router import router as router_pages
from app.images.router import router as router_images

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_users) #подключение роутера для пользователей
app.include_router(router_bookings) #подключение роутера для бронирований
app.include_router(router_hotels)
app.include_router(router_pages)# html страницы
app.include_router(router_images) # роутер добавления картинок



origins = [
    "http://localhost:3000"
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", 
                   "Access-Control-Allow-Origin", "Authorization"],
)














#------------------------------------------------------------------------------
# app.include_router(router_rooms)
# class SHotel(BaseModel):#схема ответа на гет запрос
#     address: str
#     name: str
#     stars: int

# class HotelsSearchArgs:# схема гет запроса
#     def __init__(
#         self,
#         location: str,
#         date_from: date, 
#         date_to: date,
#         has_spa: Optional[bool] = None,
#         stars: Optional[int] = Query(None, ge=1, le=5)
#     ):
#         self.location = location        
#         self.date_from = date_from        
#         self.date_to = date_to        
#         self.has_spa = has_spa        
#         self.stars = stars        
        

# @app.get('/hotels',response_model=list[SHotel])
# def get_hotels(
#     search_args: HotelsSearchArgs = Depends()
# ):
#     return search_args

# class SBooking(BaseModel): #схема пост запроса
#     room_id: int
#     date_from: date 
#     date_to: date
#     cost: float

# @app.post('/bookings')
# def add_booking(booking:SBooking):
#     pass
#установил зависимости
