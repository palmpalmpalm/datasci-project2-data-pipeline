import random
import requests
from datetime import datetime
import json

def insert_data():
    url = 'http://localhost:8000/pcd/insert'
    data = {
        "pcd_lat": random.uniform(0, 1),
        "pcd_long": random.uniform(0, 1),
        "pcd_date_aq": None,
        "pcd_pm25": 1.3,
        "pcd_PM10": 0,
        "pcd_aqi": 0,
        "pcd_ground": True,
        "pcd_mobile": True
    }
    res = requests.post(url = url, json = data)
    print(res.json())
    
def get_data():
    url = 'http://localhost:8000/pcd/all'
    req = requests.get(url = url)
    print(len(req.json()))

def test():
    insert_data()
    get_data()
    

if __name__ == '__main__':
    test()