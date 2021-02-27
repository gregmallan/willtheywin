#!/usr/bin/env bash

set -e

echo "Deploying willtheywin to https://grega.pythonanywhere.com/will-they-win/ ..."

cd && cd willtheywin

git fetch
git checkout main
git pull

source venv/bin/activate
python --version
pip freeze
pip install -r conf/pip/requirements.txt
deactivate

echo "Deployment complete.
You might need to reload the app at:
https://www.pythonanywhere.com/user/grega/webapps/#tab_id_grega_pythonanywhere_com
"

exit 0
