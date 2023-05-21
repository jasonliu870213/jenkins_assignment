#!/bin/zsh
source /Users/liuchenghsuan/PycharmProjects/Automation-Test-Program-Batch2-Project/venv/bin/activate
pip install -r requirements.txt
ls -l
echo 'gggggggggggggg'
python -m pytest --alluredir=./
