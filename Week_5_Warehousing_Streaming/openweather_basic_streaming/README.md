# OpenWeather Streaming Pipeline

## Overview

This project collects real-time weather data from OpenWeather API, processes it using Apache Kafka, and stores the results in Google BigQuery.

## Architecture

1. **Producer**: Fetches weather data from OpenWeather API and publishes it to a Kafka topic.
2. **Kafka Broker**: Manages the message queue.
3. **Consumer**: Reads data from Kafka and uploads it to Google BigQuery.

## Prerequisites

- Docker & Docker Compose installed
- OpenWeather API Key
- Google Cloud service account with BigQuery access

## Setup

### 1. Configure Environment Variables

Create a `.env` file in the project directory and add:

```sh
OPENWEATHER_API_KEY=your_openweather_api_key
GOOGLE_APPLICATION_CREDENTIALS=/app/config/gcs_config.json
```

### 2. Setup Google Cloud Credentials

Place your `gcs_config.json` file in the `config/` directory and ensure it is correctly mapped in `docker-compose.yml`.

### 3. Run the Pipeline

Use Docker Compose to start all services:

```sh
docker-compose up -d
```

This will start:

- Zookeeper
- Kafka
- Producer
- Consumer

### 4. Verify Kafka Messages

Check if the producer is publishing messages:

```sh
docker logs producer -f
```

Check if the consumer is consuming messages:

```sh
docker logs consumer -f
```

## Code Structure

```
openweather_basic_streaming/
│── config/
│   ├── gcs_config.json       # Google Cloud credentials
│── producer.py               # Fetches and sends weather data to Kafka
│── consumer.py               # Reads data from Kafka and uploads to BigQuery
│── requirements.txt          # Python dependencies
│── Dockerfile                # Container setup
│── docker-compose.yml        # Service orchestration
│── .env                      # Environment variables
```

## Troubleshooting

- **Kafka Connection Issues**: Ensure Kafka and Zookeeper are running properly.
- **Consumer Not Uploading to BigQuery**: Verify `gcs_config.json` and BigQuery table setup.
- **Incorrect Timestamp Format**: Ensure `timestamp` is converted using:
  ```python
  df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s", errors="coerce")
  ```

## Stopping the Services

To stop and remove all containers:

```sh
docker-compose down
```

## Conclusion

This pipeline automates real-time weather data collection, processing, and storage in BigQuery. You can extend it with data transformations, alerting, or visualization tools like Looker Studio.
