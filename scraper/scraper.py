from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import requests
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from typing import List, Optional
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel




# get data from .env
dotenv_path = os.path.join(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(dotenv_path)

API_ENDPOINT = os.environ.get("API_ENDPOINT")
API_PORT = os.environ.get("API_PORT")

API_URL = f"{API_ENDPOINT}:{API_PORT}"

# Init fastapi server
app = FastAPI()

class EarthNullBase(BaseModel):
    class Config:
        orm_mode = True

# Data schema
class Data(BaseModel):
    earthnull_timestamp : Optional[datetime] = None
    earthnull_station_id : Optional[str] = None
    earthnull_station_name : Optional[str] = None
    earthnull_region : Optional[str] = None
    earthnull_province : Optional[str] = None
    earthnull_lat : Optional[float] = None
    earthnull_long : Optional[float] = None
    earthnull_pm25 : Optional[float] = None
    earthnull_pm10 : Optional[float] = None
    earthnull_wind_dir : Optional[int] = None
    earthnull_wind_speed : Optional[int] = None
    earthnull_RH : Optional[int] = None

def insert_data(data):
    url = 'http://localhost:8000/earthnull/insert'
    res = requests.post(url = url, json = data)
    print(res.json())

def waiting(driver):
    data_status = driver.find_element(By.XPATH,'/html/body/main/div[3]/div[1]/div')
    while data_status.text=="Downloading...":
        data_status = driver.find_element(By.XPATH,'/html/body/main/div[3]/div[1]/div')
        if data_status.text=="Downloading...":
            continue
        else :
            return

def insert_data(data):
    url = 'http://localhost:8000/earthnull/insert'
    res = requests.post(url = url, json = data)
    print(res.json())

def get_scrape_data():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    driver.get('https://google.com/%27')
    print(driver.page_source)
    driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

    positions = [(99.823357, 19.909242), (98.9881062, 18.7909205), (99.659873, 18.282664), (99.893048, 19.200226), (100.776359, 18.788878), (102.780926, 17.414174), (104.133216, 17.15662), (102.835251, 16.445329), (98.918138, 8.059199), (104.094535, 17.191391), (102.098301, 14.979726), (99.123056, 16.883611), (100.110542, 15.686254), (100.258056, 16.820833), (99.325355, 9.126057), (100.48404, 7.020545), (99.961469, 8.426923), (99.588743, 7.570238), (101.2831, 6.546197), (100.536443, 13.729984), (100.343164, 13.705582), (100.784069, 13.72205), (100.558606, 13.7619223), (100.785866, 13.570333), (101.286359, 13.588554), (100.977777, 13.355065), (101.098128, 13.054551), (101.180975, 12.706325), (102.523721, 12.234862)]
    station_id = ['57t', '36t', '40t', '70t', '67t', '91t', '90t', '46t', 'o20', 'm1', '47t', 'o35', '41t', '86t', '42t', '44t', '89t', '93t', '63t', '50t', 'bkp89t', 'bkp78t', 'bkp56t', '19t', '60t', '34t', '33t', '74t', '87t']
    last_date = datetime.datetime.now()
    first_date = last_date - datetime.timedelta(hours = 1)
    date_collect_temp = first_date
    hours_step = 1

    while date_collect_temp < last_date:
        year = date_collect_temp.strftime("%Y")
        month = date_collect_temp.strftime("%m")
        day = date_collect_temp.strftime("%d")
        hour = date_collect_temp.strftime("%H")
        local_time = date_collect_temp + datetime.timedelta(hours = 7)
        for i in range(len(positions)):
            lat = positions[i][1]
            long = positions[i][0]
            for j in range(5):
                ################ --------- Relative Humidity --------- ################
                if j == 0:
                    driver.get(f'https://earth.nullschool.net/#{year}/{month}/{day}/{hour}00Z/wind/surface/level/overlay=relative_humidity/orthographic=99.20,12.40,2283/loc={positions[i][0]},{positions[i][1]}')
                    waiting(driver)
                    data_RH = driver.find_element(By.XPATH,'//*[@id="spotlight-panel"]/div[3]/div')
                    RH_data = data_RH.text
                    # RH_collect.append(RH_data)
                
                ################ --------- PM 2.5 --------- ################
                elif j == 1:
                    driver.get(f'https://earth.nullschool.net/#{year}/{month}/{day}/{hour}00Z/particulates/surface/level/overlay=pm2.5/orthographic=99.20,12.40,2283/loc={positions[i][0]},{positions[i][1]}')
                    waiting(driver)
                    data_pm25 = driver.find_element(By.XPATH,'//*[@id="spotlight-panel"]/div[3]/div')
                    pm25_data = data_pm25.text
                    # pm25_collect.append(pm25_data)
                
                ################ --------- PM 10 --------- ################
                elif j == 2:
                    driver.get(f'https://earth.nullschool.net/#{year}/{month}/{day}/{hour}00Z/particulates/surface/level/overlay=pm10/orthographic=99.20,12.40,2283/loc={positions[i][0]},{positions[i][1]}')
                    waiting(driver)
                    data_pm10 = driver.find_element(By.XPATH,'//*[@id="spotlight-panel"]/div[3]/div')
                    pm10_data = data_pm10.text
                    # pm10_collect.append(pm10_data)
                
                ################ --------- Wind --------- ################
                elif j == 3:
                    driver.get(f'https://earth.nullschool.net/#{year}/{month}/{day}/{hour}00Z/wind/isobaric/850hPa/orthographic=99.20,12.40,2283/loc={positions[i][0]},{positions[i][1]}')
                    waiting(driver)
                    data_wind = driver.find_element(By.XPATH, '//*[@id="spotlight-panel"]/div[2]/div')
                    wind_data = data_wind.text
                    if wind_data.split("° @ ").__len__()!=2:
                        wind_dir =''
                        wind_speed=''
                    else :
                        wind_dir = wind_data.split("° @ ")[0]
                        wind_speed = wind_data.split("° @ ")[1]
                    # wind_dir_collect.append(wind_dir)
                    # wind_speed_collect.append(wind_speed)
                
                ################ --------- Temperature --------- ################
                else:
                    driver.get(f'https://earth.nullschool.net/#{year}/{month}/{day}/{hour}00Z/wind/surface/level/overlay=temp/orthographic=99.20,12.40,2283/loc={positions[i][0]},{positions[i][1]}')
                    waiting(driver)
                    data_temp = driver.find_element(By.XPATH,'//*[@id="spotlight-panel"]/div[3]/div')
                    temp_data = data_temp.text
                    # temp_collect.append(temp_data)
            data = {
                "earthnull_timestamp": str(local_time),
                "earthnull_station_id": station_id[i],
                "earthnull_lat": lat,
                "earthnull_long": long,
                "earthnull_pm25": pm25_data,
                "earthnull_pm10": pm10_data,
                "earthnull_wind_dir": wind_dir,
                "earthnull_wind_speed": wind_speed,
                "earthnull_RH": RH_data
            }
            insert_data(data)
        hours_added = datetime.timedelta(hours = hours_step)
        date_collect_temp = date_collect_temp + hours_added  


# api for get lastest data -> inference the data -> insert prediction's result to database
@app.post("/scrape-data")
async def scrape_data():
    get_scrape_data()
    return "very good"
