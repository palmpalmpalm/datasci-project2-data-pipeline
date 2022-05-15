from sqlalchemy import  Column, ForeignKey, String, Date, Float, Integer, RealQuantity, Boolean
from ..database.init_db import Base

class SFA(Base):
    __tablename__ = "sfa"
    
    sfa_id = Column(String(100), primary_key=True)
    sfa_temp = Column(Float)
    sfa_humid = Column(Float)
    sfa_pm25_corrected = Column(Float)
    sfa_pm10_corrected = Column(Float)
    sfa_lat = Column(RealQuantity)
    sfa_long = Column(RealQuantity)

    
    