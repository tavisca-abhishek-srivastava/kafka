import boto3
from time import sleep
from json import dumps
from kafka import KafkaProducer
from aws_schema_registry import DataAndSchema, SchemaRegistryClient
from aws_schema_registry.avro import AvroSchema
from aws_schema_registry.adapter.kafka import KafkaSerializer

session = boto3.Session( region_name='us-east-1')
glue_client = session.client("glue", region_name="us-east-1")                      
schema_registry_client = SchemaRegistryClient(glue_client, registry_name='pgsql_nrt_registry')
serializer = KafkaSerializer(schema_registry_client)
producer = KafkaProducer(bootstrap_servers=["b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092"],value_serializer=serializer)
#producer = KafkaProducer(bootstrap_servers=['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
data = {
    "name": "Hello",
    "Age":45 }
schema_file =  open('./user.avsc', 'r')
schema = AvroSchema(schema_file.read())
record_metadata =producer.send("consumerlagdemo", value=(data, schema))
print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)
