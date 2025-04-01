from pandas_gbq import to_gbq


def upload_to_bq(df, project_id, dataset_id, table_id, credentials):
    """Tải dữ liệu từ DataFrame lên BigQuery."""
    table_full_id = f"{project_id}.{dataset_id}.{table_id}"
    print("📊 Dữ liệu mẫu đã xử lý")
    print(df.head())

    try:
        # Đẩy dữ liệu vào BigQuery, thêm dữ liệu mới (if_exists='append')
        to_gbq(
            df,
            table_full_id,
            project_id=project_id,
            credentials=credentials,
            if_exists="append",
        )
        print(f"✅ Dữ liệu đã được tải lên BigQuery bảng {table_full_id} thành công!")
    except Exception as e:
        print(f"❌ Lỗi khi upload dữ liệu vào BigQuery: {e}")
