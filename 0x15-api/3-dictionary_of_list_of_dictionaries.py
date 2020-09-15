#!/usr/bin/python3
""" REST API, returns info
    about TODOs list progress of all employees
"""
import json
import requests


if __name__ == '__main__':
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    tasks = {'{}'.format(user.get('id')):
             [{'username': user.get('username'),
               'task': (task.get('title')),
               'completed': task.get('completed')}
              for task in todos if task.get('userId') == user.get('id')]
             for user in users}
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(tasks, jsonfile)
