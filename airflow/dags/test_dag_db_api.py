from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta

import requests
import random

args = {
    'owner' : 'datasci-project2',
    'start_date' : datetime(2022, 5, 15)
}


dag = DAG(dag_id='test_dag_db_api', default_args=args, schedule_interval='*/1 * * * *', description='my test DAG',catchup=False) # run every 1 minute

def insert_data():
    url = 'http://host.docker.internal:8000/pcd/insert'
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
    url = 'http://host.docker.internal:8000/pcd/all'
    req = requests.get(url = url)
    print(len(req.json()))

with dag:
    run_this_task = PythonOperator(
        task_id = 'insert_random_data_to_db',
        python_callable = insert_data,    
    )
    
    run_this_task2 = PythonOperator(
        task_id = 'get_all_data_from_db',
        python_callable = get_data,
    )
    
    run_this_task >> run_this_task2