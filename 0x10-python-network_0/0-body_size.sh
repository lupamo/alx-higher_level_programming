#!/bin/bash
#a script that takes a url sends a request to that url  and displays the size of the url body
curl -sI "$1" | grep "content-Length:" | cut -d " " -f 2
