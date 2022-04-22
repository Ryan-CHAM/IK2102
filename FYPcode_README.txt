1.py
To generate the "University.xlsx", which records the scores for each candidate
in the database.

2.py
By using the "Universit.xlsx", input type and input id, it generates the estimated
salary for the candidate.

cluster_skill.py
Generate three files, namely skillnew.txt, skillcompare.txt, skillgrowing.txt for
the tracking function.

cluster_skill_old.py
Old version of cluster_skill.py

cluster_type.py
Generate three files, namely typenew.txt, typecompare.txt, typegrowing.txt for
the tracking function.

company.py
Generate the hard_skills needed by the specific company, similar to cluster_skill,
but we did not run it on the website because of the lack of real data.

Dataset.csv
The standard university score file we use to generate "University.xlsx"

forecast.py
By input to list y, it generates the estimated salary in X month.
y[0] is the salary one year ago, y[1] is 6 months ago, y[2] is 3 months ago, y[3] 
is the current salary.

job_upload.py
To upload the json file to the mongoDB database we use for the code.

model_skill_v2.model
The model skill for matching the skill.

Ranking_GPA.py
To calculate the candidates' GPA and store it in a Dataframe.

Recommendation.py
The recommendation system code.

salary.py
Data gathering for the salary attributes. It outputs the average salary, high/
medium/low income job number for a specific job type.

simulation.py
The simulation for the recommendation system.

skill.txt/skillcompare.txt/skillgrowing.txt
The sample output file for the skill_cluster function.

type_change.py
It is for changing the typenew.txt to type.txt after each update.

stype_skill.py
The integrated version of cluster_skill.txt. For each job type, it stores the result
in different text file, making the results of each industry stored in different files.

University.xlsx
The sample file for the generated University.xlsx by 2.py.

upload.py
upload a single json file to the mongoDB database.

wc.py
Generate the Word Cloud for skills in the databsase.

wc_cmp.py
Generate the Word Cloud for skills that are requested by a company in the
database.