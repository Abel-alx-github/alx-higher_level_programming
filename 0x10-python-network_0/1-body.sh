#!/bin/bash
#sends a GET request to the URL, and displays the body of the response

code=$(curl -sI "$1" | awk '/HTTP/ {print $2}')
if [[ "$code" == "200" ]]; then
  curl -s "$1" 
fi
