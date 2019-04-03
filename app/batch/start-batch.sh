#!/bin/bash

python3 indexer.py
mod_wsgi-express start-server --reload-on-changes batch/esgi.py
