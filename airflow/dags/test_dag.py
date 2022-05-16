from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

from datetime import datetime

args = {
    'owner' : 'testowner',
    'start_date' : days_ago(1)
}


dag = DAG(dag_id='my_test_dag', default_args=args, schedule_interval=None, description='my test DAG')

def run_this_func():
    print('hi')
    
def run_this_func2():
    print('hi2')

with dag:
    run_this_task = PythonOperator(
        task_id = 'run_this',
        python_callable = run_this_func,    
    )
    
    run_this_task2 = PythonOperator(
        task_id = 'run_this2',
        python_callable = run_this_func2,
    )
    
    run_this_task >> run_this_task2