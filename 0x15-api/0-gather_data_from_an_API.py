#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = int(argv[1])
    user_response = get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    todo_response = get('https://jsonplaceholder.typicode.com/todos')

    user = user_response.json()
    todos = todo_response.json()

    employee_name = user.get('name')
    total_tasks = len([todo for todo in todos if todo.get('userId') == user_id])
    completed_tasks = len([todo for todo in todos if todo.get('userId') == user_id and todo.get('completed')])
    tasks_titles = [todo.get('title') for todo in todos if todo.get('userId') == user_id and todo.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for title in tasks_titles:
        print("\t {}".format(title))
