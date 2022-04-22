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
start = time.time()
university_data_set = pd.read_csv("C:/Users/Coo1ng/Desktop/Dataset.csv", encoding = "ISO-8859-1")

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

client = pymongo.MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.resume
collection = db.resumes
results = collection.find()
resume_id = []
school_names = []
temparray = []
finalarray = []
length = {}
l = 0

for r in results:
    resume_id.append(r['_id'])
    school_name = []
    for i in r['education']: school_name.append(i['school'])
    school_names.append(school_name)
resume_df = pd.DataFrame({'id': resume_id, 'school_name': school_names})

for i in range (len(resume_df)):
    if resume_df.iloc[i, 1]:
        temparray = np.array(resume_df.iloc[i, 1])
        length[i] = len(temparray)
        finalarray = np.concatenate((finalarray, temparray), axis = 0)
    else: length[i] = 0

flag = 0
ttt = 0
id = []
university = []
score = []
defultscore = 30
for i in range (len(resume_df)):
    id.append(resume_df.iloc[i, 0])
    if length[i] == 0:
        university.append("NOUNIVERSITY")
        score.append(defultscore)
    else:
        for j in range (length[i]):
            for k in range (len(university_data_set)):
                if string_similar(finalarray[l], university_data_set.iloc[k, 1]) > 0.9 and flag == 0:
                    #print("The School name is " + finalarray[l] + "; The university is " + university_data_set.iloc[k, 1])
                    #print(university_data_set.iloc[k, 12])
                    #print("the candidate is NO." + str(i))
                    university.append(university_data_set.iloc[k, 1])
                    score.append(university_data_set.iloc[k, 12])
                    flag = 1
            l = l + 1
        if flag == 0:
            university.append("NOUNIVERSITY")
            ttt = ttt + 1
            score.append(defultscore)
        flag = 0

end = time.time()
finalranking_df = pd.DataFrame({'ID': id, 'School': university, 'Score': score})
print(finalranking_df.sort_values(by='Score', ascending=False))
finalfinalranking_df = finalranking_df.sort_values(by='Score', ascending=False)
finalfinalranking_df.to_excel("University.xlsx")
print(end - start)
print(len(resume_df))
print(ttt)