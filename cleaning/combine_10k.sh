#!/bin/bash

# Two arguments are required:
# 1. The directory of all files to be combined
# 2. The name of the combined file

csv_directory=${1}
output=${2}
out_csv="${output}.csv"

# Combine CSV files

readarray files < <(ls ${csv_directory}/*.csv | sort)
head -1 ${files[0]} > ${out_csv}
for f in "${files[@]}"
do
tail -n +2 ${f} >> ${out_csv}
done
unset files