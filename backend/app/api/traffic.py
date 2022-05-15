from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from app.database import init_db
from sqlalchemy.orm import Session
from app.schemas.traffic import TrafficAttribute
from app.crud.traffic  import insert_traffic , get_all_traffic 


router = APIRouter(
    prefix = "/traffic ",
    tags = ['Traffic'],
    responses = {404 : {'message' : 'Not found'}}
)

get_db = init_db.get_db

@router.post("/insert", response_model=TrafficAttribute, status_code=status.HTTP_201_CREATED)
async def insert_traffic_data(request:TrafficAttribute, db:Session = Depends(get_db)):
    return insert_traffic(request, db)


@router.get("/all", response_model = List[TrafficAttribute])
async def get_all_traffic_data(db:Session = Depends(get_db)):
    return get_all_traffic(db)