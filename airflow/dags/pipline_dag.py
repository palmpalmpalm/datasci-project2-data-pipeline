from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
import subprocess
import requests
import random

subprocess.call('pip3 install python-dotenv')
from dotenv import load_dotenv



dotenv_path = os.path.join(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(dotenv_path)

POSTGRES_USER=os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB=os.environ.get("POSTGRES_DB")

SCRAPER_ENDPOINT=os.environ.get("SCRAPER_ENDPOINT")
SCRAPER_PORT=os.environ.get("SCRAPER_PORT")

CLEANSING_ENDPOINT=os.environ.get("CLEANSING_ENDPOINT")
CLEANSING_PORT=os.environ.get("CLEANSING_PORT")

PREDICTOR_ENDPOINT=os.environ.get("PREDICTOR_ENDPOINT")
PREDICTOR_PORT=os.environ.get("PREDICTOR_PORT")

args = {
    'owner' : 'datasci-project2',
    'start_date' : datetime(2022, 5, 15)
}


dag = DAG(dag_id='pipline_dag', default_args=args, schedule_interval='*/1 * * * *', description='data pipeline for data science project 2',catchup=False) # run every 1 minute

# def insert_data():
#     url = 'http://host.docker.internal:8000/pcd/insert'
#     data = {
#         "pcd_lat": random.uniform(0, 1),
#         "pcd_long": random.uniform(0, 1),
#         "pcd_date_aq": None,
#         "pcd_pm25": 1.3,
#         "pcd_PM10": 0,
#         "pcd_aqi": 0,
#         "pcd_ground": True,
#         "pcd_mobile": True
#     }
#     res = requests.post(url = url, json = data)
#     print(res.json())
    
# def get_data():
#     url = 'http://host.docker.internal:8000/pcd/all'
#     req = requests.get(url = url)
#     print(len(req.json()))

def test():
    print('hi')

with dag:
    run_this_task = PythonOperator(
        task_id = 'insert_random_data_to_db',
        python_callable = test,    
    )
    
    run_this_task2 = PythonOperator(
        task_id = 'get_all_data_from_db',
        python_callable = test,
    )
    
    run_this_task >> run_this_task2