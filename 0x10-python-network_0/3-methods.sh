#!/bin/bash
#a script that takes URL and displays all HTTP methods a server will accept
 curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
