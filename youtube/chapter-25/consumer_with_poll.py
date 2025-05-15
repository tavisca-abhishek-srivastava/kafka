from kafka import KafkaConsumer
from kafka import KafkaConsumer
from kafka import TopicPartition , OffsetAndMetadata
import json
from random import *
from time import sleep
from kafka.coordinator.assignors.roundrobin import RoundRobinPartitionAssignor
from kafka.coordinator.assignors.range import RangePartitionAssignor


consumer = KafkaConsumer(    'hello_world1',    bootstrap_servers=['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],    group_id='my-group',    auto_offset_reset='earliest', enable_auto_commit =False,partition_assignment_strategy =[RoundRobinPartitionAssignor])
while True:
    records = consumer.poll(timeout_ms=1000)  # Fetch messages for 1 second
    for topic_partition, messages in records.items():
        for message in messages:
            #print(f"{message.topic}:{message.partition} {message.offset}: {message.value}")
            print(message)