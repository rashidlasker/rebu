from kafka import KafkaProducer
from kafka import KafkaConsumer
import json

connected = False
while not connected:
    try:
        meals_consumer = KafkaConsumer('meal-view-topic', group_id='meal-view-indexer', bootstrap_servers=['kafka:9092'])
        connected = True
    except:
        continue
while(True):
    try:
        for message in meals_consumer:
            new_listing = json.loads((message.value).decode('utf-8'))
            with open("/tmp/data/access.log-example", "a+") as file:
                file.write ("%d\t%d\n" % (new_listing["user_id"], new_listing["meal_id"]))

            print('Success!')
            print(new_listing)
    except Exception as e:
        print("Error: " + str(e))
