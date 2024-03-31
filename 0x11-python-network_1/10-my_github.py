#!/usr/bin/python3
"""
github API to display my ID credential
"""


import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    passwd = sys.argv[2]

    resp = requests.get(url, auth=(username, passwd))
    if resp.status_code == 200:
        user_data = resp.json()
        print("{}".format(user_data['id']))
    else:
        print("None")
