from pyspark.sql import SparkSession

def get_spark_session():
    return SparkSession.builder.master('local').appName('App Name').getOrCreate()