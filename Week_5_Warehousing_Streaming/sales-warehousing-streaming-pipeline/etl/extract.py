import pandas as pd
import logging


def extract_data(file_path):
    """Đọc dữ liệu từ CSV"""
    logging.info(f"📥 Đang đọc dữ liệu từ {file_path}")
    df = pd.read_csv(file_path)
    return df
