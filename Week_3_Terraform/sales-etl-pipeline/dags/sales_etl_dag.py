import logging
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from datetime import timedelta

from etl.main import run_pipeline

# Cấu hình logger của Airflow
logger = logging.getLogger(__name__)

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


@dag(
    schedule="0 3 * * *",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=["sales", "ETL"],
)
def sales_etl_pipeline():

    @task()
    def run_sales_etl():
        logger.info("DAG file is being loaded...")  # Debug thông báo khi DAG được load
        try:
            logger.info("Running the ETL pipeline...")  # Debug khi chạy pipeline
            run_pipeline()
            logger.info(
                "ETL pipeline completed successfully."
            )  # Debug sau khi pipeline chạy xong
        except Exception as e:
            logger.error(
                f"Error occurred while running the ETL pipeline: {str(e)}"
            )  # Log lỗi nếu có exception
            raise  # Raise lại exception để Airflow biết có lỗi xảy ra

    run_sales_etl()


dag = sales_etl_pipeline()
