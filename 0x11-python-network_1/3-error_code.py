#!/usr/bin/python3
"""
A script that takes in a URL, sends a request and
displays the body of the response
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            body_decoded = body.decode("utf-8")
            print(body_decoded)
    except urllib.error.HTTPError as err:
        print("{}".format(err.code))
