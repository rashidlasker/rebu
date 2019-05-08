from pyspark import SparkContext
from itertools import combinations

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log-example", 2)

pairs = data.map(lambda line: tuple(line.split("\t")))
distinct_pairs = pairs.distinct()
list_pairs = distinct_pairs.groupByKey()
coview_pairs = list_pairs.flatMap(lambda pair: [[pair[0], tuple(x)] for x in combinations(list(pair[1]), 2)])

output = coview_pairs.collect()
for page_id, ids in output:
    print ("page_id %s list %s" % (page_id, ids))
print ("Popular items done")

sc.stop()
