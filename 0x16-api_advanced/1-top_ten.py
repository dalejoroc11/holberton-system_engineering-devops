#!/usr/bin/python3
""" Top_ten() method """
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed for a given
    subreddit """
    hotp = requests.get('https://www.reddit.com/r/{}/hot.json'
                        .format(subreddit),
                        headers={"User-Agent": "Simon & Lennox"},
                        allow_redirects=False,
                        params={'limit': 10})
    if hotp.status_code != 200:
        print(None)
    else:
        hotp = hotp.json()
        for post in hotp['data']['children']:
            print(post['data']['title'])
