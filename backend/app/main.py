from fastapi import FastAPI
from .database.init_db import engine
from .models.pcd import PCD
from .api import pcd

PCD.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(pcd.router)


@app.get("/hello")
def hello():
    return "hello world"


