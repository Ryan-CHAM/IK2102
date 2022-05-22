'''
This script generates *occ-skill_relation.txt* and *jaccard.txt*.
'''

import pandas as pd
import networkx as nx

# TODO: insert real data instead of demo data below
jobs = pd.read_json("data.json")

# read data
occ_dict, skill_dict, pair_dict = {}, {}, {}
for i in range(len(jobs)):
    t = jobs['tier-2_type'][i]
    occ_dict[t] = occ_dict.get(t, 0) + 1
    for s in jobs['requirements'][i]['hard_skills']:
        skill_dict[s] = skill_dict.get(s, 0) + 1
        p = (s, t)
        pair_dict[p] = pair_dict.get(p, 0) + 1

# find occupation-skill relation
file = open("occ-skill_relation.txt", 'w')
for k, v in pair_dict.items():
    file.write(str(k) + ': ' + str(v) + '\n')
file.close()

G = nx.Graph()
for t in occ_dict.keys(): G.add_node(t)
for s in skill_dict.keys(): G.add_node(s)
for p in pair_dict.keys(): G.add_edge(p[0], p[1])

jaccard_dict = {}
for t1 in occ_dict.keys():
    for t2 in occ_dict.keys():
        if not (t1, t2) in jaccard_dict and not (t2, t1) in jaccard_dict and t1 != t2:
            s1 = set(G.neighbors(t1))
            s2 = set(G.neighbors(t2))
            jaccard_dict[(t1, t2)] = 1 - len(s1 & s2) / len(s1 | s2)

file = open("jaccard.txt", 'w')
for k, v in jaccard_dict.items():
    file.write(str(k) + ': ' + str(v) + '\n')
file.close()