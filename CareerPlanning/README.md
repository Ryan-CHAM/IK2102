# Career Planning

#### Workflow:
1. *data.json* -> *support/Occ-SkillRelation.py* -> *support/occ-skill_relation.txt*, *support/jaccard.txt*
2. *support/occ-skill_relation.txt* -> *SkillRecommendation.py*
3. *support/jaccard.txt* -> *OccupationTransition.py*

## *SkillRecommendation.py*
### This script recommends the most in-demand jobs to the user.
#### Input:
1. Selected type
2. Occupation-skill relation
#### Output: Skill ranking

## *OccupationTransition.ipynb*
### This notebook is to display how *OccupationTransition.py* works. They are identical in function.

## *OccupationTransition.py*
### This script gives possible paths from present occupation to target occupation.
#### Input:
1. Present occupation
2. Target occupation
3. Threshold
#### Output: Paths

## *support*
### This directory includes the input and output of the scripts.