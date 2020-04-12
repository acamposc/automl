#!/bin/bash
#########################################################

#activate / deactivate virtual environment
#https://www.youtube.com/watch?v=Kg1Yvry_Ydk
#python3 -m venv automl/venv
#source h2oautoml/venv/bin/activate
#deactivate
# venv/ is ignored in .gitignore

# install requirements.txt
##pip install -r requirements.txt

#pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o

#run pip freeze before pushing to update requirements.txt!!!!
#pip freeze > requirements.txt

#deleting the venv:
#rm -rf h2oautoml
#removes the whole project

source env.sh
# run anywhere
PYTHONIOENCODING=utf-8 python3.8 app.py
