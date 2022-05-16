from fastapi import HTTPException, status
from sqlalchemy.orm import Session ,load_only
from app.models.pcd import PCD
from app.schemas.pcd import PCDAttribute
from datetime import date


def insert_pcd(request:PCDAttribute, db:Session):
    db_pcd = PCD(pcd_lat = request.pcd_lat,
                 pcd_long = request.pcd_long,
                 pcd_date_aq = request.pcd_date_aq,
                 pcd_pm25 = request.pcd_pm25,
                 pcd_PM10 = request.pcd_PM10,
                 pcd_aqi = request.pcd_aqi,
                 pcd_ground = request.pcd_ground,
                 pcd_mobile = request.pcd_mobile)
    db.add(db_pcd)
    db.commit()
    db.refresh(db_pcd)
    return db_pcd

def get_all_pcd(db: Session):
    return db.query(PCD).all()

def get_pcd_by_date(datetime:date, db:Session):
    pass

def get_pcd_by_range_date(from_date:date, til_date:date, db:Session):
    pass

def get_pm25_by_date(datetime:date, db:Session):
    pass