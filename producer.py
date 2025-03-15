from kafka import KafkaProducer
import time

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Number of messages to send
num_messages = 1000

# Loop to send multiple messages
for i in range(num_messages):
    # Construct the message
    message = f"Message number {i}".encode('utf-8')
    
    # Send the message to the 'test-topic'
    producer.send('test-topic', message)
    
    # Optionally, print the sent message for confirmation
    print(f"Sent: Message number {i}")
    
    # Optional: sleep to throttle sending speed (adjust as needed)
    time.sleep(0.1)

# Ensure all messages are sent before closing
producer.flush()
producer.close()

print("Finished sending messages.")

