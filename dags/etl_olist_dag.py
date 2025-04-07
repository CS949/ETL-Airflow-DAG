from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(PROJECT_PATH)

from etl_olist_project import run_etl

default_args = {
    'owner': 'chaitanya',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='olist_etl_kpis',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['olist', 'etl', 'kpi']
) as dag:

    run_etl_task = PythonOperator(
        task_id='run_olist_etl',
        python_callable=run_etl,
    )

    run_etl_task
