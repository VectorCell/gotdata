#!/bin/bash

echo -e "books\ncharacters\nhouses" | while read base; do

	if [ ! -d "$base" ]; then
		mkdir "$base"
	fi

	for i in {1..5000}; do
		if [ ! -e "$base/$i.json" ]; then
			echo -e "\n$base $i"
			curl "http://anapioficeandfire.com/api/$base/$i" > "$base/$i.json"
		fi
		if [ "$?" -ne "0" ] || [ "0" == "$(ls -l $base/$i.json | awk '{print $5}')" ]; then
			echo "Stopping at $base/$i"
			rm -f "$base/$i.json"
			break
		fi
	done


done
