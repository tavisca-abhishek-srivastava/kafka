from kafka import KafkaConsumer
from kafka import TopicPartition , OffsetAndMetadata
import json
from random import *
from time import sleep

consumer = KafkaConsumer ('hello_world1',bootstrap_servers = ['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],
value_deserializer=lambda m: json.loads(m.decode('utf-8')),group_id='demo112215sgtrjwrykvjh1',auto_offset_reset='earliest', enable_auto_commit =False,partition_assignment_strategy=['RoundRobinPartitionAssignor'])

for message in consumer:
    number = randint(-2147483648 , 2147483647)
    print(message)
    print("The value is : {0}".format(message.value))
    print("The key is : {0}".format(message.key))
    print("The topic is : {0}".format(message.topic))
    print("The partition is : {0}".format(message.partition))
    print("The offset is : {0}".format(message.offset))
    print("The timestamp is : {0}".format((message.timestamp)))
    print("The leader_epoch is : {0}".format(message.leader_epoch))
    tp=TopicPartition(message.topic,message.partition)
    om = OffsetAndMetadata(message.offset + 1, message.leader_epoch, number)
    consumer.commit({tp:om})
    print('*' * 101)
    sleep(1)