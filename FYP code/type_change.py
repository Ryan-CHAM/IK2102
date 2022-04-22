import os

os.remove("cluster.txt")
os.rename("clusternew.txt", "cluster.txt")