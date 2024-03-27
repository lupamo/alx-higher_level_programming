#!/usr/bin/env bash
#a script that takes a url sends a request to that url  and displays the size of the body

#check url
if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

#Fetching URL
URL="$1"

content=$(curl -s -w "\n%{size_download}\n" "$URL")
size=${content#* }

echo "$size"
