"""
Testing - pyspark Docker image :::: API
"""

from fastapi import FastAPI  # type: ignore
from pyspark.sql import SparkSession  # type: ignore

app = FastAPI()
spark = SparkSession.builder.appName("SparkPoC").master("local[*]").getOrCreate()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/sum")
def sum_numbers():
    df = spark.createDataFrame([(1,), (2,), (3,), (4,)], ["value"])
    total = df.groupBy().sum("value").collect()[0][0]

    return {"sum": total}
