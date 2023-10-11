#эндпоинты
from fastapi import APIRouter
from app.gko_data.dao import GKO_DataDAO

router = APIRouter(
    prefix='/data_gko',
    tags=["Данные из таблицы data"],
)


@router.get('')
async def get_GKO_Data():
    return await GKO_DataDAO.find_all()
     
    
