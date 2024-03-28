#!/usr/bin/python3
"""A script that fetches a URL(https://alx-intranet.hbtn.io/status) """

import urllib.request

client_request = urllib.request.Request('https://alx-intranet.hbtn.io/status')

with urllib.request.urlopen(client_request) as response:
    body = response.read()
    char_set = response.headers.get_content_charset() or 'utf-8'
    body_decoded = body.decode(char_set)
    print("Body response:")
    print("	- type: {}".format(type(body)))
    print("	- content: {}".format(body))
    print("	- utf8 content: {}".format(body_decoded))
