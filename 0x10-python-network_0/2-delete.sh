#!/bin/bash
#a script that sends delete request to a URL passed as the first argument
curl -sX DELETE "$1"
