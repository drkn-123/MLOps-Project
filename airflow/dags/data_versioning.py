from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import shutil

DATA_DIR = os.path.abspath("../../data/PetImages")
VERSIONED_DIR = os.path.abspath("../../data/versions")

def version_dataset():
    version_name = f"version_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    target_path = os.path.join(VERSIONED_DIR, version_name)
    shutil.copytree(DATA_DIR, target_path)
    print(f"Dataset versioned at: {target_path}")

with DAG("dataset_versioning_dag",
         start_date=datetime(2023, 1, 1),
         schedule_interval=None,
         catchup=False) as dag:

    task = PythonOperator(
        task_id="version_dataset",
        python_callable=version_dataset
    )