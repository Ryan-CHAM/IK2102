'''
This script generates *skill.txt* and *skill_compare.txt* in *support/records/*.
Input:
    1. New database of jobs
    2. *skill'.txt*
Output:
    1. *skill.txt*
    2. *skill_compare.txt*
'''

import pandas as pd

# TODO: insert real data instead of demo data below
jobs = pd.read_json("support/data.json")

# record new data
data = []
for i in range(len(jobs)):
    data.append(jobs['requirements'][i]['hard_skills'])

count = {}
for i in range(len(data)):
    for s in data[i]:
        count[s] = count.get(s, 0) + 1

file = open("support/records/skill.txt", 'w')
for k, v in count.items():
    file.write(str(k) + ': ' + str(v) + '\n')
file.close()

# load old record
old_count = {}
file = open("support/records/skill'.txt", 'r')
for l in file.readlines():
    l = l.strip()
    k = l.split(': ')[0]
    v = l.split(': ')[1]
    old_count[k] = int(v)
file.close()

# compare two records
compare_dict = {}
for k, v in count.items():
    if k in old_count and count[k] != old_count[k]:
        compare_dict[k] = (count[k] - old_count[k]) / old_count[k]
compare_rank = sorted(compare_dict.items(), key=lambda x: x[1], reverse=True)

file = open("support/records/skill_compare.txt", 'w')
for r in compare_rank:
    file.write(r[0] + ': ' + ("%.2f" % (r[1] * 100)) + '%' + '\n')
file.close()