# Kafka Streaming Data Project

## Overview
This project demonstrates a Kafka streaming data pipeline using Python. It includes:
- A **Kafka Producer** that sends messages to a Kafka topic.
- A **Kafka Consumer** that listens to and processes messages from the topic.
- An introduction to stream processing concepts, with the option to extend the project to use advanced frameworks like Kafka Streams, or Apache Spark Streaming.

## Project Structure
- **README.md**: This file.
- **producer.py**: Python script for producing messages to Kafka.
- **consumer.py**: Python script for consuming messages from Kafka.
- **requirements.txt**: Lists the dependencies needed for the project.

## Prerequisites
- **Docker and Docker Compose:** Ensure you have Docker and Docker Compose installed.
- **Python 3.x:** Make sure Python 3 is installed.
- **pip:** Python package installer.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/abanoub1555/kafka-streaming-data-project.git
   cd kafka-streaming-data-project
   
   
## How to run?
1-run the command to set a docker container for kafka and zookeeper.
   docker-compose up -d
   
2-go inside the container
   docker exec -it kafka bash
  
3- cd /opt/kafka

4- to write massege from producer.
   bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic
   
5-Viewing Messages with the Console Consumer
   bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning
   
4.A- Writing a Custom Kafka Producer Application
   python producer.py  (outside the container)
  
5.A- reading data as consumer Application
   python consumer.py   (outside the container)


