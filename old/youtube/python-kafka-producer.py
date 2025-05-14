#https://www.youtube.com/watch?v=BdZ76q2vWKU&list=PLjfRmoYoxpNrs0VmIq6mOTqXP52RfZdRf&index=13
#  Video13

from time import sleep
from json import dumps
from kafka import KafkaProducer


#Lab 1: Write message to a partition (mentioning the partition number while publishing the message)
topic_name = "helloworld1"

producer = KafkaProducer(bootstrap_servers=["b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092"], value_serializer=lambda x :dumps(x).encode('utf-8'))
data1 = {'number' : 1}
data2 = {'number' : 2}
data3 = {'number' : 3}
data4 = {'number' : 4}
data5 = {'number' : 5}
data6 = {'number' : 6}
producer.send(topic_name, value=data1,partition=1)
producer.send(topic_name, value=data2,partition=1)
producer.send(topic_name, value=data3,partition=1)
producer.send(topic_name, value=data4,partition=2)
producer.send(topic_name, value=data5,partition=2)
producer.send(topic_name, value=data6,partition=0)
producer.close()

#Lab 2: Pass key value pair and data will be placed in partition accroding to key using murmur3 partitioner

from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'])
topic_name='helloworld2'
producer.send(topic_name, key=b'foo', value=b'bar') #Note :key & value serialization we are doing while publishing the message
                                                    #itself , so explicitly not mentioning the key or value serializer
producer.send(topic_name, key=b'foo', value=b'bar')
producer.send(topic_name, key=b'foo1', value=b'foo1')
producer.send(topic_name, key=b'foo2', value=b'foo2')
producer.send(topic_name, key=b'foo3', value=b'foo3')
producer.send(topic_name, key=b'foo4', value=b'foo4')

producer.close()

producer = KafkaProducer(bootstrap_servers=['b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092'],key_serializer=str.encode,value_serializer=lambda x: dumps(x).encode('utf-8'))
topic_name='helloworld3'
data1 = {'number' : 1}
data2 = {'number' : 2}
data3 = {'number' : 3}
data4 = {'number' : 4}
data5 = {'number' : 5}
data6 = {'number' : 6}
producer.send(topic_name,  key='ping',value=data1)
producer.send(topic_name, key='ping',value=data2)
producer.send(topic_name, key='ping',value=data3)
producer.send(topic_name, key='pong',value=data4)
producer.send(topic_name, key='pong',value=data5)
producer.send(topic_name, key='pong',value=data6)
producer.close()