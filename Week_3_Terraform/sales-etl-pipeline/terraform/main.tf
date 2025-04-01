provider "google" {
  credentials = file("../config/gcs_config.json")  # Đọc credentials từ file JSON
  project     = var.project_id  # Sử dụng biến project_id
  region      = var.region  # Sử dụng biến region
}

resource "google_storage_bucket" "sales-bucket-290819987te" { # tên sử dụng để tham chiếu trong terraform, cái này có thể trùng
  name          = var.bucket_name  # Sử dụng biến bucket_name # tên bucket trên GCP, không thể trùng được
  location      = var.region  # Lấy region từ biến
  storage_class = "STANDARD"

  versioning {
    enabled = true  # Bật versioning để lưu các phiên bản cũ của file
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30  # Xóa file sau 30 ngày
    }
  }
}
