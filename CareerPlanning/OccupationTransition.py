'''
This script gives possible paths from present occupation to target occupation.
Input:
    1. Present occupation
    2. Target occupation
    3. Threshold
Output: Paths
'''

import pandas as pd
import networkx as nx

# TODO: modify input instead of demo input below
source = 'software-development'
target = 'photography-video'

# TODO: modify threshold below as the developer wishes
THRESHOLD = 0.6

# read and process data
jaccard_dict = {}
file = open("support/jaccard.txt", 'r')
for l in file.readlines():
    l = l.strip()
    k = (l.split("'")[1], l.split("'")[3])
    v = float(l.split(": ")[1])
    jaccard_dict[k] = v
file.close()

G = nx.Graph()
for j in jaccard_dict.items():
    if j[1] <= THRESHOLD: G.add_edge(j[0][0], j[0][1], weight=j[1])

# TODO: take output here
print("Shortest path: %s" % nx.shortest_path(G, source, target, 'weight'))
print("Length: %s" % nx.shortest_path_length(G, source, target, 'weight'))