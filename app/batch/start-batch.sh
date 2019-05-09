#!/bin/bash

python3 -u coview_indexer.py &
python3 -u kafka_indexer.py
