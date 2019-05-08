#!/bin/bash

docker start mysql
docker-compose build
docker-compose up
sleep 20
./start_spark.sh
