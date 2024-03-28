#!/usr/bin/python3
"""
A script that sends request nd displays
value of X-Request-Id variable in header
"""


import urllib.request

from sys import argv

url = argv[1]

r = urllib.request.urlopen(url)
for header in r.getheaders():
    if header[0] == 'X-Request-Id':
        request_id = header[1]
        print(request_id)
        break
