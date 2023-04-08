#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    user_id = argv[1]
    response = requests.get(
        f'{API_URL}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

    if response.status_code == 200:
        data = response.json()
        EMPLOYEE_NAME = data[0]['user']['name']
        fn_task = [task for task in data if task['completed']]
        NUMBER_OF_DONE_TASKS = len(fn_task)
        TOTAL_NUMBER_OF_TASKS = len(data)

        str_first = f'Employee {EMPLOYEE_NAME} is done with tasks'
        print(f'{str_first}({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
        for task in fn_task:
            print(f'\t{task["title"]}')
    else:
        print(f'Error: {response.status_code}')
