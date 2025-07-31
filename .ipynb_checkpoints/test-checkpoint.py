import os
os.environ["JAVA_HOME"] = "C:\\Program Files\\Java\\jdk1.8.0_202"

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SpotifyTest") \
    .getOrCreate()

print("✅ SparkSession Created Successfully!")
print("Spark Version:", spark.version)

df = spark.createDataFrame([(1, "Song A"), (2, "Song B")], ["id", "track"])
df.show()
