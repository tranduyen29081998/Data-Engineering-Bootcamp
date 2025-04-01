import json
import time
import requests
import os
from kafka import KafkaProducer
from datetime import datetime

# Đọc API_KEY từ biến môi trường
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Ho Chi Minh City"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Kết nối Kafka
producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

TOPIC = "weather"


def fetch_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "timestamp": int(data.get("dt", 0)),  # Dùng số nguyên (epoch time)
        }
        return weather_data
    else:
        print("Error fetching data")
        return None


while True:
    weather = fetch_weather()
    if weather:
        producer.send(TOPIC, weather)
        print(f"Produced: {weather}")
    time.sleep(10)
