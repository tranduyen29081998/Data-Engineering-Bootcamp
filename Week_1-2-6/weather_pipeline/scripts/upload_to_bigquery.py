from google.oauth2 import service_account
import pandas as pd
from pandas_gbq import to_gbq
import os

# Cấu hình thông tin BigQuery
PROJECT_ID = "my-bigquery-project-453503"  # Thay bằng ID thật của bạn
DATASET_ID = "weather_dataset"
TABLE_ID = "weather_table"
TABLE_FULL_ID = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

# Đường dẫn file service account
SERVICE_ACCOUNT_FILE = "/opt/airflow/config/service_account.json"

# Kiểm tra nếu file service account không tồn tại
if not os.path.exists(SERVICE_ACCOUNT_FILE):
    raise FileNotFoundError(f"❌ Không tìm thấy file {SERVICE_ACCOUNT_FILE}")

# Đọc credentials từ service account
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

# Đọc dữ liệu từ CSV
CSV_FILE = "/opt/airflow/data/weather_data.csv"  # Thay bằng đường dẫn file CSV thật
df = pd.read_csv(CSV_FILE)
# Đảm bảo cột timestamp có định dạng TIMESTAMP của BigQuery
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s", errors="coerce")
# Đẩy dữ liệu vào BigQuery
try:
    to_gbq(
        df,
        TABLE_FULL_ID,
        project_id=PROJECT_ID,
        credentials=credentials,
        if_exists="append",  # Thêm dữ liệu mới, không ghi đè
    )
    print("✅ Dữ liệu đã đẩy vào BigQuery thành công!")
except Exception as e:
    print(f"❌ Lỗi khi upload dữ liệu: {e}")
