#!/bin/zsh
cd /Users/liuchenghsuan/PycharmProjects/Automation-Test-Program-Batch2-Project
source venv/bin/activate
ls -l
python -m pytest --alluredir=./
