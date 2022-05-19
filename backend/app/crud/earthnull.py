from fastapi import HTTPException, status
from sqlalchemy.orm import Session ,load_only
from app.models.earthnull import EarthNull
from app.schemas.earthnull import EarthNullAttribute
from datetime import date


def insert_earthnull(request:EarthNullAttribute, db:Session):
    db_pcd = EarthNull(earthnull_station_id = request.earthnull_station_id,
                       earthnull_timestamp = request.earthnull_timestamp,
                       earthnull_lat = request.earthnull_lat,
                       earthnull_long = request.earthnull_long,
                       earthnull_pm25 = request.earthnull_pm25,
                       earthnull_pm10 = request.earthnull_pm10,
                       earthnull_wind_dir = request.earthnull_wind_dir,
                       earthnull_wind_speed = request.earthnull_wind_speed,
                       earthnull_RH = request.earthnull_RH)
    db.add(db_pcd)
    db.commit()
    db.refresh(db_pcd)
    return db_pcd

def get_all_earthnull(db: Session):
    return db.query(EarthNull).all()

def get_earthnull_by_date(datetime:date, db:Session):
    pass

def get_earthnull_by_range_date(from_date:date, til_date:date, db:Session):
    pass

def get_earthnull_by_date(datetime:date, db:Session):
    pass