# kafka


zookeeper server
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

kafka server
.\bin\windows\kafka-server-start.bat .\config\server.properties

create topic
.\bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic topic_name

producer
.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic topic_name
Hello World Javainuse

consumer
.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic topic_name --from-beginning


kafka_producer.py -> simple kafka producer which publishes msg to an topic.

kafka_consumer.py -> simple kafka consumer which consumes msg from an topic.

kafka_spark.py -> data from kafka topic is read using spark streaming and processed.
