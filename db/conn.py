import pandas as pd
from pymongo import MongoClient

data = pd.read_csv('<<INSERT NAME OF DATASET>>.csv')

client = MongoClient(
    "mongodb+srv://<<YOUR USERNAME>>:<<PASSWORD>>@clustertest-icsum.mongodb.net/test?retryWrites=true&w=majority")
db = client['<<INSERT NAME OF DATABASE>>']
collection = db['<<INSERT NAME OF COLLECTION>>']
data.reset_index(inplace=True)
data_dict = data.to_dict("records")

collection.insert_many(data_dict)
