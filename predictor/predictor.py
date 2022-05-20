from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import requests
import os
import random
import pandas as pd
import sklearn
import joblib

# get data from .env
dotenv_path = os.path.join(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(dotenv_path)

API_ENDPOINT = os.environ.get("API_ENDPOINT")
API_PORT = os.environ.get("API_PORT")

API_URL = f"http://{API_ENDPOINT}:{API_PORT}"

# Init fastapi server
app = FastAPI()

# Demo model class
class DemoModel:
    def __init__(self) -> None:
        # load weight here
        self.name = 'demo model'

    def predict(data):
        # Real model should pass the data to the model
        return random.uniform(0, 1)

# Init model
demo_model = DemoModel()

# insert prediction result to database
def insert_data(data):
    url = API_ENDPOINT + "/predict/insert"
    res = requests.post(url=url, json=data.json())
    print(res.json())

# get latest data
def get_latest_data(stationid):
    url = API_ENDPOINT + "/cleaned_earthnull/latest-by-station/stations/"
    url +=  str(stationid)+'/limits/'+str(72)
    req = requests.get(url=url)
    print(len(req.json()))
    return req.json()


# api for get lastest data -> inference the data -> insert prediction's result to database
@app.post("/predict-and-post")
async def predict_and_post():
    # for loop each station
    # prepare data for predict
    data = get_latest_data()
    df = pd.DataFrame(data)
    df_selected = df[['cleaned_earthnull_temp', 'cleaned_earthnull_wind_speed', 'cleaned_earthnull_wind_dir',
                      'cleaned_earthnull_RH', 'cleaned_earthnull_pm25', 'cleaned_earthnull_station_id']]
    scaler = joblib.load(
        'datasci-project2-data-pipeline/predictor/data/scaler.save')
    df_scale = scaler.transform(df_selected)

    predicted = demo_model.predict(data)

    insert_data(demo_model.predict(data))
    #
    return insert_data(demo_model.predict(data))
