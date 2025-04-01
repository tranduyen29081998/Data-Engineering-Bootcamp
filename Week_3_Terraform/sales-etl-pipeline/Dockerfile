FROM apache/airflow:2.5.0

# Chạy với quyền root để thiết lập quyền file
USER root

# Tạo các thư mục cần thiết
RUN mkdir -p /opt/airflow/data /opt/airflow/config /opt/airflow/dags /opt/airflow/etl

# Cấp quyền đọc/ghi cho airflow
RUN chmod -R 777 /opt/airflow/data /opt/airflow/config /opt/airflow/dags /opt/airflow/etl || true

# Copy thư viện Python cần thiết
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt


# Chạy lại với quyền airflow
USER airflow
# Copy các thư mục source code vào đúng vị trí
COPY dags/ /opt/airflow/dags/
COPY etl/ /opt/airflow/etl/
COPY config/gcs_config.json /opt/airflow/config/gcs_config.json


