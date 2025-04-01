def transform_data(df):
    """Làm sạch dữ liệu & tính tổng doanh thu"""
    df = df.dropna()
    df["Total sales"] = df["Quantity"] * df["Price"]
    return df
