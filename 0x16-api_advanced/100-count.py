#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, after='start', words_count=None):
    """Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if not word_list:
     	return 0

    if words_count is None:
        words_count = {word.lower(): 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "DON-JOE"}
    if after != 'start':
        url += "?after={}".format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    for post in response.json().get('data').get('children'):
        title = post.get('data').get('title')
        for word in title.split():
            if word.lower() in words_count.keys():
                words_count[word.lower()] += 1

    after = response.json().get('data').get('after')
    if after:
        return count_words(subreddit, word_list, after, words_count)
    else:
        words_count = dict(sorted(words_count.items(),
                                  key=lambda x: x[1], reverse=True))
        for word, count in words_count.items():
            if count != 0:
                print(str(word) + ": " + str(count))
        return 1

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
