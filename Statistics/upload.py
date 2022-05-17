import pymongo
import json
from pymongo import MongoClient
import pandas as pd
import os
client = MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.resume
collection = db.resumes

#for i in range (1, 1003):
pathname = 'C:/Users/Coo1ng/Documents/WeChat Files/wxid_pglk6l347vxk11/FileStorage/File/2022-01/collab/collab/job_postings_with_types/engineering/chemical.json'
if os.path.exists(pathname) == True:
        with open(pathname,'r') as load_f:
            load_dict = json.load(load_f)
        result = collection.insert_one(load_dict)
#for i in range (1003, 2003):
    #pathname = 'C:/Users/Coo1ng/Desktop/1003-2002_results/' + str(i) + '.json'
    #if os.path.exists(pathname) == True:
        #with open(pathname,'r') as load_f:
            #load_dict = json.load(load_f)
        #result = collection.insert_one(load_dict)
#for i in range (2003, 2616):
    #pathname = 'C:/Users/Coo1ng/Desktop/2003-2615_results/' + str(i) + '.json'
    #if os.path.exists(pathname) == True:
        #with open(pathname,'r') as load_f:
            #load_dict = json.load(load_f)
        #result = collection.insert_one(load_dict)
#print(result.inserted_ids)