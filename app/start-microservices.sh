#!/bin/bash

python microservices/manage.py migrate
python microservices/manage.py flush --no-input
python microservices/manage.py loaddata microservices/rebu/fixtures/rebu/rebu_testdata.json 
mod_wsgi-express start-server --working-directory microservices/ --reload-on-changes microservices/microservices/wsgi.py