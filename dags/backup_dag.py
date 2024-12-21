from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import snowflake.connector

# Function to create a daily backup
def create_daily_backup():
    current_date = datetime.now().strftime('%Y_%m_%d')
    conn = snowflake.connector.connect(
        user='<user>',
        password='<password>',
        account='<account>',
        warehouse='<warehouse>'
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE product_catalog_backup_{current_date} CLONE product_catalog;")
    cursor.close()
    conn.close()

# Function to manage backups and keep only the last 7 days
def cleanup_old_backups():
    conn = snowflake.connector.connect(
        user='<user>',
        password='<password>',
        account='<account>',
        warehouse='<warehouse>'
    )
    cursor = conn.cursor()
    cursor.execute("""
        SHOW DATABASES LIKE 'product_catalog_backup_%';
    """)
    databases = cursor.fetchall()
    
    # Filter backups older than 7 days
    retention_date = datetime.now() - timedelta(days=7)
    for db in databases:
        backup_name = db[1]  # Assuming database name is the second item
        date_str = backup_name.split('_')[-3:]  # Extract the date part
        backup_date = datetime.strptime('_'.join(date_str), '%Y_%m_%d')
        if backup_date < retention_date:
            cursor.execute(f"DROP DATABASE IF EXISTS {backup_name};")

    cursor.close()
    conn.close()

with DAG(
    'daily_backup_management_dag',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:

    # Task to create a daily backup
    backup_task = PythonOperator(
        task_id='create_daily_backup',
        python_callable=create_daily_backup
    )

    # Task to clean up backups older than 7 days
    cleanup_task = PythonOperator(
        task_id='cleanup_old_backups',
        python_callable=cleanup_old_backups
    )

    # Define task dependencies
    backup_task >> cleanup_task
def restore_latest_backup():
    conn = snowflake.connector.connect(
        user='<user>',
        password='<password>',
        account='<account>',
        warehouse='<warehouse>'
    )
    cursor = conn.cursor()
    # Get the most recent backup
    cursor.execute("SHOW DATABASES LIKE 'product_catalog_backup_%';")
    databases = cursor.fetchall()
    latest_backup = max(databases, key=lambda db: datetime.strptime(db[1].split('_')[-3:], '%Y_%m_%d'))
    latest_backup_name = latest_backup[1]

    # Create restored database
    cursor.execute(f"CREATE DATABASE product_catalog_restored CLONE {latest_backup_name};")
    cursor.close()
    conn.close()

restore_task = PythonOperator(
    task_id='restore_latest_backup',
    python_callable=restore_latest_backup,
    dag=dag  # Adding it to the existing DAG if needed
)
