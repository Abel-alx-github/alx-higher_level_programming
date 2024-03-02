#!/usr/bin/python3
"""  takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally
displays the body of the response."""


if __name__ == '__main__':
    import requests
    import sys

    data = {"email": sys.argv[2]}

    respond = requests.post(sys.argv[1], json=data)
    print("Your email is:", respond.json())
