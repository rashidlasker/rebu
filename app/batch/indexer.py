from elasticsearch import Elasticsearch
from kafka import KafkaProducer
from kafka import KafkaConsumer
import json

""" Kafka Stuff """
# producer = KafkaProducer(bootstrap_servers='kafka:9092')
# some_new_listing = {'title': 'Used MacbookAir 13"', 'description': 'This is a used Macbook Air in great condition', 'id':42}
# producer.send('new-listings-topic', json.dumps(some_new_listing).encode('utf-8'))
# consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
# for message in consumer:
#     print(json.loads((message.value).decode('utf-8')))

""" ES Stuff """
# es = Elasticsearch(['es'])
# some_new_listing = {'title': 'Used MacbookAir 13"', 'description': 'This is a used Macbook Air in great condition', 'id':42}
# es.index(index='listing_index', doc_type='listing', id=some_new_listing['id'], body=some_new_listing)
# es.indices.refresh(index="listing_index")
# res = es.search(index='listing_index', body={'query': {'query_string': {'query': 'macbook air'}}, 'size': 10})
# print(res)

