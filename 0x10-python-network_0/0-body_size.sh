#!/usr/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ "$#" == 0 ]; then
  echo "usage: ./0-body_size.sh ip"
  exit 1
fi

url="$1"
curl -Is "$url" | awk '/Content-Length:/ {print $2}'
