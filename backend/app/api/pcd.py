from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from app.database import init_db
from sqlalchemy.orm import Session
from app.schemas.pcd import PCDBase
from app.crud.pcd import insert_pcd, get_all_pcd


router = APIRouter(
    prefix = "/pcd",
    tags = ['PCD'],
    responses = {404 : {'message' : 'Not found'}}
)

get_db = init_db.get_db

@router.post("/insert", response_model=PCDBase, status_code=status.HTTP_201_CREATED)
async def insert_pcd_data(request:PCDBase, db:Session = Depends(get_db)):
    return insert_pcd(request, db)


@router.get("/all", response_model = List[PCDBase])
async def get_pcd_data(db:Session = Depends(get_db)):
    return get_all_pcd(db)