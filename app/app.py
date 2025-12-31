
import json
from kafka import KafkaConsumer

def main():
    consumer = KafkaConsumer(
        'vitals-topic',
        bootstrap_servers=['localhost:9092'],  # Replace with your Kafka broker address
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        print(f"Received: {message.value}")

if __name__ == "__main__":
    main()
