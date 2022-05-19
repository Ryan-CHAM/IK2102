from contextlib import contextmanager, nullcontext
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
########################################################## PART3 ###########################################################################
###################################################### University Score ####################################################################
university_data_set = pd.read_csv("C:/Users/Coo1ng/Desktop/Dataset.csv", encoding = "ISO-8859-1")

client = pymongo.MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.resume
collection = db.resumes
results = collection.find()
resume_id = []
gpas = []
temparray = []
finalarray = []
length = {}
l = 0

for r in results:
    resume_id.append(r['_id'])
    gpa = []
    for i in r['education']: gpa.append(i['gpa'])
    gpas.append(gpa)
resume_df = pd.DataFrame({'id': resume_id, 'gpa': gpas})
print(resume_df)