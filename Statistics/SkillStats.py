import pandas as pd

job_df = pd.read_json("support/data.json")

job_id = []
hss = []
dict = {}

##############################RECORDING NEW CLUSTER OF DATABASE#######################################
for r in results:
    hs = []
    for i in r['requirements']['hard_skills']:
        hs.append(i)
    hss.append(hs)
job_df = pd.DataFrame({'hardskills': hss})
for i in range(len(job_df)):
    for key in job_df.iloc[i, 0]:
        dict[key] = dict.get(key, 0) + 1
file = open('skillnew.txt', 'w') 
for k,v in dict.items():
    file.write(str(k)+'&&&'+str(v)+'\n')
file.close()
##################################LOADING OLD CLUSTER FROM THE FILE##################################
old_dict = {}
file = open('skill.txt','r')
for line in file.readlines():
    line = line.strip()
    k = line.split('&&&')[0]
    v = line.split('&&&')[1]
    old_dict[k] = int(v)
file.close()
#####################################COMPARING TWO CLUSTER FILE#########################################
compare_dict = {}
for k,v in dict.items():
    if dict.get(k, 0) != old_dict.get(k, 0):
        compare_dict[k] = dict.get(k, 0) - old_dict.get(k, 0)
sorted_compare_dict = sorted(compare_dict.items(), key=lambda d:d[1], reverse=True)
file=open('skillcompare.txt','w')
file1 = open('skillgrowing.txt', 'w')
for line in sorted_compare_dict:
    for a in line:
        if(isinstance(a, int) == 1):
            file.write(str(a))
        if(isinstance(a, int) == 0):
            if(old_dict.get(a, 0) != 0):   
                temp = float((dict.get(a, 0) - old_dict.get(a, 0)) / (old_dict.get(a, 0)))
                temp = int(temp * 10000)
                file1.write(a)
                file1.write('&&&')
                file1.write(str(temp))
                file1.write('\n')
            file.write(a)
            file.write('&&&')
    file.write('\n')
file.close()
file1.close()

growing_dict = {}
file = open('skillgrowing.txt','r')
for line in file.readlines():
    line = line.strip()
    k = line.split('&&&')[0]
    v = line.split('&&&')[1]
    growing_dict[k] = int(v)
file.close()

sorted_growing_dict = sorted(growing_dict.items(), key=lambda d:d[1], reverse=True)
file = open('skillgrowing.txt', 'w')
for line in sorted_growing_dict:
      for a in line:
        if(isinstance(a, int) == 1):
            file.write(str(float(a/10000)))
        if(isinstance(a, int) == 0):
            file.write(a)
            file.write('&&&')
      file.write('\n')
file.close()