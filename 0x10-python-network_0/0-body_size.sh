#!/usr/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
url="$1"
curl -s -I "$url" | awk '/Content-Length:/ {print $2}'
