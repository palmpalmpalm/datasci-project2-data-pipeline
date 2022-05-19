import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random
import json


def insert_earthnull_data(i, name, lat, long):
    url = 'http://localhost:8000/earthnull/insert'
    timenow = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    print(i, name)
    data = {
        "earthnull_timestamp": timenow,
        "earthnull_station_id": i,
        "earthnull_station_name": name,
        "earthnull_region": name,
        "earthnull_province": name,
        "earthnull_lat": lat,
        "earthnull_long": long,
        "earthnull_pm25": random.randint(0, 100),
        "earthnull_pm10": random.randint(0, 100),
        "earthnull_wind_dir": random.randint(0, 365),
        "earthnull_wind_speed": random.randint(0, 200),
        "earthnull_RH": random.randint(0, 100)
    }
    res = requests.post(url=url, json=data)
    print(res.json())


def insert_cleaned_earthnull_data(i, name, lat, long):
    url = 'http://localhost:8000/cleaned_earthnull/insert'
    timenow = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    print(i, name)
    data = {
        "cleaned_earthnull_timestamp": timenow,
        "cleaned_earthnull_station_id": i,
        "cleaned_earthnull_station_name": name,
        "cleaned_earthnull_region": name,
        "cleaned_earthnull_province": name,
        "cleaned_earthnull_lat": lat,
        "cleaned_earthnull_long": long,
        "cleaned_earthnull_pm25": random.randint(0, 100),
        "cleaned_earthnull_pm10": random.randint(0, 100),
        "cleaned_earthnull_wind_dir": random.randint(0, 365),
        "cleaned_earthnull_wind_speed": random.randint(0, 200),
        "cleaned_earthnull_RH": random.randint(0, 100)
    }
    res = requests.post(url=url, json=data)
    print(res.json())


if __name__ == '__main__':

    name = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
    long = {1: 99.458001, 2: 103.439169,
            3: 101.378487, 4: 100.523237, 5: 99.673471}
    lat = {1: 18.104180, 2: 16.694087, 3: 12.769930, 4: 13.743236, 5: 7.888617}
    while (True):
        for i in range(1, 6):
            # insert_earthnull_data(str(i), name[i], lat[i], long[i])
            insert_cleaned_earthnull_data(str(i), name[i], lat[i], long[i])
        time.sleep(5)
        print('xx')
