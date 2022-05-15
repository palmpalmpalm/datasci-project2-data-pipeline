from sqlalchemy import  Column, String, Date, Float, Integer, RealQuantity, Boolean
from sqlalchemy.dialects.postgresql import UUID
from ..database.init_db import Base

class PCD(Base):
    __tablename__ = "pcd"
    
    pcd_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    pcd_lat = Column(RealQuantity)
    pcd_long = Column(RealQuantity)
    pcd_date_aq = Column(Date)
    pcd_pm25 = Column(Float)
    pcd_PM10 = Column(Float)
    pcd_aqi = Column(Integer)
    pcd_ground = Column(Boolean)
    pcd_mobile = Column(Boolean)
    
    