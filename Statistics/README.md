# Statistics

#### Workflow:
1. *support/data.json* -> *support/TimeSimulation.py* -> *support/data'.json*, *support/data''.json*, *support/data'''.json*
2. *support/data.json*, *support/data'.json*, *support/data''.json*, *support/data'''.json* -> *SkillStats.py*, *TypeStats.py*, *SkillInTypeStats.py* -> *support/records*
3. *support/data.json* -> *SalaryStats.py*
4. *support/data.json*, *Hong_Kong_18_Districts.geojson* -> *LocationStats.py*
3. *support/records* -> *Forecasting.py*

## *Forecasting.py*
### This script gives forecast based on former records.
#### Input:
1. Former time stamps and corresponding values
2. Wanted time stamp
#### Output: Forecasted value corresponding to wanted time stamp

## *LocationStats.ipynb*
### This notebook is **only for reference**. The function has been implemented by IK2103 on the website.

## *SalaryStats.ipynb*
### This notebook is to display how *SalaryStats.py* works. They are identical in function.

## *SalaryStats.py*
### This script gives the statistics of salary.
#### Input:
1. Database of jobs
2. Selected type
#### Output:
1. Average salary
2. Number of jobs in each salary interval

## *SkillInTypeStats.py*
### This script generates *type/skill.txt* and *type/skill_compare.txt* in *support/records*.
#### Input:
1. New database of jobs
2. Selected type
3. *type/skill'.txt*
#### Output:
1. *type/skill.txt*
2. *type/skill_compare.txt*

## *SkillStats.ipynb*
### This notebook is to display how *SkillStats.py* works. They are identical in function.

## *SkillStats.py*
### This script generates *skill_update.txt* and *skill_compare.txt* in *support/records*.
#### Input:
1. New database of jobs
2. *skill'.txt*
#### Output:
1. *skill.txt*
2. *skill_compare.txt*

## *support*
### This directory includes the input and output of the scripts.

## *TimeStampUpdate.py*
### This script changes the time stamps of output files before tracking.

## *TypeStats.py*
### This script generates *type.txt* and *type_compare.txt* in *support/records*.
#### Input:
1. New database of jobs
2. *type'.txt*
#### Output:
1. *type.txt*
2. *type_compare.txt*

## *WordCloud.py*
### This script is **only for reference**. The function has been implemented by IK2103 on the website.