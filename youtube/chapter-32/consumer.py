
#pip3 install boto3 -t.
#pip3 install aws-glue-schema-registry --upgrade --use-pep517 -t .
#pip install kafka-python -t .
import boto3
from aws_schema_registry import SchemaRegistryClient
from kafka import TopicPartition , OffsetAndMetadata
from aws_schema_registry.adapter.kafka import KafkaDeserializer
from kafka import KafkaConsumer



glue_client = boto3.client('glue', region_name='us-east-1')
client = SchemaRegistryClient(glue_client, registry_name='pgsql_nrt_registry')
deserializer = KafkaDeserializer(client)
topic_name='consumerlagdemo'
consumer = KafkaConsumer (topic_name,bootstrap_servers = ['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],
value_deserializer=deserializer,group_id='glueschemaregistry123',auto_offset_reset='earliest',enable_auto_commit =False)
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