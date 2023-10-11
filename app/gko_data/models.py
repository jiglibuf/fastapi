from sqlalchemy import Column, Date, Float,Integer,String
from app.database import Base

class GKO_data(Base):
    __tablename__ = 'gko_data'

    id = Column(Integer, primary_key=True)
    kn = Column(String(20),nullable=False)
    kc = Column(Float, nullable=False)
    doc_type = Column(String, nullable=False)
    doc_num = Column(String,nullable=False)
    doc_date = Column(Date,nullable=False)
    doc_name = Column(String,nullable=False)
    url = Column(String,nullable=False)
    date_time = Column(Date,nullable=False)
    author = Column(String,nullable=False)
    comment = Column(String,nullable=True)
    date_found = Column(Date,nullable=False)
    status = Column(String,nullable=True)
    date_start = Column(Date,nullable=False)
    date_placement = Column(Date,nullable=True)

