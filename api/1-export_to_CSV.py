#!/usr/bin/python3
"""Export an employee's TODO list data to a CSV file."""
import csv
import requests
import sys

if len(sys.argv) > 1:
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    username = user.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username,
                             task.get("completed"), task.get("title")])
