from pyspark import SparkContext
from itertools import combinations
from collections import defaultdict
import urllib.request
import urllib.parse
import json

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log-example", 2)

# Step 1
pairs = data.map(lambda line: tuple(line.split("\t")))
distinct_pairs = pairs.distinct()

# Step 2
list_pairs = distinct_pairs.groupByKey().mapValues(lambda pages: sorted(pages))

# Step 3
single_coview_pairs = list_pairs.flatMap(lambda pair: [[pair[0], tuple(x)] for x in combinations(list(pair[1]), 2)])

# Step 4
flipped_single_coview_pairs = single_coview_pairs.map(lambda pair: [pair[1], pair[0]])
list_coview_pairs = flipped_single_coview_pairs.groupByKey()

# Step 5
sum_pairs = list_coview_pairs.mapValues(lambda users: len(users))

# Step 6
filtered_pairs = sum_pairs.filter(lambda x : x[1] >= 3)

output = filtered_pairs.collect()
recommendations = defaultdict(set)
with open("/tmp/data/spark_output.log-example", "w+") as file:
    for coview, count in output:
        recommendations[coview[0]].add(coview[1])
        recommendations[coview[1]].add(coview[0])
        file.write ("%s\t%s\n" % (str(coview), str(count)))
recommendations = {x: ",".join(str(y) for y in recommendations[x]) for x in recommendations}
print(str(recommendations))

# Send request
data = urllib.parse.urlencode({"recommendations": json.dumps(recommendations) }).encode('utf-8')
req = urllib.request.Request("http://models:8000/api/v1/recommendations/create/", data=data)
resp_json = urllib.request.urlopen(req).read().decode('utf-8')
print(resp_json)

sc.stop()
