#!/usr/bin/python3
""" Recurse() method """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Write a recursive function that queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit. """
    hotp = requests.get('https://www.reddit.com/r/{}/hot.json'
                        .format(subreddit),
                        headers={"User-Agent": "Simon & Lennox"},
                        allow_redirects=False,
                        params={'after': after})
    if hotp.status_code != 200:
        return(None)
    else:
        hotp = hotp.json()
        for post in hotp['data']['children']:
            hot_list.append(post['data']['title'])
        if hotp['data']['after'] is None:
            return hot_list
        else:
            recurse(subreddit, hot_list, hotp['data']['after'])
    return hot_list
