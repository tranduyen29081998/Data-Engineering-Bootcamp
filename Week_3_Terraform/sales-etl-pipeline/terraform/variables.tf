variable "project_id" {
  description = "Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "Google Cloud region"
  type        = string
  default     = "us-central1"  # Chọn vùng mặc định (Bạn có thể thay đổi region tại đây)
}

variable "bucket_name" {
  description = "Tên Google Cloud Storage bucket"
  type        = string
}
