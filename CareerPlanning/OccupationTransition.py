'''
This script gives possible paths from present occupation to target occupation.
Input:
    1. Database of jobs
    2. Present occupation
    3. Target occupation
Output: Paths
'''

import pandas as pd
import networkx as nx

# TODO: modify input instead of demo input below
source = 'software-development'
target = 'photography-video'

# TODO: insert real data instead of demo data below
jobs = pd.read_json("support/data.json")

# read data
type_vocab, skill_vocab, pair_vocab = {}, {}, {}
for i in range(len(jobs)):
    t = jobs['tier-2_type'][i]
    type_vocab[t] = type_vocab.get(t, 0) + 1
    for s in jobs['requirements'][i]['hard_skills']:
        skill_vocab[s] = skill_vocab.get(s, 0) + 1
        p = (s, t)
        pair_vocab[p] = pair_vocab.get(p, 0) + 1

# build occupation-skill graph
G1 = nx.Graph()
for t in type_vocab.keys(): G1.add_node(t)
for s in skill_vocab.keys(): G1.add_node(s)
for p in pair_vocab.keys(): G1.add_edge(p[0], p[1])

# calculate jaccard distance
jaccard_dict = {}
for t1 in type_vocab.keys():
    for t2 in type_vocab.keys():
        if not (t1, t2) in jaccard_dict and not (t2, t1) in jaccard_dict and t1 != t2:
            s1 = set(G1.neighbors(t1))
            s2 = set(G1.neighbors(t2))
            jaccard_dict[(t1, t2)] = 1 - len(s1 & s2) / len(s1 | s2)

# build job transition graph
G2 = nx.Graph()
for t in type_vocab.keys(): G2.add_node(t)
for j in jaccard_dict.items():
    if j[1] <= 0.6: G2.add_edge(j[0][0], j[0][1], weight=j[1])

# TODO: take output here
print("Shortest path: %s" % nx.shortest_path(G2, source, target, 'weight'))
print("Length: %s" % nx.shortest_path_length(G2, source, target, 'weight'))