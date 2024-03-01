#!/bin/bash
#print allowed option 

curl -X OPTIONS -I "$1" | awk '/Allow/ {print $0}' | cut -d " " -f2-4
