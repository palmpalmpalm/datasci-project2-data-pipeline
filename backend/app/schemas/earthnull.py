from typing import List, Optional
from datetime import date
from uuid import UUID
from pydantic import BaseModel


class EarthNullBase(BaseModel):
    class Config:
        orm_mode = True

class PCDAttribute(EarthNullBase):    
    earthnull_timestamp = Optional[date] = None
    earthnull_station_id = Optional[str] = None
    earthnull_lat = Optional[float] = None
    earthnull_long = Optional[float] = None
    earthnull_pm25 = Optional[float] = None
    earthnull_PM10 = Optional[float] = None
    earthnull_wind_dir = Optional[int] = None
    earthnull_wind_speed = Optional[int] = None
    earthnull_RH = Optional[int] = None
