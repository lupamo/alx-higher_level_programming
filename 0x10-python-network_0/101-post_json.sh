#!/bin/bash
# a script that sends JSON post Request to a URL and display body of response
curl -s -X POST -H "Content-Type: application/json" -d @"${2}" "${1}"
