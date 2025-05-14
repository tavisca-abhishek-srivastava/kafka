from kafka import KafkaConsumer
import json
import time
from time import sleep
i = 10
while i > 2:
    bootstrap_servers = ['b-1.cassandra-cdc-kafka.g6bgfd.c23.kafka.us-east-1.amazonaws.com:9092']
    topicName = 'pulsar-kafka'
    consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers)
    print(consumer)

    for msg in consumer:
        rec_data = msg.key.decode('utf-8')

        print(rec_data)
        rec_datavalue = msg.value.decode('utf-8')

        print(rec_datavalue)

