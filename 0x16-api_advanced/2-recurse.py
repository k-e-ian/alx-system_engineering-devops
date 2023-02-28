#!/usr/bin/python3
"""function to query a list of all hot posts on a given reddit sureddit

"""
import requests


def recurse(subreddit, hot_list=[]):
    headers = {'User-Agent': 'alice'}
    params = {'limit': 100}
    url = 'https://www.reddit.com/r/{subreddit}/hot.json'

    if hot_list is None:
        hot_list = []

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']

    if after:
        params['after'] = after
        recurse(subreddit, hot_list)

    return hot_list
