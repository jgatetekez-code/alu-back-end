#!/usr/bin/python3
"""Export all employees' TODO lists to a JSON file."""

import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    users = users_response.json()

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        all_tasks[user_id] = []

        for todo in todos:
            if todo.get("userId") == user.get("id"):
                task = {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                }
                all_tasks[user_id].append(task)

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)

