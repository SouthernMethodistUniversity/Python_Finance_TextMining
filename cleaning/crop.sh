#!/bin/bash

for file in *.txt
do 
  #head -5000 "$file" > data10k/"$file"
  echo "$file"
  wc -l "$file"
done
