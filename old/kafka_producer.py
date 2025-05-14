from kafka import KafkaProducer
import json
import time
from time import sleep

bootstrap_servers = ['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092']
topicName = 'demo_testing'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
# with open('C:\Abhishek-Work\Python\100-Days\27-Day\Kafka\abc.csv','r') as myfile:
#     for record in myfile:
#         data = record
#         producer.send('csv2pgTopic',json.dumps(data).encode('utf-8'))
#         sleep(2)

for record in range(0,300000):
    data = "myvalue-" + str(record)
    producer.send(topicName,json.dumps(data).encode('utf-8'))
    sleep(2)