import pymongo
import wordcloud
import pandas as pd
import matplotlib.pyplot as plt

client = pymongo.MongoClient('mongodb+srv://Yuzhen:1155124469@cluster0.xzpuo.mongodb.net/test')
db = client.job
collection = db.jobs
results = collection.find()
job_id = []
hss = []
dict = {}

for r in results:
    hs = []
    for i in r['requirements']['hard_skills']:
        hs.append(i)
    hss.append(hs)
job_df = pd.DataFrame({'hardskills': hss})
file = open('test.txt', 'w') 
for i in range(len(job_df)):
    for key in job_df.iloc[i, 0]:
        file.write(key + ' ')
file.close()
text = open('test.txt','r').read()
w = wordcloud.WordCloud(font_path="msyh.ttc",
      width=1000, height=800, background_color="white",
      )
w.generate(text)
w.to_file("word_cloud.png")