#!/bin/bash
#a that sends rquest to a URL as an argument, and displays only the status code of the response.
curl -so /dev/null -w "%{http_code}" "$1"
