#!/usr/bin/python3
"""
returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com'

    user_id = argv[1]
    rp = requests.get(
        f'{URL}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

    if rp.status_code == 200:
        data = rp.json()
        name = data[0]['user']['name']
        fn_task = [task for task in data if task['completed']]
        len_task = len(fn_task)
        len_data = len(data)

        first = f'Employee {name} is done with tasks'
        print(f'{first}({len_task}/{len_data}):')
        for task in fn_task:
            print(f'\t{task["title"]}')
    else:
        print(f'Error: {rp.status_code}')
