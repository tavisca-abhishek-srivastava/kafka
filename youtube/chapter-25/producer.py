# Producer Code used:
#----------------------------------------
from time import sleep
from json import dumps
from kafka import KafkaProducer
from random import randint
from kafka import KafkaProducer

topic_name='hello_world1'
producer = KafkaProducer(bootstrap_servers=['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))


for e in range(10000):
    data = {'number' : e}
    key = ["key-0","key-1","key-2","key-3","key-4","key-5","key-6","key-7","key-8","key-9","key-10","key-11"]
    i = randint(0,11)
    print(data)
    print(i)
    print(key[i])
    producer.send(topic_name, key=(key[i]).encode('utf-8') , value=data)
    sleep(0.5)
producer.close()

