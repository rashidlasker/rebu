#!/bin/bash

python manage.py collectstatic --no-input --clear -v 0
mod_wsgi-express start-server --reload-on-changes web/wsgi.py