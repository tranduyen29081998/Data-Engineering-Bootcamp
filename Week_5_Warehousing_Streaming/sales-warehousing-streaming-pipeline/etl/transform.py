import pandas as pd


def transform_data(df):
    """Làm sạch dữ liệu & tính tổng doanh thu"""
    # Xóa các hàng có giá trị null
    df = df.dropna()

    # Tính tổng doanh thu (Quantity * Price)
    df["Total_sales"] = df["Quantity"] * df["Price"]

    # Chuyển đổi kiểu dữ liệu để khớp với schema trong BigQuery (NẾU CẦN)
    # df["Invoice"] = df["Invoice"].astype(str)  # Invoice: STRING
    # df["StockCode"] = df["StockCode"].astype(str)  # StockCode: STRING
    # df["Description"] = df["Description"].astype(str)  # Description: STRING
    # df["Quantity"] = df["Quantity"].astype(int)  # Quantity: INTEGER
    # # Chuyển InvoiceDate thành kiểu datetime với định dạng phù hợp
    # df["Price"] = df["Price"].astype(float)  # Price: FLOAT
    # df["Customer_ID"] = df["Customer_ID"].astype(str)  # Customer_ID: STRING
    # df["Country"] = df["Country"].astype(str)  # Country: STRING
    # df["Total_sales"] = df["Total_sales"].astype(float)  # Total_sales: FLOAT
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    pd.set_option("display.max_columns", None)  # Hiển thị tất cả các cột
    pd.set_option(
        "display.width", None
    )  # Đảm bảo không có giới hạn chiều rộng hiển thị
    # Kiểm tra lại kiểu dữ liệu sau khi xử lý
    print("✅ Kiểu dữ liệu sau khi xử lý:")
    print(df.dtypes)

    return df
