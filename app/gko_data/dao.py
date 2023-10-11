#Data access object (работаем с бд)
from app.dao.base import BaseDAO
from app.gko_data.models import GKO_data

class GKO_DataDAO(BaseDAO):
    model = GKO_data
