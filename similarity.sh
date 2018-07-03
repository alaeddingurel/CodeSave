#!/bin/bash

search_dir=$1


echo $PWD



for file1 in $search_dir/*; do
    for file2 in $search_dir/*; do
	if [ "$(basename "$file1")" != "$(basename "$file2")" ];
	then
		echo "$(basename "$file1")"
		echo "$(basename "$file2")"
		sed -i '/^$/d' $file1
		sed -i '/^$/d' $file2
		similarity=$(comm -12 <(sort $file1) <(sort $file2) | wc -l)
		len_file1=$(cat $file1 | wc -l)
		len_file2=$(cat $file2 | wc -l)
		a=$(echo "$similarity / $len_file1" | bc -l)
		echo "$similarity" 
		echo "$len_file1"
		echo "$a"
	else
		echo "They are same"
	fi
    done
	

    # while IFS='' read -r line || [[ -n "$line" ]]; do
    # echo "Text read from file: $line"
    # done < "$file1"
done





