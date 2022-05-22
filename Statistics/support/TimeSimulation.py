'''
This script simulates a case where we maintain 4 time stamps, and generates 3 past datasets.
'''

import pandas as pd

# read data
jobs = pd.read_json("data.json")

# shuffle and save
jobs = jobs.sample(frac=1, random_state=64)
jobs[:12500].to_json("data'''.json", orient='records')
jobs[:15000].to_json("data''.json", orient='records')
jobs[:17500].to_json("data'.json", orient='records')