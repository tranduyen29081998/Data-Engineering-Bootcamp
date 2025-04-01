**README.md**

# Sales ETL Pipeline with Airflow & Terraform

## Overview

This project is a fully automated ETL pipeline using Apache Airflow to extract, transform, and load sales data into Google Cloud Storage (GCS). Terraform is used to provision cloud resources like GCS and BigQuery.

## Project Structure

```
.
├── airflow/
│   ├── dags/
│   │   ├── sales_etl_dag.py
├── config/
│   ├── gcs_config.json
├── data/
│   ├── raw/
│   │   ├── sales_data.csv
│   ├── processed/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── terraform.tfvars
│   ├── terraform.tfstate
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
```

## Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Terraform
- Google Cloud SDK

## Setup

### 1. Deploy Cloud Infrastructure with Terraform

```sh
cd terraform
terraform init
terraform apply -auto-approve
```

### 2. Start Airflow with Docker Compose

```sh
docker-compose up -d --build
```

### 3. Access Airflow Web UI

Visit `http://localhost:8080`, login with default creds (admin/admin), and enable the `sales_etl_dag` DAG.

## Running the ETL Pipeline Manually

```sh
cd etl
python main.py
```

## Expected Output

- Transformed data will be saved in `data/processed/`
- Processed data will be uploaded to GCS
