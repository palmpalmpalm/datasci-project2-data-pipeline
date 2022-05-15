from typing import List, Optional
from datetime import date
from uuid import UUID
from pydantic import BaseModel


class PCDBase(BaseModel):
    pcd_lat : Optional[float] = None
    pcd_long : Optional[float] = None
    pcd_date_aq = Optional[date] = None
    pcd_pm25 = Optional[float] = None
    pcd_PM10 = Optional[float] = None
    pcd_aqi = Optional[int] = None
    pcd_ground = Optional[bool] = None
    pcd_mobile = Optional[bool] = None