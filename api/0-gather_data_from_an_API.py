#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    done = [t["title"] for t in todos if t["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
