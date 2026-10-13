from pyspark.sql import SparkSession

print("Starting Spark (this might take a few seconds)...")

# Initialize a local Spark session
spark = SparkSession.builder \
    .appName("MyFirstSparkApp") \
    .master("local[*]") \
    .getOrCreate()

# Create some dummy data
data = [
    ("Web Crawling", "Acquisition"), 
    ("WARC", "Storage"), 
    ("MapReduce", "Processing")
]
df = spark.createDataFrame(data, ["Concept", "Category"])

print("\n--- SPARK DATAFRAME ---")
df.show()

# Shut down cleanly
spark.stop()