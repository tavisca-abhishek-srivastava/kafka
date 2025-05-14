from kafka import KafkaConsumer
import json
import time
from time import sleep
i = 10
while i > 2:
    bootstrap_servers = ['b-1.mskpg.f9784u.c14.kafka.us-east-1.amazonaws.com:9092']
    topicName = 'TLSTestTopic'
    consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers)
   # print(consumer)

    for msg in consumer:

        rec_datavalue = msg.value

        print(rec_datavalue)