'''
This script recommends the most in-demand jobs to the user.
Input:
    1. Selected type
    2. Occupation-skill relation
Output: Skill ranking
'''

import pandas as pd

# TODO: modify options below to deal with different types
selected_occ = input("Please enter the type: ")

# read occupation-skill relation
skill_dict = {}
file = open("support/occ-skill_relation.txt", 'r')
for l in file.readlines():
    skill = l.split("'")[1]
    occ = l.split("'")[3]
    if selected_occ == 'all' or occ == selected_occ:
        skill_dict[skill] = skill_dict.get(skill, 0) + 1
file.close()

# take output here
skill_rank = sorted(skill_dict.items(), key=lambda x: x[1], reverse=True)
print(skill_rank)