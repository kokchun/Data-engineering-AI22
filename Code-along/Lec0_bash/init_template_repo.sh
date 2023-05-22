#!/bin/bash

echo "running initializations"
sleep 1

mkdir theory code-alongs explorations
touch theory/.gitkeep code-alongs/.gitkeep explorations/explore.txt

for i in {1..5}; do
  echo "This is file $i" > file$i.txt
done


