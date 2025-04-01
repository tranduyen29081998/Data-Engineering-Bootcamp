# 🚀 DevOps Learning - Week 3: Docker & Terraform

## 📌 Overview

This project covers **containerization** using Docker and **Infrastructure as Code (IaC)** using Terraform.  
It includes a **Python Flask application** containerized with Docker and a **Terraform script** to provision a Google Cloud Storage (GCS) bucket.

---

## 🐳 Docker: Containerizing a Python Flask App

### 🔹 Steps to Build and Run the Docker Container

1. **Navigate to the Docker project**:
   ```sh
   cd devops-learning/Week_3_Docker
   ```
2. **Build the Docker image**:
   ```sh
   docker build -t my-python-app .
   ```
3. **Run the container**:
   ```sh
   docker run -p 5000:5000 my-python-app
   ```
4. **Access the application**: Open **http://localhost:5000/** in your browser.  
   You should see:
   ```txt
   Hello, Docker!
   ```
5. **Stop and remove the container**:
   ```sh
   docker ps         # Get container ID
   docker stop <ID>  # Stop container
   docker rm <ID>    # Remove container
   ```
6. **Remove Docker image** (if needed):
   ```sh
   docker rmi my-python-app
   ```

---

## ☁️ Terraform: Deploying Google Cloud Storage (GCS) Bucket

### 🔹 Steps to Deploy GCS Bucket Using Terraform

1. **Authenticate with Google Cloud**:
   ```sh
   gcloud auth application-default login
   ```
2. **Navigate to the Terraform directory**:
   ```sh
   cd ../Week_3_Terraform
   ```
3. **Initialize Terraform**:
   ```sh
   terraform init
   ```
4. **Plan and apply the Terraform script**:
   ```sh
   terraform plan
   terraform apply -auto-approve
   ```
5. **Verify the bucket creation**:
   ```sh
   gcloud storage buckets list
   ```
6. **Destroy resources (if no longer needed)**:
   ```sh
   terraform destroy -auto-approve
   ```

---

## 📜 License

MIT License

✅ This repository is structured for easy DevOps automation and cloud provisioning. 🚀
