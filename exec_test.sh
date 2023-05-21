#!/bin/zsh
source /Users/liuchenghsuan/PycharmProjects/Automation-Test-Program-Batch2-Project/venv/bin/activate
export PATH="/Users/liuchenghsuan/PycharmProjects/Automation-Test-Program-Batch2-Project/venv/bin:$PATH"

ls -l
echo 'gggggggggggggg'
python -m pytest --alluredir=./
