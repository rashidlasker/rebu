#!/bin/bash

docker start mysql
docker-compose build
docker-compose up
