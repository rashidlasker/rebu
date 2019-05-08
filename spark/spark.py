from pyspark import SparkContext
from itertools import combinations

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log-example", 2)

# Step 1
pairs = data.map(lambda line: tuple(line.split("\t")))
distinct_pairs = pairs.distinct()

# Step 2
list_pairs = distinct_pairs.groupByKey().mapValues(lambda pages: sorted(pages))

# Step 3
coview_pairs = list_pairs.flatMap(lambda pair: [[pair[0], tuple(x)] for x in combinations(list(pair[1]), 2)])

# Step 4
flipped_pairs = coview_pairs.map(lambda pair: [pair[1], pair[0]])
coview_pairs_reversed = flipped_pairs.groupByKey()

# Step 5
sum_pairs = coview_pairs_reversed.mapValues(lambda users: len(users))

# Step 6
filtered_pairs = sum_pairs.filter(lambda x : x[1] >= 3)

output = filtered_pairs.collect()
for page_id, ids in output:
    print ("page_id %s list %s" % (str(page_id), str(ids)))
print ("Popular items done")

sc.stop()
