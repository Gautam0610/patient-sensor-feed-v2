
import time
import json
from kafka import KafkaProducer
import random

def generate_vitals():
    vitals = {
        'patient_id': random.randint(1, 100),
        'heart_rate': random.randint(60, 100),
        'spo2': random.randint(95, 100),
        'temperature': round(random.uniform(36.5, 37.5), 1),
        'timestamp': time.time()
    }
    return vitals


def main():
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],  # Replace with your Kafka broker address
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

    while True:
        vitals = generate_vitals()
        print(f"Sending: {vitals}")
        producer.send('vitals-topic', value=vitals)
        time.sleep(1)

if __name__ == "__main__":
    main()
