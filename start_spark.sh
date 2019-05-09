#!/bin/bash

trap printout SIGINT
printout() {
  echo "Stopping spark"
  exit
}

sleep 30
while true; do
  ./app/spark/spark.sh
  sleep 120
done
