#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    response = requests.get(
        f'{API_URL}/todos',
        params={'_expand': 'user'}
    )

    if response.status_code == 200:
        data = response.json()
        dictionary = dict()

        for task in data:
            dictionary[task['userId']] = []

        with open('todo_all_employees.json', 'w',
                  encoding='utf-8') as file:
            for task in data:
                actual_dr = {
                        'task': task['title'],
                        'completed': task['completed'],
                        'username': task['user']['username']
                }
                dictionary[task['userId']].append(actual_dr)
            json.dump(dictionary, file, indent=4)
    else:
        print(f'Error: {response.status_code}')
