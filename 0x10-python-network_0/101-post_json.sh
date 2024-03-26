#!/bin/bash
#post json format file
curl -s -H "Content-Type: application/json" -X POST -d "$(cat "$2")" "$1"
