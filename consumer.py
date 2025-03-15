from kafka import KafkaConsumer

# Initialize the consumer:
# 'auto_offset_reset' set to 'earliest' ensures that the consumer reads messages from the beginning
# if no previous offset is stored.
consumer = KafkaConsumer(
    'test-topic',                        # Topic to subscribe to
    bootstrap_servers=['localhost:9092'], # Address of the Kafka broker
    auto_offset_reset='earliest',         # Start reading at the earliest available message
    enable_auto_commit=True,              # Automatically commit offsets
    group_id='my-consumer-group'          # Consumer group id for coordination
)

print("Consumer is now listening to 'test-topic'...")

# Continuously listen for messages on the topic
for message in consumer:
    # message is a ConsumerRecord, you can access various attributes:
    # - message.value: The content of the message (in bytes)
    # - message.topic: The topic name
    # - message.partition: The partition the message came from
    # - message.offset: The offset position of the message
    print(f"Received message: {message.value.decode('utf-8')} from topic: {message.topic}, "
          f"partition: {message.partition}, offset: {message.offset}")

