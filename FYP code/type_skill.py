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
results = collection.find()
thss = []
job_id = []
dict = {}

job_type = input('please enter the type')
##############################RECORDING NEW CLUSTER OF DATABASE#######################################
for r in results:
    print("fuck")
    ths = []
    temp = r['_id']
    for i in r['categories']:
        if (i == job_type):
            job_id.append(temp)
            for j in r['requirements']['hard_skills']:
                ths.append(j)
    thss.append(ths)
if(len(job_id) == 0 or len(thss) == 0):
    print("No result found")
    exit(0)
job_df = pd.DataFrame({'hardskills': thss})
for i in range(len(job_df)):
    for key in job_df.iloc[i, 0]:
        dict[key] = dict.get(key, 0) + 1
file = open(job_type + 'new.txt', 'w') 
for k,v in dict.items():
    file.write(str(k)+'&&&'+str(v)+'\n')
file.close()
##################################LOADING OLD CLUSTER FROM THE FILE##################################
old_dict = {}
file = open(job_type + '.txt','r')
for line in file.readlines():
    line = line.strip()
    k = line.split('&&&')[0]
    v = line.split('&&&')[1]
    old_dict[k] = int(v)
file.close()
#####################################COMPARING TWO CLUSTER FILE#########################################
compare_dict = {}
for k,v in dict.items():
    if dict.get(k, 0) != old_dict.get(k, 0):
        compare_dict[k] = dict.get(k, 0) - old_dict.get(k, 0)
sorted_compare_dict = sorted(compare_dict.items(), key=lambda d:d[1], reverse=True)
file=open(job_type + 'compare.txt','w')
file1 = open(job_type + 'growing.txt', 'w')
for line in sorted_compare_dict:
    for a in line:
        if(isinstance(a, int) == 1):
            file.write(str(a))
        if(isinstance(a, int) == 0):
            if(old_dict.get(a, 0) != 0):   
                temp = float((dict.get(a, 0) - old_dict.get(a, 0)) / (old_dict.get(a, 0)))
                temp = int(temp * 10000)
                file1.write(a)
                file1.write('   ')
                file1.write(str(temp))
                file1.write('\n')
            file.write(a)
        file.write('   ')
    file.write('\n')
file.close()
file1.close()

growing_dict = {}
file = open(job_type + 'growing.txt','r')
for line in file.readlines():
    line = line.strip()
    k = line.split('   ')[0]
    v = line.split('   ')[1]
    growing_dict[k] = int(v)
file.close()

sorted_growing_dict = sorted(growing_dict.items(), key=lambda d:d[1], reverse=True)
file = open(job_type + 'growing.txt', 'w')
for line in sorted_growing_dict:
      for a in line:
        if(isinstance(a, int) == 1):
            file.write(str(float(a/10000)))
        if(isinstance(a, int) == 0):
            file.write(a)
        file.write('   ')
      file.write('\n')
file.close()
##################################CALCULATE THE TOTAL AMOUNT#########################################
total_dict = {}
file = open(job_type + 'new.txt','r')
for line in file.readlines():
    line = line.strip()
    k = line.split('&&&')[0]
    v = line.split('&&&')[1]
    total_dict[k] = int(v)
file.close()
total_dict = sorted(total_dict.items(), key=lambda d:d[1], reverse=True)
file = open(job_type + 'total.txt', 'w')
for line in total_dict:
      for a in line:
        if(isinstance(a, int) == 1):
            file.write(str(a))
        if(isinstance(a, int) == 0):
            file.write(a)
        file.write('   ')
      file.write('\n')
file.close()