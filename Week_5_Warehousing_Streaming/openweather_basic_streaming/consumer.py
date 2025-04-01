from google.oauth2 import service_account
import pandas as pd
from pandas_gbq import to_gbq
from kafka import KafkaConsumer
import json

PROJECT_ID = "my-bigquery-project-453503"
DATASET_ID = "weather_dataset"
TABLE_ID = "weather_table123"
TABLE_FULL_ID = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
SERVICE_ACCOUNT_FILE = "/app/config/gcs_config.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

consumer = KafkaConsumer(
    "weather",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
)

print("🚀 Listening for messages...")

for message in consumer:
    weather_data = message.value
    print(f"📩 Received: {weather_data}")

    try:
        # Chuyển đổi dữ liệu thành DataFrame
        df = pd.DataFrame([weather_data])

        # ✅ Fix lỗi timestamp
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

        # Đẩy dữ liệu vào BigQuery
        to_gbq(
            df,
            TABLE_FULL_ID,
            project_id=PROJECT_ID,
            credentials=credentials,
            if_exists="replace",
        )
        print("✅ Dữ liệu đã đẩy vào BigQuery thành công!")

    except Exception as e:
        print(f"❌ Lỗi khi upload dữ liệu: {e}")
