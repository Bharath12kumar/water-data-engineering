from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

import sys

sys.path.insert(0,r'/home/sbharath9444/water-data-engineering/etl') 

from daily_summary_etl import daily_summary_elt
from monthly_summary_etl import monthly_summary_elt
from update_order_status import update_order_status

with DAG("water_distribution_dag",
         start_date=datetime(2026,5,1),
         schedule_interval='@daily',
         catchup=False) as dag:

    task1= PythonOperator(
        task_id='update_order_status',
        python_callable=update_order_status
    )

    task2= PythonOperator(
        task_id='daily_summary_elt',
        python_callable=daily_summary_elt
    )

    task3= PythonOperator(
        task_id='monthly_summary_elt',
        python_callable=monthly_summary_elt
    )


    task1 >> task2 >>task3








              








