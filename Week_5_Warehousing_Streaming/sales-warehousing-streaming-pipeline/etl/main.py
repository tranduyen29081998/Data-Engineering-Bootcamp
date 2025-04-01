from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import upload_to_bq
from google.oauth2 import service_account

# Cấu hình thông tin BigQuery
PROJECT_ID = "my-bigquery-project-453503"  # Thay bằng ID thật của bạn
DATASET_ID = "sales"  # Thay bằng dataset của bạn
TABLE_ID = "sales_table"  # Thay bằng tên bảng đã tạo trong BigQuery
SERVICE_ACCOUNT_FILE = "/opt/airflow/config/gcs_config.json"

# Đọc credentials từ service account
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

FILE_PATH = "data/raw/sales_data.csv"  # Đường dẫn tới file dữ liệu gốc


def run_pipeline():
    """Chạy pipeline ETL: Extract, Transform, Load vào BigQuery."""
    # 1. Extract: Đọc dữ liệu từ file CSV
    df = extract_data(FILE_PATH)

    # 2. Transform: Làm sạch và tính toán tổng doanh thu
    df = transform_data(df)

    df.to_csv("data/processed/sales_processed.csv", index=False)

    # 4. Load: Tải dữ liệu vào BigQuery
    upload_to_bq(df, PROJECT_ID, DATASET_ID, TABLE_ID, credentials)


# Chạy pipeline
run_pipeline()
