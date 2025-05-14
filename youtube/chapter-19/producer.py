from time import sleep
from json import dumps
from kafka import KafkaProducer

topic_name='hello_world1'
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

while True:
    message=input("Enter the message you want to send : ")
    partition_no=int(input("In which partition you want to send ?  "))
    producer.send(topic_name, value=message,partition=partition_no)

producer.close()

# Start Consumer with Group:
# --------------------------------------------------------
# F:/kafka_2.12-3.2.0/bin/windows/kafka-console-consumer.bat --topic hello_world1 --from-beginning --bootstrap-server localhost:9092 --group my-first-consumer-group