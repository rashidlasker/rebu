#!/bin/bash

python manage.py migrate
python manage.py flush --no-input -v 0
python manage.py loaddata rebu/fixtures/rebu/rebu_testdata.json 
python manage.py collectstatic --no-input --clear -v 0
mod_wsgi-express start-server --reload-on-changes microservices/wsgi.py