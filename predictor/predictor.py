from fastapi import FastAPI
from fastapi import status
from dotenv import load_dotenv, find_dotenv
from tensorflow import keras
import requests
import os
import pandas as pd
import joblib
import numpy as np
from datetime import timedelta
from datetime import datetime

# Get data from .env
dotenv_path = os.path.join('.env')
load_dotenv(dotenv_path)

API_ENDPOINT = os.environ.get("API_ENDPOINT")
API_PORT = os.environ.get("API_PORT")

# Create database endpoint from .env
API_URL = f"http://{API_ENDPOINT}:{API_PORT}"
# API_URL = "http://localhost:8000"

# Init fastapi server
app = FastAPI()

# Model constraints
TS = 72

# Demo model class
class Model:
    def __init__(self) -> None:
        self.scaler = joblib.load('./data/scaler.save')
        self.yscaler = joblib.load('./data/yscaler.save')
        self.model = keras.models.load_model('./data/my_model.h5')

    def transform(self, data):
        return self.scaler.transform(data)
    
    def inverse_transform(self, data):
        return self.yscaler.inverse_transform(data)
    
    def predict(self, data):
        return self.model.predict(data)

# Init model
model = Model()

# insert prediction result to database
def insert_data(data):
    url = API_URL + "/predict/insert"
    res = requests.post(url=url, json=data.json())
    print(res.json())

# get latest data
def get_latest_data(station_id:str):
    url = API_URL + "/cleaned_earthnull/latest-by-station/stations/"
    url += station_id + "/limits/" + str(TS) # get latest 72 time stamps
    req = requests.get(url=url)
    return req


# api for get lastest data -> inference the data -> insert prediction's result to database
@app.post("/predict-and-post")
async def predict_and_post():
    # for loop each station
    # prepare data for predict
    data = get_latest_data("1")  
    if (data == ""):
        return status.HTTP_417_EXPECTATION_FAILED    
    
    df = pd.DataFrame(data.json())
    print(df.shape)
    
    if (df.shape[0] < 72):
        return status.HTTP_406_NOT_ACCEPTABLE
    
    predicted_desc = {
        "predicted_station_id": "string",
        "predicted_start_time": "2022-05-20T12:07:28.364Z",
        "predicted_timestamp": "2022-05-20T12:07:28.364Z",
        "predicted_interval_length": 0,
        "predicted_n_interval": 0,
        "predicted_lat": 0,
        "predicted_long": 0,
        "predicted_result": "string"
    }
    
    df_present = df.iloc[0]
    df_last = df.iloc[71]
    print(df_present)
    print(df_last)

    
    df_selected = df[['cleaned_earthnull_temp', 'cleaned_earthnull_wind_speed', 'cleaned_earthnull_wind_dir',
                      'cleaned_earthnull_RH', 'cleaned_earthnull_pm25', 'cleaned_earthnull_station_id']]
    
    df_scale = model.transform(df_selected)      
    
    df_format = np.array([df_scale])
    
    predicted = model.predict(df_format)
    
    result = model.inverse_transform(predicted.reshape(-1, 1))
    
    print(result)
    
    # insert_data(predicted)
    
    #return insert_data(model.predict(data))