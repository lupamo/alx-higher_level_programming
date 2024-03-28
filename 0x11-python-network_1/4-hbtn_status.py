#!/usr/bin/python3
"""
A script that fetches a specific URL
"""

import requests

if __name__ == "__main__":
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    body = resp.text
    print("Body response:")
    print("	- type: {}".format(type(body)))
    print("	- content: {}".format(body))
