from elasticsearch import Elasticsearch
import json

connected = False
while not connected:
    try:
        es = Elasticsearch(['es'])
        connected = True
    except:
        continue


with open('rebu/fixtures/rebu/rebu_testdata.json') as json_file:  
    data = json.load(json_file)
    for obj in data:
        if obj['model'] == 'rebu.meal':
            meal = obj['fields']
            meal['id'] = obj['pk']
            es.index(index='meals_index', doc_type='meal', id=meal['id'], body=meal)
es.indices.refresh(index="meals_index")
print("Successfully loaded fixtures into ES")