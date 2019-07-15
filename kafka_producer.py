import time
import random
import string
from kafka import KafkaProducer

def msg_generator():
    size = 6
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def main():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    while(1):
        msg = msg_generator()
        producer.send('test', bytes(msg, 'utf-8'))
        time.sleep(5)

if __name__ == "__main__":
    main()
