from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'hello_world1',
    bootstrap_servers='b-2.tfs3topg.3nd1ah.c1.kafka.us-east-1.amazonaws.com:9092',
    group_id='my-group',
    auto_offset_reset='earliest'
)
while True:
    records = consumer.poll(timeout_ms=1000)  # Fetch messages for 1 second
    for topic_partition, messages in records.items():
        for message in messages:
            print(f"{message.topic}:{message.partition} {message.offset}: {message.value}")