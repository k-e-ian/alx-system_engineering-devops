#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    # Base case
    if not word_list:
        return

    # Initialize counts dictionary on the first call
    if counts is None:
        counts = {}

    # Query the Reddit API
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("Invalid subreddit: {}".format(subreddit))
        return

    # Parse the titles of the hot articles
    data = response.json()['data']
    for post in data['children']:
        title = post['data']['title']
        title_lower = title.lower()
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title_lower:
                # Count the word occurrence
                if word_lower in counts:
                    counts[word_lower] += title_lower.count(word_lower)
                else:
                    counts[word_lower] = title_lower.count(word_lower)

    # Recursive call with the next batch of posts
    next_page = data['after']
    if next_page:
        count_words(subreddit, word_list, next_page, counts)
    else:
        # Print the sorted count of the given keywords
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
