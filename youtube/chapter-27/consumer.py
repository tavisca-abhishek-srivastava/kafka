from kafka import KafkaConsumer
from kafka import TopicPartition , OffsetAndMetadata, ConsumerRebalanceListener
import json
from random import *
from time import sleep
from kafka.coordinator.assignors.roundrobin import RoundRobinPartitionAssignor
from kafka.coordinator.assignors.range import RangePartitionAssignor

topic_name=["consumerlagdemo"]

class MyConsumerRebalanceListener(ConsumerRebalanceListener):

    def on_partitions_revoked(self, revoked):
        print("Partitions %s revoked" % revoked)
        print('*' * 50)

    def on_partitions_assigned(self, assigned):
        print("Partitions %s assigned" % assigned)
        print('*' * 50)

consumer = KafkaConsumer(bootstrap_servers=['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                         group_id='demo112215sgtrjwrykvjh', auto_offset_reset='earliest',
                         enable_auto_commit=False,partition_assignment_strategy=[RoundRobinPartitionAssignor])

listener = MyConsumerRebalanceListener()
consumer.subscribe(topic_name,listener=listener)

for message in consumer:
    number = randint(-2147483648 , 2147483647)
    print(message)
    print("The value is : {}".format(message.value))
    tp=TopicPartition(message.topic,message.partition)
    om = OffsetAndMetadata(message.offset+1, message.leader_epoch, number)
    consumer.commit({tp:om})
    sleep(0.8)