from utils import sparkutils

def handler():
    spark = sparkutils.get_spark_session()
    return spark.range(10000).where('id > 1000').selectExpr('sum(id)').collect()