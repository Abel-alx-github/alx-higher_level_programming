#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_userwith the letter as a parameter."""
import requests
import sys

if __name__ == '__main__':
    try:
        data = {"q": sys.argv[1]}
    except Exception as e:
        data = {"q": ""}
    url = "http://0.0.0.0:5000/search_user"
    respond = requests.post(url, data=data)

    try:
        j_data = respond.json()
        if j_data:
            print("[{}] {}".format(j_data['id'], j_data['name']))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
