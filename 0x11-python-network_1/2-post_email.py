#!/usr/bin/python3


import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({'email': email}).encode('utf-8')
    req = Request(url, data=data)
    with urlopen(req) as res:
        content = res.read().decode('utf-8')
        print(content)
