# Producer Code used:
#----------------------------------------
from time import sleep
from json import dumps
from kafka import KafkaProducer
from random import randint
from kafka import KafkaProducer

topic_name='hello_world1'
producer = KafkaProducer(bootstrap_servers=['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))


for e in range(100):
    data = {'number' : e}
    key = ["partition-0","partition-1","partition-2"]
    i = randint(0,2)
    print(data)
    print(i)
    producer.send(topic_name, key=(key[i]).encode('utf-8') , value=data)
    sleep(1)
producer.close()

