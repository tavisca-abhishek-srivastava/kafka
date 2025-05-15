#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import kafka
from kafka.structs import TopicPartition


def count_messages(consumer):
    i = 0
    try_cnt = 0
    while True:
        records = consumer.poll(50)     # timeout in millis
        if not records:
            try_cnt += 1
            if try_cnt > 10:
                break
            for _, consumer_records in records.items():
                for _ in consumer_records:
                    i += 1
    return i


def show_messageges_assign(kafka_server, topic):
    cnt = 0
    consumer = kafka.KafkaConsumer(bootstrap_servers=kafka_server, group_id=None, auto_offset_reset='earliest', enable_auto_commit=False)
    try:
        partitions = consumer.partitions_for_topic(topic)
        if partitions:
            for partition in partitions:
                tp = TopicPartition(topic, partition)
                consumer.assign([tp])
                consumer.seek(partition=tp, offset=0)
                cnt += count_messages(consumer)
    finally:
        consumer.close()
    print('%s assign, partitions: %s, msg cnt=%d' % (topic, partitions, cnt))


def show_messageges_subscribe(kafka_server, topic):
    cnt = 0
    consumer = kafka.KafkaConsumer(bootstrap_servers=kafka_server, group_id=None, auto_offset_reset='earliest', enable_auto_commit=False)
    try:
        consumer.subscribe([topic])
        cnt += count_messages(consumer)
    finally:
        consumer.close()
    print('%s, subscribe, msg cnt=%d' % (topic, cnt))


def test_topic(kafka_server, topic):
    show_messageges_assign(kafka_server, topic)
    show_messageges_subscribe(kafka_server, topic)
    print('')


def main():
    kafka_server = '169.0.1.77:9092'
    test_topic(kafka_server, 'gc.ifd.analyse.fdp')
    test_topic(kafka_server, 'gc.ifd.result.fdp')


if __name__ == '__main__':
    main()