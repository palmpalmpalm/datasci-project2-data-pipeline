from typing import List, Optional
from datetime import date
from uuid import UUID
from pydantic import BaseModel


class SFABase(BaseModel):
    class Config:
        orm_mode = True

class SFAAttribute(SFABase):
    sfa_time_aq : Optional[date] = None
    sfa_temp : Optional[float] = None
    sfa_humid : Optional[float] = None
    sfa_pm25_corrected : Optional[float] = None
    sfa_pm10_corrected : Optional[float] = None
    sfa_lat : Optional[float] = None
    sfa_long : Optional[float] = None

