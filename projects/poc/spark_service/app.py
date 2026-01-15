"""
Testing - pyspark Docker image :::: API
"""

from fastapi import FastAPI, Request  # type: ignore
from pyspark.sql import SparkSession  # type: ignore

app = FastAPI()
spark = SparkSession.builder.appName("SparkPoC").master("local[*]").getOrCreate()


@app.get("/health")
def health():
    return {"status": "PySpark API running"}


@app.post("/agg")
async def sum_numbers(request: Request):
    data = await request.json()
    employee_data = data.get("employee_data", {})

    df = spark.createDataFrame(
        list(
            zip(
                employee_data["id"],
                employee_data["name"],
                employee_data["badge"],
                employee_data["score"],
            )
        ),
        list(employee_data.keys()),
    )
    agg_data = dict(
        df.groupBy("badge")
        .sum("score")
        .withColumnRenamed("sum(score)", "agg_score")
        .collect()
    )

    return {"Aggregated score by Badge": agg_data}
