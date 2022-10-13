import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
import sys

def main():
    if len(sys.argv) != 3: #expect 3 arguments
        print('Usage: spark-submit word_count.py <host> <port>',file=sys.stderr)
        exit(-1)
    
    host = sys.argv[1]
    port = int(sys.argv[2])

    spark = SparkSession \
    .builder \
    .appName("Word Count") \
    .getOrCreate()

    spark.sparkContext.setLogLevel('ERROR')

    dfs = (spark.readStream
    .format('socket')
    .option('host',host)
    .option('port',port)
    .load()
    )

    print('Streaming source ready: ',dfs.isStreaming)

    dfs.printSchema()

    words = (dfs.select(explode(split(dfs.value,' ')).alias('word')))

    wordCounts = words.groupby('word').count().orderBy('count')

    query = (
    wordCounts.writeStream.outputMode('complete')
    .format('console').start().awaitTermination()
    )

if __name__ == '__main__':
    main()

