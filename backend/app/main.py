from fastapi import FastAPI
from .database.init_db import engine
# from .models.pcd import PCD
# from .models.sfa import SFA
# from .models.traffic import Traffic
from .models.earthnull import EarthNull
from .models.predicted import Predicted
# from .api import pcd
# from .api import sfa
# from .api import traffic
from .api import earthnull
from .api import predicted

# PCD.metadata.create_all(bind=engine)
# SFA.metadata.create_all(bind=engine)
# Traffic.metadata.create_all(bind=engine)
EarthNull.metadata.create_all(bind=engine)
Predicted.metadata.create_all(bind=engine)


app = FastAPI(title='Data Sciene Project 2 Database Management')

# app.include_router(pcd.router)
# app.include_router(sfa.router)
# app.include_router(traffic.router)
app.include_router(earthnull.router)
app.include_router(predicted.router)
