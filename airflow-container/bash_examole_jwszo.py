from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

def print_hello():
    return 'Bash example operator!'

dag = DAG('hello_create', description='Simple tutorial DAG',
          schedule_interval='*/5 * * * *',
          start_date=datetime(2019, 2, 21), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

run_this = BashOperator(
    task_id='run_after_loop',
    bash_command='touch example.txt && echo "test123" > /tmp/example.txt',
    dag=dag,
)

# hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> run_this
