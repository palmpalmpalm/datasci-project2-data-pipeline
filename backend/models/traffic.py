from sqlalchemy import  Column, ForeignKey, String, Date, Float, Integer, RealQuantity, Boolean
from ..database.init_db import Base

class Traffic(Base):
    __tablename__ = "traffic"
    

    
    