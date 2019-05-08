from pyspark import SparkContext

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log-example", 2)

pairs = data.map(lambda line: line.split("\t"))
count = pairs.groupByKey()

output = count.collect()
for page_id, ids in output:
    print ("page_id %s list %s" % (page_id, list(ids)))
print ("Popular items done")

sc.stop()
