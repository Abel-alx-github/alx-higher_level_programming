#!/bin/bash
#post json format file
curl -s -X POST -d "$(cat "$2")" "$1"
