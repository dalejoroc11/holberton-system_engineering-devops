#!/usr/bin/python3
""" REST API, give employee ID, returns
    info about his/her TODOs list progress
"""
import requests
import sys


if __name__ == '__main__':
    userid = sys.argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(userid)).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(userid)).json()

    completed = [task.get('title') for task in todos if task
                 .get('completed') is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(completed), len(todos)))
    for task in completed:
        print("\t {}".format(task))
