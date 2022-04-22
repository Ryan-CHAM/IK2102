import pymongo
import pandas as pd
import tensorflow as tf
from sklearn import metrics
import tensorflow_hub as hub
from scipy.stats import pearsonr
import math
import node2vec
import networkx as nx
import numpy as np

client = pymongo.MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')

results = client.job.jobs.find()
job_title, job_skills = [], []
job_vocab = {}
for r in results:
    if len(r['requirements']['hard_skills']) != 0:
        job_title.append(r['job_title'])
        job_skills.append(r['requirements']['hard_skills'])
        for s in r['requirements']['hard_skills']:
            if not s in job_vocab: job_vocab[s] = 1
            else: job_vocab[s] += 1
#print("Number of jobs: %s" % len(job_title))
#rint("Number of skills: %s" % len(job_vocab))
#print(sorted(job_vocab.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))
job_df = pd.DataFrame({"title": job_title, "skills": job_skills})

results = client.resume.resumes.find()
candidate_name, candidate_skills = [], []
candidate_vocab = {}
for r in results:
    if len(r['skill']) != 0:
        candidate_name.append(r['profile']['name'])
        candidate_skills.append(r['skill'])
        for s in r['skill']:
            if not s in candidate_vocab: candidate_vocab[s] = 1
            else: candidate_vocab[s] += 1
#print("Number of candidates: %s" % len(candidate_name))
#print("Number of skills: %s" % len(candidate_vocab))
#print(sorted(candidate_vocab.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))
candidate_df = pd.DataFrame({"name": candidate_name, "skills": candidate_skills})

CANDIDATE_NUM = 0
#############################################################1############################################################################
score_matrix_1 = []
for i in range(len(job_df)):
    row = []
    for j in range(len(candidate_df)):
        tp = len(set(job_df['skills'][i]) & set(candidate_df['skills'][j]))
        row.append(tp / len(set(candidate_df['skills'][j])))
    score_matrix_1.append(row)
score_matrix_1 = np.array(score_matrix_1)
#print("Candidate name: %s; skills: %s" % (candidate_df['name'][CANDIDATE_NUM],
                                          #candidate_df['skills'][CANDIDATE_NUM]))
rank = pd.DataFrame(score_matrix_1[:, CANDIDATE_NUM])
rank.insert(1, 1, [job_df['title'][i] for i in range(len(rank))])
rank.insert(2, 2, [job_df['skills'][i] for i in range(len(rank))])
rank = rank.sort_values(0, ascending=False)
rank.columns = ['recall', 'title', 'skills']
rank.to_excel("C:/Users/Coo1ng/Desktop/ranking_1.xlsx")
#############################################################2############################################################################
score_matrix_2 = []
for i in range(len(job_df)):
    row = []
    for j in range(len(candidate_df)):
        tp = len(set(job_df['skills'][i]) & set(candidate_df['skills'][j]))
        if tp != 0:
            precision = tp / len(set(job_df['skills'][i]))
            recall = tp / len(set(candidate_df['skills'][j]))
            row.append(2 * precision * recall / (precision + recall))
        else: row.append(0)
    score_matrix_2.append(row)
score_matrix_2 = np.array(score_matrix_2)
#print("Candidate name: %s, skills: %s" % (candidate_df['name'][CANDIDATE_NUM],
                                          #candidate_df['skills'][CANDIDATE_NUM]))
rank = pd.DataFrame(score_matrix_2[:, CANDIDATE_NUM])
rank.insert(1, 1, [job_df['title'][i] for i in range(len(rank))])
rank.insert(2, 2, [job_df['skills'][i] for i in range(len(rank))])
rank = rank.sort_values(0, ascending=False)
rank.columns = ['f1 score', 'title', 'skills']
rank.to_excel("C:/Users/Coo1ng/Desktop/ranking_2.xlsx")
#############################################################3############################################################################
score_matrix_3 = []
for i in range(len(job_df)):
    row = []
    for j in range(len(candidate_df)):
        d = {candidate_df['skills'][j][k]: 1 / math.log(k + 2, 2) for k in range(len(candidate_df['skills'][j]))}
        dcg = 0
        for s in set(job_df['skills'][i]) & set(candidate_df['skills'][j]): dcg += d[s]
        row.append(dcg / sum(d.values()))
    score_matrix_3.append(row)
score_matrix_3 = np.array(score_matrix_3)

#print("Candidate name: %s, skills: %s" % (candidate_df['name'][CANDIDATE_NUM],
                                          #candidate_df['skills'][CANDIDATE_NUM]))
rank = pd.DataFrame(score_matrix_3[:, CANDIDATE_NUM])
rank.insert(1, 1, [job_df['title'][i] for i in range(len(rank))])
rank.insert(2, 2, [job_df['skills'][i] for i in range(len(rank))])
rank = rank.sort_values(0, ascending=False)
rank.columns = ['ndcg', 'title', 'skills']
rank.to_excel("C:/Users/Coo1ng/Desktop/ranking_3.xlsx")
#############################################################4############################################################################
use_model = hub.load("C:/Users/Coo1ng/Downloads/universal-sentence-encoder_4")
job_vector, candidate_vector = [], []
for i in range(len(job_df)): job_vector.append(sum(use_model(job_df['skills'][i])))
for i in range(len(candidate_df)): candidate_vector.append(sum(use_model(candidate_df['skills'][i])))
score_matrix_4 = metrics.pairwise.cosine_similarity(job_vector, candidate_vector)

#print("Candidate name: %s, skills: %s" % (candidate_df['name'][CANDIDATE_NUM],
                                          #candidate_df['skills'][CANDIDATE_NUM]))
rank = pd.DataFrame(score_matrix_4[:, CANDIDATE_NUM])
rank.insert(1, 1, [job_df['title'][i] for i in range(len(rank))])
rank.insert(2, 2, [job_df['skills'][i] for i in range(len(rank))])
rank.insert(3, 3, score_matrix_2[:, CANDIDATE_NUM])
rank.insert(4, 4, score_matrix_3[:, CANDIDATE_NUM])
rank = rank.sort_values(0, ascending=False)
rank.columns = ['pre-trained embedding', 'title', 'skills', 'f1 score', 'ndcg']
rank.to_excel("C:/Users/Coo1ng/Desktop/ranking_4.xlsx")
#############################################################5############################################################################
results = client.job.jobs.find()
G = nx.Graph()
for r in results:
    if len(r['requirements']['hard_skills']) != 0:
        for s in r['requirements']['hard_skills']: G.add_edge(r['job_title'], s)
#print("Number of nodes: %s" % len(G.nodes))
#print("Number of edges: %s" % len(G.edges))
n2v_model = node2vec.Node2Vec(G, workers=4).fit()
job_vector, candidate_vector = [], []
for i in range(len(job_df)): job_vector.append(sum([n2v_model.wv[s] for s in job_df['skills'][i]]))
for i in range(len(candidate_df)):
    vector = np.zeros(128)
    for s in candidate_df['skills'][i]:
        if s in n2v_model.wv: vector += n2v_model.wv[s]
    candidate_vector.append(vector)
similar_matrix_5 = metrics.pairwise.cosine_similarity(job_vector, candidate_vector)

#print("Candidate name: %s, skills: %s" % (candidate_df['name'][CANDIDATE_NUM],
                                          #candidate_df['skills'][CANDIDATE_NUM]))
rank = pd.DataFrame(similar_matrix_5[:, CANDIDATE_NUM])
rank.insert(1, 1, [job_df['title'][i] for i in range(len(rank))])
rank.insert(2, 2, [job_df['skills'][i] for i in range(len(rank))])
rank.insert(3, 3, score_matrix_2[:, CANDIDATE_NUM])
rank.insert(4, 4, score_matrix_3[:, CANDIDATE_NUM])
rank = rank.sort_values(0, ascending=False)
rank.columns = ['node representation', 'title', 'skills', 'f1 score', 'ndcg']
rank_1 = rank.max('node representation')
rank_2 = rank.max('f1 score')
rank_3 = rank.max('ndcg')
rank['node representation'] = rank['node representation'].div(rank_1).round(2)
rank['f1 score'] = rank['f1 score'].div(rank_1).round(2)
rank['ndcg'] = rank['ndcg'].div(rank_1).round(2)
rank['sum'] = rank.sum(axis=1)
rank['sum'] = rank['sum'].div(3).round(2)
print(rank)
rank.to_excel("C:/Users/Coo1ng/Desktop/ranking_5.xlsx")