from fastapi import FastAPI
from .database.init_db import engine
from .models.pcd import PCD
from .models.sfa import SFA
from .models.traffic import Traffic
from .api import pcd
from .api import sfa
from .api import traffic

PCD.metadata.create_all(bind=engine)
SFA.metadata.create_all(bind=engine)
Traffic.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pcd.router)
app.include_router(sfa.router)
app.include_router(traffic.router)


@app.get("/hello")
def hello():
    return "hello world"


