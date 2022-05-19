'''
This script simulates a case where we maintain 4 time stamps, and generates 3 past records (in *records* directory).
'''

import pandas as pd

# read data
jobs = pd.read_json("support/data.json")
jobs = jobs.sample(frac=1, random_state=64)

# simulate time stamp
time = []
time.append(df[:12500])
time.append(df[:15000])
time.append(df[:17500])
time.append(df)

# generate basic statistics
for i in range(3):
    # skills
    skill_dict = {}
    for j in range(len(time[i])):
        for key in time[i]['requirements'].iloc[j]['hard_skills']: temp_dict[key] = temp_dict.get(key, 0) + 1
    file_path = "files/skill_%s_%s.txt"
    if i < 4: file_path = file_path % ('year', i)
    elif i < 8: file_path = file_path % ('month', i-4)
    else: file_path = "files/skill_now.txt"
    file = open(file_path, 'w') 
    for k, v in temp_dict.items(): file.write(str(k) + '&&&' + str(v) + '\n')
    file.close()

    # types
    temp_dict = {}
    for key in time[i]['type']: temp_dict[key] = temp_dict.get(key, 0) + 1
    file_path = "files/type_%s_%s.txt"
    if i < 4: file_path = file_path % ('year', i)
    elif i < 8: file_path = file_path % ('month', i-4)
    else: file_path = "files/type_now.txt"
    file = open(file_path, 'w') 
    for k, v in temp_dict.items(): file.write(str(k) + '&&&' + str(v) + '\n')
    file.close()