from kafka import KafkaConsumer

def main():
    consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest')
    for message in consumer:
        print (message.value.decode('utf-8'))

if __name__ == "__main__":
    main()
