#!/bin/zsh
source /Users/liuchenghsuan/PycharmProjects/jenkins_assignment/venv/bin/activate
pip install -r requirements.txt
echo 'gggggggggggggg'
python -m pytest --alluredir=./allure-results

