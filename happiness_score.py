import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
import sys

def main():
    if len(sys.argv) != 3: #expect 3 arguments
        print('Usage: spark-submit hapiness_score.py <host> <port>',file=sys.stderr)
        exit(-1)
    
    host = sys.argv[1]
    port = int(sys.argv[2])

    spark = SparkSession \
    .builder \
    .appName("Calculate average happiness score") \
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

    reads = dfs.selectExpr("split(value,' ')[0] as Country","split(value,' ')[1] as Region","split(value,' ')[2] as HappinessScore")

    reads.createOrReplaceTempView('happiness')

    averageScoredf = spark.sql("""SELECT Region, AVG(HappinessScore) as avgScore FROM happiness GROUP BY Region""")

    query = (
    averageScoredf.writeStream.outputMode('complete')
    .format('console').start().awaitTermination()
    )

if __name__ == '__main__':
    main()

