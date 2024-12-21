from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'clone_dev_database_dag',
    default_args=default_args,
    description='Daily cloning of production database for development testing',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

# Define the cloning task
clone_dev_db = SnowflakeOperator(
    task_id='clone_dev_database',
    sql="""
    CREATE OR REPLACE DATABASE dev_product_catalog CLONE product_catalog;
    """,
    snowflake_conn_id='snowflake_conn',
    dag=dag
)
