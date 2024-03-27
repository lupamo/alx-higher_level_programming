#!/bin/bash
#a script that takes URL as an argumenent and displays the body response with a custom headeer
curl -s --header "X-School-User-id: 98" "$1"
