from fastapi import HTTPException, status
from sqlalchemy.orm import Session ,load_only
from app.models.traffic import Traffic
from app.schemas.traffic import TrafficAttribute
from datetime import date


def insert_traffic(request:TrafficAttribute, db:Session):
    db_traffic = Traffic(traffic_datetime  = request.traffic_datetime,
                 traffic_index = request.traffic_index
                 )
    db.add(db_traffic)
    db.commit()
    db.refresh(db_traffic)
    return db_traffic

def get_all_traffic(db: Session):
    return db.query(Traffic).all()

def get_traffic_by_date(datetime:date, db:Session):
    pass

def get_traffic_by_range_date(from_date:date, til_date:date, db:Session):
    pass

def get_traffic_by_date(datetime:date, db:Session):
    pass