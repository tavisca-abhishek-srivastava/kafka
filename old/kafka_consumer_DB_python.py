from kafka import KafkaConsumer
import json
import time
from time import sleep
import mysql.connector

dbconn = mysql.connector.connect(host='mysql-version-validation-orch.cfihahod2vsa.us-east-1.rds.amazonaws.com',
                        database='vt',
                        user='admin',
                        password='welcome1234')

bootstrap_servers = ['b-1.csv-pg.1p1tf8.c22.kafka.us-east-1.amazonaws.com:9092']
topicName = 'csv2pgTopic'
consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers)
i = 1

for msg in consumer:
    rec_data = msg.value.decode('utf-8')
    r = rec_data.replace('"','')
    record = r.strip('\\n')
    
    f_rec = record.split(",")
    name = f_rec[0]
    age = f_rec[1]
    address = f_rec[2]
    print(name)
    print(age)
    print(address)
    if i != 1:
        data = (name,int(age),address)
        mycursor = dbconn.cursor()
        savequery = ("insert into emp (name,age,address) values(%s,%s,%s)")
        #savequery = "insert into vt.emp (name , age , address) values('{0}',{1},'{2}' );".format(name,int(age),address)
        mycursor.execute(savequery,data)
        dbconn.commit()
    i=i+1


mycursor.close()
dbconn.close()
