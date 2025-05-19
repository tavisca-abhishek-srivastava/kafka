import boto3
from time import sleep
from json import dumps
from kafka import KafkaProducer
from aws_schema_registry import DataAndSchema, SchemaRegistryClient
from aws_schema_registry.avro import AvroSchema
from aws_schema_registry.adapter.kafka import KafkaSerializer

#producer = KafkaProducer(bootstrap_servers=["b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092"],value_serializer=serializer)
#producer = KafkaProducer(bootstrap_servers=['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))


# record_metadata =producer.send("consumerlagdemo", value=(data1, schema))
# print(record_metadata.topic)
# print(record_metadata.partition)
# print(record_metadata.offset)

def custom_partitioner(key, all_partitions, available):
    """
    Customer Kafka partitioner to get the partition corresponding to key
    :param key: partitioning key
    :param all_partitions: list of all partitions sorted by partition ID
    :param available: list of available partitions in no particular order
    :return: one of the values from all_partitions or available
    """
    print("The key is  : {}".format(key))
    print("All partitions : {}".format(all_partitions))
    print("After decoding of the key : {}".format(key.decode('UTF-8')))
    return int(key.decode('UTF-8'))%len(all_partitions)

glue_client = boto3.client("glue", region_name="us-east-1")  
schema_registry_client = SchemaRegistryClient(glue_client, registry_name='pgsql_nrt_registry')
serializer = KafkaSerializer(schema_registry_client)
schema_file =  open('./user.avsc', 'r')
schema = AvroSchema(schema_file.read())
producer = KafkaProducer(bootstrap_servers=['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],value_serializer=serializer,partitioner=custom_partitioner)
topic_name='consumerlagdemo'
#data={"name":"abc"+str(e),
        #   "Age":e}
for e in range(0,1000):
    data={"name":"abc"+str(e),
          "Age":e}
    record_metadata = producer.send(topic_name, key=str(e).encode('UTF-8'),value=(data, schema))
    sleep(.4)