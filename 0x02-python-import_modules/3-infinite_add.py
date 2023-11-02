#!/usr/bin/python3
import sys
summ = 0
if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        summ += int(sys.argv[i])
print("{}".format(summ))
