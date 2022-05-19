from sqlalchemy import  Column, String, Date, Float, Integer, Boolean
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from ..database.init_db import Base

class PCD(Base):
    __tablename__ = "pcd"
    
    pcd_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    pcd_lat = Column(Float)
    pcd_long = Column(Float)
    pcd_date_aq = Column(Date)
    pcd_pm25 = Column(Float)
    pcd_pm10 = Column(Float)
    pcd_aqi = Column(Integer)
    pcd_ground = Column(Boolean)
    pcd_mobile = Column(Boolean)
    
