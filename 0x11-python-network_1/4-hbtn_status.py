#!/usr/bin/python3
"""
A script that fetches a specific URL
"""

from urllib import request

if __name__ == "__main__":
    url_read = request.Request("https://alx-intranet.hbtn.io/status")

    with request.urlopen(url_read) as resp:
        body = resp.read()
        header_set = resp.headers.get_content_charset() or "utf-8"
        body_decoded = body.decode(header_set)
        print("Body response:")
        print("	-type: {}".format(type(body)))
        print("	-content: {}".format(body))
