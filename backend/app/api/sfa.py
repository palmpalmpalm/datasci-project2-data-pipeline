from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from app.database import init_db
from sqlalchemy.orm import Session
from app.schemas.sfa import SFAAttribute
from app.crud.sfa import insert_sfa, get_all_sfa


router = APIRouter(
    prefix = "/sfa",
    tags = ['SFA'],
    responses = {404 : {'message' : 'Not found'}}
)

get_db = init_db.get_db

@router.post("/insert", response_model=SFAAttribute, status_code=status.HTTP_201_CREATED)
async def insert_sfa_data(request:SFAAttribute, db:Session = Depends(get_db)):
    return insert_sfa(request, db)


@router.get("/all", response_model = List[SFAAttribute])
async def get_all_sfa_data(db:Session = Depends(get_db)):
    return get_all_sfa(db)