from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
import requests
import random
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(dotenv_path)

POSTGRES_USER=os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB=os.environ.get("POSTGRES_DB")

SCRAPER_ENDPOINT=os.environ.get("SCRAPER_ENDPOINT")
SCRAPER_PORT=os.environ.get("SCRAPER_PORT")

PREDICTOR_ENDPOINT=os.environ.get("PREDICTOR_ENDPOINT")
PREDICTOR_PORT=os.environ.get("PREDICTOR_PORT")

args = {
    'owner' : 'datasci-project2',
    'start_date' : datetime(2022, 5, 15)
}
    
def trigger_scraper():
    url = f"http://{SCRAPER_ENDPOINT}:{SCRAPER_PORT}" # end point path + "/"
    req = requests.get(url)
    print(req.json())

def trigger_predictor():
    url = f"http://{PREDICTOR_ENDPOINT}:{PREDICTOR_PORT}" # end point path + "/"
    req = requests.get(url)
    print(req.json())

dag = DAG(dag_id='pipline_dag', 
          default_args=args, 
          schedule_interval='*/1 * * * *', # run every 1 minute for hourly, use '@hourly'
          description='Data Pipeline for Data Science Project 2', 
          catchup=False) 

with dag:
    scraping = PythonOperator(
        task_id = 'Scrape data from websites and insert them to database',
        python_callable = trigger_scraper,    
    )
    
    predicting = PythonOperator(
        task_id = 'Predict future PM2.5 with cleaned data and insert them to database',
        python_callable = trigger_predictor,
    )
    
    scraping >> predicting