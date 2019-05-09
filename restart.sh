#!/bin/bash

docker-compose down
docker-compose build
./start.sh
