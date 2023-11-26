from fastapi import APIRouter

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.hotels.router import get_hotels_by_location_with_available_rooms
from app.hotels.schemas import SHotelWithRoomsLeft


router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]
)
@router.get("/hotels", response_model=list[SHotelWithRoomsLeft])
async def get_hotels(request: Request, hotels=Depends(get_hotels_by_location_with_available_rooms)):
    return hotels


#----------------------КАК ВЫ КУРСЕ-------------------------------------
# templates = Jinja2Templates(directory="app/templates")

# @router.get("/hotels", response_class=HTMLResponse)
# async def get_hotels_page(
#     request:Request,
#     hotels = Depends(get_hotels_by_location_with_available_rooms)
# ):
#     return templates.TemplateResponse(
#         name='hotels.html', 
#         context={'request': request, 'hotels':hotels}
#         )



# @router.get("/login", response_class=HTMLResponse)
# async def get_login_page(request: Request):
#     return templates.TemplateResponse("auth/login.html", {"request": request})