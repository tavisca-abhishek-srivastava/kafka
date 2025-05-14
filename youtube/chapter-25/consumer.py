from kafka import KafkaConsumer
from kafka import TopicPartition , OffsetAndMetadata
import json

consumer = KafkaConsumer ('hello_world1',bootstrap_servers = ['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],
value_deserializer=lambda m: json.loads(m.decode('utf-8')),group_id='demo112215sgtrjwrykvjh',auto_offset_reset='earliest', enable_auto_commit =False)

for message in consumer:
    print(message)
    print("The value is : {}".format(message.value))
    print("The key is : {}".format(message.key))
    print("The topic is : {}".format(message.topic))
    print("The partition is : {}".format(message.partition))
    print("The offset is : {}".format(message.offset))
    print("The timestamp is : {}".format(message.timestamp))
    tp=TopicPartition(message.topic,message.partition)
    om = OffsetAndMetadata(message.offset+1, message.timestamp)
    consumer.commit({tp:om})
    print('*' * 100)