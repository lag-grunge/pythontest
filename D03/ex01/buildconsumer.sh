#!/bin/bash
redis-server
python3.8 -m venv $1/my_venv
source $1/my_venv/bin/activate
pip install -r $1/requirements.txt
python $3 &
python $2 -e '2222222222','3333333333' > log_file
deactivate
redis-cli shutdown
exit