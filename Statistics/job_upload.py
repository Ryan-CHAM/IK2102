import pymongo
import json
from pymongo import MongoClient
import pandas as pd
import os
client = MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.job
collection = db.jobs
with open("C:/Users/Coo1ng/Desktop/database.json", encoding="utf-8") as jf:
    str = jf.read()
    data = []
    data.extend(json.loads(str))
    collection.insert_many(data)
client.close()