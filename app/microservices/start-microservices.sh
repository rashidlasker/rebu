#!/bin/bash
ls
python manage.py migrate
python manage.py flush --no-input
python manage.py loaddata rebu/fixtures/rebu/rebu_testdata.json 
mod_wsgi-express start-server --reload-on-changes microservices/wsgi.py