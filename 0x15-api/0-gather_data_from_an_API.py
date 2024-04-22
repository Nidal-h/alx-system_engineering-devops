#!/usr/bin/python3
import json
import requests
import sys


USER_BASE_URL = "https://jsonplaceholder.typicode.com/users/"
TODOS_BASE_URL = "https://jsonplaceholder.typicode.com/todos?userId="

def get_todos(employee_id):
    # get users infos
    response = requests.get(USER_BASE_URL + str(employee_id))
    user = json.loads(response.content)
    user_name = user['name']

    # get user's todos
    response = requests.get(TODOS_BASE_URL + str(employee_id))
    todos = json.loads(response.content)

    number_of_done_tasks = 0
    number_of_tasks = len(todos)
    done_tasks_titles = []
    for todo in todos:
        if todo['completed']:
            number_of_done_tasks+=1
            done_tasks_titles.append(todo['title'])
    
    print('Employee %s is done with tasks(%d/%d):' %(user_name,number_of_done_tasks, number_of_tasks))
    for title in done_tasks_titles:
        print('\t', title)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_todos(employee_id)
