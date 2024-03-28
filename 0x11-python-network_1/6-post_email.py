#!/usr/bin/python3
"""
a script to send a POST req a email pased as parameter
"""
import requests
import sys

if __name__ == "__main__":
    resp = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(resp.text)
