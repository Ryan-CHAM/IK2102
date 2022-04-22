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

client = pymongo.MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.job
collection = db.jobs
job_id = []
salary_low = []
salary_high = []
h_num = 0
m_num = 0
l_num = 0
flag = 0
job = []

job_type = input('please enter the type\n')
results = collection.find({"salary_visible" : True, "categories" : job_type})
##############################RECORDING NEW CLUSTER OF DATABASE#######################################
for r in results:
    job_id.append(r['_id'])
    salary_h = []
    salary_l = []
    salary_h.append(r['salary']['max'])
    salary_high.append(salary_h)
    salary_l.append(r['salary']['min'])
    salary_low.append(salary_l)
job_df = pd.DataFrame({'id': job_id, 'salary_high': salary_high, 'salary_low': salary_low})
print(job_df)
salary_total = 0
for i in range(len(job_df)):
    h_temp = 0
    l_temp = 0
    if len(''.join(str(i) for i in job_df.iloc[i, 1])) == 5 and len(''.join(str(i) for i in job_df.iloc[i, 2])) == 5:
        h_temp = int(''.join(str(i) for i in job_df.iloc[i, 1]))
        l_temp = int(''.join(str(i) for i in job_df.iloc[i, 2]))
        if (h_temp + l_temp) / 2 < 20000: l_num += 1
        if (h_temp + l_temp) / 2 > 20000 and (h_temp + l_temp) / 2 < 50000: m_num += 1
        if (h_temp + l_temp) / 2 > 50000: h_num += 1
        salary_total += (h_temp + l_temp) / 2
        job.append(((h_temp + l_temp) / 2))
    if len(''.join(str(i) for i in job_df.iloc[i, 1])) != 5 and len(''.join(str(i) for i in job_df.iloc[i, 2])) == 5:
        l_temp = int(''.join(str(i) for i in job_df.iloc[i, 2]))
        if l_temp < 20000: l_num += 1
        if l_temp > 20000 and l_temp < 50000: m_num += 1
        if l_temp > 50000: h_num += 1
        salary_total += l_temp
        job.append(l_temp)
    if len(''.join(str(i) for i in job_df.iloc[i, 1])) == 5 and len(''.join(str(i) for i in job_df.iloc[i, 2])) != 5:
        h_temp = int(''.join(str(i) for i in job_df.iloc[i, 1]))
        if h_temp < 20000: l_num += 1
        if h_temp > 20000 and h_temp < 50000: m_num += 1
        if h_temp > 50000: h_num += 1
        salary_total += h_temp
        job.append(l_temp)
if (len(job_df) != 0):
    salary_average_temp = salary_total / len(job_df)
    salary_average = int(salary_average_temp)
    print("THIS IS THE AVERAGE SALARY OF " + job_type + ": ")
    print(salary_average)

id = input('please enter the id\n')
df = pd.read_excel("C:/Users/Coo1ng/Desktop/University.xlsx")
finali = 0
for i in range(len(df)):
    if df.iloc[i, 1] == id:
        finali = i
        break
finali = finali + 1
percent = (1 - float(finali / len(df)))
ans = int(percent * len(job))
job.sort()
#print(job)
print("the estimated salary is:")
print(job[ans])
