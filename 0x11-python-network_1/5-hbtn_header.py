#!/usr/bin/python3
"""
A script that takes in a URL and display value of
variable X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    print(resp.headers.get("X-Request-Id"))
