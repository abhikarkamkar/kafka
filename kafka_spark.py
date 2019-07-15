from pyspark.sql import SparkSession

def process_row(df):
    data = df.value.decode('utf-8')
    print(data)

def main():

    spark = SparkSession \
        .builder \
        .appName("Python kafka Spark example") \
        .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.1') \
        .getOrCreate()

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "test") \
        .option("startingOffsets", "earliest") \
        .load()


    # query = df.writeStream \
    #                     .outputMode("append") \
    #                     .format("console") \
    #                     .start()

    query = df.writeStream.foreach(process_row).start()

    query.awaitTermination()


if __name__ == "__main__":
    main()
