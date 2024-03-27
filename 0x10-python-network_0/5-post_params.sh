#!/bin/bash
# a script that sends POST request to a URL and display body of the response
curl -s -X POST -d "email":"test@gmail.com&subject=I will always be here for PLD" "$1"
