'''
This script generates *type/skill.txt* and *type/skill_compare.txt* in *support/records*.
Input:
    1. New database of jobs
    2. Selected type
    3. *type/skill'.txt*
Output:
    1. *type/skill.txt*
    2. *type/skill_compare.txt*
'''

import pandas as pd

# TODO: modify options below to deal with different types
selected_type = input("Please enter the type: ")

# TODO: insert real data instead of demo data below
jobs = pd.read_json("support/data.json")

# record new data
data = []
for i in range(len(jobs)):
    if selected_type == 'all' or jobs['tier-1_type'][i] == selected_type:  # also works for tier-2 types
        data.append(jobs['requirements'][i]['hard_skills'])

count = {}
for i in range(len(data)):
    for s in data[i]:
        count[s] = count.get(s, 0) + 1

file = open("support/records/" + selected_type + "/skill.txt", 'w') 
for k, v in count.items():
    file.write(str(k) + ': ' + str(v) + '\n')
file.close()

# load old record
old_count = {}
file = open("support/records/" + selected_type + "/skill'.txt", 'r')
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
compare_list = sorted(compare_dict.items(), key=lambda x: x[1], reverse=True)

file = open("support/records/" + selected_type + "/skill_compare.txt", 'w')
for r in compare_list:
    file.write(r[0] + ': ' + ("%.2f" % (r[1] * 100)) + '%' + '\n')
file.close()