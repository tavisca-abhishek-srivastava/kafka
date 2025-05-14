from audioop import add
from kafka import KafkaConsumer
import json
import time
from time import sleep
import mysql.connector

dbconn = mysql.connector.connect(host='mysql-version-validation-orch.cfihahod2vsa.us-east-1.rds.amazonaws.com',
                        database='vt',
                        user='admin',
                        password='welcome1234',
                        port = 3306)

name = "Abhishek"
age = '25'
address = "802 c2b lomgisland "
data = ("Abhishek",25,"802 c2b lomgisland ")
mycursor = dbconn.cursor()
savequery = ("insert into emp (name,age,address) values(%s,%s,%s)")

mycursor.execute(savequery,data)

dbconn.commit()
mycursor.close()
dbconn.close()