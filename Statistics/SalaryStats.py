'''
This script gives the statistics of salary.
Input:
    1. Database of jobs
    2. Selected type
Output:
    1. Average salary
    2. Number of jobs in each salary interval
'''

import pandas as pd

# TODO: modify options below to deal with different types
selected_type = input("Please enter the type: ")

# TODO: insert real data instead of demo data below
jobs = pd.read_json("support/data.json")
if selected_type != 'all':
    jobs = jobs.groupby('tier-1_type').get_group(selected_type)  # also works for tier-2 types

# read data
data = []
for i in range(len(jobs)):
    if jobs['salary_visible'][i]:
        data.append((jobs['salary'][i]['max'], jobs['salary'][i]['min']))

# process data
total = 0
interval = [0 for i in range(5)]
for i in range(len(data)):
    h = data[i][0]
    l = data[i][1]
    if isinstance(h, int) and isinstance(l, int) and h >= 1000 and l >= 1000:
        s = (h + l) / 2
        if s < 15000: interval[0] += 1
        elif 15000 <= s < 30000: interval[1] += 1
        elif 30000 <= s < 45000: interval[2] += 1
        elif 45000 <= s < 60000: interval[3] += 1
        else: interval[4] += 1
        total += s
    if not isinstance(h, int) and isinstance(l, int) and l >= 1000:
        if l < 15000: interval[0] += 1
        elif 15000 <= l < 30000: interval[1] += 1
        elif 30000 <= l < 45000: interval[2] += 1
        elif 45000 <= l < 60000: interval[3] += 1
        else: interval[4] += 1
        total += l
    if isinstance(h, int) and not isinstance(l, int) and h >= 1000:
        if h < 15000: interval[0] += 1
        elif 15000 <= h < 30000: interval[1] += 1
        elif 30000 <= h < 45000: interval[2] += 1
        elif 45000 <= h < 60000: interval[3] += 1
        else: interval[4] += 1
        total += h

# TODO: take output here
avg = int(total / len(data))
print(avg)
print(interval)