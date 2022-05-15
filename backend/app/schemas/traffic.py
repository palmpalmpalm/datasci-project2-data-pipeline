from typing import List, Optional
from datetime import date
from uuid import UUID
from pydantic import BaseModel


class TrafficBase(BaseModel):
    class Config:
        orm_mode = True

class TrafficAttribute(TrafficBase):
    traffic_datetime : Optional[date] = None
    traffic_index : Optional[float] = None
    
