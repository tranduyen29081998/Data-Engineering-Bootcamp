from google.cloud import storage


def upload_to_gcs(bucket_name, file_path, destination_blob_name):
    """Tải file lên Google Cloud Storage"""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(file_path)
