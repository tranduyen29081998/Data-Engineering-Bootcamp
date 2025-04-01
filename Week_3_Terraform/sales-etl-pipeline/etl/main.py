from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import upload_to_gcs

FILE_PATH = "data/raw/sales_data.csv"
BUCKET_NAME = "sales-bucket-2908199829081998"


def run_pipeline():

    df = extract_data(FILE_PATH)
    # print(df)
    df_transformed = transform_data(df)
    df_transformed.to_csv("data/processed/sales_processed.csv", index=False)
    upload_to_gcs(
        BUCKET_NAME,
        "data/processed/sales_processed.csv",
        "processed_data/sales_processed.csv",
    )
