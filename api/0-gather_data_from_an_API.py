#!/usr/bin/python3
"""
returns information about his/her TODO list progress
"""
from sys import argv
import requests

if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com'

    id = argv[1]
    rp = \
        requests.get(
            f'{URL}/users/{id}/todos',
            params={'_expand': 'user'}
        )
 
if rp.status_code == 200:
    data = rp.json()
    data_name = data[0]['user']['name']
    fn_task = [task for task in data if task['completed']]
    len_task = len(fn_task)
    len_data = len(data)

    first = f'Employee {data_name} is done with tasks'
    print('{}({}/{}):'.format(first, len_task, len_data))
    for task in fn_task:
        print(f'\t{task["title"]}')
else:
    print('Error: {}'.format(rp.status_code))
