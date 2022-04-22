from contextlib import contextmanager
import pandas as pd
from sklearn import metrics
import math
from re import S
import pymongo
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import os
import time
########################################################## PART1 #########################################################################
################################################### Embedding Dataframe ##################################################################
# visit resume database
t = time.time()
client = pymongo.MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.resume
collection = db.resumes
results = collection.find()
resume_id = []
skills = []
for r in results:
    resume_id.append(r['_id'])
    skills.append(r['hard_skill'])
resume_df = pd.DataFrame({'id': resume_id, 'skills':skills})


# visit job database

client = pymongo.MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.job
collection = db.jobs
results = collection.find()
job_id = []
titles = []
categories = []
for r in results:
    job_id.append(r['_id'])
    titles.append(r['job_title'])
    categories.append(r['categories'])
job_df = pd.DataFrame({'id': job_id, 'titles': titles, 'categories': categories})


# embedding

use = hub.load("C:/Users/Coo1ng/Downloads/universal-sentence-encoder_4")
resume_vector = []
for i in range(len(resume_df)):
    if resume_df.iloc[i, 1] != []: resume_vector.append(use(resume_df.iloc[i, 1]))
    else: resume_vector.append([])
job_vector = []
for i in range(len(job_df)):
    if job_df.iloc[i, 2] != []: job_vector.append(use(job_df.iloc[i, 2]))
    else: job_vector.append([])

# calculate similarity

resume_vs_job1 = []
for i in range(len(resume_df)):
    resume_vs_job1.append([])
    if len(resume_vector[i]) != 0:
        for j in range(len(job_df)):
            if len(job_vector[j]) != 0:
                similarity = metrics.pairwise.cosine_similarity(resume_vector[i], job_vector[j])
                total = 0
                for r in similarity: total += sum(r)
                resume_vs_job1[i].append(total / similarity.shape[0] / similarity.shape[1])
            else:
                resume_vs_job1[i].append(None)
resume_vs_job1 = pd.DataFrame(resume_vs_job1)
print(resume_vs_job1)

client = pymongo.MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.resume
collection = db.resumes
results = collection.find()
resume_id = []
positions = []
for r in results:
    resume_id.append(r['_id'])
    position = []
    for i in r['working_experience']: position.append(i['position'])
    positions.append(position)
resume_df = pd.DataFrame({'id': resume_id, 'positions': positions})


client = pymongo.MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.job
collection = db.jobs
results = collection.find()
job_id = []
titles = []
for r in results:
    job_id.append(r['_id'])
    titles.append(r['job_title'])
job_df = pd.DataFrame({'id': job_id, 'title': titles})


se = hub.load("C:/Users/Coo1ng/Downloads/universal-sentence-encoder_4")
resume_vector = []
for i in range(len(resume_df)):
    if resume_df.iloc[i, 1] != []: resume_vector.append(use(resume_df.iloc[i, 1]))
    else: resume_vector.append([])
job_vector = use(job_df['title'])

resume_vs_job2 = []
for i in range(len(resume_df)):
    resume_vs_job2.append([])
    if len(resume_vector[i]) != 0:
        similarity = metrics.pairwise.cosine_similarity(job_vector, resume_vector[i])
        for j in range(len(similarity)): resume_vs_job2[i].append(sum(similarity[j]) / similarity.shape[1])
    else: resume_vs_job2[i].append(None)
resume_vs_job2 = pd.DataFrame(resume_vs_job2)
print(resume_vs_job2)

test1 = resume_vs_job1.isnull()
test2 = resume_vs_job2.isnull()
resume_vs_job_all = []
resume_vs_job_all=resume_vs_job1.add(resume_vs_job2,fill_value=0)
print("This is the overall dataframe:")
print(resume_vs_job_all)

print(f'Time Cost:{time.time() - t:.4f}s')
t1 = time.time()

########################################################## PART2 #########################################################################
###################################################### Personal Score ####################################################################

file_object = open('C:/Users/Coo1ng/Desktop/Update.txt')
try:
	content = file_object.read()
finally:
    file_object.close()

for i in range (len(resume_df)):
    if str(resume_df.iloc[i, 0]) == content:
        if not math.isnan(resume_vs_job_all.idxmax()[i]):
            print("Candidate's id is %s, No. %s" %(content,i))
            if str(job_df.iloc[int(resume_vs_job_all.T.idxmax()[i]), 1]):
                print("  the title of top matching job is: %s" % job_df.iloc[int(resume_vs_job_all.T.idxmax()[i]), 1])
            else: print(" There is currently no suitable job for you")
            print("  with score: %s\n" % resume_vs_job_all.iloc[i, int(resume_vs_job_all.T.idxmax()[i])])
            with open("C:/Users/Coo1ng/Desktop/Result.txt","w") as f:
                f.write("Candidate's id is %s, No. %s \n" %(content,i))
                f.write(" the title of top matching job is: %s\n" % job_df.iloc[int(resume_vs_job_all.T.idxmax()[i]), 1])
                f.write(" with score: %s\n" % resume_vs_job_all.iloc[i, int(resume_vs_job_all.T.idxmax()[i])])

print(f'Time Cost:{time.time() - t1:.4f}s')