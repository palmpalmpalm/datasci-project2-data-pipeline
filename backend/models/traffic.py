from sqlalchemy import  Column, ForeignKey, String, Date, Float, Integer, RealQuantity, Boolean
from ..database.init_db import Base
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

class Traffic(Base):
    __tablename__ = "traffic"
    
    traffic_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    traffic_datetime = Column(Date)
    traffic_index = Column(Float)

    
    