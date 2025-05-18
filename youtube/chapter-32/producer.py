import boto3
from time import sleep
from json import dumps
from kafka import KafkaProducer
from aws_schema_registry import DataAndSchema, SchemaRegistryClient
from aws_schema_registry.avro import AvroSchema
from aws_schema_registry.adapter.kafka import KafkaSerializer

session = boto3.Session(aws_access_key_id='{}', aws_secret_access_key='{}')
glue_client = session.client('glue', region_name='us-east-1')                      
schema_registry_client = SchemaRegistryClient(glue_client, registry_name='pgsql_nrt_registry')
serializer = KafkaSerializer(schema_registry_client)
producer = KafkaProducer(bootstrap_servers=['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],value_serializer=serializer)
with open('./user.avsc', 'r') as schema_file:
    schema = AvroSchema(schema_file.read())

record_metadata =producer.send('glue_schema_bms', value=(data, schema)).get(timeout=10)
print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)
