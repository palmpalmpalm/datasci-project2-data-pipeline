from fastapi import HTTPException, status
from sqlalchemy.orm import Session ,load_only
from app.models.sfa import SFA
from app.schemas.sfa import SFAAttribute
from datetime import date


def insert_sfa(request:SFAAttribute, db:Session):
    db_sfa = SFA(sfa_time_aq  = request.sfa_time_aq,
                 sfa_temp = request.sfa_temp,
                 sfa_humid = request.sfa_humid,
                 sfa_pm25_corrected= request.sfa_pm25_corrected,
                 sfa_pm10_corrected  = request.sfa_pm10_corrected ,
                 sfa_lat = request.sfa_lat,
                 sfa_long  = request.sfa_long)
    db.add(db_sfa)
    db.commit()
    db.refresh(db_sfa)
    return db_sfa

def get_all_sfa(db: Session):
    return db.query(SFA).all()

def get_sfa_by_date(datetime:date, db:Session):
    pass

def get_sfa_by_range_date(from_date:date, til_date:date, db:Session):
    pass

def get_sfa_by_date(datetime:date, db:Session):
    pass