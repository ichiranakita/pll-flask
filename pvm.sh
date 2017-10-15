# use pip to install virtualenv
# virtualenv env
# source env/bin/activate
# deactivate
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt
