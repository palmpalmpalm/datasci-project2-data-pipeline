from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import requests
import os
import random

# get data from .env
dotenv_path = os.path.join(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(dotenv_path)

API_ENDPOINT = os.environ.get("API_ENDPOINT")
API_PORT = os.environ.get("API_PORT")

API_URL = f"{API_ENDPOINT}:{API_PORT}"

# Init fastapi server
app = FastAPI()

# Data schema


class Data(BaseModel):
    demo_int: int
    demo_float: float

# Demo model class


class DemoModel:
    def __init__(self) -> None:
        # load weight here
        self.name = 'demo model'

    def predict(data: Data):
        # Real model should pass the data to the model
        return random.uniform(0, 1)


# Init model
demo_model = DemoModel()

# insert prediction result to database


def insert_data(data):
    url = 'http://localhost:8000/predicted/insert'
    res = requests.post(url=url, json=data.json())
    print(res.json())

# get latest data


def get_latest_data(stationid):
    url = 'http://localhost:8000/predicted/cleaned_earthnull/'+str(stationid)
    req = requests.get(url=url)
    print(len(req.json()))
    return req.json()


# api for get lastest data -> inference the data -> insert prediction's result to database
@app.post("/predict-and-post")
async def predict_and_post():
    # for loop each station
    data = get_latest_data()
    predicted = demo_model.predict(data)

    insert_data(demo_model.predict(data))
    #
    return insert_data(demo_model.predict(data))
