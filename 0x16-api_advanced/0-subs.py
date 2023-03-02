#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import json
import requests

#def number_of_subscribers(subreddit):
 #   """Return the total number of subscribers on a given subreddit."""
    #url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    #headers = {
    #    "User-Agent": "Ahmed_belhaj"#"linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    #}
   # response = requests.get(url, headers=headers, allow_redirects=False)
   # if response.status_code == 404:
  #      return 0
 #   results = response.json().get("data")
#    return results.get("subscribers")

def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)'}

    response = requests.get(url, headers=headers).json()
    subscribers = response.get("data", {}).get("subscribers", 0)
    return subscribers
