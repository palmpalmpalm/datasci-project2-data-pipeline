from fastapi import FastAPI
from fastapi import status
from dotenv import load_dotenv
from tensorflow import keras
import requests
import os
import pandas as pd
import joblib
import uvicorn

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
class Model:
    def __init__(self) -> None:
        print(os.getcwd())
        self.scaler = joblib.load('./data/scaler.save')
        self.model = keras.models.load_model('./data/my_model.h5')

    def transform(self, data):
        return self.scaler.transform(data)
    
    def predict(self, data):
        return self.model.predict(data)

# Init model
model = Model()

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
    
    if (df.shape[0] == 0):
        return status.HTTP_204_NO_CONTENT
    
    df_selected = df[['cleaned_earthnull_temp', 'cleaned_earthnull_wind_speed', 'cleaned_earthnull_wind_dir',
                      'cleaned_earthnull_RH', 'cleaned_earthnull_pm25', 'cleaned_earthnull_station_id']]
    
    df_scale = model.transform(df_selected)      

    predicted = model.predict(df_scale)
    
    #insert_data(model.predict(data))
    
    #return insert_data(model.predict(data))

if __name__ == "__main__":
    uvicorn.run(app, port=7000, host='0.0.0.0')