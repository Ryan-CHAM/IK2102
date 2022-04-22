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
import wordcloud
import matplotlib.pyplot as plt

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
file = open('wc_cmp.txt', 'w') 
for i in range(len(job_df)):
    for key in job_df.iloc[i, 0]:
        file.write(key + ' ')
file.close()
text = open('wc_cmp.txt','r').read()
if not job_df.empty:
    w = wordcloud.WordCloud(font_path="msyh.ttc",
        width=1000, height=800, background_color="white",
        )
    w.generate(text)
    w.to_file("wc_cmp.png")
if job_df.empty:
    print("Cannot find a skill")