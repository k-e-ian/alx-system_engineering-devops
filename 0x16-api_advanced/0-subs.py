#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import json
import requests


#def number_of_subscribers(subreddit):
#    user = {"User-Agent": "Ahmed_belhaj"}
#    request = requests.get("https://www.reddit.com/r/{}/about.json"
#                           .format(subreddit), headers=user)
#    if request.status_code == 200:
#        return request.json().get("data").get("subscribers")
#    else:
#        return 0

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Ahmed_belhaj"#"linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
