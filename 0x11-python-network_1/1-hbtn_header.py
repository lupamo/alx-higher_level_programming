#!/usr/bin/python3
"""
A script that sends request nd displays
value of X-Request-Id variable in header
"""


import urllib.request
import sys

if len(sys.argv) < 1:
    print("No Url found")
    
url = sys.argv[1]
r = urllib.request.urlopen(url)
for header in r.getheaders():
    if header[0] == 'X-Request-Id':
        request_id = header[1]
        print(request_id)
        break
