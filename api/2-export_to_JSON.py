
#!/usr/bin/python3
"""Export employee TODO list data to a JSON file."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Get employee information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    user = requests.get(user_url).json()

    # Get all employee tasks
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(
        todos_url, params={"userId": employee_id}
    ).json()

    # Prepare tasks for JSON export
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    # Export tasks to JSON file
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile)


