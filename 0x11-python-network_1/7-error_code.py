#!/usr/bin/python3
"""
a script that sends a requet to the URL and displays
body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)
    
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
    
	
        
        