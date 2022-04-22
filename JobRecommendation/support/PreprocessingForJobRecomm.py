'''
This python code reads data from results directory and writes data.json
    1. Append types as attributes of jobs
    2. Merge synonymous hard skills according to same_hard_group.json
    3. Merge synonymous soft skills according to same_soft_group.json
    4. Modify languages according to std_language.json
    5. Modify locations according to std_location.json
'''

import os
import json
import pandas as pd

# read raw data from results directory
df = pd.DataFrame()
t1_type, t2_type = [], []
for d in os.listdir("results"):
    if d != ".DS_Store":
        count = 0
        for f in os.listdir("results/" + d):
            if f != ".DS_Store":
                temp_df = pd.read_json("results/" + d + "/" + f)
                df = pd.concat((df, temp_df), ignore_index=True)
                count += len(temp_df)
                t2_type += [f[:-5] for i in range(len(temp_df))]
        t1_type += [d for i in range(count)]
df['tier-1_type'] = t1_type
df['tier-2_type'] = t2_type

# import hard skill map
f = open("same_hard_group.json")
hard_group = json.load(f)
hard_map = {}
for k, v in hard_group.items():
    for s in v: hard_map[s] = k

# import soft skill map
f = open("same_soft_group.json")
soft_group = json.load(f)
soft_map = {}
for k, v in soft_group.items():
    for s in v: soft_map[s] = k

# import language info
f = open("language_info.json")
lang_info = json.load(f)
lang_map = {}
impl_map = {}
for d in lang_info:
    for a in d['aliases']: lang_map[a] = d['language']
    for i in d['implications']:
        if d['language'] in impl_map: impl_map[d['language']].append(i)
        else: impl_map[d['language']] = [i]

# import location map
f = open("location_info.json")
loc_info = json.load(f)
loc_map = {}
for d in loc_info:
    for l in d['locations']: loc_map[l] = d['district']
f.close()

# process and output data
for i in range(len(df)):
    for j in range(len(df['requirements'][i]['hard_skills'])):
        s = df['requirements'][i]['hard_skills'][j]
        if s in hard_map: df.at[i, 'requirements']['hard_skills'][j] = hard_map[s]
    for j in range(len(df['requirements'][i]['soft_skills'])):
        s = df['requirements'][i]['soft_skills'][j]
        if s in soft_map: df.at[i, 'requirements']['soft_skills'][j] = soft_map[s]
    for j in range(len(df['requirements'][i]['languages'])):
        l = df['requirements'][i]['languages'][j]
        if l in lang_map: df.at[i, 'requirements']['languages'][j] = lang_map[l]
        if l in impl_map:
            for L in impl_map[l]:
                if not L in df['requirements'][i]['languages']: df.at[i, 'requirements']['languages'].append(L)
    l = df['locations'][i][0]
    if l in loc_map: df.at[i, 'locations'] = loc_map[l]
    else: df.at[i, 'locations'] = 'Others'
df.to_json("data.json", orient='records')
