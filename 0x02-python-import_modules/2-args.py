#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argu = len(sys.argv) - 1
    if argu == 0:
        print(f"{argu} arguments.")
    elif argu == 1:
        print(f"{argu} argument:\n{1}: {sys.argv[1]}")
    else:
        print(f"{argu} arguments:")
        for i in range(1, argu + 1):
            print(f"{i}: {sys.argv[i]}")
