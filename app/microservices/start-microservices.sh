#!/bin/bash

python manage.py migrate
python manage.py flush --no-input
python manage.py loaddata rebu/fixtures/rebu/rebu_testdata.json 
python manage.py collectstatic --no-input --clear
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'rashidlasker@gmail.com', 'root')" | python manage.py shell
mod_wsgi-express start-server --reload-on-changes microservices/wsgi.py