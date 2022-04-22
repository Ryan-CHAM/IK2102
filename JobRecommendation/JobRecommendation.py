'''
This script is the main body of Job Recommendation function.
Input:
    1. Database of jobs
    2. Profile of one candidate
    3. Recommendation options
Components:
    1. Hard skill matching
    2. Soft skill matching
    3. Language matching
    4. Location matching
    5. Integration and ranking
Ouput: Job ranking
'''

import json
import math
import numpy as np
import pandas as pd

def angle(x):
    return x * math.pi / 180

# TODO: modify options below as the user wishes
HARD = True
SOFT = True
LANG = True
LOC = True

# TODO: modify weights below as the developer wishes
HARD_WEIGHT = 1
SOFT_WEIGHT = 0.25
LANG_WEIGHT = 0.5
LOC_WEIGHT = 0.25
BETA = 1  # parameter in F-beta score

# TODO: insert real data instead of demo data below
jobs = pd.read_json("support/data.json")
candidate = {'hard skills': ['python', 'linux', 'c'],
             'soft skills': ['analytical skill'],
             'languages': ['cantonese', 'english'],
             'location': 'Sha Tin'
             }

# match hard skills
hard_score = []
cs = candidate['hard skills']
for r in jobs['requirements']:
    js = r['hard_skills']
    tp = len(set(cs) & set(js))
    if tp != 0:
        precision = tp / len(set(cs))
        recall = tp / len(set(js))
        f = (1 + BETA ** 2) * precision * recall / (BETA ** 2 * precision + recall)
        hard_score.append(f)
    else: hard_score.append(0)
hard_score = np.array(hard_score)
hard_score /= max(hard_score)

# match soft skills
soft_score = []
cs = candidate['soft skills']
for r in jobs['requirements']:
    js = r['soft_skills']
    tp = len(set(cs) & set(js))
    if tp != 0:
        precision = tp / len(set(cs))
        recall = tp / len(set(js))
        f = (1 + BETA ** 2) * precision * recall / (BETA ** 2 * precision + recall)
        soft_score.append(f)
    else: soft_score.append(0)
soft_score = np.array(soft_score)
soft_score /= max(soft_score)

# match languages
f = open("support/language_info.json")
lang_info = json.load(f)
lang_map = {}
impl_map = {}
for d in lang_info:
    for a in d['aliases']: lang_map[a] = d['language']
    for i in d['implications']:
        if d['language'] in impl_map: impl_map[d['language']].append(i)
        else: impl_map[d['language']] = [i]

lang_score = []
cl = candidate['languages']
for i in range(len(cl)):
    l = cl[i]
    if l in lang_map: cl[i] = lang_map[l]
    if l in impl_map:
        for L in impl_map[l]:
            if not L in cl: cl.append(L)

for r in jobs['requirements']:
    jl = r['languages']
    tp = len(set(cl) & set(jl))
    if tp != 0:
        precision = tp / len(set(cl))
        recall = tp / len(set(jl))
        f = (1 + BETA ** 2) * precision * recall / (BETA ** 2 * precision + recall)
        lang_score.append(f)
    else: lang_score.append(0)
lang_score = np.array(lang_score)
lang_score /= max(lang_score)

# match location
f = open("support/location_info.json")
loc_info = json.load(f)
loc_map = {}
for d in loc_info:
    for l in d['locations']: loc_map[l] = d['district']
coordinate = {d['district']: d['coordinate'] for d in loc_info}
f.close()

loc_score = []
cl = candidate['location']
if not cl in coordinate:
    if cl in loc_map: cl = loc_map[cl]
    else: cl = 'Others'

if cl == 'Others': loc_score = [0 for i in range(len(jobs))]
else:
    dist_map = {}
    v1 = (math.cos(angle(coordinate[cl][0])) * math.cos(angle(coordinate[cl][1])),
          math.cos(angle(coordinate[cl][0])) * math.sin(angle(coordinate[cl][1])),
          math.sin(angle(coordinate[cl][0])))
    for k, v in coordinate.items():
        v2 = (math.cos(angle(v[0])) * math.cos(angle(v[1])),
              math.cos(angle(v[0])) * math.sin(angle(v[1])),
              math.sin(angle(v[0])))
        dist_map[k] = 1 - np.dot(v1, v2)

    for jl in jobs['locations']:
        if jl == 'Others': loc_score.append(-1)
        else: loc_score.append(dist_map[jl])
    scale = max(loc_score)
    for i in range(len(loc_score)):
        if loc_score[i] != -1: loc_score[i] = 1 - loc_score[i] / scale
        else: loc_score[i] = 0

# integrate and rank
if not HARD: HARD_WEIGHT = 0
if not SOFT: SOFT_WEIGHT = 0
if not LANG: LANG_WEIGHT = 0
if not LOC: LOC_WEIGHT = 0

intg_score = HARD_WEIGHT * hard_score +\
             SOFT_WEIGHT * soft_score +\
             LANG_WEIGHT * lang_score +\
             [LOC_WEIGHT * s for s in loc_score]
jobs['hard_skill_score'] = hard_score
jobs['soft_skill_score'] = soft_score
jobs['language_score'] = lang_score
jobs['location_score'] = loc_score
jobs['integrated_score'] = intg_score
jobs = jobs.sort_values('integrated_score', ascending=False)

# TODO: take output here
jobs.to_excel("demo_results.xlsx")