from typing import final
import pandas as pd
from sklearn import metrics
import math
from re import I, S
import pymongo
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import os
import time
import difflib
import datetime

client = pymongo.MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.job
collection = db.jobs
job_id = []
hss = []
dict = {}

##############################SEARCHING THE HARD SKILLS FOR COMPANY#######################################
cmp = input("Please input the company name:")
results = collection.find({"company" : cmp})
for r in results:
    hs = []
    for i in r['requirements']['hard_skills']:
        hs.append(i)
    hss.append(hs)
job_df = pd.DataFrame({'hardskills': hss})
print(job_df)
for i in range(len(job_df)):
    for key in job_df.iloc[i, 0]:
        dict[key] = dict.get(key, 0) + 1
sorted_dict = sorted(dict.items(), key=lambda d:d[1], reverse=True)

file = open('company.txt', 'w')
for line in sorted_dict:
      for a in line:
        if(isinstance(a, int) == 1):
            file.write(str(a))
        if(isinstance(a, int) == 0):
            file.write(a)
            file.write('&&&')
      file.write('\n')
file.close()
company_dict = {}
file = open('company.txt','r')
for line in file.readlines():
    line = line.strip()
    k = line.split('&&&')[0]
    v = line.split('&&&')[1]
    company_dict[k] = v
file.close()
print(company_dict)