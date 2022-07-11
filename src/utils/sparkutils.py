from pyspark.sql import SparkSession

def get_spark_session(env, app_name):
    if env == 'DEV': 
        return SparkSession.builder.master('local').appName(app_name).getOrCreate()
    elif env == 'PROD':
        return SparkSession.builder.master('yarn').appName(app_name).getOrCreate()