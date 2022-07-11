from collections import defaultdict
from utils import sparkutils

def handler(env, app_name, src_dir, tgt_dir):
    spark = sparkutils.get_spark_session(env, app_name)
    
    # read from source
    records = spark.sparkContext.textFile(src_dir)
    
    # apply function to eac partition
    pair_rdd = records.mapPartitions(process_partition)
    
    # collecting frequencies
    frequencies_rdd = pair_rdd.reduceByKey(lambda a,b: a + b)
    
    # write result
    frequencies_rdd.saveAsTextFile(tgt_dir)
    
    # return result
    return frequencies_rdd.collect()
    
def process_partition(iterator):
    hashmap = defaultdict(int)
    
    for record in iterator:
        if record.startswith(">"):
            hashmap["z"] += 1
        else:
            chars = record.lower()
            for char in chars:
                hashmap[char] += 1
     
    key_value_list = [(k, v) for k, v in hashmap.items()]
                
    print("hashmap=", hashmap)
    print('key_value_list', key_value_list)
        
    return key_value_list
    