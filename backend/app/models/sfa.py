from sqlalchemy import  Column, ForeignKey, String, Date, Float, Integer, Boolean
from ..database.init_db import Base
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

class SFA(Base):
    __tablename__ = "sfa"
    
    sfa_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    sfa_time_aq = Column(Date)
    sfa_temp = Column(Float)
    sfa_humid = Column(Float)
    sfa_pm25_corrected = Column(Float)
    sfa_pm10_corrected = Column(Float)
    sfa_lat = Column(Float)
    sfa_long = Column(Float)

    
    