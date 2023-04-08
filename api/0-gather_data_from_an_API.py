#!/usr/bin/python3
"""
returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == '__main__':
    site_URL = 'https://jsonplaceholder.typicode.com'

    user_id = argv[1]
    response = requests.get(
        f'{site_URL}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

    if response.status_code == 200:
        data = response.json()
        name = data[0]['user']['name']
        fn_task = [task for task in data if task['completed']]
        len_task = len(fn_task)
        len_task_total = len(data)

        str_first = f'Employee {name} is done with tasks'
        print(f'{str_first}({len_task}/{len_task_total}):')
        for task in fn_task:
            print(f'\t{task["title"]}')
    else:
        print(f'Error: {response.status_code}')

