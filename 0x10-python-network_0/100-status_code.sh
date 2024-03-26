#!/bin/bash
# print only response_code
curl -s -w "%{response_code}" -o /dev/null "$1"
