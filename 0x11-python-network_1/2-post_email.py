#!/usr/bin/python3
"""
script that takes in a email and URl and sends a post request to the passed URL
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    email_data = urllib.parse.urlencode({'email': email})
    email_data = email_data.encode('utf-8')
    request_client = urllib.request.Request(url, data=email_data)

    with urllib.request.urlopen(request_client) as response:
        read_content = response.read()

        print(read_content.decode('utf-8'))
