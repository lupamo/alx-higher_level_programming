#!/usr/bin/python3
"""
A script that sends request nd displays
value of X-Request-Id variable in header
"""


import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
