#!/usr/bin/python3
"""Export employee TODO list data to a CSV file."""

import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    user = requests.get(user_url).json()

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(
        todos_url, params={"userId": employee_id}
    ).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                user.get("username"),
                task.get("completed"),
                task.get("title")
            ])
