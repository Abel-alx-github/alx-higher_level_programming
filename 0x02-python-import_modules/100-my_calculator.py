#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == '__main__':
    opr = ["+", "-", "*", "/"]
    arg = sys.argv[1:]
    length = len(arg)
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in opr:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
        elif sys.argv[2] == "*":
            print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
        else:
            print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
