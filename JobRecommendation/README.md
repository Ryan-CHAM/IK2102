# Job Recommendation

#### Workflow:
1. *support/LanguageInfoGenerator.py* -> *support/language_info.json*
2. *support/LocationInfoGenerator.py* -> *support/location_info.json*
3. *support/result*, *support/same_hard_group.json*, *support/same_soft_group.json*, *support/language_info.json*, *support/location_info.json* -> *support/PreprocessingForJobRecomm.py* -> *support/data.json*
4. *support/data.json* -> *JobRecommendation.py* -> *demo_results.xlsx*

## *demo_results.xlsx*
### This excel file is the output of the **Job Recommendation** demostration.

## *JobRecommendation.ipynb*
### This notebook is to display how *JobRecommendation.py* works. They are identical in function.

## *JobRecommendation.py*
### This script is the main body of **Job Recommendation** function. 
#### Input:
1. Database of jobs
2. Profile of a candidate
3. Recommendation options
#### Components:
1. Hard skill matching
2. Soft skill matching
3. Language matching
4. Location matching
5. Integration and ranking
#### Output: Job ranking

## *support*
### This directory includes a number of scripts and files, which can be used to generate job data for demostrating the function.