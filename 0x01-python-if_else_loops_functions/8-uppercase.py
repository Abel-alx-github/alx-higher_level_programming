#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord('a') <= ord(ch) <= ord('z'):
            ch = chr(ord(ch) - 32)
        print("{:s}".format(ch), end="")
    print()
