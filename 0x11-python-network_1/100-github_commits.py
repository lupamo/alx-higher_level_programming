#!/usr/bin/python3
"""
a script that list 10 commits from
github starting with the latest one and
Prints all commits by: `<sha>: <author name>` (one by line)
"""


import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = (
        f'https://api.github.com/repos/{owner}/{repo_name}/commits'
        '?per_page=10'
    )

    resp = requests.get(url)

    if resp.status_code == 200:
        commits = resp.json()
        for commit in commits:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    else:
        print("Failed to get commits, status code:", resp.status_code)
