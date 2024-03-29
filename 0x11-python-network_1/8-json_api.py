#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST
request to a url
"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    v = {"q": q}

    try:
        resp = requests.post(url, data=v)
        data = resp.json()

        if data:
            print("[{}] {}".format(data.get(id), data.get('name')))
        else:
            print("No result")
    except (ValueError) as ecrr:
        print("Not a valid JSON")
